import sys, os, shutil; sys.path.insert(0, '/home/claude/komik')
from ep2_v2 import *
S = '/home/claude/sheets/'; A = '/home/claude/attach/ep02v2/'
out = ["# Komik Episode 2: Pemeta Molekul (versi 2, dibuat ulang per panel)\n",
       "*Gala Ignis & The Galians · Season 1 · sampul + 8 halaman · 27 gambar (26 panel + sampul)*\n",
       "## Metode\n",
       "- Setiap panel dibuat sebagai SATU gambar tanpa teks, di chat Gemini baru.",
       "- Lampiran bernomor per panel (kode file di bawah). Urutan lampiran harus sama dengan urutan di prompt.",
       "- Halaman disusun lokal, semua teks ditulis dengan Comic Neue Bold (dialog, narasi) dan Bangers (SFX), lalu gambar diperjelas dengan Real-ESRGAN.",
       "- Panel versi 1 yang sudah bagus disimpan sebagai cadangan; per panel dipilih yang lebih baik.\n",
       "## Aturan kesinambungan\n"] + [f"- {r}" for r in RULES] + ["",
       "## Keputusan cerita\n",
       "| Keputusan | Alasan |", "|---|---|",
       "| Teknisi di 2A.1a diganti Instruktur Ketiga | Tidak perlu karakter baru |",
       "| Hitung mundur 19 jam lalu 14 jam | Menyambung ultimatum Episode 1 |",
       "| Tendangan api memotong ketiga proyektil | Storyboard hanya memotong satu |",
       "| Dialog \"Api... ke kaki!\" (tanpa kanan/kiri) | Kaki yang berapi = kaki kiri demi kesinambungan |",
       "| Ethylene menyatu ke api kaki (Hal. 5) lalu keluar dari asap (Hal. 6) | Ethylene tidak boleh hilang tanpa penjelasan |",
       "| Tulisan layar Hal. 7 ditulis lokal | Model gambar sering salah eja tulisan |", "",
       "## Daftar paket per panel\n", "| Halaman | Panel | Lampirkan (urutan) | Teks |", "|---|---|---|---|"]
allp = [(p['title'], x) for p in PAGES for x in p['panels']] + [("Sampul", COVER)]
for t, x in allp:
    out.append(f"| {t.split(':')[0]} | {x['name']} | {', '.join(x['files'])} | {' · '.join(v for _, v in x['text']) or '(tanpa teks)'} |")
out.append("")
for pi, p in enumerate(PAGES, 1):
    out.append(f"## {p['title']}\n\nTata letak: {p['layout']}\n")
    for qi, x in enumerate(p['panels'], 1):
        out.append(f"### Panel {x['name']}\n\n**Lampirkan:** " + ", ".join(f"{i+1}) {f}" for i, f in enumerate(x['files'])) + "\n")
        out.append("```text\n" + x['prompt'] + "\n```\n")
        d = f"{A}h{pi:02d}_p{qi}"; os.makedirs(d, exist_ok=True)
        for i, f in enumerate(x['files']): shutil.copy(S + f + '.png', f"{d}/{i+1}_{f}.png")
    out.append("---\n")
out.append("## Sampul\n\n**Lampirkan:** " + ", ".join(f"{i+1}) {f}" for i, f in enumerate(COVER['files'])) + "\n\n```text\n" + COVER['prompt'] + "\n```\n")
d = A + "sampul"; os.makedirs(d, exist_ok=True)
for i, f in enumerate(COVER['files']): shutil.copy(S + f + '.png', f"{d}/{i+1}_{f}.png")
open('/home/claude/gala-ignis/komik-episode-02.md', 'w').write("\n".join(out))
print(len(allp), 'panels')
