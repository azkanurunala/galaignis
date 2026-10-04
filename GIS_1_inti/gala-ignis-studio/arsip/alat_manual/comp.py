"""Shared comic page composition + lettering helpers (page scale 2x: 1374x2060)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, cv2, math
S = 4
BODY = '/home/claude/fonts/comic-neue-latin-700-normal.woff'
SFX = '/home/claude/fonts/bangers-latin-400-normal.woff'
PAGE_W, PAGE_H, M, G, BORDER = 1374, 2060, 24, 20, 4

def inpaint(img, polys, r=6, dil=5):
    a = cv2.cvtColor(np.asarray(img.convert('RGB')), cv2.COLOR_RGB2BGR)
    m = np.zeros(a.shape[:2], np.uint8)
    for kind, g in polys:
        if kind == 'ell': cv2.ellipse(m, g[0], g[1], 0, 0, 360, 255, -1)
        else: cv2.fillPoly(m, [np.array(g, np.int32)], 255)
    if dil: m = cv2.dilate(m, np.ones((dil, dil), np.uint8))
    out = cv2.inpaint(a, m, r, cv2.INPAINT_TELEA)
    return Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))

def glow_dots(img, centers, rad):
    """white glowing dot eyes (supersampled)"""
    K = 4
    ov = Image.new('RGBA', (img.size[0]*K, img.size[1]*K), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for cx, cy in centers:
        R = rad*2.2*K; d.ellipse((cx*K-R, cy*K-R, cx*K+R, cy*K+R), fill=(255, 220, 150, 110))
    ov = ov.filter(ImageFilter.GaussianBlur(rad*K))
    d = ImageDraw.Draw(ov)
    for cx, cy in centers:
        R = rad*K; d.ellipse((cx*K-R, cy*K-R, cx*K+R, cy*K+R), fill=(255, 250, 235, 255))
    ov = ov.resize(img.size, Image.LANCZOS)
    out = img.convert('RGBA'); out.alpha_composite(ov); return out.convert('RGB')

def fit(img, w, h, fx=0.5, fy=0.5):
    """scale to cover w x h, crop at focus fraction"""
    sc = max(w / img.size[0], h / img.size[1])
    r = img.resize((round(img.size[0]*sc), round(img.size[1]*sc)), Image.LANCZOS)
    x = round((r.size[0]-w)*fx); y = round((r.size[1]-h)*fy)
    return r.crop((x, y, x+w, y+h))

def framed(img, w, h, fx=0.5, fy=0.5):
    p = Image.new('RGB', (w, h), 'black')
    p.paste(fit(img, w-2*BORDER, h-2*BORDER, fx, fy), (BORDER, BORDER)); return p

def _lines_size(lines, font, spacing):
    d = ImageDraw.Draw(Image.new('L', (1, 1)))
    ws = [d.textbbox((0, 0), l, font=font)[2] for l in lines]
    return max(ws), spacing*(len(lines)-1) + font.size

def bubble(img, center, lines, size=30, spacing=33, tail=None, pad=(26, 18), jagged=False, lw=2.6):
    """speech bubble sized to text. tail = tip point (x,y). drawn supersampled."""
    f = ImageFont.truetype(BODY, size*S)
    tw, th = _lines_size(lines, f, spacing*S); tw /= S; th /= S
    rx, ry = tw/2 + pad[0], th/2 + pad[1]
    cx, cy = center
    pts = [(cx-rx, cy-ry), (cx+rx, cy+ry)] + ([tail] if tail else [])
    x0 = int(min(p[0] for p in pts)) - 20; y0 = int(min(p[1] for p in pts)) - 20
    x1 = int(max(p[0] for p in pts)) + 20; y1 = int(max(p[1] for p in pts)) + 20
    ov = Image.new('RGBA', ((x1-x0)*S, (y1-y0)*S), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    T = lambda p: ((p[0]-x0)*S, (p[1]-y0)*S)
    def shape(grow, fill):
        R = (rx+grow, ry+grow)
        if jagged:
            n = 44; poly = []
            for i in range(n):
                a = 2*math.pi*i/n; k = 1.22 if i % 2 == 0 else 1.06
                poly.append(T((cx + R[0]*k*math.cos(a), cy + R[1]*k*1.1*math.sin(a))))
            d.polygon(poly, fill=fill)
        else:
            d.ellipse([T((cx-R[0], cy-R[1])), T((cx+R[0], cy+R[1]))], fill=fill)
        if tail:
            ang = math.atan2(tail[1]-cy, tail[0]-cx); base = 0.32
            b1 = (cx + R[0]*0.8*math.cos(ang-base), cy + R[1]*0.8*math.sin(ang-base))
            b2 = (cx + R[0]*0.8*math.cos(ang+base), cy + R[1]*0.8*math.sin(ang+base))
            tip = tail if grow > 0 else (tail[0] - (lw*1.6)*math.cos(ang), tail[1] - (lw*1.6)*math.sin(ang))
            d.polygon([T(b1), T(tip), T(b2)], fill=fill)
    shape(lw, 'black'); shape(0, 'white')
    for i, ln in enumerate(lines):
        yy = cy + (i-(len(lines)-1)/2)*spacing
        d.text(T((cx, yy)), ln, font=f, fill='black', anchor='mm')
    ov = ov.resize((x1-x0, y1-y0), Image.LANCZOS)
    img.paste(ov, (x0, y0), ov)

def caption(img, xy, lines, size=30, spacing=33, pad=(18, 12), lw=3):
    f = ImageFont.truetype(BODY, size)
    tw, th = _lines_size(lines, f, spacing)
    x, y = xy; w, h = tw + 2*pad[0], th + 2*pad[1]
    d = ImageDraw.Draw(img)
    d.rectangle((x, y, x+w, y+h), fill='black'); d.rectangle((x+lw, y+lw, x+w-lw, y+h-lw), fill=(255, 243, 176))
    for i, ln in enumerate(lines):
        d.text((x+pad[0], y+pad[1] + i*spacing), ln, font=f, fill='black', anchor='la')

def sfx(img, center, text, size=90, angle=-8, fill=(255, 225, 77), stroke=(20, 12, 10), sw=None):
    f = ImageFont.truetype(SFX, size*2)
    sw = sw or max(6, size//7)
    d0 = ImageDraw.Draw(Image.new('L', (1, 1)))
    bb = d0.textbbox((0, 0), text, font=f, stroke_width=sw*2)
    w, h = bb[2]-bb[0] + 40, bb[3]-bb[1] + 40
    ov = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.text((w/2, h/2), text, font=f, fill=fill, stroke_width=sw*2, stroke_fill=stroke, anchor='mm')
    ov = ov.rotate(angle, resample=Image.BICUBIC, expand=True)
    ov = ov.resize((ov.size[0]//2, ov.size[1]//2), Image.LANCZOS)
    img.paste(ov, (int(center[0]-ov.size[0]/2), int(center[1]-ov.size[1]/2)), ov)
