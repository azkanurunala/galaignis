# Status Referensi Visual

*Gala Ignis & The Galians · catatan progres pembuatan sheet di Gemini · diperbarui 23 September 2026*

Simpan setiap sheet yang lolos dengan nama kode di kolom **File final**. Semua keputusan desain di bawah sudah diterapkan ke anchor di bible (season-01 sampai season-10, referensi-karakter, referensi-latar).

## Karakter utama (K01-K20)

| Kode | Status | File final | Keputusan yang dikunci |
|---|---|---|---|
| K01 Gala v1 | Lolos | K01_final | |
| K02 Gala v2 | Lolos | K02_final | Pin roset emas bermata merah dengan dua pita kecil di **dada kanan atas** |
| K03 Ethylene | Lolos | K03_final | Bola kuning keemasan mengilap, mahkota api, dua sayap api, ekor api, mata titik putih, **tanpa mulut** |
| K04 Aila | Lolos | K04 | Visor bening, mata terlihat |
| K05 Dhruva | Lolos | K05_final | Tanpa pedang dan jubah; perisai kawung di semua tampilan |
| K06 Kalia, K07 Gala Bayang, K10 Maheswari, K12 Agni, K13 Hampa, K17 Arka, K18 Taraka, K19 Utusan | Lolos | kode masing-masing | |
| K08 Wirasena bertopeng | Lolos | K08_final | Topeng batu retak tanpa mulut; kain batik di **lengan kiri**; tangan kosong |
| K09 Wirasena tanpa topeng | Lolos | K09_final | Bekas luka di **alis kanan** |
| K11 Indra | Lolos | K11_final | Lensa kacamata ungu, pin "V" |
| K14 Vikrama berjubah | Lolos | K14_final | Proporsi chibi |
| K15 Vikrama berzirah | Lolos | K15 | Sheet awal dipakai; proporsi chibi, wajah cukup dekat dengan K14_final |
| K16 Nira | **Belum** | | Poni harus menutup mata kanan |
| K20 Katalis Entropi | **Belum, prioritas** | | Generate ulang tanpa teks liar |

## Karakter pendukung (K30-K68)

| Kode | Status | Catatan |
|---|---|---|
| K30-K38, K40-K42, K44, K47-K50, K52-K57, K59-K63, K66, K67 | Lolos | K42: crop kotak kosong kiri bawah |
| K39 Komandan **Himakara** | Lolos (K39_final) | Nama diganti dari "Sub-Zero"; kulit kebiruan, wajah terbuka, tanpa jubah |
| K43 Pejuang Perlawanan | **Belum** | Ganti senapan realistis jadi senapan energi rakitan |
| K45 Pertapa | **Belum** | Hapus monokel di potret netral |
| K46 Chrono-Wraith | **Belum** | Generate ulang, gaya animasi, tanpa tengkorak |
| K51 Lima Pendiri | **Belum** | Harus lima wajah berbeda |
| K58 Sprite Desa | **Belum, prioritas** | Generate ulang 3D, bola api tanpa kaki |
| K64 Penjaga Timur | **Belum** | Ganti tongkat dengan jaring ikan |
| K65 Penjaga Selatan | **Belum** | Hapus tongkat |
| K68 Kapal Angkut Galians | Menunggu L07 | Entri baru; sheet L07 berfungsi sebagai referensinya |

## Latar (L01-L68)

| Kode | Status | Keputusan yang dikunci |
|---|---|---|
| L01 Arena 7 | Lolos (L01_final) | Pintu hazard di dinding kiri, jendela observasi di dinding belakang |
| L02 Laboratorium | Lolos (L02_final) | Pintu kedua di dinding kiri, tabung kaca di dinding belakang dan kanan |
| L03 Lorong Tembak | Lolos (L03_final) | Layar lebar di atas pintu masuk |
| L04 Ruang Simulasi | Lolos (L04_final) | Empat kapsul telur berkursi rebah dengan pintu kaca; layar besar di dinding belakang |
| L05 Kota Virtual | Lolos (L05_final) | Atap joglo, ujung atap lurus |
| L06 War Room | Lolos (L06_final) | **Lambang resmi Galians:** sepasang sayap emas mengapit lingkaran berisi api |
| L07 Hanggar | **Berikutnya** | Prompt sudah ada di percakapan |
| L08-L68 | Belum | |

## Pola prompt yang terbukti berhasil

- Buka dengan "Generate a completely NEW image" setiap kali ada lampiran, dan pakai chat baru. Tanpa ini Gemini kadang mengembalikan lampiran apa adanya.
- Tentukan letak setiap elemen dan arah panel reverse secara eksplisit ("pintu yang tadinya di kiri kini di KANAN").
- Untuk latar akademi, lampirkan L01_final sebagai acuan gaya, bukan sheet karakter.
- Tulis "No other text, no labels" untuk mencegah label liar.
- Kalau Gemini konsisten menggeser sisi (kiri atau kanan), terima dan kunci di anchor, jangan dilawan.

## Komik Episode 1

Selesai: sampul + 8 halaman, semuanya lolos review (file Sampul_final, Hal01_final sampai Hal08_final, digabung jadi Gala_Ignis_Komik_Episode_01.pdf).

Pelajaran untuk episode berikutnya:
- Lampirkan sheet final tokoh yang muncul, sheet latar, dan satu halaman yang sudah lolos sebagai acuan gaya dan huruf. Pilih halaman acuan yang tokohnya sama dengan halaman baru, supaya tokoh lain tidak ikut muncul.
- Tulis tata letak panel secara eksplisit (baris dan kolom), dan larang elemen menembus batas panel.
- Jangan minta efek rumit seperti "wajah terpantul di layar"; pecah jadi panel yang sederhana.
- Kalau sebuah panel membicarakan tokoh yang tidak ada di panel itu, tulis tegas "X is NOT in this panel", karena Gemini cenderung menaruh tokoh yang disebut di tempat terdekat.
- Untuk tokoh di luar panel yang berbicara, tulis "tail pointing off-panel".
- Close-up wajah Gala paling rawan mata tembus kacamata; tulis "fully opaque dark lenses".
