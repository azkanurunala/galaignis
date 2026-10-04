import sys, time; sys.path.insert(0, '/home/claude/komik'); sys.path.insert(0, '/home/claude/models')
from reletter import *
from esrgan import upscale as U
S = '/home/claude/sheets/'
t0 = time.time()
# --- cover
c = U(Image.open(S+'E02_Sampul_final.png').convert('RGB'))
c = c.resize((1374, round(c.size[1]*1374/c.size[0])), Image.LANCZOS); c.save(S+'E02_Sampul_final_hq.png'); print('cover', c.size, round(time.time()-t0))
# --- page 1
img = reletter(S+'E02_Hal01_v1_687.png', '/tmp/hq1.png',
  bubbles=[((28,358,188,455), ['Chip pemindai','molekul. Pasang di','goggles-mu.']),
           ((552,358,662,465), ['Keren!','Tapi... ini','buat apa?']),
           ((432,728,618,842), ['Apimu meledak','karena kamu tidak','melihat apa yang','kamu bakar.'])],
  captions=[((26,22,200,100), ['Laboratorium','Teknologi Akademi.','Sisa waktu: 19 jam.'])],
  sfxs=[((358,482,414,520), 'KLIK', dict(size=62, angle=12, fill=(255,255,255)))], H=2060, up=U)
img = clean_margins(img)
img = inpaint(img, [('ell', ((364,351),(8,6))), ('ell', ((384,352),(6,5)))], r=4, dil=3)
img = glow_dots(img, [(365,351),(384,352)], 3.2); img.save(S+'E02_Hal01_final.png'); print('p1', round(time.time()-t0))
# --- page 2
img = reletter('/tmp/h2pre.png', '/tmp/hq2.png',
  bubbles=[((22,356,170,455), ['Ugh...','terlalu banyak...','kepalaku...']),
           ((226,700,390,795), ['Jangan lawan','datanya. Pilih satu','titik saja.'])],
  sfxs=[((494,372,572,412), 'BZZT!', dict(size=72, angle=-10, fill=(255,255,255), at=(1040,760))),
        ((550,392,632,438), 'BZZT!', dict(size=72, angle=-6, fill=(255,255,255), at=(1190,850)))], up=U)
bubble(img, (686, 566), ['Wah... semuanya kelihatan', 'sampai ke atomnya!'], tail=(575, 664))
img = clean_margins(img)
pg = Image.new('RGB', (1374, 2060), 'white'); pg.paste(img, (0, 6))
bubble(pg, (585, 1262), ['Pip?!'], size=32, tail=(676, 1205), pad=(22, 13)); pg.save(S+'E02_Hal02_final.png'); print('p2', round(time.time()-t0))
# --- page 3
E = '/home/claude/komik/e2p3/'
B = Image.open(E+'B.png').convert('RGB'); C = Image.open(E+'C.png').convert('RGB'); P4 = Image.open(E+'P4_nomouth.png').convert('RGB')
B = inpaint(B, [('ell', ((277,68),(38,28))), ('poly', [(234,104),(246,78),(265,84)])], dil=7)
B, info = erase_bubble(B, (360, 252, 450, 332))
capbox = caption_box(C, (20, 490, 140, 570))
B, C = U(B), U(C); K = 4
W = PAGE_W - 2*M; page = Image.new('RGB', (PAGE_W, PAGE_H), 'white')
pw = (W - G)//2; ph = round(pw*321/318)
def place(src_crop, w, h):
    iw, ih = w-2*BORDER, h-2*BORDER; sc = max(iw/src_crop[2], ih/src_crop[3])
    return lambda x, y: (BORDER + (x*K-src_crop[0])*sc - (src_crop[2]*sc-iw)/2, BORDER + (y*K-src_crop[1])*sc - (src_crop[3]*sc-ih)/2), sc
k4 = lambda t: tuple(v*K for v in t)
p1 = framed(B.crop(k4((24,21,334,334))), pw, ph); t1, s1 = place(k4((24,21,310,313)), pw, ph)
p2 = framed(B.crop(k4((354,21,664,334))), W-G-pw, ph); t2, s2 = place(k4((354,21,310,313)), W-G-pw, ph)
bubble(p1, t1(277, 68), ['Pip...'], tail=t1(290, 110), size=32)
text_block(p2, t2(*info['center']), ['Satu', 'titik...', 'oke.'], 30, 34, maxw=info['w']*K*s2*0.86)
h3 = round(W*238/659)
p3 = framed(C.crop(k4((17,345,670,577))), W, h3); t3, s3 = place(k4((17,345,653,232)), W, h3)
x0, y0 = t3(capbox[0], capbox[1]); x1, y1 = t3(capbox[2], capbox[3])
d = ImageDraw.Draw(p3); d.rectangle((x0, y0, x1, y1), fill='black'); d.rectangle((x0+3, y0+3, x1-3, y1-3), fill=(255,243,176))
text_block(p3, ((x0+x1)/2, (y0+y1)/2), ['Kena.'], 40, 40)
h4 = PAGE_H - 2*M - ph - h3 - 2*G
p4 = framed(P4, W, h4, 0.5, 0.5)
bubble(p4, (1150, 110), ['Bagus.', 'Sekarang ujian', 'sungguhan.'], tail=(1095, 225))
y = M
page.paste(p1, (M, y)); page.paste(p2, (M+pw+G, y)); y += ph + G
page.paste(p3, (M, y)); y += h3 + G
page.paste(p4, (M, y)); page.save(S+'E02_Hal03_final.png'); print('p3', round(time.time()-t0))
