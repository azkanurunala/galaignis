"""Ekspor bible ke data/episodes.json dan data/refs.json. Jalankan dari folder bible/: python export_data.py"""
import json, os, re, glob
import render as R
import antislop_lib as AS
from antislop_data import GAGASAN
from antislop_gagal import GAGAL, PEMBUKA2
from catalog import LOCS, SECONDARY, secondary_for, location_for
import refs as RF  # juga menulis ulang docs/referensi-*.md

ROOT = os.path.abspath("..")
episodes = []
v2 = False
for S in RF.SEASONS:
    for A in S["arcs"]:
        for E in A["eps"]:
            a = AS.audit(E); eth = AS.eth_patch(E); n = E["n"]
            if n in PEMBUKA2: hook = PEMBUKA2[n][0]
            elif a["static_open"] and a["hook"] != a["first"] and a["hook_score"] >= 5: hook = a["hook"]
            else: hook = None
            ep = {"n": n, "season": S["n"], "arc": A["title"], "judul": E["title"], "ringkasan": E["focus"],
                  "gagasan": {"jenis": GAGASAN[n][0], "teks": GAGASAN[n][1]}, "pembuka": hook,
                  "gagal": GAGAL[n], "subs": []}
            for SE in E["subs"]:
                sub = {"id": SE["id"], "judul": SE["title"], "frames": []}
                for AC in SE["acts"]:
                    for fr in AC["frames"]:
                        code, shot, vis, scene, flags = eth.get(fr[0], fr)
                        if code == R.V2_START: v2 = True
                        low = scene.lower()
                        f = flags + ("AD" if ("squad" in low or "teammate" in low) else "")
                        chars = []
                        if "G" in f: chars.append("K02" if v2 else "K01")
                        chars += [RF.FLAG2K[c] for c in f if c in RF.FLAG2K and RF.FLAG2K[c] not in chars]
                        chars += [k for k in secondary_for(n, scene) if k not in chars]
                        sub["frames"].append({"kode": code, "act": AC["id"], "shot": shot, "id": vis, "scene": scene,
                                              "tokoh": chars, "latar": location_for(code),
                                              "prompt": R.prompt(scene, flags, v2, code)})
                ep["subs"].append(sub)
            episodes.append(ep)

def find(sub, code):
    hits = sorted(glob.glob(f"{ROOT}/refs/{sub}/{code}_*.png"))
    main = [h for h in hits if "potongan" not in h and "skala" not in h]
    return os.path.relpath((main or hits)[0], ROOT) if hits else None

status = {}
for line in open(f"{ROOT}/refs/STATUS.tsv") if os.path.exists(f"{ROOT}/refs/STATUS.tsv") else []:
    c, s = line.rstrip("\n").split("\t"); status[c] = s
refs = {}
kinds = {k: v[2] for k, v in RF.MAIN.items()}
for k, (name, anchor) in RF.ALLCHAR.items():
    kind = kinds.get(k)
    p = RF.char_prompt(k, name, anchor, kind) if kind else RF.group_prompt(k, name, anchor)
    f = find("karakter", k); st = status.get(k, "Lolos" if f else "Belum ada")
    refs[k] = {"nama": name, "jenis": "karakter", "file": f, "lolos": st.startswith("Lolos"), "catatan": st,
               "anchor": anchor, "prompt_sheet": p}
for k, (name, anchor) in LOCS.items():
    f = find("latar", k)
    refs[k] = {"nama": name, "jenis": "latar", "file": f, "lolos": bool(f), "catatan": "Lolos" if f else "Belum ada",
               "anchor": anchor, "prompt_sheet": RF.loc_prompt(k, name, anchor)}
refs["K30_ketiga"] = {"nama": "Instruktur Ketiga (potongan)", "jenis": "potongan", "lolos": True, "catatan": "Potongan dari K30",
                      "file": "refs/karakter/K30_Instruktur_Ketiga_potongan.png", "anchor": "", "prompt_sheet": ""}
refs["L03_pintu"] = {"nama": "Lorong Tembak, ujung pintu (potongan)", "jenis": "potongan", "lolos": True, "catatan": "Potongan dari L03",
                     "file": "refs/latar/L03_Lorong_Tembak_ujung_pintu_potongan.png", "anchor": "", "prompt_sheet": ""}
os.makedirs(f"{ROOT}/data", exist_ok=True)
json.dump(episodes, open(f"{ROOT}/data/episodes.json", "w"), ensure_ascii=False, indent=1)
json.dump(refs, open(f"{ROOT}/data/refs.json", "w"), ensure_ascii=False, indent=1)
nf = sum(len(s["frames"]) for e in episodes for s in e["subs"])
print(len(episodes), "episode,", nf, "frame;", sum(1 for r in refs.values() if r["lolos"]), "referensi lolos dari", len(refs))
