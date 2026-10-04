"""Status dan pemeriksaan data. Menulis out/STATUS.md."""
import re
from .common import ROOT, OUT, log, episodes, ep_dir, load_refs, read_json, frames_final
from . import stage_refs


def periksa_data():
    """Cek keutuhan data tanpa memanggil model. Jalankan setelah mengubah bible."""
    eps = episodes(); refs = load_refs(); masalah = []
    if len(eps) != 150:
        masalah.append(f"jumlah episode {len(eps)}, seharusnya 150")
    kode_all = set()
    for n, e in eps.items():
        fr = [f for s in e["subs"] for f in s["frames"]]
        if len(fr) != 16:
            masalah.append(f"ep {n}: {len(fr)} frame")
        ks = {f["kode"] for f in fr}; kode_all |= ks
        g = e["gagal"]; c = g.get("sebelum") or g.get("frame")
        if c not in ks:
            masalah.append(f"ep {n}: kode ketukan gagal {c} tidak ada")
        if e["pembuka"] and e["pembuka"] not in ks:
            masalah.append(f"ep {n}: frame pembuka {e['pembuka']} tidak ada")
        for f in fr:
            for k in f["tokoh"] + ([f["latar"]] if f["latar"] else []):
                if k not in refs:
                    masalah.append(f"{f['kode']}: referensi {k} tidak dikenal")
            if "—" in f["id"] or "Scene: " not in f["prompt"] or " Rendering style:" not in f["prompt"]:
                masalah.append(f"{f['kode']}: teks atau prompt tidak sesuai format")
    for k, r in refs.items():
        if r["lolos"] and not (r["file"] and (ROOT / r["file"]).exists()):
            masalah.append(f"referensi {k} ditandai lolos tetapi berkasnya tidak ada")
    siap = sum(1 for r in refs.values() if r["lolos"])
    log(f"Data: {len(eps)} episode, {len(kode_all)} frame, {siap}/{len(refs)} referensi siap.")
    for m in masalah[:40]:
        log("  MASALAH:", m)
    log("Periksa data:", "lolos" if not masalah else f"{len(masalah)} masalah")
    return not masalah


def status(eps):
    rows = []; semua = True; tinjau = []
    for n in eps:
        d = ep_dir(n); e = episodes()[n]
        naskah = read_json(d / "naskah.json", {}); meta = read_json(d / "panel.json", {}); vid = read_json(d / "video.json", {})
        subs = frames_final(n); fr = [f for s in subs for f in s["frames"]]
        ok = [f["kode"] for f in fr if meta.get(f["kode"], {}).get("lolos") and (d / "panel" / f"{f['kode']}.png").exists()]
        bad = [f["kode"] for f in fr if f["kode"] not in ok]
        nq = naskah.get("qc", {}).get("lolos")
        vq = [s["id"] for s in subs if vid.get(s["id"], {}).get("lolos") and (d / f"GalaIgnis_Ep{n:03d}{s['id'][-1]}.mp4").exists()]
        kurang = stage_refs.missing([n])
        selesai = bool(nq) and not bad and len(vq) == len(subs)
        semua &= selesai
        rows.append(f"| {n} | {e['judul']} | {'siap' if not kurang else 'kurang ' + ', '.join(kurang)} | {'lolos' if nq else ('tinjau' if naskah else 'belum')} | {len(ok)}/{len(fr)} | {len(vq)}/{len(subs)} | {'SELESAI' if selesai else ''} |")
        if naskah and not nq:
            tinjau.append(f"- Ep {n} naskah: " + "; ".join(naskah.get("qc", {}).get("masalah", []))[:300])
        for k in bad:
            if k in meta:
                tinjau.append(f"- {k}: " + "; ".join(map(str, meta[k].get("masalah", [])))[:300] + f" (lihat out/ep{n:03d}/kontak_{k.split('.')[0]}.png)")
        for s in subs:
            v = vid.get(s["id"])
            if v and not v.get("lolos"):
                tinjau.append(f"- Video {s['id']}: " + "; ".join(v.get("masalah", []) + ([f"panel gagal {v['panel_gagal']}"] if v.get("panel_gagal") else [])))
    u = read_json(OUT / "pemakaian.json", {})
    txt = ["# Status produksi", "", f"Pemakaian model sejauh ini: {u.get('gambar', 0)} gambar, {u.get('teks', 0)} panggilan teks, {u.get('suara', 0)} suara.", "",
           "| Ep | Judul | Referensi | Naskah | Panel lolos | Video lolos | |", "|---|---|---|---|---|---|---|"] + rows
    if tinjau:
        txt += ["", "## Perlu ditinjau manusia", ""] + tinjau
    OUT.mkdir(exist_ok=True); (OUT / "STATUS.md").write_text("\n".join(txt) + "\n", encoding="utf-8")
    done = sum(1 for r in rows if "SELESAI" in r)
    log(f"Status: {done}/{len(eps)} episode selesai, {len(tinjau)} butir perlu ditinjau. Rincian di out/STATUS.md")
    return semua


def pindai():
    """Memindai seluruh 150 episode dan menulis apa yang masih bolong beserta langkah berikutnya (out/PINDAI.md dan PINDAI.json)."""
    eps = episodes(); hasil = []; refs = load_refs()
    for n in sorted(eps):
        e = eps[n]; d = OUT / f"ep{n:03d}"
        naskah = read_json(d / "naskah.json", {}); meta = read_json(d / "panel.json", {}); vid = read_json(d / "video.json", {})
        kurang = stage_refs.missing([n], refs)
        tinjau_ref = [k for k in kurang if refs[k].get("sumber") == "auto" and refs[k]["file"]]
        fr = [f["kode"] for s in e["subs"] for f in s["frames"]]
        if naskah.get("gagal") and e["gagal"]["status"] == "tambah":
            fr.append("g")
        ada = [k for k in meta if (d / "panel" / f"{k}.png").exists()]
        lolos = [k for k in ada if meta[k].get("lolos")]; gagal = [k for k in ada if not meta[k].get("lolos")]
        vok = [k for k, v in vid.items() if v.get("lolos") and (d / f"GalaIgnis_Ep{n:03d}{k[-1]}.mp4").exists()]
        if len(vok) == len(e["subs"]):
            st, aksi = "selesai", ""
        elif tinjau_ref:
            st, aksi = "tinjau", "lihat sheet " + ", ".join(tinjau_ref) + " di refs/auto, lalu setujui atau buat ulang"
        elif naskah and not naskah.get("qc", {}).get("lolos"):
            st, aksi = "tinjau", f"perbaiki out/ep{n:03d}/naskah.json lalu set qc.lolos true"
        elif gagal:
            st, aksi = "tinjau", "lihat kontak, lalu: python run.py ulang " + " ".join(gagal[:6]) + ' --catatan "..."'
        elif any(v and not v.get("lolos") for v in vid.values()):
            st, aksi = "tinjau", "video gagal QC: " + "; ".join(m for v in vid.values() for m in v.get("masalah", []))[:160]
        elif not naskah and not ada:
            st, aksi = "belum", f"python run.py semua -e {n}"
        else:
            st, aksi = "sebagian", f"python run.py semua -e {n}"
        hasil.append({"ep": n, "season": e["season"], "arc": e["arc"], "judul": e["judul"], "status": st, "aksi": aksi,
                      "referensi_kurang": kurang, "panel_lolos": len(lolos), "panel_total": len(fr), "video": len(vok)})
    from .common import write_json
    write_json(OUT / "PINDAI.json", hasil)
    hit = {k: sum(1 for h in hasil if h["status"] == k) for k in ("selesai", "sebagian", "tinjau", "belum")}
    ref_kurang = sorted({k for h in hasil for k in h["referensi_kurang"]})
    tunggu = stage_refs.menunggu(refs)
    txt = ["# Pindai seluruh seri", "", ("**Gerbang referensi TERBUKA.**" if not ref_kurang else f"**Gerbang referensi TERTUTUP: {len(ref_kurang)} referensi belum siap ({len(tunggu)} tinggal disetujui). Belum ada episode yang boleh dibuat.**"), "", f"Selesai {hit['selesai']} · sebagian {hit['sebagian']} · menunggu tinjauan {hit['tinjau']} · belum mulai {hit['belum']} (dari 150 episode, target 300 video).", "",
           f"Referensi yang belum siap: {len(ref_kurang)} ({', '.join(ref_kurang) or 'tidak ada'}).", ""]
    for s in range(1, 11):
        hs = [h for h in hasil if h["season"] == s]
        txt += [f"## Season {s}: {sum(1 for h in hs if h['status'] == 'selesai')}/{len(hs)} episode selesai", "", "| Ep | Arc | Judul | Status | Panel | Video | Langkah berikutnya |", "|---|---|---|---|---|---|---|"]
        txt += [f"| {h['ep']} | {h['arc']} | {h['judul']} | {h['status']} | {h['panel_lolos']}/{h['panel_total']} | {h['video']}/2 | {h['aksi']} |" for h in hs] + [""]
    (OUT / "PINDAI.md").write_text("\n".join(txt), encoding="utf-8")
    log(f"Pindai: selesai {hit['selesai']}, sebagian {hit['sebagian']}, menunggu tinjauan {hit['tinjau']}, belum {hit['belum']}. Rincian di out/PINDAI.md")
    return hasil
