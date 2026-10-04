# Panduan untuk Claude di repo ini

Proyek: seri animasi anak *Gala Ignis & The Galians*. Sasaran akhir repo ini: **setiap episode di semua season dan semua arc punya dua video Short vertikal (bagian A dan B), total 300 video dari 150 episode**, dengan tokoh dan latar sesuai sheet referensi.

Semua komunikasi dengan pengguna dalam bahasa Indonesia, tanpa tanda pisah panjang. Bersikap kritis: jangan memuji hasil yang belum kamu lihat sendiri.

## Mode otomatis: pindai lalu tambal yang bolong

Setiap kali sesi dimulai, atau pengguna berkata "lanjut", "lanjutkan", "pindai", atau tidak memberi tugas lain, jalankan putaran ini tanpa bertanya dulu:

0. **Gerbang referensi (wajib lebih dulu).** Tidak ada satu pun episode yang boleh dibuat sebelum SEMUA sheet tokoh dan latar seri ini lolos dan disetujui pengguna. Pipeline menolak tahap naskah, panel, dan video selama gerbang tertutup. Urutannya:
   - `python run.py refs --semua` membuat semua sheet yang kurang (62 latar, 10 tokoh saat repo ini dibuat) dan lembar kontak `refs/auto/KONTAK_*.png`.
   - Buka setiap lembar kontak dan setiap sheet. Bandingkan dengan deskripsinya (`anchor` di `data/refs.json`) dan dengan gaya sheet buatan pengguna di `refs/karakter/` dan `refs/latar/`. Tulis penilaianmu per kode untuk pengguna: cocok, atau salah beserta sebabnya.
   - **Persetujuan adalah hak pengguna.** Tunjukkan lembar kontak dan penilaianmu, lalu tunggu. Jalankan `python run.py setujui KODE ...` hanya untuk kode yang pengguna setujui, dan `setujui --semua` hanya kalau pengguna berkata semua disetujui.
   - Sheet yang salah: `python run.py tolak KODE --catatan "<koreksi bahasa Inggris>"`, lalu `python run.py refs --semua` lagi.
   - Ulangi sampai `python run.py pindai` menulis "Gerbang referensi TERBUKA".
1. **Pindai.** `python run.py periksa` lalu `python run.py pindai`. Baca `out/PINDAI.md`. Sebutkan ke pengguna dalam satu baris: berapa episode selesai, sebagian, menunggu tinjauan, belum mulai.
2. **Kalau belum pernah ada panggilan Vertex yang berhasil** (`out/pemakaian.json` belum ada), jalankan `python run.py doctor` dulu. Kalau ada model yang tidak terlihat, ganti ID-nya di `config.yaml` dengan yang ada di daftar, lalu ulangi `doctor`. Jangan lanjut produksi sebelum uji teks dan uji gambar berhasil.
3. **Bereskan yang menunggu tinjauan lebih dulu**, urut dari nomor episode terkecil, sesuai kolom "Langkah berikutnya":
   - Panel gagal: buka `out/epNNN/kontak_NA.png` atau `kontak_NB.png`, lalu `python run.py ulang KODE --catatan "<instruksi bahasa Inggris, sebut sisi gambar kiri atau kanan>"`.
   - Naskah gagal: sunting `out/epNNN/naskah.json` sampai memenuhi aturan, ubah `qc.lolos` menjadi true, lalu `python run.py video -e N --paksa`.
4. **Produksi yang bolong.** `python run.py lanjut --jumlah 1`. Perintah ini memilih episode bolong pertama dan menjalankan semua tahapnya: referensi, naskah, panel, video.
5. **Periksa hasilnya sendiri** dengan daftar di bawah. Setiap tahap sudah punya juri otomatis (sheet, naskah, panel, posisi balon, klip pembuka, video jadi), tetapi juri adalah model: lolos QC otomatis belum berarti benar. Tidak ada tahap yang boleh dilewati tanpa diperiksa.
6. **Ulangi dari langkah 1** sampai `out/PINDAI.md` menunjukkan 150 episode selesai.

Berhenti dan lapor ke pengguna, jangan memaksa, kalau:

- episode yang sama gagal dua putaran berturut-turut dengan sebab yang sama;
- sebuah panel masih salah setelah tiga kali `ulang`;
- muncul galat kuota, tagihan, atau izin dari Google Cloud;
- kamu akan menjalankan lebih dari lima episode sekaligus: sebutkan dulu perkiraan jumlah gambar (sekitar 17 panel dan 2 klip pembuka per episode, dikali rata-rata 1,5 percobaan) dan tunggu persetujuan, karena berbiaya.

Setiap berhenti, laporkan: episode yang selesai di sesi ini, yang diperbaiki, yang masih meragukan beserta gambarnya, dan angka di `out/pemakaian.json`.

## Seperti apa video yang benar

Acuan rasa: `arsip/contoh/Gala_Ignis_Episode_01_Short.mp4`. Itu dibuat tangan dari halaman komik; pipeline ini menghasilkan bentuk yang setara secara otomatis, bukan salinannya. Setiap Short harus punya:

- pembuka dari momen terkuat (klip bergerak kalau model video tersedia, gambar diam dengan dorongan kamera kalau tidak), lalu judul besar;
- kilat putih dan guncangan di frame aksi, dan SFX di frame yang memang berbunyi;
- cerita dibawa balon percakapan di dalam panel, tanpa suara narator; balon tidak menutup wajah dan ekornya mengarah ke penutur;
- musik yang naik menuju puncak dan hentakan di puncak;
- penutup yang menggantung: "Bersambung" di bagian A, judul episode berikutnya di bagian B.

Kalau sebuah Short terasa datar, penyebabnya hampir selalu naskah: tidak ada SFX, tidak ada kalimat yang menggantung di akhir bagian A, atau `judul_short` yang lemah. Perbaiki di `naskah.json`, lalu buat ulang videonya.

## Daftar periksa per episode

Panel (buka lembar kontak, periksa SEMUA panel, termasuk yang ditandai lolos):

- Mata Gala tidak pernah terlihat; lensa kacamata gelap dan tertutup.
- Ethylene: bola api kuning keemasan, dua mata titik putih, tanpa mulut, tanpa lengan dan kaki. Ia ada di dekat Gala kecuali plot menyatakan lain (Episode 38 dan 76 sampai 88; di Episode 27 ia hadir tetapi membeku).
- Tokoh sama dengan sheet (warna rambut, zirah, aksesori). Gala memakai pin roset di dada kanan atas sejak frame 15A.2c.
- Latar sama dengan sheetnya, dan sama antara panel yang berlatar sama.
- Arah kamera masuk akal: apa yang ada di belakang tokoh sesuai arah hadapnya.
- Sisi tubuh konsisten sepanjang episode (kaki atau tangan yang dipakai).
- Tidak ada teks, bingkai, atau tata letak sheet di dalam gambar. Gaya render 3D, bukan 2D.
- Dua panel berurutan tidak hampir sama.

Naskah (baca `naskah.json` seluruhnya; seri ini tanpa narator, jadi cerita harus terbaca dari dialog):

- Kotak keterangan ("narasi") hanya untuk tempat dan waktu, paling banyak di empat frame.
- Gagasan inti episode terlihat sekali di sekitar puncak, dengan kata sederhana.
- Tokoh gagal dulu sebelum berhasil.
- Ethylene hanya berbunyi pendek seperti "Pip!".
- Tidak ada kalimat pahlawan generik, tidak ada tanda pisah panjang, paling banyak dua titik tiga.
- Gagasan berlabel sains adalah penyederhanaan; jangan disajikan sebagai fakta.

Video (ambil bingkai di detik 1, di tengah, dan 1 detik sebelum akhir dengan ffmpeg, lalu lihat):

- Judul pembuka dan penutup terbaca dan tidak menutupi wajah.
- Balon tidak menutup wajah, tangan, atau aksi utama, tidak saling bertumpuk, dan ekornya mengarah ke penutur yang benar.
- SFX tidak menutupi kepala tokoh.
- Kalau posisi salah, sunting `out/epNNN/tata.json` untuk kode frame itu (angka 0 sampai 1 dari kiri atas panel), lalu `python run.py video -e N --paksa`.

Enam belas aturan mutu lengkap ada di `docs/00-inti.md` bagian 6.

## Batas

- Jangan menandai referensi atau panel sebagai lolos tanpa melihat gambarnya.
- Jangan mengubah `data/*.json` dengan tangan. Sumbernya `bible/`; setelah mengubah, jalankan `python run.py data` lalu `python run.py periksa`.
- Sheet di `refs/karakter/` dan `refs/latar/` adalah buatan pengguna yang sudah disetujui; jangan ditimpa.
- Jangan mengubah cerita (isi frame di `bible/`) untuk mengakali panel yang sulit digambar. Laporkan saja.
- Jangan menghapus isi `out/` tanpa diminta; itu hasil berbayar.
