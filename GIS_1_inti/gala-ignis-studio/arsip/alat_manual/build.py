REF = ("Use the attached reference images: the character sheet for the exact design of every character, the Arena 7 sheet for the "
       "exact room, and, if attached, the style reference page for the exact 3D rendering style. Match them precisely; do not redesign anything.")
STYLE = ("Rendering style, identical in every panel and on every page: 3D CGI render, like still frames taken from a modern 3D animated "
         "feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Every panel is a "
         "3D rendered image. The only 2D elements on the page are the panel borders, speech bubbles, caption boxes and lettering, overlaid "
         "on top of the renders. Page layout: 2:3 portrait, thin black panel borders, white gutters. Lettering: white speech bubbles with "
         "thin black outlines and tails pointing to the speaker, pale yellow caption boxes with black text, bold clean comic font. Render "
         "every text exactly as written, in Indonesian, with correct spelling.")
GALA = ("Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; "
        "dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes; his eyes are never visible through the lenses, even in close-ups; fitted green tactical shirt; purple armor plates with gold "
        "batik engravings on chest, shoulders and forearms; green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; "
        "black pants; green-and-purple combat boots.")
ETH = ("Ethylene: a fist-sized fire sprite, a perfectly round glossy glowing amber orb with a small flickering flame crown on top, two small flame wisps on its sides like tiny wings and a thin flame tail, "
       "two simple glowing white dot eyes, no mouth, no limbs.")
INSTR = ("The three instructors, adult proportions, about twice Gala's height, all in identical dark navy sci-fi uniforms with thin gold trim: "
         "Lead Instructor, tall stern man, grey buzz cut, sharp jaw; Second Instructor, stocky man, thick black mustache; Third Instructor, "
         "woman, short black bob, round glasses.")
ARENA = ("Setting, Arena 7, the same room on every page: a large hexagonal training hall; walls of dark gunmetal hexagon panels; two "
         "horizontal cyan-blue neon strips running around the walls, one at waist height and one near the ceiling; a polished dark floor "
         "with a large faint glowing hexagon emblem at the center; one wide blast door with yellow-and-black hazard stripes on the left wall; "
         "a tinted observation window high on the back wall.")
AFTER = ("The room after the explosion: scorched black marks spreading from the center emblem, thin drifting smoke, one ceiling panel "
         "cracked open, the neon strips flickering dim blue.")
AVOID = ("Avoid: goggles pushed up or removed, Gala's eyes visible, helmets, capes, masks, extra accessories, changed hair or armor colors, "
         "a different room design, extra limbs, distorted hands, misspelled text, 2D illustration, drawn line art, ink outlines on characters, "
         "anime or manga style, cel shading, flat colors, sketch, watercolor, screentone.")

pages = []


SHEETS = {"GALA": ("K01_final", "the Gala character sheet"), "ETH": ("K03_final", "the Ethylene sheet"),
          "INSTR": ("K30", "the three instructors sheet")}

def attach_list(chars):
    keys = [k for k, v in (("GALA", GALA), ("ETH", ETH), ("INSTR", INSTR)) if v in chars]
    return [SHEETS[k] for k in keys] + [("L01_final", "the Arena 7 environment sheet")]

PAGE1 = ("Hal01_final", "the approved page 1 of this comic, as the reference for rendering quality, lighting, panel borders, speech bubbles, caption boxes and lettering style only (do not copy its panels or poses)")
PAGE3 = ("Hal03_final", "the approved page 3 of this comic, as the reference for rendering quality, speech bubbles, caption boxes, lettering style and the exact look of the cracked ceiling panels only (do not copy its panels or poses)")
PAGE4 = ("Hal04_final", "the approved page 4 of this comic, as the reference for rendering quality, speech bubbles, lettering style, how Gala and Ethylene look together, and the aftermath state of the room only (do not copy its panels or poses)")
PAGE5 = ("Hal05_final", "the approved page 5 of this comic, as the reference for rendering quality, speech bubbles, caption boxes, lettering style, the look of the instructors in a scene and the aftermath state of the room only (do not copy its panels or poses)")
COVER = ("Sampul_final", "the approved cover of this comic, as the reference for rendering quality, lighting and lettering style only (do not copy its pose or layout)")

def page(title, table, n_panels, chars, lighting, panels, extra=""):
    style_ref = [] if n_panels == 1 else ([COVER] if len(pages) == 1 else ([PAGE1] if len(pages) <= 3 else ([PAGE3] if len(pages) <= 5 else ([PAGE5] if len(pages) == 6 else [PAGE4]))))
    att = attach_list(chars) + style_ref
    ref = ("Attached reference images, in order: " + "; ".join(f"{i+1}) {d}" for i, (_, d) in enumerate(att)) +
           ". Copy every character's design and the room's layout EXACTLY from these sheets; they override any description below. "
           "Do not draw the sheets themselves, their captions, labels or grey backgrounds on the page.")
    opener = "Create a NEW image: a single full-page comic book cover." if n_panels == 1 else f"Create a NEW image: a single comic page with {n_panels} separate panels."
    body = [opener, ref, STYLE, *chars, ARENA, lighting]
    if extra:
        body.append(extra)
    body += panels
    body.append(AVOID)
    pages.append((title, table, "\n".join(body), [a for a, _ in att]))


page("Sampul", "Gala dalam kuda-kuda silat di tengah Arena 7, api di gauntlet, Ethylene di bahunya. Judul di atas, nomor episode di bawah.",
 1, [GALA, ETH], "Lighting: cool cyan-blue neon behind, warm orange firelight in front.",
 ["Single full-page 3D render, a comic book cover: Gala in a low pencak silat stance on the center hexagon emblem, orange-gold flames swirling around his gauntlets, the gold batik on his armor glowing; Ethylene hovers beside his right shoulder.",
  'Text at the top in large bold letters: "GALA IGNIS & THE GALIANS". Text at the bottom: "EPISODE 1: PERCIKAN PERTAMA DI AWAL ERA".'])

page("Halaman 1: Arena Tujuh", [
 ("1 (lebar, setengah atas)", "Arena kosong, tenang", "Narasi: Akademi Galians. Arena 7. Pukul 05.12."),
 ("2 (tengah kiri)", "Gala berdiri santai di atas emblem", "Gala: Oke, Arena 7. Hari ini kita akur, ya."),
 ("3 (tengah kanan)", "Kuda-kuda silat, sudut rendah", "Narasi: Gala Ignis. Taruna tahun pertama. Tiga kali gagal. / Gala: Tarik napas..."),
 ("4 (strip bawah)", "Close-up batik dada berpijar", "SFX: VWMMM...")],
 4, [GALA], "Lighting: calm cool cyan-blue neon, quiet early morning mood.",
 ['Panel 1 (wide, top half): the empty Arena 7 seen from a high corner, calm. Caption box top-left: "Akademi Galians. Arena 7. Pukul 05.12."',
  'Panel 2 (middle left): Gala stands relaxed on the center hexagon emblem, full body visible, confident grin. Speech bubble: "Oke, Arena 7. Hari ini kita akur, ya."',
  'Panel 3 (middle right): low angle, Gala in a pencak silat stance, knees bent, fists chambered at his waist, the hazard-striped blast door visible behind him. Caption box: "Gala Ignis. Taruna tahun pertama. Tiga kali gagal." Speech bubble: "Tarik napas..."',
  'Panel 4 (bottom strip): extreme close-up of Gala\'s chest plate, the gold batik engravings starting to glow orange, tiny sparks on his gauntlets. Sound effect in glowing orange letters: "VWMMM..."'])

page("Halaman 2: Lonjakan", [
 ("1 (lebar)", "Neon berubah merah, alarm", "SFX: WIIIUU! / Layar: LONJAKAN PLASMA 240%"),
 ("2 (close-up)", "Wajah panik Gala", "Gala: Eh? Eh, tunggu dulu!"),
 ("3", "Batik dan kain sarung berpijar menahan panas", "Gala: Kain sarung, tahan...!"),
 ("4 (besar)", "Gala menahan bola plasma raksasa", "Gala: Jangan meledak...!")],
 4, [GALA], "Lighting: the cyan-blue neon strips have switched to flashing red alarm light; red light sweeps across the hexagon panels.",
 ['Panel 1 (wide, top): the same arena bathed in flashing red, a red holographic warning floating in the air reading "LONJAKAN PLASMA 240%". Sound effect in red jagged letters: "WIIIUU!"',
  'Panel 2 (middle left, close-up): Gala\'s face in panic, eyebrows raised high above the goggles, mouth wide open, red and orange light reflected on the lenses. Speech bubble: "Eh? Eh, tunggu dulu!"',
  'Panel 3 (middle right): Gala straining, heat haze around him, the gold batik on his armor and his brown sash glowing bright. Speech bubble: "Kain sarung, tahan...!"',
  'Panel 4 (bottom, large): low angle, Gala crossing both forearms in front of his chest as a huge unstable orange-gold plasma orb swells before him above the center emblem. Shaky speech bubble: "Jangan meledak...!"'])

page("Halaman 3: Ledakan", [
 ("1 (splash, 2/3 atas)", "Ledakan memenuhi arena, atap retak", "SFX: BLAAARRR!!"),
 ("2 (kiri bawah)", "Gala bertahan dengan siku", "Gala: Nggh...!"),
 ("3 (kanan bawah)", "Partikel api berkumpul di satu titik", "Narasi: Di tengah api itu, sesuatu... berkumpul.")],
 3, [GALA], "Lighting: blinding orange-gold explosion light, then smoke.",
 ['Panel 1 (splash, top two thirds): the plasma orb detonates at the center emblem, a golden-orange shockwave filling Arena 7, one ceiling panel cracking open from the blast, Gala a small silhouette at the center. Huge fiery sound effect: "BLAAARRR!!"',
  'Panel 2 (bottom left): Gala in an elbow-guard stance inside the blast wind, shirt and brown sash whipping, hair pushed back. Speech bubble: "Nggh...!"',
  'Panel 3 (bottom right, macro): glowing fire particles spiraling into a single point inside the smoke. Caption box: "Di tengah api itu, sesuatu... berkumpul."'])

page("Halaman 4: Pip?", [
 ("1 (makro)", "Ethylene terbentuk", "SFX: fwsh..."),
 ("2 (lebar)", "Gala menengadah takjub", "Gala: ...Kamu siapa?"),
 ("3 (close-up)", "Ethylene memiringkan badan", "Ethylene: Pip?"),
 ("4", "Gala nyengir lemah, berjelaga", "Gala: Ledakanku... punya mata?")],
 4, [GALA, ETH], "Lighting: dim flickering blue neon, soft warm glow from Ethylene.",
 ['Panel 1 (top, macro): the spiraling particles condense into Ethylene, glowing softly as it is born. Small gold sound effect: "fwsh..."',
  'Panel 2 (middle, wide): smoke thinning around the scorched center emblem; Gala lowers his arms and tilts his head up in exhausted wonder at Ethylene hovering by his shoulder. Speech bubble: "...Kamu siapa?"',
  'Panel 3 (bottom left, close-up): Ethylene tilts to one side, its white dot eyes blinking. Small round speech bubble: "Pip?"',
  'Panel 4 (bottom right): Gala\'s tired lopsided grin, messy hair, soot on his cheek, Ethylene near his face. Speech bubble: "Ledakanku... punya mata?"'],
 AFTER)

page("Halaman 5: Para Instruktur", [
 ("1 (lebar)", "Pintu hazard terbuka, asap keluar", "SFX: KSSSHHH"),
 ("2 (lebar)", "Tiga instruktur masuk", "Instruktur Utama: Taruna Gala Ignis."),
 ("3", "Gala canggung, Ethylene sembunyi di bahu", "Gala: Ini... tidak seperti kelihatannya. / Instruktur Kedua: Kamu meledakkan arena."),
 ("4 (close-up)", "Instruktur Ketiga membetulkan kacamata", "Instruktur Ketiga: Itu apa di bahumu?")],
 4, [GALA, ETH, INSTR], "Lighting: dim flickering blue neon, bright white light pouring in from the open blast door.",
 ['Panel 1 (wide, top): the hazard-striped blast door on the left wall slides open, dense white smoke pouring out into a bright corridor. Sound effect: "KSSSHHH"',
  'Panel 2 (upper middle, wide): the three instructors stride through the smoke into Arena 7 from the open, brightly lit blast door on the left, stern faces, the Lead Instructor in front. Speech bubble from the Lead Instructor: "Taruna Gala Ignis."',
  'Panel 3 (lower middle): Gala stands guiltily on the scorched center emblem, soot on his shirt, the edge of his sash singed, rubbing the back of his head; Ethylene peeks from behind his shoulder. Speech bubble from Gala: "Ini... tidak seperti kelihatannya." A second speech bubble near the left edge, its tail pointing off-panel to the left, spoken by the Second Instructor who is out of frame: "Kamu meledakkan arena."',
  'Panel 4 (bottom, close-up): the Third Instructor, alone in this panel, adjusts her round glasses and looks off-panel to the left toward Gala with a sharp, curious expression; Ethylene is NOT in this panel and nothing sits on her shoulder. Speech bubble: "Itu apa di bahumu?"'],
 AFTER + " The hazard-striped blast door on the left wall is open.")

page("Halaman 6: Dua Puluh Empat Jam", [
 ("1 (kiri atas)", "Instruktur Utama mengangkat tablet merah", "Instruktur Utama: Tiga kali gagal. Satu arena hancur."),
 ("2 (kanan atas)", "Close-up layar tablet di tangan instruktur", "Tablet: 24 JAM TERSISA / Instruktur Utama: Kendalikan apimu, atau keluar."),
 ("3 (tengah, lebar)", "Gala kaget total, tangan di kepala", "Gala: DUA PULUH EMPAT JAM?!"),
 ("4 (bawah, lebar)", "Dari belakang Gala: instruktur pergi lewat pintu, Ethylene menempel di pipi Gala", "Narasi: Hitung mundur dimulai.")],
 4, [GALA, ETH, INSTR], "Lighting: dim flickering blue neon mixed with red light from a holographic tablet.",
 ['Panel layout: exactly four rectangular panels. Top row: panel 1 on the left and panel 2 on the right, side by side, equal size. Middle row: panel 3, full width. Bottom row: panel 4, full width. Nothing crosses or breaks out of the panel borders; every image stays fully inside its own panel.',
  'Panel 1 (top left): the Lead Instructor, alone in this panel, holds up a glowing red holographic tablet in one hand, cold stern expression; no fire sprite in this panel. Speech bubble: "Tiga kali gagal. Satu arena hancur."',
  'Panel 2 (top right, close-up): only the red holographic tablet held in the Lead Instructor\'s gloved hand, its screen facing the viewer and reading "24 JAM TERSISA" in big clear letters; no faces and no reflections on the screen, no fire sprite in this panel. Speech bubble with its tail pointing off-panel to the left, spoken by the Lead Instructor: "Kendalikan apimu, atau keluar."',
  'Panel 3 (middle, full width): Gala in total shock, both hands clutching the sides of his head, eyebrows shot up very high above the goggles, mouth wide open in a big yell, hair standing up; the goggle lenses stay fully opaque and dark. Ethylene beside him, startled, its flame wisps flared up. Big jagged speech bubble: "DUA PULUH EMPAT JAM?!"',
  'Panel 4 (bottom, full width): camera behind Gala. Gala in the foreground on the right, seen from behind at a three-quarter angle, shoulders slumped; Ethylene presses gently against his cheek. In the background, the three instructors walk AWAY from the camera, their backs turned to us, leaving through the open blast door on the left wall into the bright corridor. Caption box: "Hitung mundur dimulai."'],
 AFTER + " The hazard-striped blast door on the left wall is open.")

page("Halaman 7: Nama", [
 ("1 (lebar)", "Gala duduk sendirian di lantai hangus", "Gala: Hari pertama yang hebat, Gala."),
 ("2", "Ethylene hinggap di telapak tangan", "Ethylene: Pip."),
 ("3 (close-up)", "Gala tersenyum pada Ethylene", "Gala: Lahir dari reaksi gagal... Namamu Ethylene."),
 ("4", "Ethylene melompat kecil, menyala terang", "Ethylene: Pip!")],
 4, [GALA, ETH], "Lighting: first pale dawn light falling through the cracked ceiling panel onto the center emblem, neon strips dim.",
 ['Panel layout: exactly four rectangular panels. Top row: panel 1, full width. Middle row: panel 2 on the left and panel 3 on the right, side by side. Bottom row: panel 4, full width. Nothing crosses or breaks out of the panel borders.',
  'Panel 1 (top, wide): the instructors are gone; Gala sits on the scorched center emblem, leaning back on his hands, shoulders slumped, soot on his shirt; Ethylene hovers quietly a little above him. Speech bubble: "Hari pertama yang hebat, Gala."',
  'Panel 2 (middle left): Ethylene drifts down slowly and settles into Gala\'s open palm. Small round speech bubble: "Pip."',
  'Panel 3 (middle right, close-up): Gala smiles softly at Ethylene, its warm glow lighting his face; only a small warm highlight shines on the glossy surface of his fully opaque dark lenses, his eyes stay hidden. Speech bubble: "Lahir dari reaksi gagal... Namamu Ethylene."',
  'Panel 4 (bottom): Ethylene flares brighter and does a tiny happy hop in his palm, sparks around it. Small round speech bubble: "Pip!"'],
 AFTER)

page("Halaman 8: Awal Sebuah Era", [
 ("1 (lebar, 2/3 atas)", "Fajar menembus atap retak; Gala berdiri, Ethylene di atas telapak", "Narasi: Hari itu bukan hanya awal seorang taruna."),
 ("2 (strip bawah)", "Kartu penutup, pratinjau chip batik", "Narasi: Hari itu adalah awal sebuah era. / BERSAMBUNG / Episode 2: Pemeta Molekul")],
 2, [GALA, ETH], "Lighting: golden dawn beams through the cracked ceiling panel, dust motes floating.",
 ['Panel layout: exactly two rectangular panels. Panel 1 fills the top two thirds of the page, full width. Panel 2 is a full-width strip across the bottom third. Nothing crosses the panel borders.',
  'Panel 1 (top two thirds, wide): Gala stands on the center emblem seen from behind at a slight angle, one hand raised with Ethylene glowing above his palm, dawn light pouring down on them. Caption box: "Hari itu bukan hanya awal seorang taruna."',
  'Panel 2 (bottom strip): a dark end-card panel with a small glowing image of a tiny scanner chip engraved with batik lines. Caption box: "Hari itu adalah awal sebuah era." Large bold text: "BERSAMBUNG". Smaller text: "Episode 2: Pemeta Molekul"'],
 AFTER)

REF_CHAR = ("Create a character reference sheet on a plain light grey background, 3D CGI render like a modern 3D animated feature film, rounded stylized 3D shapes, soft realistic materials, soft even studio lighting, no drawn line art, "
 "no text except name labels.\n" + GALA + " Show Gala in front view, three-quarter view and back view, full body, plus three head close-ups: "
 "confident grin, panic with raised eyebrows and open mouth, soft smile. Expressions only through eyebrows and mouth; the goggles always stay on.\n"
 + ETH + " Show Ethylene front view and floating next to Gala's shoulder for scale.\n" + INSTR + " Show all three standing side by side, full body, "
 "next to Gala for height comparison.\nLabel each figure with its name in small clean letters: \"GALA\", \"ETHYLENE\", \"INSTRUKTUR UTAMA\", "
 "\"INSTRUKTUR KEDUA\", \"INSTRUKTUR KETIGA\".\n" + AVOID)
REF_ROOM = ("Create an environment reference sheet, 3D CGI render like a modern 3D animated feature film, soft realistic materials, volumetric lighting, no drawn line art, no characters, no text.\n" + ARENA +
 "\nShow the room in three views: a wide shot from a high corner, a straight-on view of the left wall with the hazard-striped blast door, "
 "and a view toward the back wall with the observation window. Cool cyan-blue neon lighting, clean and empty.")

out = ["""# Komik Episode 1: Percikan Pertama di Awal Era (v4)

*Gala Ignis & The Galians · Season 1 · Adaptasi komik dari storyboard 1A.1a sampai 1B.2d*

Sampul + 8 halaman · 29 panel · potret 2:3 · satu prompt per halaman, teks sudah di dalamnya

## Yang Berubah dari v3

| Perubahan | Alasan |
|---|---|
| Referensi A dan B dihapus; setiap halaman kini melampirkan **sheet final** (K01_final, K03_final, K30, L01_final) | Sheet final sudah lolos review satu per satu, jadi jauh lebih andal daripada sheet gabungan buatan sekali jalan |
| Tiap halaman punya daftar **Lampirkan** sendiri | Hanya sheet tokoh yang muncul di halaman itu yang dilampirkan; lampiran lebih sedikit, perhatian Gemini lebih fokus |
| Prompt dibuka dengan "Create a NEW image" | Pelajaran dari L04: tanpa kalimat ini Gemini kadang mengembalikan gambar lampiran apa adanya |
| Larangan menggambar sheet itu sendiri | Mencegah caption, label, atau latar abu-abu sheet ikut muncul di halaman komik |
| Desain Ethylene diperbarui | Mengikuti K03_final: bola kuning keemasan mengilap bermahkota api, tanpa mulut |

## Cara Pakai

1. **Siapkan delapan file:** K01_final, K03_final, K30, L01_final, Sampul_final (acuan gaya untuk Halaman 1), Hal01_final (acuan gaya, balon, dan huruf untuk Halaman 2-3), Hal03_final (acuan yang sama plus bentuk langit-langit retak untuk Halaman 4-5), Hal05_final (untuk Halaman 6), dan Hal04_final (untuk Halaman 7-8, karena tanpa instruktur).
2. **Buka chat Gemini baru untuk tiap halaman**, lalu lampirkan sheet yang tercantum di bagian **Lampirkan** halaman itu dan tempel prompt-nya. Chat baru mencegah Gemini masuk mode edit dari halaman sebelumnya.
3. **Kalau satu panel meleset,** balas di chat yang sama dengan halaman itu terlampir: *"Edit this image. Fix only panel 3: ... Keep all other panels identical."*
4. **Kalau satu halaman keluar 2D,** lampirkan halaman itu bersama L01_final, lalu kirim: *"Re-render this page in exactly the 3D CGI style of the second image. Keep the panel layout, poses and all text."*

**Batas yang perlu diketahui:** tidak ada model gambar yang menjamin karakter 100% identik di setiap generasi. Dengan sheet terlampir hasilnya jauh lebih stabil, tapi detail kecil seperti jumlah garis batik masih bisa bergeser [High confidence]. Kalau halaman empat panel terus meleset, jalan cadangannya: buat tiap panel sebagai gambar terpisah dengan lampiran yang sama, lalu susun di Canva.

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
out.append("""## Catatan

- **Nama Ethylene** diberikan Gala di halaman 7 ("lahir dari reaksi gagal"). Ini tambahan dari versi komik yang belum tercatat di bible.
- **Tiga instruktur** memakai sheet K30. Instruktur Utama adalah yang berambut cepak abu-abu.
- **Kalau Gemini hanya memberi satu gambar tanpa panel,** tambahkan di awal prompt: *"This must be a single image laid out as a comic page with separate panels."*
""")
open("/home/claude/gala-ignis/komik-episode-01.md", "w").write("\n".join(out))
print(len(pages))
