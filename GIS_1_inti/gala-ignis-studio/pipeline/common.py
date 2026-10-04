"""Jalur, setelan, dan data bersama."""
import json, os, re, sys, time
from functools import lru_cache
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
CFG = yaml.safe_load(open(ROOT / "config.yaml", encoding="utf-8"))
if (ROOT / ".env").exists():
    for line in open(ROOT / ".env", encoding="utf-8"):
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.strip().split("=", 1); os.environ.setdefault(k, v)


def mock():
    return os.environ.get("GALA_MOCK") == "1"


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


@lru_cache(None)
def episodes():
    return {e["n"]: e for e in json.load(open(ROOT / "data/episodes.json", encoding="utf-8"))}


def load_refs():
    return json.load(open(ROOT / "data/refs.json", encoding="utf-8"))


def save_refs(r):
    json.dump(r, open(ROOT / "data/refs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def ep_dir(n):
    d = OUT / f"ep{n:03d}"
    for s in ("panel", "audio", "slide"):
        (d / s).mkdir(parents=True, exist_ok=True)
    return d


def parse_eps(s):
    out = []
    for part in str(s).split(","):
        if "-" in part:
            a, b = part.split("-"); out += range(int(a), int(b) + 1)
        elif part.strip():
            out.append(int(part))
    bad = [n for n in out if n not in episodes()]
    if bad:
        sys.exit(f"Episode tidak dikenal: {bad}")
    return out


def read_json(p, default=None):
    p = Path(p)
    return json.load(open(p, encoding="utf-8")) if p.exists() else default


def write_json(p, obj):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    tmp = str(p) + ".tmp"
    json.dump(obj, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(tmp, p)


def frames_final(n):
    """Daftar frame per sub-episode, termasuk frame 'ketukan gagal' dari naskah bila ada."""
    ep = episodes()[n]
    script = read_json(ep_dir(n) / "naskah.json", {})
    g = ep["gagal"]; extra = script.get("gagal") if g["status"] == "tambah" else None
    subs = []
    for sub in ep["subs"]:
        fl = []
        for f in sub["frames"]:
            if extra and f["kode"] == g["sebelum"]:
                x = dict(f)
                x["kode"] = f"{sub['id']}.g"; x["shot"] = extra.get("shot") or "Medium Shot"
                x["scene"] = extra["scene_en"]; x["id"] = g["ketukan"]; x["tambahan"] = True
                x["prompt"] = re.sub(r"Scene: .*? Rendering style:", lambda m: "Scene: " + extra["scene_en"] + " Rendering style:", f["prompt"], flags=re.S)
                fl.append(x)
            fl.append(f)
        subs.append({"id": sub["id"], "judul": sub["judul"], "frames": fl})
    return subs


def usage(kind, n=1):
    p = OUT / "pemakaian.json"; u = read_json(p, {})
    u[kind] = u.get(kind, 0) + n; write_json(p, u)
