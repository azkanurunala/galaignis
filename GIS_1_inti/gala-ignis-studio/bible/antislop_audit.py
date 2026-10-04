import re, json, difflib
import render as R
R.merge()
SEASONS = [R.S1, R.S2, R.S3F, R.S4F, R.S5F] + [SF for n, txt, SF in R.EXTRA]
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
    if "title card" in t or "text" in t or "reading '" in t: s -= 6
    return s
def audit(E):
    fr = frames(E); n = len(fr)
    first = fr[0]; static_open = any(k in first[1].lower() for k in STATIC) or score(first) <= 1
    best = max(fr, key=lambda f: (score(f), fr.index(f) >= n//2))
    gala = [f for f in fr if "G" in f[4]]; withS = [f for f in gala if "S" in f[4]]
    anyS = any("S" in f[4] for f in fr)
    shots = [re.sub(r"\(.*?\)", "", f[1]).strip().lower() for f in fr]
    dup = 0
    for i in range(n):
        for j in range(i+1, n):
            if difflib.SequenceMatcher(None, fr[i][3].lower(), fr[j][3].lower()).ratio() > 0.72: dup += 1
    pov = sum("pov" in s or "first-person" in s for s in shots)
    return dict(n=E["n"], frames=n, static_open=static_open, open_shot=first[1], hook=best[0], hook_shot=best[1], hook_score=score(best),
                gala=len(gala), gala_with_eth=len(withS), any_eth=anyS, shot_kinds=len(set(shots)), dup=dup, pov=pov)
ALL = {}
for S in SEASONS:
    for A in S["arcs"]:
        for E in A["eps"]:
            ALL[E["n"]] = audit(E)
if __name__ == "__main__":
    a = list(ALL.values())
    print("episodes", len(a), "frames", sum(x["frames"] for x in a))
    print("static openings", sum(x["static_open"] for x in a))
    print("episodes with no Ethylene at all", sum(not x["any_eth"] for x in a))
    print("Gala frames", sum(x["gala"] for x in a), "with Ethylene", sum(x["gala_with_eth"] for x in a))
    print("episodes with near-duplicate frames", sum(x["dup"] > 0 for x in a), "total dup pairs", sum(x["dup"] for x in a))
    print("avg shot kinds", sum(x["shot_kinds"] for x in a)/len(a))
    print("hook in first frame", sum(x["hook"].endswith("A.1a") for x in a))
    for k in (2, 14, 29, 47, 59, 89, 104, 119, 148, 150): print(k, ALL[k]["open_shot"], "| hook", ALL[k]["hook"], ALL[k]["hook_shot"], ALL[k]["hook_score"], "| G/S", ALL[k]["gala"], ALL[k]["gala_with_eth"])
    json.dump(ALL, open("../out/audit.json", "w"))
