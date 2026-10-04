import numpy as np, wave
from scipy.signal import butter, lfilter, fftconvolve
import timeline as TL
SR=44100
segs,T=TL.build()
N=int((T+2)*SR); M=np.zeros(N); S=np.zeros(N)
rng=np.random.default_rng(11)
def A(pg,i): return TL.at(segs,pg,i)
def put(buf,x,t0,g=1.0):
    i=int(t0*SR); j=min(N,i+len(x)); 
    if i<N: buf[i:j]+=g*x[:j-i]
def lpf(x,fc,o=2): b,a=butter(o,fc/(SR/2)); return lfilter(b,a,x)
def hpf(x,fc,o=2): b,a=butter(o,fc/(SR/2),'high'); return lfilter(b,a,x)
def envl(n,a,r,s=1.0):
    e=np.full(n,s); na=max(1,int(a*SR)); nr=max(1,int(r*SR))
    e[:na]=np.linspace(0,s,na); e[-nr:]*=np.linspace(1,0,nr); return e
def saw(f,n,det=(0,)):
    t=np.arange(n)/SR; return sum(2*((t*f*(1+d))%1)-1 for d in det)/len(det)
NOTE={'C':-9,'C#':-8,'D':-7,'Eb':-6,'E':-5,'F':-4,'F#':-3,'G':-2,'Ab':-1,'A':0,'Bb':1,'B':2}
def hz(n,o): return 440*2**((NOTE[n]+12*(o-4))/12)
def pad(chord,t0,dur,g=0.18,fc=1600,a=0.6,r=0.8):
    n=int(dur*SR); x=sum(saw(hz(nm,o),n,(-0.004,0,0.005)) for nm,o in chord)/len(chord)
    put(M,lpf(x,fc)*envl(n,a,r),t0,g)
def low(nm,o,t0,dur,g=0.22,fc=500):
    n=int(dur*SR); put(M,lpf(saw(hz(nm,o),n,(0,0.003)),fc)*envl(n,0.005,dur*0.6),t0,g)
def timp(t0,g=0.6,f=55):
    n=int(1.6*SR); t=np.arange(n)/SR
    x=np.sin(2*np.pi*np.cumsum(f*(1+0.6*np.exp(-t*18)))/SR)*np.exp(-t*2.6)+lpf(rng.standard_normal(n),300)*np.exp(-t*25)*0.6
    put(M,x,t0,g)
def brass(chord,t0,dur,g=0.3):
    n=int(dur*SR); x=sum(saw(hz(nm,o),n,(-0.003,0.003)) for nm,o in chord)/len(chord)
    tt=np.arange(n)/SR; y=np.zeros(n)
    for k in range(0,n,2048):  # time-varying filter approximation: blend bright->dark
        pass
    bright=lpf(x,3500); dark=lpf(x,900); w=np.exp(-tt*3)
    put(M,(bright*w+dark*(1-w))*envl(n,0.02,dur*0.7),t0,g)
def bell(nm,o,t0,g=0.12):
    n=int(2.5*SR); t=np.arange(n)/SR; f=hz(nm,o)
    x=(np.sin(2*np.pi*f*t)+0.4*np.sin(2*np.pi*f*2.76*t)*np.exp(-t*3))*np.exp(-t*1.6); put(M,x,t0,g)
def pluck(nm,o,t0,g=0.12):
    n=int(1.2*SR); t=np.arange(n)/SR; f=hz(nm,o)
    x=sum(np.sin(2*np.pi*f*k*t)/k for k in (1,2,3))*np.exp(-t*4); put(M,x,t0,g)
def riser(t0,t1,g=0.2):
    n=int((t1-t0)*SR); t=np.arange(n)/SR; p=t/t[-1]
    tone=np.sin(2*np.pi*np.cumsum(200+1400*p**2)/SR)*p**2
    noise=hpf(rng.standard_normal(n),800)*p**3
    put(M,(0.5*tone+0.6*noise),t0,g)
BEAT=60/92
# --- cover: title hit
c0=segs[1]['t']; timp(0.0,0.7,50); brass([('D',3),('A',3),('D',4),('F',4)],c0,2.6,0.28); timp(c0,0.5)
# --- page 1: calm tension pad + slow pulse
p1=A('Hal01',-1); p2=A('Hal02',-1)
pad([('D',3),('A',3),('F',4)],p1,(p2-p1)/2+0.3,0.14,1200,1.2,0.6)
pad([('Bb',2),('F',3),('D',4)],p1+(p2-p1)/2,(p2-p1)/2+0.4,0.14,1200,0.8,0.6)
t=p1
while t<p2-0.1: low('D',2,t,BEAT*0.9,0.16,350); t+=BEAT*2
# --- page 2: alarm ostinato + progression + riser
p3=A('Hal03',0); prog=[[('D',3),('A',3),('F',4)],[('Bb',2),('F',3),('D',4)],[('G',2),('D',3),('Bb',3)],[('A',2),('E',3),('C#',4)]]
L=(p3-p2)/4
for k,ch in enumerate(prog): pad(ch,p2+k*L,L+0.3,0.16+0.03*k,1400+400*k,0.1,0.3)
t=p2; roots=['D','Bb','G','A']
while t<p3-0.05:
    k=min(3,int((t-p2)/L)); low(roots[k],2 if roots[k] in('D','A') else 1,t,BEAT/2*0.8,0.2+0.05*k,550+150*k); t+=BEAT/2
for b in np.arange(p2,p3-0.2,BEAT*2): timp(b,0.25)
riser(p3-2.4,p3,0.28)
# --- explosion
timp(p3,0.9,45); brass([('D',2),('A',2),('D',3),('F',3),('A',3)],p3,3.5,0.4)
p4=A('Hal04',-1); pad([('D',2),('A',2)],p3+0.5,p4-p3,0.10,300,0.5,1.5)
# --- page 4: birth of Ethylene, magical
p5=A('Hal05',-1)
pad([('F',3),('A',3),('C',4),('E',4)],p4,p5-p4+0.5,0.10,2200,1.5,1.2)
arp=[('F',5),('A',5),('C',6),('E',6),('C',6),('A',5)]
t=A('Hal04',0); k=0
while t<p5-0.3: bell(*arp[k%6],t,0.07); t+=BEAT/2; k+=1
# --- pages 5-6: instructors, tension
p7=A('Hal07',-1)
pad([('D',2),('Ab',2),('D',3)],p5,p7-p5,0.13,700,0.8,0.6)
t=p5
while t<p7-0.2: timp(t,0.22,48); timp(t+BEAT*0.35,0.15,48); t+=BEAT*2   # heartbeat
timp(A('Hal05',1),0.5); brass([('D',3),('Ab',3),('D',4)],A('Hal05',1),1.8,0.22)
for key in (('Hal06',1),('Hal06',2)):
    tt=A(*key); timp(tt,0.8,42); brass([('D',2),('A',2),('D',3),('Eb',3)],tt,2.0,0.34)
riser(A('Hal06',2)-1.2,A('Hal06',2),0.18)
# --- pages 7-8: dawn, hopeful resolution
hope=[[('F',3),('A',3),('C',4)],[('C',3),('G',3),('E',4)],[('D',3),('A',3),('F',4)],[('Bb',2),('F',3),('D',4)]]
L=(T-p7)/5
for k,ch in enumerate(hope+[[('F',2),('C',3),('A',3),('F',4)]]):
    pad(ch,p7+k*L,L+0.8 if k<4 else L+1.5,0.12+0.025*k,1500+300*k,0.9,0.9 if k<4 else 2.5)
mel=[('A',4),('C',5),('F',5),('E',5),('G',4),('C',5),('E',5),('D',5),('F',4),('A',4),('D',5),('C',5),('F',4),('Bb',4),('D',5),('C',5)]
for k,nm in enumerate(mel): pluck(*nm,p7+k*(4*L/16),0.10)
timp(A('Hal08',-1),0.4); bell('F',5,T-3.8,0.12); bell('C',6,T-3.6,0.1); bell('A',5,T-3.4,0.1)
# ---------- SFX (retimed)
def lp(x,k): return np.convolve(x,np.ones(k)/k,mode='same')
for s in segs[1:]:
    n=int(0.35*SR); put(S,lp(rng.standard_normal(n),6)*np.hanning(n),s['t']-0.15,0.07)
def boom(t0,g):
    n=int(2.2*SR); tt=np.arange(n)/SR
    put(S,lp(rng.standard_normal(n),30)*np.exp(-tt*3)*1.2+np.sin(2*np.pi*(60*np.exp(-tt*1.5)+30)*tt)*np.exp(-tt*2),t0,g)
boom(0.0,0.45); boom(p3,0.55)
a0=A('Hal02',0); a1=A('Hal02',2); n=int((a1-a0)*SR); tt=np.arange(n)/SR
ph=2*np.pi*np.cumsum(np.where((tt%0.5)<0.25,880,660))/SR; put(S,np.sign(np.sin(ph))*envl(n,0.02,0.2),a0,0.035)
def sparkle(t0):
    for j in range(8):
        n=int(0.12*SR); tt=np.arange(n)/SR; put(S,np.sin(2*np.pi*(1500+rng.random()*2500)*tt)*np.exp(-tt*30),t0+j*0.07,0.07)
sparkle(A('Hal04',0)+0.1); sparkle(A('Hal07',3)+0.1)
def pip(t0,up=False):
    n=int(0.14*SR); tt=np.arange(n)/SR; fq=(900+1400*tt/tt[-1]) if up else (1300-200*tt/tt[-1])
    put(S,np.sin(2*np.pi*np.cumsum(fq)/SR)*envl(n,0.005,0.06),t0,0.18)
pip(A('Hal04',2)+0.3); pip(A('Hal07',1)+0.3); pip(A('Hal07',3)+0.3,True); pip(A('Hal07',3)+0.5,True)
n=int(1.2*SR); put(S,lp(rng.standard_normal(n),3)*envl(n,0.05,0.8),A('Hal05',0),0.12)
# ---------- reverb + mix
n=int(1.8*SR); ir=rng.standard_normal(n)*np.exp(-np.arange(n)/SR*3.2); ir=lpf(ir,5000); ir/=np.sqrt((ir**2).sum())
wet=fftconvolve(M,ir)[:N]; M2=M*0.75+wet*0.45
mix=M2/np.max(np.abs(M2))*0.75+S/np.max(np.abs(S))*0.45
mix=mix[:int(T*SR)]; fade=int(1.5*SR); mix[-fade:]*=np.linspace(1,0,fade)
mix=np.tanh(mix*1.2)/np.tanh(1.2); mix=mix/np.max(np.abs(mix))*0.92
w=wave.open('music_sfx.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close()
print('audio',round(T,2))
