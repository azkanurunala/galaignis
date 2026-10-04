import numpy as np
from PIL import Image
from scipy import ndimage
import json
fs=['Sampul_final.png']+[f'Hal0{i}_final.png' for i in range(1,9)]
out={}
for f in fs:
    im=np.asarray(Image.open('/home/claude/sheets/'+f).convert('L')).astype(int)
    nonwhite=im<235
    filled=ndimage.binary_fill_holes(nonwhite)
    lab,n=ndimage.label(filled)
    boxes=[]
    for sl in ndimage.find_objects(lab):
        y0,y1=sl[0].start,sl[0].stop; x0,x1=sl[1].start,sl[1].stop
        if (y1-y0)*(x1-x0)>0.04*im.size: boxes.append([x0,y0,x1,y1])
    boxes.sort(key=lambda b:(round(b[1]/40),b[0]))
    out[f]=boxes
    print(f,len(boxes),boxes)
json.dump(out,open('panels.json','w'))
