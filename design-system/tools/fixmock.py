import sys
from PIL import Image
import numpy as np
Z=sys.argv[1]; OUT=sys.argv[2]
def load(p): return Image.open(Z+'/'+p).convert('RGB')
def art(p):
    im=Image.open(p).convert('RGBA'); return im.crop(im.getbbox())
def paste(base,a,w,cx,top=None,cy=None):
    h=round(a.height*w/a.width); a=a.resize((w,h),Image.LANCZOS)
    x=round(cx-w/2); y=top if top is not None else round(cy-h/2)
    base.paste(a,(x,y),a); return (x,y,x+w,y+h)
def mug(src,artp,w):
    im=load(src); a=np.asarray(im).astype(int)
    bg=a[5,450]; clean_y=615
    nb=np.where(np.abs(a[clean_y]-bg).sum(1)>12)[0]
    L=nb.min(); R=L
    while R+1<900 and abs(a[clean_y,R+1]-bg).sum()>12: R+=1
    for y in range(228,clean_y): a[y,L:R+1]=a[clean_y,L:R+1]
    out=Image.fromarray(a.astype('uint8'))
    box=paste(out,art(artp),w,(L+R)/2,cy=440)
    print(src,'body',L,R,'new',box); return out
def tee(src,artp,w,top,ebox):
    im=load(src); a=np.asarray(im).astype(float)
    x0,y0,x1,y1=ebox
    for y in range(y0,y1):
        l=a[y,x0-6:x0-2].mean(0); r=a[y,x1+2:x1+6].mean(0)
        t=np.linspace(0,1,x1-x0)[:,None]
        a[y,x0:x1]=l*(1-t)+r*t
    out=Image.fromarray(a.round().astype('uint8'))
    box=paste(out,art(artp),w,450,top=top); print(src,'new',box); return out
def beanie(src,artp,w):
    im=load(src); a=np.asarray(im).astype(int)
    # old patch: find patch pixels in cuff band around center
    box=paste(im,art(artp),w,450,cy=547); print(src,'patch',box); return im
R1='r1/crooked-merch/mockups/';R2='r2/crooked-round-2/merch-mockups/';H='hats/crooked-everybody-in-hats/mockups/'
P1=Z+'/r1/crooked-merch/print-art/';P2=Z+'/r2/crooked-round-2/merch-print-art/'
res={
 'mug-banker':mug(R2+'mug-banker.png',P2+'art-banker.png',300),
 'mug-hottakes':mug(R1+'mug-hottakes.png',P1+'art-hottakes.png',300),
 'mug-ballot':mug(R1+'mug-ballot.png',P1+'art-ballot.png',300),
 'mug-news':mug(R1+'mug-news.png',P1+'art-news.png',250),
 'tee-doorknock':tee(R1+'tee-doorknock.png',P1+'art-doorknock.png',236,250,(290,250,612,470)),
 'tee-jersey':tee(R2+'tee-jersey.png','art-jersey.png',240,215,(300,200,600,480)),
 'beanie-turnout':beanie(R1+'beanie-turnout.png','art-turnout.png',236),
 'beanie-build-it-here':beanie(H+'beanie-build-it-here.png','art-build.png',176),
}
for k,v in res.items(): v.save(f'{OUT}/{k}.png')
W=450;sheet=Image.new('RGB',(W*4,496*2),'white')
for i,(k,v) in enumerate(res.items()): sheet.paste(v.resize((450,496)),((i%4)*W,(i//4)*496))
sheet.save(OUT+'/after8.png')
