# Season 3, Arc 2 (Ep 36-40). Flags: G=Gala, S=Ethylene, K=Kalia
from s3 import half

ENG = "an elderly resistance engineer with a white beard and a brass magnifying monocle"
HERMIT = "an old hermit in a faded Galians robe with a long grey braid"

ARC2 = {"n": 2, "title": "Pengait Nanoselulosa", "en": "The Nanocellulose Tether",
 "focus": "Gala mencari cara menambatkan diri ke lini masa ini, kehilangan lalu menemukan kembali Ethylene, dan menghidupkan monumen sebagai jangkar waktu.",
 "eps": [
 {"n": 36, "title": "Benang yang Mengikat Waktu", "focus": "Motif batik di kain sarung ternyata menyimpan catatan keadaan tubuh Gala; tambatan pertama berhasil sementara.",
  "subs": [
  half("36A", "Membaca Motif",
   "Kembali ke Markas", [
   ("36A.1a", "Wide Shot", "Kalia dan dua pejuang memapah Gala yang lemas masuk ke markas stasiun.", "Kalia and two hooded fighters carry a limp Gala into the underground station base, lanterns swaying.", "GK"),
   ("36A.1b", "Medium Shot", "Gala dibaringkan di meja kerja penuh rongsokan; Ethylene melayang cemas.", "Gala is laid on a cluttered scrap workbench while the sprite hovers anxiously above him.", "GS"),
   ("36A.1c", "Medium Shot", "Insinyur tua berjanggut putih dan monokel kuningan memeriksa kain sarung Gala.", f"Close on {ENG}, leaning over Gala's batik sash with the monocle glowing.", "G"),
   ("36A.1d", "Macro Shot", "Lewat monokel, motif batik tampak tersusun dari simbol data yang sangat kecil.", "Macro view through the monocle: the batik motif resolves into tiny glowing data glyphs woven into the fibers.", ""),
   ],
   "Catatan Keadaan", [
   ("36A.2a", "Medium Shot", "Insinyur memproyeksikan pola batik ke dinding; bentuknya menyerupai siluet tubuh Gala.", f"{ENG.capitalize()} projects the sash's pattern onto the wall; it forms an outline shaped like Gala's body.", ""),
   ("36A.2b", "Close-Up", "Kalia menyadari: kain sarung menyimpan cetak biru diri Gala.", "Close-up: Kalia's eyebrows lift as she realizes the sash holds a blueprint of Gala himself.", "K"),
   ("36A.2c", "Medium Close-Up", "Gala bangun setengah duduk, menyentuh simpul kain sarungnya.", "Gala pushes himself up on one elbow and touches the knot of his sash.", "G"),
   ("36A.2d", "First-Person POV (HUD)", "HUD: 'STATE RECORD FOUND - ANCHOR POSSIBLE'.", "First-person HUD, still glitchy: 'STATE RECORD FOUND - ANCHOR POSSIBLE'.", ""),
   ]),
  half("36B", "Tambatan Pertama",
   "Bingkai Tambat", [
   ("36B.1a", "Wide Shot", "Para pejuang merakit bingkai tambat dari panel batik bekas.", "Resistance fighters assemble a tall ring-shaped frame from scavenged batik panels in the station hall.", ""),
   ("36B.1b", "Medium Shot", "Gala berdiri di tengah bingkai; ujung kain sarungnya dikaitkan ke bingkai.", "Gala stands inside the ring frame as the loose end of his sash is clipped to its rim.", "G"),
   ("36B.1c", "Medium Shot", "Kalia memutar tuas; bingkai berdengung dan menyala emas redup.", "Kalia pulls a heavy lever; the frame hums and glows a dim gold.", "K"),
   ("36B.1d", "Wide Shot", "Partikel ungu di sekitar Gala tersedot kembali ke tubuhnya.", "Drifting purple particles around Gala are pulled back into his body in a slow spiral.", "G"),
   ],
   "Hanya Sementara", [
   ("36B.2a", "First-Person POV (HUD)", "HUD: 'TEMPORAL INTEGRITY: 63% - STABLE'.", "First-person HUD, clearer now: 'TEMPORAL INTEGRITY: 63% - STABLE'.", ""),
   ("36B.2b", "Close-Up", "Serat kain sarung di titik kait mulai berjumbai dan menipis.", "Close-up: the sash fibers at the clip point begin to fray and thin out.", ""),
   ("36B.2c", "Medium Shot", "Insinyur menggeleng: kain ini tak akan bertahan lama.", f"{ENG.capitalize()} shakes his head gravely at the fraying fibers.", ""),
   ("36B.2d", "Medium Shot", "Kalia dan Gala saling pandang, tahu harus mencari jalan lain.", "Kalia and Gala exchange a look, both knowing they need another way.", "GK"),
   ])]},
 {"n": 37, "title": "Serat dari Sektor 7", "focus": "Jangkar permanen butuh serat nanoselulosa murni; satu-satunya sumber adalah pabrik Sektor 7 yang kini jadi sarang Wraith.",
  "subs": [
  half("37A", "Bahan yang Hilang",
   "Peta Menuju Sektor 7", [
   ("37A.1a", "Close-Up", "Insinyur menunjuk gulungan serat murni di arsip foto pabrik lama.", f"{ENG.capitalize()} taps an old archive photo of pure nanocellulose fiber spools in a factory.", ""),
   ("37A.1b", "Medium Close-Up", "Gala mengenali pabrik itu: lokasi misi pertamanya.", "Gala recognizes the factory in the photo, his lips parting in surprise.", "G"),
   ("37A.1c", "Medium Shot", "Kalia memasang pelindung dada rongsokan dan mengencangkan gauntlet jamnya.", "Kalia straps on scrap chest armor and tightens her clockwork gauntlet.", "K"),
   ("37A.1d", "Wide Shot", "Gala dan Kalia berangkat berdua lewat terowongan utara.", "Gala and Kalia set off alone through a dark northern tunnel, the sprite lighting the way.", "GSK"),
   ],
   "Kawasan yang Ditinggalkan", [
   ("37A.2a", "Wide Establishing Shot", "Kawasan industri Sektor 7 versi kalah: pabrik membeku, cerobong patah.", "The defeated version of Sector 7: frozen factories, broken smokestacks, no lights at all.", ""),
   ("37A.2b", "Medium Shot", "Gala berdiri di halaman yang sama tempat ia dulu mendarat di Ep 6.", "Gala stands in the same courtyard where he once landed on his first mission, now buried in snow.", "G"),
   ("37A.2c", "Close-Up", "Kaca jam pecah berserakan di salju, berkilau ungu.", "Close-up: shards of clock glass scattered in the snow, glinting purple.", ""),
   ("37A.2d", "Medium Shot", "Kalia memberi isyarat diam; ada suara detak dari dalam gudang.", "Kalia raises a hand for silence; a faint ticking echoes from inside the warehouse.", "K"),
   ]),
  half("37B", "Sarang di Pabrik Lama",
   "Kepompong Kaca", [
   ("37B.1a", "Wide Interior Shot", "Gudang dipenuhi kepompong kaca jam yang menggantung dan berdetak.", "The warehouse is filled with hanging cocoons of clock glass, each one ticking softly.", ""),
   ("37B.1b", "Medium Shot", "Gala dan Kalia mengendap di antara kepompong.", "Gala and Kalia creep between the hanging cocoons, barely breathing.", "GK"),
   ("37B.1c", "Close-Up", "Di dalam satu kepompong, bayangan Wraith kecil bergerak.", "Close-up: inside one cocoon, the shadow of a small Wraith shifts.", ""),
   ("37B.1d", "Medium Shot", "Gala menemukan gulungan serat murni yang masih utuh di rak.", "Gala finds an intact spool of pure glowing nanocellulose fiber on a shelf.", "G"),
   ],
   "Sarang Terbangun", [
   ("37B.2a", "Close-Up", "Ethylene menyentuh gulungan; serat menyala emas.", "Close-up: the sprite touches the spool and the fiber lights up gold.", "S"),
   ("37B.2b", "Wide Shot", "Cahaya itu membangunkan semua kepompong; kaca retak serentak.", "The golden glow wakes every cocoon; the glass cracks open all at once.", ""),
   ("37B.2c", "Action Shot", "Kalia mengangkat gauntlet; waktu di sekitar pintu membeku sesaat.", "Kalia raises her clockwork gauntlet; a ring of brass light freezes the air around the exit door for a moment.", "K"),
   ("37B.2d", "Action Shot", "Gala berlari keluar sambil memeluk gulungan serat; Wraith menyusul.", "Gala sprints for the frozen doorway hugging the fiber spool, Wraiths pouring after them.", "G"),
   ])]},
 {"n": 38, "title": "Ethylene yang Terbelah", "focus": "Putaran waktu Wraith memecah Ethylene menjadi tiga salinan dari tiga masa; Gala mengenali yang asli lewat ikatan mereka.",
  "subs": [
  half("38A", "Tiga Nyala",
   "Serangan di Jalan Pulang", [
   ("38A.1a", "Wide Action Shot", "Kawanan Wraith memburu Gala dan Kalia di jalan beku.", "A pack of Wraiths chases Gala and Kalia down a frozen avenue.", "GK"),
   ("38A.1b", "Action Shot", "Ethylene melesat melindungi gulungan serat dari cakar Wraith.", "The sprite streaks in to shield the fiber spool from a Wraith's glass claw.", "S"),
   ("38A.1c", "Impact Shot", "Gelombang putar-balik Wraith menghantam Ethylene.", "A Wraith's rewind wave hits the sprite in a burst of purple-silver light.", "S"),
   ("38A.1d", "Wide Shot", "Wraith mundur ke bayangan, puas.", "The Wraiths retreat into the shadows, their afterimages lingering.", ""),
   ],
   "Tiga Ethylene", [
   ("38A.2a", "Medium Shot", "Tiga Ethylene melayang: satu kecil seperti baru lahir, satu berlapis kristal es, satu seperti sekarang.", "Three sprites float before Gala: one tiny like a newborn spark, one encased in a thin ice crystal, one exactly as it is now.", "G"),
   ("38A.2b", "Close-Up", "Ketiganya menoleh ke Gala bersamaan.", "Close-up: all three sprites turn toward Gala at the same time.", ""),
   ("38A.2c", "Medium Close-Up", "Gala ragu; alisnya berkerut.", "Gala hesitates, brows knitted, the three glows reflected on his lenses.", "G"),
   ("38A.2d", "Medium Shot", "Kalia memperingatkan: dua di antaranya tiruan Wraith.", "Kalia warns him, gauntlet raised toward the three sprites.", "GK"),
   ]),
  half("38B", "Yang Asli",
   "Isyarat Lama", [
   ("38B.1a", "Close-Up", "Gala membuka telapak tangan ke atas, seperti malam di balkon akademi.", "Close-up: Gala slowly opens his palm upward, the same quiet gesture from the night on the academy balcony.", "G"),
   ("38B.1b", "Medium Shot", "Satu Ethylene melayang turun dan meringkuk di telapak itu.", "One sprite drifts down and curls up in his open palm.", "GS"),
   ("38B.1c", "Close-Up", "Dua tiruan retak menjadi kaca jam.", "Close-up: the two copies crack into clock glass.", ""),
   ("38B.1d", "Wide Shot", "Pecahan kaca jatuh dan hancur di salju.", "The glass shards fall and shatter in the snow around Gala.", "G"),
   ],
   "Pelajaran dari Tiruan", [
   ("38B.2a", "Close-Up", "Ethylene asli berkedip lemah tapi hangat.", "Close-up: the real sprite flickers weakly but warmly in Gala's palm.", "GS"),
   ("38B.2b", "Medium Shot", "Kalia menurunkan gauntletnya, tersenyum tipis.", "Kalia lowers her gauntlet with a faint smile.", "K"),
   ("38B.2c", "First-Person POV (HUD)", "HUD: 'WRAITH TACTIC: TEMPORAL COPY - ORIGIN SIGNAL TRACED'.", "First-person HUD: 'WRAITH TACTIC: TEMPORAL COPY - ORIGIN SIGNAL TRACED', a line pointing toward the monument.", ""),
   ("38B.2d", "Wide Shot", "Mereka bergegas ke markas; monumen mati di kejauhan.", "Gala and Kalia hurry back toward the base, the dead monument towering in the distance.", "GK"),
   ])]},
 {"n": 39, "title": "Jejak Sang Penenun", "focus": "Motif monumen identik dengan kain sarung Gala; seorang pertapa Galians memberi dua petunjuk besar.",
  "subs": [
  half("39A", "Motif yang Sama",
   "Perbandingan Pola", [
   ("39A.1a", "Medium Shot", "Insinyur menjajarkan pola monumen dan pola kain sarung dalam dua hologram.", f"{ENG.capitalize()} places two holograms side by side: the monument's pattern and the sash's pattern.", ""),
   ("39A.1b", "Close-Up", "Kedua pola saling menumpuk dan cocok sempurna.", "Close-up: the two patterns slide over each other and match perfectly.", ""),
   ("39A.1c", "Medium Close-Up", "Gala memandangi kain sarungnya dengan heran.", "Gala stares down at his own sash in astonishment.", "G"),
   ("39A.1d", "Medium Shot", "Kalia menyebut satu nama: pertapa di kuil utara yang masih ingat ordo lama.", "Kalia points on the map to a shrine in the northern hills.", "K"),
   ],
   "Kuil di Bukit Utara", [
   ("39A.2a", "Wide Establishing Shot", "Kuil batu kecil di bukit bersalju, satu lentera menyala.", "A small stone shrine on a snowy hill, a single lantern glowing at its door.", ""),
   ("39A.2b", "Medium Shot", "Gala dan Kalia menaiki tangga kuil.", "Gala and Kalia climb the worn shrine steps.", "GK"),
   ("39A.2c", "Medium Shot", "Pertapa tua berjubah Galians pudar dengan kepang abu panjang membuka pintu.", f"{HERMIT.capitalize()} opens the shrine door, lantern in hand.", ""),
   ("39A.2d", "Close-Up", "Pertapa menatap goggles dan kain sarung Gala, terpaku.", "Close-up: the hermit freezes, staring at Gala's goggles and sash.", ""),
   ]),
  half("39B", "Pertapa Galian",
   "Ordo Leluhur", [
   ("39B.1a", "Wide Interior Shot", "Di dalam kuil, relief dinding kuno bergambar prajurit berkain sarung batik.", "Inside the shrine, an ancient wall relief shows warriors wearing batik sashes.", ""),
   ("39B.1b", "Medium Shot", "Pertapa bercerita tentang ordo leluhur yang menenun kain pertama.", "The hermit gestures at the relief as he speaks of an ancestral order that wove the first sash.", ""),
   ("39B.1c", "Close-Up", "Satu figur di relief wajahnya dipahat terhapus.", "Close-up: one warrior in the relief has his face deliberately chiseled away.", ""),
   ("39B.1d", "Medium Close-Up", "Gala menyentuh figur yang terhapus itu.", "Gala reaches out and touches the erased figure.", "G"),
   ],
   "Tubuh yang Tak Pernah Ditemukan", [
   ("39B.2a", "Medium Shot", "Pertapa memutar kristal rekaman ledakan arena bertahun-tahun lalu.", "The hermit plays an old recording crystal showing the arena explosion years ago.", ""),
   ("39B.2b", "Close-Up", "Rekaman: di pusat ledakan, celah ungu menelan sosok kecil.", "Close-up of the recording: at the blast's center, a purple crack swallows a small figure.", ""),
   ("39B.2c", "Close-Up", "Kalia menutup mulut dengan tangan, terguncang.", "Close-up: Kalia covers her mouth with her hand, shaken.", "K"),
   ("39B.2d", "Medium Close-Up", "Gala menyadari dirinya di dunia ini tidak mati.", "Gala's mouth opens slowly in realization, the purple glow of the recording on his lenses.", "G"),
   ])]},
 {"n": 40, "title": "Jangkar Terpasang", "focus": "Monumen dihidupkan sebagai jangkar waktu; semua Wraith menyatu menjadi Penjaga Cakrawala, dengan siluet anak di dalam kristalnya.",
  "subs": [
  half("40A", "Menenun Ulang",
   "Menenun di Jantung Menara", [
   ("40A.1a", "Wide Interior Shot", "Di dasar monumen, insinyur dan pejuang memasang gulungan serat di soket.", f"At the monument's base, {ENG} and fighters fit the fiber spool into the cracked socket.", ""),
   ("40A.1b", "Close-Up", "Gala mencabut satu helai benang emas dari kain sarungnya.", "Close-up: Gala pulls a single gold thread from his sash; the sash stays tied at his waist.", "G"),
   ("40A.1c", "Macro Shot", "Helai benang menyatu dengan serat baru, menenun motif yang sama.", "Macro: the gold thread merges with the new fiber, weaving the same batik motif.", ""),
   ("40A.1d", "Medium Shot", "Gala menekan kedua gauntlet ke soket; Ethylene masuk ke dalamnya.", "Gala presses both gauntlets into the socket as the sprite dives in with him.", "GS"),
   ],
   "Menara yang Bangun", [
   ("40A.2a", "Wide Shot", "Garis batik emas menjalar naik sepanjang menara, pertama kali dalam bertahun-tahun.", "Gold batik lines race up the entire spire, lighting it for the first time in years.", ""),
   ("40A.2b", "Wide Panoramic Shot", "Cahaya emas memantul di kota beku; warga keluar dari persembunyian.", "Golden light washes over the frozen city as survivors step out of hiding to look up.", ""),
   ("40A.2c", "First-Person POV (HUD)", "HUD: 'TEMPORAL INTEGRITY: 100% - ANCHORED'.", "First-person HUD, crisp and clean: 'TEMPORAL INTEGRITY: 100% - ANCHORED'.", ""),
   ("40A.2d", "Medium Shot", "Kalia tertawa lega dan meninju bahu Gala pelan.", "Kalia laughs with relief and lightly punches Gala's shoulder.", "GK"),
   ]),
  half("40B", "Wraith Menyatu",
   "Kawanan Datang", [
   ("40B.1a", "Wide Shot", "Dari segala arah, ratusan Wraith merayap menuju menara.", "From every direction, hundreds of Wraiths crawl toward the glowing monument.", ""),
   ("40B.1b", "Medium Shot", "Para pejuang membentuk barisan di kaki menara.", "Resistance fighters form a line at the monument's base, rifles raised.", ""),
   ("40B.1c", "Wide Action Shot", "Wraith berputar menjadi satu pusaran kaca raksasa.", "The Wraiths swirl together into one giant vortex of clock glass.", ""),
   ("40B.1d", "Low Angle Shot", "Gala dan Kalia menatap pusaran itu dari platform menara.", "Low angle: Gala and Kalia on the monument platform stare up at the vortex.", "GK"),
   ],
   "Penjaga Cakrawala", [
   ("40B.2a", "Wide Epic Shot", "Pusaran memadat menjadi Penjaga Cakrawala: raksasa kaca jam dengan roda gigi di punggung.", "The vortex solidifies into the Horizon Warden: a towering giant of clock glass with slowly turning gears on its back.", ""),
   ("40B.2b", "Close-Up", "Di dada Penjaga, kristal ungu bening berdenyut.", "Close-up: a clear purple crystal pulses in the Warden's chest.", ""),
   ("40B.2c", "Extreme Close-Up", "Di dalam kristal, siluet gelap anak kecil berambut spiky membeku.", "Extreme close-up: inside the crystal, the dark silhouette of a small spiky-haired boy hangs frozen.", ""),
   ("40B.2d", "Title Card", "Gala terpaku menatap siluet itu: 'SEASON 3 - ARC 2 COMPLETE'.", "Gala stands frozen, staring up at the silhouette in the crystal; title card 'SEASON 3 - ARC 2 COMPLETE'.", "G"),
   ])]},
 ]}
