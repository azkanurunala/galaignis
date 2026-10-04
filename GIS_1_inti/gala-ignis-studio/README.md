# Gala Ignis Studio

Repo produksi *Gala Ignis & The Galians*: dari bible 150 episode sampai video komik vertikal, dengan gambar dibuat lewat Google Cloud Vertex AI dan pemeriksaan mutu di setiap tahap.

Status saat diekspor (3 Oktober 2026): bible, data, referensi, dan pipeline lengkap. Pipeline sudah diuji ujung ke ujung dalam mode tiruan (tanpa Vertex). **Panggilan ke Vertex AI belum pernah dijalankan**, karena lingkungan tempat repo ini dibuat tidak punya akses ke Google Cloud. Anggap langkah 3 di bawah sebagai uji pertama yang sesungguhnya.

## Isi

| Folder | Isi |
|---|---|
| `bible/` | Sumber cerita (Python). Ubah di sini, lalu `python run.py data`. |
| `docs/` | Bible dalam bentuk dokumen: `00-inti.md`, `season-01..10.md`, `audit-mutu.md`, riset, naskah komik Episode 1 dan 2. |
| `data/` | `episodes.json` (150 episode, 2.400 frame, prompt siap pakai) dan `refs.json` (129 referensi dan statusnya). |
| `refs/` | Sheet tokoh (`karakter/`), latar (`latar/`), panel acuan gaya (`gaya/`), versi lama (jangan dipakai). |
| `pipeline/` | Kode tahap produksi dan QC. |
| `arsip/` | Komik Episode 1 (final), Episode 2 versi 1, dan alat susun manual yang dipakai sebelumnya. |
| `out/` | Hasil produksi per episode. Tidak masuk git. |

## Menyiapkan

1. Python 3.10 ke atas dan `ffmpeg` terpasang.
2. `python -m venv .venv`, aktifkan, lalu `pip install -r requirements.txt`.
3. Google Cloud: aktifkan Vertex AI API di project Anda, lalu `gcloud auth application-default login`.
4. Salin `.env.example` menjadi `.env` dan isi ID project.
5. `git init` kalau ingin menjadikannya repo.

## Menjalankan

```bash
python run.py periksa                 # cek keutuhan data, tanpa biaya
python run.py doctor                  # cek login, daftar model, satu uji teks dan satu uji gambar

# Tahap 1: SEMUA referensi dulu. Selama belum lengkap, pipeline menolak membuat episode.
python run.py refs --semua            # membuat 72 sheet yang kurang (62 latar, 10 tokoh) + lembar kontak refs/auto/KONTAK_*.png
python run.py setujui L07 L08 K16     # setujui sheet yang sudah Anda lihat (atau: setujui --semua)
python run.py tolak L19 --catatan "the factory must have three chimneys"   # tolak; lalu jalankan refs --semua lagi
python run.py pindai                  # baris pertama menyebut gerbang referensi terbuka atau tertutup

# Tahap 2: episode, setelah gerbang terbuka
python run.py semua -e 2              # satu episode sungguhan
python run.py lanjut --jumlah 3       # kerjakan 3 episode bolong berikutnya
```

Uji alur tanpa Vertex: tambahkan `--tiruan` pada perintah mana pun (gambar tiruan). Setelah uji tiruan, hapus `refs/auto/` dan jalankan `python run.py data` supaya status referensi kembali ke semula.

Dengan Claude Code di folder ini, cukup ketik "lanjut". `CLAUDE.md` menyuruhnya memindai, membereskan yang menunggu tinjauan, memproduksi yang bolong, dan memeriksa hasilnya, berulang sampai 300 video jadi.

Mulailah dari satu episode. Setelah hasilnya Anda setujui, baru jalankan rentang, misalnya `-e 1-15`. Semua tahap bisa dilanjutkan: yang sudah lolos tidak dibuat ulang.

`doctor` penting dijalankan lebih dulu. ID model di `config.yaml` adalah perkiraan terbaik saat repo ini dibuat dan belum diverifikasi di project Anda. Kalau `doctor` menyebut sebuah model tidak terlihat, ganti ID-nya di `config.yaml` dengan yang ada di daftar.

## Tahap dan QC di tiap tahap

| Perintah | Yang dibuat | QC otomatis | Kalau gagal |
|---|---|---|---|
| `refs` | Sheet latar L07 sampai L68 dan sheet tokoh yang belum lolos, untuk seluruh seri | Juri model membandingkan sheet dengan deskripsi dan catatan koreksi | Dibuat ulang sampai 3 kali. Yang lolos QC tetap menunggu persetujuan Anda; tidak ada episode yang dibuat sebelum semuanya disetujui |
| `naskah` | Dialog untuk balon percakapan, kotak keterangan seperlunya, SFX per frame, dan adegan untuk ketukan gagal. Tanpa narator | Aturan pasti (panjang, tanda pisah, titik tiga, Ethylene tidak berbicara) lalu juri naskah (gagasan inti terlihat, tidak generik, penutur ada di frame) | Ditulis ulang sampai 3 kali dengan daftar masalahnya |
| `panel` | Satu gambar 4:5 per frame, tanpa teks | Cek lokal (ukuran, rasio, bingkai sheet, kembaran panel sebelumnya) lalu juri gambar dengan 10 butir wajib | Dibuat ulang dari nol sampai 3 kali dengan instruksi perbaikan, lalu ditandai |
| balon (bagian dari `video`) | Posisi balon, kotak keterangan, dan SFX di tiap panel | Juri melihat panel berbalon: wajah terlihat, aksi terlihat, ekor ke penutur yang benar, teks utuh, tidak bertumpuk | Ditata ulang sampai 3 kali dengan catatan perbaikan, lalu ditandai dan video tidak lolos |
| klip pembuka (bagian dari `video`) | Klip bergerak dari panel terkuat | Juri membandingkan bingkai awal, tengah, akhir dengan panel aslinya: desain tetap, tanpa teks, tanpa distorsi | Dibuat ulang sekali; kalau gagal lagi klip dibuang dan pembuka memakai gambar diam |
| `video` | Dua Short 1080x1920 per episode (A dan B): pembuka dari momen terkuat, judul, balon percakapan di dalam panel, guncangan dan kilat di frame aksi, musik dan efek suara sintetis, penutup menggantung. Tanpa suara narator | Teknis (ukuran, durasi, suara) lalu juri melihat lima bingkai video jadi: judul terbaca dan tidak menutup wajah, teks utuh, tanpa cacat, penutup terbaca. Video tidak dibuat kalau ada panel yang belum lolos | Ditandai di status |

Sepuluh butir wajib untuk panel: satu panel, tanpa teks, bukan tata letak sheet, gaya 3D, adegan sesuai, tokoh sesuai sheet, latar sesuai sheet, mata Gala tertutup, Ethylene tanpa mulut, anatomi wajar. Satu saja gagal, panel tidak lolos.

Ketukan gagal dari bible otomatis menjadi satu frame tambahan (kode berakhiran `.g`), sehingga sebagian besar episode punya 17 frame.

## Peran manusia

QC otomatis menyaring, bukan menjamin. Juri adalah model yang bisa salah, jadi tiga pemeriksaan ini tetap perlu mata manusia:

1. **Sheet referensi buatan otomatis** (`refs/auto/`, lembar kontak `KONTAK_*.png`). Ini gerbang wajib: lolos QC model belum cukup, tiap sheet baru dipakai setelah Anda setujui. Satu sheet latar yang keliru merusak semua panel di lokasi itu.
2. **Lembar kontak** `out/epNNN/kontak_NA.png`. Semua panel satu sub-episode dalam satu gambar; bingkai merah berarti belum lolos.
3. **Video akhir**, sekali tonton sebelum diunggah.

Memperbaiki satu panel:

```bash
python run.py ulang 2B.1c --catatan "the kicking leg is on the right side of the image"
```

Catatan ditulis dalam bahasa Inggris karena diteruskan ke model gambar. Mengubah teks: sunting `out/epNNN/naskah.json`, lalu `python run.py video -e N --paksa`.

## Perkiraan biaya dan waktu

Total sekitar 2.500 frame. Dengan rata-rata 1,5 percobaan per frame, itu sekitar 3.800 gambar, 3.800 pemeriksaan juri, 70 sheet referensi, 150 naskah, 2.500 permintaan posisi balon beserta 2.500 pemeriksaan balon, 300 klip video pembuka, dan 600 pemeriksaan video dan klip. Harga per gambar berubah-ubah dan **perlu Anda cek di halaman harga Vertex AI** sebelum menjalankan rentang besar. `out/pemakaian.json` mencatat jumlah panggilan supaya bisa dicocokkan dengan tagihan.

## Yang belum beres

- Panggilan Vertex belum pernah diuji (lihat atas).
- Posisi balon ditentukan model yang melihat panelnya, supaya tidak menutup wajah dan ekornya mengarah ke penutur. Kalau model gagal, dipakai posisi cadangan di tepi panel dengan ekor pendek. Posisi tersimpan di `out/epNNN/tata.json` dan bisa disunting tangan (angka 0 sampai 1 dari kiri atas panel).
- Sheet tokoh K16, K20, K43, K45, K46, K51, K58, K64, K65 belum lolos dan K68 belum ada; tahap `refs` akan membuat ulang dengan catatan koreksinya.
- Audit naskah putaran kedua sudah mencakup kesepuluh season, dan 45 catatan kesinambungan sudah ditangani (rincian di `docs/audit-mutu.md`, perbaikan di `bible/perbaikan.json`). Perbaikan itu belum diperiksa silang antarseason.
- Episode 1 dan 2 versi komik halaman ada di `arsip/` dan dibuat dengan cara manual. Pipeline ini menghasilkan video komik per frame, bukan halaman komik.
- Musik dan efek suara disintesis oleh kode (gaya sama dengan Short Episode 1), bukan musik berlisensi.
- Klip pembuka bergerak memakai model video (Veo). Ini bagian termahal per detik dan ID modelnya paling mungkin perlu diganti. Matikan dengan `veo_pembuka: false`; pembuka lalu memakai gambar diam.
- `arsip/contoh/` memuat Short Episode 1 buatan tangan sebagai acuan rasa. Pipeline memakai bahasa yang sama (balon di dalam panel, SFX, musik, tanpa narator), tetapi menampilkan satu panel per layar, bukan kamera yang berjalan di atas halaman komik.
