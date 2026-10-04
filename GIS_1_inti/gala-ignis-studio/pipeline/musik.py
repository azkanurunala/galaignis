"""Musik latar dan efek suara sintetis (tanpa berkas audio luar), mengikuti gaya Short Episode 1."""
import numpy as np
from scipy.signal import butter, lfilter

SR = 24000
NOTE = {"C": -9, "C#": -8, "D": -7, "Eb": -6, "E": -5, "F": -4, "F#": -3, "G": -2, "Ab": -1, "A": 0, "Bb": 1, "B": 2}
PROG = [[("D", 3), ("A", 3), ("F", 4)], [("Bb", 2), ("F", 3), ("D", 4)], [("G", 2), ("D", 3), ("Bb", 3)], [("A", 2), ("E", 3), ("C#", 4)]]
ROOT = [("D", 2), ("Bb", 1), ("G", 1), ("A", 1)]
BEAT = 60 / 92


def hz(n, o): return 440 * 2 ** ((NOTE[n] + 12 * (o - 4)) / 12)
def lpf(x, fc): b, a = butter(2, min(0.99, fc / (SR / 2))); return lfilter(b, a, x)
def hpf(x, fc): b, a = butter(2, fc / (SR / 2), "high"); return lfilter(b, a, x)


def env(n, a, r):
    e = np.ones(n); na = max(1, min(n, int(a * SR))); nr = max(1, min(n, int(r * SR)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] *= np.linspace(1, 0, nr); return e


def saw(f, n, det=(0,)):
    t = np.arange(n) / SR; return sum(2 * ((t * f * (1 + d)) % 1) - 1 for d in det) / len(det)


class Mix:
    def __init__(self, dur):
        self.n = int((dur + 1) * SR); self.m = np.zeros(self.n); self.rng = np.random.default_rng(11)

    def put(self, x, t0, g=1.0):
        i = max(0, int(t0 * SR)); j = min(self.n, i + len(x))
        if i < self.n:
            self.m[i:j] += g * x[:j - i]

    def pad(self, chord, t0, dur, g=0.14, fc=1300):
        n = int(dur * SR); x = sum(saw(hz(a, o), n, (-0.004, 0, 0.005)) for a, o in chord) / len(chord)
        self.put(lpf(x, fc) * env(n, 0.5, 0.5), t0, g)

    def low(self, note, t0, dur, g=0.18, fc=420):
        n = int(dur * SR); self.put(lpf(saw(hz(*note), n, (0, 0.003)), fc) * env(n, 0.005, dur * 0.6), t0, g)

    def timp(self, t0, g=0.6, f=52):
        n = int(1.4 * SR); t = np.arange(n) / SR
        x = np.sin(2 * np.pi * np.cumsum(f * (1 + 0.6 * np.exp(-t * 18))) / SR) * np.exp(-t * 2.8) + lpf(self.rng.standard_normal(n), 300) * np.exp(-t * 25) * 0.6
        self.put(x, t0, g)

    def brass(self, chord, t0, dur, g=0.3):
        n = int(dur * SR); x = sum(saw(hz(a, o), n, (-0.003, 0.003)) for a, o in chord) / len(chord)
        w = np.exp(-np.arange(n) / SR * 3)
        self.put((lpf(x, 3500) * w + lpf(x, 900) * (1 - w)) * env(n, 0.02, dur * 0.7), t0, g)

    def riser(self, t0, t1, g=0.22):
        n = int((t1 - t0) * SR)
        if n < SR // 4:
            return
        p = np.linspace(0, 1, n)
        self.put(0.5 * np.sin(2 * np.pi * np.cumsum(200 + 1400 * p ** 2) / SR) * p ** 2 + 0.6 * hpf(self.rng.standard_normal(n), 800) * p ** 3, t0, g)

    def pop(self, t0, g=0.16):
        n = int(0.09 * SR); t = np.arange(n) / SR
        self.put(np.sin(2 * np.pi * np.cumsum(500 + 900 * np.exp(-t * 60)) / SR) * np.exp(-t * 45), t0, g)

    def whoosh(self, t0, g=0.25):
        n = int(0.5 * SR); p = np.linspace(0, 1, n)
        self.put(hpf(self.rng.standard_normal(n), 500) * np.sin(np.pi * p) ** 2, t0, g)


def susun(klip, total):
    """klip: daftar (t_mulai, durasi, kuat 0..1, jenis). Mengembalikan musik float mono sepanjang total detik."""
    mx = Mix(total)
    frames = [k for k in klip if k[3] == "frame"]
    puncak = max(frames[len(frames) // 2:], key=lambda k: k[2]) if frames else None
    for i, (t, d, kuat, jenis) in enumerate(klip):
        ch = PROG[i % 4]
        mx.pad(ch, t, d + 0.4, 0.10 + 0.07 * kuat, 1100 + 900 * kuat)
        step = BEAT / 2 if kuat >= 0.35 else BEAT * 2
        tt = t
        while tt < t + d - 0.05:
            mx.low(ROOT[i % 4], tt, step * 0.8, 0.12 + 0.12 * kuat, 350 + 300 * kuat); tt += step
        if jenis == "buka":
            mx.riser(t, t + d, 0.25); mx.timp(t, 0.6)
            mx.timp(t + d, 0.8, 46); mx.brass([("D", 3), ("A", 3), ("D", 4), ("F", 4)], t + d, 2.4, 0.26)
        elif jenis == "tutup":
            mx.timp(t, 0.7, 46); mx.brass([("D", 2), ("A", 2), ("D", 3), ("F", 3)], t, min(d + 0.6, 2.6), 0.3)
        elif jenis == "frame":
            mx.pop(t + 0.06)
        if jenis == "frame" and kuat >= 0.5:
            mx.timp(t, 0.3 + 0.5 * kuat); mx.whoosh(max(0, t - 0.25), 0.12 + 0.15 * kuat)
        if puncak is not None and (t, d, kuat, jenis) == puncak and kuat >= 0.5:
            mx.riser(max(0, t - 2.0), t, 0.26); mx.brass([("D", 2), ("A", 2), ("D", 3), ("F", 3), ("A", 3)], t, 2.6, 0.34)
    return mx.m[:int(total * SR)]


def campur(suara, musik):
    """Mencampur jalur suara (kosong bila tanpa narator) dengan musik dan efek. Mengembalikan int16."""
    n = min(len(suara), len(musik)); v = suara[:n].astype(np.float64) / 32768; m = musik[:n]
    aktif = lpf((np.abs(v) > 0.01).astype(np.float64), 4)
    out = v * 1.0 + m * 0.75 * (1 - 0.6 * np.clip(aktif, 0, 1))
    pk = np.abs(out).max() or 1.0
    return (out / max(pk, 1.0) * 0.92 * 32767).astype(np.int16)
