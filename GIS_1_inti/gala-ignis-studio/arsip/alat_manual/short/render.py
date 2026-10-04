import json, subprocess, numpy as np
from PIL import Image, ImageFilter, ImageEnhance
W,H,FPS=1080,1920,30
P=json.load(open('panels.json'))
TXT={'Hal01':[46,43,81,13],'Hal02':[42,26,28,24],'Hal03':[15,14,48],'Hal04':[12,20,14,30],
     'Hal05':[12,36,83,37],'Hal06':[53,73,27,30],'Hal07':[36,14,49,14],'Hal08':[49,81]}
pages={}
def page(name):
    if name not in pages:
        im=Image.open(f'/home/claude/sheets/{name}_final.png').convert('RGB')
        bg=im.resize((W,int(W*im.height/im.width)),Image.LANCZOS)
        bg=bg.resize((W*im.height//im.width*0+W, H)) if False else bg
        # cover-fit background
        s=max(W/im.width,H/im.height)
        bg=im.resize((int(im.width*s)+1,int(im.height*s)+1),Image.LANCZOS)
        l=(bg.width-W)//2; t=(bg.height-H)//2
        bg=bg.crop((l,t,l+W,t+H)).filter(ImageFilter.GaussianBlur(40))
        bg=ImageEnhance.Brightness(bg).enhance(0.35)
        pages[name]=(im,bg)
    return pages[name]
# segments: (page, box, duration, zoom_from, zoom_to)
segs=[]
b=P['Hal03_final.png'][0]; segs.append(('Hal03',b,1.3,1.10,1.00))   # cold open: explosion
segs.append(('Sampul',P['Sampul_final.png'][0],2.8,1.00,1.06))
for pg,lens in TXT.items():
    for i,box in enumerate(P[f'{pg}_final.png']):
        d=max(1.8,1.5+0.038*lens[i])
        if pg=='Hal03' and i==0: d=2.6
        if pg=='Hal08' and i==1: d=4.0
        segs.append((pg,box,d,1.00,1.07))
total=sum(s[2] for s in segs); print('segments',len(segs),'seconds',round(total,1))
XF=0.25
def frame_of(seg,t):
    pg,box,d,z0,z1=seg
    im,bg=page(pg if pg!='Sampul' else 'Sampul')
    x0,y0,x1,y1=box; pw,ph=x1-x0,y1-y0
    maxw,maxh=1000,1500
    sc=min(maxw/pw,maxh/ph,2.6)
    z=z0+(z1-z0)*(t/d)
    # crop tighter as zoom increases (Ken Burns inside panel)
    cw,ch=pw/z,ph/z; cx,cy=x0+pw/2,y0+ph/2
    crop=im.crop((cx-cw/2,cy-ch/2,cx+cw/2,cy+ch/2)).resize((int(pw*sc),int(ph*sc)),Image.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=2))
    fr=bg.copy()
    fr.paste(crop,((W-crop.width)//2,(H-crop.height)//2))
    return fr
cmd=['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
     '-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-movflags','+faststart','ep01_short_silent.mp4']
pr=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
starts=np.cumsum([0]+[s[2] for s in segs])
n=int(total*FPS)
for f in range(n):
    t=f/FPS
    k=np.searchsorted(starts,t,side='right')-1; k=min(k,len(segs)-1)
    lt=t-starts[k]
    fr=frame_of(segs[k],lt)
    if k+1<len(segs) and segs[k][2]-lt<XF:
        a=1-(segs[k][2]-lt)/XF
        fr=Image.blend(fr,frame_of(segs[k+1],0),a)
    if f<int(0.25*FPS) and k==0:   # white flash-in on cold open
        fr=Image.blend(Image.new('RGB',(W,H),'white'),fr,f/(0.25*FPS))
    pr.stdin.write(fr.tobytes())
pr.stdin.close(); pr.wait(); print('done')
