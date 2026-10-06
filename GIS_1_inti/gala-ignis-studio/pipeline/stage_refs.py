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
GAYA_PEMBUKA = ("The first attached images are approved references from the same series: match their stylized 3D CGI animated-film rendering style "
                "and materials exactly (rounded chunky shapes, clean simplified textures, soft studio lighting, like a modern 3D animated feature film, never photorealistic "
                "or gritty), but do not copy their layout or content. ")
BUDAYA_DASAR = ("The series is set in a futuristic Nusantara (Indonesian) world. Never introduce European or Western elements: no stained glass, "
                "no Gothic or Roman arches, no Mediterranean terracotta villas, no Western statues. Never show real national symbols: no Garuda Pancasila, "
                "no eagle emblems, no flags. ")
NUSANTARA = "Architecture and props are inspired by Javanese and Indonesian design (joglo tiered roofs, batik motifs, carved teak wood, gold trim) mixed with clean sci-fi technology. "
TANPA_LAMBANG = "No emblem or crest of any kind. "
# pemilik tempat menentukan ornamen dan lambang; deskripsi latar sering tidak menyebut pemiliknya
FAKSI = {
    "akademi": NUSANTARA + "This place belongs to the Galians academy: the Galians crest (a pair of golden wings flanking a circle that contains a flame) may appear. ",
    "kota": NUSANTARA + "A civilian place in the city of Nusantara. " + TANPA_LAMBANG,
    "industri": "A neutral industrial place: clean stylized sci-fi industry with only light Nusantara touches. " + TANPA_LAMBANG,
    "musuh": "An ENEMY place: cold industrial metal or dark crystal, no Nusantara ornament, no carved wood, no gold trim. " + TANPA_LAMBANG,
    "paralel": "A dead, frozen version of the world in a defeated parallel timeline: ruined, dark, snowbound, no lights. " + TANPA_LAMBANG,
    "markas": "The hidden, lived-in base of the resistance in a frozen parallel timeline: cold old structure, but warmly lit by lanterns built from "
              "salvaged batik panels, with scrap workbenches, bedrolls and supplies; cosy and hopeful. " + TANPA_LAMBANG,
    "kuno": "An ancient mystical Nusantara place: candi stone, carved reliefs and nature, no modern technology. " + TANPA_LAMBANG,
    "gaib": "An otherworldly elemental realm, not built by people. " + TANPA_LAMBANG,
}
_GRUP = {"akademi": "L07-L18 L40", "kota": "L22-L25 L27 L28 L32 L33 L64 L66 L67", "industri": "L19-L21 L26 L30 L31",
         "musuh": "L29 L34-L39 L65 L68", "paralel": "L41 L42 L44 L45", "markas": "L43", "kuno": "L46-L50 L58-L62", "gaib": "L51-L57 L63"}


def _faksi(k):
    n = int(k[1:])
    for grup, rentang in _GRUP.items():
        for bagian in rentang.split():
            a, _, b = bagian.partition("-")
            if int(a[1:]) <= n <= int((b or a)[1:]):
                return grup
    return "kota"


def BUDAYA_UNTUK(k):
    return BUDAYA_DASAR + FAKSI[_faksi(k)]
TANPA_TEKS = (" Absolutely no text anywhere: no words, no letters, no numbers, no direction labels such as FRONT, BACK, LEFT or RIGHT, "
              "no caption bar, no border, no watermark. The image is pure picture from edge to edge.")
# ponytail: daftar tangan objek tengah yang punya sheet sendiri; ganti dengan deteksi otomatis kalau latar berobjek bertambah banyak
OBJEK_REF = {"L07": "K68"}
# urutan figur di turnaround tokoh dan arah hadap yang diharapkan
TURNAROUND = [("depan", "camera"), ("kiri", "right"), ("belakang", "away"), ("kanan", "left")]


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
        prompt = ("You are a set designer. Turn this location into a fixed layout plan seen from one camera position near the back.\n"
                  + BUDAYA_UNTUK(k) + "Invent only details that fit this world. Never plan written labels, signs or lettering, "
                  "and never plan people, robots, automatons, statues of beings or any other figures. "
                  "If the location is outdoors (a city, street, plaza, landscape, sea, sky), the camera stands outdoors in the open: the four sides are the surrounding "
                  "buildings or scenery and 'atas' is the sky; never turn an outdoor place into a room or a lobby.\n"
                  f"Location: {r['anchor']}{koreksi}\n"
                  'Answer JSON only: {"penanda": {"depan": str, "kanan": str, "belakang": str, "kiri": str}, "sisi": {"depan": str, "kanan": str, "belakang": str, "kiri": str}, '
                  '"tengah": str, "atas": str}. "penanda" is a short noun phrase naming the ONE distinctive landmark of that side; the four must be completely different objects. '
                  "Each 'sisi' value is one English sentence listing concrete landmarks (doors, windows, openings, large props, light sources, distant scenery outdoors), "
                  "each landmark appearing exactly once in the whole plan. 'depan' is the most important side, 'kanan' and 'kiri' are to the right and left of a viewer facing 'depan', "
                  "'belakang' is opposite 'depan'. 'tengah' holds free-standing objects between the camera and 'depan', with the direction they face; 'atas' is the ceiling or sky.")
    else:
        prompt = ("You are a character designer. List the asymmetric details of this design so it can be drawn from four directions without mirroring mistakes.\n"
                  f"Design: {r['anchor']}{koreksi}\n"
                  'Answer JSON only: {"asimetris": [{"detail": str, "sisi": "kanan" or "kiri"}], "tetap": str}. '
                  "'sisi' is the character's OWN right or left. 'tetap' is one English sentence fixing every state that must not change between views "
                  "(hood up or down, mask on or off, hair loose or tied, what each hand holds), choosing the state the description implies. "
                  "If the design is fully symmetric, 'asimetris' is an empty list.")
    mock = lambda: {"penanda": {a: f"landmark {a}" for a in ARAH}, "sisi": {a: f"a wall with landmark {a}" for a in ARAH}, "tengah": "", "atas": "", "asimetris": [], "tetap": ""}
    for _ in range(3):
        d = vertex.gen_json(prompt, model=CFG["models"]["judge"], mock_value=mock)
        pen = [v.strip().lower() for v in d.get("penanda", {}).values()]
        if r["jenis"] != "latar" or (len(pen) == 4 and len(set(pen)) == 4):
            break
        prompt += "\nYour previous answer gave two sides the same landmark. Invent a distinctive, fitting landmark for each plain side so no two sides look alike."
    path.parent.mkdir(parents=True, exist_ok=True)
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return d


def _tata_panorama(d):
    s = d["sisi"]
    return (f"FRONT side in the exact center of the image ({s['depan']}); LEFT side centered at one quarter of the width ({s['kiri']}); "
            f"RIGHT side centered halfway between the center and the right edge ({s['kanan']}); BACK side at BOTH the far left edge and the far right edge of the image ({s['belakang']}), "
            f"so the image wraps around through the back side. Between the camera and the front side: {d.get('tengah', '')} Ceiling or sky: {d.get('atas', '')}")


ZONA = ("Divide the LAST image into five vertical zones and check each: far-left edge zone (0-12% of the width) must show the back side; "
        "zone around 25% must show the left side; center zone (around 50%) must show the front side and the center object; zone around 75% must show the right side; "
        "far-right edge zone (88-100%) must show the back side again. The back side appearing at BOTH edges is intentional and correct: "
        "never count it as a duplicate or as an error. Landmarks of one side must not appear in another side's zone.")


def _prompt_latar(k, r, d, objek, fix):
    p = (GAYA_PEMBUKA + BUDAYA_UNTUK(k) + f"Location: {r['anchor']}\n"
         "Draw ONE seamless 360-degree equirectangular panorama of this location from a single camera at eye level standing near the back side. "
         "The horizontal axis covers a full turn. It is ONE continuous scene: never split it into panels, never draw vertical dividing lines, bars or gaps, not a triptych. Layout: " + _tata_panorama(d)
         + " One continuous ceiling (or sky, outdoors) and floor (or ground) all the way around; each landmark appears once only. No characters. "
         "If this location is outdoors, the camera stands outdoors in the open, never inside a room looking out through a window. "
         "This is a cartoon world from a modern 3D animated feature film, NOT a photograph: saturated friendly colors, rounded bevelled edges, simplified clean surfaces, "
         "soft bright lighting, no rust, no grime, no dirt, no stains, no photographic realism.")
    if objek:
        p += f" The attached images right after the style references show the center object ({objek}) from its sheet: copy its exact shape, colors and crest."
    return p + TANPA_TEKS + _koreksi(r, fix)


def _prompt_tokoh(r, d, fix):
    pos = []
    for a in d.get("asimetris", []):
        kanan = a.get("sisi") == "kanan"
        pos.append(f"{a.get('detail')} is on the character's own {'right' if kanan else 'left'}: in the front figure it is on the {'left' if kanan else 'right'} side of the figure, "
                   f"in the back figure on the {'right' if kanan else 'left'} side, visible in the {'fourth' if kanan else 'second'} figure and hidden in the {'second' if kanan else 'fourth'}")
    return (GAYA_PEMBUKA + f"Design: {r['anchor']}\n"
            "Draw ONE character turnaround sheet: exactly four full-body figures of this SAME design standing in one row, evenly spaced, same scale, same neutral pose, "
            "on a plain light grey background, nothing else. From left to right: 1) front view facing the camera; 2) side view showing the character's LEFT side, facing the RIGHT edge "
            "of the image; 3) back view facing away from the camera; 4) side view showing the character's RIGHT side, facing the LEFT edge of the image. "
            + (f"Fixed states in all four figures: {d['tetap']} " if d.get("tetap") else "")
            + ("Asymmetric details: " + "; ".join(pos) + ". " if pos else "")
            + "Colors, proportions and accessories identical in all four; never mirror the design." + TANPA_TEKS + _koreksi(r, fix))


def _ada_pembatas(img):
    """True kalau ada garis pembatas vertikal (kolom yang hampir seragam dari atas ke bawah) di tengah gambar: tanda kolase atau triptych."""
    import numpy as np
    a = np.asarray(img.convert("L").resize((800, 340)), dtype=float)
    std = a.std(axis=0)
    return bool((std[16:-16] < 4).any())


def _juri(img, r, d, acuan):
    """Juri dengan butir yang sama seperti prompt. Arah hadap tokoh dibandingkan oleh kode, bukan oleh model."""
    if r["jenis"] == "latar" and _ada_pembatas(img):
        return False, ["gambar terpecah menjadi beberapa panel dengan garis pembatas"], "Draw one single continuous panorama with no panels, no dividing lines and no gaps."
    if r["jenis"] == "latar":
        prompt = ("You are a strict continuity supervisor for a 3D-animated series. The LAST image must be a wide wrap-around panorama of: " + r["anchor"]
                  + "\nBy design the back side is drawn complete at BOTH the left and the right edge (it is not split by a seam); this repetition is correct."
                  + "\nRequired layout: " + _tata_panorama(d)
                  + '\nAnswer JSON only: {"ok": bool, "masalah": ["<kalimat pendek bahasa Indonesia>"], "perbaikan": "<one English sentence or empty>"}. '
                  "Check each requirement one by one. " + ZONA + " Apart from the back side repeating at both edges, no landmark appears twice; "
                  "the same stylized cartoon 3D animated-film look as the reference images (not 2D, not photoreal); no text, no people"
                  + (", and the center object matches the attached object references" if acuan else "") + ". ok is true only if all hold. "
                  "Judge only what matters for continuity: a MAJOR landmark on the wrong side, a major landmark missing or duplicated, any text or letter-like glyphs "
                  "(look closely at banners, screens and signs), any eagle or national emblem, any people, robots or figures, "
                  "panels or dividing lines, or a non-3D or photoreal style. Ignore small prop details such as rust, wear, the exact pose or orientation of small loose items.")
    else:
        prompt = ("You are a strict continuity supervisor for a 3D-animated series. The LAST image must be a turnaround of four figures of: " + r["anchor"]
                  + (f"\nFixed states: {d['tetap']}" if d.get("tetap") else "")
                  + f"\nAsymmetric details (character's own side): {json.dumps(d.get('asimetris', []))}"
                  + '\nAnswer JSON only: {"ok": bool, "hadap": [4 values], "masalah": ["<kalimat pendek bahasa Indonesia>"], "perbaikan": "<one English sentence or empty>"}. '
                  '"hadap" lists, for the four figures from left to right, where each figure\'s face or front points: "camera", "away", "left" (toward the left edge of the image) '
                  'or "right" (toward the right edge of the image). ok is true only if there are exactly four figures of the same design, every fixed state and asymmetric detail '
                  "is consistent across them (judged from the character's own left and right), the style is 3D CGI animated film, and there is no text.")
    j = vertex.gen_json(prompt, images=list(acuan) + [img], model=CFG["models"]["judge"], temperature=0.0,
                        mock_value=lambda: {"ok": True, "masalah": [], "perbaikan": "", "hadap": [h for _, h in TURNAROUND]})
    ok, masalah, perbaikan = bool(j.get("ok")), j.get("masalah", []), j.get("perbaikan", "")
    if r["jenis"] != "latar":
        harap = [h for _, h in TURNAROUND]
        if j.get("hadap") == ["camera", "left", "away", "right"]:  # tampak samping tertukar: cukup tukar kolom 2 dan 4
            w4 = img.width // 4; tukar = img.copy()
            tukar.paste(img.crop((3 * w4, 0, 4 * w4, img.height)), (w4, 0)); tukar.paste(img.crop((w4, 0, 2 * w4, img.height)), (3 * w4, 0))
            img.paste(tukar); j["hadap"] = harap
        if j.get("hadap") != harap:
            ok = False; masalah = [f"arah hadap {j.get('hadap')}, seharusnya {harap}"] + masalah
            perbaikan = ("Figure order must be: front facing camera, then facing the RIGHT edge, then back facing away, then facing the LEFT edge. " + perbaikan).strip()
    return ok, masalah, perbaikan


def tampilan(pano, yaw_deg, fov_deg=100, size=(1600, 900)):
    """Potong panorama equirectangular (lebar = 360 derajat) menjadi tampilan perspektif biasa.
    yaw 0 = tengah gambar (depan), 90 = kanan, -90 = kiri. Dinding belakang digambar utuh di kedua tepi, jadi tampak belakang
    diambil dari salinan tepi kiri (yaw -152), bukan dari sambungan (yaw 180) yang memperlihatkan dua salinan."""
    import numpy as np
    src = np.asarray(pano.convert("RGB")); H, W = src.shape[:2]
    vspan = np.pi * 2 * H / W
    w, h = size; f = (w / 2) / np.tan(np.radians(fov_deg) / 2)
    xs, ys = np.meshgrid(np.arange(w) - w / 2 + 0.5, np.arange(h) - h / 2 + 0.5)
    lon = np.radians(yaw_deg) + np.arctan2(xs, f)
    lat = -np.arctan2(ys, np.hypot(xs, f))
    u = (((lon / (2 * np.pi) + 0.5) % 1.0) * W).astype(int) % W
    v = np.clip((0.5 - lat / vspan) * H, 0, H - 1).astype(int)
    return Image.fromarray(src[v, u])


def _susun(k, r, img):
    """Sheet akhir: panorama utuh + empat tampilan (latar), atau turnaround apa adanya (tokoh), plus keterangan."""
    from PIL import ImageDraw, ImageFont
    g = 16; cap = 56
    if r["jenis"] == "latar":
        views = {a: tampilan(img, yaw) for a, yaw in (("depan", 0), ("kanan", 90), ("belakang", -152), ("kiri", -90))}
        for a, v in views.items():
            v.save(ROOT / f"refs/auto/views/{k}_{a}.png")
        pw = 4 * 800 + 3 * g; ph = int(img.height * pw / img.width)
        sheet = Image.new("RGB", (pw + 2 * g, ph + 450 + 3 * g + cap), (205, 205, 205))
        sheet.paste(img.convert("RGB").resize((pw, ph)), (g, g))
        for i, a in enumerate(("kiri", "depan", "kanan", "belakang")):  # urutan sama dengan posisi di panorama
            sheet.paste(views[a].resize((800, 450)), (g + i * (800 + g), ph + 2 * g))
    else:
        sheet = Image.new("RGB", (img.width + 2 * g, img.height + 2 * g + cap), (205, 205, 205))
        sheet.paste(img.convert("RGB"), (g, g))
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
    # objek yang jadi acuan latar dibuat lebih dulu
    todo = sorted(todo, key=lambda k: k not in OBJEK_REF.values())
    log(f"Referensi yang dibuat: {len(todo)} ({', '.join(todo)})")
    (ROOT / "refs/auto/views").mkdir(parents=True, exist_ok=True)
    gaya_k = [Image.open(ROOT / refs[k]["file"]) for k in ("K01", "K03") if refs[k]["file"]]
    gaya_l = [Image.open(ROOT / refs[k]["file"]) for k in ("L01", "L02") if refs[k]["file"]]
    for k in todo:
        refs = load_refs(); r = refs[k]; latar = r["jenis"] == "latar"
        gaya = gaya_l if latar else gaya_k
        objek = OBJEK_REF.get(k) if latar else None
        acuan = [Image.open(ROOT / refs[objek]["file"])] if objek and refs[objek]["file"] else []
        d = _denah(k, r); fix = ""; best = None
        for i in range(CFG["panel"]["max_attempts"]):
            p = _prompt_latar(k, r, d, objek if acuan else None, fix) if latar else _prompt_tokoh(r, d, fix)
            img = vertex.gen_image(p, gaya + acuan, aspect="21:9")
            ok, masalah, perbaikan = _juri(img, r, d, acuan)
            if best is None or ok:
                best = (img, ok, masalah)
            if ok:
                break
            fix = perbaikan or "; ".join(masalah)
            log(f"  {k} percobaan {i + 1} gagal: {'; '.join(masalah)[:160]}")
        img, ok, masalah = best
        img.save(ROOT / f"refs/auto/views/{k}_{'panorama' if latar else 'turnaround'}.png")
        sheet = _susun(k, r, img); path = f"refs/auto/{k}.png"; sheet.save(ROOT / path)
        j = qc.juri_sheet(sheet, r, gaya) if ok else {"lolos": False, "skor": 0, "gagal": ["kontinuitas"], "masalah": masalah, "perbaikan": ""}
        asal = r.get("catatan_asal") or r["catatan"]
        r.update(file=path, lolos=False, sumber="auto", qc=j, catatan_asal=asal,
                 catatan="Lolos QC model, menunggu persetujuan manusia" if j["lolos"] else "GAGAL QC: " + "; ".join(j["masalah"])[:200])
        save_refs(refs)
        log(f"  {k} {r['nama']}: {'lolos QC, menunggu persetujuan' if j['lolos'] else 'GAGAL QC'} (skor {j['skor']})")
    kontak()
    return False
