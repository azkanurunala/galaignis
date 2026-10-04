STYLE = ("Rendering style, identical in every panel and on every page: 3D CGI render, like still frames taken from a modern 3D animated "
         "feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Every panel is a "
         "3D rendered image. The only 2D elements on the page are the panel borders, speech bubbles, caption boxes and lettering, overlaid on "
         "top of the renders. Page layout: 2:3 portrait, thin black panel borders, white gutters. Lettering: white speech bubbles with thin "
         "black outlines and tails pointing to the speaker, pale yellow caption boxes with black text, bold clean comic font. Render every "
         "text exactly as written, in Indonesian, with correct spelling.")
GALA = ("Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; "
        "dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes; his eyes are never visible through the lenses, "
        "even in close-ups; fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; "
        "green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots. "
        "No pin or badge on his chest.")
ETH = ("Ethylene: a fist-sized fire sprite, a perfectly round glossy glowing amber orb with a small flickering flame crown on top, two small "
       "flame wisps on its sides like tiny wings and a thin flame tail, two simple glowing white dot eyes, no mouth, no limbs.")
INSTR3 = ("The Third Instructor: an adult woman with adult proportions, about twice Gala's height, short black bob hair, round glasses, "
          "a dark navy sci-fi uniform with thin gold trim, calm and sharp-eyed. She is the ONLY instructor in this comic; the other two "
          "instructors from the sheet never appear.")
LAB = ("Setting, the academy tech lab, the same room on every lab page: a bright white-and-teal room with smoothly curved walls; a central "
       "workbench under a large circular ring light; two rows of glowing teal hologram pedestals on the left and right; tall glass containment "
       "cylinders of glowing teal liquid along the back wall and the right wall; a sliding white door with a teal light strip in the middle of "
       "the front wall.")
CORR = ("Setting, the academy firing corridor, the same place on every corridor page: a long narrow corridor with dark gunmetal hexagon wall "
        "panels and a low ceiling; two lines of small glowing orange guide lights along the floor edges; at the far end, five robotic plasma "
        "cannons mounted in one horizontal row on the end wall; at the near end, a heavy entrance door with yellow-and-black hazard stripes "
        "and a wide wall display screen above it.")
HUD = ("The goggle HUD look, whenever the view is through Gala's goggles: thin glowing blue and green grid lines and small round scan nodes "
       "overlaid on the scene, a faint dark vignette at the edges like looking through goggle lenses, no readable text or numbers in the HUD.")
def avoid(chars):
    a = ["goggles pushed up or removed", "Gala's eyes visible", "a pin or badge on Gala's chest"]
    if "ETH" in chars: a.append("a mouth on the fire sprite")
    if "INSTR3" in chars: a.append("the other two instructors")
    a += ["helmets", "capes", "masks", "extra accessories", "changed hair or armor colors", "a different room design", "extra limbs",
          "distorted hands", "misspelled text", "2D illustration", "drawn line art", "ink outlines on characters", "anime or manga style",
          "cel shading", "flat colors", "sketch", "watercolor", "screentone"]
    return "Avoid: " + ", ".join(a) + "."

SHEET = {"GALA": ("K01_final", "the Gala character sheet"), "ETH": ("K03_final", "the Ethylene sheet"),
         "INSTR3": ("K30", "the instructors sheet, use ONLY the woman with the short black bob and round glasses")}
LOCSHEET = {"LAB": ("L02_final", "the tech lab environment sheet"), "CORR": ("L03_final", "the firing corridor environment sheet")}
STYLEREF = {"cover": ("Sampul_final", "the approved cover of Episode 1, as the reference for rendering quality and title lettering only (do not copy its pose, room or text)"),
            "page": ("Hal01_final", "an approved page from Episode 1, as the reference for rendering quality, panel borders, speech bubbles, caption boxes and lettering only (do not copy its panels, room or poses)")}
STYLE_BY_PAGE = {
    0: None,
    1: None,
    2: ("E02_Hal01_final", "the approved page 1 of this episode, same lab, as the reference for rendering quality, speech bubbles, caption boxes and lettering only (do not copy its panels or poses)"),
    3: ("E02_Hal01_final", "the approved page 1 of this episode, same lab, as the reference for rendering quality, speech bubbles, caption boxes and lettering only (do not copy its panels or poses)"),
    4: ("E02_Sampul_final", "the approved cover of this episode, same corridor, as the reference for rendering quality and the look of the corridor only (do not copy its pose or text)"),
    5: ("E02_Hal04_final", "the approved page 4 of this episode, same corridor, as the reference for rendering quality, speech bubbles, caption boxes and lettering only (do not copy its panels or poses)"),
    6: ("E02_Hal04_final", "the approved page 4 of this episode, same corridor, as the reference for rendering quality, speech bubbles, caption boxes and lettering only (do not copy its panels or poses)"),
    7: ("E02_Hal04_final", "the approved page 4 of this episode, same corridor, as the reference for rendering quality, speech bubbles, caption boxes and lettering only (do not copy its panels or poses)"),
    8: ("E02_Hal04_final", "the approved page 4 of this episode, same corridor, as the reference for rendering quality, speech bubbles, caption boxes and lettering only (do not copy its panels or poses)"),
}
TEXT = {"GALA": GALA, "ETH": ETH, "INSTR3": INSTR3}
LOCTEXT = {"LAB": LAB, "CORR": CORR}

pages = []


def page(title, table, layout, chars, loc, lighting, panels, extra="", cover=False):
    sref = STYLE_BY_PAGE.get(len(pages))
    att = [SHEET[c] for c in chars] + [LOCSHEET[loc]] + ([sref] if sref else [])
    n = len(panels)
    opener = ("Create a NEW image: a single full-page comic book cover." if cover
              else f"Create a NEW image: a single comic page with {n} separate panels.")
    ref = ("Attached reference images, in order: " + "; ".join(f"{i+1}) {d}" for i, (_, d) in enumerate(att)) +
           ". Copy every character's design and the place's layout EXACTLY from these sheets; they override any description below. "
           "Do not draw the sheets themselves, their captions, labels or grey backgrounds on the page.")
    body = [opener, ref, STYLE, *[TEXT[c] for c in chars], LOCTEXT[loc], lighting]
    if extra:
        body.append(extra)
    if layout:
        body.append("Panel layout: " + layout + " Nothing crosses or breaks out of the panel borders; every image stays fully inside its own panel.")
    body += panels
    body.append(avoid(chars))
    pages.append((title, table, "\n".join(body), [a for a, _ in att]))


# ---------------- Cover
page("Sampul", "Gala di lorong tembak, tendangan api membelah proyektil plasma merah, HUD biru-hijau berpendar di kacamata, Ethylene di dekatnya. Judul di atas, nomor episode di bawah.",
 None, ["GALA", "ETH"], "CORR", "Lighting: dim corridor lit by the orange floor lights, red glow from the plasma, bright golden-orange firelight from Gala's kick.",
 ["Single full-page 3D render, a comic book cover: in the firing corridor, Gala mid-air in a spinning fire kick, an arc of golden-orange flame trailing from his right boot, slicing a red plasma sphere cleanly in half; thin blue and green HUD grid lines glow faintly on the glossy surface of his opaque goggle lenses; Ethylene hovers just behind his shoulder; the five cannons are small in the far background.",
  'Text at the top in large bold letters: "GALA IGNIS & THE GALIANS". Text at the bottom: "EPISODE 2: PEMETA MOLEKUL".'],
 cover=True)

# ---------------- Page 1: lab, chip
page("Halaman 1: Chip Pemindai", [
 ("1 (atas, lebar)", "Lab terang; Gala dan Ethylene masuk; Instruktur Ketiga di meja kerja", "Narasi: Laboratorium Teknologi Akademi. Sisa waktu: 19 jam."),
 ("2 (tengah kiri)", "Instruktur Ketiga menyodorkan chip kecil berukir batik", "Instruktur Ketiga: Chip pemindai molekul. Pasang di goggles-mu."),
 ("3 (tengah kanan)", "Close-up chip terpasang di bingkai goggles, garis cahaya di tepi lensa", "SFX: KLIK / Gala: Keren! Tapi... ini buat apa?"),
 ("4 (bawah, lebar)", "Instruktur Ketiga membetulkan kacamata, serius", "Instruktur Ketiga: Apimu meledak karena kamu tidak melihat apa yang kamu bakar.")],
 "exactly four rectangular panels. Top row: panel 1, full width. Middle row: panel 2 on the left and panel 3 on the right, side by side. Bottom row: panel 4, full width.",
 ["GALA", "ETH", "INSTR3"], "LAB", "Lighting: bright, clean white lab light with teal glows from the pedestals and cylinders.",
 ['Panel 1 (top, wide): establishing shot of the bright lab; Gala walks in through the sliding door with Ethylene hovering by his shoulder; the Third Instructor waits at the central workbench under the ring light. Caption box top-left: "Laboratorium Teknologi Akademi. Sisa waktu: 19 jam."',
  'Panel 2 (middle left): the Third Instructor holds out, between two fingers, a tiny square molecular-scanner chip engraved with gold batik lines toward Gala. Speech bubble from her: "Chip pemindai molekul. Pasang di goggles-mu."',
  'Panel 3 (middle right, close-up): the tiny chip snaps into the side of Gala\'s goggle frame, a thin line of blue light running around the rim of the lens; Gala grins; the lenses stay opaque and dark. Small sound effect: "KLIK". Speech bubble from Gala: "Keren! Tapi... ini buat apa?"',
  'Panel 4 (bottom, wide): the Third Instructor adjusts her round glasses with one finger, serious and calm, the lab softly out of focus behind her; no fire sprite in this panel. Speech bubble: "Apimu meledak karena kamu tidak melihat apa yang kamu bakar."'])

# ---------------- Page 2: overload
page("Halaman 2: Kebanjiran Data", [
 ("1 (atas, lebar)", "Sudut pandang dari balik goggles: kisi HUD menempel di seluruh lab", "Gala (luar panel): Wah... semuanya kelihatan sampai ke atomnya!"),
 ("2 (tengah kiri)", "Gala memegang kepala, limbung, aliran data di permukaan lensa", "Gala: Ugh... terlalu banyak... kepalaku..."),
 ("3 (tengah kanan)", "Dari belakang bahu: matriks atom hologram glitch merah", "SFX: BZZT! BZZT!"),
 ("4 (bawah, lebar)", "Instruktur Ketiga tenang, memegang tablet", "Instruktur Ketiga: Jangan lawan datanya. Pilih satu titik saja.")],
 "exactly four rectangular panels. Top row: panel 1, full width. Middle row: panel 2 on the left and panel 3 on the right, side by side. Bottom row: panel 4, full width.",
 ["GALA", "INSTR3"], "LAB", "Lighting: bright lab light, with blue-green HUD glow and flickers of red error light in panels 2 and 3.",
 ['Panel 1 (top, wide, first-person view through Gala\'s goggles): the whole bright lab seen through the goggle HUD, every pedestal, cylinder and wall tagged with glowing grid lines and small scan nodes; no characters visible except the Third Instructor small in the background. Speech bubble near the bottom edge, its tail pointing down off-panel, spoken by Gala who is off-panel: "Wah... semuanya kelihatan sampai ke atomnya!"',
  'Panel 2 (middle left, medium close-up): Gala clutches his head with one hand, swaying and dizzy; streams of blue and green data glow across the glossy surface of his opaque dark goggle lenses, his eyes stay hidden. Speech bubble: "Ugh... terlalu banyak... kepalaku..."',
  'Panel 3 (middle right, over-the-shoulder from behind Gala): in front of him, floating holographic atomic lattices flicker and glitch, streaked with red error bars. Jagged sound effect: "BZZT! BZZT!"',
  'Panel 4 (bottom, wide): the Third Instructor, calm, holds a small glowing tablet and looks toward Gala, who stands dizzy in the foreground seen from behind. Speech bubble from her: "Jangan lawan datanya. Pilih satu titik saja."'],
 HUD)

# ---------------- Page 3: Ethylene calms, focus lock
page("Halaman 3: Satu Titik", [
 ("1 (atas kiri)", "Ethylene di dekat telinga Gala, partikel emas hangat", "Ethylene: Pip..."),
 ("2 (atas kanan)", "Close-up Gala bernapas pelan, pantulan HUD tenang, senyum tipis", "Gala: Satu titik... oke."),
 ("3 (tengah, lebar)", "Sudut pandang goggles: crosshair mengunci boneka latihan hologram", "Kotak narasi: Kena."),
 ("4 (bawah, lebar)", "Gala kuda-kuda silat menghadap boneka hologram (tampak belakang sesuai sheet); Instruktur Ketiga dewasa, dua kali tinggi Gala", "Instruktur Ketiga: Bagus. Sekarang ujian sungguhan.")],
 "exactly four rectangular panels. Top row: panel 1 on the left and panel 2 on the right, side by side, equal size. Middle row: panel 3, full width. Bottom row: panel 4, full width.",
 ["GALA", "ETH", "INSTR3"], "LAB", "Lighting: bright lab light, warm golden particle glow from Ethylene in panel 1, calm blue HUD glow.",
 ['Panel 1 (top left, close-up): Ethylene hovers right beside Gala\'s ear, releasing soft warm golden particles that drift around his head. Small round speech bubble to the upper right, its tail pointing down to Ethylene (not to Gala): "Pip..."',
  'Panel 2 (top right, close-up): Gala breathes slowly, a small relieved smile; his lenses are fully opaque dark smoky glass with thin, faint horizontal lines of blue HUD light and a few small scan nodes reflected across the surface, spread unevenly and never forming round shapes in the lens centers, so nothing looks like eyes or pupils. Speech bubble: "Satu titik... oke."',
  'Panel 3 (middle, full width, first-person view through Gala\'s goggles): a translucent blue holographic training dummy standing on a lab pedestal, one clean golden crosshair locked on its chest, the rest of the HUD quiet and dim. Pale yellow caption box in the bottom-left corner (a caption box, not a speech bubble, because this is Gala\'s own point of view): "Kena."',
  'Panel 4 (bottom, full width): Gala seen in a three-quarter back view from behind his left side, facing the translucent blue holographic training dummy at the back center of the lab, in a low pencak silat stance aimed at it: front foot toward the dummy, knees bent, one fist forward, one fist guarding his chest. His back matches the back view on the Gala sheet EXACTLY: chibi proportions with a large head, big spiky hair with the goggle strap around the back of his head, a plain purple back plate with no engravings, the brown batik sash wrapped snugly at the waist (not a skirt), straight black pants, green boots with purple straps. Ethylene hovers by his shoulder. On the right side, roughly level with Gala, the Third Instructor stands at full adult scale: her figure spans almost the whole height of the panel, clearly about twice Gala\'s height, with adult body proportions and a small head; she lowers her tablet with a slight approving nod. Speech bubble from her, top right: "Bagus. Sekarang ujian sungguhan."'],
 HUD)

# ---------------- Page 4: corridor, cannons fire
page("Halaman 4: Lorong Tembak", [
 ("1 (atas, lebar)", "Lorong panjang; Gala di ujung dekat; lima meriam mengisi daya", "Narasi: Lorong Tembak Akademi. / Speaker: Lima meriam. Jangan meledakkan apa pun."),
 ("2 (tengah kiri)", "Close-up moncong meriam menyala merah", "SFX: WRRRM"),
 ("3 (tengah kanan)", "Gala menyeringai, Ethylene bersemangat", "Gala: Kali ini aku yang pegang kendali. / Ethylene: Pip!"),
 ("4 (bawah, lebar)", "Tiga proyektil plasma merah melesat bersamaan", "SFX: DZING! DZING! DZING!")],
 "exactly four rectangular panels. Top row: panel 1, full width. Middle row: panel 2 on the left and panel 3 on the right, side by side. Bottom row: panel 4, full width.",
 ["GALA", "ETH"], "CORR", "Lighting: dim corridor lit by the orange floor lights and the red glow of the charging cannons.",
 ['Panel 1 (top, wide): strong one-point perspective down the long corridor; Gala small at the near end with Ethylene beside him, the five cannons charging with red glows at the far wall. Caption box top-left: "Lorong Tembak Akademi." A speech bubble with a jagged electronic outline coming from a small wall speaker: "Lima meriam. Jangan meledakkan apa pun."',
  'Panel 2 (middle left, close-up): the dark barrels of the cannons, their muzzles glowing brighter red as they charge. Sound effect: "WRRRM"',
  'Panel 3 (middle right): Gala smirks confidently, one fist raised in front of his chest, goggles opaque; Ethylene bounces excitedly beside him. Speech bubble from Gala: "Kali ini aku yang pegang kendali." Small round speech bubble from Ethylene: "Pip!"',
  'Panel 4 (bottom, wide): three red glowing plasma spheres fire at the same moment from three of the cannons, streaking down the corridor toward the camera with motion-blur trails. Sound effect: "DZING! DZING! DZING!"'])

# ---------------- Page 5: HUD lock, charge, kick
page("Halaman 5: Titik Lemah", [
 ("1 (atas, lebar)", "Sudut pandang goggles: garis lintasan dan titik lemah emas di tiap proyektil", "Narasi: Titik lemahnya... di situ."),
 ("2 (tengah, lebar)", "Sudut rendah: plasma ke boots kanan, api membungkus kaki, kain sarung terhempas", "Gala: Api... ke kaki!"),
 ("3 (bawah, besar)", "Gala di udara, tendangan api berputar, busur api emas", "SFX: WHOOSH!")],
 "exactly three rectangular panels stacked vertically, each full width: panel 1 on top, panel 2 in the middle, panel 3 at the bottom and the largest.",
 ["GALA"], "CORR", "Lighting: dim corridor, orange floor lights, red plasma glow, then bright golden-orange firelight.",
 ['Panel 1 (top, first-person view through Gala\'s goggles): three red plasma spheres rushing toward the viewer down the corridor, thin predicted trajectory lines drawn ahead of each, one small golden weak-point dot locked on each sphere. Caption box: "Titik lemahnya... di situ."',
  'Panel 2 (middle, low angle): Gala plants his left foot and channels plasma into his right boot; golden-orange flames wrap around his right leg; his brown batik sash is blown backward by the heat. Speech bubble: "Api... ke kaki kanan!"',
  'Panel 3 (bottom, largest): Gala mid-air in a spinning fire kick, a wide arc of golden-orange flame trailing from his right boot across the corridor toward the three incoming red spheres, the flames reflected on his opaque goggle lenses. Big sound effect: "WHOOSH!"'],
 HUD)

# ---------------- Page 6: slice, landing
page("Halaman 6: Terbelah", [
 ("1 (atas, splash)", "Busur api membelah tiga proyektil tepat di titik lemahnya, tanpa ledakan", "SFX: SRAAAK!"),
 ("2 (bawah kiri)", "Sudut rendah: Gala mendarat tiga tumpuan, asap dari boots, belahan jadi percikan", ""),
 ("3 (bawah kanan)", "Gala menoleh ke belakang, heran", "Gala: ...Nggak meledak?")],
 "exactly three rectangular panels. Panel 1 fills the top two thirds of the page, full width. Bottom row: panel 2 on the left and panel 3 on the right, side by side.",
 ["GALA"], "CORR", "Lighting: golden sparks and firelight in the dim orange-lit corridor.",
 ['Panel 1 (top two thirds, splash): the arc of golden-orange flame from Gala\'s kick slices all three red plasma spheres cleanly in half at their golden weak points, showers of golden sparks spraying along each cut; there is NO explosion and NO fireball. Gala at the end of his spin. Huge sound effect: "SRAAAK!"',
  'Panel 2 (bottom left, low angle): Gala lands in a three-point landing, one fist on the floor, thin smoke curling from his right boot; behind him the six sphere halves dissolve harmlessly into drifting sparks.',
  'Panel 3 (bottom right): Gala looks back over his shoulder at the fading sparks, surprised, eyebrows raised above his opaque goggles. Speech bubble: "...Nggak meledak?"'])

# ---------------- Page 7: result
page("Halaman 7: 99,8 Persen", [
 ("1 (atas, lebar)", "Layar di atas pintu masuk: TARGET NEUTRALIZED - PRECISION: 99.8%", "SFX: DING!"),
 ("2 (tengah, lebar)", "Gala mengacungkan jempol ke Ethylene, layar di belakang", "Gala: 99,8 persen! Lihat itu, Ethylene! / Ethylene: Pip! Pip!"),
 ("3 (bawah, lebar)", "Instruktur Ketiga di pintu masuk, tangan bersilang, senyum tipis", "Instruktur Ketiga: Tidak buruk, Taruna. Tapi panasmu masih bocor.")],
 "exactly three rectangular panels stacked vertically, each full width: panel 1 on top, panel 2 in the middle, panel 3 at the bottom.",
 ["GALA", "ETH", "INSTR3"], "CORR", "Lighting: dim orange-lit corridor, bright green glow from the display screen.",
 ['Panel 1 (top, wide): the wide wall display screen above the hazard-striped entrance door lights up green with the text "TARGET NEUTRALIZED - PRECISION: 99.8%". Sound effect: "DING!"',
  'Panel 2 (middle, wide): Gala grins and gives a big thumbs-up to Ethylene, who bounces happily in the air in front of him; the glowing green screen above the door behind them. Speech bubble from Gala: "99,8 persen! Lihat itu, Ethylene!" Small round speech bubble from Ethylene: "Pip! Pip!"',
  'Panel 3 (bottom, wide): the entrance door is open; the Third Instructor stands in the doorway with her arms crossed and a small approving smile, pointing her chin at the thin smoke still rising from Gala\'s boot and sash. Speech bubble from her: "Tidak buruk, Taruna. Tapi panasmu masih bocor."'])

# ---------------- Page 8: end
page("Halaman 8: Panas yang Tersisa", [
 ("1 (atas, 2/3)", "Gala menatap kain sarung batiknya yang berasap tipis dan berpendar samar", "Narasi: Sisa waktu: 14 jam."),
 ("2 (strip bawah)", "Kartu penutup: kain batik cokelat berpendar", "Narasi: Bagaimana menjinakkan panas yang tersisa? / BERSAMBUNG / Episode 3: Nanoselulosa Penyeimbang")],
 "exactly two rectangular panels. Panel 1 fills the top two thirds of the page, full width. Panel 2 is a full-width strip across the bottom third.",
 ["GALA", "ETH"], "CORR", "Lighting: dim corridor, warm glow from the sash and from Ethylene.",
 ['Panel 1 (top two thirds): Gala stands alone in the corridor holding up the end of his brown batik sash in one hand, looking down at it; thin smoke rises from the fabric and its batik lines glow faintly orange; Ethylene hovers beside his shoulder looking at it too. Caption box: "Sisa waktu: 14 jam."',
  'Panel 2 (bottom strip): a dark end-card panel showing only a small folded piece of brown batik cloth with faintly glowing orange batik lines. Caption box: "Bagaimana menjinakkan panas yang tersisa?" Large bold text: "BERSAMBUNG". Smaller text: "Episode 3: Nanoselulosa Penyeimbang"'])


out = ["""# Komik Episode 2: Pemeta Molekul

*Gala Ignis & The Galians · Season 1 · Adaptasi komik dari storyboard 2A.1a sampai 2B.2d*

Sampul + 8 halaman · 28 panel · potret 2:3 · satu prompt per halaman, teks sudah di dalamnya

## Keputusan cerita

| Keputusan | Alasan |
|---|---|
| Teknisi di 2A.1a diganti **Instruktur Ketiga** | Dia yang penasaran dengan Ethylene di Episode 1; tidak perlu sheet karakter baru. Bible frame 2A.1a sudah diperbarui |
| Hitung mundur 24 jam dilanjutkan ("Sisa waktu: 19 jam" lalu "14 jam") | Menyambung ultimatum Episode 1 |
| Tendangan api memotong **ketiga** proyektil | Storyboard menembakkan tiga proyektil tapi hanya memotong satu |
| Dialog \"Api... ke kaki kanan!\" diringkas jadi \"Api... ke kaki!\" | Gemini berulang kali menaruh api di kaki kiri; sisi kaki tidak penting bagi cerita |
| Ethylene menyatu ke api tendangan (Hal. 5 \"Pip!\" dari dalam api) lalu muncul lagi dari asap sepatu (Hal. 6 panel 4) | Ethylene hilang di Hal. 5 sampai 6 padahal ada di Hal. 4 dan 7; ini menjelaskan ke mana dia pergi |
| Penutup mengarah ke kain sarung yang berasap | Menyiapkan Episode 3 (Nanoselulosa Penyeimbang) |

## Pelajaran dari Episode 1 yang sudah masuk ke setiap prompt

- Tata letak panel ditulis eksplisit per baris, dan tidak ada gambar yang boleh menembus batas panel.
- Kacamata Gala ditulis "fully opaque dark lenses" dan Ethylene "no mouth" di setiap halaman.
- Hanya Instruktur Ketiga yang boleh muncul; dua instruktur lain dilarang tegas.
- Tokoh yang berbicara dari luar panel diberi ekor balon "pointing off-panel".
- Tidak ada efek rumit seperti pantulan wajah; sudut pandang HUD digambarkan dengan aturan tetap (garis kisi, titik pindai, tanpa teks).
- Gala Episode 2 masih versi v1: tanpa pin di dada.

## Cara pakai

1. Siapkan file: K01_final, K03_final, K30, L02_final, L03_final. Acuan gaya diambil dari halaman Episode 2 yang sudah lolos di lokasi yang sama (E02_Sampul_final, E02_Hal01_final, E02_Hal04_final), karena acuan dari lokasi lain membuat Gemini menyalin ruangannya.
2. **Buka chat Gemini baru untuk setiap halaman**, lampirkan file di bagian *Lampirkan* sesuai urutan, lalu tempel prompt-nya.
3. Panel meleset: balas di chat yang sama dengan halaman itu terlampir: *"Edit this image. Fix only panel N: ... Keep all other panels identical."*

---
"""]
for title, table, prompt, att in pages:
    out.append(f"## {title}\n")
    out.append("**Lampirkan:** " + ", ".join(att) + "\n")
    if isinstance(table, str):
        out.append(table + "\n")
    else:
        out.append("| Panel | Visual | Teks |\n|---|---|---|")
        for p, v, t in table:
            out.append(f"| {p} | {v} | {t} |")
        out.append("")
    out.append("```text\n" + prompt + "\n```\n\n---\n")
open("/home/claude/gala-ignis/komik-episode-02.md", "w").write("\n".join(out))
print(len(pages), sum(len(t) if not isinstance(t, str) else 1 for _, t, _, _ in pages))

# --- page-specific Avoid additions (Halaman 3 revision, 24 Sep)
_p = '/home/claude/gala-ignis/komik-episode-02.md'
_s = open(_p).read(); _a = _s.index('## Halaman 3'); _b = _s.index('## Halaman 4')
_sec = _s[_a:_b]
if 'childlike instructor' not in _sec:
    _sec = _sec.replace('Avoid: goggles pushed up', "Avoid: a small or childlike instructor, chibi proportions on the instructor, adult or teenage proportions on Gala, a skirt or flared cloth at Gala's waist, engravings on Gala's back plate, a character sheet or turnaround drawn inside any panel, goggles pushed up", 1)
    open(_p, 'w').write(_s[:_a] + _sec + _s[_b:])

# --- Halaman 4+ switched to per-panel method (24 Sep): replace page section with per-panel prompts
import sys; sys.path.insert(0, '/home/claude/komik')
from panels_ep2 import PAGES as _PP
_s = open(_p).read()
for _n, _pg in _PP.items():
    _a = _s.index(f'## Halaman {_n}'); _b = _s.index('## Halaman', _a + 5) if f'## Halaman {_n+1}' in _s else len(_s)
    _old = _s[_a:_b]
    _tbl = _old[:_old.index('```text')] if '```text' in _old else _old
    _tbl = _tbl.split('**Lampirkan:**')[0]
    _out = _tbl + "**Metode:** satu gambar per panel, tanpa teks. Balon, narasi dan SFX ditulis lokal saat menyusun halaman.\n\n"
    for _i, _pn in enumerate(_pg['panels'], 1):
        _out += f"### Panel {_i}\n\n**Lampirkan:** {', '.join(_pn['files'])}\n\n```text\n{_pn['prompt']}\n```\n\n"
    _s = _s[:_a] + _out + "---\n\n" + _s[_b:]
open(_p, 'w').write(_s)
