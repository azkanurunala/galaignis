# Location and secondary-character catalog for the Gala Ignis bible.
import re

LOCS = {
 "L01": ("Arena 7 Akademi", "Arena 7, the academy training arena: a large hexagonal hall; walls of dark gunmetal hexagon panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall."),
 "L02": ("Laboratorium Teknologi Akademi", "The academy tech lab: a bright white-and-teal room with curved walls, a central workbench under a large circular ring light; two rows of glowing teal hologram pedestals on the left and right; tall glass containment cylinders of glowing teal liquid along the back wall and the right wall; a sliding white door with a teal light strip in the middle of the front wall and a second identical door on the left wall."),
 "L03": ("Lorong Tembak Akademi", "The academy firing corridor: a long narrow gunmetal corridor with orange guide lights along the floor and five robotic plasma cannons mounted in a row on the far wall; at the near end, a wide wall display screen above the entrance door."),
 "L04": ("Ruang Simulasi dan Kontrol", "The simulation control room: a dim room with a row of four white egg-shaped simulation pods on the left, each with a reclined padded seat inside and a hinged reinforced-glass hatch; a curved wall of technician terminals with blue screens on the right; a large wall display screen on the back wall."),
 "L05": ("Kota Virtual Nusantara", "The virtual Nusantara city: a clean digital city of glowing towers with joglo-style tiered rooftops around a wide stone plaza, faint grid lines visible across the sky."),
 "L06": ("War Room Akademi", "The academy war room: a dark circular room with a large round tactical table projecting a 3D hologram, a ring of blue-lit screens around the curved walls, a heavy double door with a large gold Galians crest above it (a pair of gold wings around a round emblem with a flame at its center)."),
 "L07": ("Hanggar Akademi", "The academy hangar: a tall hangar with a sleek white-and-purple Galians transport ship on a landing pad, yellow floor markings, a huge sliding door open to the mountain sky."),
 "L08": ("Halaman Akademi", "The academy courtyard: a wide stone courtyard ringed by tiered academy buildings with joglo-style rooftops and gold trim on a mountainside, a golden dome shield faintly visible overhead."),
 "L09": ("Lorong Bawah Tanah Akademi", "The academy underground tunnels: narrow riveted metal tunnels with pipes along the ceiling and caged amber work lights."),
 "L10": ("Ruang Inti Akademi", "The academy core chamber: a vast round chamber with a colossal floating atomic crystal above a pool of golden plasma, metal catwalks ringing it."),
 "L11": ("Aula Upacara", "The academy ceremonial hall: tall pillars carved with gold batik, a long red aisle leading to a raised council altar, gold banners bearing the Galians crest."),
 "L12": ("Kamar dan Balkon Gala", "Gala's dorm room and balcony: a small room with a bunk bed and a desk by the window, opening onto a stone balcony that overlooks the city."),
 "L13": ("Ruang Dewan", "The council chamber: a semicircular chamber with tiered wooden seats, a raised council bench of dark wood with gold parang batik inlay, a public gallery above, a holographic projector in the center."),
 "L14": ("Menara Arsip Akademi", "The academy archive tower: a tall round library with spiral shelves of scrolls and glowing record crystals, a vault door with a batik-patterned lock at the lowest level, a domed roof on top."),
 "L15": ("Ruang Medis Akademi", "The academy medbay: a quiet white room with rounded beds, soft green monitor lights and tall windows."),
 "L16": ("Sel Tahanan", "The holding cells: a clean grey corridor of cells closed with glowing blue energy bars."),
 "L17": ("Bengkel Akademi", "The academy workshop: tool racks, a large workbench under hanging lamps, disassembled gadgets and floating holographic schematics."),
 "L18": ("Pusat Komunikasi Akademi", "The academy comm center: a dark room full of curved screens showing maps and signal lines around one central console chair."),
 "L19": ("Kawasan Pabrik Sektor 7", "The Sector 7 nano-fiber factory complex: grey factory blocks, tall smokestacks, a wide courtyard, a huge warehouse door."),
 "L20": ("Gudang Pabrik Sektor 7", "Inside the Sector 7 factory warehouse: towering fiber spools, conveyor belts and thick pipes, a broken skylight in the roof, a side room with frosted glass walls."),
 "L21": ("Ruang Reaktor Sektor 7", "The Sector 7 reactor room: a round room built around a tall cylindrical reactor core, a control console at its base."),
 "L22": ("Kota Nusantara", "The city of Nusantara: futuristic towers with joglo-style tiered rooftops and glowing gold batik light lines, elevated monorail tracks, greenery on terraces."),
 "L23": ("Alun-Alun Monumen Atom", "The monument plaza: a wide circular stone plaza at the foot of the Atomic Monument, a 300-meter spire engraved with glowing gold batik lines."),
 "L24": ("Puncak Monumen Atom", "The top of the Atomic Monument: a narrow circular platform around the spire tip with a glowing core socket at the center, the whole city far below."),
 "L25": ("Rumah Sakit Kota", "The city hospital: a white futuristic hospital with rounded wards of medical pods, a basement battery room and a rooftop with a radar tower."),
 "L26": ("Kilang Gas Atom", "The atomic gas plant: a maze of giant pipes, valve wheels and metal platforms."),
 "L27": ("Pasar Tua", "The old market: a narrow lane of wooden stalls under patched tarps lit by oil lamps, an herbal-drink stall at the corner."),
 "L28": ("Rumah Keluarga Dhruva", "Dhruva's family home: a small modest house in the east district with a flat rooftop and a living room with a worn couch."),
 "L29": ("Menara Vextron", "The Vextron Tower: a black glass skyscraper with thin violet circuit lines; inside, a black-glass lobby, an executive office with glass walls, server floors of violet-lit racks and a domed top chamber."),
 "L30": ("Gudang Persembunyian Nira", "Nira's hideout: an old warehouse full of electronic scrap with a scrap-built terminal in the middle."),
 "L31": ("Pelabuhan Timur dan Gudang 9", "The east docks: cranes and shipping containers, and Warehouse 9, a large former Vextron warehouse with a retractable roof."),
 "L32": ("Menara Siaran Kota", "The city broadcast tower control room: rows of cameras and broadcast screens with a wide window over the city."),
 "L33": ("Atap-Atap Kota", "The city rooftops: flat rooftops with water tanks, antennas and billboards, joglo-style tower roofs in the background."),
 "L34": ("Pegunungan Es dan Benteng Cryo-Tech", "The ice mountains: jagged icy peaks, and a dark mechanical fortress built into the frozen cliffs."),
 "L35": ("Interior Benteng Cryo-Tech", "Inside the Cryo-Tech fortress: long frozen metal corridors with blue lights and ice-crusted walls and pipes."),
 "L36": ("Ruang Generator Es", "The fortress generator room: a colossal room with a giant blue ice crystal spinning inside a metal ring, three catwalks circling it."),
 "L37": ("Absolute Zero Citadel", "The Absolute Zero Citadel: a massive dark crystal citadel in a frozen black valley under a perpetual blizzard."),
 "L38": ("Aula Citadel", "The citadel halls: grand halls of dark blue crystal with lines glowing beneath crystal floors."),
 "L39": ("Ruang Singgasana", "The citadel throne room: a dark crystal throne room with a black crystal throne atop tall stairs."),
 "L40": ("Kabin Kapal Angkut Galians", "Inside the Galians transport: a compact cabin with fold-down seats along both walls, round windows and an overhead grab rail."),
 "L41": ("Kota Cermin (lini masa paralel)", "The mirror city: the same city layout, but dark, abandoned and snowbound, no lights anywhere, faded blue snowflake banners on ruined towers."),
 "L42": ("Reruntuhan Akademi (lini masa paralel)", "The academy ruins of the parallel timeline: shattered academy buildings buried in snow, the scorched hexagonal arena open to the sky."),
 "L43": ("Markas Perlawanan Bawah Tanah", "The resistance base: an underground metro station with tiled walls, old train cars, lanterns built from salvaged batik panels and scrap workbenches."),
 "L44": ("Monumen Mati (lini masa paralel)", "The dead monument of the parallel timeline: the same Atomic Monument encased in dark ice, its batik lines unlit, a cracked dark core socket at its base."),
 "L45": ("Sektor 7 Paralel", "The defeated Sector 7: snowbound factories and broken smokestacks; inside the warehouse, hanging cocoons of clock glass."),
 "L46": ("Kuil Bukit Utara", "The hermit's shrine: a small stone shrine on a snowy hill with a single lantern at the door and an ancient wall relief inside."),
 "L47": ("Candi Kuno Hutan Selatan", "The ancient temple in the southern jungle: a stone temple rising from misty jungle, walls carved with reliefs of batik-sashed warriors, a carved stone gate at the top of the steps."),
 "L48": ("Interior Candi Kuno", "Inside the ancient temple: a corridor lined with stone guardian statues leading to a tomb chamber with a chained sarcophagus beneath a giant relief."),
 "L49": ("Desa dan Candi Kecil", "A countryside village of wooden houses around a small village temple with stone statues."),
 "L50": ("Candi Sungai", "The river temple: a small stone temple on stepping stones in a misty river."),
 "L51": ("Alam Nyala", "The realm of flame: a red-gold sky, rivers of glowing lava, floating stone islands and warm stone plains."),
 "L52": ("Gua Bara Agni", "Agni's ember cave: a cave with glowing red crystal walls and floating embers."),
 "L53": ("Padang Abu", "The ash fields: a silent grey field of dead ash under a dull sky, all color drained."),
 "L54": ("Desa Sprite", "The sprite village: small round huts of glowing stone perched on tall stone pillars."),
 "L55": ("Jembatan Lava dan Ceruk Batu", "The lava bridges: narrow stone bridges over rivers of lava, and a cooler rock alcove used for shelter."),
 "L56": ("Kawah Jantung", "The Heart Crater: a vast crater with steep glowing walls and a giant pulsing Heart of fire at its bottom."),
 "L57": ("Bagian Dalam Sang Hampa", "Inside Sang Hampa: an endless silent void of white static."),
 "L58": ("Pulau Emas (Simpul Barat)", "The golden terraces: stepped rice terraces on a hillside, a village on the slope and an ancient stone spire on the hilltop."),
 "L59": ("Hutan Awan (Simpul Utara)", "The cloud forest: giant ancient trees wrapped in mist, huge roots used as walkways, a node glowing inside the largest trunk."),
 "L60": ("Karang Laut (Simpul Timur)", "The coral sea: a fishing village on stilts above clear water, a stone spire standing on the coral seabed below."),
 "L61": ("Gunung Api (Simpul Selatan)", "The volcano: steep lava-rock slopes and a summit crater with an ancient stone spire at its rim."),
 "L62": ("Palung Tengah", "The central sea: open sea above a deep trench whose steep dark walls descend into darkness."),
 "L63": ("Bagian Dalam Katalis", "Inside the Entropy Catalyst: an endless silent white space."),
 "L64": ("Dermaga Kota", "The city pier: a long wooden-and-steel pier facing the open sea."),
 "L65": ("Laboratorium Rahasia Vikrama", "Vikrama's secret lab: a dark hidden lab behind a sliding bookshelf, with rows of glowing liquid tanks."),
 "L66": ("Jalur Monorail", "The elevated monorail line: a sleek monorail on a high track above the city streets."),
 "L67": ("Rumah Maheswari", "Maheswari's house: a traditional joglo-style wooden house with an open pendopo veranda and a quiet garden."),
 "L68": ("Kantor Vikrama", "Vikrama's office: a severe grey office with tall shelves, a large dark desk and a wall screen."),
}

# (id, name, anchor, regex, first_ep, last_ep)
SECONDARY = [
 ("K30", "Tiga Instruktur Akademi", "The three academy instructors, adult proportions, about twice Gala's height, in identical dark navy sci-fi uniforms with thin gold trim: Lead Instructor, tall stern man, grey buzz cut, sharp jaw; Second Instructor, stocky man, thick black mustache; Third Instructor, woman, short black bob, round glasses.", r"\binstructors?\b", 1, 30),
 ("K31", "Komandan Akademi", "The Academy Commander: an adult woman in her fifties with short grey-streaked black hair, a dark navy command uniform with gold epaulettes and a gold Galians crest on the chest.", r"Academy Commander|\bthe Commander\b(?! Hima| Frost)", 1, 45),
 ("K32", "Komandan Lapangan", "A senior Galians field commander: a broad-shouldered adult man with a grey beard in dark green field armor with a gold crest.", r"field commander", 1, 30),
 ("K33", "Drone Tempur AI (simulasi)", "Hexagon-armored AI combat drones: child-height humanoid training robots with hexagon plating and a single sensor eye, blue when normal and red when corrupted.", r"drone", 4, 5),
 ("K34", "Cryo-Drone", "Cryo-Drones: hovering spherical combat drones the size of a beach ball, white-and-ice-blue frosted armor plates, a single glowing ice-blue sensor eye, two small frost cannons.", r"Cryo-Drone|ice drone|\bdrones?\b", 6, 30),
 ("K35", "Cryo-Walker", "The Cryo-Walker: a giant four-legged walking tank of white-and-ice-blue armor with twin frost cannons on its back and a single blue sensor eye.", r"Walker", 8, 8),
 ("K36", "Cryo-Berserker", "Cryo-Berserkers: hulking humanoid robots in thick frost armor with glowing blue eyes, each wielding a glowing ice axe.", r"Berserker", 12, 12),
 ("K37", "Jenderal Eksekutif Cryo-Tech", "The Cryo-Tech Executive General: a towering humanoid in jagged frost armor with a torn ice cape, a glowing blue visor and a long ice spear.", r"\bGeneral\b", 13, 14),
 ("K38", "Cryo-Guard", "Cryo-Guards: humanoid soldiers in heavy white-and-ice-blue armor with blue visors and frost rifles.", r"Cryo-Guard|\bguards\b", 16, 26),
 ("K39", "Komandan Himakara", "Commander Himakara: a tall humanoid with pale blue-tinted skin and a stern bare face, in spiked blue crystal armor with a horned ice helmet that leaves his face uncovered, twin glowing frost swords, frost canisters on his back, no cape.", r"Himakara", 18, 20),
 ("K40", "Komandan Frostwing", "Commander Frostwing: a lean humanoid in sleek ice armor with huge mechanical wings made of ice blades and a heavy frost cannon.", r"Frostwing", 23, 24),
 ("K41", "Pengawal Elit Absolute Zero", "Elite Absolute Zero Guards: towering knights in black-and-deep-blue crystal armor wielding ice halberds.", r"guards?|halberd", 28, 28),
 ("K42", "Lord Absolute Zero", "Lord Absolute Zero: a massive figure in black and deep-blue spiked ice armor, a crown of ice spikes, a glowing crystal core in his chest, a dark blue anti-matter orb floating above one palm.", r"Lord Absolute Zero|\bthe Lord\b|Lord's", 28, 29),
 ("K43", "Pejuang Perlawanan", "Resistance fighters: people in hooded patched coats of faded indigo and grey, carrying makeshift rifles.", r"fighters?|resistance", 33, 45),
 ("K44", "Insinyur Tua Perlawanan", "An elderly resistance engineer with a white beard and a brass magnifying monocle, in a patched brown work apron.", r"resistance engineer", 36, 45),
 ("K45", "Pertapa Galians", "An old hermit in a faded Galians robe with a long grey braid, carrying a lantern.", r"hermit", 39, 39),
 ("K46", "Chrono-Wraith", "A Chrono-Wraith: a gaunt humanoid made of shattered clock glass and bent clock hands, trailing purple-silver afterimages, with long glass claws.", r"Wraith", 34, 42),
 ("K47", "Penjaga Cakrawala", "The Horizon Warden: a towering giant made of clock glass with slowly turning brass gears on its back and a clear purple crystal in its chest.", r"Warden", 40, 44),
 ("K48", "Anak Berjas Hujan Kuning", "A small boy with short black hair in a bright yellow raincoat with the hood down, a grey-and-white striped shirt, dark jeans, red rubber rain boots and a small tan backpack.", r"yellow raincoat", 1, 150),
 ("K49", "Arca Penjaga", "Stone guardian statues: tall carved mossy green-grey stone warriors with crested helmets, batik-patterned armor and stone staffs, black-violet glowing batik lines and glowing eyes.", r"statue", 47, 52),
 ("K50", "Laskar Purba", "Stone warriors: ancient warrior statues of plain grey sandstone with no moss, with black-violet glowing batik lines across their bodies, carrying stone spears.", r"stone warriors?", 52, 60),
 ("K51", "Lima Pendiri Dewan", "The five founders of the Council: elders in ancient ceremonial robes of deep green and gold, their faces stern.", r"founders", 51, 150),
 ("K52", "Staf Vextron", "Vextron staff: people in sleek grey suits with thin violet circuit collars.", r"grey suits?|grey-suited|Vextron response team", 60, 75),
 ("K53", "Vex-Guard", "Vex-Guards: sleek white humanoid androids with glossy armor, thin violet circuit lines and violet visors.", r"Vex-Guard|android", 61, 75),
 ("K54", "Vex-Drone", "Vex-Drones: small white-and-violet quadcopter drones with a glowing violet sensor ring.", r"Vex-Drone|\bdrones?\b", 61, 75),
 ("K55", "Vex-Core", "Vex-Core: a floating hologram of a faceless geometric head made of violet light.", r"Vex-Core|hologram of a faceless", 65, 75),
 ("K56", "Ibu dan Adik Dhruva", "Dhruva's mother, a kind woman in a rust-colored headscarf, and his little sister with her hair in twin buns.", r"Dhruva's mother|little sister", 60, 150),
 ("K57", "Nenek Penjual Jamu", "The old herbal-drink seller: an elderly woman in a faded batik kebaya and a simple headscarf, carrying a woven basket of herbal-drink bottles.", r"herbal-drink seller|\bold woman\b(?! with a bamboo)", 67, 150),
 ("K58", "Sprite Desa Alam Nyala", "Small fire sprites of various warm colors: tiny glowing orbs of red, amber and yellow flame with two white dot eyes each.", r"small fire sprites|village sprites|surviving sprites|\bthe sprites\b|tiny sprite|tiny orange sprite", 76, 150),
 ("K59", "Makhluk Abu", "Ash creatures: faceless humanoid shapes made of drifting grey ash.", r"ash creature", 79, 90),
 ("K60", "Garda Besi", "Garda Besi cadets: teenage cadets in steel-grey armor with red visors.", r"Garda Besi|\bcadets?\b", 91, 105),
 ("K61", "Penjaga Bersenjata Siphon", "Taraka's guards: soldiers in black-and-steel uniforms with red visors carrying small siphon rifles.", r"siphon rifle|\bGuards\b", 113, 113),
 ("K62", "Penjaga Simpul Barat", "The western node keeper: an old woman in a faded brown kebaya with a woven shawl and a bamboo staff.", r"keeper", 122, 125),
 ("K63", "Penjaga Simpul Utara", "The northern node keeper: an old man in a wide woven bamboo hat and a green sarong.", r"keeper", 126, 126),
 ("K64", "Penjaga Simpul Timur", "The eastern node keeper: an old fisherman with a white beard, a straw hat and a faded blue shirt.", r"keeper|old fisherman", 127, 127),
 ("K65", "Penjaga Simpul Selatan", "The southern node keeper: a very old thin man with long white hair in a simple grey robe.", r"keeper|old figure", 131, 134),
 ("K66", "Bayang Gerhana", "Eclipse shades: wolf-like shadow creatures outlined with a thin white corona.", r"eclipse shades|\bshades\b", 121, 135),
 ("K67", "Pengawal Dewan", "Council guards: guards in dark green ceremonial armor with gold trim, carrying long staffs.", r"council guards?", 1, 150),
 ("K68", "Kapal Angkut Galians", "The Galians transport ship: a sleek rounded dropship about the size of a city bus, glossy white hull with purple accent stripes, a gold winged Galians crest on each side, a tinted dark cockpit canopy at the front, two short swept-back wings each ending in a downward-angled engine pod glowing cyan, and a rear loading ramp.", r"\btransport\b|transport ship|dropship", 1, 150),
]
SECONDARY_RX = [(k, n, a, re.compile(rx, re.I if rx[0] != '\\' or True else 0), lo, hi) for k, n, a, rx, lo, hi in SECONDARY]
# Keeper overlap: the West keeper also appears at the terraces in Ep 142.
EXTRA_EP = {"K62": {142, 146, 149}, "K64": {128, 129, 133, 142, 146}, "K34": {32}}


def secondary_for(ep, scene):
    hits = []
    for k, n, a, rx, lo, hi in SECONDARY_RX:
        if (lo <= ep <= hi or ep in EXTRA_EP.get(k, ())) and rx.search(scene):
            hits.append(k)
    return hits


def load_locmap(path="locmap.txt"):
    m = {}
    for line in open(path):
        line = line.split("#")[0].strip()
        for tok in line.split():
            k, v = tok.split("=")
            m[k] = v
    return m


LOCMAP = load_locmap()


def location_for(code):
    ep = re.match(r"\d+", code).group()
    sub = re.match(r"\d+[AB]", code).group()
    act = code[:-1]
    for key in (code, act, sub, "E" + ep):
        if key in LOCMAP:
            v = LOCMAP[key]
            return None if v == "-" else v
    return None
