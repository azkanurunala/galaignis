# Komik Episode 2: Pemeta Molekul (versi 2, dibuat ulang per panel)

*Gala Ignis & The Galians · Season 1 · sampul + 8 halaman · 27 gambar (26 panel + sampul)*

## Metode

- Setiap panel dibuat sebagai SATU gambar tanpa teks, di chat Gemini baru.
- Lampiran bernomor per panel (kode file di bawah). Urutan lampiran harus sama dengan urutan di prompt.
- Halaman disusun lokal, semua teks ditulis dengan Comic Neue Bold (dialog, narasi) dan Bangers (SFX), lalu gambar diperjelas dengan Real-ESRGAN.
- Panel versi 1 yang sudah bagus disimpan sebagai cadangan; per panel dipilih yang lebih baik.

## Aturan kesinambungan

- Gala menghadap meriam selama aksi di lorong. Kaki yang berapi dan menendang = kaki KIRI Gala: muncul di KANAN gambar saat Gala menghadap kamera, di KIRI gambar saat dilihat dari belakang.
- Kamera di belakang Gala = meriam terlihat di ujung lorong. Kamera di depan Gala = pintu bergaris kuning-hitam terlihat di belakangnya.
- Ethylene selalu ada: di bahu Gala, menyatu ke api kaki di Hal. 5, keluar dari asap sepatu di Hal. 6.
- Instruktur Ketiga satu-satunya orang dewasa; referensinya potongan K30_ketiga, bukan sheet tiga instruktur.
- Tidak ada teks di gambar. Semua balon, narasi, SFX dan tulisan layar ditulis lokal dengan Comic Neue Bold dan Bangers.
- Sains episode ini satu gagasan saja: ikatan terlemah putus lebih dulu. Chip memetakan ikatan, Gala memutus satu ikatan terlemah, bukan membakar semuanya. Ini fiksi yang bertumpu pada prinsip kimia umum, bukan klaim tentang plasma sungguhan.
- Video Short dibuka dengan panel tendangan api (Hal. 5 panel 3) selama 1 sampai 2 detik sebelum Halaman 1, bukan dengan panel lab yang tenang.

## Keputusan cerita

| Keputusan | Alasan |
|---|---|
| Teknisi di 2A.1a diganti Instruktur Ketiga | Tidak perlu karakter baru |
| Hitung mundur 19 jam lalu 14 jam | Menyambung ultimatum Episode 1 |
| Tendangan api memotong ketiga proyektil | Storyboard hanya memotong satu |
| Dialog "Api... ke kaki!" (tanpa kanan/kiri) | Kaki yang berapi = kaki kiri demi kesinambungan |
| Ethylene menyatu ke api kaki (Hal. 5) lalu keluar dari asap (Hal. 6) | Ethylene tidak boleh hilang tanpa penjelasan |
| Tulisan layar Hal. 7 ditulis lokal | Model gambar sering salah eja tulisan |

## Daftar paket per panel

| Halaman | Panel | Lampirkan (urutan) | Teks |
|---|---|---|---|
| Halaman 1 | 1 (atas, lebar) | K01_final, K03_final, K30_ketiga, L02_final, E02_REF_lab | Laboratorium Teknologi Akademi. / Sisa waktu: 19 jam. |
| Halaman 1 | 2 (tengah kiri) | K30_ketiga, L02_final, E02_REF_lab | Chip pemindai / molekul. Pasang di / goggles-mu. |
| Halaman 1 | 3 (tengah kanan) | K01_final, K03_final, E02_REF_lab | KLIK · Keren! / Ini buat apa? |
| Halaman 1 | 4 (bawah, lebar) | K30_ketiga, L02_final, E02_REF_lab | Apimu meledak / karena kamu tidak / melihat apa yang / kamu bakar. |
| Halaman 2 | 1 (atas, lebar) | K30_ketiga, L02_final, E02_REF_lab | Semuanya kelihatan. / Sampai ke atomnya! · BZZT! |
| Halaman 2 | 2 (tengah, besar) | K01_final, K03_final, E02_REF_lab | Terlalu banyak! / Kepalaku! · Pip?! |
| Halaman 2 | 3 (bawah, lebar) | K01_final, K03_final, K30_ketiga, E02_REF_lab | Jangan lihat semuanya. / Cari satu ikatan / yang paling lemah. |
| Halaman 3 | 1 (atas kiri) | K01_final, K03_final, E02_REF_lab | Pip. |
| Halaman 3 | 2 (atas kanan) | K01_final, E02_REF_lab | Satu ikatan / saja. |
| Halaman 3 | 3 (tengah, lebar) | L02_final, E02_REF_lab | Kena. |
| Halaman 3 | 4 (bawah, lebar) | K01_final, K03_final, K30_ketiga, L02_final, E02_REF_lab | Itu baru latihan. / Ujiannya / menembak balik. |
| Halaman 4 | 1 (atas, lebar) | K01_final, K03_final, L03_final, E02_Hal04_P4_raw | Lorong Tembak Akademi. · Lima meriam. / Jangan meledakkan apa pun. |
| Halaman 4 | 2 (tengah kiri) | L03_final, E02_Hal04_P4_raw | WRRRM |
| Halaman 4 | 3 (tengah kanan) | K01_final, K03_final, L03_final, E02_Hal04_P3_raw | Jangan dibakar semua. / Cari ikatannya. · Pip! |
| Halaman 4 | 4 (bawah, lebar) | L03_final, E02_Hal04_P4_raw | DZING! · DZING! · DZING! |
| Halaman 5 | 1 (atas, lebar) | L03_final, E02_Hal04_P4_raw | Ikatan terlemahnya. Di situ. |
| Halaman 5 | 2 (tengah, lebar) | K01_final, K03_final, L03_pintu, E02_Hal05_P2_raw | Ethylene, / ke kakiku! · Pip! |
| Halaman 5 | 3 (bawah, besar) | K01_final, L03_final, E02_Hal05_P3_raw | WHOOSH! |
| Halaman 6 | 1 (atas, splash) | K01_final, L03_final, E02_Hal05_P3_raw | SRAAAK! |
| Halaman 6 | 2 (bawah kiri) | K01_final, L03_pintu, E02_Hal05_P2_raw | (tanpa teks) |
| Halaman 6 | 3 (bawah kanan) | K01_final, L03_pintu, E02_Hal05_P2_raw | Nggak meledak? |
| Halaman 6 | 4 (strip bawah) | K03_final, K01_final, E02_Hal05_P2_raw | Pip! |
| Halaman 7 | 1 (atas, besar) | K01_final, K03_final, L03_pintu, E02_Hal05_P2_raw | TARGET NEUTRALIZED / PRECISION: 99.8% · DING! · 99,8 persen! / Lihat itu, Ethylene! · Pip! Pip! |
| Halaman 7 | 2 (bawah, lebar) | K01_final, K03_final, K30_ketiga, L03_pintu, E02_Hal05_P2_raw | Tidak buruk, Taruna. / Tapi panasmu / masih bocor. |
| Halaman 8 | 1 (atas, besar) | K01_final, K03_final, L03_final, E02_Hal05_P2_raw | Sisa waktu: 14 jam. |
| Halaman 8 | 2 (strip bawah) | K01_final, E02_Hal05_P2_raw | Bagaimana menjinakkan panas yang tersisa? · BERSAMBUNG · Episode 3: Nanoselulosa Penyeimbang |
| Sampul | Sampul (gambar saja) | K01_final, K03_final, L03_final, E02_Hal05_P3_raw | GALA IGNIS & THE GALIANS · EPISODE 2: PEMETA MOLEKUL |

## Halaman 1: Chip Pemindai

Tata letak: wide / persegi + persegi / wide

### Panel 1 (atas, lebar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) K30_ketiga, 4) L02_final, 5) E02_REF_lab

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the Third Instructor reference (the only instructor in this story); 4) the tech lab environment sheet; 5) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: eye level from the back of the lab, looking toward the front wall with the door.
Scene: wide establishing shot of the whole bright lab. Gala walks in through the sliding white door on the left, Ethylene hovering beside his shoulder; the Third Instructor waits at the central workbench under the ring light, small in the middle distance.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult proportions, about twice Gala's height. She is the only instructor; no other adults appear.
Place: the bright white-and-teal academy tech lab from the lab sheet: curved walls, a central workbench under a large circular ring light, rows of glowing teal hologram pedestals on both sides, tall glass cylinders of teal liquid along the back and right walls, a sliding white door with a teal light strip in the front wall.
Keep the upper left corner as plain wall. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, other instructors or adults, a slim realistic model-like woman.
```

### Panel 2 (tengah kiri)

**Lampirkan:** 1) K30_ketiga, 2) L02_final, 3) E02_REF_lab

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Third Instructor reference (the only instructor in this story); 2) the tech lab environment sheet; 3) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: at her chest height, she faces slightly to the left of the camera.
Scene: medium shot of the Third Instructor at the workbench, holding out between two fingers a tiny square chip engraved with gold batik lines, toward someone off-panel on the left. Calm, sharp-eyed.
The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult proportions, about twice Gala's height. She is the only instructor; no other adults appear.
Place: the bright white-and-teal academy tech lab from the lab sheet: curved walls, a central workbench under a large circular ring light, rows of glowing teal hologram pedestals on both sides, tall glass cylinders of teal liquid along the back and right walls, a sliding white door with a teal light strip in the front wall.
Keep the upper left quarter as plain softly blurred lab wall.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, other instructors or adults, a slim realistic model-like woman, Gala, children.
```

### Panel 3 (tengah kanan)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) E02_REF_lab

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: close, at Gala's eye level, bright soft lab light.
Scene: close-up of Gala snapping the tiny gold-engraved chip into the side of his goggle frame with his fingers; a thin line of blue light runs around the rim of the goggles; big excited grin. Ethylene peeks in curiously from the right edge. The lenses stay fully opaque and dark.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Keep the upper right corner as plain softly blurred lab wall.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, glowing lenses.
```

### Panel 4 (bawah, lebar)

**Lampirkan:** 1) K30_ketiga, 2) L02_final, 3) E02_REF_lab

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Third Instructor reference (the only instructor in this story); 2) the tech lab environment sheet; 3) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: medium close-up at her eye level.
Scene: the Third Instructor adjusts her round glasses with one finger, serious and calm, looking straight at the viewer (at Gala); the lab softly out of focus behind her. She stands on the left half of the image.
The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult proportions, about twice Gala's height. She is the only instructor; no other adults appear.
Place: the bright white-and-teal academy tech lab from the lab sheet: curved walls, a central workbench under a large circular ring light, rows of glowing teal hologram pedestals on both sides, tall glass cylinders of teal liquid along the back and right walls, a sliding white door with a teal light strip in the front wall.
Keep the right third of the image as plain softly blurred lab. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, other instructors or adults, a slim realistic model-like woman, Gala, the fire sprite.
```

---

## Halaman 2: Terlalu Banyak Data

Tata letak: wide / besar (Gala pusing, sudut miring) / wide

### Panel 1 (atas, lebar)

**Lampirkan:** 1) K30_ketiga, 2) L02_final, 3) E02_REF_lab

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Third Instructor reference (the only instructor in this story); 2) the tech lab environment sheet; 3) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: Gala's eye level, looking into the lab.
Scene: first-person view through Gala's goggles: the whole bright lab, every pedestal, cylinder and wall tagged with glowing grid lines and scan nodes, far too many of them, and several of the floating holographic lattices glitch with red error bars; the Third Instructor small in the background near the cylinders. No body parts of Gala visible.
Goggle HUD look: thin glowing blue and green grid lines and small round scan nodes overlaid on the view, a faint dark vignette like looking through goggle lenses, no readable text or numbers.
The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult proportions, about twice Gala's height. She is the only instructor; no other adults appear.
Place: the bright white-and-teal academy tech lab from the lab sheet: curved walls, a central workbench under a large circular ring light, rows of glowing teal hologram pedestals on both sides, tall glass cylinders of teal liquid along the back and right walls, a sliding white door with a teal light strip in the front wall.
Keep the bottom center as plain floor. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, other instructors or adults, a slim realistic model-like woman, hands, readable HUD text.
```

### Panel 2 (tengah, besar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) E02_REF_lab

```text
Create a NEW single image, landscape 3:2. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: close, tilted about 20 degrees, slightly below Gala's face.
Scene: a strongly tilted Dutch-angle close shot of Gala clutching his head with both hands, swaying, gritted teeth; streams of blue and green data race across the glossy surface of his opaque dark lenses; wobble lines around his head. Ethylene hovers close to his cheek on the right side, worried, its flame crown flattened.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Keep the upper left corner as plain softly blurred lab wall.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, a level horizon.
```

### Panel 3 (bawah, lebar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) K30_ketiga, 4) E02_REF_lab

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the Third Instructor reference (the only instructor in this story); 4) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: behind and left of Gala, at the instructor's chest height.
Scene: the Third Instructor, calm, holds a small glowing glass tablet and looks toward Gala; Gala stands dizzy in the left foreground seen from behind (big spiky hair, goggle strap, plain purple back plate), Ethylene hovering beside his head. She stands on the right half of the image.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult proportions, about twice Gala's height. She is the only instructor; no other adults appear.
Place: the bright white-and-teal academy tech lab from the lab sheet: curved walls, a central workbench under a large circular ring light, rows of glowing teal hologram pedestals on both sides, tall glass cylinders of teal liquid along the back and right walls, a sliding white door with a teal light strip in the front wall.
Keep the upper middle as plain softly blurred lab. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, other instructors or adults, a slim realistic model-like woman, the instructor shorter than Gala.
```

---

## Halaman 3: Satu Ikatan

Tata letak: persegi + persegi / wide / wide

### Panel 1 (atas kiri)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) E02_REF_lab

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: close, at Gala's eye level, bright soft lab light.
Scene: close-up of Gala's face and shoulders, eyes hidden behind opaque dark lenses, a small calm smile; Ethylene hovers right beside his ear on the right, releasing soft warm golden particles that drift around his head.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Keep the upper right corner as plain softly blurred lab wall.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite.
```

### Panel 2 (atas kanan)

**Lampirkan:** 1) K01_final, 2) E02_REF_lab

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: close, slightly lower than his eyes.
Scene: close-up of Gala breathing slowly, a small relieved smile; his lenses are opaque dark smoky glass with only thin faint horizontal lines of blue HUD light reflected across the surface, never round shapes in the lens centers.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Keep the lower left corner as plain softly blurred lab.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, round shapes on the lenses, the fire sprite.
```

### Panel 3 (tengah, lebar)

**Lampirkan:** 1) L02_final, 2) E02_REF_lab

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the tech lab environment sheet; 2) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: Gala's eye level.
Scene: first-person view through Gala's goggles: a translucent blue holographic training dummy standing on a lab pedestal, one clean golden crosshair locked on its chest, the rest of the HUD quiet and dim. No characters, no body parts.
Goggle HUD look: thin glowing blue and green grid lines and small round scan nodes overlaid on the view, a faint dark vignette like looking through goggle lenses, no readable text or numbers.
Keep the lower left corner plain. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, people, hands, readable HUD text.
```

### Panel 4 (bawah, lebar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) K30_ketiga, 4) L02_final, 5) E02_REF_lab

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the Third Instructor reference (the only instructor in this story); 4) the tech lab environment sheet; 5) an approved panel of this comic in the same lab, reference for rendering style and lighting only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: behind and left of Gala, eye level.
Scene: Gala in the left foreground seen in a three-quarter back view, in a low pencak silat stance aimed at a translucent blue holographic training dummy at the back center; Ethylene hovers by his shoulder. On the right, the Third Instructor lowers her tablet with a slight approving nod, clearly taller than Gala.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult proportions, about twice Gala's height. She is the only instructor; no other adults appear.
Place: the bright white-and-teal academy tech lab from the lab sheet: curved walls, a central workbench under a large circular ring light, rows of glowing teal hologram pedestals on both sides, tall glass cylinders of teal liquid along the back and right walls, a sliding white door with a teal light strip in the front wall.
Keep the upper right corner as plain wall. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, other instructors or adults, a slim realistic model-like woman, Gala facing the camera, the instructor shorter than Gala.
```

---

## Halaman 4: Lorong Tembak

Tata letak: wide / persegi + persegi / wide

### Panel 1 (atas, lebar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) L03_final, 4) E02_Hal04_P4_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the firing corridor environment sheet; 4) an approved panel of this comic in the same corridor, reference for rendering style, lighting and the red plasma spheres only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: behind Gala, looking down the corridor to the cannons.
Scene: strong one-point perspective down the long dark corridor. Gala stands small in the lower left foreground seen from behind, looking toward the far end; Ethylene hovers beside his shoulder. At the far end, the five cannons charge with a red glow. His hands are empty.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the upper left and upper right corners as plain dark wall. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, a bright room, a different number of cannons, glowing objects in his hands.
```

### Panel 2 (tengah kiri)

**Lampirkan:** 1) L03_final, 2) E02_Hal04_P4_raw

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the firing corridor environment sheet; 2) an approved panel of this comic in the same corridor, reference for rendering style, lighting and the red plasma spheres only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: low angle, facing the end wall.
Scene: dramatic close-up of the five robotic plasma cannons on the end wall, dark metal barrels pointing at the camera, muzzles glowing hot red, faint heat haze and small sparks. No characters.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the lower third fairly plain.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, characters, people.
```

### Panel 3 (tengah kanan)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) L03_final, 4) E02_Hal04_P3_raw

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the firing corridor environment sheet; 4) an approved panel of this comic showing how Gala and Ethylene are rendered and lit in this corridor (style reference only, do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: in front of Gala, on the cannon side, looking back toward the entrance door.
Scene: medium shot of Gala facing the camera, confident smirk, one fist raised in front of his chest; Ethylene bounces excitedly beside his head. Red glow from the cannons behind the camera lights his front; lenses opaque with only a tiny red reflection. Behind him: the hazard-striped entrance door.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the top third above their heads as plain dark wall.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, cannons behind Gala.
```

### Panel 4 (bawah, lebar)

**Lampirkan:** 1) L03_final, 2) E02_Hal04_P4_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the firing corridor environment sheet; 2) an approved panel of this comic in the same corridor, reference for rendering style, lighting and the red plasma spheres only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: at Gala's position, looking down the corridor to the cannons.
Scene: three glowing red plasma spheres fired at the same moment from three of the five cannons, streaking down the dark corridor straight toward the camera with long motion-blur trails, the nearest one large. No characters.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the upper band fairly plain. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, characters, people, explosions.
```

---

## Halaman 5: Ikatan Terlemah

Tata letak: wide / wide / wide besar

### Panel 1 (atas, lebar)

**Lampirkan:** 1) L03_final, 2) E02_Hal04_P4_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the firing corridor environment sheet; 2) an approved panel of this comic in the same corridor, reference for rendering style, lighting and the red plasma spheres only (do not copy its composition). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: Gala's eye level, looking toward the cannons.
Scene: first-person view through Gala's goggles, an extreme close view of ONE red plasma sphere filling most of the frame, the other two blurred behind it. The goggle HUD draws a thin glowing blue molecular lattice over the sphere's surface, like a net of linked nodes, and exactly ONE link in that net glows bright gold and is circled by a small golden target ring: the weakest bond. No body parts.
Goggle HUD look: thin glowing blue and green grid lines and small round scan nodes overlaid on the view, a faint dark vignette like looking through goggle lenses, no readable text or numbers.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the upper left corner plain. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, people, hands, readable HUD text.
```

### Panel 2 (tengah, lebar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) L03_pintu, 4) E02_Hal05_P2_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the entrance end of the firing corridor: hazard-striped door with a wide display screen above it; 4) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: low angle in front of Gala, on the cannon side, looking back toward the entrance door.
Scene: Gala faces the camera in a wide low stance, determined grin, fists clenched. Ethylene dives down into the leg on the RIGHT side of the image, and golden-orange flames burst up and wrap tightly around that leg from boot to knee; Ethylene is half merged into the fire, still recognizable. His brown batik sash blows backward.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Behind Gala: the hazard-striped entrance door with the display screen above it, exactly as in reference 3. No cannons visible.
Keep the upper right corner as plain dark wall. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, cannons, flames on the leg on the left side of the image, fire spread on the floor.
```

### Panel 3 (bawah, besar)

**Lampirkan:** 1) K01_final, 2) L03_final, 3) E02_Hal05_P3_raw

```text
Create a NEW single image, landscape 3:2. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the firing corridor environment sheet; 3) an approved panel of this comic showing Gala from behind, kicking toward the cannons (camera-side and style reference, do not copy it). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: behind and slightly below Gala, looking down the corridor to the cannons.
Scene: Gala mid-air in a spinning pencak silat kick, seen in a three-quarter back view, aimed at the far end. His kicking leg, on the LEFT side of the image, is wrapped in bright golden-orange flame and sweeps a wide flaming arc across the corridor right in the path of three red plasma spheres flying from the cannons straight at him. Sparks and embers. His back: big spiky hair with the goggle strap, plain purple back plate, green sleeves, brown batik sash.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the top quarter of the image as plain dark ceiling.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, Gala facing the camera, spheres coming from the side, explosions, spheres already destroyed, the fire sprite as a separate orb.
```

---

## Halaman 6: Terbelah

Tata letak: splash wide / persegi + persegi / strip

### Panel 1 (atas, splash)

**Lampirkan:** 1) K01_final, 2) L03_final, 3) E02_Hal05_P3_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the firing corridor environment sheet; 3) an approved panel of this comic showing Gala from behind, kicking toward the cannons (camera-side and style reference, do not copy it). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: behind Gala, looking down the corridor to the cannons.
Scene, the moment right after reference 3: Gala at the end of his spinning kick seen in a three-quarter back view, his flaming kicking leg on the LEFT side of the image; a huge glowing golden-orange flame arc has sliced all three red plasma spheres cleanly in half: six half-spheres drifting apart, bright golden sparks spraying along each clean cut. NO explosion, NO fireball, NO smoke cloud.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the top fifth as plain dark ceiling. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, explosions, fireballs, whole unbroken spheres, Gala facing the camera.
```

### Panel 2 (bawah kiri)

**Lampirkan:** 1) K01_final, 2) L03_pintu, 3) E02_Hal05_P2_raw

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the entrance end of the firing corridor: hazard-striped door with a wide display screen above it; 3) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: low, in front of Gala on the cannon side, looking back toward the door.
Scene: Gala lands in a three-point landing facing the camera, one knee low, one fist on the floor, head up. Thin grey smoke curls from the boot on the RIGHT side of the image. Behind him six red half-spheres dissolve harmlessly into drifting golden sparks. Calm.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Behind Gala: the hazard-striped entrance door, exactly as in reference 2. No cannons.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, cannons, explosions, fire on his body.
```

### Panel 3 (bawah kanan)

**Lampirkan:** 1) K01_final, 2) L03_pintu, 3) E02_Hal05_P2_raw

```text
Create a NEW single image, square 1:1. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the entrance end of the firing corridor: hazard-striped door with a wide display screen above it; 3) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: in front of Gala on the cannon side.
Scene: medium close-up of Gala still crouched, twisting to look back over his shoulder at the last golden sparks fading behind him near the door; surprised, eyebrows raised high above his thick goggles, mouth slightly open. Lenses fully opaque and dark.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Behind Gala: the hazard-striped entrance door. Keep the top third as plain dark wall.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, cannons, thin sunglasses instead of thick goggles.
```

### Panel 4 (strip bawah)

**Lampirkan:** 1) K03_final, 2) K01_final, 3) E02_Hal05_P2_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Ethylene fire sprite sheet; 2) the Gala character sheet; 3) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: at floor level.
Scene: floor-level close-up: on the left third only Gala's green-and-purple boot and lower leg with thin grey smoke curling up; in the middle Ethylene pops out of that smoke with a tiny burst of golden sparks, shaking the smoke off, cheerful. The hazard-striped door softly out of focus behind.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Keep all action inside the middle horizontal band; top and bottom fifths plain dark wall and floor.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, a mouth on the fire sprite, Gala's face, a full figure of Gala, cannons.
```

---

## Halaman 7: 99,8 Persen

Tata letak: besar (Gala, Ethylene dan layar hasil) / wide

### Panel 1 (atas, besar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) L03_pintu, 4) E02_Hal05_P2_raw

```text
Create a NEW single image, landscape 3:2. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the entrance end of the firing corridor: hazard-striped door with a wide display screen above it; 4) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: in front of Gala on the cannon side, slightly low, looking toward the door.
Scene: Gala grins widely and gives a big thumbs-up to Ethylene, who bounces happily in the air in front of him. Above the hazard-striped door behind them, the wide display screen glows plain bright green with an empty frame and NO writing (the words are added later); green light spills over both of them. Gala on the left half, Ethylene right of center, the whole screen visible in the upper part of the image.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
The screen must be BLANK. Keep the lower corners plain.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, cannons, any writing on the screen.
```

### Panel 2 (bawah, lebar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) K30_ketiga, 4) L03_pintu, 5) E02_Hal05_P2_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the Third Instructor reference (the only instructor in this story); 4) the entrance end of the firing corridor: hazard-striped door with a wide display screen above it; 5) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: behind Gala, looking toward the open entrance door.
Scene: the entrance door is open; the Third Instructor stands in the doorway on the right half, arms crossed, a small approving smile. In the left foreground Gala is seen from behind (spiky hair, goggle strap, plain purple back plate), thin smoke still rising from one boot and his sash; Ethylene by his shoulder.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
The Third Instructor: the adult woman from her reference: short black bob, round glasses, navy uniform jacket with a diagonal gold-piped closure and a small name plate, black belt with pouches, navy trousers tucked into knee-high black boots; adult proportions, about twice Gala's height. She is the only instructor; no other adults appear.
Keep the upper left corner plain. Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, other instructors or adults, a slim realistic model-like woman, the instructor shorter than Gala.
```

---

## Halaman 8: Panas yang Tersisa

Tata letak: besar / strip penutup

### Panel 1 (atas, besar)

**Lampirkan:** 1) K01_final, 2) K03_final, 3) L03_final, 4) E02_Hal05_P2_raw

```text
Create a NEW single image, portrait 4:5. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the firing corridor environment sheet; 4) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: medium shot, slightly above Gala, looking down at him.
Scene: Gala stands alone in the dim corridor holding up the end of his brown batik sash in one hand, looking down at it; thin smoke rises from the fabric and its batik lines glow faintly orange; Ethylene hovers beside his shoulder looking at it too, a little worried. Quiet, reflective mood.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Place: the dark academy firing corridor from the corridor sheet: gunmetal hexagon wall panels, orange light strips, small orange guide lights along the floor edges; five robotic plasma cannons in one row on the far end wall; the hazard-striped entrance door with a display screen above it at the near end.
Keep the upper left corner as plain dark wall.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite.
```

### Panel 2 (strip bawah)

**Lampirkan:** 1) K01_final, 2) E02_Hal05_P2_raw

```text
Create a NEW single image, landscape 16:9. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) an approved panel of this comic showing Gala facing the camera with the entrance end of the corridor behind him (style and background reference, do not copy his pose). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: close, slightly above the cloth.
Scene: a dark, moody end-card image: only a small folded piece of brown batik cloth resting on a dark metal floor, its batik lines glowing faintly orange, a thin wisp of smoke. Lots of empty dark space on the left and right for titles.
Keep every important element away from the top and bottom tenth of the image, because the panel will be cropped a little wider.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, characters, people.
```

---

## Sampul

**Lampirkan:** 1) K01_final, 2) K03_final, 3) L03_final, 4) E02_Hal05_P3_raw

```text
Create a NEW single image, portrait 9:16. This is ONE comic panel, not a page: no panel borders, no text, no letters, no numbers, no speech bubbles, no captions, no sound-effect lettering.
Attached references, in order: 1) the Gala character sheet; 2) the Ethylene fire sprite sheet; 3) the firing corridor environment sheet; 4) an approved panel of this comic showing Gala from behind, kicking toward the cannons (camera-side and style reference, do not copy it). Copy the characters and the place EXACTLY from these references. Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.
Style: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.
Camera: low angle in front of Gala.
Scene: dynamic cover art: Gala mid-air in a flaming pencak silat kick toward the camera, his kicking leg wrapped in golden-orange flame, slicing a red plasma sphere in half with golden sparks; Ethylene flying beside him; the dark hexagon corridor with orange lights behind. Thrilling, heroic.
Gala: chibi boy with a big head (about one third of his height), big spiky dark purple hair, thick dark tactical goggles with fully opaque dark smoky lenses always over his eyes (his eyes are never visible), green shirt, purple armor with gold batik engravings on chest and shoulders, green-and-purple gauntlets, brown batik sash tied at the waist, black pants, green-and-purple boots. No pin or badge on his chest.
Ethylene: a fist-sized round glossy glowing amber orb with a small flame crown, two tiny flame wisps on its sides and a thin flame tail, two simple glowing white dot eyes, NO mouth, no limbs.
Keep the top quarter and the bottom tenth of the image as plain dark background for the title.
Avoid: any text, letters or numbers, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors, extra limbs, distorted hands, goggles pushed up or removed, Gala's eyes visible through the lenses, a pin or badge on Gala's chest, changed hair or armor colors, a mouth on the fire sprite, explosions.
```
