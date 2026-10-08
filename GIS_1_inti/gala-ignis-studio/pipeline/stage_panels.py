"""Tahap panel: satu gambar per frame, tanpa teks, dengan referensi tokoh, latar, dan gaya. QC di setiap gambar."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from .common import CFG, ROOT, log, mock, episodes, ep_dir, load_refs, read_json, write_json, frames_final
from . import vertex, qc, stage_refs

GAYA_TENANG = "refs/gaya/gaya_tenang.png"   # panel komik yang disetujui, tanpa aksi: acuan render saja, tidak bisa disalin posenya

HEAD = ("Create a NEW single image, portrait aspect ratio {aspect}. This is ONE comic panel, not a page: no panel borders, no text, no letters, "
        "no speech bubbles, no captions, no sound-effect lettering, no watermark.")
RULE = ("Copy every character and the place EXACTLY from the references. Each character keeps exactly the proportions, face, hair, goggles or "
        "headwear, outfit and colors of its reference; no extra straps, belts, capes or accessories. Copy the place's walls, doors, windows and "
        "large props and keep them on the same sides as in its reference. Do not copy the pose, composition or camera of any reference image, "
        "do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture. "
        "If the scene says a character is hit, pushed, blasted, caught in a blast or shielding, the force comes from OUTSIDE toward that character; "
        "the character does not emit it unless the scene says so. Describe left and right by image side.")
AVOID = ("Avoid: any text or letters, speech bubbles, panel borders, reference-sheet layout, several views of the same character, grey sheet "
         "background, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands.")

# kotak tampak depan (pecahan lebar dan tinggi) untuk sheet buatan tangan yang tidak terbaca heuristik
POTONG_MANUAL = {"K03": (0.03, 0.08, 0.36, 0.50), "K10": (0.04, 0.06, 0.28, 0.97), "K12": (0.18, 0.06, 0.43, 0.97),
                 "K17": (0.06, 0.05, 0.31, 0.97), "K39": (0.21, 0.07, 0.47, 0.97), "K40": (0.02, 0.07, 0.34, 0.72),
                 "K54": (0.07, 0.12, 0.50, 0.50), "K50": (0.03, 0.10, 0.30, 0.97)}
SHEET_UTUH = {"K51"}   # kelompok: semua figur dibutuhkan


def _blok_pertama(img):
    """Kotak figur paling kiri di sheet berlatar polos: blok kolom berisi pertama yang cukup lebar."""
    a = np.asarray(img, dtype=np.int16); H, W = a.shape[:2]
    band = a[int(H * 0.08):int(H * 0.88)]
    bg = np.median(np.concatenate([band[:6].reshape(-1, 3), band[:, :6].reshape(-1, 3), band[:, -6:].reshape(-1, 3)]), axis=0)
    diff = np.abs(band - bg).sum(axis=2) > 80
    xs = np.where(diff.mean(axis=0) > 0.04)[0]
    if not len(xs):
        return None
    gap = max(3, int(W * 0.012)); blocks = []; st = en = xs[0]
    for x in xs[1:]:
        if x - en > gap:
            blocks.append((st, en)); st = x
        en = x
    blocks.append((st, en))
    blocks = [b for b in blocks if b[1] - b[0] >= W * 0.08] or blocks
    st, en = blocks[0]
    rows = np.where(diff[:, st:en + 1].mean(axis=1) > 0.02)[0]
    y0, y1 = (rows[0], rows[-1]) if len(rows) else (0, band.shape[0] - 1)
    off = int(H * 0.08); m = int(W * 0.015)
    return (max(0, st - m), max(0, y0 + off - m), min(W, en + m), min(H, y1 + off + m))


def ref_tokoh(k, refs, scene=""):
    """Satu gambar bersih dari tokoh: tampak depan dari sheet-nya (dicache di refs/potong). Kelompok memakai sheet utuh."""
    r = refs[k]; src = ROOT / r["file"]
    if k == "K30":
        sc = scene.lower()
        if "third instructor" in sc and "lead instructor" not in sc:
            return ROOT / refs["K30_ketiga"]["file"]
        if "instructors" in sc or "three" in sc:
            return src
    if k in SHEET_UTUH or r["jenis"] == "potongan":
        return src
    out = ROOT / f"refs/potong/{k}_depan.png"
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    if r.get("sumber") == "auto":
        t = ROOT / f"refs/auto/views/{k}_turnaround.png"
        img = Image.open(t if t.exists() else src).convert("RGB"); w, h = img.size
        img = img.crop((0, 0, w // 4, h))
    else:
        img = Image.open(src).convert("RGB"); W, H = img.size
        if k in POTONG_MANUAL:
            x0, y0, x1, y1 = POTONG_MANUAL[k]; img = img.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
        else:
            box = _blok_pertama(img); img = img.crop(box) if box else img
    out.parent.mkdir(exist_ok=True); img.save(out)
    return out


def ref_latar(k, refs):
    """Satu tampak depan tempat: potongan panorama (sheet otomatis) atau bidikan lebar teratas (sheet buatan tangan)."""
    v = ROOT / f"refs/auto/views/{k}_depan.png"
    if v.exists():
        return v
    src = ROOT / refs[k]["file"]
    if refs[k]["jenis"] == "potongan":
        return src
    out = ROOT / f"refs/potong/{k}_depan.png"
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return out
    img = Image.open(src).convert("RGB"); W, H = img.size
    out.parent.mkdir(exist_ok=True); img.crop((int(W * 0.01), int(H * 0.03), int(W * 0.99), int(H * 0.47))).save(out)
    return out


def refs_for(f, refs, gaya=None):
    """Mengembalikan (file untuk generator, label, file untuk juri, label juri)."""
    files, labels = [], []
    for k in f["tokoh"][:CFG["panel"]["max_tokoh_ref"]]:
        if refs[k]["file"] and (ROOT / refs[k]["file"]).exists():
            files.append(ref_tokoh(k, refs, f["scene"]))
            labels.append(f"{refs[k]['nama']}: exact design, front view; copy face, proportions, hair, outfit and colors exactly")
    if f["latar"] and refs[f["latar"]]["file"] and (ROOT / refs[f["latar"]]["file"]).exists():
        files.append(ref_latar(f["latar"], refs))
        labels.append(f"the place {refs[f['latar']]['nama']}: copy its walls, doors, windows, large props and their positions exactly")
    juri_files, juri_labels = list(files), list(labels)
    files.append(ROOT / GAYA_TENANG); labels.append("an approved panel of this series, ONLY for rendering style and lighting; it shows no action, do not copy it")
    return files, labels, juri_files, juri_labels


def build_prompt(f, labels, fix="", manual=""):
    p = [HEAD.format(aspect=CFG["panel"]["aspect"]),
         "Attached references, in order: " + "; ".join(f"{i + 1}) {l}" for i, l in enumerate(labels)) + ".", RULE,
         f"Camera shot: {f['shot']}.", f["prompt"]]
    if any(k in f["tokoh"] for k in ("K01", "K02")):
        p.append("Gala's goggle lenses are fully opaque and dark at all times; his eyes are never visible.")
    if "K03" in f["tokoh"]:
        p.append("The fire sprite Ethylene has two white dot eyes and NO mouth, no arms and no legs.")
    p.append(AVOID)
    if manual:
        p.append("Director's note: " + manual)
    if fix:
        p.append("The previous attempt was rejected. Fix this: " + fix)
    return "\n".join(p)


def kontak(n, subs, meta):
    d = ep_dir(n); font = ImageFont.load_default()
    for sub in subs:
        fr = sub["frames"]; cols = 4; rows = -(-len(fr) // cols); tw, th = 360, 450
        sheet = Image.new("RGB", (cols * tw, rows * (th + 40)), (26, 20, 16)); dr = ImageDraw.Draw(sheet)
        for i, f in enumerate(fr):
            p = d / "panel" / f"{f['kode']}.png"; x, y = (i % cols) * tw, (i // cols) * (th + 40)
            m = meta.get(f["kode"], {})
            if p.exists():
                sheet.paste(Image.open(p).convert("RGB").resize((tw - 8, th - 8)), (x + 4, y + 4))
            if not m.get("lolos"):
                dr.rectangle([x + 1, y + 1, x + tw - 2, y + th - 2], outline=(230, 60, 40), width=5)
            dr.text((x + 8, y + th + 6), f"{f['kode']}  skor {m.get('skor', '-')}  {'LOLOS' if m.get('lolos') else 'TINJAU'}", fill=(255, 240, 210), font=font)
        sheet.save(d / f"kontak_{sub['id']}.png")


def run(n, force=False, paksa=False, only=None):
    refs = load_refs(); d = ep_dir(n); subs = frames_final(n)
    kurang = stage_refs.missing([n], refs)
    if kurang and not paksa:
        log(f"Ep {n}: referensi belum siap ({', '.join(kurang)}). Jalankan `python run.py refs --episode {n}` atau setujui dengan `python run.py setujui KODE`.")
        return False
    meta = read_json(d / "panel.json", {}); gaya = {}; prev = None; aspect = CFG["panel"]["aspect"]
    for sub in subs:
        for f in sub["frames"]:
            kode = f["kode"]; path = d / "panel" / f"{kode}.png"; m = meta.get(kode, {})
            redo = force or (only and kode in only) or m.get("ulang")
            if path.exists() and m.get("lolos") and not redo:
                prev = Image.open(path); continue
            if only and kode not in only and path.exists():
                prev = Image.open(path); continue
            files, labels, jf, jl = refs_for(f, refs, gaya)
            best = None; fix = ""
            for i in range(CFG["panel"]["max_attempts"]):
                img = vertex.gen_image(build_prompt(f, labels, fix, m.get("catatan_manual", "")), files, aspect)
                probs = qc.lokal(img, aspect)
                if prev is not None and not mock() and qc.mirip(img, prev) > 0.97:
                    probs.append("hampir sama dengan panel sebelumnya")
                j = qc.juri_panel(img, f, jf, jl) if not probs else {"lolos": False, "skor": 0, "gagal": ["lokal"], "masalah": probs, "perbaikan": "; ".join(probs)}
                j["percobaan"] = i + 1
                if best is None or (j["lolos"], j["skor"]) > (best[1]["lolos"], best[1]["skor"]):
                    best = (img, j)
                if j["lolos"]:
                    break
                fix = j["perbaikan"] or "; ".join(j["masalah"])
                log(f"  {kode} percobaan {i + 1} gagal QC: {'; '.join(map(str, j['masalah']))[:160]}")
            img, j = best; img.save(path)
            j["refs"] = [p.name for p in files]
            if m.get("catatan_manual"):
                j["catatan_manual"] = m["catatan_manual"]
            meta[kode] = j; write_json(d / "panel.json", meta)
            prev = img
            log(f"  {kode}: {'lolos' if j['lolos'] else 'PERLU DITINJAU'} (skor {j['skor']}, {j['percobaan']} percobaan)")
    kontak(n, subs, meta)
    total = sum(len(s["frames"]) for s in subs); ok = sum(1 for s in subs for f in s["frames"] if meta.get(f["kode"], {}).get("lolos"))
    log(f"Panel ep {n}: {ok}/{total} lolos")
    return ok == total
