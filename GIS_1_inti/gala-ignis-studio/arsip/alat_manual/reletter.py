import sys; sys.path.insert(0, '/home/claude/komik')
from comp import *
from scipy import ndimage as ndi
CAPCOL = (255, 243, 176)

def component(a, box, cond):
    x0, y0, x1, y1 = box
    sub = cond(a[y0:y1, x0:x1])
    lab, n = ndi.label(sub)
    best, bs = None, 0
    for i in range(1, n+1):
        ys, xs = np.where(lab == i)
        if ys.min() == 0 or xs.min() == 0 or ys.max() == sub.shape[0]-1 or xs.max() == sub.shape[1]-1: continue
        if len(ys) > bs: best, bs = i, len(ys)
    m = ndi.binary_fill_holes(lab == best)
    full = np.zeros(a.shape[:2], bool); full[y0:y1, x0:x1] = m
    return full

def erase_bubble(img, box, erode=2):
    a = np.asarray(img).copy()
    m = component(a, box, lambda s: (s.min(2) > 200))
    m = ndi.binary_erosion(m, iterations=erode)
    a[m] = 255
    dt = ndi.distance_transform_edt(m); cy, cx = np.unravel_index(dt.argmax(), dt.shape)
    ys, xs = np.where(m)
    return Image.fromarray(a), dict(center=(cx, cy), w=xs.max()-xs.min(), h=ys.max()-ys.min(), inner=dt.max())

def caption_box(img, box):
    a = np.asarray(img)
    m = component(a, box, lambda s: (s[..., 0] > 215) & (s[..., 1] > 200) & (s[..., 2] > 110) & (s[..., 2] < 215))
    ys, xs = np.where(m)
    return (xs.min(), ys.min(), xs.max(), ys.max())

def text_block(img, center, lines, size, spacing, maxw=None):
    f = ImageFont.truetype(BODY, size)
    tw, th = (lambda d: (max(d.textbbox((0, 0), l, font=f)[2] for l in lines), 0))(ImageDraw.Draw(Image.new('L', (1, 1))))
    if maxw and tw > maxw:
        return text_block(img, center, lines, int(size*maxw/tw), int(spacing*maxw/tw))
    d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        d.text((center[0], center[1] + (i-(len(lines)-1)/2)*spacing), ln, font=f, fill='black', anchor='mm')

def sfx_mask(img, box):
    a = np.asarray(img).astype(int); x0, y0, x1, y1 = box
    s = a[y0:y1, x0:x1]
    m = (s.min(2) > 195) | (s.max(2) < 45)
    m = ndi.binary_dilation(m, iterations=2)
    full = np.zeros(a.shape[:2], np.uint8); full[y0:y1, x0:x1] = m*255
    b = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    return Image.fromarray(cv2.cvtColor(cv2.inpaint(b, full, 5, cv2.INPAINT_TELEA), cv2.COLOR_BGR2RGB))

def reletter(src, out, bubbles=(), captions=(), sfxs=(), size=30, spacing=33, H=None, up=None):
    img = Image.open(src).convert('RGB') if isinstance(src, str) else src
    jobs = []
    for box, lines in bubbles:
        img, info = erase_bubble(img, box); jobs.append(('b', info, lines))
    for box, lines in captions:
        jobs.append(('c', caption_box(img, box), lines))
    for box, text, kw in sfxs:
        img = sfx_mask(img, box); jobs.append(('s', box, (text, kw)))
    img = (up(img).resize((img.size[0]*2, img.size[1]*2), Image.LANCZOS) if up else img.resize((img.size[0]*2, img.size[1]*2), Image.LANCZOS))
    for kind, info, lines in jobs:
        if kind == 'b':
            c = (info['center'][0]*2, info['center'][1]*2)
            text_block(img, c, lines, size, spacing, maxw=info['w']*2*0.86)
        elif kind == 'c':
            x0, y0, x1, y1 = [v*2 for v in info]
            d = ImageDraw.Draw(img); d.rectangle((x0, y0, x1, y1), fill='black'); d.rectangle((x0+3, y0+3, x1-3, y1-3), fill=CAPCOL)
            text_block(img, ((x0+x1)/2, (y0+y1)/2), lines, size, spacing, maxw=(x1-x0)*0.88)
        else:
            (bx0, by0, bx1, by1) = info; text, kw = lines
            kw = dict(kw); at = kw.pop('at', ((bx0+bx1), (by0+by1)))
            sfx(img, at, text, **kw)
    if H and img.size[1] != H:
        c = Image.new('RGB', (img.size[0], H), 'white'); c.paste(img, (0, (H-img.size[1])//2)); img = c
    img.save(out); return img

def clean_margins(img, thr=0.5):
    a = np.asarray(img).copy(); g = a.min(2) < 80
    rows = np.where(g.mean(1) > thr)[0]; cols = np.where(g.mean(0) > thr)[0]
    if len(rows): a[:max(rows.min()-1, 0)] = 255; a[rows.max()+2:] = 255
    if len(cols): a[:, :max(cols.min()-1, 0)] = 255; a[:, cols.max()+2:] = 255
    return Image.fromarray(a)
