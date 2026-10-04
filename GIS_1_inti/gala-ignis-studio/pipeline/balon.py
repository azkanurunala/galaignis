"""Balon percakapan, kotak keterangan dan SFX di dalam panel, seperti komik Episode 1.

Posisi tiap balon ditentukan model yang melihat panelnya (supaya tidak menutup wajah dan ekornya mengarah ke penutur).
Kalau model tidak tersedia atau jawabannya tidak masuk akal, dipakai posisi cadangan di tepi atas dan bawah panel.
"""
import math
from PIL import Image, ImageDraw, ImageFont
from .common import CFG, ROOT
from . import vertex

BODY = str(ROOT / "assets/fonts/comic-neue-latin-700-normal.woff")
SFXF = str(ROOT / "assets/fonts/bangers-latin-400-normal.woff")
S = 3            # supersampling
TEPI = 0.055     # jarak aman dari tepi panel (bagian tepi terpotong saat kamera masuk)

PROMPT = """This is one comic panel (image). I need to place lettering on it without covering faces, hands or the key action.
Text boxes to place, each with its size as a fraction of image width and height:
{daftar}
Answer with JSON only: {{"teks": [{{"i": <index>, "cx": <0-1>, "cy": <0-1>, "mulut": [<x 0-1>, <y 0-1>] or null}}], "sfx": [<x>, <y>] or null}}
- cx, cy: center of the box. Keep every box fully inside the image with a 6 percent margin, and do not let boxes overlap each other.
- Captions (jenis narasi) go in a top corner or along the top edge. Speech (jenis dialog) goes near its speaker but beside or above the head, never on the face.
- mulut: for speech, the position of the speaker's mouth in the image, so the balloon tail can point at it; null if the speaker is not visible. For captions use null.
- sfx: center for a large sound-effect word near the source of the sound, away from faces and from the boxes; null if no sound effect is listed.
Coordinates are fractions: x from the left edge, y from the top edge."""


def _wrap(dr, text, f, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if dr.textlength(t, font=f) <= width or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + ([cur] if cur else [])


def ukur(blocks, w, h):
    """Menghitung baris dan ukuran tiap kotak. Dialog dibuat agak sempit supaya balonnya membulat."""
    dr = ImageDraw.Draw(Image.new("RGB", (8, 8))); out = []
    size = max(26, int(w * 0.036)); f = ImageFont.truetype(BODY, size); lh = int(size * 1.16)
    for jenis, nama, teks in blocks:
        maxw = w * (0.46 if jenis == "narasi" else 0.36)
        lines = _wrap(dr, teks, f, maxw)
        tw = max(dr.textlength(l, font=f) for l in lines); th = len(lines) * lh
        px, py = (size * 0.6, size * 0.45) if jenis == "narasi" else (size * 1.0, size * 0.8)
        out.append({"jenis": jenis, "nama": nama, "lines": lines, "bw": tw + 2 * px, "bh": th + 2 * py, "size": size, "lh": lh})
    return out


def cadangan(kotak, w, h, sfx):
    """Posisi cadangan: keterangan kiri atas, dialog pertama kanan atas (turun kalau bertabrakan), dialog kedua kiri bawah.
    Ekor pendek mengarah ke tengah panel karena posisi penutur tidak diketahui."""
    m = TEPI; pos = []; y_kiri = m * h; n_dialog = 0; lebar_kiri = 0
    for k in kotak:
        if k["jenis"] == "narasi":
            pos.append({"cx": m * w + k["bw"] / 2, "cy": y_kiri + k["bh"] / 2, "mulut": None}); y_kiri += k["bh"] + 16; lebar_kiri = max(lebar_kiri, k["bw"])
        elif n_dialog == 0:
            rx = k["bw"] * 0.54; ry = k["bh"] * 0.56
            y = m * h + ry if lebar_kiri + 2 * rx + 24 < w * (1 - 2 * m) else y_kiri + ry
            cx = w - m * w - rx
            pos.append({"cx": cx, "cy": y, "mulut": (cx - rx * 0.3, y + ry + k["size"] * 2.2)}); n_dialog += 1
        else:
            rx = k["bw"] * 0.54; ry = k["bh"] * 0.56; cx = m * w + rx; y = h - m * h - ry
            pos.append({"cx": cx, "cy": y, "mulut": (cx + rx * 0.3, y - ry - k["size"] * 2.2)}); n_dialog += 1
    return pos, ((w * 0.5, h * 0.56) if sfx else None)


def _tabrak(a, b, ka, kb):
    return abs(a["cx"] - b["cx"]) < (ka["bw"] + kb["bw"]) / 2 + 6 and abs(a["cy"] - b["cy"]) < (ka["bh"] + kb["bh"]) / 2 + 6


def tata(img, kotak, sfx, perbaikan=""):
    """Meminta posisi ke model; memvalidasi; kembali ke cadangan kalau tidak sah."""
    w, h = img.size; cad, cad_sfx = cadangan(kotak, w, h, sfx)
    if not kotak and not sfx:
        return [], None
    daftar = "\n".join(f"{i}: jenis {k['jenis']}, speaker {k['nama'] or '-'}, width {k['bw'] / w:.2f}, height {k['bh'] / h:.2f}, text: {' '.join(k['lines'])}" for i, k in enumerate(kotak))
    if sfx:
        daftar += f"\nSound effect word: {sfx}"
    try:
        if perbaikan:
            daftar += "\nA previous placement was rejected. Fix this: " + perbaikan
        r = vertex.gen_json(PROMPT.format(daftar=daftar or "(none)"), images=[img], model=CFG["models"]["judge"], temperature=0.0, mock_value=None)
    except Exception:
        r = None
    if not r:
        return cad, cad_sfx
    pos = list(cad)
    for t in r.get("teks") or []:
        try:
            i = int(t["i"]); k = kotak[i]
            cx = min(max(float(t["cx"]) * w, TEPI * w + k["bw"] / 2), w - TEPI * w - k["bw"] / 2)
            cy = min(max(float(t["cy"]) * h, TEPI * h + k["bh"] / 2), h - TEPI * h - k["bh"] / 2)
            m = t.get("mulut"); m = (float(m[0]) * w, float(m[1]) * h) if m and k["jenis"] == "dialog" else None
            pos[i] = {"cx": cx, "cy": cy, "mulut": m}
        except (KeyError, ValueError, TypeError, IndexError):
            continue
    if any(_tabrak(pos[i], pos[j], kotak[i], kotak[j]) for i in range(len(pos)) for j in range(i)):
        return cad, cad_sfx
    s = r.get("sfx")
    try:
        ps = (min(max(float(s[0]), 0.2), 0.8) * w, min(max(float(s[1]), 0.12), 0.88) * h) if s and sfx else cad_sfx
    except (ValueError, TypeError, IndexError):
        ps = cad_sfx
    return pos, ps


def _balon(d, T, k, p, lw):
    cx, cy = p["cx"], p["cy"]; rx, ry = k["bw"] / 2 * 1.08, k["bh"] / 2 * 1.12; tail = p["mulut"]
    if tail:  # ekor pendek: keluar dari tepi balon paling jauh dua tinggi huruf, dan berhenti sebelum mulut
        dx, dy = tail[0] - cx, tail[1] - cy; L = math.hypot(dx, dy) or 1; c, sn = dx / L, dy / L
        tepi = 1 / math.sqrt((c / rx) ** 2 + (sn / ry) ** 2)
        if L <= tepi + 6:
            tail = None
        else:
            pj = min(tepi + (L - tepi) * 0.8, tepi + k["size"] * 2.0); tail = (cx + c * pj, cy + sn * pj)

    def bentuk(grow, fill):
        d.ellipse([T((cx - rx - grow, cy - ry - grow)), T((cx + rx + grow, cy + ry + grow))], fill=fill)
        if tail:
            ang = math.atan2(tail[1] - cy, tail[0] - cx); b = 0.26
            b1 = (cx + (rx + grow) * 0.86 * math.cos(ang - b), cy + (ry + grow) * 0.86 * math.sin(ang - b))
            b2 = (cx + (rx + grow) * 0.86 * math.cos(ang + b), cy + (ry + grow) * 0.86 * math.sin(ang + b))
            tip = tail if grow > 0 else (tail[0] - lw * 1.8 * math.cos(ang), tail[1] - lw * 1.8 * math.sin(ang))
            d.polygon([T(b1), T(tip), T(b2)], fill=fill)
    bentuk(lw, (20, 16, 14)); bentuk(0, (255, 255, 255))


def gambar(panel, blocks, sfx="", posisi=None, perbaikan=""):
    """Mengembalikan (panel berteks, posisi yang dipakai). posisi boleh diisi dari hasil sebelumnya."""
    img = panel.convert("RGB"); w, h = img.size; kotak = ukur(blocks, w, h)
    if posisi and len(posisi.get("teks", [])) == len(kotak):
        pos = [{"cx": p["cx"] * w, "cy": p["cy"] * h, "mulut": (p["mulut"][0] * w, p["mulut"][1] * h) if p.get("mulut") else None} for p in posisi["teks"]]
        ps = (posisi["sfx"][0] * w, posisi["sfx"][1] * h) if posisi.get("sfx") and sfx else None
    else:
        pos, ps = tata(img, kotak, sfx, perbaikan)
    ov = Image.new("RGBA", (w * S, h * S), (0, 0, 0, 0)); d = ImageDraw.Draw(ov); T = lambda p: (p[0] * S, p[1] * S)
    lw = max(3, w // 320)
    if sfx and ps:
        f = ImageFont.truetype(SFXF, int(w * 0.15) * S)
        while d.textlength(sfx.upper(), font=f) > w * 0.62 * S and f.size > 40 * S:
            f = ImageFont.truetype(SFXF, f.size - 6 * S)
        lay = Image.new("RGBA", (int(w * 0.7) * S, int(f.size * 1.5)), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.text((lay.width // 2, lay.height // 2), sfx.upper(), font=f, fill=(255, 225, 77), anchor="mm", stroke_width=f.size // 13, stroke_fill=(20, 12, 10))
        lay = lay.rotate(8, resample=Image.BICUBIC, expand=True)
        x = int(min(max(ps[0] * S - lay.width / 2, TEPI * w * S), (w - TEPI * w) * S - lay.width)); y = int(min(max(ps[1] * S - lay.height / 2, 0), h * S - lay.height))
        ov.alpha_composite(lay, (x, y))
    for k, p in zip(kotak, pos):
        f = ImageFont.truetype(BODY, k["size"] * S)
        if k["jenis"] == "narasi":
            x0, y0 = p["cx"] - k["bw"] / 2, p["cy"] - k["bh"] / 2
            d.rectangle([T((x0, y0)), T((x0 + k["bw"], y0 + k["bh"]))], fill=(255, 244, 190), outline=(20, 16, 14), width=lw * S)
        else:
            _balon(d, T, k, p, lw)
        for i, ln in enumerate(k["lines"]):
            yy = p["cy"] + (i - (len(k["lines"]) - 1) / 2) * k["lh"]
            d.text(T((p["cx"], yy)), ln, font=f, fill=(20, 16, 14), anchor="mm")
    ov = ov.resize((w, h), Image.LANCZOS); out = img.convert("RGBA"); out.alpha_composite(ov)
    simpan = {"teks": [{"cx": p["cx"] / w, "cy": p["cy"] / h, "mulut": [p["mulut"][0] / w, p["mulut"][1] / h] if p["mulut"] else None} for p in pos],
              "sfx": [ps[0] / w, ps[1] / h] if ps else None}
    return out.convert("RGB"), simpan
