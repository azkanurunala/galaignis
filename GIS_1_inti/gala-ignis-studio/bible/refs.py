import re
from collections import defaultdict, OrderedDict
import render as R
from catalog import LOCS, SECONDARY, secondary_for, location_for

R.merge()
SEASONS = [R.S1, R.S2, R.S3F, R.S4F, R.S5F] + [x[2] for x in R.EXTRA]
TITLES = {1: "Inisiasi Sang Galian", 2: "Ancaman Inti Atom", 3: "Paradoks Waktu", 4: "Bayangan Sang Purba",
          5: "Invasi Cyber-Nusantara", 6: "Realm of Ethylene", 7: "Keretakan Aliansi", 8: "Resonansi Emas",
          9: "Gerhana Atom", 10: "Era Baru Galians"}

MAIN = OrderedDict([
 ("K01", ("Gala Ignis (v1, sebelum pin)", R.GALA_V1, "human")),
 ("K02", ("Gala Ignis (v2, dengan pin lambang)", R.GALA_V2, "human")),
 ("K03", ("Ethylene", R.SPRITE, "creature")),
 ("K04", ("Aila", R.AILA, "human")),
 ("K05", ("Dhruva", R.DHRUVA, "human")),
 ("K06", ("Kalia", R.KALIA, "human")),
 ("K07", ("Gala Bayang", R.GALA_BAYANG, "human")),
 ("K08", ("Wirasena (bertopeng)", R.WIRA_M, "human")),
 ("K09", ("Wirasena (tanpa topeng)", R.WIRA_V, "human")),
 ("K10", ("Maheswari", R.MAHESWARI, "human")),
 ("K11", ("Indra Mahadana", R.INDRA, "human")),
 ("K12", ("Tetua Agni", R.EXTRA_ANCHORS["a"], "creature")),
 ("K13", ("Sang Hampa", R.EXTRA_ANCHORS["h"], "entity")),
 ("K14", ("Vikrama (berjubah)", R.EXTRA_ANCHORS["r"], "human")),
 ("K15", ("Vikrama (berzirah besi)", R.EXTRA_ANCHORS["R"], "human")),
 ("K16", ("Nira", R.EXTRA_ANCHORS["n"], "human")),
 ("K17", ("Arka (Subjek Zero)", R.EXTRA_ANCHORS["k"], "human")),
 ("K18", ("Komandan Taraka", R.EXTRA_ANCHORS["t"], "human")),
 ("K19", ("Sang Utusan", R.EXTRA_ANCHORS["u"], "human")),
 ("K20", ("Katalis Entropi", R.EXTRA_ANCHORS["c"], "entity")),
])
FLAG2K = {"S": "K03", "A": "K04", "D": "K05", "K": "K06", "X": "K07", "W": "K08", "V": "K09", "M": "K10", "I": "K11",
          "a": "K12", "h": "K13", "r": "K14", "R": "K15", "n": "K16", "k": "K17", "t": "K18", "u": "K19", "c": "K20"}
SEC = OrderedDict((k, (n, a)) for k, n, a, rx, lo, hi in SECONDARY)
ALLCHAR = OrderedDict(list((k, v[:2]) for k, v in MAIN.items()) + list(SEC.items()))

char_eps, loc_eps = defaultdict(set), defaultdict(set)
char_frames, loc_frames = defaultdict(int), defaultdict(int)
ep_chars, ep_locs = defaultdict(set), defaultdict(set)
ep_season, ep_title, ep_arc = {}, {}, {}
missing_loc = []
v2 = False
for S in SEASONS:
    for A in S["arcs"]:
        for E in A["eps"]:
            ep = E["n"]
            ep_season[ep] = S["n"]; ep_title[ep] = E["title"]; ep_arc[ep] = A["title"]
            for SE in E["subs"]:
                for AC in SE["acts"]:
                    for code, shot, vis, scene, flags in AC["frames"]:
                        if code == R.V2_START:
                            v2 = True
                        low = scene.lower()
                        f = flags + ("AD" if ("squad" in low or "teammate" in low) else "")
                        ids = set()
                        if "G" in f:
                            ids.add("K02" if v2 else "K01")
                        ids |= {FLAG2K[c] for c in f if c in FLAG2K}
                        ids |= set(secondary_for(ep, scene))
                        for i in ids:
                            char_eps[i].add(ep); char_frames[i] += 1; ep_chars[ep].add(i)
                        loc = location_for(code)
                        if loc:
                            loc_eps[loc].add(ep); loc_frames[loc] += 1; ep_locs[ep].add(loc)
                        else:
                            missing_loc.append(code)


def ranges(eps):
    eps = sorted(eps)
    out, start, prev = [], None, None
    for e in eps:
        if start is None:
            start = prev = e
        elif e == prev + 1:
            prev = e
        else:
            out.append((start, prev)); start = prev = e
    if start is not None:
        out.append((start, prev))
    return ", ".join(f"{a}" if a == b else f"{a}-{b}" for a, b in out)


SHEET_STYLE = ("3D CGI render like a modern 3D animated feature film, rounded stylized 3D shapes, soft realistic materials, "
               "plain light grey background, soft even studio lighting, no drawn line art, no 2D illustration.")


def char_prompt(kid, name, anchor, kind):
    if kind == "human":
        views = ("Show the full body in front view, three-quarter view and back view, plus three head close-ups: neutral, happy, determined. "
                 "Show expressions only with eyebrows and mouth whenever the eyes are covered by goggles, a visor or a mask.")
    elif kind == "creature":
        views = "Show it from the front, from the side, and in one expressive pose, with a small silhouette of a child next to it for scale."
    else:
        views = "Show it as one large full view and one close-up of its defining feature, with a tiny human silhouette for scale."
    label = name.split(" (")[0].upper()
    return (f"Create a character reference sheet, {SHEET_STYLE}\n{anchor}\n{views}\n"
            f'Label the sheet with one small clean caption: "{kid} {label}".')


def group_prompt(kid, name, anchor):
    return (f"Create a character reference sheet, {SHEET_STYLE}\n{anchor}\n"
            "Show one figure in front view and side view, plus one small group shot of three of them together, and a small "
            f'silhouette of a child for scale.\nLabel the sheet with one small clean caption: "{kid} {name.upper()}".')


def loc_prompt(lid, name, anchor):
    return (f"Create an environment reference sheet, {SHEET_STYLE.replace('plain light grey background, soft even studio lighting, ', '')}"
            f" No characters, no text except one small caption.\nSetting: {anchor}\nShow the place in three views: a wide establishing shot, "
            "a medium shot of its most important feature, and a reverse angle looking the other way. Neutral daylight or its usual lighting.\n"
            f'Caption in one corner: "{lid} {name.upper()}".')


# ---------- referensi-karakter.md
out = ["# Perpustakaan Referensi Karakter",
       "",
       "*Gala Ignis & The Galians · Seluruh 10 season*",
       "",
       f"{len(ALLCHAR)} lembar karakter: {len(MAIN)} tokoh utama (termasuk versi desain) dan {len(SEC)} tokoh pendukung, unit musuh, dan kelompok figuran yang berulang.",
       "",
       "## Cara Pakai",
       "",
       "1. **Buat setiap lembar sekali saja,** lalu simpan gambarnya dengan nama file berkode, misalnya `K01.png`. Ulangi pembuatan sampai desainnya benar, karena gambar ini akan menjadi acuan untuk ratusan frame.",
       "2. **Urutan pembuatan yang disarankan:** K01, K03, lalu tokoh lain sesuai season yang sedang dikerjakan. Untuk K02, lampirkan K01 dan minta *\"Same character, add a small round gold rosette pin with a red gem center and two tiny ribbon tails on the upper right chest.\"* Cara ini menjaga dua versi tetap identik. Lakukan hal yang sama untuk K09 dari K08 dan K15 dari K14.",
       "3. **Saat membuat frame atau halaman komik,** lampirkan lembar yang tercantum di `kit-per-episode.md` untuk episode itu. Lampirkan hanya yang muncul di halaman atau frame tersebut, bukan semuanya.",
       "4. Setiap prompt storyboard di file season sudah memuat deskripsi teks yang sama persis dengan lembar ini. Gambar referensi adalah penguat, bukan pengganti.",
       "",
       "## Daftar Isi",
       "",
       "| Kode | Nama | Muncul di episode | Jumlah frame |",
       "|---|---|---|---|"]
for k, (n, a) in ALLCHAR.items():
    out.append(f"| {k} | {n} | {ranges(char_eps[k]) or '-'} | {char_frames[k]} |")
out += ["", "---", "", "## Tokoh Utama dan Versi Desain", ""]
for k, (n, a, kind) in MAIN.items():
    out += [f"### {k} · {n}", "", f"**Muncul di episode:** {ranges(char_eps[k])} · **{char_frames[k]} frame**", "",
            "```text", char_prompt(k, n, a, kind), "```", ""]
out += ["---", "", "## Tokoh Pendukung, Unit Musuh, dan Kelompok", ""]
for k, (n, a) in SEC.items():
    groupish = any(w in a.lower() for w in ("cadets", "guards", "drones", "fighters", "staff", "statues", "warriors", "creatures", "shades", "sprites", "androids", "instructors", "founders"))
    p = group_prompt(k, n, a) if groupish else char_prompt(k, n, a, "human" if not any(w in n for w in ("Walker", "Core", "Penjaga Cakrawala", "Wraith")) else "entity")
    out += [f"### {k} · {n}", "", f"**Muncul di episode:** {ranges(char_eps[k]) or '-'} · **{char_frames[k]} frame**", "",
            "```text", p, "```", ""]
open("../docs/referensi-karakter.md", "w").write("\n".join(out))

# ---------- referensi-latar.md
out = ["# Perpustakaan Referensi Latar",
       "",
       "*Gala Ignis & The Galians · Seluruh 10 season*",
       "",
       f"{len(LOCS)} lokasi. Setiap act di 150 episode sudah dipetakan ke satu lokasi, dan deskripsi lokasinya otomatis masuk ke setiap prompt storyboard sebagai baris `Setting:`.",
       "",
       "## Cara Pakai",
       "",
       "1. Buat lembar latar sekali, simpan sebagai `L01.png` dan seterusnya.",
       "2. Lembar latar dibuat dalam kondisi normal. Perubahan kondisi seperti alarm merah, setelah ledakan, malam, atau gerhana ditulis di Scene tiap frame, jadi satu lembar cukup untuk semua kondisi.",
       "3. Lampirkan lembar latar bersama lembar karakter setiap kali membuat frame atau halaman di lokasi itu.",
       f"4. Frame tanpa latar tetap: {len(missing_loc)} dari 2.400. Semuanya adalah layar terbelah, kilas balik, POV HUD lintas lokasi, atau montase beberapa tempat sekaligus. Frame seperti ini sengaja tidak diberi satu latar.",
       "",
       "## Daftar Isi",
       "",
       "| Kode | Lokasi | Muncul di episode | Jumlah frame |",
       "|---|---|---|---|"]
for lid, (n, a) in LOCS.items():
    out.append(f"| {lid} | {n} | {ranges(loc_eps[lid]) or '-'} | {loc_frames[lid]} |")
out += ["", "---", ""]
for lid, (n, a) in LOCS.items():
    out += [f"### {lid} · {n}", "", f"**Muncul di episode:** {ranges(loc_eps[lid]) or '-'} · **{loc_frames[lid]} frame**", "",
            "```text", loc_prompt(lid, n, a), "```", ""]
open("../docs/referensi-latar.md", "w").write("\n".join(out))

# ---------- kit-per-episode.md
out = ["# Kit Referensi per Episode",
       "",
       "*Lembar karakter (K) dan latar (L) yang dipakai di setiap episode. Kode merujuk ke `referensi-karakter.md` dan `referensi-latar.md`.*",
       "",
       "Kit ini dihitung otomatis dari 2.400 frame, jadi daftarnya pasti cocok dengan isi storyboard. Untuk satu halaman komik atau satu frame, lampirkan hanya kode yang benar-benar muncul di halaman itu. Kalau aplikasi membatasi jumlah lampiran, prioritaskan: Gala, tokoh lain yang berbicara, lalu latar.",
       ""]
cur = None
for ep in sorted(ep_season):
    s = ep_season[ep]
    if s != cur:
        cur = s
        out += ["", f"## Season {s}: {TITLES[s]}", "", "| Ep | Judul | Karakter | Latar |", "|---|---|---|---|"]
    ks = sorted(ep_chars[ep], key=lambda x: int(x[1:]))
    ls = sorted(ep_locs[ep], key=lambda x: int(x[1:]))
    out.append(f"| {ep} | {ep_title[ep]} | {', '.join(ks)} | {', '.join(ls) or '-'} |")
out += ["", "## Legenda", "", "| Kode | Nama |", "|---|---|"]
for k, (n, a) in ALLCHAR.items():
    out.append(f"| {k} | {n} |")
for lid, (n, a) in LOCS.items():
    out.append(f"| {lid} | {n} |")
open("../docs/kit-per-episode.md", "w").write("\n".join(out))

unused_c = [k for k in ALLCHAR if not char_eps[k]]
unused_l = [l for l in LOCS if not loc_eps[l]]
print("chars", len(ALLCHAR), "unused", unused_c)
print("locs", len(LOCS), "unused", unused_l)
print("frames without location", len(missing_loc), missing_loc[:40])
print("eps", len(ep_season), "eps w/o loc", [e for e in ep_season if not ep_locs[e]])
