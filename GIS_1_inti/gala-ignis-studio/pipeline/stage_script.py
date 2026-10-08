"""Tahap naskah: narasi, dialog dan SFX per frame, plus adegan untuk ketukan gagal."""
import json
from .common import CFG, log, episodes, ep_dir, read_json, write_json, frames_final
from . import vertex, qc

PROMPT = """Kamu penulis komik anak berbahasa Indonesia untuk seri animasi 3D "Gala Ignis & The Galians" (penonton 7 sampai 12 tahun).
Tulis teks untuk video komik TANPA narator: cerita dibawa oleh balon percakapan di dalam panel dan efek suara. Tiap frame tampil beberapa detik.

Episode {n}: {judul}
Ringkasan: {ringkasan}
Gagasan inti ({jenis}): {gagasan}
{gagal}
Frame berurutan (kode | shot | adegan | tokoh di frame):
{frames}

Aturan:
- Bahasa Indonesia sehari-hari, kalimat pendek. Cerita dibawa DIALOG di dalam balon: paling panjang 60 huruf per balon, paling banyak 2 balon per frame.
- "narasi" adalah kotak keterangan kecil, hanya untuk tempat, waktu, atau lompatan waktu. Paling panjang 60 huruf dan paling banyak di 4 frame per episode. Kosongkan di frame lain.
- Total paling banyak 24 kata per frame, supaya balon tidak menutupi gambar.
- Jangan menceritakan ulang apa yang sudah terlihat di gambar; tambahkan pikiran, alasan, atau taruhannya.
- Gagasan inti harus diucapkan dengan kata sederhana di sekitar puncak episode, satu kali, bukan diulang-ulang.
- Dialog spesifik untuk adegan ini. Hindari kalimat pahlawan umum. Tanpa tanda pisah panjang. Titik tiga paling banyak 2 kali di seluruh episode.
- Ethylene adalah sprite api tanpa mulut: ia tidak berbicara dengan kata-kata, hanya bunyi pendek seperti "Pip!" atau "Pip?".
- Penutur dialog harus tokoh yang ada di frame itu. Mata Gala tidak pernah terlihat, jadi jangan menulis soal tatapan matanya.
- Frame terakhir sub-episode A harus menggantung. Frame pertama sub-episode B langsung menyambungnya.
- SFX satu kata, huruf besar, paling panjang 12 huruf (contoh: WHOOSH, KRAK, BLAAR). Wajib di frame yang berbunyi keras (ledakan, hantaman, tembakan); kosongkan di frame tenang.
- Frame aksi murni boleh tanpa balon, cukup SFX. Paling banyak 4 frame tanpa teks dan tanpa SFX.
{perbaikan}
Jawab JSON saja, bentuk persis:
{{"frames": {{"<kode>": {{"narasi": "", "dialog": [{{"tokoh": "", "teks": ""}}], "sfx": ""}}}}{gagal_schema},
"judul_short": {{"A": "<judul Short A yang memancing, paling panjang 34 huruf>", "B": "<judul Short B>"}},
"pembuka_gerak_en": {{"A": "<one English sentence: how the strongest moment of part A moves as an 6-second shot, camera and action>", "B": "<same for part B>"}}}}
Semua kode frame di atas wajib ada."""

GAGAL_TAMBAH = """Ketukan gagal yang HARUS ditambahkan sebagai satu frame baru tepat sebelum frame {sebelum}: {ketukan}
Untuk frame baru itu, isi kunci "gagal" dengan shot kamera, deskripsi adegan dalam bahasa Inggris untuk model gambar (satu sampai dua kalimat, konkret, sebut tokoh dengan nama yang sama seperti adegan lain), dan teksnya."""
GAGAL_SCHEMA = ',\n"gagal": {"shot": "<mis. Medium Shot>", "scene_en": "<English scene description>", "narasi": "", "dialog": [], "sfx": ""}'


def _tiruan(ep, perlu):
    fr = {}
    for sub in ep["subs"]:
        for f in sub["frames"]:
            fr[f["kode"]] = {"narasi": "", "dialog": [{"tokoh": "Gala", "teks": f["id"][:56]}], "sfx": "KRAK" if "Action" in f["shot"] else ""}
    out = {"frames": fr, "judul_short": {"A": ep["judul"] + " (A)", "B": ep["judul"] + " (B)"}}
    if perlu:
        out["gagal"] = {"shot": "Medium Shot", "scene_en": "Gala tries the wrong approach and it fails.", "narasi": "", "dialog": [{"tokoh": "Gala", "teks": ep["gagal"]["ketukan"][:56]}], "sfx": ""}
    return out


def rapikan(s):
    """Perbaikan pasti sebelum lint: tanda pisah panjang jadi koma, titik tiga maksimal 2 per episode, Ethylene hanya Pip."""
    sisa = 2
    semua = list((s.get("frames") or {}).values()) + ([s["gagal"]] if s.get("gagal") else [])
    for v in semua:
        def bersih(t):
            nonlocal sisa
            t = t.replace("—", ",").replace("–", ",").replace("…", "...").replace(" ,", ",")
            while "..." in t:
                if sisa > 0:
                    sisa -= 1; t = t.replace("...", "@@", 1)
                else:
                    t = t.replace("...", "", 1)
            return t.replace("@@", "...").replace(" .", ".").replace(",,", ",").strip()
        if v.get("narasi"):
            v["narasi"] = bersih(v["narasi"])
        for d in v.get("dialog") or []:
            d["teks"] = bersih(d.get("teks", ""))
            if (d.get("tokoh") or "").lower().startswith(qc.NAMA_SPRITE) and (" " in d["teks"].strip() or len(d["teks"].strip()) > 8):
                d["teks"] = "Pip!"


def run(n, force=False):
    ep = episodes()[n]; d = ep_dir(n); path = d / "naskah.json"
    if path.exists() and not force and read_json(path).get("qc", {}).get("lolos"):
        return read_json(path)
    g = ep["gagal"]; perlu = g["status"] == "tambah"
    rows = []; kode = []
    for sub in ep["subs"]:
        rows.append(f"--- Sub-episode {sub['id']}: {sub['judul']}")
        for f in sub["frames"]:
            kode.append(f["kode"]); rows.append(f"{f['kode']} | {f['shot']} | {f['id']} | {', '.join(f['tokoh']) or '-'}")
    gagal_txt = GAGAL_TAMBAH.format(**g) if perlu else f"Ketukan gagal sudah ada di frame {g['frame']}: pertegas lewat teks bahwa cara pertama tokoh tidak berhasil."
    fb = ""; best = None
    for i in range(CFG["qc"]["naskah_attempts"]):
        s = vertex.gen_json(PROMPT.format(n=n, judul=ep["judul"], ringkasan=ep["ringkasan"], jenis=ep["gagasan"]["jenis"], gagasan=ep["gagasan"]["teks"],
                                          gagal=gagal_txt, frames="\n".join(rows), gagal_schema=GAGAL_SCHEMA if perlu else "", perbaikan=fb),
                            temperature=0.8, mock_value=lambda: _tiruan(ep, perlu))
        rapikan(s)
        masalah = qc.lint_naskah(s, kode, perlu); juri = None
        if not masalah:
            write_json(path, s)  # supaya frames_final melihat frame gagal
            juri = qc.juri_naskah(ep, s, [f for sub in frames_final(n) for f in sub["frames"]])
            masalah = [] if juri["lolos"] else [f"juri: {x}" for x in (juri["masalah"] or juri["gagal"])]
        s["qc"] = {"lolos": not masalah, "masalah": masalah, "percobaan": i + 1}
        if best is None or len(masalah) < len(best["qc"]["masalah"]):
            best = s
        if not masalah:
            break
        log(f"  naskah ep {n} percobaan {i + 1}: {len(masalah)} masalah")
        fb = "\nPerbaiki masalah dari percobaan sebelumnya:\n- " + "\n- ".join(masalah[:12]) + "\n"
    write_json(path, best)
    log(f"Naskah ep {n}: {'lolos' if best['qc']['lolos'] else 'PERLU DITINJAU'}")
    return best
