"""Tahap video: menyusun panel menjadi video komik vertikal per sub-episode, dengan teks, gerak kamera pelan, dan suara narator."""
import json, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from .common import CFG, ROOT, log, episodes, ep_dir, read_json, write_json, frames_final
from . import vertex, musik, balon, qc

BODY = str(ROOT / "assets/fonts/comic-neue-latin-700-normal.woff")
SFXF = str(ROOT / "assets/fonts/bangers-latin-400-normal.woff")
BG, INK, PAPER, AMBER, CREAM, NAME = (26, 20, 16), (29, 23, 18), (255, 244, 207), (242, 169, 59), (255, 240, 214), (166, 74, 20)
V = CFG["video"]; W, H = V["w"], V["h"]
PANEL_H = 1350; PANEL_Y = (H - PANEL_H) // 2      # panel 4:5 di tengah; pita hitam bawah adalah area antarmuka Shorts
HEAD_H, BAND_Y = PANEL_Y - 4, PANEL_Y; PAD = 40; RATE = 24000


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(dr, text, f, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if dr.textlength(t, font=f) <= width or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def layout(dr, blocks, size):
    """blocks: [(jenis, nama, teks)]. Mengembalikan (tinggi total, daftar kotak) untuk ukuran huruf tertentu."""
    f = font(BODY, size); lh = int(size * 1.22); px, py = 26, 18; gap = 16; out = []; y = 0
    for jenis, nama, teks in blocks:
        t = (nama + ": " if nama else "") + teks
        lines = wrap(dr, t, f, W - 2 * PAD - 2 * px)
        h = len(lines) * lh + 2 * py
        out.append((jenis, nama, lines, y, h)); y += h + gap
    return y - gap if out else 0, out, f, lh, px, py


def draw_band(img, label, judul, blocks):
    dr = ImageDraw.Draw(img)
    dr.text((PAD, HEAD_H - 22), label, font=font(SFXF, 58), fill=AMBER, anchor="ls")
    lw = dr.textlength(label, font=font(SFXF, 58))
    jf = font(BODY, 32); j = judul
    while dr.textlength(j, font=jf) > W - 2 * PAD - lw - 28 and len(j) > 8:
        j = j[:-2]
    dr.text((PAD + lw + 28, HEAD_H - 24), j if j == judul else j.rstrip() + ".", font=jf, fill=CREAM, anchor="ls")
    if not blocks:
        return
    avail = PANEL_Y - BAND_Y - 36
    for size in range(46, 25, -2):
        total, boxes, f, lh, px, py = layout(dr, blocks, size)
        if total <= avail:
            break
    y0 = BAND_Y + 12 + max(0, (avail - total) // 2)
    for jenis, nama, lines, y, h in boxes:
        box = [PAD, y0 + y, W - PAD, y0 + y + h]
        if jenis == "narasi":
            dr.rectangle(box, fill=PAPER, outline=INK, width=4)
        else:
            dr.rounded_rectangle(box, radius=26, fill=(255, 255, 255), outline=INK, width=4)
        ty = y0 + y + py
        for i, ln in enumerate(lines):
            x = PAD + px
            if i == 0 and nama:
                dr.text((x, ty), nama + ":", font=f, fill=NAME); x += dr.textlength(nama + ": ", font=f); ln = ln[len(nama) + 2:]
            dr.text((x, ty), ln, font=f, fill=INK); ty += lh


def draw_sfx(panel_rgba, text):
    f = font(SFXF, 150); tmp = Image.new("RGBA", (900, 260), (0, 0, 0, 0)); d = ImageDraw.Draw(tmp)
    while d.textlength(text, font=f) > 820:
        f = font(SFXF, f.size - 10)
    d.text((450, 130), text, font=f, fill=(255, 225, 77), stroke_width=9, stroke_fill=(20, 12, 10), anchor="mm")
    tmp = tmp.rotate(8, resample=Image.BICUBIC, expand=True)
    bb = tmp.getbbox(); tmp = tmp.crop(bb)
    panel_rgba.alpha_composite(tmp, (W - tmp.width - 36, 36))


def slide(panel_path, label, judul, blocks, sfx="", tata=None, kode=""):
    """Mengembalikan (kanvas statis, panel berbalon yang diperbesar untuk gerak kamera, None).
    tata: kamus tembolok posisi balon per kode frame; diisi di sini."""
    canvas = Image.new("RGB", (W, H), (10, 8, 7))
    draw_band(canvas, label, judul, [])
    z = 1 + V["zoom"]; bw, bh = int(W * z), int(PANEL_H * z)
    src = Image.open(panel_path).convert("RGB"); sw, sh = src.size; tr = bw / bh
    if sw / sh > tr:
        nw = int(sh * tr); src = src.crop(((sw - nw) // 2, 0, (sw - nw) // 2 + nw, sh))
    else:
        nh = int(sw / tr); src = src.crop((0, 0, sw, nh))  # potong dari bawah, kepala tokoh aman
    base = src.resize((bw, bh), Image.LANCZOS)
    kunci = repr((blocks, sfx, int(panel_path.stat().st_mtime) if hasattr(panel_path, "stat") else 0))
    lama = (tata or {}).get(kode, {}); polos = base
    if lama.get("kunci") == kunci and lama.get("qc", {}).get("lolos"):
        base, posisi = balon.gambar(polos, blocks, sfx, lama["posisi"]); j = lama["qc"]
    else:  # tata letak baru: diperiksa juri, diulang dengan catatan perbaikan sampai tiga kali
        fix = ""; terbaik = None
        for i in range(3 if (blocks or sfx) else 1):
            img, posisi = balon.gambar(polos, blocks, sfx, None, fix)
            j = qc.juri_balon(img, blocks, sfx) if (blocks or sfx) else {"lolos": True, "gagal": [], "masalah": []}
            j["percobaan"] = i + 1
            if terbaik is None or (j["lolos"], -len(j["gagal"])) > (terbaik[2]["lolos"], -len(terbaik[2]["gagal"])):
                terbaik = (img, posisi, j)
            if j["lolos"]:
                break
            fix = j.get("perbaikan") or "; ".join(map(str, j["masalah"]))
        base, posisi, j = terbaik
    if tata is not None and kode:
        tata[kode] = {"kunci": kunci, "posisi": posisi, "qc": j}
    return canvas, base, None


def frame_at(canvas, base, over, t, arah, geser=(0, 0), tambah=0.0):
    """t dari 0 ke 1. Kamera masuk pelan sambil bergeser sedikit; geser = guncangan, tambah = hentakan zoom."""
    bw, bh = base.size; e = t * t * (3 - 2 * t); s = 1 + V["zoom"] * e + tambah + 0.02
    cw, ch = bw / s, bh / s; mx, my = bw - cw, bh - ch
    x0 = min(max(0, mx / 2 + arah[0] * e * mx / 2 * 0.6 + geser[0]), mx); y0 = min(max(0, my / 2 + arah[1] * e * my / 2 * 0.6 + geser[1]), my)
    p = base.resize((W, PANEL_H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
    if over is not None:
        p = p.convert("RGBA"); p.alpha_composite(over); p = p.convert("RGB")
    out = canvas.copy(); out.paste(p, (0, PANEL_Y)); return out


def speech(d, kode, text, state):
    """PCM narator untuk satu frame, disimpan di audio/KODE.wav. Bila suara gagal, lanjut tanpa suara."""
    if not V["narasi_suara"] or not text.strip() or state.get("mati"):
        return np.zeros(0, np.int16)
    p = d / "audio" / f"{kode}.wav"; tp = d / "audio" / f"{kode}.txt"
    if p.exists() and tp.exists() and tp.read_text(encoding="utf-8") == text:
        with wave.open(str(p)) as w:
            return np.frombuffer(w.readframes(w.getnframes()), np.int16)
    try:
        pcm, rate = vertex.tts(text)
    except Exception as e:
        log(f"  Suara narator tidak tersedia ({str(e)[:140]}). Video dilanjutkan tanpa suara."); state["mati"] = True
        return np.zeros(0, np.int16)
    a = np.frombuffer(pcm, np.int16)
    if rate != RATE:
        a = np.interp(np.linspace(0, len(a), int(len(a) * RATE / rate), endpoint=False), np.arange(len(a)), a).astype(np.int16)
    with wave.open(str(p), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(a.tobytes())
    tp.write_text(text, encoding="utf-8")
    return a


def blocks_of(v):
    b = []
    if (v.get("narasi") or "").strip():
        b.append(("narasi", "", v["narasi"].strip()))
    for x in v.get("dialog") or []:
        if x.get("teks"):
            b.append(("dialog", x.get("tokoh", ""), x["teks"].strip()))
    return b


KATA_AKSI = ("explo", "blast", "kick", "punch", "shatter", "slam", "strike", "crash", "burst", "charge", "attack", "dodge", "leap", "roar",
             "shockwave", "collaps", "beam", "slash", "erupt", "smash", "fires ", "hurl", "impact", "action")


def kekuatan(f, sfx):
    """0 sampai 1: seberapa keras frame ini diperlakukan (guncangan, kilat, musik)."""
    t = (f["scene"] + " " + f["shot"]).lower()
    return min(1.0, 0.22 * sum(k in t for k in KATA_AKSI) + (0.4 if sfx else 0.0))


def penuh(panel_path, z=1.14):
    """Panel dipotong memenuhi layar 9:16, dipakai untuk pembuka dan penutup."""
    src = Image.open(panel_path).convert("RGB"); sw, sh = src.size; tr = W / H
    nw = int(sh * tr)
    if nw <= sw:
        src = src.crop(((sw - nw) // 2, 0, (sw - nw) // 2 + nw, sh))
    else:
        nh = int(sw / tr); src = src.crop((0, 0, sw, nh))
    return src.resize((int(W * z), int(H * z)), Image.LANCZOS)


def lapis_judul(kecil, besar, y=1180):
    """Lapisan teks besar untuk pembuka dan penutup."""
    over = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(over)
    d.text((W // 2, y - 20), kecil, font=font(BODY, 44), fill=CREAM, anchor="ms", stroke_width=5, stroke_fill=(20, 12, 10))
    size = 150
    while True:
        f = font(SFXF, size); lines = wrap(d, besar.upper(), f, W - 150)
        if (len(lines) <= 3 and all(d.textlength(l, font=f) <= W - 150 for l in lines)) or size <= 60:
            break
        size -= 8
    yy = y + 30
    for ln in lines:
        d.text((W // 2, yy), ln, font=f, fill=(255, 225, 77), anchor="mt", stroke_width=max(6, size // 14), stroke_fill=(20, 12, 10)); yy += int(size * 1.08)
    return over


def kilat(img, a):
    if a < 0.02:
        return img
    arr = np.asarray(img, dtype=np.float32); a = min(a, 0.88)
    return Image.fromarray((arr * (1 - a) + np.array([255, 236, 200], np.float32) * a).astype(np.uint8))


def baca_klip(path, maks):
    """Membaca klip video (pembuka Veo) menjadi daftar bingkai 1080x1920."""
    cmd = ["ffmpeg", "-loglevel", "error", "-i", str(path), "-t", str(maks), "-vf",
           f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={V['fps']}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout; n = len(raw) // (W * H * 3)
    return [Image.frombytes("RGB", (W, H), raw[i * W * H * 3:(i + 1) * W * H * 3]) for i in range(n)]


GERAK_DEFAULT = ("Animate the starting image into one smooth cinematic shot with a slow push-in. Natural motion of the scene: sparks, light, cloth and "
                 "energy move; characters move slightly and stay exactly on-model. No text, no captions, no camera cuts.")


def bingkai_video(path, detik):
    """Mengambil bingkai dari berkas video pada detik tertentu, diperkecil untuk juri."""
    out = []
    for t in detik:
        raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{max(0, t):.2f}", "-i", str(path), "-frames:v", "1", "-vf", "scale=540:-2",
                              "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
        if raw:
            import io
            out.append(Image.open(io.BytesIO(raw)).convert("RGB"))
    return out


def pembuka_veo(d, sub_id, panel, gerak):
    """Klip pembuka bergerak dari panel terkuat, diperiksa juri. Kalau dua kali gagal QC, klip dibuang dan pembuka memakai gambar diam."""
    out = d / "veo" / f"{sub_id}.mp4"; cat = d / "veo" / f"{sub_id}.json"
    if out.exists() and read_json(cat, {}).get("lolos"):
        return out, read_json(cat)
    if read_json(cat, {}).get("dibuang") or not V.get("veo_pembuka") or vertex.mock():
        return None, read_json(cat, {})
    out.parent.mkdir(exist_ok=True); j = {}
    for i in range(2):
        try:
            vertex.gen_video((gerak or GERAK_DEFAULT) + " Keep every character design identical to the starting image. No text.", penuh(panel, 1.0), out)
        except Exception as e:
            log(f"  Pembuka bergerak {sub_id} tidak jadi ({str(e)[:140]}). Dipakai gambar diam.")
            return None, {"lolos": False, "masalah": [f"klip tidak jadi: {str(e)[:100]}"]}
        fr = bingkai_video(out, (0.1, 2.5, 4.8))
        j = qc.juri_veo(Image.open(panel).convert("RGB"), fr) if fr else {"lolos": False, "gagal": ["kosong"], "masalah": ["klip tidak terbaca"]}
        j["percobaan"] = i + 1
        if j["lolos"]:
            write_json(cat, j); return out, j
        log(f"  Pembuka bergerak {sub_id} percobaan {i + 1} gagal QC: {'; '.join(map(str, j['masalah']))[:160]}")
    out.unlink(missing_ok=True); j["dibuang"] = True; write_json(cat, j)
    log(f"  Pembuka bergerak {sub_id} dibuang setelah dua kali gagal QC. Dipakai gambar diam.")
    return None, j


def run(n, force=False, izinkan_gagal=False):
    ep = episodes()[n]; d = ep_dir(n); script = read_json(d / "naskah.json"); meta = read_json(d / "panel.json", {})
    if not script:
        log(f"Ep {n}: naskah belum ada."); return False
    subs = frames_final(n); state = {}; semua_ok = True; fps = V["fps"]
    nxt = episodes().get(n + 1); rng = np.random.default_rng(n)
    for si, sub in enumerate(subs):
        out = d / f"GalaIgnis_Ep{n:03d}{sub['id'][-1]}.mp4"
        bad = [f["kode"] for f in sub["frames"] if not (d / "panel" / f"{f['kode']}.png").exists() or not meta.get(f["kode"], {}).get("lolos")]
        if bad and not izinkan_gagal:
            log(f"Ep {sub['id']}: {len(bad)} panel belum lolos QC ({', '.join(bad)}). Video tidak dibuat."); semua_ok = False; continue
        if out.exists() and not force and not bad and read_json(d / "video.json", {}).get(sub["id"], {}).get("lolos"):
            continue
        huruf = sub["id"][-1]; kodes = [f["kode"] for f in sub["frames"]]
        hook = ep["pembuka"] if ep["pembuka"] in kodes else max(sub["frames"], key=lambda f: kekuatan(f, ""))["kode"]
        judul_short = (script.get("judul_short") or {}).get(huruf) or ep["judul"]
        hook_panel = d / "panel" / f"{hook}.png"
        veo, veo_qc = pembuka_veo(d, sub["id"], hook_panel, (script.get("pembuka_gerak_en") or {}).get(huruf))
        veo_frames = baca_klip(veo, 5.0) if veo else []
        klip = [dict(jenis="buka", panel=hook_panel, dur=(len(veo_frames) / fps if veo_frames else 2.2), pcm=np.zeros(0, np.int16), kuat=0.8,
                     over=lapis_judul(f"Episode {n} · Bagian {huruf}", judul_short), veo=veo_frames)]
        for f in sub["frames"]:
            v = script.get("gagal", {}) if f.get("tambahan") else script["frames"].get(f["kode"], {})
            bl = blocks_of(v); text = " ".join(t for _, _, t in bl); sfx = v.get("sfx") or ""
            a = speech(d, f["kode"], text, state)
            dur = max(V["detik_min"], len(text.split()) * V["detik_per_kata"] + 1.2, len(a) / RATE + 0.6)
            klip.append(dict(jenis="frame", panel=d / "panel" / f"{f['kode']}.png", blocks=bl, sfx=sfx, dur=dur, pcm=a, kuat=max(kekuatan(f, sfx), 0.5 if sfx else 0)))
        tutup = ("Bersambung", f"Episode {n} Bagian B") if si == 0 and len(subs) > 1 else (("Episode berikutnya", nxt["judul"]) if nxt else ("Gala Ignis & The Galians", "Tamat"))
        klip.append(dict(jenis="tutup", panel=d / "panel" / f"{kodes[-1]}.png", dur=2.6, pcm=np.zeros(0, np.int16), kuat=0.5, over=lapis_judul(*tutup, y=820)))
        for c in klip:
            c["k"] = int(round(c["dur"] * fps))
        total = sum(c["k"] for c in klip) / fps
        # suara: narator + musik
        suara = []; t = 0.0; ev = []
        for c in klip:
            k = c["k"] * RATE // fps; a = np.zeros(k, np.int16); off = RATE // 5; s = c["pcm"][:max(0, k - off)]
            a[off:off + len(s)] = s; suara.append(a); ev.append((t, c["k"] / fps, c["kuat"], c["jenis"])); t += c["k"] / fps
        suara = np.concatenate(suara)
        campuran = musik.campur(suara, musik.susun(ev, len(suara) / RATE + 0.01)) if V.get("musik", True) else suara
        wav = d / "audio" / f"_{sub['id']}.wav"
        with wave.open(str(wav), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(campuran.tobytes())
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-",
               "-i", str(wav), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "160k",
               "-movflags", "+faststart", str(out)]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE); tata = read_json(d / "tata.json", {})
        label = f"EP {sub['id']}"; prev_kuat = 0
        for ci, c in enumerate(klip):
            k = c["k"]; nz = rng.standard_normal((k, 2))
            if c["jenis"] == "frame":
                canvas, base, over = slide(c["panel"], label, ep["judul"], c["blocks"], c["sfx"], tata, c["panel"].stem)
                frame_at(canvas, base, over, 0.5, (0, 0)).save(d / "slide" / f"{c['panel'].stem}.jpg", quality=90)
                arah = [(1, 0), (-1, 0), (0, -1), (0.6, -0.6)][ci % 4]; kuat = c["kuat"]
                awal = 0.9 if ci == 1 else (0.75 * kuat if kuat >= 0.5 else 0.0)   # kilat putih setelah pembuka dan di frame keras
                for i in range(k):
                    lt = i / fps; g = 20 * kuat * np.exp(-lt * 3.2) if kuat >= 0.3 else 0
                    img = frame_at(canvas, base, over, i / max(1, k - 1), arah, geser=(nz[i, 0] * g, nz[i, 1] * g), tambah=0.05 * kuat * np.exp(-lt * 5))
                    proc.stdin.write(kilat(img, awal * np.exp(-lt * 9)).tobytes())
            else:
                base = penuh(c["panel"]); bw, bh = base.size; gelap = c["jenis"] == "tutup"
                for i in range(k):
                    q = i / max(1, k - 1); e = q * q * (3 - 2 * q)
                    if c.get("veo"):
                        img = c["veo"][min(i, len(c["veo"]) - 1)].copy()
                    else:
                        s = 1 + 0.14 * (e if not gelap else 0.3 * e); cw, ch = bw / s, bh / s
                        g = (10 * q ** 1.6) if not gelap else 0
                        x0 = (bw - cw) / 2 + nz[i, 0] * g; y0 = (bh - ch) / 2 + nz[i, 1] * g
                        img = base.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
                    if gelap:
                        img = Image.eval(img, lambda p: int(p * 0.42))
                    muncul = min(1.0, max(0.0, (i / fps - (0.25 if not gelap else 0.1)) / 0.25))
                    if muncul > 0:
                        o = c["over"] if muncul >= 1 else Image.eval(c["over"], lambda p: p).copy()
                        if muncul < 1:
                            o.putalpha(o.getchannel("A").point(lambda p: int(p * muncul)))
                        img = img.convert("RGBA"); img.alpha_composite(o); img = img.convert("RGB")
                    proc.stdin.write(kilat(img, 0.7 * np.exp(-i / fps * 9) if gelap else 0).tobytes())
        proc.stdin.close(); rc = proc.wait(); write_json(d / "tata.json", tata)
        q = periksa(out, total, bersuara=True)
        if state.get("mati") and V["narasi_suara"]:
            q["masalah"].append("suara narator tidak tersedia, video hanya bermusik"); q["lolos"] = False
        # juri melihat bingkai video jadi: pembuka, tiap seperempat, penutup
        buka = klip[0]["k"] / fps
        fr = bingkai_video(out, [min(buka - 0.2, 1.4), buka + (total - buka) * 0.25, buka + (total - buka) * 0.5, buka + (total - buka) * 0.7, total - 1.0])
        jv = qc.juri_video(fr) if len(fr) >= 3 else {"lolos": False, "gagal": ["bingkai"], "masalah": ["bingkai video tidak terbaca"]}
        if not jv["lolos"]:
            q["masalah"] += [f"tampilan: {m}" for m in (jv["masalah"] or jv["gagal"])]; q["lolos"] = False
        balon_gagal = [c["panel"].stem for c in klip if c["jenis"] == "frame" and not tata.get(c["panel"].stem, {}).get("qc", {}).get("lolos")]
        if balon_gagal:
            q["masalah"].append("balon perlu ditinjau di " + ", ".join(balon_gagal) + " (sunting tata.json)"); q["lolos"] = False
        q["juri_video"] = jv; q["balon_gagal"] = balon_gagal
        q["panel_gagal"] = bad; q["lolos"] = q["lolos"] and rc == 0 and not bad
        q["pembuka_bergerak"] = bool(veo_frames); q["pembuka_qc"] = veo_qc
        semua_ok &= q["lolos"]
        allv = read_json(d / "video.json", {}); allv[sub["id"]] = q; write_json(d / "video.json", allv)
        log(f"Video {out.name}: {q['durasi']:.1f} detik, {'lolos' if q['lolos'] else 'PERLU DITINJAU: ' + '; '.join(q['masalah'])}")
    return semua_ok


def periksa(path, durasi_harap, bersuara):
    """QC berkas video: ukuran, durasi, jalur suara, dan volume."""
    masalah = []
    try:
        r = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
                                      capture_output=True, text=True, check=True).stdout)
    except Exception as e:
        return {"lolos": False, "durasi": 0, "masalah": [f"berkas tidak terbaca: {str(e)[:80]}"]}
    vs = [s for s in r["streams"] if s["codec_type"] == "video"]; au = [s for s in r["streams"] if s["codec_type"] == "audio"]
    dur = float(r["format"]["duration"])
    if not vs or (vs[0]["width"], vs[0]["height"]) != (W, H):
        masalah.append("ukuran video salah")
    if abs(dur - durasi_harap) > 0.6:
        masalah.append(f"durasi {dur:.1f} detik, seharusnya {durasi_harap:.1f}")
    if not au:
        masalah.append("tanpa jalur suara")
    if dur > 180:
        masalah.append("lebih dari 3 menit, terlalu panjang untuk Short")
    if bersuara:
        v = subprocess.run(["ffmpeg", "-i", str(path), "-af", "volumedetect", "-vn", "-f", "null", "-"], capture_output=True, text=True).stderr
        if "mean_volume: -91" in v or "mean_volume: -inf" in v:
            masalah.append("suara kosong")
    return {"lolos": not masalah, "durasi": dur, "masalah": masalah}
