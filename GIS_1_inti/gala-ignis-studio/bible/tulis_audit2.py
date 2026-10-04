"""Menulis ulang bagian 'Audit putaran kedua' di docs/audit-mutu.md dari data audit dan perbaikan.json."""
import json
from antislop_gagal import GAGAL, PEMBUKA2, MIRIP2, KESINAMBUNGAN, AUDIT2_SEASONS

P = json.load(open("perbaikan.json", encoding="utf-8"))
p = "../docs/audit-mutu.md"; t = open(p, encoding="utf-8").read()
k = [v["ketukan"] for v in GAGAL.values() if v["status"] == "tambah"]
per = [v["perpanjang"] for v in GAGAL.values() if v.get("perpanjang")]
tindakan = {(c["episode"], c["frame"]): c for c in P["catatan"]}
diubah = sum(1 for c in P["catatan"] if c.get("frame_diubah"))
sec = ["## Audit putaran kedua (3 Oktober 2026)", "",
       f"Ketukan gagal, komplikasi puncak arc, pembuka video, dan frame mirip dibaca ulang per episode oleh pemeriksa terpisah untuk kesepuluh season ({len(AUDIT2_SEASONS)} dari 10).", "",
       f"- Ketukan gagal sekarang: {len(k)} ditambahkan sebagai rencana, {150 - len(k)} sudah ada di frame. Beberapa status dibalik dari sudah ada menjadi tambah karena frame yang ditunjuk bukan kegagalan sungguhan.",
       f"- Pola kalimat mencoba lalu tetapi atau namun tersisa di {sum(', tetapi' in x or ', namun' in x for x in k)} dari {len(k)} ketukan. Pola harus memilih tersisa di {sum('harus memilih' in x for x in per)} dari {len(per)} komplikasi puncak arc.",
       f"- Pembuka video dipilih manual untuk {len(PEMBUKA2)} episode. Saran konkret frame mirip ditulis untuk {len(MIRIP2)} episode.",
       "- Di beberapa episode tabel lama hanya mencatat jumlah frame mirip, sehingga pasangan frame yang disebut di saran adalah dugaan pemeriksa.", "",
       "### Kesinambungan", "",
       f"Pemeriksa mencatat {len(KESINAMBUNGAN)} masalah kesinambungan. {diubah} diperbaiki dengan menulis ulang {len(P['frames'])} frame yang sudah ada dan {len(P['ringkasan'])} ringkasan, tanpa mengubah jumlah atau kode frame. Sisanya dinilai tidak perlu diubah, dengan alasan di tabel. Perbaikannya ada di `bible/perbaikan.json`.", "",
       "Batas: tiap perbaikan diperiksa terhadap frame di sekitarnya oleh pemeriksa season itu saja. Belum ada pemeriksaan silang antarseason, dan baru Season 2 yang dibaca penuh oleh penyunting utama.", "",
       "| Ep | Frame | Masalah | Tindakan | Frame diubah |", "|---|---|---|---|---|"]
for x in sorted(KESINAMBUNGAN, key=lambda x: x["episode"]):
    c = tindakan.get((x["episode"], x["frame"])) or next((c for c in P["catatan"] if c["episode"] == x["episode"] and c["frame"] == x["frame"]), None)
    act = c["tindakan"] if c else "BELUM DITANGANI"
    ch = ", ".join(c.get("frame_diubah") or []) if c else ""
    sec.append(f"| {x['episode']} | {x['frame']} | {x['masalah'].replace('|', '/')} | {act.replace('|', '/')} | {ch} |")
if "## Audit putaran kedua" in t:
    t = t[:t.index("## Audit putaran kedua")] + t[t.index("## Tabel per episode"):]
t = t.replace("## Tabel per episode", "\n".join(sec) + "\n\n## Tabel per episode")
open(p, "w", encoding="utf-8").write(t)
print(len(KESINAMBUNGAN), "masalah,", diubah, "diperbaiki,", sum(1 for s in sec if "BELUM DITANGANI" in s), "belum ditangani")
