"""Tahap referensi: membuat sheet tokoh dan latar yang belum ada atau belum lolos."""
import json
from PIL import Image
from .common import CFG, ROOT, log, episodes, load_refs, save_refs
from . import vertex, qc


def needed(eps):
    out = []
    for n in eps:
        for sub in episodes()[n]["subs"]:
            for f in sub["frames"]:
                for k in f["tokoh"] + ([f["latar"]] if f["latar"] else []):
                    if k not in out:
                        out.append(k)
    return out


def missing(eps, refs=None):
    refs = refs or load_refs()
    return [k for k in needed(eps) if not (refs[k]["lolos"] and refs[k]["file"] and (ROOT / refs[k]["file"]).exists())]


def semua_episode():
    return sorted(episodes())


def menunggu(refs=None):
    """Sheet otomatis yang lolos QC model tetapi belum disetujui manusia."""
    refs = refs or load_refs()
    return [k for k, r in refs.items() if r.get("sumber") == "auto" and not r["lolos"] and r.get("qc", {}).get("lolos") and r["file"] and (ROOT / r["file"]).exists()]


def gerbang():
    """True kalau SEMUA referensi yang dipakai seri ini sudah lolos dan disetujui. Produksi episode menunggu ini."""
    return not missing(semua_episode())


def kontak():
    """Lembar kontak semua sheet otomatis, 12 per lembar, untuk ditinjau manusia."""
    from PIL import ImageDraw, ImageFont
    refs = load_refs(); items = [(k, r) for k, r in refs.items() if r.get("sumber") == "auto" and r["file"] and (ROOT / r["file"]).exists()]
    out = []; tw, th = 640, 360; font = ImageFont.load_default()
    for old in (ROOT / "refs/auto").glob("KONTAK_*.png"):
        old.unlink()
    for n in range(0, len(items), 12):
        part = items[n:n + 12]; rows = -(-len(part) // 3)
        sheet = Image.new("RGB", (3 * tw, rows * (th + 44)), (26, 20, 16)); dr = ImageDraw.Draw(sheet)
        for i, (k, r) in enumerate(part):
            x, y = (i % 3) * tw, (i // 3) * (th + 44)
            sheet.paste(Image.open(ROOT / r["file"]).convert("RGB").resize((tw - 8, th - 8)), (x + 4, y + 4))
            st = "DISETUJUI" if r["lolos"] else ("menunggu persetujuan" if r.get("qc", {}).get("lolos") else "GAGAL QC")
            if not r["lolos"]:
                dr.rectangle([x + 1, y + 1, x + tw - 2, y + th - 2], outline=(242, 169, 59) if r.get("qc", {}).get("lolos") else (230, 60, 40), width=4)
            dr.text((x + 8, y + th + 8), f"{k}  {r['nama']}  [{st}]", fill=(255, 240, 210), font=font)
        p = ROOT / f"refs/auto/KONTAK_{n // 12 + 1:02d}.png"; sheet.save(p); out.append(p)
    return out


ARAH = ["depan", "kanan", "belakang", "kiri"]  # searah jarum jam dilihat dari atas
ARAH_EN = {"depan": "front", "kanan": "right", "belakang": "back", "kiri": "left"}
GAYA_PEMBUKA = ("The first attached images are approved sheets from the same series: match their 3D rendering style and materials exactly "
                "(stylized 3D CGI like a modern 3D animated feature film, rounded shapes, soft studio lighting), but do not copy their content. ")
# ponytail: daftar tangan objek tengah yang punya sheet sendiri; ganti dengan deteksi otomatis kalau latar berobjek bertambah banyak
OBJEK_REF = {"L07": "K68"}
SATU_GAMBAR = " One single image filling the whole frame: no grid, no panels, no borders, no text, no labels, no characters."


def _koreksi(r, fix):
    asal = r.get("catatan_asal") or r["catatan"]
    t = ""
    if asal.startswith("BELUM"):
        t += "\nImportant correction from the previous rejected version: " + asal.split(":", 1)[-1].strip()
    if fix:
        t += "\nFix this problem from the previous attempt: " + fix
    return t


def _denah(k, r):
    """Peta penanda tetap untuk satu lokasi atau satu tokoh. Disimpan supaya bisa dipakai ulang dan diperiksa."""
    path = ROOT / f"refs/auto/denah/{k}.json"
    if path.exists():
        return json.load(open(path, encoding="utf-8"))
    koreksi = _koreksi(r, "")
    if r["jenis"] == "latar":
        prompt = ("You are a set designer. Turn this location into a fixed layout plan so it can be drawn from four directions without contradictions.\n"
                  f"Location: {r['anchor']}{koreksi}\n"
                  'Answer JSON only: {"penanda": {"depan": str, "kanan": str, "belakang": str, "kiri": str}, "sisi": {"depan": str, "kanan": str, "belakang": str, "kiri": str}, "tengah": str, "atas": str}. "penanda" is a short noun phrase naming the ONE distinctive landmark of that side (for example "red tool racks", "glass office balcony"); the four must be completely different objects. '
                  "Each value is one English sentence listing concrete landmarks (doors, windows, openings, large props, light sources, distant scenery for outdoor places). "
                  "'depan' is the most important side, 'kanan' and 'kiri' are the sides to the right and left of a viewer facing 'depan', 'belakang' is opposite 'depan'. "
                  "Assign every landmark from the description to exactly ONE place; 'tengah' holds free-standing objects in the middle with the direction they face; "
                  "'atas' is the ceiling or sky. Every side must have at least one distinctive landmark so the four views are easy to tell apart. "
                  "Also add \"tengah_hadap\": the side (depan, kanan, belakang or kiri) that the FRONT of the main center object points to, or \"\" if there is no directional center object.")
    else:
        prompt = ("You are a character designer. List the asymmetric details of this design so it can be drawn from four directions without mirroring mistakes.\n"
                  f"Design: {r['anchor']}{koreksi}\n"
                  'Answer JSON only: {"asimetris": [{"detail": str, "sisi": "kanan" or "kiri"}], "depan": str, "belakang": str}. '
                  "'sisi' is the character's OWN right or left. 'depan' and 'belakang' are one English sentence each describing what is seen from the front and from the back. "
                  "If the design is fully symmetric, 'asimetris' is an empty list. "
                  "Also add \"tetap\": one English sentence fixing every state that must not change between views (hood up or down, mask on or off, hair loose or tied, "
                  "what each hand holds, sleeves rolled or not), choosing the state the description implies.")
    mock = lambda: {"sisi": {a: f"a wall with landmark {a}" for a in ARAH}, "tengah": "", "atas": "", "asimetris": [], "depan": "", "belakang": ""}
    for _ in range(3):
        d = vertex.gen_json(prompt, model=CFG["models"]["judge"], mock_value=mock)
        pen = [v.strip().lower() for v in d.get("penanda", {}).values()]
        if r["jenis"] != "latar" or (len(pen) == 4 and len(set(pen)) == 4):
            break
        prompt += ("\nYour previous answer gave two sides the same description. Every side must be different: invent a distinctive, "
                   "fitting landmark for each plain side (for example racks, a balcony, a mural, pipes, a side door) so no two sides look alike.")
    path.parent.mkdir(parents=True, exist_ok=True)
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return d


def _hadap(r, d, arah):
    """Arah hadap yang diharapkan (camera, away, left, right) untuk tokoh, atau untuk objek tengah sebuah latar."""
    if r["jenis"] != "latar":
        return {"depan": "camera", "belakang": "away", "kiri": "right", "kanan": "left"}[arah]
    if d.get("tengah_hadap") not in ARAH:
        return ""
    return ["away", "right", "camera", "left"][(ARAH.index(d["tengah_hadap"]) - ARAH.index(arah)) % 4]


# tampilan sheet objek yang cocok dengan arah hadap objek di sebuah latar
VIEW_OBJEK = {"camera": "depan", "away": "belakang", "right": "kiri", "left": "kanan"}


def _arah_objek(d, arah):
    """Ke mana bagian depan objek tengah tampak di gambar, dilihat dari kamera yang menghadap `arah`."""
    hadap = d.get("tengah_hadap")
    if hadap not in ARAH:
        return ""
    beda = (ARAH.index(hadap) - ARAH.index(arah)) % 4
    return ["its front points away from the camera (we see its rear)", "its front points toward the RIGHT edge of the image",
            "its front points toward the camera (we see its front)", "its front points toward the LEFT edge of the image"][beda]


def _posisi_tokoh(d, arah):
    out = []
    for a in d.get("asimetris", []):
        s_ = a.get("sisi")
        if arah == "depan":
            w = "appears on the LEFT half of the image" if s_ == "kanan" else "appears on the RIGHT half of the image"
        elif arah == "belakang":
            w = "appears on the RIGHT half of the image" if s_ == "kanan" else "appears on the LEFT half of the image"
        else:
            w = "is clearly visible" if s_ == arah else "is hidden or only barely visible"
        out.append(f"{a.get('detail')} (on the character's own {'right' if s_ == 'kanan' else 'left'}) {w}")
    return out


def _harapan(r, d, arah):
    """Apa yang wajib terlihat di satu sudut pandang. Dipakai oleh prompt gambar dan oleh juri, supaya keduanya sama."""
    if r["jenis"] == "latar":
        i = ARAH.index(arah); kiri, kanan, lawan = ARAH[(i - 1) % 4], ARAH[(i + 1) % 4], ARAH[(i + 2) % 4]
        sisi = d["sisi"]; orient = _arah_objek(d, arah)
        return (f"one wide eye-level view standing at the {ARAH_EN[lawan]} edge and looking toward the {ARAH_EN[arah]} side. "
                f"Straight ahead, filling the center background: the {ARAH_EN[arah]} side ({sisi[arah]}). "
                f"Along the LEFT edge of the image only: the {ARAH_EN[kiri]} side ({sisi[kiri]}). "
                f"Along the RIGHT edge of the image only: the {ARAH_EN[kanan]} side ({sisi[kanan]}). "
                f"Clearly visible in the middle ground: {d.get('tengah', '')}" + (f"; {orient}" if orient else "") + ". "
                f"Behind the camera and NOT visible anywhere: the {ARAH_EN[lawan]} side ({sisi[lawan]}).")
    tampak = {"depan": "front view, facing the camera", "belakang": "back view, facing away from the camera",
              "kiri": "side view showing the character's LEFT side (the character faces the right edge of the image)",
              "kanan": "side view showing the character's RIGHT side (the character faces the left edge of the image)"}[arah]
    pos = _posisi_tokoh(d, arah)
    return (f"the full design once, in {tampak}, standing in a neutral relaxed pose, centered, on a plain light grey background. "
            + (f"Fixed states in every view: {d['tetap']} " if d.get("tetap") else "")
            + ("Asymmetric details in this view: " + "; ".join(pos) + "." if pos else ""))


def _prompt_view(r, d, arah, fix, objek=None):
    if r["jenis"] == "latar":
        p = (GAYA_PEMBUKA + f"Location: {r['anchor']}\nFixed layout plan of this location (never change it): "
             + " ".join(f"{ARAH_EN[a]} side (landmark: {d.get('penanda', {}).get(a, '')}): {d['sisi'][a]}" for a in ARAH)
             + f" Center: {d.get('tengah', '')} Above: {d.get('atas', '')}\nDraw " + _harapan(r, d, arah))
        if objek:
            p += (f" One attached image (right after the style sheets) shows the center object ({objek}) exactly as it must appear in this view, "
                  "already in the correct orientation: copy its shape, colors, crest and facing direction exactly.")
        acuan = {"depan": "", "belakang": " The last attached image is the front view of this same location.",
                 "kiri": " The last two attached images are the front view and the back view of this same location.",
                 "kanan": " The last two attached images are the front view and the back view of this same location."}[arah]
        if acuan:
            p += (acuan + " Keep every material, color, light and object identical to them and reuse their walls exactly; "
                  "this is a NEW camera direction, so do not copy their composition.")
    else:
        p = GAYA_PEMBUKA + f"Design: {r['anchor']}\nDraw " + _harapan(r, d, arah)
        if arah != "depan":
            p += (" The attached front view" + (" and back view" if arah in ("kiri", "kanan") else "")
                  + " show this same design: keep every color, proportion, accessory, state and detail identical, only the viewing direction changes; never mirror the design.")
    return p + SATU_GAMBAR + _koreksi(r, fix)


def _cek_view(img, r, d, arah, acuan):
    """Juri per sudut pandang, dengan harapan yang sama persis seperti di prompt gambar."""
    nama = {1: "The first image is the approved front view; ", 2: "The first two images are the approved front and back views; "}.get(len(acuan), "")
    prompt = ("You are a strict continuity supervisor for a 3D-animated series. " + nama
              + "the LAST image must show " + _harapan(r, d, arah)
              + '\nAnswer JSON only: {"ok": bool, "masalah": ["<kalimat pendek bahasa Indonesia>"], "perbaikan": "<one English sentence or empty>"}. '
              "Check each requirement above one by one. ok is true only if every requirement holds, nothing listed as not visible appears, the style is the same 3D CGI "
              "animated-film look (not 2D, not photoreal), there is no text and no grid"
              + (", and it is unmistakably the same place or design as the approved views, seen from a genuinely different direction" if acuan else "") + ".")
    harap = _hadap(r, d, arah)
    if harap:
        prompt += (' Also add "hadap": where the FRONT (face, nose or cockpit) of ' + ("the character" if r["jenis"] != "latar" else "the main center object")
                   + ' points in the LAST image: "camera", "away", "left" (toward the left edge of the image) or "right" (toward the right edge of the image).')
    j = vertex.gen_json(prompt, images=list(acuan) + [img], model=CFG["models"]["judge"], temperature=0.0,
                        mock_value=lambda: {"ok": True, "masalah": [], "perbaikan": "", "hadap": harap})
    ok, masalah, perbaikan = bool(j.get("ok")), j.get("masalah", []), j.get("perbaikan", "")
    if harap and j.get("hadap") != harap:
        ok = False; masalah = [f"arah hadap {j.get('hadap')}, seharusnya {harap}"] + masalah
        perbaikan = (f"The front must point {'toward the camera' if harap == 'camera' else 'away from the camera' if harap == 'away' else 'toward the ' + harap.upper() + ' edge of the image'}. " + perbaikan).strip()
    return ok, masalah, perbaikan


def _susun(k, r, views):
    from PIL import ImageDraw, ImageFont
    w, h = views["depan"].size
    urut = [["depan", "belakang"], ["kiri", "kanan"]] if r["jenis"] == "latar" else [["depan", "kiri", "belakang", "kanan"]]
    g = 16; cap = 56
    sheet = Image.new("RGB", (len(urut[0]) * (w + g) + g, len(urut) * (h + g) + g + cap), (205, 205, 205))
    for y, baris in enumerate(urut):
        for x, a in enumerate(baris):
            sheet.paste(views[a].convert("RGB").resize((w, h)), (g + x * (w + g), g + y * (h + g)))
    try:
        font = ImageFont.truetype("arial.ttf", 34)
    except OSError:
        font = ImageFont.load_default()
    ImageDraw.Draw(sheet).text((g, sheet.height - cap + 8), f"{k} {r['nama'].upper()}", fill=(40, 40, 40), font=font)
    return sheet


def run(eps, force=False):
    refs = load_refs(); todo = needed(eps) if force else missing(eps, refs)
    todo = [k for k in todo if not (refs[k].get("sumber") != "auto" and refs[k]["lolos"])]  # jangan timpa sheet buatan tangan
    if not force:
        tunggu = set(menunggu(refs)); todo = [k for k in todo if k not in tunggu]         # sudah lolos QC, tinggal disetujui
    if not todo:
        log("Referensi: tidak ada yang perlu dibuat."); return not missing(eps)
    log(f"Referensi yang dibuat: {len(todo)} ({', '.join(todo)})")
    (ROOT / "refs/auto/views").mkdir(parents=True, exist_ok=True)
    tunggal = ROOT / "refs/auto/views/K16_depan.png"   # tampilan tunggal yang sudah disetujui; sheet kolase membuat model ikut membuat kolase
    gaya_k = [Image.open(tunggal)] if tunggal.exists() else [Image.open(ROOT / refs[k]["file"]) for k in ("K01", "K03") if refs[k]["file"]]
    gaya_l = [Image.open(ROOT / refs[k]["file"]) for k in ("L01", "L02") if refs[k]["file"]]
    for k in todo:
        r = refs[k]; gaya = gaya_l if r["jenis"] == "latar" else gaya_k
        objek = OBJEK_REF.get(k)
        aspect = "16:9" if r["jenis"] == "latar" else "3:4"
        d = _denah(k, r); views = {}; masalah_akhir = []
        for arah in ("depan", "belakang", "kiri", "kanan"):
            fix = ""; terbaik = None; ok = False
            for i in range(CFG["panel"]["max_attempts"]):
                acuan = [views[a] for a in ("depan", "belakang") if a in views]
                f_objek = objek and ROOT / f"refs/auto/views/{objek}_{VIEW_OBJEK.get(_hadap(r, d, arah), 'depan')}.png"
                pakai_objek = bool(f_objek and f_objek.exists())
                img = vertex.gen_image(_prompt_view(r, d, arah, fix, objek if pakai_objek else None),
                                       gaya + ([Image.open(f_objek)] if pakai_objek else []) + acuan, aspect=aspect)
                ok, masalah, perbaikan = _cek_view(img, r, d, arah, acuan)
                if terbaik is None or ok:
                    terbaik = (img, masalah)
                if ok:
                    break
                fix = perbaikan or "; ".join(masalah)
                log(f"  {k} {arah} percobaan {i + 1} gagal: {'; '.join(masalah)[:160]}")
            views[arah] = terbaik[0]; terbaik[0].save(ROOT / f"refs/auto/views/{k}_{arah}.png")
            if not ok:
                masalah_akhir += [f"{arah}: {m}" for m in terbaik[1]]
        sheet = _susun(k, r, views); path = f"refs/auto/{k}.png"; sheet.save(ROOT / path)
        j = qc.juri_sheet(sheet, r, gaya)
        if masalah_akhir:
            j["lolos"] = False; j["masalah"] = masalah_akhir + j["masalah"]
        asal = r.get("catatan_asal") or r["catatan"]
        r.update(file=path, lolos=False, sumber="auto", qc=j, catatan_asal=asal,
                 catatan="Lolos QC model, menunggu persetujuan manusia" if j["lolos"] else "GAGAL QC: " + "; ".join(j["masalah"])[:200])
        save_refs(refs)
        log(f"  {k} {r['nama']}: {'lolos QC, menunggu persetujuan' if j['lolos'] else 'GAGAL QC'} (skor {j['skor']})")
    kontak()
    return False
