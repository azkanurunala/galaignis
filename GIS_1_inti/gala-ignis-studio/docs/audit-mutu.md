# Audit Mutu Seluruh Seri (3 Oktober 2026)

*Gala Ignis & The Galians · 150 episode · 2.400 frame · audit otomatis ditambah gagasan inti yang ditulis per episode*

## Ringkasan

- **Gagasan inti:** 150 episode sekarang punya satu gagasan inti (65 berlabel sains, 85 berlabel cerita).
- **Pembuka video:** 78 episode dibuka dengan frame yang tenang dan diberi usulan frame aksi sebagai pembuka; 15 episode sudah dibuka dengan aksi; 57 episode tidak punya frame aksi yang jelas dan pembukanya perlu dipilih manual.
- **Ethylene:** sebelum audit, Ethylene hanya ada di 116 dari 958 frame yang memuat Gala, dan 71 episode sama sekali tanpa Ethylene. Sekarang ditambahkan otomatis di 395 frame.
- **Frame mirip:** 18 pasang frame di 17 episode punya deskripsi yang hampir sama; ditandai di bawah judul episodenya, belum diubah.
- **Ketukan gagal:** 150 episode sekarang punya baris *Ketukan gagal*. Di 43 episode ketukan itu sudah ada di frame yang ada; di 107 episode ditulis satu ketukan baru beserta titik sisipnya. Ini rencana, jumlah frame tetap 2.400.
- **Rilis:** tiap episode dirilis sebagai dua Short (sub-episode A lalu B).
- **Puncak arc:** 30 episode kelipatan lima diberi satu komplikasi baru sebagai bahan perpanjangan menjadi tiga sub-episode. Belum ditulis menjadi frame.
- **Aturan mutu:** 16 aturan produksi ditambahkan ke `00-inti.md` bagian 6.
- **Episode 2** di bible disesuaikan dengan keputusan komik: ikatan terlemah, Ethylene menyelam ke kaki, sisi kaki tidak lagi disebut.

## Batas audit ini

- Penambahan Ethylene memakai aturan otomatis: hanya shot medium, wide, dan sejenisnya; bukan close-up, sudut pandang pertama, atau puncak aksi; Episode 27, 38, dan 76 sampai 88 tidak disentuh. Aturan ini belum diperiksa frame per frame, jadi sebagian frame mungkin tidak cocok dan perlu dicek saat episodenya diadaptasi.
- Frame pembuka dipilih dengan skor kata kunci aksi, bukan dengan melihat gambarnya. Anggap sebagai usulan.
- Gagasan berlabel sains adalah penyederhanaan dan belum diperiksa ahli.
- Storyboard tidak memuat dialog, jadi aturan dialog baru bisa diterapkan saat tiap episode diadaptasi menjadi komik.
- Ketukan gagal dan komplikasi puncak arc ditulis per season oleh sepuluh proses terpisah dan hanya diperiksa secara otomatis (kode frame ada, format benar) ditambah contoh acak. Belum dibaca satu per satu, dan belum dicek bentrok dengan episode sesudahnya.
- Rumusannya seragam: 43 dari 107 ketukan berpola "mencoba, tetapi gagal", dan 27 dari 30 komplikasi berpola "harus memilih". Variasikan saat adaptasi supaya tidak terasa satu cetakan.

## Audit putaran kedua (3 Oktober 2026)

Ketukan gagal, komplikasi puncak arc, pembuka video, dan frame mirip dibaca ulang per episode oleh pemeriksa terpisah untuk kesepuluh season (10 dari 10).

- Ketukan gagal sekarang: 122 ditambahkan sebagai rencana, 28 sudah ada di frame. Beberapa status dibalik dari sudah ada menjadi tambah karena frame yang ditunjuk bukan kegagalan sungguhan.
- Pola kalimat mencoba lalu tetapi atau namun tersisa di 11 dari 122 ketukan. Pola harus memilih tersisa di 0 dari 30 komplikasi puncak arc.
- Pembuka video dipilih manual untuk 53 episode. Saran konkret frame mirip ditulis untuk 17 episode.
- Di beberapa episode tabel lama hanya mencatat jumlah frame mirip, sehingga pasangan frame yang disebut di saran adalah dugaan pemeriksa.

### Kesinambungan

Pemeriksa mencatat 45 masalah kesinambungan. 42 diperbaiki dengan menulis ulang 58 frame yang sudah ada dan 2 ringkasan, tanpa mengubah jumlah atau kode frame. Sisanya dinilai tidak perlu diubah, dengan alasan di tabel. Perbaikannya ada di `bible/perbaikan.json`.

Batas: tiap perbaikan diperiksa terhadap frame di sekitarnya oleh pemeriksa season itu saja. Belum ada pemeriksaan silang antarseason, dan baru Season 2 yang dibaca penuh oleh penyunting utama.

| Ep | Frame | Masalah | Tindakan | Frame diubah |
|---|---|---|---|---|
| 1 | 1B.2d | Ultimatum 24 jam tidak pernah dirujuk atau dihitung mundur di Episode 2 sampai 4, sehingga tenggatnya hilang sebelum kelulusan di 5B.2c. | Hitung mundur ultimatum ditambahkan sebagai layar di 2A.1a (21 jam), 3A.2d (6 jam), dan 4A.1a (0 jam, ujian evaluasi dimulai) sehingga tenggat terbawa sampai kelulusan di 5B.2c. | 2A.1a, 3A.2d, 4A.1a |
| 4 | 4B.2d | Siluet peretas dengan pemancar sinyal tidak pernah muncul lagi; Episode 5 hanya menghancurkan inti kristal di 5B.1c dan nasib peretas tidak disinggung. | 5B.1c menaruh inti kristal di pemancar yang dipegang siluet peretas, dan 5B.2a menunjukkan siluet itu pecah menjadi piksel dan lenyap saat sambungan terputus tanpa membuka identitasnya. | 5B.1c, 5B.2a |
| 5 | 5A.2a | Dua rekan taruna muncul tanpa nama di dalam simulasi yang terkunci dan tidak dijelaskan cara masuknya, lalu Aila dan Dhruva baru disebut namanya di 6B.1c tanpa perkenalan. | 5A.1b kini memperlihatkan tiga kapsul yang ikut terkunci dan 5A.2a menamai kedua rekan sebagai Aila dan Dhruva yang termaterialisasi dari ujian yang sama, sehingga cara masuk dan perkenalan mereka terjawab sebelum 6B.1c. | 5A.1b, 5A.2a |
| 8 | 8A.1a | Tim menganalisis puing dengan santai padahal para pekerja masih terkurung di ruang samping sejak 7B.1a dan baru dibebaskan di 8B.2c. | 8A.1a ditambah Aila dan Dhruva di latar belakang yang berusaha membuka pintu ruang samping yang terkunci es, sehingga pekerja tidak diabaikan dan pembebasan di 8B.2c tetap masuk akal setelah serangan Cryo-Walker memotong upaya itu. | 8A.1a |
| 15 | 15A.2b | Pin disematkan di dada kanan atas, padahal ringkasan episode menyebut desain v2 memakai pin di dada kiri dan baru berlaku mulai 15A.2c. | Frame sudah benar sesuai desain terkunci (pin di dada kanan atas), jadi ringkasan Episode 15 yang dibetulkan dari kiri ke kanan atas dan diberi keterangan bahwa pin disematkan di 15A.2b sehingga v2 tampil mulai 15A.2c. |  |
| 19 | 19B.1d | Himakara lenyap menjadi embun beku dan tidak pernah muncul atau disebut lagi sampai akhir season, sehingga nasibnya menggantung. | Menegaskan di 19B.1d bahwa Himakara musnah dan hanya zirah kosong dengan inti padam yang tersisa, sehingga nasibnya tidak menggantung. | 19B.1d |
| 20 | 20A.2c | Aila dan Dhruva masih menahan dua gerbang dari serbuan Cryo-Guard di 19B.2b dan 19B.2c, tetapi tidak ada frame yang menunjukkan mereka lepas sebelum regu melompati ngarai. | Menambah klausa di 20A.1d bahwa Aila dan Dhruva melepas kedua gerbang dan berlari ke ramp saat evakuasi, sehingga lompatan di 20A.2c punya sebab. | 20A.1d |
| 22 | 22B.2a | Aila dan Dhruva ditugasi menjaga warga di stasiun pada 21B.2b, lalu tiba di atap rumah sakit tanpa penjelasan siapa yang menggantikan mereka. | Menambah klausa di 22B.2a bahwa petugas kota mengambil alih penjagaan warga di stasiun sebelum Aila dan Dhruva tiba. | 22B.2a |
| 27 | 27A.2d | Gala sudah menuju pintu singgasana padahal Aila dan Dhruva baru dibebaskan dari es di 27B.1a dan 27B.1b; urutannya terbalik. | Mengubah 27A.2d sehingga Gala hanya melihat pintu singgasana lalu berbalik mencari regunya, jadi pembebasan di 27B.1 terjadi sebelum ia menuju pintu di 27B.2d. | 27A.2d |
| 27 | 27A.1b | Frame 27A.1b sampai 27A.2c menampilkan Ethylene bersama Gala, bertentangan dengan catatan plot bahwa Ethylene tidak bersama Gala di episode 27. | Tidak diubah: episode 27 memang tentang Ethylene yang membeku lalu hidup kembali, jadi kehadirannya benar. Catatan plot yang menyebut ia absen keliru dan sudah dibetulkan. |  |
| 35 | 35A.1c | Gala melepas lilitan kain sarung dari lengan tanpa alasan padahal 34B.1d menunjukkan lilitan itulah yang menahan erosi, sehingga anjloknya integritas ke 58 persen di 35B.2b terasa dibuat-buat. | Gala tidak lagi melepas lilitan melainkan mengencangkannya, dan ketukan gagal 35B.1c diberi sebab: soket mati menyedot pijar emas lilitan itu sehingga erosi ke goggles dan angka 58 persen punya alasan. | 35A.1c, 35B.1c |
| 38 | 38A.2d | Kalia menyebut dua Ethylene sebagai tiruan Wraith dan 38B.1c memecahnya jadi kaca jam, padahal ringkasan dan 38A.2a menyatakan ketiganya salinan Ethylene dari tiga masa. | Peringatan Kalia diganti menjadi dua gema Ethylene dari masa lain (bukan tiruan Wraith), dan 38B.1c menyebut kedua salinan masa lain itu membeku jadi kaca jam lalu retak sehingga cocok dengan ringkasan, 38A.2a, dan pecahan kaca di 38B.1d. | 38A.2d, 38B.1c |
| 43 | 43B.1d | Ethylene masuk ke soket monumen di 40A.1d dan tidak pernah digambarkan keluar, tetapi di sini sudah menempel di pipi Gala. | 43B.1d tidak diubah; 40A.2d kini menunjukkan Ethylene keluar dari soket dan hinggap di bahu Gala setelah menara menyala (flags ditambah S). | 40A.2d |
| 44 | 44A.1a | Kain sarung dinyatakan berjumbai dan tidak akan bertahan lama di 36B.2b dan 36B.2c, tetapi di sini menahan beban Buster Kick tanpa ada frame perbaikan. | Ketukan gagal 44A.1a dibiarkan; 44A.1b ditambah klausa bahwa cahaya menara merajut kembali serat kain sarung yang berjumbai sebelum Buster dilepas. | 44A.1b |
| 45 | 45A.2b | HUD mencatat hanya 7 menit 41 detik berlalu di lini masa utama, padahal 42A.1b memasang penstabil bersama teknisi akademi dan 42B.2c masih meminta lima menit lagi. | Tidak diubah: hanya beberapa menit berlalu adalah inti paradoks waktu season ini dan judul sub-episodenya. Kalau adegan lini masa utama di episode 42 terasa terlalu panjang, yang dipadatkan adalah episode 42. |  |
| 49 | 49B.2c | Gala kembali menendang dengan api padahal sejak 47A.2a ia tahu Batik Terbalik menyerap api; sebaiknya tendangan ini silat murni atau diberi alasan refleks. | Tendangan Gala dijadikan silat murni tanpa api, sesuai pelajaran di 47B.1c, dan tetap mendorong Wirasena ke jendela untuk 49B.2d. | 49B.2c |
| 53 | 53B.2d | Aila ikut menarik Gala dari sungai, padahal di 52B.2b ia menolak rencana dan hanya Dhruva yang menawarkan menunggu di batas hutan di 52B.2c. | Di 52B.2d Aila dibuat mengalah dan ikut menunggu di batas hutan bersama Dhruva, lalu 53B.2d menyebut keduanya datang berlari dari batas hutan. | 52B.2d, 53B.2d |
| 58 | 58A.1c | Kain kuno Wirasena membelit di udara padahal di 55A.2c kain itu ditancapkan ke soket inti dan tidak pernah dicabut. | Yang membelit kain sarung Gala kini benang hitam-ungu yang menjulur dari kain kuno, sedangkan kain kuno tetap tertancap di soket sesuai 55A.2c dan 59A.2a. | 58A.1c |
| 58 | 58A.2c | Layar kota menampilkan relief berwajah utuh, padahal satu-satunya gambar itu ada di gulungan yang dibawa kabur Wirasena di 49B.2d; sumber gambar Maheswari tidak dijelaskan. | Sumber gambar dijelaskan: Maheswari memasang kristal rekaman brankas arsip (51B.1d sampai 51B.2b) ke konsol siaran dan layar kota memutar rekaman itu. | 58A.2b, 58A.2c |
| 59 | 59A.2a | Tendangan berapi memutus tautan hitam-ungu, padahal sejak 47A.2a api selalu terserap; perlu satu frame yang menunjukkan api tenunan baru tidak bisa diserap. | Ditambahkan sebab sebelum tendangan: api di boots berpola tenunan baru dan benang hitam-ungu terlihat gagal menyerapnya, sejalan dengan override 0% di 57A.2d; 59A.2a sendiri tidak diubah. | 59A.1c, 59A.1d |
| 69 | 69B.1a | Ibu Dhruva terbaring di samping Hub, padahal Hub untuk ibunya sudah dibongkar Aila di 63A.1a dan Dhruva sudah tahu isinya; tidak ada frame yang menjelaskan Hub kedua. | Hub di samping ibu Dhruva dijelaskan sebagai Hub pengganti yang baru dikirim Vextron, sehingga tidak bentrok dengan Hub pertama yang dibongkar Aila di 63A.1a. | 69B.1a |
| 70 | 70B.2a | Regu berkumpul di atap rumah Dhruva walau Gala masih buronan dan drone sudah mendatangi rumah itu di 69B.2a, sehingga tempat itu seharusnya tidak aman. | Tempat berkumpul dipindah dari atap rumah Dhruva ke atap pasar tua di distrik lama yang bebas Hub (sudah mapan sebagai tempat aman di episode 67); 70B.2d tetap cocok karena hanya menyebut atap. | 70B.2a |
| 71 | 71A.2d | Maheswari dan pengawal dewan bekerja sama terbuka dengan Gala padahal status buronan dari 66B.2d belum pernah dicabut dalam frame mana pun sebelum 75A.2a. | Ditambahkan Maheswari merobek selebaran buronan Gala, sehingga dewan terlihat menolak status buronan sebelum bekerja sama dengannya; permintaan maaf publik di 75A.2a tetap berlaku. | 71A.2d |
| 74 | 74B.1b | Dhruva menerobos masuk ke ruang puncak padahal tugasnya menahan lobi di 73A.2a, dan tidak ada frame yang menunjukkan front lobi selesai atau ia naik. | Ditambahkan klausa bahwa Dhruva naik lewat poros lift setelah Vex-Guard di lobi roboh saat tenunan terurai di 74A.2c, sehingga kedatangannya di ruang puncak punya sebab. | 74B.1b |
| 82 | 82B.2a | Aila dan Dhruva baru tiba bersama Agni padahal episode 81 berakhir dengan seluruh regu berkemah bersama di 81B.2a; tidak ada frame yang menunjukkan Gala berangkat lebih dulu. | 81B.2d kini menunjukkan Gala berangkat sendirian ke tepi kawah selagi yang lain beristirahat di ceruk yang didinginkan Agni, dan 82B.2a menyebut Aila dan Dhruva menyusul dari kemah. | 81B.2d, 82B.2a |
| 83 | 83A.1a | Ethylene bersama regu di tepi kawah pada 82B.1b lalu hilang tanpa penjelasan sepanjang episode 83 dan baru muncul lagi di 84A.1d. | 82B.1b ditambah klausa Ethylene melayang turun ke kawah untuk menjaga Jantung, sehingga ketidakhadirannya di episode 83 dan posisinya di 84A.1d terjelaskan. | 82B.1b |
| 85 | 85B.1a | Agni yang terluka di 83B.1c tidak terlihat ikut menuruni kawah di 84A.1a maupun diterbangkan keluar di 85A.2d, tetapi sudah ada di ceruk. | 84A.1a kini menunjukkan Agni yang terluka ditinggal di ceruk di tepi kawah, dan 85B.1a menyebut regu mundur ke ceruk tempat Agni menunggu. | 84A.1a, 85B.1a |
| 87 | 87A.1b | Kain sarung adalah sumber selubung panas bagi Aila dan Dhruva sejak 77B.2a dan menipis di 85B.1c, tetapi saat Gala masuk ke Hampa tidak dijelaskan apa yang melindungi keduanya dari panas. | 87A.1b dan 87A.2c menjelaskan bahwa ujung kain sarung yang dipegang Dhruva tetap memancarkan selubung emas yang melindungi dia dan Aila. | 87A.1b, 87A.2c |
| 90 | 90B.1b | Pusaran pulang terbuka tanpa sebab, padahal pusaran di 76B.1c berasal dari titik plasma dan tidak ada frame yang menunjukkan siapa atau apa yang membukanya kembali. | 90B.1b kini menunjukkan Jantung yang pulih menembakkan titik plasma yang melebar menjadi pusaran pulang, sejalan dengan asal pusaran di 76B.1c. | 90B.1b |
| 94 | 94B.1d | Disebut dua kasur kosong padahal baru Aila yang pergi dan Gala serta Dhruva masih duduk di kamar pada 94B.1c, jadi seharusnya satu kasur kosong. | Mengganti dua kasur kosong menjadi satu kasur kosong milik Aila karena Gala dan Dhruva masih di kamar. | 94B.1d |
| 96 | 96A.2a | Dhruva menemukan gudang persembunyian tanpa ada frame yang menjelaskan bagaimana ia tahu lokasinya setelah Gala dan Nira kabur lewat saluran air di 95B.2a. | Menambah klausa di 96A.2a bahwa Dhruva datang dipandu pesan lokasi yang dikirim Gala ke komlinknya. | 96A.2a |
| 99 | 99A.1d | Nira sudah menunggu di atap untuk menangkap chip padahal Aila dan Nira baru pertama bertemu di 99B.2a dan tidak ada frame yang menunjukkan mereka menyepakati saluran itu. | Aila kini mengenali Nira bersama Gala di atap pada 98B.2d, lalu di 99A.1b melihat kilau emitter Nira yang mengawasi dari atap seberang sehingga chip sengaja dikirim ke sana dan di 99A.1d Nira menangkapnya tanpa janji sebelumnya; ringkasan Ep 99 disesuaikan karena tidak ada saluran yang disepakati. | 98B.2d, 99A.1b, 99A.1d |
| 112 | 112A.1b | Visor Subjek Zero tertinggal retak di 110B.2b, tetapi sejak 112A.1b tidak pernah dijelaskan apakah wajahnya kini tanpa visor atau memakai pengganti. | Frame 112A.1b kini menyebut anak itu masih memakai visor putihnya yang retak dan sompal di satu sudut, sesuai serpihan yang tertinggal di 110B.2b. | 112A.1b |
| 114 | 114B.2a | Dinding baja yang menutup di 113B.2a terbuka begitu saja di 114B.2a tanpa sebab; kaitkan dengan pembobolan Nira di 113B.2c atau ledakan rangka di 114B.1c. | Frame 114B.2a kini menyebut ledakan rangka di 114B.1c memutus daya kunci sehingga dinding baja terbuka. | 114B.2a |
| 116 | 116B.1b | Dhruva masih di gudang pelabuhan menangkap Aila di 115A.1d, tetapi di 116B.1b sudah berdiri di kaki monumen mendahului Gala yang terbang. | Frame 115A.2d ditambah klausa Maheswari mengirim Dhruva lebih dulu ke monumen, sehingga kehadirannya di 116B.1b punya sebab. | 115A.2d |
| 117 | 117B.1b | Aila ditembak jatuh di 115A.1c dan bergabung lagi di 117B.1b tanpa satu frame pun yang memperlihatkan ia pulih. | Frame 115A.1d menegaskan Aila hanya terguncang dan tidak terluka, dan 117B.1b memperlihatkan ia sudah pulih dan terbang lagi. | 115A.1d, 117B.1b |
| 118 | 118B.2b | Anak itu tiba-tiba punya gauntlet di 118B.2b padahal ia keluar dari tabung tanpa perlengkapan dan tidak ada frame yang memberinya. | Gauntlet di 118B.2b diganti kepalan tangan kosong karena anak itu tidak pernah diberi perlengkapan. | 118B.2b |
| 124 | 124B.1a | Utusan berdiri di bawah menara dan tidak mengejar di 123B.2d, tetapi di episode 124 warga dan regu mengelilingi menara tanpa penjelasan ke mana Utusan pergi. | Menambah klausa di 123B.2d bahwa Utusan berbalik dan pergi meninggalkan menara, sehingga kaki menara kosong saat warga mengelilinginya di episode 124 dan selaras dengan 125B.2b (Utusan menonton dari bukit jauh). | 123B.2d |
| 127 | 127B.1b | Perisai Dhruva memudar kelabu di 123B.2b tetapi dipakai normal sebagai jangkar tanpa pernah diperlihatkan pulih. | Menambah klausa di 124B.2d yang memperlihatkan warna perisai Dhruva pulih saat simpul barat menyala, sehingga pemakaiannya di 127B.1b wajar tanpa mengubah frame itu. | 124B.2d |
| 129 | 129B.1b | Aila menempelkan tangan ke simpul timur padahal menaranya ada di dasar laut (127A.2c) dan ia sedang bertarung di permukaan pada 129A.2b. | Menulis ulang 129B.1b agar Aila menyelam dengan gelembung udara ke menara laut sebelum menempelkan tangan, dan Gala disebut menyentuh simpul di dalam pohon. | 129B.1b |
| 133 | 133A.1a | Nira berada di hutan awan bersama Gala dan Arka sampai 129A.1d, lalu tiba-tiba sudah di pusat komunikasi akademi tanpa frame kepindahan. | Menambah keterangan di 130B.1d bahwa Nira berada di kapal terpisah yang pulang ke akademi, sehingga kepindahannya dari hutan awan ke pusat komunikasi terjelaskan dan cocok dengan ketidakhadirannya di gunung api (episode 131). | 130B.1d |
| 135 | 135B.2a | Regu di gunung api selatan menatap ke selatan, padahal palung berada di tengah laut menurut 125A.1b dan 135A.2b sehingga seharusnya mereka menatap utara. | Membetulkan arah di 135B.2a dari selatan menjadi utara ke arah laut tengah, dan menyamakan deskripsi Inggrisnya. | 135B.2a |
| 144 | 144A.2d | Anak berjas hujan kuning muncul tanpa pengenalan di season ini dan baru dipakai lagi di 150A.2b; anak yang menangkap sprite di 139A.2d sebaiknya ditegaskan sebagai anak yang sama. | Menegaskan anak di 139A.2d sebagai anak berjas hujan kuning dan menambahkan sprite kecil tangkapannya di bahunya pada 144A.2d, sehingga ia sudah diperkenalkan di season ini sebelum 144 dan 150. | 139A.2d, 144A.2d |
| 146 | 146A.1d | Ribuan warga mengangkat pelita di sekitar monumen padahal 145B.2b menyatakan kelabu sudah mencapai Monumen Atom dan 137A.1b menunjukkan warga di dalam kelabu bergerak sangat lambat. | Menulis ulang 146A.1d agar warga kota berdiri di dalam lingkar cahaya monumen yang masih menahan kelabu (sesuai 137A.1c), sehingga mereka bisa bergerak normal walau kelabu sudah mencapai monumen. | 146A.1d |
| 147 | 147A.1a | Arka meninggalkan simpul Hutan Awan untuk menyusul Gala padahal 142 menyatakan rencana hanya berhasil jika setiap sekutu tetap di tempatnya, dan tidak ada frame yang menunjukkan siapa yang menjaga simpul itu sesudahnya, termasuk di 149A.1a sampai 149A.1c. | Menambah klausa di 147A.1a bahwa Arka menyerahkan obornya kepada tetua Hutan Awan yang tetap menjaga simpul bersama warga sebelum ia berangkat, sehingga simpul tidak kosong. | 147A.1a |

## Tabel per episode

| Ep | Judul | Jenis gagasan | Pembuka video | Ethylene ditambah | Frame mirip |
|---|---|---|---|---|---|
| 1 | Percikan Pertama di Awal Era | sains | frame aksi 1B.1a | 0 |  |
| 2 | Pemeta Molekul | sains | frame aksi 2B.2b | 5 |  |
| 3 | Nanoselulosa Penyeimbang | sains | frame pertama | 3 |  |
| 4 | Simulasi Tanpa Batas | cerita | frame aksi 4A.2a | 6 |  |
| 5 | Sinyal Asing di Ruang Ujian | sains | frame aksi 5B.1d | 4 |  |
| 6 | Panggilan Pertama di Lapangan | sains | frame aksi 6A.2d | 2 |  |
| 7 | Jejak Es di Serat Nano | sains | frame aksi 7A.2b | 0 |  |
| 8 | Sandi Cryo-Tech | sains | frame aksi 8A.2c | 2 |  |
| 9 | Penyelamatan Pabrik Serat Nano | sains | pilih manual | 6 |  |
| 10 | Fajar di Sektor 7 | cerita | pilih manual | 6 |  |
| 11 | Badai Es di Benteng Akademi | sains | frame aksi 11B.1d | 2 |  |
| 12 | Benteng yang Terisolasi | cerita | frame pertama | 4 |  |
| 13 | Pertempuran di Reaktor Inti | sains | frame aksi 13A.2a | 1 |  |
| 14 | Resonansi Galian Buster | sains | frame aksi 14A.2a | 2 |  |
| 15 | Pelantikan Sang Vanguard | cerita | pilih manual | 3 |  |
| 16 | Panggilan dari Benteng Es | sains | frame aksi 16A.2b | 4 |  |
| 17 | Pemutihan Energi | sains | frame pertama | 4 |  |
| 18 | Taktik Selulosa | sains | frame aksi 18A.2c | 8 |  |
| 19 | Penyergapan Himakara | sains | frame aksi 19A.2c | 0 |  |
| 20 | Sabotase Generator Es | sains | frame aksi 20A.2a | 4 |  |
| 21 | Kota dalam Kegelapan | sains | frame aksi 21A.2b | 6 |  |
| 22 | Rantai Resonansi | sains | frame aksi 22A.2c | 6 |  |
| 23 | Pilihan Sang Vanguard | cerita | frame aksi 23A.2a | 6 |  |
| 24 | Pertempuran di Atas Monumen Atom | cerita | frame aksi 24A.2c | 3 |  |
| 25 | Pemulihan Daya Kota | sains | frame pertama | 5 |  |
| 26 | Gerbang Absolute Zero | cerita | frame aksi 26A.2c | 5 |  |
| 27 | Krisis Ionisasi | sains | frame aksi 27A.2c | 0 |  |
| 28 | Batik Atomik Tingkat Tinggi | sains | frame aksi 28A.1d | 1 |  |
| 29 | Klimaks Dua Elemen | sains | frame aksi 29A.2b | 3 |  |
| 30 | Kemenangan Berharga | cerita | pilih manual | 3 |  |
| 31 | Retakan di Langit Kota | cerita | frame aksi 31B.2a | 2 |  |
| 32 | Kota Tanpa Galians | cerita | pilih manual | 5 |  |
| 33 | Perlawanan Bawah Tanah | cerita | frame pertama | 3 |  |
| 34 | Pemburu Waktu | cerita | frame aksi 34A.2c | 2 |  |
| 35 | Menara yang Tertidur | cerita | pilih manual | 6 |  |
| 36 | Benang yang Mengikat Waktu | sains | pilih manual | 6 |  |
| 37 | Serat dari Sektor 7 | cerita | frame aksi 37B.2d | 4 |  |
| 38 | Ethylene yang Terbelah | cerita | frame pertama | 0 |  |
| 39 | Jejak Sang Penenun | cerita | frame aksi 39B.2a | 3 |  |
| 40 | Jangkar Terpasang | cerita | pilih manual | 0 |  |
| 41 | Cakrawala yang Menganga | cerita | frame aksi 41A.1b | 2 |  |
| 42 | Dua Kota, Satu Langit | cerita | frame aksi 42A.2d | 1 |  |
| 43 | Penjaga Cakrawala | sains | frame pertama | 3 |  |
| 44 | Tendangan Melintasi Waktu | sains | frame aksi 44A.2c | 1 |  |
| 45 | Pulang | cerita | frame aksi 45A.1d | 5 |  |
| 46 | Resonansi dari Hutan | cerita | frame aksi 46A.1b | 3 |  |
| 47 | Penjaga dari Batu | sains | frame aksi 47B.1d | 4 |  |
| 48 | Segel yang Retak | cerita | frame pertama | 4 |  |
| 49 | Jejak ke Akademi | cerita | frame aksi 49B.2c | 1 |  |
| 50 | Wajah di Balik Topeng | cerita | frame pertama | 3 |  |
| 51 | Pengakuan Setengah | cerita | pilih manual | 4 |  |
| 52 | Laskar Purba | cerita | frame aksi 52A.2d | 4 |  |
| 53 | Pertemuan di Candi Sungai | cerita | frame aksi 53B.2c | 4 |  |
| 54 | Kain yang Membangkang | cerita | pilih manual | 5 | 1 |
| 55 | Menara yang Direbut | sains | frame aksi 55A.2a | 3 |  |
| 56 | Kota yang Terkuras | cerita | frame aksi 56B.1a | 2 |  |
| 57 | Permintaan Maaf yang Terlambat | cerita | frame aksi 57A.1b | 2 |  |
| 58 | Dua Penenun | cerita | frame pertama | 4 | 1 |
| 59 | Tendangan Sang Pewaris | sains | frame aksi 59A.2a | 0 |  |
| 60 | Wajah yang Dipulihkan | cerita | pilih manual | 2 |  |
| 61 | Hadiah untuk Semua | cerita | pilih manual | 3 |  |
| 62 | Tawaran Kemitraan | cerita | pilih manual | 4 |  |
| 63 | Pola yang Dikenali | sains | frame aksi 63A.2d | 4 |  |
| 64 | Perang Layar | sains | pilih manual | 4 |  |
| 65 | Vex-Core Terbangun | sains | pilih manual | 2 |  |
| 66 | Menyusup ke Menara | sains | frame aksi 66B.2a | 4 |  |
| 67 | Buronan | cerita | frame pertama | 5 |  |
| 68 | Penjaga Candi | cerita | pilih manual | 5 |  |
| 69 | Hub yang Lapar | sains | frame aksi 69B.2c | 0 | 1 |
| 70 | Sang Pencipta Terkunci | sains | pilih manual | 1 |  |
| 71 | Kota yang Dikunci | sains | pilih manual | 1 |  |
| 72 | Pesan dari Dalam Menara | cerita | pilih manual | 3 |  |
| 73 | Serbuan ke Menara | cerita | frame aksi 73B.1b | 2 |  |
| 74 | Melepas Tenunan | cerita | frame aksi 74B.2a | 0 |  |
| 75 | Setelah Layar Padam | cerita | frame aksi 75B.1d | 2 |  |
| 76 | Titik yang Memanggil | cerita | frame aksi 76B.2d | 0 |  |
| 77 | Alam Nyala | sains | frame aksi 77B.2a | 0 |  |
| 78 | Tetua Agni | cerita | pilih manual | 0 | 1 |
| 79 | Abu yang Merayap | sains | frame aksi 79B.1c | 0 | 1 |
| 80 | Sang Hampa | sains | frame aksi 80B.1b | 0 |  |
| 81 | Jalan ke Kawah Jantung | cerita | frame aksi 81A.2a | 0 |  |
| 82 | Asal Sang Nyala | cerita | pilih manual | 0 |  |
| 83 | Desa Terakhir | cerita | frame aksi 83A.2b | 0 |  |
| 84 | Pilihan Ethylene | cerita | frame aksi 84B.1d | 0 | 1 |
| 85 | Ditelan Hampa | cerita | frame aksi 85A.2a | 0 |  |
| 86 | Api Tanpa Sprite | sains | pilih manual | 0 |  |
| 87 | Menyelam ke Kehampaan | sains | frame aksi 87A.2a | 0 |  |
| 88 | Suara di Dalam Diam | sains | frame aksi 88B.2c | 0 |  |
| 89 | Buster Dua Nyala | sains | frame pertama | 0 |  |
| 90 | Nyala Muda | sains | pilih manual | 3 |  |
| 91 | Berkas yang Disembunyikan | sains | pilih manual | 4 |  |
| 92 | Bayangan Berjaket Toska | cerita | frame aksi 92A.2c | 4 |  |
| 93 | Tuduhan | cerita | pilih manual | 4 | 1 |
| 94 | Retak | cerita | pilih manual | 7 |  |
| 95 | Sang Peretas | cerita | frame aksi 95B.1c | 3 | 1 |
| 96 | Buronan Lagi | cerita | pilih manual | 4 |  |
| 97 | Aila di Dalam Dewan | sains | pilih manual | 0 |  |
| 98 | Garda Besi | cerita | pilih manual | 1 | 2 |
| 99 | Pesan Rahasia | sains | pilih manual | 5 |  |
| 100 | Protokol Besi | cerita | pilih manual | 2 |  |
| 101 | Membebaskan yang Ditahan | cerita | frame aksi 101A.1c | 2 |  |
| 102 | Siaran Kebenaran | sains | pilih manual | 2 | 1 |
| 103 | Garda di Monumen | cerita | frame aksi 103A.2c | 2 |  |
| 104 | Vikrama | sains | frame pertama | 1 |  |
| 105 | Aliansi Baru | cerita | pilih manual | 1 |  |
| 106 | Tabung yang Pecah | sains | frame aksi 106A.1c | 1 |  |
| 107 | Anak dari Api yang Sama | cerita | frame aksi 107B.1a | 5 | 1 |
| 108 | Guru yang Tak Siap | cerita | frame aksi 108B.1c | 6 |  |
| 109 | Nyala Pertama | sains | pilih manual | 2 | 1 |
| 110 | Taraka | cerita | frame aksi 110A.2d | 1 |  |
| 111 | Jejak Siphon | sains | pilih manual | 2 |  |
| 112 | Pabrik Senjata | cerita | frame aksi 112B.2c | 1 |  |
| 113 | Penyusupan | cerita | frame aksi 113B.1a | 2 |  |
| 114 | Resonansi Pertama | sains | pilih manual | 4 |  |
| 115 | Meriam Emas | sains | pilih manual | 2 |  |
| 116 | Kejar di Langit | sains | frame pertama | 2 |  |
| 117 | Anak Itu Memilih | cerita | frame aksi 117A.2a | 3 |  |
| 118 | Dua Api Satu Irama | sains | frame aksi 118A.2a | 1 |  |
| 119 | Resonansi Emas | sains | frame pertama | 2 |  |
| 120 | Nama Sendiri | cerita | pilih manual | 4 |  |
| 121 | Menara yang Padam | sains | pilih manual | 3 | 1 |
| 122 | Pulau Emas | cerita | frame aksi 122B.1b | 3 |  |
| 123 | Sang Utusan | cerita | frame aksi 123B.1a | 3 |  |
| 124 | Menyalakan Simpul Barat | sains | pilih manual | 3 |  |
| 125 | Peta Jaring | sains | pilih manual | 4 |  |
| 126 | Hutan Awan | sains | frame aksi 126B.1c | 2 |  |
| 127 | Karang Laut | sains | pilih manual | 0 |  |
| 128 | Kebenaran Wirasena | cerita | pilih manual | 3 |  |
| 129 | Utusan di Dua Tempat | cerita | frame aksi 129A.2b | 1 |  |
| 130 | Simpul Selatan | cerita | pilih manual | 2 |  |
| 131 | Gunung Api | cerita | pilih manual | 4 |  |
| 132 | Gerhana Penuh | cerita | frame aksi 132B.1a | 2 |  |
| 133 | Resonansi Nusantara | sains | pilih manual | 1 |  |
| 134 | Pertarungan di Kawah | cerita | frame aksi 134A.2d | 0 |  |
| 135 | Retak di Palung | cerita | pilih manual | 2 |  |
| 136 | Palung yang Terbuka | cerita | pilih manual | 3 | 1 |
| 137 | Kota yang Memudar | sains | frame aksi 137B.1c | 4 |  |
| 138 | Sekutu Lama | cerita | pilih manual | 4 |  |
| 139 | Panggilan ke Dunia Lain | cerita | pilih manual | 1 | 1 |
| 140 | Tenunan Pertama | cerita | frame aksi 140B.2a | 3 |  |
| 141 | Monumen yang Retak | cerita | pilih manual | 6 | 1 |
| 142 | Lima Penjuru | cerita | pilih manual | 2 |  |
| 143 | Menyelam ke Palung | sains | frame aksi 143A.1c | 4 |  |
| 144 | Suara-Suara | cerita | frame aksi 144B.2d | 2 |  |
| 145 | Jantung Katalis | cerita | pilih manual | 4 |  |
| 146 | Tenunan yang Memberi | sains | pilih manual | 1 | 1 |
| 147 | Semua Nyala | cerita | pilih manual | 2 |  |
| 148 | Buster Terakhir | cerita | frame aksi 148A.2a | 4 |  |
| 149 | Warna Kembali | cerita | pilih manual | 3 |  |
| 150 | Era Baru Galians | cerita | pilih manual | 4 |  |
