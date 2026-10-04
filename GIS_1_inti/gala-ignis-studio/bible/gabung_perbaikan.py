"""Menggabungkan hasil perbaikan kesinambungan per season menjadi perbaikan.json. Dipakai sekali; disimpan sebagai catatan cara kerjanya."""
import json, re, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/fb3"
F = {}; Rg = {}; C = []
for n in range(1, 11):
    d = json.load(open(f"{SRC}/fix_{n:02d}.json", encoding="utf-8"))
    src = open(f"{SRC}/season_{n:02d}.txt", encoding="utf-8").read()
    for k, v in d.get("frames", {}).items():
        assert re.search(r"^" + re.escape(k) + r" \|", src, re.M), k
        s = json.dumps(v, ensure_ascii=False)
        assert "—" not in s and "…" not in s, k
        assert set(v) >= {"shot", "id", "en", "flags"}, k
        F[k] = [v["shot"], v["id"], v["en"], v["flags"]]
    for k, v in d.get("ringkasan", {}).items():
        Rg[str(int(k))] = v
    C += d.get("catatan", [])

# Dua usulan ditolak penyunting utama: keduanya mengubah inti cerita.
for k in ("27A.1b", "27A.1c", "27A.1d", "27A.2b", "27A.2c", "27B.2d", "45A.2b"):
    F.pop(k, None)
Rg.pop("27", None); Rg.pop("45", None)
F["27A.2d"] = ["Medium Shot", "Pintu singgasana tampak di ujung aula, tetapi Gala berbalik mencari regunya.",
               "With the sprite back at his shoulder, Gala sees a giant dark door at the end of the hall, but turns back to look for Aila and Dhruva.", "GS"]
C = [c for c in C if not ((c["episode"] == 27 and c["frame"] == "27A.1b") or c["frame"] == "45A.2b")]
C.append({"episode": 27, "frame": "27A.1b", "frame_diubah": [],
          "tindakan": "Tidak diubah: episode 27 memang tentang Ethylene yang membeku lalu hidup kembali, jadi kehadirannya benar. Catatan plot yang menyebut ia absen keliru dan sudah dibetulkan."})
C.append({"episode": 45, "frame": "45A.2b", "frame_diubah": [],
          "tindakan": "Tidak diubah: hanya beberapa menit berlalu adalah inti paradoks waktu season ini dan judul sub-episodenya. Kalau adegan lini masa utama di episode 42 terasa terlalu panjang, yang dipadatkan adalah episode 42."})
json.dump({"frames": F, "ringkasan": Rg, "catatan": sorted(C, key=lambda c: c["episode"])},
          open("perbaikan.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "frame,", list(Rg), "ringkasan,", len(C), "catatan")
