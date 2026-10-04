# Per-panel prompts (no text in images; lettering done locally)
HEAD = ("Create a NEW single image, {ar}. This is ONE comic panel, not a page: no panel borders, no text, no letters, no speech bubbles, "
        "no captions, no sound-effect lettering.\nAttached references, in order: {refs}. Copy {what} EXACTLY from these references. "
        "Do not draw the sheets themselves, and do not reuse or edit any attached image as the canvas: paint a completely new picture.\nStyle: 3D CGI render like a still from a modern 3D animated feature film, identical to the last reference.")
G_SHORT = ("Gala: chibi boy with a big head, big spiky dark purple hair, dark goggles with fully opaque dark lenses always over his eyes, "
           "green shirt, purple armor with gold batik engravings, brown batik sash, black pants, green-and-purple boots, exactly as on sheet 1.")
E_SHORT = "Ethylene: the round glowing amber fire sprite from sheet 2, two white dot eyes, no mouth, small flame crown, tiny flame wisps on its sides."
REF = {"K01_final": "the Gala character sheet", "K03_final": "the Ethylene sheet", "L03_final": "the firing corridor environment sheet",
       "E02_Sampul_final": "the approved cover of this episode, same corridor, as the reference for rendering style and the look of the corridor and the red plasma spheres only (do not copy its pose)",
       "K30": "the instructors sheet, use ONLY the woman with the short black bob and round glasses",
       "L02_final": "the tech lab environment sheet"}
def P(ar, files, what, body, avoid):
    refs = "; ".join(f"{i+1}) {REF[f]}" for i, f in enumerate(files))
    return HEAD.format(ar=ar, refs=refs, what=what) + "\n" + body + "\nAvoid: " + avoid + "."
BASE_AV = "any text or letters, speech bubbles, panel borders, 2D illustration, anime style, cel shading, flat colors"
GAV = "goggles pushed up or removed, Gala's eyes visible, a pin or badge on Gala's chest, changed hair or armor colors, extra limbs, distorted hands"

PAGES = {}
PAGES[4] = dict(title="Halaman 4: Lorong Tembak", layout=("wide", "pair", "tall"), panels=[
 dict(files=["K01_final", "K03_final", "L03_final", "E02_Sampul_final"], ar="landscape 16:9",
      text=[("caption", "Lorong Tembak Akademi."), ("speaker", "Lima meriam. Jangan meledakkan apa pun.")],
      prompt=P("landscape 16:9", ["K01_final", "K03_final", "L03_final", "E02_Sampul_final"], "the characters and the corridor",
        "Scene: strong one-point perspective down the long dark firing corridor from sheet 3, dark gunmetal hexagon wall panels, orange guide lights along the floor edges. At the far end, five robotic plasma cannons in one row on the end wall, their muzzles charging with a red glow. Gala stands small in the lower left foreground, seen from behind, looking down the corridor; Ethylene hovers beside his shoulder.\n" + G_SHORT + "\n" + E_SHORT + "\nKeep the upper left and upper right corners as plain dark wall and ceiling.",
        BASE_AV + ", " + GAV + ", a mouth on the fire sprite, a bright or white room, a different number of cannons")),
 dict(files=["L03_final", "E02_Sampul_final"], ar="square 1:1",
      text=[("sfx", "WRRRM")],
      prompt=P("square 1:1", ["L03_final", "E02_Sampul_final"], "the corridor and the cannons",
        "Scene: dramatic low-angle close-up of the robotic plasma cannons on the end wall of the corridor, their dark metal barrels pointing at the camera, the muzzles glowing hot red and brighter at the centers as they charge, faint red heat haze and small sparks. No characters in this image.",
        BASE_AV + ", characters, people, a bright room")),
 dict(files=["K01_final", "K03_final", "L03_final", "E02_Sampul_final"], ar="square 1:1",
      text=[("gala", "Kali ini aku yang pegang kendali."), ("eth", "Pip!")],
      prompt=P("square 1:1", ["K01_final", "K03_final", "L03_final", "E02_Sampul_final"], "the characters and the corridor",
        "Scene: medium shot of Gala from the front, waist up, in the dark corridor lit by orange floor lights and a red glow from behind the camera. He smirks confidently, one gauntleted fist raised in front of his chest; his goggle lenses stay fully opaque and dark, with only a small red reflection on their surface. Ethylene bounces excitedly beside his head, trailing small sparks.\n" + G_SHORT + "\n" + E_SHORT + "\nKeep the top third of the image above their heads as plain dark corridor wall.",
        BASE_AV + ", " + GAV + ", a mouth on the fire sprite, eyes or pupils visible through the lenses")),
 dict(files=["L03_final", "E02_Sampul_final"], ar="landscape 3:2",
      text=[("sfx", "DZING! DZING! DZING!")],
      prompt=P("landscape 3:2", ["L03_final", "E02_Sampul_final"], "the corridor and the red plasma spheres",
        "Scene: three glowing red plasma spheres, like the red spheres on the cover, fired at the same moment from three of the five cannons at the far end, streaking down the dark corridor straight toward the camera with long bright motion-blur trails, the nearest one large in the foreground; orange floor lights streaking past. No characters in this image.",
        BASE_AV + ", characters, people, explosions, a bright room")),
])

REF["E02_Hal04_P4_raw"] = ("an approved panel of this episode, same corridor, as the reference for rendering style, lighting, "
                          "the corridor and the red plasma spheres only (do not copy its composition)")
HUD_SHORT = ("The goggle HUD look: thin glowing blue and green grid lines and small round scan nodes overlaid on the scene, a faint dark "
             "vignette at the edges like looking through goggle lenses, no readable text or numbers anywhere in the HUD.")
PAGES[5] = dict(title="Halaman 5: Titik Lemah", panels=[
 dict(files=["L03_final", "E02_Hal04_P4_raw"], text=[("caption", "Titik lemahnya... di situ.")],
      prompt=P("landscape 16:9", ["L03_final", "E02_Hal04_P4_raw"], "the corridor and the red plasma spheres",
        "Scene: first-person view through Gala's goggles, looking down the dark firing corridor: three glowing red plasma spheres rushing toward the viewer, a thin glowing predicted trajectory line drawn ahead of each one, and one small bright golden target dot locked onto each sphere. No characters and no body parts visible.\n" + HUD_SHORT,
        BASE_AV + ", numbers, HUD text, characters, people, hands, explosions, a bright room")),
 dict(files=["K01_final", "L03_final", "E02_Hal04_P4_raw"], text=[("gala", "Api... ke kaki!")],
      prompt=P("landscape 16:9", ["K01_final", "L03_final", "E02_Hal04_P4_raw"], "Gala and the corridor",
        "Scene: dramatic low-angle shot in the dark corridor. Gala plants his left foot firmly and channels power into his right boot; golden-orange flames wrap around his whole right leg and boot; his brown batik sash is blown backward by the heat; determined grin, fists clenched. Orange firelight on his armor and on the floor.\n" + G_SHORT + "\nKeep the upper right corner as plain dark corridor wall.",
        BASE_AV + ", " + GAV + ", the fire sprite, flames on the left leg, fire covering his face")),
 dict(files=["K01_final", "L03_final", "E02_Hal04_P4_raw"], text=[("sfx", "WHOOSH!")],
      prompt=P("landscape 3:2", ["K01_final", "L03_final", "E02_Hal04_P4_raw"], "Gala, the corridor and the red plasma spheres",
        "Scene: Gala mid-air in the dark corridor in a spinning pencak silat fire kick, body horizontal, his right leg sweeping a wide bright arc of golden-orange flame across the corridor toward three incoming red plasma spheres at the right side of the image. The flames reflect as small orange highlights on the surface of his opaque goggle lenses. Sparks and embers everywhere, dynamic motion.\n" + G_SHORT + "\nKeep the top quarter of the image as plain dark corridor ceiling.",
        BASE_AV + ", " + GAV + ", the fire sprite, explosions, spheres already destroyed")),
])

# --- Page 5 revision (24 Sep): camera direction fixed. Gala faces the cannons.
REF["L03_pintu"] = "the entrance end of the firing corridor (hazard-striped door with a wide display screen above it), which is what lies BEHIND Gala in this shot"
REF["E02_Hal04_P3_raw"] = "an approved panel of this episode showing how Gala is rendered and lit in this corridor (style reference only, do not copy its composition or background)"
PAGES[5]["panels"][1] = dict(files=["K01_final", "L03_pintu", "E02_Hal04_P3_raw"], text=[("gala", "Api... ke kaki!")],
  prompt=P("landscape 16:9", ["K01_final", "L03_pintu", "E02_Hal04_P3_raw"], "Gala and the corridor",
    "Camera direction: Gala faces the five cannons, and the cannons are BEHIND THE CAMERA, so they are NOT visible. The camera looks back toward the entrance end of the corridor: behind Gala we see exactly reference 2, the heavy door with yellow-and-black hazard stripes and the wide dark display screen above it, with orange floor lights leading to it. A red glow from the unseen cannons lights Gala's front.\n"
    "Scene: dramatic low-angle shot, Gala facing the camera. He plants his left foot and channels power into his RIGHT leg, which appears on the LEFT side of the image because he faces the camera: golden-orange flames wrap tightly around his right leg from the boot up to the knee, not spreading across the floor. His brown batik sash is blown backward by the heat; determined grin, fists clenched.\n" + G_SHORT + "\nKeep the upper right corner as plain dark corridor wall.",
    BASE_AV + ", " + GAV + ", cannons, the fire sprite, flames on his left leg, flames on the right side of the image, a fire on the floor, fire covering his face"))
PAGES[5]["panels"][2] = dict(files=["K01_final", "L03_final", "E02_Hal04_P4_raw"], text=[("sfx", "WHOOSH!")],
  prompt=P("landscape 3:2", ["K01_final", "L03_final", "E02_Hal04_P4_raw"], "Gala, the corridor and the red plasma spheres",
    "Camera direction: a pure side view, the camera looks straight at one side wall of the corridor. Behind Gala there is ONLY the dark hexagon side wall with its orange light strips; the end wall and the cannons are NOT visible (they are off-image to the right). The three red plasma spheres fly in from the right edge of the image.\n"
    "Scene: Gala mid-air in a spinning pencak silat fire kick, facing right, his right leg sweeping a wide bright arc of golden-orange flame to the right toward the three incoming red spheres. His goggle lenses stay dark and opaque with only a thin orange rim of reflected light. Sparks and embers, dynamic motion.\n" + G_SHORT + "\nKeep the top quarter of the image as plain dark corridor wall.",
    BASE_AV + ", " + GAV + ", cannons, the end wall of the corridor, a one-point perspective view down the corridor, glowing or fiery lenses, the fire sprite, explosions, spheres already destroyed"))

# --- Page 5 panel 3 revision 2: camera behind Gala looking down the corridor (Gemini keeps one-point perspective)
PAGES[5]["panels"][2] = dict(files=["K01_final", "L03_final", "E02_Hal04_P4_raw"], text=[("sfx", "WHOOSH!")],
  prompt=P("landscape 3:2", ["K01_final", "L03_final", "E02_Hal04_P4_raw"], "Gala, the corridor and the red plasma spheres",
    "Camera direction: the camera is BEHIND Gala and slightly below him, looking down the corridor toward the five cannons at the far end, like reference 3. Gala faces AWAY from the camera, toward the cannons.\n"
    "Scene: Gala mid-air in the foreground, seen in a three-quarter back view from behind his left side, in a spinning pencak silat fire kick aimed forward at the far end. The three glowing red plasma spheres come out of the cannons and fly down the corridor straight at him, in front of him, as in reference 3. His kicking leg sweeps a wide bright arc of golden-orange flame across the corridor right in the path of the three spheres, just before they hit. His back matches the back view on sheet 1: big spiky purple hair with the goggle strap around it, plain purple back plate, green sleeves, brown batik sash, black pants, green-and-purple boots. Sparks and embers, dynamic motion.\n"
    "Keep the top quarter of the image as plain dark corridor ceiling.",
    BASE_AV + ", " + GAV + ", Gala facing the camera, spheres coming from the side, spheres flying away from the camera, the fire sprite, explosions, spheres already destroyed"))

# --- Page 6: continuity locked: Gala faces the cannons; the burning/kicking leg is his LEFT leg.
REF["E02_Hal05_P3_raw"] = ("the previous panel of this episode (Gala's fire kick seen from behind), for continuity of camera side, "
                           "rendering style and lighting (paint the next moment, do not copy it)")
REF["E02_Hal05_P2_raw"] = ("an approved panel of this episode showing Gala in front of the entrance end of the corridor, for rendering "
                           "style, lighting and the background (do not copy his pose)")
PAGES[6] = dict(title="Halaman 6: Terbelah", panels=[
 dict(files=["K01_final", "L03_final", "E02_Hal05_P3_raw"], text=[("sfx", "SRAAAK!")],
      prompt=P("square 1:1", ["K01_final", "L03_final", "E02_Hal05_P3_raw"], "Gala, the corridor and the red plasma spheres",
        "Camera direction: exactly like reference 3, the camera is behind Gala looking down the corridor toward the five cannons at the far end; Gala is seen from behind in a three-quarter back view.\n"
        "Scene, the moment right after reference 3: Gala at the end of his spinning kick, his extended kicking leg on the LEFT side of the image, a huge glowing arc of golden-orange flame sweeping across the corridor. The arc has sliced all three red plasma spheres cleanly in half: six separated half-spheres drifting apart in the air, bright showers of golden sparks spraying along each clean cut. There is NO explosion, NO fireball and NO smoke cloud. His back matches sheet 1: big spiky purple hair with the goggle strap, plain purple back plate, green sleeves, brown batik sash, black pants, green-and-purple boots.\n"
        "Keep the top fifth of the image as plain dark corridor ceiling.",
        BASE_AV + ", " + GAV + ", explosions, fireballs, whole unbroken spheres, Gala facing the camera, the fire sprite")),
 dict(files=["K01_final", "L03_pintu", "E02_Hal05_P2_raw"], text=[],
      prompt=P("square 1:1", ["K01_final", "L03_pintu", "E02_Hal05_P2_raw"], "Gala and the corridor",
        "Camera direction: like reference 3, the camera is on the cannon side looking back toward the entrance end; behind Gala we see the hazard-striped door with the display screen above it, exactly as in reference 2. No cannons visible.\n"
        "Scene: low-angle shot of Gala landing in a three-point superhero landing facing the camera: one knee bent low, one fist planted on the floor, head up. Thin grey smoke curls up from the boot on the RIGHT side of the image, the same leg that burned in reference 3. Behind him, six red half-spheres fall apart and dissolve harmlessly into drifting golden sparks. Calm, no explosion.\n" + G_SHORT,
        BASE_AV + ", " + GAV + ", cannons, explosions, fire on his body, the fire sprite")),
 dict(files=["K01_final", "L03_pintu", "E02_Hal05_P2_raw"], text=[("gala", "...Nggak meledak?")],
      prompt=P("square 1:1", ["K01_final", "L03_pintu", "E02_Hal05_P2_raw"], "Gala and the corridor",
        "Camera direction: same as reference 3, the camera faces Gala from the cannon side, and behind him is the entrance end with the hazard-striped door. No cannons visible.\n"
        "Scene: medium close-up of Gala, still crouched, turning his head to look back over his shoulder toward the last golden sparks fading in the air behind him near the door. Surprised face: eyebrows raised high above his goggles, mouth slightly open. His goggle lenses stay fully opaque and dark.\n" + G_SHORT + "\nKeep the top third of the image as plain dark corridor wall.",
        BASE_AV + ", " + GAV + ", cannons, explosions, eyes visible through the lenses, the fire sprite")),
])

# --- Page 6 panel 4 (added 24 Sep): Ethylene merged into the fire kick and pops back out of the boot smoke.
REF["E02_Hal06_P2_raw"] = ("the previous panel of this episode (Gala after landing, thin smoke rising from his boot), for continuity of the boot, "
                           "the smoke, the corridor background, rendering style and lighting (do not copy its composition)")
PAGES[6]["panels"].append(dict(files=["K03_final", "K01_final", "E02_Hal06_P2_raw"], text=[("eth", "Pip!")],
  prompt=P("landscape 16:9", ["K03_final", "K01_final", "E02_Hal06_P2_raw"], "Ethylene, Gala's boot and the corridor",
    "Scene: floor-level close-up in the same dark corridor as reference 3, the hazard-striped door softly out of focus in the background. On the left third of the image, only Gala's green-and-purple combat boot and lower leg, with thin grey smoke curling up from it. In the middle, Ethylene pops out of that smoke with a tiny burst of golden sparks, shaking the smoke off like a wet puppy, cheerful. Ethylene: the round glowing amber fire sprite from sheet 1, two white dot eyes, no mouth, small flame crown, tiny flame wisps on its sides.\n"
    "Keep all the action inside the middle horizontal band of the image; the top and bottom fifths are plain dark wall and floor.",
    BASE_AV + ", a mouth on the fire sprite, Gala's face, a full figure of Gala, explosions, cannons")))
