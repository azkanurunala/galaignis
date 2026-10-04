import re, difflib
from antislop_data import *
ACTION = [("explos", 5), ("detonat", 5), ("impact", 5), ("mid-air", 5), ("buster", 5), ("kick", 4), ("clash", 4), ("strike", 4), ("slash", 4),
          ("shockwave", 4), ("action", 3), ("fast motion", 3), ("dynamic", 3), ("fire", 2), ("plasma", 2), ("charge", 2), ("crash", 4),
          ("shatter", 4), ("collaps", 4), ("burst", 3), ("duel", 3), ("attack", 3), ("lung", 3), ("dodg", 2), ("blast", 4), ("erupt", 4)]
STATIC = ("establishing", "wide atmospheric", "title card", "wide shot", "wide interior", "wide exterior")
def frames(E):
    return [f for SE in E["subs"] for AC in SE["acts"] for f in AC["frames"]]
def score(f):
    code, shot, vis, scene, flags = f
    t = (shot + " " + scene).lower(); s = sum(w for k, w in ACTION if k in t)
    if "G" in flags: s += 2
    if "title card" in t or "reading '" in t or "complete'" in t: s -= 6
    return s
def eth_patch(E):
    """Return {code: (code, shot, vis, scene, flags)} for frames where Ethylene is added beside Gala."""
    n = E["n"]; out = {}
    if n in ETH_SKIP_EPISODES: return out
    merged = False
    for f in frames(E):
        code, shot, vis, scene, flags = f
        low = (vis + " " + scene).lower()
        if n == 1 and code < "1B.1d": continue
        if "S" in flags:
            merged = any(k in low for k in ETH_MERGE)
            continue
        if any(k in low for k in ETH_MERGE) and ("ethylene" in low or "sprite" in low): merged = True
        if merged or "G" not in flags: continue
        if any(k in shot.lower() for k in ETH_SKIP_SHOT) or any(k in low for k in ETH_SKIP_TEXT): continue
        sl = shot.lower()
        if not any(k in sl for k in ETH_OK_SHOT) or any(k in sl for k in ETH_NO_SHOT): continue
        if 'close-up' in sl and 'medium close-up' not in sl: continue
        if "ethylene" in low or "sprite" in low: continue
        out[code] = (code, shot, vis.rstrip() + ETH_ADD_ID, scene.rstrip() + ETH_ADD_EN, flags + "S")
    return out
def audit(E):
    fr = frames(E); n = len(fr); first = fr[0]
    static_open = score(first) < 5
    best = max(fr, key=lambda f: (score(f), fr.index(f)))
    dups = []
    for i in range(n):
        for j in range(i+1, n):
            if difflib.SequenceMatcher(None, fr[i][3].lower(), fr[j][3].lower()).ratio() > 0.72: dups.append((fr[i][0], fr[j][0]))
    gala = [f for f in fr if "G" in f[4]]
    return dict(n=E["n"], static_open=static_open, first=first[0], open_shot=first[1], hook=best[0], hook_shot=best[1], hook_score=score(best),
                dups=dups, gala=len(gala), gala_eth=sum("S" in f[4] for f in gala), eth_added=len(eth_patch(E)))
from antislop_gagal import GAGAL, PEMBUKA2, MIRIP2

def episode_block(E):
    a = audit(E); kind, idea = GAGASAN[E["n"]]
    lines = [f"**Gagasan inti ({kind}):** {idea}"]
    if E["n"] in PEMBUKA2:
        lines.append(f"**Pembuka video:** mulai dengan frame {PEMBUKA2[E['n']][0]}. {PEMBUKA2[E['n']][1]}")
    elif a["static_open"] and a["hook"] != a["first"] and a["hook_score"] >= 5:
        lines.append(f"**Pembuka video:** mulai 1 sampai 2 detik dengan frame {a['hook']} ({a['hook_shot']}), baru masuk ke {a['first']}. Frame pertama berupa {a['open_shot']} yang tenang.")
    else:
        lines.append(f"**Pembuka video:** frame pertama ({a['first']}, {a['open_shot']}) sudah cukup kuat sebagai pembuka." if not a["static_open"]
                     else f"**Pembuka video:** episode ini tidak punya frame aksi yang jelas; pilih frame paling emosional saat adaptasi.")
    if a["dups"]:
        lines.append("**Frame mirip:** " + ", ".join(f"{x} dan {y}" for x, y in a["dups"]) + ". " + MIRIP2.get(E["n"], "Bedakan sudut kamera atau lebur saat adaptasi."))
    if E["n"] in MIRIP2 and not a["dups"]:
        lines.append("**Frame mirip:** " + MIRIP2[E["n"]])
    g = GAGAL[E["n"]]
    if g["status"] == "tambah":
        lines.append(f"**Ketukan gagal (rencana, belum jadi frame):** sisipkan sebelum {g['sebelum']}. {g['ketukan']}")
    else:
        lines.append(f"**Ketukan gagal:** sudah ada di frame {g['frame']}; cukup dipertegas saat adaptasi.")
    lines.append(f"**Rilis:** dua Short, sub-episode {E['n']}A lalu {E['n']}B. Short A ditutup tepat di ketukan yang menggantung.")
    if g.get("perpanjang"):
        lines.append(f"**Puncak arc, kandidat diperpanjang jadi tiga sub-episode:** {g['perpanjang']}")
    return "\n\n".join(lines) + "\n", a
