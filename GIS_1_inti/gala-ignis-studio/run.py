#!/usr/bin/env python3
"""Gala Ignis Studio: dari bible sampai video komik, lewat Vertex AI. Lihat README.md."""
import argparse, os, sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("perintah", choices=["doctor", "data", "periksa", "refs", "naskah", "panel", "video", "semua", "status", "setujui", "ulang", "pindai", "lanjut", "tolak"])
    ap.add_argument("target", nargs="*", help="untuk setujui: kode referensi; untuk ulang: kode frame")
    ap.add_argument("--episode", "-e", default="1", help="contoh: 2  atau  1-15  atau  1,3,7-9")
    ap.add_argument("--paksa", action="store_true", help="buat ulang walau sudah ada")
    ap.add_argument("--tanpa-ref", action="store_true", help="lanjut walau referensi belum lolos")
    ap.add_argument("--izinkan-gagal", action="store_true", help="buat video walau ada panel yang belum lolos QC")
    ap.add_argument("--semua", action="store_true", help="untuk refs: buat semua referensi seluruh seri; untuk setujui: setujui semua yang lolos QC")
    ap.add_argument("--jumlah", type=int, default=1, help="untuk lanjut: berapa episode bolong yang dikerjakan")
    ap.add_argument("--catatan", default="", help="catatan sutradara untuk perintah ulang")
    ap.add_argument("--tiruan", action="store_true", help="uji alur tanpa memanggil Vertex AI")
    a = ap.parse_args()
    if a.tiruan:
        os.environ["GALA_MOCK"] = "1"
    from pipeline import common as C
    if a.perintah == "data":
        import subprocess
        for s in ("render.py", "export_data.py"):
            subprocess.run([sys.executable, s], cwd=C.ROOT / "bible", check=True)
        return
    if a.perintah == "doctor":
        from pipeline import vertex; return vertex.doctor()
    from pipeline import laporan
    if a.perintah == "periksa":
        sys.exit(0 if laporan.periksa_data() else 1)
    if a.perintah == "pindai":
        laporan.pindai(); return
    if a.perintah == "lanjut":
        antre = [h["ep"] for h in laporan.pindai() if h["status"] in ("sebagian", "belum")][:a.jumlah]
        if not antre:
            C.log("Tidak ada episode yang bisa dikerjakan otomatis. Lihat yang menunggu tinjauan di out/PINDAI.md."); return
        C.log("Dikerjakan:", antre); a.perintah = "semua"; a.episode = ",".join(map(str, antre))
    eps = C.parse_eps(a.episode)
    if a.perintah == "status":
        sys.exit(0 if laporan.status(eps) else 1)
    from pipeline import stage_refs
    if a.perintah == "setujui":
        r = C.load_refs(); kode = stage_refs.menunggu(r) if a.semua else a.target
        for k in kode:
            if k not in r or not r[k]["file"] or not (C.ROOT / r[k]["file"]).exists():
                sys.exit(f"{k}: belum ada berkas sheet")
            r[k]["lolos"] = True; r[k]["catatan"] = "Lolos, disetujui manusia"; C.log("Disetujui:", k, r[k]["file"])
        C.save_refs(r); stage_refs.kontak()
        C.log("Gerbang referensi:", "TERBUKA, produksi episode boleh dimulai" if stage_refs.gerbang() else f"masih tertutup, {len(stage_refs.missing(stage_refs.semua_episode()))} referensi belum siap")
        return
    if a.perintah == "tolak":
        r = C.load_refs()
        for k in a.target:
            if r.get(k, {}).get("sumber") != "auto":
                sys.exit(f"{k}: bukan sheet otomatis, tidak dihapus")
            (C.ROOT / r[k]["file"]).unlink(missing_ok=True); r[k].update(file=None, lolos=False, qc={}, catatan=r[k].get("catatan_asal") or "Belum ada")
            if a.catatan:
                r[k]["catatan_asal"] = "BELUM: " + a.catatan
            C.log("Ditolak, akan dibuat ulang:", k)
        C.save_refs(r); return
    if a.perintah == "refs" and a.semua:
        a.episode = "1-150"; eps = C.parse_eps(a.episode)
    wajib = C.CFG.get("produksi", {}).get("wajib_semua_referensi", True)
    if wajib and a.perintah in ("naskah", "panel", "video", "semua", "ulang") and not stage_refs.gerbang():
        kurang = stage_refs.missing(stage_refs.semua_episode()); tunggu = stage_refs.menunggu()
        C.log(f"Gerbang referensi tertutup: {len(kurang)} referensi belum siap ({len(tunggu)} di antaranya tinggal disetujui). Belum ada episode yang boleh dibuat.")
        if a.perintah == "semua":
            C.log("Membuat referensi yang kurang untuk seluruh seri dulu."); stage_refs.run(stage_refs.semua_episode())
        C.log("Langkah berikutnya: lihat refs/auto/KONTAK_*.png, lalu `python run.py setujui KODE ...` atau `setujui --semua`; yang salah `python run.py tolak KODE --catatan \"...\"` lalu `python run.py refs --semua`.")
        sys.exit(2)
    from pipeline import stage_refs, stage_script, stage_panels, stage_video
    if a.perintah == "ulang":
        import re
        for kode in a.target:
            n = int(re.match(r"\d+", kode).group()); p = C.ep_dir(n) / "panel.json"; m = C.read_json(p, {})
            m.setdefault(kode, {}); m[kode]["ulang"] = True
            if a.catatan:
                m[kode]["catatan_manual"] = a.catatan
            C.write_json(p, m); stage_panels.run(n, only=[kode], paksa=a.tanpa_ref)
            stage_video.run(n, force=True, izinkan_gagal=a.izinkan_gagal); laporan.status([n])
        return
    ok = True
    if a.perintah in ("refs", "semua"):
        ok &= stage_refs.run(eps, force=a.paksa and a.perintah == "refs")
    for n in eps:
        try:
            if a.perintah in ("naskah", "semua"):
                stage_script.run(n, force=a.paksa and a.perintah == "naskah")
            if a.perintah in ("panel", "semua"):
                if not C.read_json(C.ep_dir(n) / "naskah.json"):
                    stage_script.run(n)
                stage_panels.run(n, force=a.paksa and a.perintah == "panel", paksa=a.tanpa_ref)
            if a.perintah in ("video", "semua"):
                stage_video.run(n, force=a.paksa and a.perintah == "video", izinkan_gagal=a.izinkan_gagal)
        except KeyboardInterrupt:
            raise
        except Exception as e:  # satu episode gagal tidak menghentikan yang lain
            C.log(f"Ep {n} berhenti karena galat: {type(e).__name__}: {str(e)[:300]}"); ok = False
    if a.perintah in ("semua", "video", "panel"):
        ok &= laporan.status(eps); laporan.pindai()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
