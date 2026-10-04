"""Semua panggilan ke Vertex AI lewat SDK google-genai. Mode tiruan (GALA_MOCK=1) tidak memanggil apa pun."""
import io, json, os, sys, time, hashlib, textwrap
from PIL import Image, ImageDraw
from .common import CFG, log, mock, usage

_client = None


def client():
    global _client
    if _client is None:
        from google import genai
        project = os.environ.get("GOOGLE_CLOUD_PROJECT") or CFG["vertex"]["project"]
        if not project:
            sys.exit("Project Google Cloud belum diisi. Isi vertex.project di config.yaml atau set GOOGLE_CLOUD_PROJECT.")
        _client = genai.Client(vertexai=True, project=project, location=CFG["vertex"]["location"], credentials=_gcloud_creds())
    return _client


def _gcloud_creds():
    """Kalau GALA_GCLOUD_ACCOUNT diisi, token diambil dari akun gcloud itu (tanpa ADC, akun aktif gcloud tidak diubah)."""
    acc = os.environ.get("GALA_GCLOUD_ACCOUNT")
    if not acc:
        return None  # pakai ADC
    import datetime, subprocess
    from google.auth import credentials

    class Gcloud(credentials.Credentials):
        def __init__(self):
            super().__init__(); self._quota_project_id = os.environ.get("GOOGLE_CLOUD_PROJECT") or CFG["vertex"]["project"]

        def refresh(self, request):
            self.token = subprocess.check_output(f"gcloud auth print-access-token --account={acc}", shell=True, text=True).strip()
            self.expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=50)
    return Gcloud()


def _retry(fn, what):
    tries, jeda = CFG["retry"]["tries"], CFG["retry"]["jeda"]
    for i in range(tries):
        try:
            return fn()
        except Exception as e:  # kuota, jaringan, jawaban kosong
            if i == tries - 1:
                raise
            log(f"  {what} gagal ({type(e).__name__}: {str(e)[:160]}), coba lagi {i + 2}/{tries}")
            time.sleep(jeda * (2 ** i))


def _part(img):
    from google.genai import types
    if not isinstance(img, Image.Image):
        img = Image.open(img)
    img = img.convert("RGB"); m = CFG["panel"]["ref_max_side"]
    if max(img.size) > m:
        img.thumbnail((m, m), Image.LANCZOS)
    b = io.BytesIO(); img.save(b, "JPEG", quality=92)
    return types.Part.from_bytes(data=b.getvalue(), mime_type="image/jpeg")


def _mock_image(prompt, aspect):
    a, b = (int(x) for x in aspect.split(":")); w = 864; h = w * b // a
    hh = int(hashlib.md5(prompt.encode()).hexdigest()[:6], 16)
    base = (60 + hh % 90, 50 + (hh >> 8) % 70, 70 + (hh >> 16) % 90)
    img = Image.new("RGB", (w, h), base); d = ImageDraw.Draw(img)
    for y in range(0, h, 4):
        d.line([(0, y), (w, y)], fill=tuple(min(255, c + y * 60 // h) for c in base))
    d.ellipse([w * .3, h * .3, w * .7, h * .62], fill=(240, 180, 70))
    d.multiline_text((30, 30), "TIRUAN\n" + "\n".join(textwrap.wrap(prompt[-260:], 46)), fill=(255, 255, 255))
    return img


def gen_image(prompt, refs=(), aspect=None):
    aspect = aspect or CFG["panel"]["aspect"]
    usage("gambar")
    if mock():
        return _mock_image(prompt, aspect)
    from google.genai import types
    cfg = types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"], image_config=types.ImageConfig(aspect_ratio=aspect))

    def call():
        r = client().models.generate_content(model=CFG["models"]["image"], contents=[_part(x) for x in refs] + [prompt], config=cfg)
        for c in r.candidates or []:
            for p in (c.content.parts if c.content else []) or []:
                if p.inline_data and p.inline_data.data:
                    return Image.open(io.BytesIO(p.inline_data.data)).convert("RGB")
        raise RuntimeError("model tidak mengembalikan gambar: " + str(getattr(r, "text", "") or getattr(r, "prompt_feedback", ""))[:200])
    return _retry(call, "gambar")


def gen_json(prompt, images=(), model=None, temperature=0.4, mock_value=None):
    usage("teks")
    if mock():
        return mock_value() if callable(mock_value) else mock_value
    from google.genai import types
    cfg = types.GenerateContentConfig(response_mime_type="application/json", temperature=temperature)

    def call():
        r = client().models.generate_content(model=model or CFG["models"]["text"], contents=[_part(x) for x in images] + [prompt], config=cfg)
        t = (r.text or "").strip()
        if t.startswith("```"):
            t = t.strip("`"); t = t[t.index("\n") + 1:] if "\n" in t else t
        return json.loads(t)
    return _retry(call, "teks")


def tts(text):
    """Mengembalikan (pcm 16-bit mono, rate)."""
    usage("suara")
    if mock():
        import numpy as np
        rate = 24000; k = int(rate * max(1.2, len(text.split()) * 0.36))
        return (np.sin(np.arange(k) * 2 * np.pi * 220 / rate) * 1500).astype(np.int16).tobytes(), rate
    from google.genai import types
    cfg = types.GenerateContentConfig(response_modalities=["AUDIO"], speech_config=types.SpeechConfig(
        voice_config=types.VoiceConfig(prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=CFG["video"]["suara"]))))

    def call():
        r = client().models.generate_content(model=CFG["models"]["tts"], contents="Bacakan dengan hangat dan jelas untuk anak-anak, dalam bahasa Indonesia: " + text, config=cfg)
        p = r.candidates[0].content.parts[0].inline_data
        rate = 24000
        if p.mime_type and "rate=" in p.mime_type:
            rate = int(p.mime_type.split("rate=")[1].split(";")[0])
        return p.data, rate
    return _retry(call, "suara")


def gen_video(prompt, image, out_path):
    """Image-to-video (Veo) 9:16. Menunggu sampai operasi selesai lalu menyimpan MP4."""
    usage("video")
    from google.genai import types
    b = io.BytesIO(); image.convert("RGB").save(b, "PNG")
    cfg = types.GenerateVideosConfig(aspect_ratio="9:16", number_of_videos=1, duration_seconds=CFG["video"].get("veo_detik", 6), generate_audio=False)
    op = client().models.generate_videos(model=CFG["models"]["video"], prompt=prompt,
                                         image=types.Image(image_bytes=b.getvalue(), mime_type="image/png"), config=cfg)
    for _ in range(80):
        if op.done:
            break
        time.sleep(15); op = client().operations.get(op)
    if not op.done:
        raise RuntimeError("operasi video belum selesai setelah 20 menit")
    res = op.response or op.result
    vids = getattr(res, "generated_videos", None) or []
    if not vids or not vids[0].video or not vids[0].video.video_bytes:
        raise RuntimeError("model tidak mengembalikan video: " + str(getattr(op, "error", ""))[:200])
    open(out_path, "wb").write(vids[0].video.video_bytes)


def doctor():
    c = client()
    log("Project:", c._api_client.project if hasattr(c, "_api_client") else "?", "| lokasi:", CFG["vertex"]["location"])
    names = []
    try:
        names = sorted(m.name.split("/")[-1] for m in c.models.list())
        log("Model yang terlihat:", len(names))
        for n in names:
            if any(k in n for k in ("image", "tts", "gemini")):
                print("   ", n)
    except Exception as e:
        log("Tidak bisa mendaftar model:", str(e)[:200])
    for kind, mid in CFG["models"].items():
        ok = "ada" if mid in names else ("tidak terlihat di daftar" if names else "tidak bisa dicek")
        log(f"  models.{kind} = {mid}: {ok}")
    try:
        r = gen_json('Balas dengan JSON {"ok": true}')
        log("Uji teks:", r)
        img = gen_image("A small glossy amber fire sprite orb with a flame crown, 3D CGI render, plain background. No text.", aspect="1:1")
        log("Uji gambar: berhasil, ukuran", img.size)
    except Exception as e:
        log("UJI GAGAL:", str(e)[:400])
