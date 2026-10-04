# Season 9 (Ep 121-135). Flags: G S A D M n k V, u=Sang Utusan
from gen import E, ARC

ECL = "desaturated grey, colors drained, a pale white corona in a darkened sky"
SHADE = "eclipse shades, wolf-like shadows outlined with a thin white corona"

S9A1 = ARC(1, "Gerhana dari Barat", "Eclipse from the West",
 "Simpul Barat padam; regu bertemu Sang Utusan dan belajar menyalakan simpul dengan resonansi banyak orang.", [
 E(121, "Menara yang Padam", "Dewan mengumumkan simpul barat padam; regu berangkat, misi pertama Arka.",
  ("Laporan Darurat", [
   ("Ruang Dewan", [
    ("Wide Interior Shot", "Peta hologram Nusantara; satu titik barat gelap.", "A holographic map of the archipelago; one western point has gone dark.", ""),
    ("Medium Shot", "Maheswari menjelaskan kepada regu.", "Maheswari briefs the squad.", "GADkM"),
    ("Close-Up", "Rekaman: sawah kehilangan warna, warga bergerak lambat.", f"Close-up: footage of rice terraces turning {ECL}.", ""),
    ("Close-Up", "Arka menegang: misi pertamanya.", "Close-up: Arka tenses; his first mission.", "k")]),
   ("Persiapan", [
    ("Medium Shot", "Nira memasang modul komunikasi jarak jauh.", "Nira installs long-range comm modules on everyone's gear.", "n"),
    ("Close-Up", "Dhruva menyerahkan perisai baru yang diperbaiki.", "Close-up: Dhruva hoists his repaired shield.", "D"),
    ("Close-Up", "Gala merapikan simpul kain sarung.", "Close-up: Gala tightens the knot of his sash.", "G"),
    ("Wide Shot", "Kapal angkut lepas landas ke barat.", "The transport lifts off toward the west.", "")])]),
  ("Menuju Barat", [
   ("Di Perjalanan", [
    ("Medium Interior Shot", "Arka menempel di jendela kapal.", "Arka presses his face to the transport window.", "k"),
    ("Wide Shot", "Di bawah, garis batas: warna di satu sisi, kelabu di sisi lain.", f"Below, a sharp border: color on one side, {ECL} on the other.", ""),
    ("Close-Up", "Ethylene meredup saat melintasi batas.", "Close-up: the sprite dims as they cross the border.", "S"),
    ("First-Person POV (HUD)", "HUD: 'ENTROPY FIELD - FLAME OUTPUT -40%'.", "First-person HUD: 'ENTROPY FIELD - FLAME OUTPUT -40%'.", "")]),
   ("Mendarat", [
    ("Wide Shot", "Kapal mendarat di tepi sawah bertingkat kelabu.", f"The transport lands beside terraced rice fields, {ECL}.", ""),
    ("Medium Shot", "Regu turun.", "The squad steps out.", "GADk"),
    ("Close-Up", "Seekor burung terbang sangat lambat.", "Close-up: a bird flies past in slow motion, trailing motion blur.", ""),
    ("Medium Close-Up", "Gala menatap menara batu di puncak bukit.", "Gala looks up at a dark stone spire on the hilltop.", "G")])])),
 E(122, "Pulau Emas", "Penjaga simpul barat menyambut regu; Bayang Gerhana menyerang dan api melemah.",
  ("Penjaga Simpul", [
   ("Desa Kelabu", [
    ("Wide Shot", "Desa di lereng; warga bergerak lambat.", f"A village on the slope, villagers moving slowly, {ECL}.", ""),
    ("Medium Shot", "Penjaga simpul, perempuan tua bertongkat bambu, menyambut regu.", "The node keeper, an old woman with a bamboo staff, greets the squad.", "GADk"),
    ("Close-Up", "Warna di wajah penjaga masih tersisa sedikit.", "Close-up: a little color still lingers on the keeper's face.", ""),
    ("Medium Shot", "Penjaga menunjuk menara.", "The keeper points to the spire.", "")]),
   ("Cerita Penjaga", [
    ("Close-Up", "Penjaga: sosok berjubah putih datang tiga malam lalu.", "Close-up: the keeper describes a white-robed visitor.", ""),
    ("Close-Up", "Ia menirukan: sosok itu bilang hanya ingin 'mengistirahatkan'.", "Close-up: the keeper folds her hands as if in rest.", ""),
    ("Medium Close-Up", "Gala dan Aila saling pandang.", "Gala and Aila exchange a look.", "GA"),
    ("Close-Up", "Arka menggenggam gauntletnya.", "Close-up: Arka grips his gauntlets.", "k")])]),
  ("Bayang Gerhana", [
   ("Serangan", [
    ("Wide Shot", "Bayang Gerhana muncul dari sawah.", f"{SHADE.capitalize()} rise out of the grey fields.", ""),
    ("Action Shot", "Gala menyerang; apinya lemah dan pendek.", "Gala strikes; his flame is weak and short.", "G"),
    ("Action Shot", "Plasma Arka juga redup.", "Arka's plasma sputters too.", "k"),
    ("Action Shot", "Dhruva menahan kawanan dengan perisai.", "Dhruva holds the pack back with his shield.", "D")]),
   ("Angin Masih Bekerja", [
    ("Action Shot", "Angin Aila menghamburkan bayangan.", "Aila's wind scatters the shades.", "A"),
    ("Close-Up", "Aila: angin tidak ikut melemah!", "Close-up: Aila grins, surprised.", "A"),
    ("Medium Shot", "Regu mundur ke desa.", "The squad falls back to the village.", "GADk"),
    ("Close-Up", "Bayang Gerhana berhenti di batas desa.", "Close-up: the shades stop at the village edge.", "")])])),
 E(123, "Sang Utusan", "Pertemuan pertama dengan Sang Utusan; sentuhannya melambatkan Gala.",
  ("Di Kaki Menara", [
   ("Kedatangan", [
    ("Wide Shot", "Senja kelabu; regu naik ke menara.", f"A grey dusk; the squad climbs to the spire, {ECL}.", "GADk"),
    ("Medium Shot", "Sang Utusan berdiri di bawah menara, membelakangi mereka.", "Sang Utusan stands beneath the spire, back turned.", "u"),
    ("Close-Up", "Utusan berbalik; wajah porselen tanpa mulut.", "Close-up: Sang Utusan turns, a porcelain face with no mouth.", "u"),
    ("Close-Up", "Celah mata tipisnya berpendar kelabu.", "Close-up: its thin eye slits glow faint grey.", "u")]),
   ("Percakapan", [
    ("Medium Shot", "Utusan: semua hal ingin beristirahat.", "Sang Utusan speaks, voice echoing, hands open.", "u"),
    ("Medium Close-Up", "Gala: warga di sini tidak meminta itu.", "Gala answers firmly.", "G"),
    ("Close-Up", "Utusan memiringkan kepala, sopan.", "Close-up: Sang Utusan tilts its head politely.", "u"),
    ("Medium Shot", "Utusan mengulurkan tangan panjangnya.", "Sang Utusan extends a long grey hand.", "u")])]),
  ("Sentuhan Entropi", [
   ("Melambat", [
    ("Action Shot", "Gala menyerang; Utusan menyentuh bahunya.", "Gala attacks; Sang Utusan touches his shoulder.", "Gu"),
    ("Medium Shot", "Gerakan Gala melambat, jejak buram.", "Gala's movements slow, trailing motion blur.", "G"),
    ("First-Person POV (HUD)", "HUD: 'MOTION: 12% - ENTROPY CONTACT'.", "First-person HUD: 'MOTION: 12% - ENTROPY CONTACT'.", ""),
    ("Action Shot", "Aila menyambar Gala dengan angin.", "Aila snatches Gala away on a gust.", "GA")]),
   ("Mundur", [
    ("Action Shot", "Dhruva menahan Utusan dengan perisai.", "Dhruva blocks Sang Utusan with his shield.", "Du"),
    ("Close-Up", "Perisai Dhruva memudar kelabu di titik sentuhan.", "Close-up: Dhruva's shield fades grey where it was touched.", "D"),
    ("Action Shot", "Arka menarik Dhruva mundur.", "Arka drags Dhruva back.", "Dk"),
    ("Wide Shot", "Utusan tidak mengejar.", "Sang Utusan does not follow.", "u")])])),
 E(124, "Menyalakan Simpul Barat", "Penjaga menjelaskan simpul butuh resonansi banyak orang; warga dan regu menyalakannya bersama.",
  ("Rahasia Simpul", [
   ("Malam di Desa", [
    ("Medium Shot", "Penjaga menunjukkan ukiran lama di batu.", "The keeper shows an old carving on a stone.", ""),
    ("Close-Up", "Ukiran: banyak orang mengangkat pelita mengelilingi menara.", "Close-up: the carving shows many people raising lamps around the spire.", ""),
    ("Close-Up", "Aila: simpul butuh resonansi banyak orang.", "Close-up: Aila realizes, visor lighting up.", "A"),
    ("Medium Shot", "Gala dan Arka saling pandang.", "Gala and Arka look at each other.", "Gk")]),
   ("Pelita", [
    ("Wide Shot", "Warga berkumpul membawa pelita.", "Villagers gather holding oil lamps.", ""),
    ("Close-Up", "Seorang anak menyerahkan pelita kepada Arka.", "Close-up: a child hands Arka a lamp.", "k"),
    ("Medium Shot", "Arka menyalakannya dengan hati-hati.", "Arka lights it carefully.", "k"),
    ("Wide Shot", "Barisan pelita naik ke bukit.", "A line of lamps climbs the hill.", "")])]),
  ("Simpul Menyala", [
   ("Lingkaran", [
    ("Wide Shot", "Warga mengelilingi menara.", "Villagers circle the spire with their lamps.", ""),
    ("Medium Shot", "Gala dan Arka menempelkan tangan ke batu menara.", "Gala and Arka press their hands to the spire stone.", "Gk"),
    ("First-Person POV (HUD)", "HUD: 'RESONANCE: 214 SOURCES'.", "First-person HUD: 'RESONANCE: 214 SOURCES'.", ""),
    ("Wide Epic Shot", "Menara menyala emas dari dasar ke puncak.", "The spire lights gold from base to tip.", "")]),
   ("Warna Kembali", [
    ("Wide Shot", "Warna mengalir kembali ke sawah.", "Color floods back into the terraces.", ""),
    ("Close-Up", "Burung terbang cepat lagi.", "Close-up: a bird darts past at full speed again.", ""),
    ("Medium Shot", "Penjaga tertawa, warnanya pulih.", "The keeper laughs, her color restored.", ""),
    ("Medium Shot", "Regu bersorak bersama warga.", "The squad cheers with the villagers.", "GADk")])])),
 E(125, "Peta Jaring", "Menara barat memperlihatkan peta jaringan; dua simpul lain meredup bersamaan.",
  ("Peta di Dalam Menara", [
   ("Hologram Kuno", [
    ("Wide Shot", "Menara memproyeksikan peta cahaya kuno.", "The spire projects an ancient map of light.", ""),
    ("Close-Up", "Empat simpul di empat penjuru dan satu titik di tengah laut.", "Close-up: four nodes at four corners and one point in the central sea.", ""),
    ("Close-Up", "Garis-garis menghubungkan semua ke Monumen Atom.", "Close-up: lines connect all of them to the atomic monument.", ""),
    ("Medium Close-Up", "Gala menyentuh garis itu.", "Gala touches one of the lines.", "G")]),
   ("Nira Terhubung", [
    ("Close-Up", "Nira muncul di hologram komunikasi.", "Close-up: Nira appears on a comm hologram.", "n"),
    ("Close-Up", "Nira: simpul utara dan timur meredup.", "Close-up: Nira points at two dimming markers.", "n"),
    ("First-Person POV (HUD)", "'NODE NORTH: 31% · NODE EAST: 28%'.", "First-person HUD: 'NODE NORTH: 31% · NODE EAST: 28%'.", ""),
    ("Medium Shot", "Regu terdiam.", "The squad falls silent.", "GADk")])]),
  ("Berpisah", [
   ("Keputusan", [
    ("Medium Shot", "Gala membagi regu.", "Gala divides the squad.", "GADk"),
    ("Close-Up", "Aila dan Dhruva ke timur.", "Close-up: Aila and Dhruva will go east.", "AD"),
    ("Close-Up", "Gala dan Arka ke utara; Nira menyusul.", "Close-up: Gala and Arka will go north, with Nira to meet them.", "Gk"),
    ("Medium Shot", "Empat tangan bertumpuk.", "Four hands stack together.", "GADk")]),
   ("Akhir Arc", [
    ("Wide Shot", "Dua kapal lepas landas ke arah berbeda.", "Two transports lift off in different directions.", ""),
    ("Close-Up", "Utusan menonton dari bukit jauh.", "Close-up: Sang Utusan watches from a distant hill.", "u"),
    ("Close-Up", "Jubahnya terurai jadi partikel kelabu.", "Close-up: its robe hem dissolves into grey particles.", "u"),
    ("Title Card", "'SEASON 9 - ARC 1 COMPLETE'.", "Two ships parting in the sky; title card 'SEASON 9 - ARC 1 COMPLETE'.", "")])]))])

S9A2 = ARC(2, "Terpisah di Nusantara", "Scattered Across the Archipelago",
 "Regu terbelah ke dua simpul, Wirasena mengungkap bahwa jaringan adalah segel, dan simpul selatan jatuh.", [
 E(126, "Hutan Awan", "Gala, Arka, dan Nira mencari simpul utara di hutan berkabut.",
  ("Hutan Raksasa", [
   ("Kabut", [
    ("Wide Establishing Shot", "Hutan pohon raksasa berselimut kabut.", "A forest of giant trees wrapped in mist.", ""),
    ("Medium Shot", "Gala, Arka, Nira berjalan di akar raksasa.", "Gala, Arka and Nira walk along giant roots.", "Gkn"),
    ("Close-Up", "Kabut di satu sisi mulai kelabu.", f"Close-up: mist on one side turning {ECL}.", ""),
    ("Close-Up", "Nira memetakan dengan emitternya.", "Close-up: Nira maps the forest with her emitter.", "n")]),
   ("Penjaga Hutan", [
    ("Medium Shot", "Penjaga tua bertopi anyaman muncul dari balik pohon.", "An old keeper in a woven hat steps out from behind a tree.", ""),
    ("Close-Up", "Ia menunjuk pohon terbesar.", "Close-up: he points to the largest tree.", ""),
    ("Wide Shot", "Simpul utara ada di dalam batang pohon raksasa.", "The northern node is set inside the giant tree's trunk.", ""),
    ("Close-Up", "Cahaya simpul berkedip lemah.", "Close-up: the node's light flickers weakly.", "")])]),
  ("Bayangan di Antara Pohon", [
   ("Serangan", [
    ("Wide Shot", "Bayang Gerhana meluncur di antara pohon.", f"{SHADE.capitalize()} glide between the trees.", ""),
    ("Action Shot", "Arka melindungi Nira.", "Arka shields Nira.", "kn"),
    ("Action Shot", "Gala menendang bayangan dengan silat murni.", "Gala kicks a shade apart with pure silat.", "G"),
    ("Close-Up", "Nira membuat hologram pengalih.", "Close-up: Nira projects decoy holograms.", "n")]),
   ("Masuk ke Pohon", [
    ("Wide Shot", "Mereka masuk ke rongga pohon.", "They slip into the hollow of the great tree.", "Gkn"),
    ("Close-Up", "Di dalam, akar-akar bercahaya lemah.", "Close-up: inside, roots glow faintly.", ""),
    ("Medium Shot", "Sosok berjubah compang-camping sudah menunggu.", "A figure in a ragged cloak is already waiting.", "V"),
    ("Close-Up", "Itu Wirasena.", "Close-up: it is Wirasena.", "V")])])),
 E(127, "Karang Laut", "Aila dan Dhruva menyelam ke simpul timur di bawah laut dan menyalakannya dengan pelita nelayan.",
  ("Laut Karang", [
   ("Pantai", [
    ("Wide Establishing Shot", "Desa nelayan di atas laut karang.", "A fishing village on stilts above a coral sea.", ""),
    ("Medium Shot", "Aila dan Dhruva turun dari kapal.", "Aila and Dhruva step off the transport.", "AD"),
    ("Close-Up", "Karang di bawah air memudar kelabu.", f"Close-up: coral below the water fading, {ECL}.", ""),
    ("Medium Shot", "Penjaga simpul, nelayan tua, menunjuk ke laut.", "The node keeper, an old fisherman, points out to sea.", "")]),
   ("Menyelam", [
    ("Action Shot", "Aila membentuk gelembung udara besar.", "Aila forms a large air bubble around them.", "AD"),
    ("Wide Shot", "Gelembung turun ke dasar laut.", "The bubble sinks toward the seabed.", "AD"),
    ("Wide Shot", "Menara batu di dasar laut, berlumut kelabu.", "A stone spire on the seabed, draped in grey moss.", ""),
    ("Close-Up", "Visor Aila: 'NODE EAST: 19%'.", "Close-up: Aila's visor reads 'NODE EAST: 19%'.", "A")])]),
  ("Pelita Nelayan", [
   ("Arus Gelap", [
    ("Wide Shot", "Bayang Gerhana berenang mengelilingi gelembung.", f"{SHADE.capitalize()} swim around the bubble.", ""),
    ("Action Shot", "Dhruva menancapkan perisai ke dasar laut, menjadi jangkar.", "Dhruva plants his shield in the seabed as an anchor.", "D"),
    ("Close-Up", "Aila menahan gelembung dengan gemetar.", "Close-up: Aila holds the bubble, trembling.", "A"),
    ("Close-Up", "Dhruva: kita tidak bisa sendirian.", "Close-up: Dhruva looks up toward the surface.", "D")]),
   ("Dari Permukaan", [
    ("Wide Shot", "Di permukaan, nelayan menurunkan pelita kedap air.", "On the surface, fishermen lower waterproof lanterns on ropes.", ""),
    ("Wide Shot", "Ratusan pelita turun mengelilingi menara.", "Hundreds of lanterns sink around the spire.", ""),
    ("Close-Up", "Dhruva menempelkan telapak ke menara.", "Close-up: Dhruva presses his palm to the spire.", "D"),
    ("Wide Epic Shot", "Menara laut menyala emas.", "The sea spire lights gold and the coral blooms back into color.", "")])])),
 E(128, "Kebenaran Wirasena", "Wirasena mengungkap bahwa jaringan adalah segel bagi Katalis Entropi.",
  ("Di Dalam Pohon", [
   ("Pengakuan", [
    ("Medium Shot", "Wirasena duduk di akar bercahaya.", "Wirasena sits on a glowing root.", "V"),
    ("Close-Up", "Wirasena: tenunanku dulu memberi makan sesuatu.", "Close-up: Wirasena looks at his frayed wrist sash.", "V"),
    ("Wide Shot", "Penglihatan: tenunan kuno mengalir ke bawah tanah, ke palung laut.", "A vision: the ancient weave flowing underground toward a deep sea trench.", ""),
    ("Close-Up", "Di palung, sesuatu tersegel.", "Close-up: something sealed in the trench.", "")]),
   ("Para Pendiri", [
    ("Wide Shot", "Penglihatan: para pendiri membangun Monumen Atom.", "The vision: the founders building the atomic monument.", ""),
    ("Close-Up", "Plasma atom menggantikan tenunan sebagai makanan segel.", "Close-up: atomic plasma replacing the weave to feed the seal.", ""),
    ("Medium Close-Up", "Gala tersadar: monumen adalah segel.", "Gala realizes, mouth open.", "G"),
    ("Close-Up", "Wirasena: mereka tidak pernah memberitahuku.", "Close-up: Wirasena's jaw tightens.", "V")])]),
  ("Katalis Entropi", [
   ("Nama", [
    ("Close-Up", "Relief kuno di batang pohon: bentuk tanpa rupa.", "Close-up: an ancient carving in the trunk of a formless shape.", ""),
    ("Close-Up", "Tulisan kuno diterjemahkan HUD: 'KATALIS ENTROPI'.", "Close-up: the HUD translates old script: 'ENTROPY CATALYST'.", ""),
    ("Medium Shot", "Arka bergidik.", "Arka shivers.", "k"),
    ("Close-Up", "Nira mengirim semua data ke Aila.", "Close-up: Nira sends everything to Aila.", "n")]),
   ("Sekutu", [
    ("Medium Shot", "Wirasena berdiri.", "Wirasena rises.", "V"),
    ("Medium Shot", "Wirasena menawarkan bantuan.", "Wirasena offers his hand to Gala.", "GV"),
    ("Close-Up", "Gala menjabatnya.", "Close-up: Gala shakes it.", "GV"),
    ("Wide Shot", "Mereka keluar ke hutan yang makin kelabu.", f"They step out into a forest growing {ECL}.", "GkV")])])),
 E(129, "Utusan di Dua Tempat", "Utusan muncul di dua simpul sekaligus; kedua tim bertahan dan menyalakan simpul utara serentak.",
  ("Dua Utusan", [
   ("Utara", [
    ("Wide Shot", "Utusan muncul di depan pohon raksasa.", "Sang Utusan appears before the giant tree.", "u"),
    ("Action Shot", "Wirasena menahannya dengan tenunan.", "Wirasena holds it back with his weave.", "Vu"),
    ("Action Shot", "Gala dan Arka menjaga pintu pohon.", "Gala and Arka guard the tree's entrance.", "Gk"),
    ("Close-Up", "Nira: ada Utusan kedua di timur!", "Close-up: Nira shouts, reading her emitter.", "n")]),
   ("Timur", [
    ("Wide Shot", "Utusan kedua berdiri di atas air laut.", "A second Utusan stands on the sea's surface.", "u"),
    ("Action Shot", "Aila menyerang dengan angin laut.", "Aila strikes with sea wind.", "A"),
    ("Action Shot", "Dhruva menjaga para nelayan.", "Dhruva guards the fishermen.", "D"),
    ("Close-Up", "Menara laut mulai meredup lagi.", "Close-up: the sea spire begins to dim again.", "")])]),
  ("Serentak", [
   ("Sinkron", [
    ("Close-Up", "Nira menyinkronkan dua simpul lewat jaringan komunikasi.", "Close-up: Nira links both nodes through the comm network.", "n"),
    ("Split Screen", "Gala di utara, Aila di timur, menempelkan tangan ke simpul bersamaan.", "Split screen: Gala in the north and Aila in the east press the nodes at the same moment.", "GA"),
    ("First-Person POV (HUD)", "'NODE NORTH + EAST: RESONANCE LINKED'.", "First-person HUD: 'NODE NORTH + EAST: RESONANCE LINKED'.", ""),
    ("Wide Epic Shot", "Pohon raksasa menyala emas.", "The giant tree blazes gold.", "")]),
   ("Utusan Mundur", [
    ("Close-Up", "Kedua Utusan memudar.", "Close-up: both Utusan figures fade.", "u"),
    ("Close-Up", "Suara bergema: 'masih ada satu'.", "Close-up: an echoing voice: 'one remains'.", ""),
    ("Medium Shot", "Gala dan Arka terengah.", "Gala and Arka catch their breath.", "Gk"),
    ("Medium Shot", "Aila dan Dhruva bertos di laut.", "Aila and Dhruva high-five in the sea spray.", "AD")])])),
 E(130, "Simpul Selatan", "Utusan pergi ke simpul terakhir, Gunung Api; simpul selatan padam total dan gerhana mencapai kota.",
  ("Satu Tersisa", [
   ("Laporan", [
    ("Medium Shot", "Maheswari di hologram: simpul selatan jatuh.", "Maheswari on a hologram: the southern node is falling.", "M"),
    ("First-Person POV (HUD)", "'NODE SOUTH: 3%'.", "First-person HUD: 'NODE SOUTH: 3%'.", ""),
    ("Wide Shot", "Gunung api jauh di selatan diselimuti kelabu.", f"A distant volcano in the south, {ECL}.", ""),
    ("Medium Shot", "Kedua tim naik kapal ke selatan.", "Both teams board transports heading south.", "GADk")]),
   ("Padam", [
    ("Wide Shot", "Menara di puncak gunung api padam.", "The spire atop the volcano goes dark.", ""),
    ("Wide Shot", "Gerhana melebar seperti gelombang.", "The eclipse spreads outward like a wave.", ""),
    ("Close-Up", "Di langit, matahari menjadi korona putih.", "Close-up: the sun in the sky becomes a pale white corona.", ""),
    ("Medium Shot", "Warga kota menengadah.", "City residents look up.", "")])]),
  ("Tepi Kota", [
   ("Gerhana Tiba", [
    ("Wide Shot", "Tepi kota mulai kelabu.", "The edge of the city begins to turn grey.", ""),
    ("Close-Up", "Garis emas Monumen Atom berkedip.", "Close-up: the atomic monument's gold lines flicker.", ""),
    ("Medium Shot", "Maheswari memimpin warga ke dekat monumen.", "Maheswari leads citizens toward the monument.", "M"),
    ("Close-Up", "Nira: kalau monumen padam, segel lepas.", "Close-up: Nira looks up from her emitter, pale.", "n")]),
   ("Akhir Arc", [
    ("Medium Interior Shot", "Di kapal, Gala menatap gunung api.", "In the transport, Gala stares at the volcano.", "G"),
    ("Close-Up", "Arka menggenggam tangan Gala.", "Close-up: Arka grips Gala's hand.", "Gk"),
    ("Close-Up", "Wirasena duduk diam.", "Close-up: Wirasena sits in silence.", "V"),
    ("Title Card", "'SEASON 9 - ARC 2 COMPLETE'.", "The transport flying toward the dark volcano; title card 'SEASON 9 - ARC 2 COMPLETE'.", "")])]))])

S9A3 = ARC(3, "Gerhana Atom", "Atomic Eclipse",
 "Pertarungan di Gunung Api, gerhana penuh, resonansi seluruh Nusantara, dan kekalahan Sang Utusan, dengan harga: segel di palung mulai pecah.", [
 E(131, "Gunung Api", "Regu berkumpul di gunung api; penjaga simpul selatan terperangkap dalam diam.",
  ("Berkumpul", [
   ("Lereng", [
    ("Wide Shot", "Lereng gunung api kelabu.", f"The grey slopes of the volcano, {ECL}.", ""),
    ("Medium Shot", "Dua kapal mendarat; regu bersatu kembali.", "Two transports land; the squad reunites.", "GADk"),
    ("Medium Shot", "Dhruva memeluk Gala dan Arka.", "Dhruva hugs Gala and Arka.", "GDk"),
    ("Medium Shot", "Aila menyapa Wirasena dengan hormat.", "Aila bows to Wirasena.", "AV")]),
   ("Pendakian", [
    ("Wide Shot", "Regu mendaki; batu lava beku kelabu.", "The squad climbs over grey lava rock.", "GADk"),
    ("Close-Up", "Gerakan mereka makin berat.", "Close-up: their movements grow heavy, trailing motion blur.", "GADk"),
    ("Close-Up", "Ethylene redup di bahu Gala.", "Close-up: the sprite dims on Gala's shoulder.", "GS"),
    ("Wide Shot", "Di puncak, sosok tua duduk diam di depan menara.", "At the summit, an old figure sits motionless before the spire.", "")])]),
  ("Penjaga yang Diam", [
   ("Membeku dalam Waktu", [
    ("Medium Shot", "Penjaga tua duduk tak bergerak, mata terbuka.", "The old keeper sits unmoving, eyes open.", ""),
    ("Close-Up", "Debu kelabu menempel di wajahnya.", "Close-up: grey dust settles on his face.", ""),
    ("Medium Shot", "Gala berlutut dan menggenggam tangannya.", "Gala kneels and takes his hand.", "G"),
    ("Close-Up", "Kehangatan dari gauntlet Gala.", "Close-up: warmth glows from Gala's gauntlet.", "G")]),
   ("Terbangun", [
    ("Close-Up", "Penjaga berkedip.", "Close-up: the keeper blinks.", ""),
    ("Medium Shot", "Penjaga menunjuk ke kawah.", "The keeper points toward the crater.", ""),
    ("Wide Shot", "Utusan berdiri di tepi kawah.", "Sang Utusan stands at the crater's rim.", "u"),
    ("Close-Up", "Utusan mengangkat kedua tangannya ke langit.", "Close-up: Sang Utusan raises both hands to the sky.", "u")])])),
 E(132, "Gerhana Penuh", "Utusan memicu gerhana penuh; semua melambat kecuali yang terhubung resonansi.",
  ("Langit Gelap", [
   ("Gerhana", [
    ("Wide Epic Shot", "Langit gelap total; matahari hanya korona putih.", "The sky goes fully dark; the sun is only a white corona.", ""),
    ("Wide Shot", "Kelabu menyebar ke seluruh Nusantara di peta hologram.", "On a hologram map, grey spreads across the whole archipelago.", ""),
    ("Close-Up", "Monumen Atom di kota berkedip lemah.", "Close-up: the atomic monument in the city flickers weakly.", ""),
    ("First-Person POV (HUD)", "'SEAL INTEGRITY: 41%'.", "First-person HUD: 'SEAL INTEGRITY: 41%'.", "")]),
   ("Semua Melambat", [
    ("Medium Shot", "Dhruva bergerak sangat lambat.", "Dhruva moves in extreme slow motion, trailing blur.", "D"),
    ("Medium Shot", "Aila juga.", "Aila too, stuck mid-step in slow motion.", "A"),
    ("Medium Shot", "Hanya Gala dan Arka bergerak normal.", "Only Gala and Arka move at normal speed.", "Gk"),
    ("Close-Up", "Arka: resonansi kita melindungi kita!", "Close-up: Arka realizes, looking at his glowing hands.", "k")])]),
  ("Berdua", [
   ("Maju", [
    ("Action Shot", "Gala dan Arka menyerang Utusan bersamaan.", "Gala and Arka attack Sang Utusan together.", "Gku"),
    ("Close-Up", "Utusan menghindar dengan tenang.", "Close-up: Sang Utusan evades calmly.", "u"),
    ("Close-Up", "Sentuhan Utusan meredupkan resonansi mereka.", "Close-up: Sang Utusan's touch dims their resonance.", "u"),
    ("Medium Shot", "Keduanya mulai melambat juga.", "Both begin to slow as well.", "Gk")]),
   ("Wirasena", [
    ("Action Shot", "Wirasena menenun benang di sekitar regu.", "Wirasena weaves threads around the squad.", "V"),
    ("Close-Up", "Benang tenunan menahan kelambatan sesaat.", "Close-up: the woven threads hold back the slowing for a moment.", ""),
    ("Close-Up", "Wirasena: resonansi kalian terlalu kecil. Butuh semua orang.", "Close-up: Wirasena strains, speaking through his teeth.", "V"),
    ("Close-Up", "Gala menoleh ke komlink.", "Close-up: Gala turns to his comm link.", "G")])])),
 E(133, "Resonansi Nusantara", "Nira menghubungkan semua simpul lewat jaringan; warga di seluruh Nusantara mengangkat pelita.",
  ("Jaringan Nira", [
   ("Di Akademi", [
    ("Medium Shot", "Nira di pusat komunikasi akademi, jari bergerak cepat.", "Nira in the academy comm center, fingers flying.", "n"),
    ("Close-Up", "Layar: tiga simpul yang sudah menyala terhubung.", "Close-up: her screen links the three relit nodes.", ""),
    ("Close-Up", "Nira menyiarkan satu pesan ke seluruh Nusantara.", "Close-up: Nira broadcasts one message to the whole archipelago.", "n"),
    ("Medium Shot", "Maheswari berbicara di siaran itu.", "Maheswari speaks on the broadcast.", "M")]),
   ("Pesan", [
    ("Close-Up", "Maheswari: nyalakan pelita kalian.", "Close-up: Maheswari raises a lamp.", "M"),
    ("Wide Shot", "Di Pulau Emas, penjaga dan warga mengangkat pelita.", "At the golden terraces, the keeper and villagers raise lamps.", ""),
    ("Wide Shot", "Di laut karang, nelayan mengangkat lentera.", "At the coral sea, fishermen raise lanterns.", ""),
    ("Wide Shot", "Di hutan awan, warga menyalakan obor.", "In the cloud forest, villagers light torches.", "")])]),
  ("Cahaya Mengalir", [
   ("Kota", [
    ("Wide Shot", "Di kota, warga mengelilingi monumen dengan pelita.", "In the city, citizens circle the monument with lamps.", ""),
    ("Close-Up", "Ibu dan adik Dhruva ikut mengangkat pelita.", "Close-up: Dhruva's mother and little sister hold up a lamp.", ""),
    ("Close-Up", "Nenek penjual jamu mengangkat pelita.", "Close-up: the old herbal-drink seller raises her lamp.", ""),
    ("Wide Epic Shot", "Garis cahaya mengalir dari semua penjuru ke gunung api.", "Lines of light flow from every direction toward the volcano.", "")]),
   ("Tiba di Kawah", [
    ("Wide Shot", "Cahaya mencapai kawah.", "The light reaches the crater.", ""),
    ("Medium Shot", "Regu bergerak normal lagi.", "The squad moves at full speed again.", "GADk"),
    ("First-Person POV (HUD)", "'RESONANCE: NUSANTARA - SOURCES: UNCOUNTABLE'.", "First-person HUD: 'RESONANCE: NUSANTARA - SOURCES: UNCOUNTABLE'.", ""),
    ("Close-Up", "Utusan mundur selangkah untuk pertama kali.", "Close-up: Sang Utusan steps back for the first time.", "u")])])),
 E(134, "Pertarungan di Kawah", "Serangan gabungan melemahkan Utusan; jubahnya terurai, tetapi ia membawa kabar buruk.",
  ("Serangan Gabungan", [
   ("Formasi Lima", [
    ("Action Shot", "Dhruva menahan tangan Utusan.", "Dhruva pins Sang Utusan's hand with his shield.", "Du"),
    ("Action Shot", "Aila memusatkan angin ke kakinya.", "Aila focuses wind at its feet.", "A"),
    ("Action Shot", "Wirasena mengikatnya dengan tenunan.", "Wirasena binds it with weave.", "Vu"),
    ("Close-Up", "Utusan tidak bisa bergerak.", "Close-up: Sang Utusan cannot move.", "u")]),
   ("Guru dan Murid", [
    ("Close-Up", "Ethylene menyatu ke boots Gala.", "Close-up: the sprite merges into Gala's boot.", "GS"),
    ("Close-Up", "Arka menyelaraskan napas dengan Gala.", "Close-up: Arka syncs his breathing with Gala.", "k"),
    ("Low Angle Shot", "Keduanya melompat bersama.", "Low angle: the two leap together.", "Gk"),
    ("Climactic Action Shot", "Buster Resonansi Emas dengan cahaya Nusantara.", "The Golden Resonance Buster, carrying the archipelago's light.", "Gk")])]),
  ("Pesan Terakhir", [
   ("Terurai", [
    ("Impact Shot", "Tendangan menembus dada Utusan.", "The kick passes through Sang Utusan's chest.", "u"),
    ("Close-Up", "Jubahnya terurai jadi partikel kelabu.", "Close-up: its robe dissolves into grey particles.", "u"),
    ("Close-Up", "Utusan berbicara tanpa mulut: 'sudah terlambat'.", "Close-up: Sang Utusan speaks without a mouth: 'too late'.", "u"),
    ("Wide Shot", "Utusan lenyap.", "Sang Utusan is gone.", "")]),
   ("Simpul Selatan", [
    ("Wide Epic Shot", "Menara gunung api menyala emas.", "The volcano spire blazes gold.", ""),
    ("Wide Shot", "Gerhana surut dari langit.", "The eclipse retreats from the sky.", ""),
    ("Medium Shot", "Penjaga tua tertawa.", "The old keeper laughs.", ""),
    ("Medium Close-Up", "Gala tidak ikut tertawa; kata-kata Utusan terngiang.", "Gala does not laugh; he frowns at the empty air.", "G")])])),
 E(135, "Retak di Palung", "Semua simpul menyala, tetapi segel di palung tengah mulai pecah. Katalis Entropi bangun.",
  ("Nusantara Menyala", [
   ("Perayaan Singkat", [
    ("Wide Shot", "Peta hologram: semua simpul emas.", "The hologram map: every node glowing gold.", ""),
    ("Medium Shot", "Warga Nusantara bersorak di siaran.", "Citizens across the islands cheer on the broadcast.", ""),
    ("Medium Shot", "Regu duduk kelelahan di tepi kawah.", "The squad sits exhausted at the crater's rim.", "GADk"),
    ("Close-Up", "Arka tertidur di bahu Dhruva.", "Close-up: Arka falls asleep on Dhruva's shoulder.", "Dk")]),
   ("Getaran", [
    ("Close-Up", "Batu di tepi kawah bergetar.", "Close-up: stones at the crater's rim tremble.", ""),
    ("Close-Up", "Nira: ada getaran dari palung tengah.", "Close-up: Nira's voice over comms, alarmed.", "n"),
    ("First-Person POV (HUD)", "'SEAL INTEGRITY: 12%'.", "First-person HUD: 'SEAL INTEGRITY: 12%'.", ""),
    ("Medium Shot", "Wirasena berdiri, pucat.", "Wirasena rises, pale.", "V")])]),
  ("Yang Terbangun", [
   ("Palung Tengah", [
    ("Wide Shot", "Di tengah laut, air berputar.", "In the middle of the sea, the water begins to spin.", ""),
    ("Wide Shot", "Retakan raksasa bercahaya kelabu-putih di dasar palung.", "A vast crack glows grey-white at the bottom of a trench.", ""),
    ("Extreme Close-Up", "Sesuatu tanpa rupa bergerak di dalam retakan.", "Extreme close-up: something formless shifts inside the crack.", ""),
    ("Wide Shot", "Warna laut di sekitarnya memudar.", f"The sea around it fades, {ECL}.", "")]),
   ("Akhir Season", [
    ("Medium Shot", "Regu berdiri di tepi kawah menatap selatan.", "The squad stands at the crater's rim, facing the sea.", "GADk"),
    ("Close-Up", "Gala mengencangkan simpul kain sarungnya.", "Close-up: Gala tightens the knot of his sash.", "G"),
    ("Close-Up", "Ethylene menyala terang, siap.", "Close-up: the sprite blazes bright, ready.", "S"),
    ("Title Card", "'SEASON 9 COMPLETE'.", "The squad silhouetted against the grey-white glow on the horizon; title card 'SEASON 9 COMPLETE'.", "GADk")])]))])
