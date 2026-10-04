import re
from s1 import S1
from s2 import S2
from b_s1 import B1
from b_s2 import B2
from s3 import S3 as S3F
from s3_arc2 import ARC2
from s3_arc3 import ARC3
S3F['arcs'] += [ARC2, ARC3]
from s4_a1 import S4A1
from s4_a23 import S4A2, S4A3
S4F = {"n": 4, "arcs": [S4A1, S4A2, S4A3]}
from s5 import S5A1, S5A2, S5A3
S5F = {"n": 5, "arcs": [S5A1, S5A2, S5A3]}
import importlib
EXTRA = []  # (season number, text file, module name)
for _n in range(6, 11):
    try:
        _m = importlib.import_module(f"s{_n}")
    except ModuleNotFoundError:
        continue
    EXTRA.append((_n, f"s{_n}_text.md", {"n": _n, "arcs": [getattr(_m, f"S{_n}A{i}") for i in (1, 2, 3)]}))

AILA = ("Aila, Gala's squadmate, a stylized 3D chibi girl scout: short silver-white bob hair with one thin braid; a clear teal visor "
        "over her eyes; fitted teal-and-silver light armor; slim wind fins mounted on both wrists; white pants; light silver boots.")
DHRUVA = ("Dhruva, Gala's squadmate, a stylized 3D chibi boy guardian, broader and a head taller than Gala: short black hair shaved "
          "at the sides; open determined face with thick eyebrows; rust-red and dark bronze heavy armor; a large rectangular tower "
          "shield engraved with a kawung batik pattern; dark brown pants; heavy bronze boots.")
KALIA = ("Kalia, leader of the resistance in the parallel timeline, a stylized 3D chibi young woman: long ash-grey hair tied high; "
         "calm face with sharp eyebrows; a patched indigo coat stitched from salvaged batik scraps; a brass clockwork gauntlet on "
         "her left arm; dark grey pants; worn brown boots.")
GALA_BAYANG = ("Gala Bayang, Gala Ignis's alternate-timeline self, a stylized 3D chibi boy of the same size: ash-white spiky hair; "
               "cracked dark goggles over his eyes with a faint purple glow in the cracks; no armor; a scorched, faded green shirt; "
               "a torn plain grey sash with no batik pattern; black pants; plain grey boots.")
WIRA_BASE = ("Wirasena, an ancient exiled Galian commander, a stylized 3D chibi figure much taller than Gala: long white hair; "
             "weathered bronze-and-stone armor cracked with glowing black-violet batik lines; a long ragged cloak of tattered black batik; "
             "a frayed ancient brown batik sash wrapped around his left forearm")
WIRA_M = WIRA_BASE + "; a rigid, smooth, cracked grey stone mask covering his whole face, its features chiseled away: no mouth, only two shallow dark eye hollows."
WIRA_V = WIRA_BASE + "; no mask; a stern old face with a deep scar across the right brow and tired dark eyes."
MAHESWARI = ("Maheswari, head of the Galians High Council, a stylized 3D chibi elderly woman: silver hair in a tall bun with a gold hairpin; "
             "a ceremonial deep green robe with gold parang batik trim; a gold Galians crest brooch; a carved wooden staff.")
INDRA = ("Indra Mahadana, founder and CEO of Vextron, a stylized 3D chibi adult man: slicked-back black hair with a single silver streak; "
         "rimless smart-glasses with violet-tinted lenses; a tailored charcoal suit with thin violet circuit lines on the lapels; a small glowing violet V-shaped Vextron pin; "
         "polished black shoes.")
EXTRA_ANCHORS = {
 "a": ("Tetua Agni, an ancient fire sprite the size of a child: a deep crimson glowing core, a flowing mane of flame, two simple white dot eyes, "
       "three thin gold rings slowly orbiting its body."),
 "r": ("Vikrama, deputy of the Galians High Council, a stylized 3D chibi middle-aged man: close-cropped grey hair; a square jaw with a "
       "trimmed grey beard; a dark steel-grey council robe with sharp angular shoulder plates; a red sash of office across one shoulder; black gloves."),
 "R": ("Vikrama, deputy of the Galians High Council, a stylized 3D chibi middle-aged man: close-cropped grey hair; a square jaw with a "
       "trimmed grey beard; wearing heavy steel-grey powered exo-armor over his council robe, a glowing red core in the chest plate, "
       "a red sash of office still across one shoulder; black gloves."),
 "n": ("Nira, a former cadet turned hacker, a stylized 3D chibi teen girl: short black asymmetrical hair covering her right eye; a dark hooded "
       "jacket with glowing cyan data-lining; fingerless black gloves; a small wrist-mounted hologram emitter; dark cargo pants; black sneakers."),
 "k": ("Arka (Subject Zero), a stylized 3D chibi boy slightly smaller than Gala: short spiky pale-gold hair; a thin white visor band "
       "covering his eyes; a white-and-gold bodysuit with glowing gold vein lines; orange-gold gauntlets; white boots; no sash, no goggles."),
 "t": ("Taraka, a rogue Garda Besi commander, a stylized 3D chibi lean adult man: shaved head with a thin red circuit tattoo along the scalp; "
       "a red monocle visor over his left eye; a long black-and-steel coat; a mechanical left arm ending in a clamp-shaped plasma siphon."),
 "u": ("Sang Utusan, envoy of the Entropy Catalyst, a stylized 3D chibi tall slender figure: a long white-grey hooded robe whose hem "
       "dissolves into drifting grey particles; a smooth porcelain-white face with no mouth and two thin horizontal eye slits glowing faint grey; "
       "long thin grey hands."),
 "c": ("Katalis Entropi (the Entropy Catalyst), a colossal formless shape of grey-white mist with pale rings turning slowly around it "
       "and a single hollow white void at its center; everything near it is drained of color."),
 "h": ("Sang Hampa, a towering hollow silhouette of pure darkness with edges fizzing with cold white static, two pinpoint white lights for eyes, "
       "no other features."),
}
SQUAD_LOCK = "Keep every character's hair, colors and gear exactly as described; do not merge or swap their designs."

# Title cards moved from end of Sub-Episode A to end of Sub-Episode B
OVERRIDES = {
 "10A.2d": ("10A.2d", "Heroic Shot", "Gala mengangkat tinju api ke langit pagi bersama Ethylene.", "Gala raises a flaming fist to the morning sky beside the sprite, sunlight on his armor.", "GS"),
 "15A.2d": ("15A.2d", "Wide Heroic Shot", "Gala mengangkat tinju api bersama Ethylene; seluruh ordo membalas hormat.", "Gala raises a flaming fist with the sprite as the whole order salutes back in the ceremonial hall.", "GS"),
 "20A.2d": ("20A.2d", "Medium Interior Shot", "Dari kapal angkut Gala menatap reruntuhan benteng.", "Inside the transport, Gala looks back through the window at the burning fortress ruins, the sprite beside him.", "GS"),
 "25A.2d": ("25A.2d", "Heroic Shot", "Gala mengangkat tinju api; Ethylene hinggap di buku jarinya.", "Gala raises a flaming fist with the sprite perched on his knuckles, the lit city below.", "GS"),
 "15A.2b": ("15A.2b", "Close-Up", "Kepala Dewan Maheswari menyematkan pin roset emas bermata merah di dada kanan atas Gala.", "Maheswari, head of the High Council, pins a small round gold rosette pin with a red gem onto the upper right chest of Gala's armor.", "GM"),
 "30A.2d": ("30A.2d", "Medium Shot", "Gala dan Ethylene di antara partikel emas, retakan di atas mereka.", "Gala stands with the sprite among floating gold particles, the rift glowing above them.", "GS"),
}

def merge():
    B = {**B1, **B2}
    for S in (S1, S2):
        for A in S["arcs"]:
            for E in A["eps"]:
                for SE in E["subs"]:
                    for AC in SE["acts"]:
                        AC["frames"] = [OVERRIDES.get(f[0], f) for f in AC["frames"]]
                if E["n"] in B and len(E["subs"]) == 1:
                    E["subs"].append(B[E["n"]])
    # Perbaikan kesinambungan (audit putaran 2): mengganti isi frame dan ringkasan tanpa mengubah kode.
    import json as _j
    P = _j.load(open("perbaikan.json", encoding="utf-8"))
    for S in [S1, S2, S3F, S4F, S5F] + [x[2] for x in EXTRA]:
        for A in S["arcs"]:
            for E in A["eps"]:
                if str(E["n"]) in P["ringkasan"]:
                    E["focus"] = P["ringkasan"][str(E["n"])]
                for SE in E["subs"]:
                    for AC in SE["acts"]:
                        AC["frames"] = [(f[0], *P["frames"][f[0]]) if f[0] in P["frames"] else f for f in AC["frames"]]

GALA_V1 = ("Gala Ignis, a stylized 3D chibi boy warrior with chibi proportions, a large head about one third of his height: spiky dark purple hair; dark tactical goggles always worn fixed over his eyes "
           "(eyes never visible); fitted green tactical shirt; purple armor plates with gold batik engravings on chest, shoulders and forearms; "
           "green-and-purple armored gauntlets; brown batik cloth sash tied at the waist; black pants; green-and-purple combat boots.")
GALA_V2 = GALA_V1[:-1] + "; a small round gold rosette pin with a red gem center and two tiny ribbon tails on the upper right chest."
SPRITE = ("Ethylene, his fist-sized fire sprite: a perfectly round glossy glowing amber orb with a small flickering flame crown on top, "
          "two small flame wisps on its sides like tiny wings and a thin flame tail; two simple glowing white dot eyes; no mouth, no limbs.")
STYLE = ("Rendering style: 3D CGI render, like a still frame from a modern 3D animated feature film; rounded stylized 3D shapes, "
         "soft realistic materials, volumetric cinematic lighting, gentle depth of field.")
STYLE_AVOID = "Avoid: 2D illustration, drawn line art, ink outlines, anime or manga style, cel shading, flat colors, sketch."
LOCK = "Maintain exact character design: goggles stay on over his eyes, no added or removed accessories, no color changes."
NEG = ("Negative: goggles removed or pushed up, visible eyes, helmet, cape, mask, extra accessories, changed hair color, "
       "changed armor color, extra limbs, distorted hands.")
V2_START = "15A.2c"

from catalog import LOCS, SECONDARY_RX, secondary_for, location_for
import antislop_lib as AS
ETH_ADDED = []
import re as _re

def prompt(scene, flags, v2, code=None):
    low = scene.lower()
    if "squad" in low or "teammate" in low:
        flags += "AD"
    parts = []
    if "G" in flags:
        parts.append(GALA_V2 if v2 else GALA_V1)
    if "S" in flags:
        parts.append(SPRITE)
    if "A" in flags:
        parts.append(AILA)
    if "D" in flags:
        parts.append(DHRUVA)
    if "K" in flags:
        parts.append(KALIA)
    if "X" in flags:
        parts.append(GALA_BAYANG)
    if "W" in flags:
        parts.append(WIRA_M)
    if "V" in flags:
        parts.append(WIRA_V)
    if "M" in flags:
        parts.append(MAHESWARI)
    if "I" in flags:
        parts.append(INDRA)
    for key, text in EXTRA_ANCHORS.items():
        if key in flags:
            parts.append(text)
    if code:
        ep = int(_re.match(r"\d+", code).group())
        sec = secondary_for(ep, scene)
        for k, n, a, rx, lo, hi in SECONDARY_RX:
            if k in sec:
                parts.append(a)
        loc = location_for(code)
        if loc:
            parts.append("Setting: " + LOCS[loc][1])
    parts.append("Scene: " + scene)
    parts.append(STYLE)
    if "G" in flags:
        parts.append(LOCK)
    if any(c in flags for c in "ADKXWVMI" + "".join(EXTRA_ANCHORS)):
        parts.append(SQUAD_LOCK)
    out = " ".join(parts)
    if "G" in flags:
        out += "\n" + NEG
    out += "\n" + STYLE_AVOID
    return out

HEADER = """# Gala Ignis & The Galians: Master Story Bible

Versi 3.3 · 3 Oktober 2026 · Status: **seri lengkap**. Season 1 sampai 10, 150 episode, 2.400 frame, semuanya sampai Level 6.

Dokumen ini merapikan seluruh hasil sesi Gemini (desain karakter, lore, peta 10 season, dan storyboard Season 1 sampai 2) menjadi satu sumber acuan. Setiap prompt storyboard sudah otomatis membawa **Character Anchor** lengkap, jadi bisa langsung disalin ke generator gambar/video tanpa menambah deskripsi karakter secara manual.

## Daftar Isi

1. Catatan Revisi dari Versi Gemini
2. Standar Struktur Cerita
3. Character Anchor dan Aturan Konsistensi
4. Lore Ringkas
5. Peta 10 Season
6. Aturan Mutu Produksi
7. Backlog dan Keputusan Terbuka

## Daftar File

Bible ini dipecah per season supaya ringan dibuka dan dicari. File ini (**00-inti**) memuat semua aturan dan anchor; file season memuat storyboard. Setiap prompt di file season sudah membawa anchor lengkap, jadi bisa langsung disalin tanpa membuka file ini.

| File | Isi | Frame |
|---|---|---|
| `00-inti.md` | Revisi, struktur, anchor karakter, lore, peta season, backlog | - |
| `season-01.md` | Season 1: Inisiasi Sang Galian (Ep 1-15) | 240 |
| `season-02.md` | Season 2: Ancaman Inti Atom (Ep 16-30) | 240 |
| `season-03.md` | Season 3: Paradoks Waktu (Ep 31-45) | 240 |
| `season-04.md` | Season 4: Bayangan Sang Purba (Ep 46-60) | 240 |
| `season-05.md` | Season 5: Invasi Cyber-Nusantara (Ep 61-75) | 240 |
| `season-06.md` | Season 6: Realm of Ethylene (Ep 76-90) | 240 |
| `season-07.md` | Season 7: Keretakan Aliansi (Ep 91-105) | 240 |
| `season-08.md` | Season 8: Resonansi Emas (Ep 106-120) | 240 |
| `season-09.md` | Season 9: Gerhana Atom (Ep 121-135) | 240 |
| `season-10.md` | Season 10: Era Baru Galians (Ep 136-150), finale | 240 |
| `referensi-karakter.md` | 58 lembar referensi karakter: tokoh utama beserta versi desainnya, tokoh pendukung, unit musuh, kelompok figuran | - |
| `referensi-latar.md` | 68 lembar referensi lokasi untuk seluruh 150 episode | - |
| `kit-per-episode.md` | Daftar lembar karakter dan latar yang dilampirkan untuk setiap episode | - |
| `komik-episode-01.md` | Adaptasi komik Episode 1 untuk Gemini | - |

---

## 1. Catatan Revisi dari Versi Gemini

Yang diubah dan alasannya. Semua bisa dibalik kalau kamu tidak setuju.

| # | Masalah di versi Gemini | Perbaikan |
|---|---|---|
| 1 | Desain dikunci "selalu pakai goggles", tetapi Episode 1 menulis Gala tanpa goggles, dan beberapa frame menaruh goggles di leher/dahi. Ini persis penyebab goggles "hilang" di video AI. | Goggles **selalu terpasang di mata** di semua frame. Episode 2 diubah dari "menerima goggles" menjadi "memasang modul HUD pemindai" ke goggles yang sudah ada. |
| 2 | Prompt per-frame pendek dan tidak konsisten: gauntlet hijau-ungu tidak pernah disebut, Ethylene tidak punya deskripsi fisik sama sekali. | Semua prompt kini diawali Character Anchor lengkap + negative prompt. Desain Ethylene diusulkan dan dikunci di Bagian 3. |
| 3 | Frame ekspresi menyebut "wide eyes" padahal mata tertutup goggles, memancing AI menggambar mata dan melepas goggles. | Ekspresi ditulis lewat alis, mulut, dan pantulan di lensa. |
| 4 | Gala "lulus" dua kali: Ep 5 (dilantik Vanguard + pin) dan Ep 15 (dilantik lagi, kali ini "Commander"). | Ep 5 = lulus Ujian Pertama (tanpa pin). Ep 15 = pelantikan resmi sebagai Galian Vanguard (bukan Commander) + pin lambang. |
| 5 | Ep 15 menambahkan jubah pendek Vanguard: aksesori baru yang lalu tidak pernah muncul lagi di prompt Season 2. | Jubah dihapus. Satu-satunya perubahan desain permanen adalah pin lambang emas (Anchor v2). Medali Ep 30 hanya seremonial. |
| 6 | Nama jurus "Galian Atomic Buster" sudah dipakai di Ep 5, sehingga debut di Ep 14 kehilangan bobot. | Ep 5 memakai Atomic Fire Kick biasa. Galian Atomic Buster Kick debut di Ep 14, Supreme Buster di Ep 29. |
| 7 | Judul Act 14A.2 "Kehancuran Faksi Absolute Zero", padahal faksi itu baru tumbang di Season 2. | Diganti "Kekalahan Jenderal Cryo-Tech". |
| 8 | Klaim hitungan "240 Sub-Act untuk Season 1" dan "480 untuk Season 1+2" tidak sesuai isi (aslinya 280). | Versi 2.1 menulis Sub-Episode B untuk Ep 6 sampai 30 (200 frame), sehingga hitungan kini benar-benar 480. |
| 9 | Season overview awal menyebut musuh Season 1 adalah Rogue Drones, tetapi naskahnya memakai Cryo-Tech sejak Arc 2. | Peta season disesuaikan dengan naskah yang sudah jadi. |
| 10 | Salah ketik (sush, rektsi, nuggles, "bersembunyi di balik matanya", dll.) dan judul yang janggal ("Sanction Cryo-Tech", "Vanguard Sektor 7" sebelum Gala jadi Vanguard). | Dibetulkan: "Sandi Cryo-Tech", "Fajar di Sektor 7", "Pelantikan Sang Vanguard", "Pemulihan Daya Kota". |
| 11 | Retakan waktu di akhir Season 2 muncul tanpa sebab. | Diberi sebab: benturan Supreme Buster dengan orb antimateri di Ep 29. HUD sudah memperingatkan risikonya di 28B.2b dan Gala tetap memilih menyerang, jadi ia ikut bertanggung jawab. Ini memberi bobot moral untuk Season 3. |
| 12 | Title card "ARC COMPLETE / SEASON COMPLETE" ada di akhir Sub-Episode A, padahal kini ada Sub-Episode B sesudahnya. | Title card dipindah ke frame terakhir Sub-Episode B (10B, 15B, 20B, 25B, 30B). Frame A yang lama diubah menjadi shot biasa. |
| 13 | Dua rekan regu tidak bernama dan tidak punya desain, sehingga wajah mereka akan berubah tiap frame. | Diberi nama dan anchor: **Aila** (pengintai angin) dan **Dhruva** (penjaga perisai). Setiap frame yang menyebut regu otomatis membawa anchor keduanya. |
| 14 | Kain sarung "terurai jadi jaring" di Ep 18 tanpa pernah kembali ke pinggang. | Frame 18B.1a dan 18B.1b menenun kembali kain sarung ke pinggang Gala. |
| 15 | Uji coba komik di Gemini: gaya berganti-ganti 3D dan 2D, latar berubah antarhalaman, tokoh pendukung berubah wajah. | Versi 3.1: (a) gaya dikunci sebagai render 3D CGI dan pemicu gaya 2D dilarang di setiap prompt; (b) setiap act dipetakan ke salah satu dari 68 lokasi, dan deskripsinya masuk otomatis sebagai baris `Setting:`; (c) 38 tokoh pendukung dan unit musuh mendapat anchor yang masuk otomatis ke prompt saat namanya muncul di adegan; (d) perpustakaan lembar referensi dan kit per episode. |

**Hitungan riil saat ini:** {counts}

---

## 2. Standar Struktur Cerita

| Level | Unit | Jumlah | Fungsi |
|---|---|---|---|
| 1 | Season | 10 | Tema besar dan musuh utama |
| 2 | Arc | 3 per season | Konflik babak |
| 3 | Episode | 5 per arc (15 per season) | Satu cerita utuh |
| 4 | Sub-Episode | 2 per episode (A setup, B payoff) | Paruh episode |
| 5 | Act | 2 per sub-episode | Adegan besar |
| 6 | Sub-Act / Storyboard Frame | 4 per act | Satu shot + prompt AI |

Satu episode penuh = 16 frame. Satu season penuh = 240 frame. Sepuluh season = 2.400 frame.

> Catatan: rancangan awal menyebut 2 Sub-Act per Act, tetapi semua naskah yang sudah jadi memakai 4. Standar ini mengikuti naskah.

**Format kode frame:** `[Episode][Sub-Episode].[Act][Sub-Act]`. Contoh: `2B.1c` = Episode 2, Sub-Episode B, Act 1, Sub-Act c.

---

## 3. Character Anchor dan Aturan Konsistensi

### 3.1 Gala Ignis

| Elemen | Detail terkunci |
|---|---|
| Rambut | Ungu gelap, spiky |
| Mata | Selalu tertutup dark tactical goggles. Mata tidak pernah terlihat |
| Kaos | Hijau taktis (base layer) |
| Armor | Pelat ungu dengan ukiran batik emas di dada, bahu, lengan bawah |
| Tangan | Gauntlet kombinasi hijau-ungu |
| Pinggang | Kain sarung batik cokelat, diikat di pinggang di atas celana |
| Celana | Hitam |
| Sepatu | Boots kombinasi hijau-ungu |
| Gaya | 3D chibi, stylized animated film |

**Versi desain**

- **v1** (Ep 1 sampai frame 15A.2b): anchor dasar.
- **v2** (mulai frame 15A.2c): tambah pin lambang Galians emas kecil di pelat dada kiri.

**Anchor v1 (bahasa Inggris, siap tempel):**

```text
{gala_v1}
```

**Anchor v2:**

```text
{gala_v2}
```

### 3.2 Ethylene (Fire Sprite)

Wujud Ethylene dikunci mengikuti lembar referensi K03 final: bola kuning keemasan mengilap tanpa mulut.

```text
{sprite}
```

### 3.3 Regu Gala dan Tokoh Season 3

Palet tiap karakter sengaja dibuat berjauhan supaya model AI tidak mencampur desain mereka: Gala ungu-hijau-emas, Aila toska-perak, Dhruva merah karat-perunggu, Kalia nila-kuningan.

| Nama | Asal nama | Peran | Debut |
|---|---|---|---|
| **Aila** | Usulanmu. Dalam tradisi Sanskerta, *Aila* berarti "keturunan Ilā", sebutan untuk Raja Pururawa. [Medium confidence: bentuk katanya benar, tetapi perlu verifikasi kamus] | Pengintai, pengendali angin, peretas terminal | Ep 5 (tanpa nama), dinamai di bible ini |
| **Dhruva** | Sanskerta *dhruva*: teguh, tak tergoyahkan; juga nama bintang kutub. [High confidence] | Penjaga perisai, tameng regu | Ep 5 (tanpa nama), dinamai di bible ini |
| **Kalia** | Diturunkan dari Sanskerta *kāla*: waktu. [High confidence untuk *kāla*; ejaan "Kalia" adalah turunan kita.] Catatan: dalam budaya Jawa ada Batara Kala, sang pemangsa waktu. Karena temanya waktu, konotasi itu bisa jadi lapisan makna, tetapi perlu disadari | Pemimpin kelompok perlawanan di lini masa paralel | Ep 33 |

Nama "Kar-Imun" dan "Agia" tidak saya pakai karena saya tidak menemukan dasar Sanskertanya [Low confidence bahwa keduanya kata Sanskerta].

```text
{aila}
```

```text
{dhruva}
```

```text
{kalia}
```

**Wirasena** (Season 4). Dua versi: bertopeng sampai 50A.2d, tanpa topeng mulai 50B.1a.

```text
{wira_m}
```

```text
{wira_v}
```

**Maheswari** (Kepala Dewan Tinggi, Season 4 dan seterusnya).

```text
{mahes}
```

**Indra Mahadana** (CEO Vextron, Season 5).

```text
{indra}
```

**Tokoh Season 6 sampai 10.** Anchor lengkap mereka ada di bawah ini dan otomatis masuk ke setiap prompt yang memuat tokoh tersebut.

{extra_anchor_list}

**Gala Bayang** (Gala dari lini masa paralel). Hanya tampil sebagai siluet di dalam kristal sampai 44B; anchor ini dipakai mulai 44B.1b. Rambut putih abu, goggles retak, dan tidak adanya zirah atau batik sengaja dipilih supaya AI tidak tertukar dengan Gala utama.

```text
{bayang}
```

### 3.4 Aturan Konsistensi (berlaku di semua prompt)

```text
{lock}
{squad_lock}
{neg}
```

Aturan menulis prompt baru:

1. Selalu tempel anchor lengkap, jangan diringkas jadi "Gala in his usual outfit".
2. Jangan menulis kata mata ("eyes", "looking with wide eyes"). Pakai alis, mulut, bahu, dan pantulan di lensa.
3. Kerusakan tempur (kaos sobek, armor retak, kain gosong) ditulis eksplisit di Scene dan hanya berlaku di frame itu.
4. Teks di layar (hologram, title card) ditulis dalam tanda kutip tunggal. Model gambar sering salah eja teks panjang; siapkan untuk dibetulkan manual di editing.
5. Untuk video, satu prompt = satu frame. Gerakan panjang lebih stabil dibuat dari beberapa frame pendek daripada satu prompt panjang.

---

## 4. Lore Ringkas

**Semesta:** Kota futuristik Nusantara yang memadukan nanoteknologi dengan motif batik sebagai struktur energi.

**Akademi dan Ordo Galians:** Akademi pelatihan prajurit penjaga energi atom. "Galians" juga dipakai sebagai nama fandom.

**Regu Vanguard:** Gala (api, penyerang), Aila (angin, pengintai), Dhruva (perisai, penjaga). Resmi menjadi satu regu di 15B.1a.

**Perlengkapan Gala**

| Item | Fungsi di cerita | Debut |
|---|---|---|
| Zirah nano-alloy ungu dengan batik emas | Menyalurkan plasma api; batik berpijar saat daya naik | Ep 1 |
| Dark tactical goggles + modul HUD | Memetakan struktur atom dan titik lemah target | Goggles Ep 1, HUD Ep 2 |
| Kain sarung batik nanoselulosa | Menyerap panas berlebih, grounding energi, jaring termal, konduktor daya | Ep 3 |
| Kaos hijau taktis | Base layer penahan benturan dan panas | Ep 1 |
| Boots hijau-ungu | Pendorong api (thruster), media tendangan | Ep 2 |

**Jurus**

| Jurus | Deskripsi | Debut |
|---|---|---|
| Atomic Fire Kick | Tendangan api presisi | Ep 2 |
| Galian Field | Perisai foton bermotif batik | Ep 3 |
| Atomic Palm Strike | Serangan telapak jarak dekat | Ep 12 |
| Galian Atomic Buster Kick | Tendangan pusaran naga plasma | Ep 14 |
| High-Level Batik Resonance | Motif batik terangkat menjadi anyaman foton | Ep 28 |
| Galian Supreme Buster Kick | Bentuk puncak Buster | Ep 29 |
| Melepas Tenunan | Teknik mengurai tenunan Batik Terbalik benang demi benang, diajarkan Wirasena | Ep 68 |
| Buster Dua Nyala | Buster Gala + Ethylene dengan restu api Agni | Ep 89 |
| Buster Resonansi Emas | Tendangan ganda Gala dan Arka yang seirama | Ep 119 |
| Tenunan yang Memberi | Menenun segel dari cahaya yang diberikan sukarela | Ep 146 |
| Buster Era Baru | Tendangan ganda yang menutup jaring segel, bukan menghancurkan | Ep 148 |
| Buster Berjangkar | Buster dengan kain sarung ditambatkan ke jangkar waktu, kebal putar ulang | Ep 44 |

**Antagonis sejauh ini**

| Nama | Afiliasi | Nasib |
|---|---|---|
| Peretas misterius (siluet) | Nira, atas perintah Vikrama | Terungkap di Season 7 |
| Cryo-Drones, Cryo-Walker, Cryo-Berserker | Cryo-Tech (sayap militer Absolute Zero) | Unit massal |
| Jenderal Eksekutif Cryo-Tech | Cryo-Tech | Kalah di Ep 14 |
| Komandan Himakara | Cryo-Tech | Kalah di Ep 19 |
| Komandan Frostwing | Cryo-Tech | Kalah di Ep 24 |
| Lord Absolute Zero | Pemimpin Faksi Absolute Zero | Musnah di Ep 29 |
| Chrono-Wraith | Residu waktu di sekitar Gala Bayang (lini masa paralel) | Menyatu menjadi Penjaga di Ep 40 |
| Penjaga Cakrawala | Gabungan Chrono-Wraith | Hancur di Ep 44; Gala Bayang terbebas |
| Panglima Wirasena | Penenun pertama ordo leluhur | Dibebaskan di Ep 59; menjadi penjaga candi |
| Arca Penjaga, Laskar Purba | Dibangkitkan Batik Terbalik | Runtuh di Ep 59 |
| Indra Mahadana | CEO Vextron | Menyerahkan diri di Ep 75 |
| Vex-Core | AI jaringan Vex-Hub, dilatih dari tenunan Wirasena | Dihancurkan di Ep 74 |
| Sang Hampa | Sisi dingin Alam Nyala | Terurai di Ep 89 |
| Peretas Ep 4 (Nira) | Direkrut Vikrama | Terungkap di Ep 95; bergabung dengan Galians di Ep 105 |
| Wakil Dewan Vikrama | Dewan Tinggi, Garda Besi | Ditahan di Ep 105 |
| Komandan Taraka | Sisa Garda Besi | Ditangkap di Ep 119 |
| Sang Utusan | Pembawa pesan Katalis Entropi | Terurai di Ep 134 |
| Katalis Entropi | Entitas di bawah Jaring Nusantara | Ditidurkan oleh segel baru di Ep 148 |

---

## 5. Peta 10 Season

| Saga | Season | Judul | Musuh / Konflik utama | Status |
|---|---|---|---|---|
| I | 1 | Inisiasi Sang Galian | Retasan sinyal asing, Cryo-Tech | Lengkap (240 frame) |
| I | 2 | Ancaman Inti Atom | Faksi Absolute Zero | Lengkap (240 frame) |
| I | 3 | Paradoks Waktu (Chronos Horizon) | Retakan waktu, Chrono-Wraith, Penjaga Cakrawala | Lengkap (240 frame) |
| II | 4 | Bayangan Sang Purba | Panglima Wirasena, Batik Terbalik | Lengkap (240 frame) |
| II | 5 | Invasi Cyber-Nusantara | Vextron, Indra Mahadana, Vex-Core | Lengkap (240 frame) |
| II | 6 | Realm of Ethylene | Sang Hampa | Lengkap (240 frame) |
| III | 7 | Keretakan Aliansi | Wakil Dewan Vikrama, Garda Besi | Lengkap (240 frame) |
| III | 8 | Resonansi Emas | Komandan Taraka (Subjek Zero menjadi sekutu) | Lengkap (240 frame) |
| III | 9 | Gerhana Atom | Sang Utusan, gerhana entropi | Lengkap (240 frame) |
| III | 10 | Era Baru Galians | Katalis Entropi | Lengkap (240 frame) |

---
"""

S3 = open("s3_text.md").read()

BACKLOG = open("backlog.md").read()

def render(seasons, v2=False, headings=True):
    frame_total = 0
    body = []
    for sec_no, S in seasons:
        if headings:
            body.append(f"## {sec_no}. Season {S['n']}: {S['title']} ({S['en']})\n\n*{S['saga']}*\n\n{S['focus']}\n")
        for A in S["arcs"]:
            eps = A["eps"]
            body.append(f"### Season {S['n']} · Arc {A['n']}: {A['title']} ({A['en']})\n\nEpisode {eps[0]['n']} sampai {eps[-1]['n']}. {A['focus']}\n")
            for E in eps:
                body.append(f"### Episode {E['n']}: {E['title']}\n\n{E['focus']}\n")
                _blk, _aud = AS.episode_block(E)
                body.append(_blk)
                _eth = AS.eth_patch(E)
                ETH_ADDED.extend(_eth)
                for SE in E["subs"]:
                    body.append(f"#### Sub-Episode {SE['id']}: {SE['title']}\n")
                    for AC in SE["acts"]:
                        body.append(f"##### Act {AC['id']}: {AC['title']}\n")
                        for code, shot, vis, scene, flags in AC["frames"]:
                            if code in _eth:
                                code, shot, vis, scene, flags = _eth[code]
                            if code == V2_START:
                                v2 = True
                            frame_total += 1
                            body.append(f"**{code} · {shot}**\n\n{vis}\n\n```text\n{prompt(scene, flags, v2, code)}\n```\n")
        if headings:
            body.append("---\n")
    return frame_total, "\n".join(body)

SEASON_NOTE = ("> Bagian dari *Gala Ignis & The Galians: Master Story Bible*. Anchor karakter, aturan konsistensi, dan lore ada di "
               "`00-inti.md`. Setiap prompt di bawah sudah memuat anchor lengkap dan siap disalin.\n\n")

def season_file(text):
    lines = text.split("\n")
    lines[0] = re.sub(r"^## \d+\. ", "# ", lines[0])
    return lines[0] + "\n\n" + SEASON_NOTE + "\n".join(lines[1:])

if __name__ == "__main__":
    import os
    merge()
    out = "../docs"
    os.makedirs(out, exist_ok=True)
    counts = []
    for n, S, v2 in ((1, S1, False), (2, S2, False)):
        t, body = render([(n, S)], v2=(n == 2))
        body = re.sub(r"^## \d+\. Season", "# Season", body, count=1)
        first, rest = body.split("\n", 1)
        body = first + "\n\n" + SEASON_NOTE + rest
        open(f"{out}/season-0{n}.md", "w").write(body)
        counts.append(t)
    t3, body3 = render([(8, S3F)], v2=True, headings=False)
    open(f"{out}/season-03.md", "w").write(season_file(S3 + "\n## Storyboard\n\n" + body3))
    t4, body4 = render([(9, S4F)], v2=True, headings=False)
    open(f"{out}/season-04.md", "w").write(season_file(open("s4_text.md").read() + "\n## Storyboard\n\n" + body4))
    t5, body5 = render([(10, S5F)], v2=True, headings=False)
    open(f"{out}/season-05.md", "w").write(season_file(open("s5_text.md").read() + "\n## Storyboard\n\n" + body5))
    counts += [t3, t4, t5]
    for n, txt, SF in EXTRA:
        tn, bodyn = render([(n + 5, SF)], v2=True, headings=False)
        open(f"{out}/season-{n:02d}.md", "w").write(season_file(open(txt).read() + "\n## Storyboard\n\n" + bodyn))
        counts.append(tn)
    summary = "Season 1 sampai 10 = " + " + ".join(str(c) for c in counts) + f" = {sum(counts)} frame."
    head = (HEADER.replace("{counts}", summary).replace("{aila}", AILA).replace("{dhruva}", DHRUVA).replace("{kalia}", KALIA)
            .replace("{bayang}", GALA_BAYANG).replace("{wira_m}", WIRA_M).replace("{wira_v}", WIRA_V).replace("{mahes}", MAHESWARI).replace("{indra}", INDRA).replace("{extra_anchor_list}", "\n\n".join(f"```text\n{v}\n```" for v in EXTRA_ANCHORS.values()))
            .replace("{squad_lock}", SQUAD_LOCK).replace("{gala_v1}", GALA_V1).replace("{gala_v2}", GALA_V2)
            .replace("{sprite}", SPRITE).replace("{lock}", LOCK).replace("{neg}", NEG))
    open(f"{out}/00-inti.md", "w").write(head + "\n" + AS.RULES_MD + "\n" + BACKLOG.replace("## 10. Backlog", "## 7. Backlog"))
    print(counts, sum(counts), "ethylene ditambahkan:", len(ETH_ADDED))
