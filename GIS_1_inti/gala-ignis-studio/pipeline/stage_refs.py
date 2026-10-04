"""Tahap referensi: membuat sheet tokoh dan latar yang belum ada atau belum lolos."""
from PIL import Image
from .common import CFG, ROOT, log, episodes, load_refs, save_refs
from . import vertex, qc


def needed(eps):
    out = []
    for n in eps:
        for sub in episodes()[n]["subs"]:
            for f in sub["frames"]:
                for k in f["tokoh"] + ([f["latar"]] if f["latar"] else []):
                    if k not in out:
                        out.append(k)
    return out


def missing(eps, refs=None):
    refs = refs or load_refs()
    return [k for k in needed(eps) if not (refs[k]["lolos"] and refs[k]["file"] and (ROOT / refs[k]["file"]).exists())]


def semua_episode():
    return sorted(episodes())


def menunggu(refs=None):
    """Sheet otomatis yang lolos QC model tetapi belum disetujui manusia."""
    refs = refs or load_refs()
    return [k for k, r in refs.items() if r.get("sumber") == "auto" and not r["lolos"] and r.get("qc", {}).get("lolos") and r["file"] and (ROOT / r["file"]).exists()]


def gerbang():
    """True kalau SEMUA referensi yang dipakai seri ini sudah lolos dan disetujui. Produksi episode menunggu ini."""
    return not missing(semua_episode())


def kontak():
    """Lembar kontak semua sheet otomatis, 12 per lembar, untuk ditinjau manusia."""
    from PIL import ImageDraw, ImageFont
    refs = load_refs(); items = [(k, r) for k, r in refs.items() if r.get("sumber") == "auto" and r["file"] and (ROOT / r["file"]).exists()]
    out = []; tw, th = 640, 360; font = ImageFont.load_default()
    for old in (ROOT / "refs/auto").glob("KONTAK_*.png"):
        old.unlink()
    for n in range(0, len(items), 12):
        part = items[n:n + 12]; rows = -(-len(part) // 3)
        sheet = Image.new("RGB", (3 * tw, rows * (th + 44)), (26, 20, 16)); dr = ImageDraw.Draw(sheet)
        for i, (k, r) in enumerate(part):
            x, y = (i % 3) * tw, (i // 3) * (th + 44)
            sheet.paste(Image.open(ROOT / r["file"]).convert("RGB").resize((tw - 8, th - 8)), (x + 4, y + 4))
            st = "DISETUJUI" if r["lolos"] else ("menunggu persetujuan" if r.get("qc", {}).get("lolos") else "GAGAL QC")
            if not r["lolos"]:
                dr.rectangle([x + 1, y + 1, x + tw - 2, y + th - 2], outline=(242, 169, 59) if r.get("qc", {}).get("lolos") else (230, 60, 40), width=4)
            dr.text((x + 8, y + th + 8), f"{k}  {r['nama']}  [{st}]", fill=(255, 240, 210), font=font)
        p = ROOT / f"refs/auto/KONTAK_{n // 12 + 1:02d}.png"; sheet.save(p); out.append(p)
    return out


def run(eps, force=False):
    refs = load_refs(); todo = needed(eps) if force else missing(eps, refs)
    todo = [k for k in todo if not (refs[k].get("sumber") != "auto" and refs[k]["lolos"])]  # jangan timpa sheet buatan tangan
    if not force:
        tunggu = set(menunggu(refs)); todo = [k for k in todo if k not in tunggu]         # sudah lolos QC, tinggal disetujui
    if not todo:
        log("Referensi: tidak ada yang perlu dibuat."); return not missing(eps)
    log(f"Referensi yang dibuat: {len(todo)} ({', '.join(todo)})")
    (ROOT / "refs/auto").mkdir(exist_ok=True)
    gaya_k = [Image.open(ROOT / refs[k]["file"]) for k in ("K01", "K03") if refs[k]["file"]]
    gaya_l = [Image.open(ROOT / refs[k]["file"]) for k in ("L01", "L02") if refs[k]["file"]]
    ok_all = True
    for k in todo:
        r = refs[k]; gaya = gaya_l if r["jenis"] == "latar" else gaya_k
        best = None; fix = ""
        for i in range(CFG["panel"]["max_attempts"]):
            p = ("The attached images are approved sheets from the same series. Match their 3D rendering style, materials and sheet layout exactly, "
                 "but do not copy their content and do not reuse them as the canvas.\n" + r["prompt_sheet"])
            if (r.get("catatan_asal") or r["catatan"]).startswith("BELUM"):
                p += "\nImportant correction from the previous rejected version: " + (r.get("catatan_asal") or r["catatan"]).split(":", 1)[-1].strip()
            if fix:
                p += "\nFix this problem from the previous attempt: " + fix
            img = vertex.gen_image(p, gaya, aspect="16:9")
            j = qc.juri_sheet(img, r, gaya)
            if best is None or (j["lolos"], j["skor"]) > (best[1]["lolos"], best[1]["skor"]):
                best = (img, j)
            if j["lolos"]:
                break
            fix = j["perbaikan"] or "; ".join(j["masalah"])
            log(f"  {k} percobaan {i + 1} gagal QC: {'; '.join(j['masalah'])[:160]}")
        img, j = best; path = f"refs/auto/{k}.png"; img.save(ROOT / path)
        asal = r.get("catatan_asal") or r["catatan"]
        r.update(file=path, lolos=False, sumber="auto", qc=j, catatan_asal=asal,
                 catatan="Lolos QC model, menunggu persetujuan manusia" if j["lolos"] else "GAGAL QC: " + "; ".join(j["masalah"])[:200])
        save_refs(refs); ok_all &= bool(j["lolos"])
        log(f"  {k} {r['nama']}: {'lolos QC, menunggu persetujuan' if j['lolos'] else 'GAGAL QC'} (skor {j['skor']})")
    kontak()
    return False
