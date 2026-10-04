"""Tahap panel: satu gambar per frame, tanpa teks, dengan referensi tokoh, latar, dan gaya. QC di setiap gambar."""
from PIL import Image, ImageDraw, ImageFont
from .common import CFG, ROOT, log, mock, episodes, ep_dir, load_refs, read_json, write_json, frames_final
from . import vertex, qc, stage_refs

GAYA_DEFAULT = "refs/gaya/E02_REF_lab.png"

HEAD = ("Create a NEW single image, portrait aspect ratio {aspect}. This is ONE comic panel, not a page: no panel borders, no text, no letters, "
        "no speech bubbles, no captions, no sound-effect lettering, no watermark.")
RULE = ("Copy every character and the place EXACTLY from the references. Do not draw the sheets themselves, and do not reuse or edit any "
        "attached image as the canvas: paint a completely new picture. Describe left and right by image side.")
AVOID = ("Avoid: any text or letters, speech bubbles, panel borders, reference-sheet layout, several views of the same character, grey sheet "
         "background, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands.")


def refs_for(f, refs, gaya):
    """Mengembalikan (file untuk generator, label, file untuk juri)."""
    files, labels = [], []
    for k in f["tokoh"][:CFG["panel"]["max_tokoh_ref"]]:
        r = refs[k]
        if k == "K30" and "third instructor" in f["scene"].lower() and "lead instructor" not in f["scene"].lower():
            r = refs["K30_ketiga"]
        if r["file"] and (ROOT / r["file"]).exists():
            files.append(ROOT / r["file"]); labels.append(f"character sheet of {refs[k]['nama']}")
    if f["latar"] and refs[f["latar"]]["file"] and (ROOT / refs[f["latar"]]["file"]).exists():
        files.append(ROOT / refs[f["latar"]]["file"]); labels.append(f"environment sheet of {refs[f['latar']]['nama']}")
    juri_files, juri_labels = list(files), list(labels)
    g = gaya.get(f["latar"]) or gaya.get("*") or ROOT / GAYA_DEFAULT
    files.append(g); labels.append("an approved panel of this series, ONLY for rendering style and lighting; do not copy its composition, pose or content")
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
                gaya.setdefault(f["latar"], path); gaya.setdefault("*", path); prev = Image.open(path); continue
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
            if j["lolos"]:
                gaya.setdefault(f["latar"], path); gaya.setdefault("*", path)
            prev = img
            log(f"  {kode}: {'lolos' if j['lolos'] else 'PERLU DITINJAU'} (skor {j['skor']}, {j['percobaan']} percobaan)")
    kontak(n, subs, meta)
    total = sum(len(s["frames"]) for s in subs); ok = sum(1 for s in subs for f in s["frames"] if meta.get(f["kode"], {}).get("lolos"))
    log(f"Panel ep {n}: {ok}/{total} lolos")
    return ok == total
