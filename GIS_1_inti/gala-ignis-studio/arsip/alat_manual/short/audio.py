import numpy as np, wave
SR=44100
TXT={'Hal01':[46,43,81,13],'Hal02':[42,26,28,24],'Hal03':[15,14,48],'Hal04':[12,20,14,30],
     'Hal05':[12,36,83,37],'Hal06':[53,73,27,30],'Hal07':[36,14,49,14],'Hal08':[49,81]}
segs=[('Hal03',0,1.3),('Sampul',0,2.8)]
for pg,l in TXT.items():
    for i,n in enumerate(l):
        d=max(1.8,1.5+0.038*n)
        if pg=='Hal03' and i==0: d=2.6
        if pg=='Hal08' and i==1: d=4.0
        segs.append((pg,i,d))
st=np.cumsum([0]+[s[2] for s in segs]); T=st[-1]
at={ (s[0],s[1]):st[k] for k,s in enumerate(segs)}
N=int(T*SR)+SR; L=np.zeros(N); t=np.arange(N)/SR
rng=np.random.default_rng(7)
def add(sig,start,gain=1.0):
    i=int(start*SR); j=min(N,i+len(sig)); L[i:j]+=gain*sig[:j-i]
def env(n,a=0.01,r=0.3):
    e=np.ones(n); na=int(a*SR); nr=int(r*SR)
    if na: e[:na]=np.linspace(0,1,na)
    if nr: e[-nr:]*=np.linspace(1,0,nr)
    return e
def lp(x,k): return np.convolve(x,np.ones(k)/k,mode='same')
# ambient drone
drone=0.05*np.sin(2*np.pi*55*t)+0.03*np.sin(2*np.pi*82.5*t)+0.02*lp(rng.standard_normal(N),200)
drone*=np.clip(t/1.5,0,1)*np.clip((T+0.5-t)/1.5,0,1); L+=drone
# whoosh on every cut
for k in range(1,len(segs)):
    n=int(0.35*SR); x=lp(rng.standard_normal(n),6)*np.hanning(n); add(x,st[k]-0.15,0.10)
def boom(start,g=1.0):
    n=int(2.2*SR); tt=np.arange(n)/SR
    x=(lp(rng.standard_normal(n),30)*np.exp(-tt*3)*1.2+np.sin(2*np.pi*(60*np.exp(-tt*1.5)+30)*tt)*np.exp(-tt*2))
    add(x,start,0.55*g)
boom(0.0,0.9); boom(at[('Hal03',0)],1.0)
# alarm siren during page 2 panels 1-2
a0=at[('Hal02',0)]; a1=at[('Hal02',2)]
n=int((a1-a0)*SR); tt=np.arange(n)/SR
f=np.where((tt%0.5)<0.25,880,660); ph=2*np.pi*np.cumsum(f)/SR
add(np.sign(np.sin(ph))*0.5*env(n,0.02,0.2),a0,0.06)
# rising hum page 2 panel 3-4 (plasma charging)
b0=at[('Hal02',2)]; b1=at[('Hal03',0)]; n=int((b1-b0)*SR); tt=np.arange(n)/SR
fr=80+220*(tt/tt[-1])**2; add(np.sin(2*np.pi*np.cumsum(fr)/SR)*env(n,0.1,0.05),b0,0.12)
# sparkle at Ethylene birth
def sparkle(start):
    for j in range(8):
        n=int(0.12*SR); tt=np.arange(n)/SR; fq=1500+rng.random()*2500
        add(np.sin(2*np.pi*fq*tt)*np.exp(-tt*30),start+j*0.07,0.10)
sparkle(at[('Hal04',0)]+0.1); sparkle(at[('Hal07',3)]+0.1)
def pip(start,up=False):
    n=int(0.14*SR); tt=np.arange(n)/SR; fq=(900+1400*tt/tt[-1]) if up else (1300-200*tt/tt[-1])
    add(np.sin(2*np.pi*np.cumsum(fq)/SR)*env(n,0.005,0.06),start,0.22)
pip(at[('Hal04',2)]+0.3); pip(at[('Hal07',1)]+0.3); pip(at[('Hal07',3)]+0.3,True); pip(at[('Hal07',3)]+0.5,True)
# door hiss page 5
n=int(1.2*SR); add(lp(rng.standard_normal(n),3)*env(n,0.05,0.8),at[('Hal05',0)],0.15)
# sting on 24 JAM
n=int(1.0*SR); tt=np.arange(n)/SR
st2=sum(np.sin(2*np.pi*f*tt) for f in (110,138.6,164.8))*np.exp(-tt*2); add(st2,at[('Hal06',1)],0.10); add(st2,at[('Hal06',2)],0.14)
# warm pad at dawn (pages 7-8)
d0=at[('Hal07',0)]; n=int((T-d0)*SR); tt=np.arange(n)/SR
pad=sum(np.sin(2*np.pi*f*tt) for f in (261.6,329.6,392.0,523.3))*0.25*env(n,2.0,2.0); add(pad,d0,0.08)
L=L[:int(T*SR)]; L=L/np.max(np.abs(L))*0.89
wf=wave.open('sfx.wav','wb'); wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
wf.writeframes((L*32767).astype(np.int16).tobytes()); wf.close(); print('audio',round(T,2),'s')
