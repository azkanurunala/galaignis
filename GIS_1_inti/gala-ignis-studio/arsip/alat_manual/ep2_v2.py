# Episode 2 remake (v2): every panel generated alone, no text; lettering done locally.
REF = {
 "K01_final": "the Gala character sheet",
 "K03_final": "the Ethylene fire sprite sheet",
 "K30_ketiga": "the Third Instructor reference (the only instructor in this story)",
 "L02_final": "the tech lab environment sheet",
 "L03_final": "the firing corridor environment sheet",
 "L03_pintu": "the entrance end of the firing corridor: hazard-striped door with a wide display screen above it",
 "E02_REF_lab": "an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition)",
 "E02_Hal04_P4_raw": "an approved panel of this comic in the same corridor, reference for rendering style, lighting and the red plasma spheres only (do not copy its composition)",
 "E02_Hal04_P3_raw": "an approved panel of this comic showing how Gala and Ethylene are rendered and lit in this corridor (style reference only, do not copy its composition)",
 "E02_Hal05_P2_raw": "an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose)",
 "E02_Hal05_P3_raw": "an approved panel of this comic showing Gala from behind, kicking toward the cannons (camera-side and style reference, do not copy it)",
}
HEAD = ("Create a NEW single image, {ar}. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, "
        "no speech bubbles, no captions, no sound-effect lettering.\n"
        "Attached references, in order: {refs}. Copy the characters and the place EXACTLY from these references. Do not draw the sheets "
        "themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.\n"
        "Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.")
G = ("Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with "
     "fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik "
     "engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, "
     "green-and-purple boots. No pin or badge on his chest.")
E = ("Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame "
     "tail, two simple glowing white dot eyes, NO mouth, no limbs.")
I = ("The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal "
     "gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult "
     "proportions, about twice Gala's height. She is the only instructor; no other adults appear.")
LAB = ("Place: the bright white-and-teal academy tech lab from the lab sheet: curved walls, a central workbench under a large circular "
       "ring light, rows of glowing teal hologram pedestals on both sides, tall glass cylinders of teal liquid along the back and right "
       "walls, a sliding white door with a teal light strip in the front wall.")
CORR = ("Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small "
        "orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped "
        "entrance door with a display screen above it at the near end.")
HUD = ("Goggle HUD look: thin glowing blue and green grid lines and small round scan nodes overlaid on the view, a faint dark vignette "
       "like looking through goggle lenses, no readable text or numbers.")
AV = ("any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, "
      "distorted hands")
AVG = "goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors"
AVE = "a mouth on the fire sprite"
AVI = "other instructors or adults, a slim realistic model-like woman"
WIDE = "Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider."

def prompt(ar, files, body, avoid):
    refs = "; ".join(f"{i+1}) {REF[f]}" for i, f in enumerate(files))
    return HEAD.format(ar=ar, refs=refs) + "\n" + body + "\nAvoid: " + avoid + "."

def pn(name, ar, files, body, avoid, text, camera):
    return dict(name=name, ar=ar, files=files, prompt=prompt(ar, files, camera + "\n" + body, avoid), text=text)

# Continuity locked for the whole episode:
RULES = [
 "Gala menghadap meriam selama aksi di lorong. Kaki yang berapi dan menendang = kaki KIRI Gala: muncul di KANAN gambar saat Gala menghadap kamera, di KIRI gambar saat dilihat dari belakang.",
 "Kamera di belakang Gala = meriam terlihat di ujung lorong. Kamera di depan Gala = pintu bergaris kuning-hitam terlihat di belakangnya.",
 "Ethylene selalu ada: di bahu Gala, menyatu ke api kaki di Hal. 5, keluar dari asap sepatu di Hal. 6.",
 "Instruktur Ketiga satu-satunya orang dewasa; referensinya potongan K30_ketiga, bukan sheet tiga instruktur.",
 "Tidak ada teks di gambar. Semua balon, narasi, SFX dan tulisan layar ditulis lokal dengan Comic Neue Bold dan Bangers.",
]

PAGES = []
# ---------- Halaman 1: lab, chip
PAGES.append(dict(title="Halaman 1: Chip Pemindai", layout="wide / persegi + persegi / wide", panels=[
 pn("1 (atas, lebar)", "landscape 16:9", ["K01_final", "K03_final", "K30_ketiga", "L02_final", "E02_REF_lab"],
    "Scene: wide establishing shot of the whole bright lab. Gala walks in through the sliding white door on the left, Ethylene hovering beside his shoulder; the Third Instructor waits at the central workbench under the ring light, small in the middle distance.\n" + G + "\n" + E + "\n" + I + "\n" + LAB + "\nKeep the upper left corner as plain wall. " + WIDE,
    AV + ", " + AVG + ", " + AVE + ", " + AVI,
    [("caption", "Laboratorium Teknologi Akademi. / Sisa waktu: 19 jam.")],
    "Camera: eye level from the back of the lab, looking toward the front wall with the door.")
 ,pn("2 (tengah kiri)", "square 1:1", ["K30_ketiga", "L02_final", "E02_REF_lab"],
    "Scene: medium shot of the Third Instructor at the workbench, holding out between two fingers a tiny square chip engraved with gold batik lines, toward someone off-panel on the left. Calm, sharp-eyed.\n" + I + "\n" + LAB + "\nKeep the upper left quarter as plain softly blurred lab wall.",
    AV + ", " + AVI + ", Gala, children",
    [("bubble", "Chip pemindai / molekul. Pasang di / goggles-mu.")],
    "Camera: at her chest height, she faces slightly to the left of the camera.")
 ,pn("3 (tengah kanan)", "square 1:1", ["K01_final", "K03_final", "E02_REF_lab"],
    "Scene: close-up of Gala snapping the tiny gold-engraved chip into the side of his goggle frame with his fingers; a thin line of blue light runs around the rim of the goggles; big excited grin. Ethylene peeks in curiously from the right edge. The lenses stay fully opaque and dark.\n" + G + "\n" + E + "\nKeep the upper right corner as plain softly blurred lab wall.",
    AV + ", " + AVG + ", " + AVE + ", glowing lenses",
    [("sfx", "KLIK"), ("bubble", "Keren! / Ini buat apa?")],
    "Camera: close, at Gala's eye level, bright soft lab light.")
 ,pn("4 (bawah, lebar)", "landscape 16:9", ["K30_ketiga", "L02_final", "E02_REF_lab"],
    "Scene: the Third Instructor adjusts her round glasses with one finger, serious and calm, looking straight at the viewer (at Gala); the lab softly out of focus behind her. She stands on the left half of the image.\n" + I + "\n" + LAB + "\nKeep the right third of the image as plain softly blurred lab. " + WIDE,
    AV + ", " + AVI + ", Gala, the fire sprite",
    [("bubble", "Apimu meledak / karena kamu tidak / melihat apa yang / kamu bakar.")],
    "Camera: medium close-up at her eye level.")
]))
# ---------- Halaman 2: overload
PAGES.append(dict(title="Halaman 2: Terlalu Banyak Data", layout="wide / persegi + persegi / wide", panels=[
 pn("1 (atas, lebar)", "landscape 16:9", ["K30_ketiga", "L02_final", "E02_REF_lab"],
    "Scene: first-person view through Gala's goggles: the whole bright lab, every pedestal, cylinder and wall tagged with glowing grid lines and scan nodes, far too many of them; the Third Instructor small in the background near the cylinders. No body parts of Gala visible.\n" + HUD + "\n" + I + "\n" + LAB + "\nKeep the bottom center as plain floor. " + WIDE,
    AV + ", " + AVI + ", hands, readable HUD text",
    [("bubble_off", "Semuanya kelihatan. / Sampai ke atomnya!")],
    "Camera: Gala's eye level, looking into the lab.")
 ,pn("2 (tengah kiri)", "square 1:1", ["K01_final", "K03_final", "E02_REF_lab"],
    "Scene: Gala clutches his head with one hand, swaying and dizzy, gritted teeth; streams of blue and green data glow across the glossy surface of his opaque dark lenses; small motion wobble lines around his head. Ethylene hovers close to his cheek on the right side, worried.\n" + G + "\n" + E + "\nKeep the upper left corner as plain softly blurred lab wall.",
    AV + ", " + AVG + ", " + AVE,
    [("bubble", "Terlalu banyak! / Kepalaku!"), ("eth", "Pip?!")],
    "Camera: medium close-up, slightly tilted.")
 ,pn("3 (tengah kanan)", "square 1:1", ["K01_final", "E02_REF_lab"],
    "Scene: over-the-shoulder view from behind Gala's head (dark purple spiky hair and goggle strap in the right foreground): in front of him floating holographic atomic lattices flicker and glitch, streaked with red error bars; the lab darkened around the hologram.\n" + HUD + "\nKeep the upper third of the image dark and plain.",
    AV + ", " + AVG + ", readable HUD text",
    [("sfx", "BZZT!"), ("sfx", "BZZT!")],
    "Camera: behind Gala's right shoulder.")
 ,pn("4 (bawah, lebar)", "landscape 16:9", ["K01_final", "K03_final", "K30_ketiga", "E02_REF_lab"],
    "Scene: the Third Instructor, calm, holds a small glowing glass tablet and looks toward Gala; Gala stands dizzy in the left foreground seen from behind (big spiky hair, goggle strap, plain purple back plate), Ethylene hovering beside his head. She stands on the right half of the image.\n" + G + "\n" + E + "\n" + I + "\n" + LAB + "\nKeep the upper middle as plain softly blurred lab. " + WIDE,
    AV + ", " + AVG + ", " + AVE + ", " + AVI + ", the instructor shorter than Gala",
    [("bubble", "Jangan lihat semuanya. / Cari satu ikatan / yang paling lemah.")],
    "Camera: behind and left of Gala, at the instructor's chest height.")
]))
# ---------- Halaman 3: focus
PAGES.append(dict(title="Halaman 3: Satu Ikatan", layout="persegi + persegi / wide / wide", panels=[
 pn("1 (atas kiri)", "square 1:1", ["K01_final", "K03_final", "E02_REF_lab"],
    "Scene: close-up of Gala's face and shoulders, eyes hidden behind opaque dark lenses, a small calm smile; Ethylene hovers right beside his ear on the right, releasing soft warm golden particles that drift around his head.\n" + G + "\n" + E + "\nKeep the upper right corner as plain softly blurred lab wall.",
    AV + ", " + AVG + ", " + AVE,
    [("eth", "Pip.")],
    "Camera: close, at Gala's eye level, bright soft lab light.")
 ,pn("2 (atas kanan)", "square 1:1", ["K01_final", "E02_REF_lab"],
    "Scene: close-up of Gala breathing slowly, a small relieved smile; his lenses are opaque dark smoky glass with only thin faint horizontal lines of blue HUD light reflected across the surface, never round shapes in the lens centers.\n" + G + "\nKeep the lower left corner as plain softly blurred lab.",
    AV + ", " + AVG + ", round shapes on the lenses, the fire sprite",
    [("bubble", "Satu ikatan / saja.")],
    "Camera: close, slightly lower than his eyes.")
 ,pn("3 (tengah, lebar)", "landscape 16:9", ["L02_final", "E02_REF_lab"],
    "Scene: first-person view through Gala's goggles: a translucent blue holographic training dummy standing on a lab pedestal, one clean golden crosshair locked on its chest, the rest of the HUD quiet and dim. No characters, no body parts.\n" + HUD + "\nKeep the lower left corner plain. " + WIDE,
    AV + ", people, hands, readable HUD text",
    [("caption", "Kena.")],
    "Camera: Gala's eye level.")
 ,pn("4 (bawah, lebar)", "landscape 16:9", ["K01_final", "K03_final", "K30_ketiga", "L02_final", "E02_REF_lab"],
    "Scene: Gala in the left foreground seen in a three-quarter back view, in a low pencak silat stance aimed at a translucent blue holographic training dummy at the back center; Ethylene hovers by his shoulder. On the right, the Third Instructor lowers her tablet with a slight approving nod, clearly taller than Gala.\n" + G + "\n" + E + "\n" + I + "\n" + LAB + "\nKeep the upper right corner as plain wall. " + WIDE,
    AV + ", " + AVG + ", " + AVE + ", " + AVI + ", Gala facing the camera, the instructor shorter than Gala",
    [("bubble", "Itu baru latihan. / Ujiannya / menembak balik.")],
    "Camera: behind and left of Gala, eye level.")
]))
# ---------- Halaman 4: corridor
PAGES.append(dict(title="Halaman 4: Lorong Tembak", layout="wide / persegi + persegi / wide", panels=[
 pn("1 (atas, lebar)", "landscape 16:9", ["K01_final", "K03_final", "L03_final", "E02_Hal04_P4_raw"],
    "Scene: strong one-point perspective down the long dark corridor. Gala stands small in the lower left foreground seen from behind, looking toward the far end; Ethylene hovers beside his shoulder. At the far end, the five cannons charge with a red glow. His hands are empty.\n" + G + "\n" + E + "\n" + CORR + "\nKeep the upper left and upper right corners as plain dark wall. " + WIDE,
    AV + ", " + AVG + ", " + AVE + ", a bright room, a different number of cannons, glowing objects in his hands",
    [("caption", "Lorong Tembak Akademi."), ("speaker", "Lima meriam. / Jangan meledakkan apa pun.")],
    "Camera: behind Gala, looking down the corridor to the cannons.")
 ,pn("2 (tengah kiri)", "square 1:1", ["L03_final", "E02_Hal04_P4_raw"],
    "Scene: dramatic close-up of the five robotic plasma cannons on the end wall, dark metal barrels pointing at the camera, muzzles glowing hot red, faint heat haze and small sparks. No characters.\n" + CORR + "\nKeep the lower third fairly plain.",
    AV + ", characters, people",
    [("sfx", "WRRRM")],
    "Camera: low angle, facing the end wall.")
 ,pn("3 (tengah kanan)", "square 1:1", ["K01_final", "K03_final", "L03_final", "E02_Hal04_P3_raw"],
    "Scene: medium shot of Gala facing the camera, confident smirk, one fist raised in front of his chest; Ethylene bounces excitedly beside his head. Red glow from the cannons behind the camera lights his front; lenses opaque with only a tiny red reflection. Behind him: the hazard-striped entrance door.\n" + G + "\n" + E + "\n" + CORR + "\nKeep the top third above their heads as plain dark wall.",
    AV + ", " + AVG + ", " + AVE + ", cannons behind Gala",
    [("bubble", "Jangan dibakar semua. / Cari ikatannya."), ("eth", "Pip!")],
    "Camera: in front of Gala, on the cannon side, looking back toward the entrance door.")
 ,pn("4 (bawah, lebar)", "landscape 16:9", ["L03_final", "E02_Hal04_P4_raw"],
    "Scene: three glowing red plasma spheres fired at the same moment from three of the five cannons, streaking down the dark corridor straight toward the camera with long motion-blur trails, the nearest one large. No characters.\n" + CORR + "\nKeep the upper band fairly plain. " + WIDE,
    AV + ", characters, people, explosions",
    [("sfx", "DZING!"), ("sfx", "DZING!"), ("sfx", "DZING!")],
    "Camera: at Gala's position, looking down the corridor to the cannons.")
]))
# ---------- Halaman 5: weak points, fire
PAGES.append(dict(title="Halaman 5: Ikatan Terlemah", layout="wide / wide / wide besar", panels=[
 pn("1 (atas, lebar)", "landscape 16:9", ["L03_final", "E02_Hal04_P4_raw"],
    "Scene: first-person view through Gala's goggles, an extreme close view of ONE red plasma sphere filling most of the frame, the other two blurred behind it. The goggle HUD draws a thin glowing blue molecular lattice over the sphere's surface, like a net of linked nodes, and exactly ONE link in that net glows bright gold and is circled by a small golden target ring: the weakest bond. No body parts.\n" + HUD + "\n" + CORR + "\nKeep the upper left corner plain. " + WIDE,
    AV + ", people, hands, readable HUD text",
    [("caption", "Ikatan terlemahnya. Di situ.")],
    "Camera: Gala's eye level, looking toward the cannons.")
 ,pn("2 (tengah, lebar)", "landscape 16:9", ["K01_final", "K03_final", "L03_pintu", "E02_Hal05_P2_raw"],
    "Scene: Gala faces the camera in a wide low stance, determined grin, fists clenched. Ethylene dives down into the leg on the RIGHT side of the image, and golden-orange flames burst up and wrap tightly around that leg from boot to knee; Ethylene is half merged into the fire, still recognizable. His brown batik sash blows backward.\n" + G + "\n" + E + "\nBehind Gala: the hazard-striped entrance door with the display screen above it, exactly as in reference 3. No cannons visible.\nKeep the upper right corner as plain dark wall. " + WIDE,
    AV + ", " + AVG + ", " + AVE + ", cannons, flames on the leg on the left side of the image, fire spread on the floor",
    [("bubble", "Ethylene, / ke kakiku!"), ("eth", "Pip!")],
    "Camera: low angle in front of Gala, on the cannon side, looking back toward the entrance door.")
 ,pn("3 (bawah, besar)", "landscape 3:2", ["K01_final", "L03_final", "E02_Hal05_P3_raw"],
    "Scene: Gala mid-air in a spinning pencak silat kick, seen in a three-quarter back view, aimed at the far end. His kicking leg, on the LEFT side of the image, is wrapped in bright golden-orange flame and sweeps a wide flaming arc across the corridor right in the path of three red plasma spheres flying from the cannons straight at him. Sparks and embers. His back: big spiky hair with the goggle strap, plain purple back plate, green sleeves, brown batik sash.\n" + G + "\n" + CORR + "\nKeep the top quarter of the image as plain dark ceiling.",
    AV + ", " + AVG + ", Gala facing the camera, spheres coming from the side, explosions, spheres already destroyed, the fire sprite as a separate orb",
    [("sfx", "WHOOSH!")],
    "Camera: behind and slightly below Gala, looking down the corridor to the cannons.")
]))
# ---------- Halaman 6: sliced
PAGES.append(dict(title="Halaman 6: Terbelah", layout="splash wide / persegi + persegi / strip", panels=[
 pn("1 (atas, splash)", "landscape 16:9", ["K01_final", "L03_final", "E02_Hal05_P3_raw"],
    "Scene, the moment right after reference 3: Gala at the end of his spinning kick seen in a three-quarter back view, his flaming kicking leg on the LEFT side of the image; a huge glowing golden-orange flame arc has sliced all three red plasma spheres cleanly in half: six half-spheres drifting apart, bright golden sparks spraying along each clean cut. NO explosion, NO fireball, NO smoke cloud.\n" + G + "\n" + CORR + "\nKeep the top fifth as plain dark ceiling. " + WIDE,
    AV + ", " + AVG + ", explosions, fireballs, whole unbroken spheres, Gala facing the camera",
    [("sfx", "SRAAAK!")],
    "Camera: behind Gala, looking down the corridor to the cannons.")
 ,pn("2 (bawah kiri)", "square 1:1", ["K01_final", "L03_pintu", "E02_Hal05_P2_raw"],
    "Scene: Gala lands in a three-point landing facing the camera, one knee low, one fist on the floor, head up. Thin grey smoke curls from the boot on the RIGHT side of the image. Behind him six red half-spheres dissolve harmlessly into drifting golden sparks. Calm.\n" + G + "\nBehind Gala: the hazard-striped entrance door, exactly as in reference 2. No cannons.",
    AV + ", " + AVG + ", cannons, explosions, fire on his body",
    [],
    "Camera: low, in front of Gala on the cannon side, looking back toward the door.")
 ,pn("3 (bawah kanan)", "square 1:1", ["K01_final", "L03_pintu", "E02_Hal05_P2_raw"],
    "Scene: medium close-up of Gala still crouched, twisting to look back over his shoulder at the last golden sparks fading behind him near the door; surprised, eyebrows raised high above his thick goggles, mouth slightly open. Lenses fully opaque and dark.\n" + G + "\nBehind Gala: the hazard-striped entrance door. Keep the top third as plain dark wall.",
    AV + ", " + AVG + ", cannons, thin sunglasses instead of thick goggles",
    [("bubble", "Nggak meledak?")],
    "Camera: in front of Gala on the cannon side.")
 ,pn("4 (strip bawah)", "landscape 16:9", ["K03_final", "K01_final", "E02_Hal05_P2_raw"],
    "Scene: floor-level close-up: on the left third only Gala's green-and-purple boot and lower leg with thin grey smoke curling up; in the middle Ethylene pops out of that smoke with a tiny burst of golden sparks, shaking the smoke off, cheerful. The hazard-striped door softly out of focus behind.\n" + E + "\nKeep all action inside the middle horizontal band; top and bottom fifths plain dark wall and floor.",
    AV + ", " + AVE + ", Gala's face, a full figure of Gala, cannons",
    [("eth", "Pip!")],
    "Camera: at floor level.")
]))
# ---------- Halaman 7: result
PAGES.append(dict(title="Halaman 7: 99,8 Persen", layout="wide / wide / wide", panels=[
 pn("1 (atas, lebar)", "landscape 16:9", ["L03_pintu", "E02_Hal05_P2_raw"],
    "Scene: the wide display screen above the hazard-striped entrance door lights up with a plain bright green glow and a simple empty frame (the words will be added later), green light spilling over the door and floor. No characters.\n" + CORR + "\nThe screen must be BLANK, with no text, numbers or symbols. " + WIDE,
    AV + ", characters, any writing on the screen",
    [("screen", "TARGET NEUTRALIZED / PRECISION: 99.8%"), ("sfx", "DING!")],
    "Camera: facing the entrance end of the corridor.")
 ,pn("2 (tengah, lebar)", "landscape 16:9", ["K01_final", "K03_final", "L03_pintu", "E02_Hal05_P2_raw"],
    "Scene: Gala grins widely and gives a big thumbs-up to Ethylene, who bounces happily in the air in front of him; green light from the screen above the door behind them. Gala on the left half, Ethylene right of center.\n" + G + "\n" + E + "\nBehind them: the hazard-striped entrance door with the glowing green screen. Keep the upper corners plain. " + WIDE,
    AV + ", " + AVG + ", " + AVE + ", cannons",
    [("bubble", "99,8 persen! / Lihat itu, Ethylene!"), ("eth", "Pip! Pip!")],
    "Camera: in front of Gala on the cannon side, looking toward the door.")
 ,pn("3 (bawah, lebar)", "landscape 16:9", ["K01_final", "K03_final", "K30_ketiga", "L03_pintu", "E02_Hal05_P2_raw"],
    "Scene: the entrance door is open; the Third Instructor stands in the doorway on the right half, arms crossed, a small approving smile. In the left foreground Gala is seen from behind (spiky hair, goggle strap, plain purple back plate), thin smoke still rising from one boot and his sash; Ethylene by his shoulder.\n" + G + "\n" + E + "\n" + I + "\nKeep the upper left corner plain. " + WIDE,
    AV + ", " + AVG + ", " + AVE + ", " + AVI + ", the instructor shorter than Gala",
    [("bubble", "Tidak buruk, Taruna. / Tapi panasmu / masih bocor.")],
    "Camera: behind Gala, looking toward the open entrance door.")
]))
# ---------- Halaman 8: ending
PAGES.append(dict(title="Halaman 8: Panas yang Tersisa", layout="besar / strip penutup", panels=[
 pn("1 (atas, besar)", "portrait 4:5", ["K01_final", "K03_final", "L03_final", "E02_Hal05_P2_raw"],
    "Scene: Gala stands alone in the dim corridor holding up the end of his brown batik sash in one hand, looking down at it; thin smoke rises from the fabric and its batik lines glow faintly orange; Ethylene hovers beside his shoulder looking at it too, a little worried. Quiet, reflective mood.\n" + G + "\n" + E + "\n" + CORR + "\nKeep the upper left corner as plain dark wall.",
    AV + ", " + AVG + ", " + AVE,
    [("caption", "Sisa waktu: 14 jam.")],
    "Camera: medium shot, slightly above Gala, looking down at him.")
 ,pn("2 (strip bawah)", "landscape 16:9", ["K01_final", "E02_Hal05_P2_raw"],
    "Scene: a dark, moody end-card image: only a small folded piece of brown batik cloth resting on a dark metal floor, its batik lines glowing faintly orange, a thin wisp of smoke. Lots of empty dark space on the left and right for titles.\n" + WIDE,
    AV + ", characters, people",
    [("caption", "Bagaimana menjinakkan panas yang tersisa?"), ("title", "BERSAMBUNG"), ("sub", "Episode 3: Nanoselulosa Penyeimbang")],
    "Camera: close, slightly above the cloth.")
]))
# ---------- Sampul (art only)
COVER = pn("Sampul (gambar saja)", "portrait 9:16", ["K01_final", "K03_final", "L03_final", "E02_Hal05_P3_raw"],
    "Scene: dynamic cover art: Gala mid-air in a flaming pencak silat kick toward the camera, his kicking leg wrapped in golden-orange flame, slicing a red plasma sphere in half with golden sparks; Ethylene flying beside him; the dark hexagon corridor with orange lights behind. Thrilling, heroic.\n" + G + "\n" + E + "\nKeep the top quarter and the bottom tenth of the image as plain dark background for the title.",
    AV + ", " + AVG + ", " + AVE + ", explosions",
    [("title", "GALA IGNIS & THE GALIANS"), ("sub", "EPISODE 2: PEMETA MOLEKUL")],
    "Camera: low angle in front of Gala.")

# ---------- Audit 3 Okt: buang panel berinformasi rendah, variasikan ritme halaman
# Halaman 2: panel glitch (lama no. 3) dilebur ke panel 1; panel Gala pusing jadi panel utama yang besar.
_p2 = PAGES[1]
_p2['layout'] = "wide / besar (Gala pusing, sudut miring) / wide"
_p2['panels'][0] = pn("1 (atas, lebar)", "landscape 16:9", ["K30_ketiga", "L02_final", "E02_REF_lab"],
    "Scene: first-person view through Gala's goggles: the whole bright lab, every pedestal, cylinder and wall tagged with glowing grid lines and scan nodes, far too many of them, and several of the floating holographic lattices glitch with red error bars; the Third Instructor small in the background near the cylinders. No body parts of Gala visible.\n" + HUD + "\n" + I + "\n" + LAB + "\nKeep the bottom center as plain floor. " + WIDE,
    AV + ", " + AVI + ", hands, readable HUD text",
    [("bubble_off", "Semuanya kelihatan. / Sampai ke atomnya!"), ("sfx", "BZZT!")],
    "Camera: Gala's eye level, looking into the lab.")
_p2['panels'][1] = pn("2 (tengah, besar)", "landscape 3:2", ["K01_final", "K03_final", "E02_REF_lab"],
    "Scene: a strongly tilted Dutch-angle close shot of Gala clutching his head with both hands, swaying, gritted teeth; streams of blue and green data race across the glossy surface of his opaque dark lenses; wobble lines around his head. Ethylene hovers close to his cheek on the right side, worried, its flame crown flattened.\n" + G + "\n" + E + "\nKeep the upper left corner as plain softly blurred lab wall.",
    AV + ", " + AVG + ", " + AVE + ", a level horizon",
    [("bubble", "Terlalu banyak! / Kepalaku!"), ("eth", "Pip?!")],
    "Camera: close, tilted about 20 degrees, slightly below Gala's face.")
del _p2['panels'][2]
_p2['panels'][2]['name'] = "3 (bawah, lebar)"
# Halaman 7: panel layar kosong dihapus; layar terlihat di panel jempol dan tulisannya ditulis lokal.
_p7 = PAGES[6]
_p7['layout'] = "besar (Gala, Ethylene dan layar hasil) / wide"
_p7['panels'][1] = pn("1 (atas, besar)", "landscape 3:2", ["K01_final", "K03_final", "L03_pintu", "E02_Hal05_P2_raw"],
    "Scene: Gala grins widely and gives a big thumbs-up to Ethylene, who bounces happily in the air in front of him. Above the hazard-striped door behind them, the wide display screen glows plain bright green with an empty frame and NO writing (the words are added later); green light spills over both of them. Gala on the left half, Ethylene right of center, the whole screen visible in the upper part of the image.\n" + G + "\n" + E + "\nThe screen must be BLANK. Keep the lower corners plain.",
    AV + ", " + AVG + ", " + AVE + ", cannons, any writing on the screen",
    [("screen", "TARGET NEUTRALIZED / PRECISION: 99.8%"), ("sfx", "DING!"), ("bubble", "99,8 persen! / Lihat itu, Ethylene!"), ("eth", "Pip! Pip!")],
    "Camera: in front of Gala on the cannon side, slightly low, looking toward the door.")
del _p7['panels'][0]
_p7['panels'][1]['name'] = "2 (bawah, lebar)"
RULES.append("Sains episode ini satu gagasan saja: ikatan terlemah putus lebih dulu. Chip memetakan ikatan, Gala memutus satu ikatan terlemah, bukan membakar semuanya. Ini fiksi yang bertumpu pada prinsip kimia umum, bukan klaim tentang plasma sungguhan.")
RULES.append("Video Short dibuka dengan panel tendangan api (Hal. 5 panel 3) selama 1 sampai 2 detik sebelum Halaman 1, bukan dengan panel lab yang tenang.")
