import subprocess, numpy as np, math
from PIL import Image, ImageFilter, ImageEnhance
import timeline as TL
W,H,FPS=1080,1920,30
segs,TOTAL=TL.build()
cache={}
def load(pg):
    if pg not in cache:
        im=Image.open(f'/home/claude/sheets/{pg}_final.png').convert('RGB')
        s=max(W/im.width,H/im.height)
        bg=im.resize((int(im.width*s)+2,int(im.height*s)+2),Image.LANCZOS)
        l=(bg.width-W)//2; t=(bg.height-H)//2
        bg=bg.crop((l,t,l+W,t+H)).filter(ImageFilter.GaussianBlur(40))
        cache[pg]=(im,ImageEnhance.Brightness(bg).enhance(0.35))
    return cache[pg]
rng=np.random.default_rng(3)
NOISE=rng.standard_normal((int(TOTAL*FPS)+10,2))
def shake_off(seg,lt,f):
    if not seg['shake']: return 0,0,0.0
    amp,kind=seg['shake']; d=seg['d']
    if kind=='hit': k=math.exp(-lt*3.2)
    elif kind=='build': k=(lt/d)**1.6
    else: k=0.55
    a=amp*k
    return int(NOISE[f,0]*a*0.6), int(NOISE[f,1]*a*0.6), (0.9*math.exp(-lt*9) if kind=='hit' and amp>=25 else 0.0)
def render(seg,lt,f=None):
    im,bg=load(seg['pg'])
    d=seg['d']; p=lt/d
    if seg['kind']=='page':
        box=(0,0,im.width,im.height); z=1.0+0.04*p; maxw,maxh=1010,1780; cap=3
    else:
        box=TL.P[f"{seg['pg']}_final.png"][seg['i']]; z=(1.10-0.10*p) if seg.get('cold') else 1.0+0.07*p; maxw,maxh=1000,1500; cap=2.6
        if seg['shake'] and seg['shake'][1]=='hit' and seg['shake'][0]>=25: z=1.0+0.12*math.exp(-lt*5)+0.03*p  # punch-in
    x0,y0,x1,y1=box; pw,ph=x1-x0,y1-y0
    sc=min(maxw/pw,maxh/ph,cap)
    cw,ch=pw/z,ph/z; cx,cy=x0+pw/2,y0+ph/2
    crop=im.crop((cx-cw/2,cy-ch/2,cx+cw/2,cy+ch/2)).resize((int(pw*sc),int(ph*sc)),Image.LANCZOS)
    if seg['kind']=='panel': crop=crop.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=2))
    dx,dy,flash=(shake_off(seg,lt,f) if f is not None else (0,0,0.0))
    fr=bg.copy(); fr.paste(crop,((W-crop.width)//2+dx,(H-crop.height)//2+dy))
    if flash>0.02: fr=Image.blend(fr,Image.new('RGB',(W,H),(255,236,200)),min(flash,0.85))
    return fr
cmd=['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
     '-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','video2.mp4']
pr=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
starts=[s['t'] for s in segs]; XF=0.22
import bisect
for f in range(int(TOTAL*FPS)):
    t=f/FPS; k=max(0,bisect.bisect_right(starts,t)-1); s=segs[k]; lt=t-s['t']
    fr=render(s,lt,f)
    if k+1<len(segs) and s['d']-lt<XF:
        fr=Image.blend(fr,render(segs[k+1],0),1-(s['d']-lt)/XF)
    pr.stdin.write(fr.tobytes())
pr.stdin.close(); pr.wait(); print('video done',round(TOTAL,2))
