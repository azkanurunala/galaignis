# Season 3, Arc 1 (Ep 31-35). Flags: G=Gala, S=Ethylene, A=Aila, D=Dhruva, K=Kalia
def half(code, title, a1t, a1, a2t, a2):
    return {"id": code, "title": title, "acts": [
        {"id": f"{code}.1", "title": a1t, "frames": a1},
        {"id": f"{code}.2", "title": a2t, "frames": a2}]}

S3 = {
 "n": 3, "title": "Paradoks Waktu", "en": "Chronos Horizon", "saga": "Saga I: Bangkitnya Sang Vanguard",
 "focus": "",
 "arcs": [
 {"n": 1, "title": "Terlempar ke Lini Masa Paralel", "en": "Cast into the Parallel Timeline",
  "focus": "Gala terseret retakan ke dunia tempat ia dinyatakan tewas, bertemu Kalia, dan mulai terkikis erosi waktu.",
  "eps": [
  {"n": 31, "title": "Retakan di Langit Kota", "focus": "Retakan makin tidak stabil; Gala menyelamatkan seorang anak dan justru terseret masuk.",
   "subs": [
   half("31A", "Tarikan Retakan",
    "Penyelidikan Malam", [
    ("31A.1a", "Wide Establishing Shot", "Alun-alun malam di bawah retakan ungu-perak; barikade Galians dan drone pemindai.", "A city plaza at night beneath a glowing purple-silver rift in the sky, Galians barricades around it and small scanner drones hovering.", ""),
    ("31A.1b", "Medium Shot", "Gala, Aila, dan Dhruva (kakinya sudah pulih) berjalan ke barikade.", "Gala, Aila and Dhruva, his leg fully healed, walk up to the barricade under the rift.", "GAD"),
    ("31A.1c", "Close-Up", "Ethylene berkedip gelisah dan bersembunyi di balik bahu Gala.", "Close-up: the sprite flickers nervously and hides behind Gala's shoulder.", "GS"),
    ("31A.1d", "First-Person POV (HUD)", "HUD: 'TEMPORAL DRIFT: +14 SEC / MIN - INCREASING'.", "First-person HUD reading on the rift: 'TEMPORAL DRIFT: +14 SEC / MIN - INCREASING'.", ""),
    ],
    "Benda yang Berkedip", [
    ("31A.2a", "Wide Shot", "Tiang lampu dekat retakan berkedip antara utuh dan patah.", "A street lamp near the rift flickers between two states, standing upright and snapped in half.", ""),
    ("31A.2b", "Close-Up", "Visor Aila menampilkan dua gambar jalan yang sama saling tumpang tindih.", "Close-up: Aila's visor shows two overlapping images of the same street, slightly out of sync.", "A"),
    ("31A.2c", "Medium Shot", "Dhruva melempar kerikil ke bayang retakan; kerikil membeku di udara lalu lenyap.", "Dhruva tosses a pebble toward the rift's shadow; it freezes in mid-air, then vanishes.", "D"),
    ("31A.2d", "Medium Close-Up", "Gala menatap retakan; alis turun, rasa bersalah.", "Gala stares up at the rift, brows drawn low with guilt, purple light on his lenses.", "G"),
    ]),
   half("31B", "Jatuh ke Garis Lain",
    "Retakan Melebar", [
    ("31B.1a", "Wide Shot", "Retakan robek melebar dengan gelombang kejut; angin menyeret puing ke atas.", "The rift tears wider with a shockwave; wind drags loose debris upward into it.", ""),
    ("31B.1b", "Medium Shot", "Anak laki-laki berjas hujan kuning yang lolos dari barikade terangkat ke arah retakan.", "A small boy in a yellow raincoat who slipped past the barricade is lifted off his feet toward the rift.", ""),
    ("31B.1c", "Action Shot", "Gala melesat dengan pendorong boots ke arah anak itu.", "Gala launches on boot thrusters toward the boy.", "G"),
    ("31B.1d", "Mid-Air Shot", "Gala meraih pergelangan anak itu tepat di bawah tepi retakan.", "Mid-air, Gala grabs the boy's wrist just below the edge of the rift.", "G"),
    ],
    "Tertarik", [
    ("31B.2a", "Mid-Air Action Shot", "Gala memutar badan dan melempar anak itu ke Dhruva yang menangkapnya.", "Gala twists and throws the boy down to Dhruva, who catches him safely.", "GD"),
    ("31B.2b", "Close-Up", "Boots Gala tersendat; cahaya ungu menelan kakinya.", "Close-up: Gala's boot thrusters sputter as purple light swallows his legs.", "G"),
    ("31B.2c", "Action Shot", "Ethylene menukik masuk ke retakan menyusul Gala.", "The sprite dives headfirst into the rift after Gala's disappearing silhouette.", "S"),
    ("31B.2d", "Wide Shot", "Aila menjangkau ke atas, Dhruva memeluk si anak; retakan menyempit, Gala hilang.", "Aila reaches up in vain and Dhruva holds the boy as the rift snaps narrower; Gala is gone.", "AD"),
    ])]},
  {"n": 32, "title": "Kota Tanpa Galians", "focus": "Gala tiba di kota yang sama tetapi kalah, menemukan tugu peringatan dirinya sendiri, dan mengalami erosi pertama.",
   "subs": [
   half("32A", "Reruntuhan yang Dikenal",
    "Mendarat di Kota Cermin", [
    ("32A.1a", "Wide Shot", "Gala terjatuh dari celah ungu ke salju di kota gelap membeku tanpa lampu.", "Gala tumbles out of a purple crack onto the snow of a dark, frozen city with no lights under a grey sky.", "G"),
    ("32A.1b", "Close-Up", "Ethylene mengibaskan embun beku, bersinar lemah, hinggap di dada Gala.", "Close-up: the sprite shakes off frost, glowing weakly, and settles on Gala's chest plate.", "GS"),
    ("32A.1c", "First-Person POV (HUD)", "HUD: 'NETWORK: NONE FOUND - GALIANS SIGNAL: 0'.", "First-person HUD: 'NETWORK: NONE FOUND - GALIANS SIGNAL: 0' over the dark city.", ""),
    ("32A.1d", "Low Angle Shot", "Gala berdiri; di atasnya Monumen Atom mati terbungkus es.", "Low angle: Gala stands up; above him the atomic monument looms, dead and encased in ice.", "G"),
    ],
    "Tugu Peringatan", [
    ("32A.2a", "Wide Shot", "Reruntuhan akademi di gunung; kubah hancur, tertimbun salju.", "The academy ruins on the mountain, its dome shattered and buried in snow.", ""),
    ("32A.2b", "Medium Shot", "Gala berjalan di arena yang runtuh, dinding heksagonal Ep 1 hangus hitam.", "Gala walks through the ruined training arena, the same hexagonal walls from his first day now scorched black.", "G"),
    ("32A.2c", "Close-Up", "Tugu batu kecil di tengah arena bertuliskan 'GALA IGNIS - CADET'.", "Close-up: a small stone memorial in the center of the arena with an engraved plaque reading 'GALA IGNIS - CADET'.", ""),
    ("32A.2d", "Medium Close-Up", "Mulut Gala terbuka kaget, tangannya menyentuh plakat; Ethylene meredup.", "Gala's mouth falls open in shock as he touches the plaque; the sprite dims beside him.", "GS"),
    ]),
   half("32B", "Erosi Pertama",
    "Tangan yang Berkedip", [
    ("32B.1a", "Close-Up", "Ujung jari gauntlet Gala berkedip menjadi partikel ungu lalu kembali.", "Close-up: the fingertips of Gala's gauntlet flicker into drifting purple particles, then snap back.", "G"),
    ("32B.1b", "First-Person POV (HUD)", "HUD: 'TEMPORAL INTEGRITY: 94%'.", "First-person HUD: 'TEMPORAL INTEGRITY: 94%' in amber.", ""),
    ("32B.1c", "Medium Shot", "Gala mengepalkan tangan; kedipan berhenti untuk sementara.", "Gala clenches his fist hard and the flickering stops for now; he looks worried.", "G"),
    ("32B.1d", "Close-Up", "Ethylene menempel di gauntlet, menghangatkannya.", "Close-up: the sprite presses itself against Gala's gauntlet, warming it.", "GS"),
    ],
    "Patroli Sang Pemenang", [
    ("32B.2a", "Wide Shot", "Patroli Cryo-Drone berpanji kepingan salju melintas di jalan runtuh.", "A Cryo-Drone patrol flying blue snowflake banners glides over ruined, frozen streets.", ""),
    ("32B.2b", "Medium Shot", "Gala merunduk di balik mobil melayang yang membeku, meredupkan Ethylene.", "Gala ducks behind a frozen hover car, cupping a hand over the sprite to dim it.", "GS"),
    ("32B.2c", "Close-Up", "Lampu sorot drone menyapu kaca mobil yang berembun.", "Close-up: a drone searchlight sweeps across the car's frosted window.", ""),
    ("32B.2d", "Wide Shot", "Gala menyelinap ke gang gelap; sosok berjubah mengawasinya dari atap.", "Gala slips into a dark alley as the patrol passes; a cloaked figure watches him from a rooftop.", "G"),
    ])]},
  {"n": 33, "title": "Perlawanan Bawah Tanah", "focus": "Gala ditangkap kelompok perlawanan pimpinan Kalia dan mendengar bagaimana dunia ini kalah.",
   "subs": [
   half("33A", "Kelompok Penyintas",
    "Jaring Rongsokan", [
    ("33A.1a", "Action Shot", "Jaring dari kabel batik rongsokan jatuh menimpa Gala di gang.", "A net woven from salvaged glowing batik cables drops over Gala in the alley.", "G"),
    ("33A.1b", "Medium Shot", "Gala meronta; jaring berpijar dan meredam apinya.", "Gala struggles inside the net as it glows and smothers his flames.", "G"),
    ("33A.1c", "Wide Shot", "Pejuang bertudung bermantel tambalan muncul dengan senapan rakitan.", "Hooded resistance fighters in patched coats step out of the shadows, aiming makeshift rifles.", ""),
    ("33A.1d", "Medium Shot", "Kalia melangkah maju, gauntlet jam kuningannya terangkat.", "Kalia steps forward, her brass clockwork gauntlet raised and ticking.", "K"),
    ],
    "Markas di Bawah Kota", [
    ("33A.2a", "Wide Shot", "Stasiun metro bawah tanah menjadi markas; lentera dari panel batik bekas.", "An underground metro station turned resistance base, lit by lanterns built from scavenged batik panels.", ""),
    ("33A.2b", "Medium Shot", "Gala duduk terikat di atas peti; Ethylene bersembunyi di simpul kain sarung.", "Gala sits bound on a crate, the sprite hiding inside the knot of his sash.", "GS"),
    ("33A.2c", "Medium Shot", "Kalia mengitarinya, mengamati goggles dan zirahnya.", "Kalia circles him slowly, studying his goggles and armor.", "GK"),
    ("33A.2d", "Close-Up", "Wajah Kalia mengeras: Gala Ignis sudah mati bertahun-tahun lalu.", "Close-up: Kalia's face hardens as she tells him Gala Ignis died years ago.", "K"),
    ]),
   half("33B", "Dunia Tanpa Vanguard",
    "Kisah Kekalahan", [
    ("33B.1a", "Wide Shot", "Kalia memproyeksikan hologram kasar: pabrik Sektor 7 membeku, drone berkerumun.", "Kalia projects a crude flickering hologram of the Sector 7 factory frozen solid and swarming with drones.", "K"),
    ("33B.1b", "Close-Up", "Hologram kubah akademi yang pecah.", "Close-up: the hologram shows the academy's golden dome shattering.", ""),
    ("33B.1c", "Medium Close-Up", "Gala mendengarkan, alis turun, rahang menegang.", "Gala listens, brows low, jaw tight, the blue hologram light on his lenses.", "G"),
    ("33B.1d", "Close-Up", "Gauntlet jam Kalia berdetak saat ia mengepalkannya.", "Close-up: the gears of Kalia's clockwork gauntlet tick as she clenches her fist.", "K"),
    ],
    "Nyala yang Tak Pernah Ada", [
    ("33B.2a", "Close-Up", "Ethylene mengintip dari simpul kain sarung.", "Close-up: the sprite peeks out of the knot of Gala's sash.", "GS"),
    ("33B.2b", "Medium Shot", "Para pejuang terkesiap dan mundur saat Ethylene melayang naik.", "Resistance fighters gasp and step back as the sprite floats up into the air.", "S"),
    ("33B.2c", "Close-Up", "Alis Kalia terangkat; cahaya hangat Ethylene menerangi wajahnya.", "Close-up: Kalia's eyebrows rise as the sprite's warm light falls on her face.", "KS"),
    ("33B.2d", "Medium Shot", "Kalia memotong ikatan Gala, masih waspada.", "Kalia cuts Gala's bonds with a small blade, still on guard.", "GK"),
    ])]},
  {"n": 34, "title": "Pemburu Waktu", "focus": "Chrono-Wraith menyerang markas; serangan biasa tak mempan; kain sarung ternyata memperlambat erosi.",
   "subs": [
   half("34A", "Kemunculan Chrono-Wraith",
    "Jam yang Berhenti", [
    ("34A.1a", "Wide Shot", "Semua jam di stasiun berhenti serentak; lentera berkedip.", "Every clock in the station stops at the same second; the lanterns flicker.", ""),
    ("34A.1b", "Close-Up", "Embun beku berwarna ungu aneh merambati ubin.", "Close-up: frost with a strange purple tint creeps across the station tiles.", ""),
    ("34A.1c", "Wide Shot", "Chrono-Wraith keluar dari terowongan: tubuh pecahan kaca jam, bayangan gerak ungu-perak.", "A Chrono-Wraith emerges from a tunnel: a body of shattered clock glass trailing purple-silver afterimages.", ""),
    ("34A.1d", "Medium Shot", "Para pejuang menembak; peluru menembus bayangan geraknya.", "Resistance fighters open fire; their bolts pass harmlessly through its afterimages.", ""),
    ],
    "Mangsa Terbesar", [
    ("34A.2a", "First-Person POV (HUD)", "HUD: 'ANOMALY HUNTER - TARGET: YOU'.", "First-person HUD warning 'ANOMALY HUNTER - TARGET: YOU' locked on the Wraith.", ""),
    ("34A.2b", "Action Shot", "Gala melompat di depan Kalia dan menendang api ke Wraith.", "Gala leaps in front of Kalia and drives a fire kick into the Wraith.", "GK"),
    ("34A.2c", "Impact Shot", "Tendangan kena, tapi Wraith memutar mundur satu langkah tanpa luka.", "The kick lands, but the Wraith rewinds one step backward, unharmed, its afterimages snapping back into place.", "G"),
    ("34A.2d", "Close-Up", "Cakar kaca Wraith menggores lengan Gala; lengannya berkedip jadi partikel.", "Close-up: the Wraith's glass claw grazes Gala's forearm, which flickers into purple particles.", "G"),
    ]),
   half("34B", "Gema Masa Lalu",
    "Erosi yang Menjalar", [
    ("34B.1a", "First-Person POV (HUD)", "HUD: 'TEMPORAL INTEGRITY: 71%'.", "First-person HUD: 'TEMPORAL INTEGRITY: 71%' flashing red.", ""),
    ("34B.1b", "Close-Up", "Pelat lengan Gala berkedip antara padat dan partikel.", "Close-up: Gala's forearm plate flickers between solid armor and drifting particles.", "G"),
    ("34B.1c", "Action Shot", "Gala menarik ujung kain sarung dan melilitkannya ke lengan.", "Gala pulls the loose end of his batik sash and wraps it around the flickering forearm.", "G"),
    ("34B.1d", "Close-Up", "Benang batik emas berpijar; kedipan melambat dan stabil.", "Close-up: the gold batik threads glow and the flickering slows, then steadies.", "G"),
    ],
    "Sang Wraith Mundur", [
    ("34B.2a", "Action Shot", "Gala memukul dengan lengan berbalut kain sarung; tubuh kaca Wraith retak.", "Gala strikes with his sash-wrapped forearm and the Wraith's glass body cracks.", "G"),
    ("34B.2b", "Wide Shot", "Wraith menjerit, memutar mundur dirinya ke terowongan, lenyap.", "The Wraith shrieks and rewinds itself backward into the tunnel, vanishing.", ""),
    ("34B.2c", "Medium Shot", "Kalia menurunkan gauntletnya, menatap kain sarung itu.", "Kalia lowers her gauntlet, staring at the glowing sash on Gala's arm.", "GK"),
    ("34B.2d", "Medium Shot", "Kalia mengulurkan tangan membantu Gala berdiri; kepercayaan mulai tumbuh.", "Kalia offers Gala her hand and pulls him to his feet.", "GK"),
    ])]},
  {"n": 35, "title": "Menara yang Tertidur", "focus": "Kalia membawa Gala ke Monumen Atom yang mati; ternyata monumen itu jangkar waktu, dan erosi mulai menyerang goggles.",
   "subs": [
   half("35A", "Jalan Pulang",
    "Rencana Kalia", [
    ("35A.1a", "Medium Shot", "Kalia membentangkan peta gambar tangan di atas peti.", "Kalia unrolls a hand-drawn map across a crate, showing a route to the monument.", "GK"),
    ("35A.1b", "Close-Up", "Sketsa monumen dengan catatan dilingkari 'TIME ANCHOR?'.", "Close-up: a pencil sketch of the monument on the map with a circled note 'TIME ANCHOR?'.", ""),
    ("35A.1c", "Medium Shot", "Gala melepas lilitan kain sarung dari lengan dan mengikatnya kembali di pinggang.", "Gala unwinds the sash from his forearm and ties it back around his waist.", "G"),
    ("35A.1d", "Wide Shot", "Gala, Kalia, dan dua pejuang bertudung berangkat lewat terowongan banjir yang membeku.", "Gala, Kalia and two hooded fighters set out through a flooded, frozen tunnel.", "GK"),
    ],
    "Melintasi Kota Beku", [
    ("35A.2a", "Wide Shot", "Rombongan kecil menyeberangi jalan raya beku di bawah langit gelap.", "The small group crosses a frozen avenue under a dark sky, drones circling in the far distance.", "GK"),
    ("35A.2b", "Close-Up", "Pantulan Gala di kaca toko berkedip dengan partikel ungu.", "Close-up: Gala's reflection in a shop window flickers with purple particles.", "G"),
    ("35A.2c", "Medium Shot", "Kalia menarik Gala ke balik pilar saat drone lewat.", "Kalia pulls Gala behind a pillar as a drone passes overhead.", "GK"),
    ("35A.2d", "Low Angle Shot", "Mereka tiba di kaki monumen mati yang menjulang, terbungkus es gelap.", "Low angle: they reach the base of the dead monument, towering and encased in dark ice.", "GK"),
    ]),
   half("35B", "Jangkar yang Retak",
    "Jantung Menara", [
    ("35B.1a", "Wide Interior Shot", "Di dalam dasar monumen, soket inti raksasa yang retak dan gelap.", "Inside the monument's base: a huge cracked core socket with no light at all.", ""),
    ("35B.1b", "First-Person POV (HUD)", "HUD: 'STRUCTURE TYPE: TEMPORAL ANCHOR - STATUS: DEAD'.", "First-person HUD scan: 'STRUCTURE TYPE: TEMPORAL ANCHOR - STATUS: DEAD'.", ""),
    ("35B.1c", "Close-Up", "Gala menekan gauntlet ke soket; percikan emas samar, lalu padam.", "Close-up: Gala presses his gauntlets into the socket; faint gold sparks, then nothing.", "G"),
    ("35B.1d", "Medium Shot", "Kalia memegang lentera, kecewa.", "Kalia holds up a lantern, disappointment on her face.", "K"),
    ],
    "Erosi di Lensa", [
    ("35B.2a", "Close-Up", "Partikel ungu mulai terlepas dari tepi bingkai goggles; goggles tetap terpasang.", "Close-up: purple particles begin drifting off the edge of Gala's goggle frame while the goggles stay on over his eyes.", "G"),
    ("35B.2b", "First-Person POV (HUD)", "HUD pecah-pecah: 'TEMPORAL INTEGRITY: 58%'.", "First-person HUD breaking apart into static: 'TEMPORAL INTEGRITY: 58%' flickering.", ""),
    ("35B.2c", "Medium Shot", "Gala terhuyung ke soket; Ethylene panik mengitarinya.", "Gala staggers against the socket as the sprite circles him in panic.", "GS"),
    ("35B.2d", "Title Card", "Kalia menangkap Gala; monumen mati menjulang: 'SEASON 3 - ARC 1 COMPLETE'.", "Kalia catches Gala as he falls, the dead monument looming above; title card 'SEASON 3 - ARC 1 COMPLETE'.", "GSK"),
    ])]},
  ]},
 ]}
