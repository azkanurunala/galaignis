# Season 6 (Ep 76-90). Flags: G S A D M, a=Tetua Agni, h=Sang Hampa
from gen import E, ARC

VEIL = "inside a thin golden heat veil cast by Gala's sash"
VILL = "small fire sprites of various warm colors"

S6A1 = ARC(1, "Gerbang Nyala", "Gate of Flame",
 "Ethylene terseret ke Alam Nyala; Gala dan regu menyusul, bertemu Tetua Agni, dan melihat Sang Hampa untuk pertama kali.", [
 E(76, "Titik yang Memanggil", "Titik plasma disimpan di laboratorium akademi; Ethylene makin gelisah sampai wadahnya pecah.",
  ("Wadah Penahan", [
   ("Laboratorium", [
    ("Wide Interior Shot", "Laboratorium akademi; titik plasma melayang dalam tabung penahan.", "The academy lab: a point of pure plasma floating inside a glass containment cylinder.", ""),
    ("Medium Shot", "Teknisi mencatat denyutnya.", "A technician logs the point's pulse on a tablet.", ""),
    ("Close-Up", "Ethylene menempel di kaca tabung.", "Close-up: the sprite presses against the containment glass.", "S"),
    ("Medium Shot", "Gala menarik Ethylene menjauh dengan lembut.", "Gala gently draws the sprite back from the glass.", "GS")]),
   ("Tanda-Tanda", [
    ("First-Person POV (HUD)", "HUD: 'PULSE SYNC WITH ETHYLENE: 71%'.", "First-person HUD: 'PULSE SYNC WITH ETHYLENE: 71%'.", ""),
    ("Close-Up", "Aila membandingkan dua grafik denyut yang hampir sama.", "Close-up: Aila compares two nearly identical pulse graphs on her visor.", "A"),
    ("Medium Shot", "Dhruva mengusulkan memindahkan titik itu jauh-jauh.", "Dhruva gestures toward the door, suggesting they move the point far away.", "D"),
    ("Medium Shot", "Maheswari menyetujui pemindahan esok pagi.", "Maheswari nods, approving the transfer for the morning.", "M")])]),
  ("Malam Pecahnya Kaca", [
   ("Tengah Malam", [
    ("Wide Shot", "Kamar Gala; Ethylene melayang di jendela, menatap laboratorium.", "Gala's dark room: the sprite hovers at the window, staring toward the lab.", "S"),
    ("Close-Up", "Tabung penahan retak.", "Close-up: the containment cylinder cracks.", ""),
    ("Wide Shot", "Titik plasma melebar menjadi pusaran api.", "The plasma point swells into a swirling ring of fire.", ""),
    ("Action Shot", "Ethylene melesat keluar jendela menuju lab.", "The sprite streaks out the window toward the lab.", "S")]),
   ("Menyusul", [
    ("Action Shot", "Gala terbangun dan berlari mengejar.", "Gala wakes and sprints after it.", "G"),
    ("Wide Shot", "Ethylene tersedot ke pusaran.", "The sprite is pulled into the fire ring.", "S"),
    ("Close-Up", "Visor Aila merekam koordinat pusaran.", "Close-up: Aila, arriving, records the ring's coordinates on her visor.", "A"),
    ("Action Shot", "Gala melompat masuk tanpa ragu.", "Gala leaps into the ring without hesitation.", "G")])])),
 E(77, "Alam Nyala", "Gala tiba di dunia api yang sebagian mati menjadi abu; Aila dan Dhruva menyusul lewat koordinat Aila.",
  ("Dunia Api", [
   ("Pendaratan", [
    ("Wide Establishing Shot", "Langit merah-emas, sungai cahaya lava, pulau batu melayang.", "A realm of flame: a red-gold sky, rivers of lava light, floating stone islands.", ""),
    ("Medium Shot", "Gala mendarat di dataran batu hangat.", "Gala lands on a warm stone plain.", "G"),
    ("Wide Shot", "Di kejauhan, padang abu kelabu yang mati.", "In the distance, a grey field of dead ash spreads.", ""),
    ("First-Person POV (HUD)", "HUD: 'LOCATION: UNKNOWN - ETHYLENE SIGNAL: FAINT'.", "First-person HUD: 'LOCATION: UNKNOWN - ETHYLENE SIGNAL: FAINT'.", "")]),
   ("Penduduk", [
    ("Medium Shot", "Sprite-sprite kecil bersembunyi di balik batu.", f"{VILL.capitalize()} hide behind rocks, peeking out.", "G"),
    ("Close-Up", "Satu sprite kecil mendekat, penasaran.", "Close-up: one tiny orange sprite drifts closer, curious.", ""),
    ("Close-Up", "Gala membuka telapak tangan pelan.", "Close-up: Gala slowly opens his palm.", "G"),
    ("Medium Shot", "Sprite kecil hinggap, lalu memanggil yang lain.", "The tiny sprite lands in his palm, then flashes to call the others.", "G")])]),
  ("Regu Menyusul", [
   ("Dua Sosok dari Langit", [
    ("Wide Shot", "Pusaran terbuka di langit; Aila dan Dhruva jatuh.", "A ring opens in the sky and Aila and Dhruva fall through.", "AD"),
    ("Action Shot", "Aila memperlambat jatuh dengan angin.", "Aila slows their fall with a gust.", "AD"),
    ("Close-Up", "Zirah Dhruva mulai berasap kepanasan.", "Close-up: steam rises from Dhruva's armor in the heat.", "D"),
    ("Close-Up", "Visor Aila berkedip merah: suhu berbahaya.", "Close-up: Aila's visor flashes red, heat warning.", "A")]),
   ("Selubung Panas", [
    ("Action Shot", "Gala membentangkan cahaya kain sarung menutupi keduanya.", f"Gala spreads light from his sash over them, placing both {VEIL}.", "GAD"),
    ("Medium Shot", "Dhruva menghela napas lega.", f"Dhruva breathes out in relief, {VEIL}.", "D"),
    ("Medium Shot", "Regu berkumpul; sprite desa mengelilingi mereka.", f"The squad regroups, circled by {VILL}.", "GAD"),
    ("Wide Shot", "Sprite menuntun mereka ke arah gunung api putih.", "The sprites lead them toward a distant white-hot mountain.", "GAD")])])),
 E(78, "Tetua Agni", "Tetua Agni mengenali jejak Ethylene pada api Gala dan menjelaskan Jantung yang sekarat.",
  ("Gua Bara", [
   ("Kediaman Tetua", [
    ("Wide Interior Shot", "Gua bara dengan dinding kristal merah.", "A cave of embers with glowing red crystal walls.", ""),
    ("Medium Shot", "Tetua Agni muncul, cincin emas mengorbit tubuhnya.", "Tetua Agni emerges, faint gold rings orbiting its body.", "a"),
    ("Close-Up", "Agni mendekati Gala, mengendus apinya.", "Close-up: Agni drifts close to Gala, sensing his flame.", "Ga"),
    ("Close-Up", "Mata putih Agni melebar: ia mengenali Ethylene.", "Close-up: Agni's white dot eyes widen in recognition.", "a")]),
   ("Cerita Jantung", [
    ("Wide Shot", "Agni memproyeksikan cahaya: Jantung raksasa di kawah.", "Agni projects a vision of a giant glowing Heart in a crater.", "a"),
    ("Wide Shot", "Penglihatan: Jantung meredup, abu merayap.", "The vision: the Heart dimming as ash creeps in.", ""),
    ("Medium Shot", "Regu mendengarkan dalam diam.", f"The squad listens in silence, Aila and Dhruva {VEIL}.", "GAD"),
    ("Medium Close-Up", "Gala menggenggam tangan, cemas akan Ethylene.", "Gala clenches his fist, worried for the sprite.", "G")])]),
  ("Serpihan yang Hilang", [
   ("Penjelasan", [
    ("Close-Up", "Agni menunjukkan celah kosong di Jantung.", "Close-up: Agni's vision shows a small missing piece in the Heart.", "a"),
    ("Close-Up", "Celah itu seukuran Ethylene.", "Close-up: the gap is exactly the size of the sprite.", ""),
    ("Medium Close-Up", "Gala tersadar.", "Gala's mouth falls open in realization.", "G"),
    ("Medium Shot", "Aila dan Dhruva saling pandang.", f"Aila and Dhruva exchange a look {VEIL}.", "AD")]),
   ("Arah Kawah", [
    ("Medium Shot", "Agni menunjuk ke kawah jauh.", "Agni points a flame wisp toward a distant crater.", "a"),
    ("First-Person POV (HUD)", "HUD: 'ETHYLENE SIGNAL: HEART CRATER - 3 DAYS'.", "First-person HUD: 'ETHYLENE SIGNAL: HEART CRATER - 3 DAYS'.", ""),
    ("Medium Shot", "Agni memutuskan ikut.", "Agni rises, gold rings brightening, choosing to come along.", "a"),
    ("Wide Shot", "Rombongan keluar gua.", "The group leaves the cave with Agni leading.", "GADa")])])),
 E(79, "Abu yang Merayap", "Makhluk Abu tidak mempan api; regu menemukan Ethylene sebentar di tepi padang abu.",
  ("Padang Kelabu", [
   ("Makhluk Abu", [
    ("Wide Shot", "Padang abu kelabu sunyi.", "A silent grey field of ash under a dull sky.", ""),
    ("Close-Up", "Abu bangkit membentuk makhluk tanpa wajah.", "Close-up: ash rises and forms faceless creatures.", ""),
    ("Action Shot", "Pukulan api Gala padam saat menyentuh abu.", "Gala's flaming punch fizzles out against the ash.", "G"),
    ("First-Person POV (HUD)", "HUD: 'FLAME NULLIFIED'.", "First-person HUD: 'FLAME NULLIFIED'.", "")]),
   ("Angin dan Perisai", [
    ("Action Shot", "Angin Aila menghamburkan makhluk abu.", f"Aila's gusts scatter the ash creatures, {VEIL}.", "A"),
    ("Action Shot", "Perisai Dhruva menyapu mereka.", f"Dhruva sweeps them aside with his shield, {VEIL}.", "D"),
    ("Medium Close-Up", "Gala tersenyum pada rekan-rekannya.", "Gala grins at his teammates.", "G"),
    ("Wide Shot", "Jalan terbuka melintasi padang abu.", "A path opens across the ash field.", "GAD")])]),
  ("Pertemuan Singkat", [
   ("Cahaya di Tepi Abu", [
    ("Wide Shot", "Di ujung padang, cahaya kecil terbang ke kawah.", "At the field's edge, a small light flies toward the crater.", ""),
    ("Close-Up", "Itu Ethylene.", "Close-up: it is the sprite.", "S"),
    ("Action Shot", "Gala berlari memanggilnya.", "Gala runs, calling out.", "G"),
    ("Medium Shot", "Ethylene berhenti dan berbalik.", "The sprite stops and turns back.", "S")]),
   ("Tetap Pergi", [
    ("Close-Up", "Ethylene menempel di pipi Gala.", "Close-up: the sprite presses against Gala's cheek.", "GS"),
    ("Close-Up", "Cahaya Ethylene berdenyut sedih.", "Close-up: the sprite's glow pulses sadly.", "S"),
    ("Medium Shot", "Ethylene terbang lagi ke kawah.", "The sprite flies away toward the crater again.", "S"),
    ("Medium Close-Up", "Gala membiarkannya, tangan terulur.", "Gala lets it go, hand still reaching.", "G")])])),
 E(80, "Sang Hampa", "Sang Hampa bangkit dari lautan abu dan menelan api sebuah desa sprite.",
  ("Lautan Abu", [
   ("Kebangkitan", [
    ("Wide Shot", "Lautan abu bergolak.", "A sea of ash begins to churn.", ""),
    ("Wide Epic Shot", "Sang Hampa bangkit: siluet hampa raksasa bertepi statis putih.", "Sang Hampa rises: a towering hollow silhouette of darkness, edges fizzing with white static.", "h"),
    ("Close-Up", "Dua titik putih di wajahnya menyala.", "Close-up: two pinpoint white lights glow where its eyes should be.", "h"),
    ("Medium Shot", "Agni gemetar.", "Agni trembles, its rings flickering.", "a")]),
   ("Desa di Kaki Hampa", [
    ("Wide Shot", "Desa sprite di bawah bayangan Hampa.", f"A village of {VILL} beneath Hampa's shadow.", ""),
    ("Action Shot", "Hampa mengulurkan tangan; api desa tersedot.", "Hampa reaches out and the village's flames are pulled into it.", "h"),
    ("Close-Up", "Sprite-sprite kecil memudar menjadi abu.", "Close-up: small sprites fading to grey ash.", ""),
    ("Medium Close-Up", "Gala meraung marah.", "Gala roars in anger.", "G")])]),
  ("Mundur", [
   ("Serangan Sia-Sia", [
    ("Action Shot", "Gala melesat menyerang Hampa.", "Gala launches at Hampa.", "Gh"),
    ("Impact Shot", "Api Gala tertelan tubuh Hampa.", "Gala's flames are swallowed by Hampa's body.", "Gh"),
    ("Action Shot", "Dhruva menarik Gala mundur.", "Dhruva hauls Gala back by the arm.", "GD"),
    ("Action Shot", "Aila menerbangkan sprite yang selamat.", f"Aila carries surviving sprites away on the wind, {VEIL}.", "A")]),
   ("Di Balik Batu", [
    ("Medium Shot", "Rombongan bersembunyi di balik batu besar.", "The group hides behind a huge rock.", "GADa"),
    ("Close-Up", "Agni redup, sedih.", "Close-up: Agni dims with grief.", "a"),
    ("Medium Close-Up", "Gala menatap kawah di kejauhan.", "Gala looks toward the distant crater.", "G"),
    ("Title Card", "'SEASON 6 - ARC 1 COMPLETE'.", "The group silhouetted against the dim crater glow; title card 'SEASON 6 - ARC 1 COMPLETE'.", "GADa")])]))])

S6A2 = ARC(2, "Jantung yang Padam", "The Dying Heart",
 "Perjalanan ke Kawah Jantung, asal-usul Ethylene terungkap, dan Ethylene ditelan Sang Hampa.", [
 E(81, "Jalan ke Kawah Jantung", "Menyeberangi jembatan lava; panas menekan Aila dan Dhruva.",
  ("Jembatan Lava", [
   ("Penyeberangan", [
    ("Wide Shot", "Jembatan batu sempit di atas sungai lava.", "A narrow stone bridge over a river of lava.", ""),
    ("Medium Shot", "Agni memimpin di depan.", "Agni leads the way across.", "a"),
    ("Medium Shot", "Regu berjalan pelan satu per satu.", f"The squad walks single file, Aila and Dhruva {VEIL}.", "GAD"),
    ("Close-Up", "Batu jembatan retak di bawah boots Dhruva.", "Close-up: the bridge stone cracks under Dhruva's boot.", "D")]),
   ("Jembatan Runtuh", [
    ("Action Shot", "Jembatan runtuh di belakang mereka.", "The bridge collapses behind them.", ""),
    ("Action Shot", "Aila mengangkat Dhruva dengan angin.", "Aila lifts Dhruva with a desperate gust.", "AD"),
    ("Action Shot", "Gala menangkap tangan Dhruva di tepi.", "Gala grabs Dhruva's hand at the edge.", "GD"),
    ("Medium Shot", "Ketiganya terengah di seberang.", "All three pant on the far side.", "GAD")])]),
  ("Batas Tubuh", [
   ("Aila Melemah", [
    ("Medium Shot", "Aila terduduk; visornya berkabut.", "Aila sinks down, her visor fogged.", "A"),
    ("First-Person POV (HUD)", "HUD: 'VEIL STRENGTH: 48%'.", "First-person HUD: 'VEIL STRENGTH: 48%'.", ""),
    ("Medium Shot", "Dhruva menggendong Aila.", "Dhruva lifts Aila onto his back.", "AD"),
    ("Close-Up", "Gala memperkuat cahaya kain sarung, berkeringat.", "Close-up: Gala strengthens the sash's glow, sweating.", "G")]),
   ("Istirahat", [
    ("Wide Shot", "Mereka berkemah di ceruk batu sejuk.", "They camp in a cooler rock alcove.", "GADa"),
    ("Medium Shot", "Agni menurunkan suhu ceruk.", "Agni dims itself to cool the alcove.", "a"),
    ("Medium Shot", "Aila pulih, tersenyum lemah.", "Aila recovers and smiles weakly.", "A"),
    ("Medium Close-Up", "Gala menatap kawah; tekad makin kuat.", "Gala stares toward the crater, resolve hardening.", "G")])])),
 E(82, "Asal Sang Nyala", "Ethylene menunggu di tepi kawah dan memperlihatkan bagaimana ia lahir.",
  ("Di Tepi Kawah", [
   ("Pertemuan Kedua", [
    ("Wide Shot", "Tepi Kawah Jantung; Ethylene melayang sendirian.", "The rim of the Heart Crater; the sprite hovers alone.", "S"),
    ("Medium Shot", "Gala mendekat pelan.", "Gala approaches slowly.", "GS"),
    ("Close-Up", "Ethylene menyentuh dahi Gala.", "Close-up: the sprite touches Gala's forehead.", "GS"),
    ("Wide Shot", "Cahaya menyelimuti mereka: penglihatan dimulai.", "Light washes over them and a vision begins.", "GS")]),
   ("Penglihatan Ep 1", [
    ("Wide Shot", "Arena akademi Ep 1; bola plasma meledak.", "A vision of the academy arena: the plasma orb from Gala's first day exploding.", ""),
    ("Close-Up", "Celah mikro terbuka sesaat di pusat ledakan.", "Close-up: a microscopic tear opens for an instant at the blast's center.", ""),
    ("Macro Shot", "Percikan dari Jantung tergelincir keluar dan menyatu dengan plasma Gala.", "Macro: a spark from the Heart slips through and fuses with Gala's plasma.", ""),
    ("Medium Shot", "Ethylene lahir di samping Gala muda.", "The sprite is born beside the younger Gala.", "GS")])]),
  ("Rumah Sebenarnya", [
   ("Setelah Penglihatan", [
    ("Medium Close-Up", "Gala membuka mata di tepi kawah, basah keringat.", "Gala comes back to the crater rim, drenched in sweat.", "G"),
    ("Close-Up", "Ethylene menatap Jantung yang redup.", "Close-up: the sprite gazes at the dim Heart below.", "S"),
    ("Wide Shot", "Jantung raksasa berdenyut lemah di dasar kawah.", "The giant Heart pulses weakly at the crater's bottom.", ""),
    ("Medium Close-Up", "Gala menyadari rumah Ethylene di sini.", "Gala lowers his head, understanding the sprite's home is here.", "G")]),
   ("Regu Menyusul", [
    ("Medium Shot", "Aila dan Dhruva tiba bersama Agni.", f"Aila and Dhruva arrive with Agni, {VEIL}.", "ADa"),
    ("Medium Shot", "Gala menceritakan penglihatannya.", "Gala tells them what he saw.", "GAD"),
    ("Close-Up", "Aila memeluk Gala sebentar.", "Close-up: Aila gives Gala a quick hug.", "GA"),
    ("Wide Shot", "Asap abu mengepul dari arah desa terakhir.", "Grey smoke rises from the direction of the last village.", "")])])),
 E(83, "Desa Terakhir", "Regu mempertahankan desa sprite terakhir; Agni terluka.",
  ("Pengepungan", [
   ("Desa di Pilar Batu", [
    ("Wide Shot", "Desa sprite di atas pilar batu; makhluk abu memanjat.", f"A village of {VILL} atop stone pillars, ash creatures climbing up.", ""),
    ("Action Shot", "Regu melompat ke pilar.", "The squad leaps onto the pillars.", "GAD"),
    ("Action Shot", "Dhruva membentuk dinding perisai.", f"Dhruva forms a shield wall at the pillar's edge, {VEIL}.", "D"),
    ("Action Shot", "Aila meniup makhluk abu jatuh.", "Aila blasts climbing ash creatures off the pillar.", "A")]),
   ("Silat Tanpa Api", [
    ("Action Shot", "Gala bertarung dengan silat murni.", "Gala fights the ash creatures with pure silat.", "G"),
    ("Impact Shot", "Tendangan Gala memecah makhluk abu.", "Gala's kick bursts an ash creature apart.", "G"),
    ("Medium Shot", "Sprite desa menyerang dengan percikan kecil.", "Village sprites join in with tiny sparks.", ""),
    ("Wide Shot", "Gelombang abu mundur.", "The ash wave recedes.", "")])]),
  ("Harga Kemenangan", [
   ("Agni Terluka", [
    ("Action Shot", "Satu tangan Hampa muncul dari kabut, menyambar desa.", "A single giant hand of Hampa reaches out of the haze at the village.", "h"),
    ("Action Shot", "Agni menghadang dengan seluruh cahayanya.", "Agni blocks it with all its light.", "a"),
    ("Close-Up", "Cahaya Agni meredup separuh.", "Close-up: Agni's light dims by half.", "a"),
    ("Wide Shot", "Tangan Hampa mundur ke kabut.", "Hampa's hand withdraws into the haze.", "")]),
   ("Janji", [
    ("Medium Shot", "Gala berlutut di samping Agni.", "Gala kneels beside Agni.", "Ga"),
    ("Close-Up", "Agni menyentuh kain sarung Gala.", "Close-up: Agni touches Gala's sash.", "Ga"),
    ("Medium Close-Up", "Gala berjanji menyelamatkan Jantung.", "Gala places a fist over his chest, a promise.", "G"),
    ("Wide Shot", "Sprite desa menyalakan cahaya kecil untuk regu.", "Village sprites light tiny flames in thanks.", "GAD")])])),
 E(84, "Pilihan Ethylene", "Jantung hampir padam; Ethylene memilih kembali menyatu dengannya, dan Hampa menghadang.",
  ("Dasar Kawah", [
   ("Turun ke Jantung", [
    ("Wide Shot", "Regu menuruni dinding kawah.", "The squad climbs down the crater wall.", "GAD"),
    ("Close-Up", "Jantung tinggal berkedip lemah.", "Close-up: the Heart now only flickers.", ""),
    ("First-Person POV (HUD)", "HUD: 'HEART OUTPUT: 4%'.", "First-person HUD: 'HEART OUTPUT: 4%'.", ""),
    ("Medium Shot", "Ethylene melayang di atas Jantung.", "The sprite hovers above the Heart.", "S")]),
   ("Perpisahan", [
    ("Close-Up", "Ethylene menoleh ke Gala.", "Close-up: the sprite turns to look at Gala.", "S"),
    ("Medium Close-Up", "Gala menggeleng, memohon.", "Gala shakes his head, pleading.", "G"),
    ("Close-Up", "Ethylene menyentuh dahi Gala sekali lagi.", "Close-up: the sprite touches Gala's forehead one more time.", "GS"),
    ("Action Shot", "Ethylene menukik ke Jantung.", "The sprite dives toward the Heart.", "S")])]),
  ("Hampa Menghadang", [
   ("Bayangan Jatuh", [
    ("Wide Shot", "Bayangan Hampa menutup kawah.", "Hampa's shadow falls over the crater.", "h"),
    ("Action Shot", "Tangan Hampa meraih Ethylene di udara.", "Hampa's hand snatches at the sprite in mid-air.", "Sh"),
    ("Action Shot", "Gala melesat ke tangan itu.", "Gala rockets toward the hand.", "Gh"),
    ("Impact Shot", "Tendangan Gala memantul tanpa bekas.", "Gala's kick bounces off harmlessly.", "Gh")]),
   ("Tergenggam", [
    ("Close-Up", "Ethylene terjepit di jari Hampa.", "Close-up: the sprite trapped between Hampa's fingers.", "Sh"),
    ("Medium Shot", "Aila dan Dhruva menyerang kaki Hampa.", f"Aila and Dhruva strike Hampa's legs, {VEIL}.", "AD"),
    ("Wide Shot", "Hampa mengangkat Ethylene ke wajahnya.", "Hampa raises the sprite toward its face.", "h"),
    ("Medium Close-Up", "Gala berteriak.", "Gala screams.", "G")])])),
 E(85, "Ditelan Hampa", "Hampa menelan Ethylene; api Gala melemah drastis, dan regu terpaksa mundur.",
  ("Kehilangan", [
   ("Ditelan", [
    ("Close-Up", "Ethylene lenyap ke dalam tubuh Hampa.", "Close-up: the sprite vanishes into Hampa's body.", "h"),
    ("Wide Shot", "Tubuh Hampa berdenyut sekali, lebih besar.", "Hampa's body pulses once and grows larger.", "h"),
    ("Close-Up", "Api di gauntlet Gala tersendat.", "Close-up: the flames on Gala's gauntlets sputter.", "G"),
    ("First-Person POV (HUD)", "HUD: 'ETHYLENE SIGNAL: LOST'.", "First-person HUD: 'ETHYLENE SIGNAL: LOST'.", "")]),
   ("Tak Berdaya", [
    ("Action Shot", "Gala menyerang membabi buta.", "Gala attacks wildly.", "G"),
    ("Impact Shot", "Hampa menepis Gala ke dinding kawah.", "Hampa swats Gala into the crater wall.", "Gh"),
    ("Action Shot", "Dhruva mengangkat Gala.", "Dhruva hauls Gala up.", "GD"),
    ("Action Shot", "Aila menerbangkan mereka keluar kawah.", "Aila lifts them out of the crater on a gust.", "GAD")])]),
  ("Malam Tanpa Nyala", [
   ("Di Ceruk Batu", [
    ("Wide Shot", "Regu bersembunyi di ceruk; Agni redup.", "The squad hides in an alcove with the dim Agni.", "GADa"),
    ("Close-Up", "Gala menatap telapak tangannya yang kosong.", "Close-up: Gala stares at his empty palm.", "G"),
    ("Close-Up", "Selubung panas kain sarung makin tipis.", "Close-up: the heat veil from his sash grows thin.", "G"),
    ("Medium Shot", "Aila dan Dhruva duduk di sisinya.", f"Aila and Dhruva sit beside him, {VEIL}.", "GAD")]),
   ("Akhir Arc", [
    ("Wide Shot", "Hampa berdiri di atas kawah, Jantung hampir padam.", "Hampa stands over the crater as the Heart nearly dies.", "h"),
    ("Close-Up", "Di dada Hampa, setitik cahaya oranye samar.", "Close-up: a faint orange speck glows deep inside Hampa's chest.", "h"),
    ("Medium Close-Up", "Gala melihat titik itu.", "Gala sees the speck and lifts his head.", "G"),
    ("Title Card", "'SEASON 6 - ARC 2 COMPLETE'.", "Gala rising in the alcove, goggles turned toward Hampa; title card 'SEASON 6 - ARC 2 COMPLETE'.", "G")])]))])

S6A3 = ARC(3, "Nyala Muda", "The Young Flame",
 "Gala belajar menyalakan api tanpa sprite, menyelam ke dalam Hampa, menyalakan kembali Ethylene, dan menanam benih Jantung baru.", [
 E(86, "Api Tanpa Sprite", "Gala harus menemukan apinya sendiri; Agni memberi restu terakhirnya.",
  ("Bara yang Tersisa", [
   ("Mencoba", [
    ("Medium Shot", "Gala mencoba menyalakan api; hanya percikan.", "Gala tries to ignite his flame; only sparks.", "G"),
    ("Close-Up", "Gala memukul tanah, frustrasi.", "Close-up: Gala punches the ground in frustration.", "G"),
    ("Medium Shot", "Dhruva mengingatkan: kau bertarung tanpa api di candi.", "Dhruva kneels beside him, speaking firmly.", "GD"),
    ("Medium Shot", "Aila: apimu tumbuh dari orang-orang yang kau lindungi.", "Aila taps Gala's chest plate over his heart.", "GA")]),
   ("Nyala Pertama", [
    ("Close-Up", "Gala menarik napas pelan, berkonsentrasi.", "Close-up: Gala breathes slowly, concentrating.", "G"),
    ("Macro Shot", "Nyala kecil muncul di telapak tangannya.", "Macro: a small steady flame appears in his palm.", ""),
    ("Medium Shot", "Nyala itu tumbuh, tanpa sprite.", "The flame grows, without any sprite.", "G"),
    ("Medium Shot", "Aila dan Dhruva tersenyum.", "Aila and Dhruva smile.", "AD")])]),
  ("Restu Agni", [
   ("Tetua Bicara", [
    ("Medium Shot", "Agni melayang ke Gala dengan sisa cahayanya.", "Agni floats to Gala with its remaining light.", "Ga"),
    ("Close-Up", "Agni menempelkan diri ke gauntlet Gala.", "Close-up: Agni presses itself against Gala's gauntlet.", "Ga"),
    ("Close-Up", "Cahaya merah tua melapisi gauntlet sementara.", "Close-up: a deep crimson glow coats the gauntlet for now.", "G"),
    ("Medium Shot", "Agni meredup, kelelahan, tapi tersenyum.", "Agni dims, exhausted but content.", "a")]),
   ("Rencana", [
    ("Medium Shot", "Gala menggambar rencana di tanah.", "Gala sketches a plan in the ash.", "GAD"),
    ("Close-Up", "Sketsa: Gala masuk ke Hampa, kain sarung dipegang Dhruva.", "Close-up: the sketch shows Gala entering Hampa, his sash held by Dhruva.", ""),
    ("Medium Close-Up", "Dhruva mengangguk: aku akan menariknya kembali.", "Dhruva nods and grips his shield strap.", "D"),
    ("Wide Shot", "Regu keluar dari ceruk.", "The squad steps out of the alcove.", "GAD")])])),
 E(87, "Menyelam ke Kehampaan", "Gala masuk ke tubuh Hampa, ditambatkan kain sarung yang dipegang Dhruva.",
  ("Tambatan", [
   ("Tepi Kawah", [
    ("Wide Shot", "Regu di tepi kawah; Hampa di bawah.", "The squad at the crater rim, Hampa below.", "GAD"),
    ("Close-Up", "Gala menyerahkan ujung kain sarung ke Dhruva; simpul tetap di pinggang.", "Close-up: Gala hands the end of his sash to Dhruva, the knot staying at his waist.", "GD"),
    ("Medium Shot", "Aila memanggil angin untuk mendorong Gala.", "Aila summons a strong wind behind Gala.", "A"),
    ("Action Shot", "Gala melompat ke dada Hampa.", "Gala leaps toward Hampa's chest.", "G")]),
   ("Menembus", [
    ("Impact Shot", "Gala menembus permukaan Hampa seperti air hitam.", "Gala breaks through Hampa's surface like dark water.", "Gh"),
    ("Close-Up", "Kain sarung meregang, menegang.", "Close-up: the sash stretches taut behind him.", "G"),
    ("Medium Shot", "Dhruva menahan kain sarung dengan kedua tangan.", "Dhruva braces, holding the sash with both hands.", "D"),
    ("Close-Up", "Aila melindungi Dhruva dari tangan Hampa.", "Close-up: Aila fends off Hampa's hand with wind.", "A")])]),
  ("Di Dalam Hampa", [
   ("Kehampaan Putih", [
    ("Wide Shot", "Ruang putih statis tanpa ujung.", "Inside Hampa: an endless void of white static.", "G"),
    ("Close-Up", "Api Gala memudar menjadi putih pucat.", "Close-up: Gala's flame fades to pale white.", "G"),
    ("Wide Shot", "Kenangan api yang ditelan melayang: desa, hutan, sprite.", "Memories of swallowed flames drift past: villages, forests, sprites.", ""),
    ("Close-Up", "Satu kenangan: Agni muda bersama Jantung.", "Close-up: one memory shows a young Agni beside the Heart.", "")]),
   ("Arah", [
    ("First-Person POV (HUD)", "HUD bergetar: 'ETHYLENE SIGNAL: 0.3%'.", "First-person HUD shaking: 'ETHYLENE SIGNAL: 0.3%'.", ""),
    ("Close-Up", "Setitik oranye jauh di dalam putih.", "Close-up: a speck of orange far away in the white.", ""),
    ("Medium Shot", "Gala berenang menuju titik itu.", "Gala swims through the static toward the speck.", "G"),
    ("Close-Up", "Kain sarung bercahaya menjadi satu-satunya warna.", "Close-up: his glowing sash is the only color in the void.", "G")])])),
 E(88, "Suara di Dalam Diam", "Gala menemukan Ethylene yang hampir padam dan memberinya apinya sendiri.",
  ("Menemukan", [
   ("Sprite yang Menggigil", [
    ("Medium Shot", "Ethylene meringkuk, hampir abu.", "The sprite curled up, nearly grey.", "S"),
    ("Close-Up", "Gala menangkupnya dengan kedua tangan.", "Close-up: Gala cups it in both hands.", "GS"),
    ("Close-Up", "Ethylene bergetar lemah.", "Close-up: the sprite trembles faintly.", "S"),
    ("Medium Close-Up", "Gala tersenyum lembut.", "Gala smiles gently.", "G")]),
   ("Kebalikan dari Ep 1", [
    ("Medium Shot", "Gala menempelkan Ethylene ke pelat dadanya.", "Gala presses the sprite to his chest plate.", "GS"),
    ("Macro Shot", "Api Gala mengalir ke Ethylene, kebalikan dari kelahirannya.", "Macro: Gala's flame flows into the sprite, the reverse of its birth.", ""),
    ("Close-Up", "Warna Ethylene kembali oranye-emas.", "Close-up: the sprite's color returns to orange-gold.", "S"),
    ("Close-Up", "Mata titik putih Ethylene terbuka.", "Close-up: the sprite's white dot eyes open.", "S")])]),
  ("Retakan Cahaya", [
   ("Hampa Bergolak", [
    ("Wide Shot", "Putih statis di sekitar mereka retak oleh cahaya.", "The white static around them cracks with light.", "GS"),
    ("Wide Shot", "Di luar, tubuh Hampa bersinar dari dalam.", "Outside, Hampa's body glows from within.", "h"),
    ("Medium Shot", "Aila dan Dhruva melihat cahaya itu.", "Aila and Dhruva see the light, hopeful.", "AD"),
    ("Close-Up", "Dhruva menarik kain sarung dengan sekuat tenaga.", "Close-up: Dhruva pulls the sash with all his strength.", "D")]),
   ("Kembali Bersama", [
    ("Medium Shot", "Ethylene hinggap di bahu Gala.", "The sprite settles on Gala's shoulder.", "GS"),
    ("Close-Up", "Keduanya menoleh ke arah tarikan kain sarung.", "Close-up: both turn toward the pull of the sash.", "GS"),
    ("Action Shot", "Gala menendang menuju cahaya luar.", "Gala kicks toward the outside light.", "GS"),
    ("Wide Shot", "Putih runtuh di belakang mereka.", "The white void collapses behind them.", "")])])),
 E(89, "Buster Dua Nyala", "Gala dan Ethylene keluar bersama dan melepas Buster Dua Nyala; Hampa terurai.",
  ("Keluar", [
   ("Menyembur", [
    ("Wide Epic Shot", "Gala dan Ethylene menyembur keluar dari dada Hampa.", "Gala and the sprite burst out of Hampa's chest.", "GSh"),
    ("Action Shot", "Dhruva jatuh terduduk menahan tarikan terakhir.", "Dhruva falls back from the final pull.", "D"),
    ("Close-Up", "Aila bersorak.", "Close-up: Aila cheers.", "A"),
    ("Wide Shot", "Hampa terhuyung, berlubang di dada.", "Hampa staggers, a hole in its chest.", "h")]),
   ("Dua Nyala", [
    ("Close-Up", "Ethylene menyatu ke boots Gala.", "Close-up: the sprite merges into Gala's boot.", "GS"),
    ("Close-Up", "Cahaya merah tua Agni dan emas Gala bercampur.", "Close-up: Agni's crimson and Gala's gold mix around his boot.", "G"),
    ("Low Angle Shot", "Gala melayang di atas kawah.", "Low angle: Gala hovers above the crater.", "G"),
    ("First-Person POV (HUD)", "HUD: 'TWIN FLAME RESONANCE: 100%'.", "First-person HUD: 'TWIN FLAME RESONANCE: 100%'.", "")])]),
  ("Hampa Terurai", [
   ("Serangan", [
    ("Climactic Action Shot", "Buster Dua Nyala.", "Gala unleashes the Twin-Flame Buster Kick, a spiral of crimson and gold.", "G"),
    ("Impact Shot", "Tendangan menghantam lubang di dada Hampa.", "The kick strikes the hole in Hampa's chest.", "Gh"),
    ("Wide Shot", "Retakan cahaya menjalar ke seluruh tubuh Hampa.", "Cracks of light spread across Hampa's whole body.", "h"),
    ("Wide Epic Shot", "Hampa pecah menjadi abu putih yang berjatuhan lembut.", "Hampa bursts into soft falling white ash.", "")]),
   ("Abu yang Subur", [
    ("Wide Shot", "Abu jatuh ke padang kelabu; bara kecil tumbuh.", "The ash falls on the grey fields and small embers sprout.", ""),
    ("Close-Up", "Api-api yang ditelan kembali ke desa.", "Close-up: swallowed flames drift home to the villages.", ""),
    ("Wide Shot", "Jantung berkedip lebih kuat, tapi belum pulih.", "The Heart flickers stronger, but not fully.", ""),
    ("Medium Shot", "Agni melayang ke kawah, cemas.", "Agni floats to the crater, still worried.", "a")])])),
 E(90, "Nyala Muda", "Ethylene meninggalkan serpihan dirinya sebagai benih Jantung dan pulang bersama Gala. Benih Season 7: peretas Ep 4 kembali.",
  ("Benih Jantung", [
   ("Keputusan Ethylene", [
    ("Medium Shot", "Ethylene melayang di atas Jantung.", "The sprite hovers over the Heart.", "S"),
    ("Close-Up", "Ethylene menoleh ke Gala, lalu ke Jantung.", "Close-up: the sprite looks at Gala, then the Heart.", "S"),
    ("Macro Shot", "Ethylene melepas percikan baru yang mungil dari dirinya.", "Macro: the sprite releases a tiny newborn spark from itself.", "S"),
    ("Wide Shot", "Percikan itu jatuh ke Jantung; Jantung menyala penuh.", "The tiny newborn spark falls into the Heart and it blazes fully alive.", "")]),
   ("Alam yang Pulih", [
    ("Wide Epic Shot", "Langit Alam Nyala kembali merah-emas.", "The realm's sky returns to red and gold.", ""),
    ("Medium Shot", "Agni bersinar terang kembali.", "Agni glows bright again, rings spinning.", "a"),
    ("Wide Shot", "Sprite desa menari di udara.", f"{VILL.capitalize()} dance in the air.", ""),
    ("Medium Shot", "Ethylene kembali ke bahu Gala, utuh.", "The sprite returns to Gala's shoulder, whole.", "GS")])]),
  ("Pulang", [
   ("Perpisahan", [
    ("Medium Shot", "Agni membungkuk kepada regu.", "Agni bows to the squad.", "GADa"),
    ("Wide Shot", "Pusaran pulang terbuka.", "A ring home opens in the sky.", ""),
    ("Wide Shot", "Regu melompat ke pusaran.", "The squad leaps into the ring.", "GAD"),
    ("Wide Shot", "Mereka mendarat di laboratorium akademi saat fajar.", "They land in the academy lab at dawn.", "GAD")]),
   ("Rekaman yang Dihapus", [
    ("Wide Shot", "Malam; sosok berjaket hitam berlapis sirkuit toska mengamati akademi.", "Night: a hooded figure in a dark jacket with cyan data-lining watches the academy from a roof.", ""),
    ("Close-Up", "Berkas dewan: 'EP4 SIMULATION BREACH - AUTHORIZED BY: [REDACTED]'.", "Close-up: a council file reading 'SIMULATION BREACH - AUTHORIZED BY: [REDACTED]'.", ""),
    ("Close-Up", "Tangan bersarung hitam menutup berkas itu.", "Close-up: a black-gloved hand closes the file.", ""),
    ("Title Card", "'SEASON 6 COMPLETE'.", "Gala asleep on the balcony, the sprite glowing beside him; title card 'SEASON 6 COMPLETE'.", "GS")])]))])
