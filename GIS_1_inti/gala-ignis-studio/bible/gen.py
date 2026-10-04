# Compact builders: frames are (shot, visual_id, scene_en, flags); codes are generated.
def E(n, title, focus, A, B):
    subs = []
    for X, (stitle, acts) in zip("AB", (A, B)):
        built = []
        for i, (atitle, frames) in enumerate(acts, 1):
            assert len(frames) == 4, (n, X, i)
            built.append({"id": f"{n}{X}.{i}", "title": atitle,
                          "frames": [(f"{n}{X}.{i}{c}",) + tuple(f) for c, f in zip("abcd", frames)]})
        assert len(built) == 2, (n, X)
        subs.append({"id": f"{n}{X}", "title": stitle, "acts": built})
    return {"n": n, "title": title, "focus": focus, "subs": subs}

def ARC(n, title, en, focus, eps):
    assert len(eps) == 5
    return {"n": n, "title": title, "en": en, "focus": focus, "eps": eps}
