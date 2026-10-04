# Video Episode 1 dengan Veo (image-to-video)

*Gala Ignis & The Galians · 8 adegan kunci dari komik Episode 1 · format vertikal 9:16*

## Alur kerja per adegan

1. **Gambar kunci.** Buka chat Gemini baru, lampirkan file di bagian *Lampirkan*, tempel **Prompt gambar kunci**. Cek: tanpa teks, tanpa balon, desain tokoh cocok dengan sheet, kacamata Gala gelap total, Ethylene tanpa mulut. Simpan sebagai `S1_key.png` dan seterusnya.
2. **Video.** Di Gemini, pilih pembuatan video (Veo), unggah gambar kunci sebagai gambar awal, tempel **Prompt video**. Simpan sebagai `S1.mp4` dan seterusnya.
3. **Kirim semua klip ke sini.** Saya satukan jadi satu short: dipotong, diberi subtitle dialog, efek suara, dan kartu judul.

## Keputusan yang sudah saya ambil

| Keputusan | Alasan |
|---|---|
| Gambar kunci dibuat ulang, bukan memakai panel komik | Balon dan teks di panel akan ikut bergerak dan meleleh di video. Panel komik hanya dipakai sebagai acuan komposisi |
| Veo diminta **tanpa dialog dan tanpa musik** | Tiap klip Veo menghasilkan suara karakter yang berbeda-beda, dan dukungan bahasa Indonesianya belum pasti [Low confidence]. Dialog masuk sebagai subtitle saat penyuntingan, supaya konsisten |
| Satu adegan satu klip, tanpa perpindahan kamera di dalam klip | Klip pendek dengan satu gerakan kamera paling jarang merusak desain tokoh |
| Deskripsi tokoh diulang di setiap prompt | Veo tidak mengingat klip sebelumnya |

## Batas yang perlu diketahui

- Panjang klip Veo, rasio 9:16, dan kuota harian bergantung pada paket Gemini Anda dan bisa berubah. **Ini perlu dicek langsung di aplikasi** [Medium confidence]. Kalau 9:16 tidak tersedia, buat 16:9 dan saya potong ke tengah saat penyuntingan (sisi kiri-kanan akan hilang).
- Video AI masih sering mengubah detail kecil di tengah klip, seperti jumlah garis batik atau bentuk sepatu [High confidence]. Kalau desain berubah drastis, ulangi klipnya; kalau hanya sedikit, biasanya tidak terlihat di layar ponsel.

---

## Adegan 1: Tarik Napas

**Acuan komposisi:** Hal01_final (panel 3)  
**Lampirkan untuk gambar kunci:** K01_final, L01_final, Hal01_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes, his eyes never visible; fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. The moment: Early morning, calm cool cyan-blue neon light. Low angle: Gala in a pencak silat stance on the center hexagon emblem, knees bent, fists chambered at his waist, the hazard-striped blast door behind him. The gold batik engravings on his chest plate have just started to glow faint orange. Avoid: text, letters, speech bubbles, panel borders, goggles removed, Gala's eyes visible, any fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S1_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. Slow push-in from low angle toward Gala. He inhales deeply, his shoulders rising and settling; the gold batik lines on his chest plate brighten from faint orange to glowing gold, tiny sparks crackling around his gauntlets. His brown sash stirs slightly. Sound: a low electric hum building, soft crackle of sparks, calm room ambience. Keep every character's design exactly as in the starting image throughout the whole clip: Gala's goggles stay on with fully opaque dark lenses and his eyes are never visible. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---

## Adegan 2: Lonjakan

**Acuan komposisi:** Hal02_final (panel 4)  
**Lampirkan untuk gambar kunci:** K01_final, L01_final, Hal02_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes, his eyes never visible; fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. The moment: The arena's neon strips glow flashing red alarm light, red light sweeping across the hexagon panels. Low angle: Gala crosses both forearms in front of his chest, straining, as a huge unstable orange-gold plasma orb swells behind and around him above the center emblem. Avoid: text, letters, speech bubbles, panel borders, goggles removed, Gala's eyes visible, any fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S2_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. The red alarm lights pulse. The plasma orb grows bigger and more unstable, crackling and wobbling; Gala slides back half a step, bracing, gritting his teeth, his sash whipping in the heat. Camera shakes slightly as the orb flares brighter and brighter until the frame nearly whites out at the end. Sound: alarm siren wail, rising roaring hum of plasma, crackling energy. Keep every character's design exactly as in the starting image throughout the whole clip: Gala's goggles stay on with fully opaque dark lenses and his eyes are never visible. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---

## Adegan 3: Ledakan

**Acuan komposisi:** Hal03_final (panel 1)  
**Lampirkan untuk gambar kunci:** K01_final, L01_final, Hal03_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes, his eyes never visible; fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. The moment: Wide shot of Arena 7 at the instant of a huge golden-orange explosion at the center emblem; Gala a small silhouette at the heart of the blast; the ceiling hexagon panels above just starting to crack. Avoid: text, letters, speech bubbles, panel borders, goggles removed, Gala's eyes visible, any fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S3_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. The explosion blooms outward in slow motion into a golden-orange shockwave rolling across the floor and up the walls; ceiling hexagon panels crack apart and a few fall, opening a hole to pale light; smoke fills the room. Gala stays standing at the center, bracing behind his forearms. Camera slowly pulls back. Sound: deep booming explosion, rushing wind, cracking metal, debris clatter. Keep every character's design exactly as in the starting image throughout the whole clip: Gala's goggles stay on with fully opaque dark lenses and his eyes are never visible. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---

## Adegan 4: Kelahiran Ethylene

**Acuan komposisi:** Hal04_final (panel 1)  
**Lampirkan untuk gambar kunci:** K01_final, K03_final, L01_final, Hal04_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Ethylene: a fist-sized fire sprite, a perfectly round glossy glowing amber orb with a small flickering flame crown on top, two small flame wisps on its sides like tiny wings and a thin flame tail, two simple glowing white dot eyes, no mouth, no limbs. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. After the explosion: scorched black marks around the center emblem, thin drifting smoke, a hole of cracked hexagon ceiling panels open to pale light above. The moment: Close-up inside drifting smoke: glowing fire particles spiral into a single point, just beginning to form a small glowing orb. The cracked ceiling hole is softly visible in the background. Avoid: text, letters, speech bubbles, panel borders, a mouth on the fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S4_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. The spiraling fire particles swirl faster and condense into Ethylene: a small glossy amber orb forms, a flame crown flickers to life on top, two tiny flame wings unfold on its sides, a thin flame tail appears, and finally two white dot eyes open and blink. It bobs gently in the air. Sound: soft whoosh of swirling embers, a gentle magical chime as its eyes open. Keep every character's design exactly as in the starting image throughout the whole clip: the fire sprite never grows a mouth. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---

## Adegan 5: Pip?

**Acuan komposisi:** Hal04_final (panel 3 and 4)  
**Lampirkan untuk gambar kunci:** K01_final, K03_final, L01_final, Hal04_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes, his eyes never visible; fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots. Ethylene: a fist-sized fire sprite, a perfectly round glossy glowing amber orb with a small flickering flame crown on top, two small flame wisps on its sides like tiny wings and a thin flame tail, two simple glowing white dot eyes, no mouth, no limbs. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. After the explosion: scorched black marks around the center emblem, thin drifting smoke, a hole of cracked hexagon ceiling panels open to pale light above. The moment: Medium close-up: Gala, soot on his cheek and messy hair, stands in the thinning smoke looking at Ethylene, who hovers near his face at eye level. Dim flickering blue neon, soft warm glow from Ethylene. Avoid: text, letters, speech bubbles, panel borders, goggles removed, Gala's eyes visible, a mouth on the fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S5_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. Ethylene tilts to one side curiously and blinks its white dot eyes; Gala tilts his head in exhausted wonder, then a slow, tired, lopsided grin spreads across his face. Ethylene bobs up and down once. Camera slowly orbits a little around them. Sound: faint crackling embers, flickering neon buzz, one tiny high-pitched chirp from Ethylene. Keep every character's design exactly as in the starting image throughout the whole clip: Gala's goggles stay on with fully opaque dark lenses and his eyes are never visible; the fire sprite never grows a mouth. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---

## Adegan 6: Para Instruktur

**Acuan komposisi:** Hal05_final (panel 2)  
**Lampirkan untuk gambar kunci:** K30, L01_final, Hal05_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. The three instructors, adult proportions, about twice Gala's height, in identical dark navy sci-fi uniforms with thin gold trim: Lead Instructor, tall stern man, grey buzz cut; Second Instructor, stocky man, thick black mustache; Third Instructor, woman, short black bob, round glasses. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. After the explosion: scorched black marks around the center emblem, thin drifting smoke, a hole of cracked hexagon ceiling panels open to pale light above. The hazard-striped blast door on the left wall is open, bright white corridor light and smoke pouring out of it. The moment: Wide shot: the three instructors walk out of the open, brightly lit blast door into the smoky arena, the Lead Instructor in front, stern faces. Avoid: text, letters, speech bubbles, panel borders, any fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S6_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. The three instructors stride forward through the rolling smoke toward the camera, in step, the smoke parting around them; the Lead Instructor's eyes narrow. Camera slowly tracks backward in front of them. Sound: heavy door hiss, measured boot footsteps echoing, low tense ambience. Keep every character's design exactly as in the starting image throughout the whole clip. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---

## Adegan 7: 24 Jam

**Acuan komposisi:** Hal06_final (panel 3)  
**Lampirkan untuk gambar kunci:** K01_final, K03_final, L01_final, Hal06_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes, his eyes never visible; fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots. Ethylene: a fist-sized fire sprite, a perfectly round glossy glowing amber orb with a small flickering flame crown on top, two small flame wisps on its sides like tiny wings and a thin flame tail, two simple glowing white dot eyes, no mouth, no limbs. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. After the explosion: scorched black marks around the center emblem, thin drifting smoke, a hole of cracked hexagon ceiling panels open to pale light above. The moment: Medium shot: Gala in total shock, both hands clutching the sides of his head, eyebrows shot up above his goggles, mouth wide open; Ethylene beside him startled with flame wisps flared. Dim blue neon mixed with red light from off-screen. Avoid: text, letters, speech bubbles, panel borders, goggles removed, Gala's eyes visible, a mouth on the fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S7_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. Gala recoils in shock, grabbing his head, then his shoulders drop and he stares ahead, stunned; Ethylene flares up in alarm then shrinks its flames. A quick dramatic camera push-in on Gala's face. Sound: a sharp dramatic sting made of a low boom and a rising whoosh, then silence with faint neon buzz. Keep every character's design exactly as in the starting image throughout the whole clip: Gala's goggles stay on with fully opaque dark lenses and his eyes are never visible; the fire sprite never grows a mouth. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---

## Adegan 8: Nama Ethylene

**Acuan komposisi:** Hal07_final (panel 4) + Hal08_final (panel 1)  
**Lampirkan untuk gambar kunci:** K01_final, K03_final, L01_final, Hal07_final

**Prompt gambar kunci:**
```text
Create a NEW image: one single vertical 9:16 cinematic film frame. NOT a comic page: no panel borders, no speech bubbles, no captions, no sound effect lettering, no text of any kind. The attached images are references only: copy each character's design and the room's layout EXACTLY from the attached sheets; the attached comic page shows the moment and composition to recreate. Do not draw the sheets or any of their labels. 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, soft realistic materials, volumetric lighting, gentle depth of field. Gala Ignis: a stylized 3D chibi boy, chibi proportions with a large head about one third of his height; spiky dark purple hair; dark tactical goggles with fully opaque dark smoky lenses always worn over his eyes, his eyes never visible; fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots. Ethylene: a fist-sized fire sprite, a perfectly round glossy glowing amber orb with a small flickering flame crown on top, two small flame wisps on its sides like tiny wings and a thin flame tail, two simple glowing white dot eyes, no mouth, no limbs. Setting, Arena 7: a large hexagonal training hall; dark gunmetal hexagon wall panels; two horizontal cyan-blue neon strips around the walls, one at waist height and one near the ceiling; a polished dark floor with a large faint glowing hexagon emblem at the center; a wide blast door with yellow-and-black hazard stripes on the left wall; a tinted observation window high on the back wall. After the explosion: scorched black marks around the center emblem, thin drifting smoke, a hole of cracked hexagon ceiling panels open to pale light above. The moment: Golden dawn light pours down through the hole in the cracked ceiling onto the center emblem, dust motes floating. Gala stands on the emblem seen from behind at a slight angle, one hand raised, Ethylene glowing and hovering just above his open palm. Avoid: text, letters, speech bubbles, panel borders, goggles removed, Gala's eyes visible, a mouth on the fire sprite, 2D illustration, drawn line art, anime style.
```

**Prompt video (unggah S8_key.png sebagai gambar awal):**
```text
Animate the starting image into a smooth 8-second shot. Ethylene does a happy little hop above Gala's palm and flares brighter, sparks dancing around it; Gala raises his hand a little higher toward the light. Camera slowly cranes up and back, revealing the whole scorched arena bathed in golden dawn beams. Sound: warm soft wind, gentle crackle of Ethylene's flame, a tiny happy chirp, peaceful ambience. Keep every character's design exactly as in the starting image throughout the whole clip: Gala's goggles stay on with fully opaque dark lenses and his eyes are never visible; the fire sprite never grows a mouth. Stylized 3D animated feature film look, smooth cinematic motion, no morphing, no extra characters. Audio: sound effects and room ambience only; no dialogue, no voices, no music. No on-screen text or subtitles.
```

---
