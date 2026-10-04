# Sub-Episode B for Episodes 6-15. Flags: G=Gala, S=Ethylene, A=Aila, D=Dhruva
def sub(i, title, a1t, a1, a2t, a2):
    return {"id": f"{i}B", "title": title, "acts": [
        {"id": f"{i}B.1", "title": a1t, "frames": a1},
        {"id": f"{i}B.2", "title": a2t, "frames": a2}]}

B1 = {
6: sub(6, "Jejak di Luar Gudang",
 "Pekerja yang Membeku", [
 ("6B.1a", "Wide Atmospheric Shot", "Halaman pabrik berkabut; kendaraan patroli membeku; seorang pekerja terkurung lapisan es tipis di dinding gudang.", "Foggy factory courtyard at night: a frozen patrol vehicle, and a night-shift worker encased in a thin shell of blue ice against the warehouse wall; Gala and his squad approach cautiously.", "GAD"),
 ("6B.1b", "Close-Up", "Gala menempelkan kain sarung ke es; es mencair menjadi uap.", "Close-up: Gala presses his glowing batik sash against the ice shell; the ice melts into rising steam.", "G"),
 ("6B.1c", "Medium Shot", "Dhruva menyelimuti pekerja yang menggigil; pekerja menunjuk ke gudang.", "Dhruva wraps a silver thermal blanket around the shivering worker, who points a trembling finger toward the warehouse.", "D"),
 ("6B.1d", "First-Person POV (HUD)", "HUD mencatat laporan: 'WORKERS TRAPPED INSIDE - WAREHOUSE B'.", "First-person HUD view: a clean alert panel reading 'WORKERS TRAPPED INSIDE - WAREHOUSE B' over the dark warehouse facade.", ""),
 ],
 "Rencana Penyusupan", [
 ("6B.2a", "Medium Shot", "Gala menggambar rencana di hologram kecil; Aila dan Dhruva mencondongkan badan.", "Gala sketches an entry plan on a small floating hologram; Aila and Dhruva lean in close, lit by its glow.", "GAD"),
 ("6B.2b", "Action Shot", "Aila menunggangi arus angin naik ke atap gudang.", "Aila rides a spiraling updraft of wind up the warehouse wall and lands lightly on the roof.", "A"),
 ("6B.2c", "Close-Up", "Visor Aila memindai ventilasi atap dan mengirim sinyal hijau.", "Close-up: Aila's teal visor scans a roof vent grille and flashes a green all-clear ping.", "A"),
 ("6B.2d", "Medium Shot", "Gala turun lewat ventilasi menyusul rekan-rekannya; Ethylene menerangi lorong.", "Gala drops down the dark roof vent shaft after his teammates, the sprite lighting the narrow metal walls.", "GS"),
 ]),
7: sub(7, "Drone yang Kabur",
 "Perisai untuk Para Pekerja", [
 ("7B.1a", "Wide Shot", "Sisa drone berbalik ke ruang samping berkaca buram tempat pekerja terkurung.", "Remaining Cryo-Drones turn toward a side room with frosted glass walls where trapped workers huddle inside.", ""),
 ("7B.1b", "Action Shot", "Dhruva menghantamkan perisainya di depan pintu; sinar pembeku memercik.", "Dhruva slams his tower shield down in front of the side-room door; freezing blue beams splash off its batik face.", "D"),
 ("7B.1c", "Close-Up", "Wajah takut para pekerja di balik kaca buram; tepi perisai berpijar.", "Close-up: frightened workers' faces behind frosted glass, the glowing edge of a bronze shield in the foreground.", ""),
 ("7B.1d", "Dynamic Action Shot", "Gala menyerbu dari samping dan menendang dua drone menjauh dari Dhruva.", "Gala charges in from the flank and sweeps a flaming arc kick that knocks two drones away from Dhruva.", "GD"),
 ],
 "Drone Pembawa Pesan", [
 ("7B.2a", "Wide Shot", "Drone terakhir kabur ke skylight pecah, antenanya berkedip 'TRANSMITTING'.", "The last Cryo-Drone flees upward toward a broken skylight, a blue antenna light blinking 'TRANSMITTING'.", ""),
 ("7B.2b", "Action Shot", "Aila melesat dengan hembusan angin, bilah angin memotong rotor drone.", "Aila launches on a gust of wind; twin crescent wind blades clip the fleeing drone's rotors.", "A"),
 ("7B.2c", "Mid-Air Action Shot", "Gala menangkap drone yang jatuh; api gauntlet memutus antenanya.", "Mid-air, Gala catches the falling drone in one gauntlet, flame crackling over it and shorting out its antenna.", "G"),
 ("7B.2d", "Medium Shot", "Gala mendarat dan menjatuhkan drone berasap; gudang menghangat, Ethylene kembali terang.", "Gala lands and drops the smoking drone at his feet as the warehouse warms; the sprite brightens again beside him.", "GS"),
 ]),
8: sub(8, "Jatuhnya Sang Walker",
 "Serangan Terakhir", [
 ("8B.1a", "Close-Up", "Sensor Cryo-Walker yang retak menyala merah lagi.", "Close-up: the cracked optical sensor of the fallen Cryo-Walker flickers back on, glowing red.", ""),
 ("8B.1b", "Wide Action Shot", "Meriam rusak Walker menembakkan beku terakhir ke pipa pendingin reaktor.", "The damaged Cryo-Walker fires one last frost blast from its broken cannon into the reactor's coolant pipes.", ""),
 ("8B.1c", "Medium Action Shot", "Gala dan Dhruva menghancurkan dudukan meriam bersamaan.", "Gala and Dhruva strike the Walker's cannon mount together, a flaming fist and a shield bash, tearing it loose.", "GD"),
 ("8B.1d", "Wide Shot", "Walker padam total; es merambat di rumah reaktor di belakang mereka.", "The Walker powers down for good while blue frost spreads across the reactor housing behind the squad.", ""),
 ],
 "Perintah Evakuasi", [
 ("8B.2a", "First-Person POV (HUD)", "HUD: 'REACTOR STABILITY: 41% - DROPPING'.", "First-person HUD warning 'REACTOR STABILITY: 41% - DROPPING' over a pulsing reactor core.", ""),
 ("8B.2b", "Medium Shot", "Gala memberi perintah: Aila dan Dhruva mengawal para pekerja.", "Gala gives firm hand orders to Aila and Dhruva, pointing toward the trapped workers' side room.", "GAD"),
 ("8B.2c", "Medium Shot", "Aila membuka ruang samping; para pekerja berhamburan keluar.", "Aila unlocks the frosted side-room door and waves the workers out as they stream past her.", "A"),
 ("8B.2d", "Close-Up", "Gala menghadap reaktor sendirian sambil mengencangkan kain sarung.", "Gala turns alone to face the unstable reactor, tightening the knot of his batik sash.", "G"),
 ]),
9: sub(9, "Setelah Reaktor Tenang",
 "Kelelahan Sang Taruna", [
 ("9B.1a", "Medium Shot", "Gala duduk bersandar di dasar reaktor, terengah; uap mengepul dari kain sarung yang mendingin.", "Gala sits slumped against the base of the calm green reactor, panting, steam curling off his cooling sash.", "G"),
 ("9B.1b", "Close-Up", "Ethylene kembali dan meringkuk di bahu Gala.", "Close-up: the sprite returns and curls up on Gala's shoulder, its warm glow on his cheek.", "GS"),
 ("9B.1c", "Medium Shot", "Aila dan Dhruva berlari masuk dengan lega.", "Aila and Dhruva rush back into the reactor room, relief on their faces at seeing Gala safe.", "GAD"),
 ("9B.1d", "Medium Shot", "Dhruva menarik Gala berdiri dengan menggenggam lengannya.", "Dhruva grips Gala's forearm and hauls him to his feet with a grin.", "GD"),
 ],
 "Data yang Tersembunyi", [
 ("9B.2a", "Close-Up", "Gala menyambungkan inti data drone ke port di bingkai goggles.", "Close-up: Gala plugs the captured drone's small data core into a port on the side of his goggle frame.", "G"),
 ("9B.2b", "First-Person POV (HUD)", "HUD: pohon berkas terenkripsi, 'DECRYPTING... 12%'.", "First-person HUD: an encrypted file tree with a progress bar reading 'DECRYPTING... 12%'.", ""),
 ("9B.2c", "Wide Shot", "Di luar, langit subuh; pekerja yang diselamatkan melambai.", "Outside under a blue pre-dawn sky, rescued workers wrapped in blankets wave at the squad leaving the factory.", ""),
 ("9B.2d", "Medium Shot", "Gala membalas lambaian; proses dekripsi terpantul di lensanya.", "Gala raises a hand back to the workers, the decryption progress still reflected on his lenses.", "G"),
 ]),
10: sub(10, "Pulang ke Akademi",
 "Laporan kepada Dewan", [
 ("10B.1a", "Wide Shot", "Kapal angkut mendarat di hanggar akademi pagi hari.", "The Galians transport touches down in the academy hangar in morning light.", ""),
 ("10B.1b", "Medium Shot", "Gala, Aila, dan Dhruva berdiri tegak di hadapan Komandan Akademi.", "Gala, Aila and Dhruva stand at attention before the Academy Commander in a command office.", "GAD"),
 ("10B.1c", "Close-Up", "Komandan meninjau berkas Absolute Zero yang melayang, wajah tegang.", "Close-up: the Academy Commander reviews floating 'ABSOLUTE ZERO' files, face grim.", ""),
 ("10B.1d", "Medium Close-Up", "Gala menangkap kabar: akademi adalah target berikutnya.", "Medium close-up: Gala's jaw tightens as the Commander delivers the news, a red academy map reflected on his lenses.", "G"),
 ],
 "Tenang Sebelum Badai", [
 ("10B.2a", "Wide Shot", "Malam; kubah akademi berkilau; Gala sendirian di balkon latihan.", "Night: the academy's golden dome shimmers faintly; Gala stands alone on a training balcony.", "G"),
 ("10B.2b", "Close-Up", "Gala dan Ethylene berbagi momen tenang; Ethylene di telapak tangannya.", "Close-up: the sprite rests quietly in Gala's open palm, both looking at the stars.", "GS"),
 ("10B.2c", "Wide Shot", "Jauh di balik pegunungan, cahaya biru armada drone berkumpul.", "Far beyond dark mountains, faint blue lights of a massing drone fleet glimmer on the horizon.", ""),
 ("10B.2d", "Title Card", "Siluet Gala dan Ethylene di balkon: 'ARC 2 COMPLETE - SECTOR 7 SECURED'.", "Gala and the sprite silhouetted on the balcony against the night sky; title card 'ARC 2 COMPLETE - SECTOR 7 SECURED'.", "GS"),
 ]),
11: sub(11, "Halaman yang Membara",
 "Menahan Gelombang Pertama", [
 ("11B.1a", "Wide Action Shot", "Gala dan barisan instruktur menahan drone di halaman.", "Gala fights beside the instructors' firing line, holding back ice drones in the snowy courtyard.", "G"),
 ("11B.1b", "Action Shot", "Dhruva menancapkan perisai melindungi taruna junior dari hujan es.", "Dhruva plants his tower shield over a group of junior cadets as shards of ice rain down.", "D"),
 ("11B.1c", "Action Shot", "Pusaran angin Aila menghamburkan drone kecil ke arah api Gala.", "Aila spins into a wind vortex that flings small drones straight into Gala's arc of fire.", "GA"),
 ("11B.1d", "Impact Shot", "Sapuan api Gala membuka jalur di halaman.", "Gala's sweeping fire kick clears a burning lane through the drones.", "G"),
 ],
 "Retakan Melebar", [
 ("11B.2a", "Wide Shot", "Celah kubah melebar; gelombang kedua yang lebih besar masuk.", "The breach in the golden dome widens; a second, larger wave of drones pours through.", ""),
 ("11B.2b", "Close-Up", "Seorang instruktur berteriak, lengannya membeku.", "Close-up: a senior instructor shouts orders, one arm crusted with frost.", ""),
 ("11B.2c", "Medium Shot", "Gala menarik instruktur ke balik perlindungan sambil melirik celah kubah.", "Gala drags the wounded instructor behind cover, glancing up at the widening breach.", "G"),
 ("11B.2d", "First-Person POV (HUD)", "HUD: 'ENEMY SIGNAL ROUTING UNDERGROUND - CORE ACCESS TUNNELS'.", "First-person HUD: a red route line diving below the courtyard, labeled 'ENEMY SIGNAL ROUTING UNDERGROUND - CORE ACCESS TUNNELS'.", ""),
 ]),
12: sub(12, "Lorong yang Runtuh",
 "Formasi di Lorong Sempit", [
 ("12B.1a", "Wide Shot", "Dua Berserker lagi menyerbu; regu membentuk formasi, Dhruva di depan.", "Two more Cryo-Berserkers charge down the tunnel; the squad forms up with Dhruva at the front.", "GAD"),
 ("12B.1b", "Action Shot", "Perisai Dhruva mengunci kapak es; Aila meluncur di bawahnya.", "Dhruva's shield locks against a glowing ice axe while Aila slides low beneath the clash.", "AD"),
 ("12B.1c", "Action Shot", "Bilah angin Aila memutus lengan kapak Berserker.", "Aila's wind blade shears through the Berserker's axe arm in a spray of ice.", "A"),
 ("12B.1d", "Impact Shot", "Tendangan api Gala menumbangkan Berserker kedua.", "Gala's flaming kick drops the second Berserker onto the tunnel floor.", "G"),
 ],
 "Terpisah", [
 ("12B.2a", "Wide Shot", "Langit-langit retak dan runtuh, memisahkan Gala dari rekan-rekannya.", "The tunnel ceiling cracks and collapses in ice and rock, sealing Gala off from his teammates.", "G"),
 ("12B.2b", "Close-Up", "Lewat celah reruntuhan, Dhruva menahan puing dengan perisai; Aila berteriak menyuruh Gala pergi.", "Through a gap in the rubble, Dhruva braces falling debris with his shield while Aila shouts at Gala to go on.", "AD"),
 ("12B.2c", "Medium Shot", "Gala ragu, kepalan tangan menegang, lalu berbalik.", "Gala hesitates, fist clenched, then turns away from the rubble.", "G"),
 ("12B.2d", "Tracking Shot", "Gala berlari di lorong gelap menuju pintu inti yang bercahaya.", "Gala sprints down the dark tunnel toward a glowing core door, the sprite lighting the way.", "GS"),
 ]),
13: sub(13, "Regu yang Kembali",
 "Api yang Menolak Padam", [
 ("13B.1a", "Action Shot", "Gala yang membara menyerbu Jenderal; pertukaran pukulan cepat.", "Blazing with gold fire, Gala charges the General in a rapid exchange of blows on the catwalk.", "G"),
 ("13B.1b", "Close-Up", "Tombak es menggores pelindung bahu Gala; es meretakkan batik emas.", "Close-up: the General's frost spear grazes Gala's shoulder plate, frost cracking across the gold batik.", "G"),
 ("13B.1c", "First-Person POV (Warning)", "HUD: 'CORE FREEZING AT 95%'.", "First-person HUD warning 'CORE FREEZING AT 95%', frost thick at the edges.", ""),
 ("13B.1d", "Medium Shot", "Gala terdorong mundur ke tepi kolam plasma.", "Gala skids backward to the very edge of the golden plasma pool, boots sparking.", "G"),
 ],
 "Bala Bantuan dari Balik Dinding", [
 ("13B.2a", "Wide Shot", "Dinding samping jebol; Dhruva menerjang dengan perisai, Aila di belakangnya.", "A side wall bursts open; Dhruva shield-charges through the rubble with Aila right behind him.", "AD"),
 ("13B.2b", "Action Shot", "Hembusan Aila meniup kabut beku dari kristal inti.", "Aila sends a powerful gust that blows the freezing mist off the core crystal, buying precious seconds.", "A"),
 ("13B.2c", "Action Shot", "Dhruva menjepit tombak Jenderal dengan perisainya.", "Dhruva pins the General's frost spear against the catwalk rail with his shield.", "D"),
 ("13B.2d", "Medium Shot", "Gala mundur dan memasang kuda-kuda; energi berkumpul di boots.", "Gala steps back and plants his feet, gold energy gathering around his boots.", "G"),
 ]),
14: sub(14, "Gema Kemenangan",
 "Sisa Sang Jenderal", [
 ("14B.1a", "Medium Shot", "Jenderal berlutut; zirahnya rontok menjadi embun beku.", "The General collapses to his knees, his armor crumbling into drifting frost.", ""),
 ("14B.1b", "Close-Up", "Visor Jenderal retak; ia tertawa dingin, lambang kepingan salju berpijar.", "Close-up: the General's visor cracks; a cold laugh as a blue snowflake emblem glows on his chest.", ""),
 ("14B.1c", "Wide Shot", "Jenderal larut menjadi awan beku, meninggalkan kristal data berbentuk kepingan salju.", "The General dissolves into a cloud of frost, leaving behind a small snowflake-shaped blue data crystal on the catwalk.", ""),
 ("14B.1d", "Close-Up", "Gala memungut kristal; pantulan HUD: 'SOURCE: ABSOLUTE ZERO COMMAND'.", "Close-up: Gala picks up the crystal in his gauntlet, his lenses reflecting 'SOURCE: ABSOLUTE ZERO COMMAND'.", "G"),
 ],
 "Kubah yang Pulih", [
 ("14B.2a", "Wide Shot", "Kristal inti berdenyut emas; kubah akademi menutup celahnya.", "The core crystal pulses gold and the academy's golden dome seals its breach from edge to edge.", ""),
 ("14B.2b", "Wide Shot", "Drone di luar kehilangan sinyal dan jatuh ke salju.", "Outside, the remaining drones lose signal and drop lifeless into the snow.", ""),
 ("14B.2c", "Medium Shot", "Aila dan Dhruva memapah Gala keluar dari ruang inti.", "Aila and Dhruva help Gala walk out of the core chamber, his arms over their shoulders.", "GAD"),
 ("14B.2d", "Wide Shot", "Ketiganya keluar ke halaman berasap; para taruna bersorak.", "The three step out into the smoky courtyard as cadets cheer and raise their fists.", "GAD"),
 ]),
15: sub(15, "Sang Vanguard dan Regunya",
 "Perintah Pertama", [
 ("15B.1a", "Medium Shot", "Komandan menugaskan Aila dan Dhruva ke regu Vanguard Gala; roster hologram menyala.", "The Academy Commander assigns Aila and Dhruva to Vanguard Gala's squad, a holographic squad roster glowing between them.", "GAD"),
 ("15B.1b", "Close-Up", "Tiga kepalan beradu; Ethylene melayang di atasnya.", "Close-up: three fists bump together in the center, the sprite hovering just above them.", "GSAD"),
 ("15B.1c", "Wide Shot", "Festival malam di halaman dengan lampion bermotif batik.", "A night festival in the academy courtyard, strings of batik-patterned lanterns glowing warm.", ""),
 ("15B.1d", "Medium Shot", "Gala tertawa bersama regunya di kedai; Ethylene mencuri percikan dari lampion.", "Gala laughs with Aila and Dhruva at a food stall while the sprite steals a spark from a lantern.", "GSAD"),
 ],
 "Sinyal dari Pegunungan", [
 ("15B.2a", "Close-Up", "Kristal data kepingan salju di meja Gala berkedip biru sendiri.", "Close-up: the snowflake data crystal on Gala's desk blinks blue on its own in the dark room.", ""),
 ("15B.2b", "First-Person POV (HUD)", "HUD: 'SIGNAL ORIGIN: NORTHERN ICE RANGE - CRYO-TECH FORTRESS'.", "First-person HUD tracing the signal to snowy peaks: 'SIGNAL ORIGIN: NORTHERN ICE RANGE - CRYO-TECH FORTRESS'.", ""),
 ("15B.2c", "Medium Shot", "Gala berdiri di jendela menatap pegunungan bersalju di bawah bulan.", "Gala stands at his window looking toward distant snowy mountains under the moon.", "G"),
 ("15B.2d", "Title Card", "Siluet Gala dan Ethylene di jendela: 'SEASON 1 COMPLETE'.", "Gala and the sprite silhouetted at the window with moonlit mountains beyond; title card 'SEASON 1 COMPLETE'.", "GS"),
 ]),
}
