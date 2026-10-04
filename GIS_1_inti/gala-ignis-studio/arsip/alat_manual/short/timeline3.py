import json
P=json.load(open('/home/claude/short/panels.json'))
TXT={'Hal01':[46,43,81,13],'Hal02':[42,26,28,24],'Hal03':[15,14,48],'Hal04':[12,20,14,30],
     'Hal05':[12,36,83,37],'Hal06':[53,73,27,30],'Hal07':[36,14,49,14],'Hal08':[49,81]}
ORDER=['Sampul']+list(TXT)
PW,PH,GAP=687,1024,260
def page_origin(pg): return ORDER.index(pg)*(PW+GAP), 0
SHAKE={('Hal03',0,'cold'):(38,'hit'),('Hal02',0):(7,'rumble'),('Hal02',3):(26,'build'),
       ('Hal03',0):(44,'hit'),('Hal03',1):(16,'rumble'),('Hal05',0):(10,'hit'),
       ('Hal06',1):(14,'hit'),('Hal06',2):(30,'hit')}
MOVE_PANEL,MOVE_PAGE=0.55,0.8
def build():
    ev=[]; t=0
    def add(kind,pg,i,d,move,cold=False):
        nonlocal t
        t+=move
        key=(pg,i,'cold') if cold else (pg,i)
        ev.append(dict(kind=kind,pg=pg,i=i,t=t,d=d,move=move,cold=cold,shake=SHAKE.get(key)))
        t+=d
    add('panel','Hal03',0,1.4,0,True)
    add('page','Sampul',-1,2.8,0)
    for pg,lens in TXT.items():
        add('page',pg,-1,0.8,MOVE_PAGE)
        for i,n in enumerate(lens):
            d=max(1.5,1.2+0.034*n)
            if pg=='Hal03' and i==0: d=2.6
            if pg=='Hal02' and i==3: d=2.5
            if pg=='Hal08' and i==1: d=4.2
            add('panel',pg,i,d,MOVE_PANEL)
    return ev,t+0.4
def at(ev,pg,i):
    for e in ev:
        if e['pg']==pg and e['i']==i and not e['cold']: return e['t']
