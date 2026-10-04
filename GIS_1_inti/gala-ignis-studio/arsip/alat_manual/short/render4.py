import subprocess, math, bisect, numpy as np
from PIL import Image, ImageDraw
import timeline3 as TL
W,H,FPS=1080,1920,30; SC=2
ev,TOTAL=TL.build()
BG=(18,18,20)
cw=len(TL.ORDER)*(TL.PW+TL.GAP)+TL.GAP
canvas=Image.new('RGB',(cw*SC,(TL.PH+2*TL.GAP)*SC),BG)
OY=TL.GAP
for pg in TL.ORDER:
    im=Image.open(f'/home/claude/sheets/{pg}_final.png').convert('RGB').resize((TL.PW*SC,TL.PH*SC),Image.LANCZOS)
    ox,_=TL.page_origin(pg); canvas.paste(im,((ox+TL.GAP)*SC,OY*SC))
def pbox(pg,i):
    ox,_=TL.page_origin(pg); ox+=TL.GAP
    if i<0: return (ox,OY,ox+TL.PW,OY+TL.PH)
    x0,y0,x1,y1=TL.P[f'{pg}_final.png'][i]; return (ox+x0,OY+y0,ox+x1,OY+y1)
def ease(p): return p*p*(3-2*p)
def lerp(a,b,p): return a+(b-a)*p
def pose(e,q):
    x0,y0,x1,y1=pbox(e['pg'],e['i']); pw,ph=x1-x0,y1-y0
    if e['i']<0:
        vw=max(pw*1.06,ph*1.06*9/16)*(1-0.03*q); return ((x0+x1)/2,(y0+y1)/2,vw),(x0,y0,x1,y1)
    if pw/ph>1.4 and not e['cold']:
        vw=max(pw*0.72,ph*1.12*9/16)
        m=pw*0.02; xa=x0+vw/2-m; xb=x1-vw/2+m
        qq=q*q*(3-2*q)
        return (lerp(xa,xb,qq),(y0+y1)/2,vw*(1-0.03*q)),(x0,y0,x1,y1)
    vw=max(pw*1.14,ph*1.14*9/16,430)
    vw*= (1.10-0.10*q) if e['cold'] else (1-0.05*q)
    return ((x0+x1)/2,(y0+y1)/2-ph*0.02*q,vw),(x0,y0,x1,y1)
rng=np.random.default_rng(3); NZ=rng.standard_normal((int(TOTAL*FPS)+50,2))
starts=[e['t']-e['move'] for e in ev]
def camera(t,f):
    k=max(0,bisect.bisect_right(starts,t)-1); e=ev[k]
    flash=0.0
    if t<e['t'] and k>0:   # moving from previous event's end pose
        (cx,cy,vw),fr=pose(e,0.0); (px,py,pv),pf=pose(ev[k-1],1.0); p=ease((t-(e['t']-e['move']))/e['move'])
        cx=lerp(px,cx,p); cy=lerp(py,cy,p); vw=math.exp(lerp(math.log(pv),math.log(vw),p))
        if e['kind']=='page': vw*=1+0.18*math.sin(math.pi*p)
        fr=tuple(lerp(a,b,p) for a,b in zip(pf,fr)); lt=None
    else:
        lt=t-e['t']; q=min(1,lt/max(e['d'],0.01)); (cx,cy,vw),fr=pose(e,q)
        if e['shake']:
            amp,kind=e['shake']
            kk=math.exp(-lt*3.2) if kind=='hit' else ((lt/e['d'])**1.6 if kind=='build' else 0.55)
            a=amp*kk*vw/W*0.6; cx+=NZ[f,0]*a; cy+=NZ[f,1]*a
            if kind=='hit' and amp>=25:
                vw*=1-0.10*math.exp(-lt*5); flash=0.9*math.exp(-lt*9)
    return cx,cy,vw,fr,flash,e,lt
def frame(t,f):
    cx,cy,vw,fr,flash,e,lt=camera(t,f); vh=vw*16/9
    box=((cx-vw/2)*SC,(cy-vh/2)*SC,(cx+vw/2)*SC,(cy+vh/2)*SC)
    img=canvas.transform((W,H),Image.EXTENT,box,Image.BICUBIC)
    a=np.asarray(img).astype(np.float32)
    # spotlight: dim outside focus rect
    sx=W/vw; x0=int((fr[0]-(cx-vw/2))*sx); y0=int((fr[1]-(cy-vh/2))*sx); x1=int((fr[2]-(cx-vw/2))*sx); y1=int((fr[3]-(cy-vh/2))*sx)
    mask=np.full((H,W),0.38,np.float32)
    mask[max(0,y0):max(0,min(H,y1)),max(0,x0):max(0,min(W,x1))]=1.0
    a*=mask[:,:,None]
    if flash>0.02: a=a*(1-min(flash,0.85))+np.array([255,236,200],np.float32)*min(flash,0.85)
    if t<1.4 and f<8: a=a*(f/8)+255*(1-f/8)
    return np.clip(a,0,255).astype(np.uint8)
cmd=['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','video4.mp4']
pr=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
cover_t=ev[1]['t']
for f in range(int(TOTAL*FPS)):
    t=f/FPS; a=frame(t,f)
    if cover_t<=t<cover_t+0.3:  # white flash cut from cold open to cover
        k=(t-cover_t)/0.3; a=(a*k+255*(1-k)).astype(np.uint8)
    pr.stdin.write(a.tobytes())
pr.stdin.close(); pr.wait(); print('done',round(TOTAL,2))
