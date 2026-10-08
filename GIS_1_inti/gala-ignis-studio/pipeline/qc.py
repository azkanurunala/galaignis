"""Pemeriksaan mutu: aturan lokal yang pasti, lalu juri model yang melihat gambar."""
import re
from PIL import Image
import numpy as np
from .common import CFG, log
from . import vertex

KRITIS = ["satu_panel", "tanpa_teks", "bukan_sheet", "gaya_3d", "adegan_sesuai", "tokoh_sesuai", "latar_sesuai",
          "mata_gala_tertutup", "ethylene_tanpa_mulut", "anatomi_wajar"]

RUBRIK = """You are a strict quality inspector for a 3D-animated children's comic. The LAST image is the panel to judge.
The images before it are the reference sheets it must match: {labels}.
Intended shot: {shot}. Intended scene: {scene}

Answer with JSON only, in this exact shape:
{{"cek": {{"satu_panel": bool, "tanpa_teks": bool, "bukan_sheet": bool, "gaya_3d": bool, "adegan_sesuai": bool,
"tokoh_sesuai": bool, "latar_sesuai": bool, "mata_gala_tertutup": bool, "ethylene_tanpa_mulut": bool, "anatomi_wajar": bool}},
"skor": 0-10, "masalah": ["<kalimat pendek bahasa Indonesia>"], "perbaikan": "<one English sentence telling the image model what to fix, or empty>"}}

Meaning of each check (true = good):
- satu_panel: one single picture, not a page with several panels or borders.
- tanpa_teks: no letters, captions, speech bubbles, labels, watermark or logo anywhere.
- bukan_sheet: it is a scene, not a reference-sheet layout (no multiple views of one character, no grey sheet background, no caption strip).
- gaya_3d: 3D CGI animated-film render, not 2D drawing, anime, or cel shading.
- adegan_sesuai: the action, the characters present and the camera shot match the intended scene.
- tokoh_sesuai: every character shown matches its sheet (hair, colors, outfit, proportions, accessories). True if no sheet applies.
- latar_sesuai: the place matches the environment sheet. True if no environment sheet was given.
- mata_gala_tertutup: Gala's goggles are on and opaque; his eyes are not visible. True if Gala is absent or seen from behind.
- ethylene_tanpa_mulut: the fire sprite has no mouth and no limbs. True if the sprite is absent.
- anatomi_wajar: no extra or missing limbs, no fused or badly distorted hands or faces.
Be strict about what matters to the viewer: Gala's eyes, text, the sprite's mouth, anatomy, a character's main design (hair color, outfit, colors,
key accessories), the place's main landmarks and their positions (doors, windows, large props on the correct side), and the main action.
Do NOT fail a panel for small details a viewer would not notice: the exact number of sides or lines in a floor pattern, the exact shape of a
light fixture, slight color shade differences, small trim patterns, or a camera angle that is close to the intended one. If unsure about a major
point, answer false and explain in masalah."""


def lokal(img, aspect):
    """Cek tanpa model: ukuran, rasio, gambar kosong, bingkai abu-abu khas sheet."""
    out = []
    a, b = (int(x) for x in aspect.split(":")); w, h = img.size
    if min(w, h) < 700:
        out.append(f"resolusi terlalu kecil ({w}x{h})")
    if abs(w / h - a / b) > 0.04:
        out.append(f"rasio {w}x{h} tidak sesuai {aspect}")
    arr = np.asarray(img.convert("L").resize((64, 64)), dtype=np.float32)
    if arr.std() < 6:
        out.append("gambar hampir polos")
    edge = np.concatenate([arr[0], arr[-1], arr[:, 0], arr[:, -1]])
    if edge.std() < 3 and abs(edge.mean() - arr[8:-8, 8:-8].mean()) > 25:
        out.append("ada bingkai polos di tepi gambar")
    return out


def ahash(img):
    a = np.asarray(img.convert("L").resize((16, 16)), dtype=np.float32)
    return (a > a.mean()).flatten()


def mirip(img1, img2):
    return float((ahash(img1) == ahash(img2)).mean())


def juri_panel(img, frame, ref_imgs, labels):
    def tiruan():
        return {"cek": {k: True for k in KRITIS}, "skor": 8, "masalah": [], "perbaikan": ""}
    r = vertex.gen_json(RUBRIK.format(labels="; ".join(labels) or "none", shot=frame["shot"], scene=frame["scene"]),
                        images=list(ref_imgs) + [img], model=CFG["models"]["judge"], temperature=0.0, mock_value=tiruan)
    cek = r.get("cek", {}); gagal = [k for k in KRITIS if cek.get(k) is not True]
    skor = float(r.get("skor", 0))
    lolos = not gagal and skor >= CFG["qc"]["min_skor"]
    return {"lolos": lolos, "skor": skor, "gagal": gagal, "masalah": r.get("masalah", []), "perbaikan": r.get("perbaikan", "")}


SHEET_RUBRIK = """You are a strict inspector of reference sheets for a 3D-animated children's series. The LAST image is the sheet to judge.
{extra}It must show exactly this design: {anchor}
Answer with JSON only: {{"cek": {{"sesuai_deskripsi": bool, "gaya_3d": bool, "tanpa_teks_liar": bool, "bersih": bool}},
"skor": 0-10, "masalah": ["<kalimat pendek bahasa Indonesia>"], "perbaikan": "<one English sentence, or empty>"}}
- sesuai_deskripsi: every stated feature is present and nothing contradicts the description.{note}
- gaya_3d: 3D CGI animated-film render, not 2D.
- tanpa_teks_liar: no text except at most one small caption.
- bersih: no distorted anatomy, no duplicated or garbled elements."""

KONTINUITAS = {
    "latar": ("\n- kontinuitas: the views are different camera directions inside ONE consistent space and together cover the whole location "
              "(front view and reverse/back view, left side and right side). Map every landmark (doors, windows, large props, openings, light sources) across the views: "
              "each keeps the same position relative to the others, what lies behind the camera in one view appears ONLY in the opposite view, left and right views agree "
              "with the front and back views, nothing appears, disappears, moves or changes shape between views. Near-duplicate angles of the same side fail."),
    "karakter": ("\n- kontinuitas: the front, back, left-side and right-side views (and close-ups) show exactly the same character or object. Every asymmetric detail "
                 "(hair parting or bangs, scars, pins, badges, cloth wrapped on one arm, weapon hand, emblems, stripes) stays on the same side of the body, judged from the "
                 "character's own left and right, and is hidden or visible consistently with each view's direction. Colors, proportions, accessories and their count are identical "
                 "in every view; nothing appears, disappears or moves between views."),
}


def juri_sheet(img, ref, style_imgs):
    def tiruan():
        return {"cek": {"sesuai_deskripsi": True, "gaya_3d": True, "tanpa_teks_liar": True, "bersih": True}, "skor": 8, "masalah": [], "perbaikan": ""}
    note = ""
    asal = ref.get("catatan_asal") or ref["catatan"]
    if asal.startswith("BELUM"):
        note = " The earlier version failed for this reason, which must now be fixed: " + asal
    extra = "The images before it show the approved house style. " if style_imgs else ""
    rubrik = SHEET_RUBRIK.format(anchor=ref["anchor"], note=note, extra=extra); n_cek = 4
    if ref.get("jenis") in KONTINUITAS:
        rubrik = rubrik.replace('"bersih": bool}', '"bersih": bool, "kontinuitas": bool}') + KONTINUITAS[ref["jenis"]]; n_cek = 5
    r = vertex.gen_json(rubrik, images=list(style_imgs) + [img],
                        model=CFG["models"]["judge"], temperature=0.0, mock_value=tiruan)
    cek = r.get("cek", {}); gagal = [k for k, v in cek.items() if v is not True]
    skor = float(r.get("skor", 0))
    return {"lolos": not gagal and len(cek) == n_cek and skor >= CFG["qc"]["min_skor"], "skor": skor, "gagal": gagal,
            "masalah": r.get("masalah", []), "perbaikan": r.get("perbaikan", "")}


# ---------- naskah
NAMA_SPRITE = ("ethylene",)


def lint_naskah(script, kode_wajib, perlu_gagal):
    """Aturan pasti untuk narasi dan dialog. Mengembalikan daftar masalah."""
    out = []; fr = script.get("frames", {})
    for k in kode_wajib:
        if k not in fr:
            out.append(f"{k}: tidak ada di naskah")
    if perlu_gagal:
        g = script.get("gagal") or {}
        if not g.get("scene_en"):
            out.append("gagal.scene_en kosong")
        elif re.search(r"Gala", g["scene_en"]) and re.search(r"(her|she|herself)", g["scene_en"], re.I):
            out.append("gagal.scene_en: Gala laki-laki, pakai he/his/himself (kalau yang dimaksud tokoh perempuan lain, sebut namanya)")
        fr = dict(fr, **{"gagal": g})
    titik3 = 0; kosong = 0; n_nar = 0
    for k, v in fr.items():
        nar = (v.get("narasi") or "").strip(); dlg = v.get("dialog") or []
        teks = [nar] + [d.get("teks", "") for d in dlg]
        if not nar and not dlg and not (v.get("sfx") or "").strip():
            kosong += 1
        if len(nar) > 70:
            out.append(f"{k}: kotak keterangan {len(nar)} huruf, maksimum 60")
        n_nar = n_nar + 1 if nar else n_nar
        if len(dlg) > 2:
            out.append(f"{k}: {len(dlg)} dialog, maksimum 2")
        if sum(len(t.split()) for t in teks) > 26:
            out.append(f"{k}: lebih dari 24 kata")
        for d in dlg:
            t = d.get("teks", "")
            if len(t) > 70:
                out.append(f"{k}: dialog {len(t)} huruf, maksimum 70")
            if d.get("tokoh", "").lower().startswith(NAMA_SPRITE) and (" " in t.strip() or len(t.strip()) > 8):
                out.append(f"{k}: Ethylene tidak berbicara dengan kata-kata, hanya bunyi pendek seperti Pip!")
            if not d.get("tokoh"):
                out.append(f"{k}: dialog tanpa nama tokoh")
        for t in teks:
            if "—" in t or "–" in t:
                out.append(f"{k}: memakai tanda pisah panjang")
            titik3 += t.count("...") + t.count("…")
        sfx = v.get("sfx") or ""
        if len(sfx) > 14:
            out.append(f"{k}: SFX terlalu panjang")
    if titik3 > 2:
        out.append(f"titik tiga dipakai {titik3} kali, maksimum 2 per episode")
    if kosong > 4:
        out.append(f"{kosong} frame tanpa teks dan tanpa SFX, maksimum 4")
    if n_nar > 5:
        out.append(f"kotak keterangan dipakai di {n_nar} frame, maksimum 4; cerita harus lewat dialog")
    return out


JURI_NASKAH = """Kamu editor naskah yang keras untuk komik anak berbahasa Indonesia. Nilai naskah balon percakapan di bawah (tanpa narator; "narasi" hanyalah kotak keterangan tempat dan waktu).
Judul: {judul}
Gagasan inti episode: {gagasan}
Ketukan gagal yang wajib terasa: {gagal}
Naskah (per kode frame, dengan deskripsi adegan):
{isi}

Jawab JSON saja: {{"cek": {{"gagasan_terlihat": bool, "gagal_terasa": bool, "tidak_generik": bool, "penutur_ada_di_frame": bool,
"sesuai_adegan": bool, "bahasa_anak": bool}}, "masalah": ["<kode frame>: <kalimat>"]}}
- gagasan_terlihat: gagasan inti diucapkan atau diperlihatkan dengan kata-kata sederhana di sekitar puncak episode.
- gagal_terasa: pembaca paham tokoh mencoba cara yang salah dulu, lalu berhasil karena gagasan inti.
- tidak_generik: tidak ada kalimat pahlawan yang bisa dipindah ke episode lain tanpa berubah.
- penutur_ada_di_frame: setiap penutur dialog memang ada di adegan frame itu.
- sesuai_adegan: teks tidak bertentangan dengan deskripsi adegan dan tidak sekadar mengulang apa yang sudah terlihat.
- bahasa_anak: kalimat pendek, kata sehari-hari, bisa dipahami anak 8 tahun.
Kalau ragu, jawab false dan jelaskan."""


def juri_naskah(ep, script, frames):
    isi = []
    for f in frames:
        v = script["frames"].get(f["kode"], {}) if not f.get("tambahan") else script.get("gagal", {})
        d = " | ".join(f"{x.get('tokoh')}: {x.get('teks')}" for x in v.get("dialog") or [])
        isi.append(f"{f['kode']} [{f['id']}] narasi: {v.get('narasi', '')} dialog: {d} sfx: {v.get('sfx', '')}")
    g = ep["gagal"]; gt = g.get("ketukan") or f"sudah ada di frame {g.get('frame')}"
    r = vertex.gen_json(JURI_NASKAH.format(judul=ep["judul"], gagasan=ep["gagasan"]["teks"], gagal=gt, isi="\n".join(isi)),
                        model=CFG["models"]["judge"], temperature=0.0,
                        mock_value={"cek": {k: True for k in ("gagasan_terlihat", "gagal_terasa", "tidak_generik", "penutur_ada_di_frame", "sesuai_adegan", "bahasa_anak")}, "masalah": []})
    cek = r.get("cek", {}); gagal = [k for k, v in cek.items() if v is not True]
    return {"lolos": not gagal and len(cek) == 6, "gagal": gagal, "masalah": r.get("masalah", [])}


# ---------- balon, video, klip bergerak
def _juri(prompt, images, kunci):
    r = vertex.gen_json(prompt, images=images, model=CFG["models"]["judge"], temperature=0.0,
                        mock_value={"cek": {k: True for k in kunci}, "masalah": [], "perbaikan": ""})
    cek = r.get("cek", {}); gagal = [k for k in kunci if cek.get(k) is not True]
    return {"lolos": not gagal, "gagal": gagal, "masalah": r.get("masalah", []), "perbaikan": r.get("perbaikan", "")}


BALON = """You inspect the lettering of ONE comic panel (the image). Lettering on it: {daftar}
Answer with JSON only: {{"cek": {{"wajah_terlihat": bool, "aksi_terlihat": bool, "ekor_benar": bool, "teks_terbaca": bool, "tidak_bertumpuk": bool}},
"masalah": ["<kalimat pendek bahasa Indonesia>"], "perbaikan": "<one English sentence: where each wrong box should move, or empty>"}}
- wajah_terlihat: no balloon, caption or sound-effect word covers any character's face or head.
- aksi_terlihat: the key action or object of the panel is not hidden by lettering.
- ekor_benar: every speech balloon's tail points toward the character who is speaking (speaker names are listed); true if a speaker is not visible or there is no speech.
- teks_terbaca: every word is complete, inside its box, and not cut by the image edge.
- tidak_bertumpuk: boxes and the sound-effect word do not overlap each other.
Be strict: if unsure, answer false and explain."""


def juri_balon(img, blocks, sfx):
    daftar = "; ".join(f"{'caption' if j == 'narasi' else 'speech by ' + (n or 'unknown')}: {t}" for j, n, t in blocks) + (f"; sound effect: {sfx}" if sfx else "")
    return _juri(BALON.format(daftar=daftar or "none"), [img], ["wajah_terlihat", "aksi_terlihat", "ekor_benar", "teks_terbaca", "tidak_bertumpuk"])


VIDEO = """These {n} images are frames taken in order from one vertical comic video for children (opening title, middle, closing card).
Answer with JSON only: {{"cek": {{"judul_terbaca": bool, "judul_tidak_menutup_wajah": bool, "teks_utuh": bool, "tanpa_cacat": bool, "penutup_terbaca": bool}},
"masalah": ["<kalimat pendek bahasa Indonesia, sebut bingkai ke berapa>"]}}
- judul_terbaca: the big title in the first frame is fully readable and not cut off.
- judul_tidak_menutup_wajah: the title does not cover a character's face.
- teks_utuh: in the middle frames, every balloon and caption is complete and readable, nothing cut by the panel edge.
- tanpa_cacat: no broken rendering: no blank or black panel, no garbled picture, no stray debug text.
- penutup_terbaca: the closing card text in the last frame is fully readable.
Be strict: if unsure, answer false and explain."""


def juri_video(frames):
    return _juri(VIDEO.format(n=len(frames)), frames, ["judul_terbaca", "judul_tidak_menutup_wajah", "teks_utuh", "tanpa_cacat", "penutup_terbaca"])


VEO = """The FIRST image is the approved still panel. The other images are frames (start, middle, end) from a short video animated from it.
Answer with JSON only: {{"cek": {{"desain_tetap": bool, "tanpa_teks": bool, "tanpa_distorsi": bool, "mata_gala_tertutup": bool, "adegan_sama": bool}},
"masalah": ["<kalimat pendek bahasa Indonesia>"]}}
- desain_tetap: every character keeps the same design as in the still in all frames (hair, colors, outfit, proportions, accessories).
- tanpa_teks: no letters, subtitles, logos or watermark appear.
- tanpa_distorsi: no melted faces, extra limbs, morphing bodies or broken hands in any frame.
- mata_gala_tertutup: if the goggle-wearing boy is present, his goggles stay on and opaque in all frames; true if absent.
- adegan_sama: it is still the same place and moment; no new characters or objects appear.
Be strict: if unsure, answer false and explain."""


def juri_veo(panel, frames):
    return _juri(VEO, [panel] + list(frames), ["desain_tetap", "tanpa_teks", "tanpa_distorsi", "mata_gala_tertutup", "adegan_sama"])
