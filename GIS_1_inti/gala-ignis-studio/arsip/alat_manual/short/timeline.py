import json
P=json.load(open('/home/claude/short/panels.json'))
TXT={'Hal01':[46,43,81,13],'Hal02':[42,26,28,24],'Hal03':[15,14,48],'Hal04':[12,20,14,30],
     'Hal05':[12,36,83,37],'Hal06':[53,73,27,30],'Hal07':[36,14,49,14],'Hal08':[49,81]}
# shake: (amplitude px, kind) kind: 'hit' decaying, 'rumble' constant, 'build' increasing
SHAKE={('Hal03',0,'cold'):(38,'hit'),('Hal02',0):(7,'rumble'),('Hal02',3):(26,'build'),
       ('Hal03',0):(44,'hit'),('Hal03',1):(16,'rumble'),('Hal05',0):(10,'hit'),
       ('Hal06',1):(14,'hit'),('Hal06',2):(30,'hit')}
def build():
    segs=[]
    segs.append(dict(kind='panel',pg='Hal03',i=0,d=1.4,cold=True))
    segs.append(dict(kind='page',pg='Sampul',i=0,d=2.8))
    for pg,lens in TXT.items():
        segs.append(dict(kind='page',pg=pg,i=-1,d=1.1))
        for i,n in enumerate(lens):
            d=max(1.6,1.35+0.034*n)
            if pg=='Hal03' and i==0: d=2.8
            if pg=='Hal02' and i==3: d=2.6
            if pg=='Hal08' and i==1: d=4.2
            segs.append(dict(kind='panel',pg=pg,i=i,d=d))
    t=0
    for s in segs:
        s['t']=t; t+=s['d']
        key=(s['pg'],s['i'],'cold') if s.get('cold') else (s['pg'],s['i'])
        s['shake']=SHAKE.get(key)
    return segs,t
def at(segs,pg,i):
    for s in segs:
        if s['pg']==pg and s['i']==i and not s.get('cold'): return s['t']
