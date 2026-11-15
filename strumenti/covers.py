import math,os
from PIL import Image,ImageDraw,ImageFont
F='/root/.claude/skills/synced/bbb5bd2f-7dc1-479e-935c-6bde90469bb2_c4d8bf62-0236-4cd2-a06c-5eb4266d5188/canvas-design/canvas-fonts/'
OUT='/home/user/bimnews.github.io/assets/copertine/';os.makedirs(OUT,exist_ok=True)
S=2;W,H=600*S,400*S
BG=(13,17,21);ACC=(231,154,120);INK=(232,236,239);MUT=(141,152,163)
def a(c,al):return c+(int(255*al),)
num=ImageFont.truetype(F+'Jura-Light.ttf',150*S)
tit=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',25*S)
sub=ImageFont.truetype(F+'InstrumentSans-Regular.ttf',14*S)
mono=ImageFont.truetype(F+'JetBrainsMono-Regular.ttf',9*S)
M=28*S  # margine
def base(n,title,subt):
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im,'RGBA')
    g=20*S
    for x in range(M,W-M+1,g):d.line([(x,M),(x,H-M)],fill=a(INK,.035),width=1)
    for y in range(M,H-M+1,g):d.line([(M,y),(W-M,y)],fill=a(INK,.035),width=1)
    d.rectangle([M,M,W-M,H-M],outline=a(INK,.16),width=S)
    for i,x in enumerate(range(M,W-M+1,g*5)):  # tacche e riferimenti come una tavola
        d.line([(x,M-6*S),(x,M)],fill=a(INK,.3),width=S)
        if x<W-M-g:d.text((x+g*2.5,M-14*S),'ABCDEFGH'[i],font=mono,fill=a(MUT,.7),anchor='mm')
    for i,y in enumerate(range(M,H-M+1,g*5)):
        d.line([(M-6*S,y),(M,y)],fill=a(INK,.3),width=S)
        if y<H-M-g:d.text((M-14*S,y+g*2.5),str(i+1),font=mono,fill=a(MUT,.7),anchor='mm')
    d.text((M+14*S,M+4*S),n,font=num,fill=tuple(round(BG[i]+(ACC[i]-BG[i])*.16) for i in range(3)))
    d.text((M+18*S,H-M-62*S),title,font=tit,fill=INK)
    d.text((M+18*S,H-M-30*S),subt,font=sub,fill=MUT)
    d.text((W-M-12*S,M+16*S),'BIM NEWS · NELLO STUDIO · MANUALE '+n,font=mono,fill=a(MUT,.8),anchor='ra')
    return im,d
def ln(d,p,al=1,w=1.2):d.line(p,fill=a(ACC,al),width=max(1,round(w*S)),joint='curve')
def box(d,x,y,w,h,al=1,dash=False):
    if not dash:d.rectangle([x,y,x+w,y+h],outline=a(ACC,al),width=round(1.2*S));return
    for (p,q) in [((x,y),(x+w,y)),((x+w,y),(x+w,y+h)),((x+w,y+h),(x,y+h)),((x,y+h),(x,y))]:
        L=math.dist(p,q);n=int(L/(8*S))
        for k in range(0,n,2):
            t0,t1=k/n,min(1,(k+1)/n);d.line([(p[0]+(q[0]-p[0])*t0,p[1]+(q[1]-p[1])*t0),(p[0]+(q[0]-p[0])*t1,p[1]+(q[1]-p[1])*t1)],fill=a(ACC,al),width=S)
def bez(d,p0,p1,p2,p3,al=1):
    pts=[];[pts.append(((1-t)**3*p0[0]+3*(1-t)**2*t*p1[0]+3*(1-t)*t*t*p2[0]+t**3*p3[0],(1-t)**3*p0[1]+3*(1-t)**2*t*p1[1]+3*(1-t)*t*t*p2[1]+t**3*p3[1])) for t in [i/60 for i in range(61)]];ln(d,pts,al)
def dot(d,x,y,r=3,al=1,fill=True):d.ellipse([x-r*S,y-r*S,x+r*S,y+r*S],fill=a(ACC,al) if fill else None,outline=a(ACC,al),width=S)
def lab(d,x,y,t,anchor='la'):d.text((x,y),t,font=mono,fill=a(MUT,.9),anchor=anchor)
X0=W*.48;Y0=M+40*S  # area del disegno, a destra

def c03():  # Property Set: entità IFC e insiemi di proprietà
    im,d=base('03','Property Set IFC','Parametri del committente, da Revit all\'IFC')
    ex,ey=X0+10*S,Y0+70*S;box(d,ex,ey,92*S,44*S);lab(d,ex+8*S,ey+10*S,'IfcWall');lab(d,ex+8*S,ey+24*S,'GlobalId',)
    for i,(nm,k) in enumerate([('Pset_WallCommon',5),('Pset_Provincia',3),('Pset_Manutenzione',4)]):
        px,py=X0+160*S,Y0+i*76*S;bez(d,(ex+92*S,ey+22*S),(ex+130*S,ey+22*S),(px-40*S,py+12*S),(px,py+12*S),.8)
        box(d,px,py,118*S,24*S+k*9*S,.9);lab(d,px+7*S,py+7*S,nm)
        for j in range(k):
            y=py+24*S+j*9*S;d.line([(px+7*S,y),(px+60*S,y)],fill=a(INK,.28),width=S);d.line([(px+70*S,y),(px+108*S,y)],fill=a(ACC,.55),width=S)
    return im
def c04():  # Dynamo: grafo di nodi e sostituzione del collegamento
    im,d=base('04','IFC collegato con Dynamo','Rileva posizione e rotazione, poi sostituisce')
    N=[(X0+10*S,Y0+30*S),(X0+10*S,Y0+110*S),(X0+120*S,Y0+70*S),(X0+120*S,Y0+165*S)]
    for (x,y) in N:d.rounded_rectangle([x,y,x+80*S,y+30*S],radius=4*S,outline=a(ACC,.9),width=round(1.2*S));dot(d,x+80*S,y+15*S,2.5);dot(d,x,y+15*S,2.5,fill=False)
    for i,j in [(0,2),(1,2),(1,3)]:bez(d,(N[i][0]+80*S,N[i][1]+15*S),(N[i][0]+105*S,N[i][1]+15*S),(N[j][0]-25*S,N[j][1]+15*S),(N[j][0],N[j][1]+15*S),.8)
    for (x,y),t in zip(N,['Fotografia','Origine','Rotazione','Sostituzione']):lab(d,x+8*S,y+10*S,t)
    cx,cy=X0+240*S,Y0+100*S;box(d,cx-34*S,cy-34*S,68*S,68*S,.5,dash=True)
    ang=math.radians(12);pts=[(cx+r*math.cos(ang+t)*1.0,cy+r*math.sin(ang+t)) for r,t in [(48*S,math.radians(45+90*k)) for k in range(4)]]
    ln(d,pts+[pts[0]],1);d.arc([cx-24*S,cy-24*S,cx+24*S,cy+24*S],0,12,fill=a(ACC,.9),width=S);lab(d,cx-52*S,cy+52*S,'rotazione 12°')
    d.line([(cx-6*S,cy),(cx+6*S,cy)],fill=a(INK,.7),width=S);d.line([(cx,cy-6*S),(cx,cy+6*S)],fill=a(INK,.7),width=S)
    return im
def c05():  # AutoCAD: tavole sovrapposte e punto di riferimento comune
    im,d=base('05','AutoCAD 2026: xrif e stampa','Un riferimento comune, tavole che non si muovono')
    ox,oy=X0+140*S,Y0+100*S
    for k,(dx,dy,al) in enumerate([(-120,-80,.35),(-95,-60,.55),(-70,-40,.9)]):box(d,ox+dx*S,oy+dy*S,190*S,120*S,al,dash=(k<2))
    d.line([(ox-140*S,oy+60*S),(ox+110*S,oy+60*S)],fill=a(INK,.25),width=S);d.line([(ox,oy-100*S),(ox,oy+90*S)],fill=a(INK,.25),width=S)
    d.ellipse([ox-9*S,oy+51*S,ox+9*S,oy+69*S],outline=a(ACC,1),width=round(1.4*S));dot(d,ox,oy+60*S,2)
    ln(d,[(ox,oy+60*S),(ox+60*S,oy+60*S)],1,1.6);ln(d,[(ox,oy+60*S),(ox,oy)],1,1.6)
    lab(d,ox+64*S,oy+56*S,'X');lab(d,ox+4*S,oy-4*S,'Y',anchor='ls');lab(d,ox-14*S,oy+76*S,'punto comune',anchor='ra')
    return im
def c08():  # i-project: schema unifilare
    im,d=base('08','Progettazione elettrica','Il flusso di lavoro con i-project, in nove fasi')
    bx,by=X0+10*S,Y0+40*S;ln(d,[(bx,by),(bx+260*S,by)],1,2.4);lab(d,bx,by-14*S,'QG · 400 V')
    ln(d,[(bx+130*S,by-34*S),(bx+130*S,by)],.9);dot(d,bx+130*S,by-34*S,3,fill=False)
    for i in range(5):
        x=bx+20*S+i*55*S;ln(d,[(x,by),(x,by+30*S)],.9);box(d,x-8*S,by+30*S,16*S,16*S,.9);ln(d,[(x-8*S,by+46*S),(x+8*S,by+30*S)],.9)
        ln(d,[(x,by+46*S),(x,by+120*S)],.7);d.line([(x-6*S,by+120*S),(x+6*S,by+120*S)],fill=a(ACC,.9),width=S)
        lab(d,x,by+136*S,'L%d'%(i+1),anchor='mm')
    return im
def c11():  # linguaggi: dal tasto al modello
    im,d=base('11','Linguaggi di programmazione','Dal tasto premuto al modello che cambia')
    kx,ky=X0,Y0+70*S
    for r in range(8):
        for c in range(8):
            on=(r*3+c*5+r*c)%7<3;x,y=kx+c*11*S,ky+r*11*S;d.ellipse([x-2.2*S,y-2.2*S,x+2.2*S,y+2.2*S],fill=a(ACC,.95) if on else None,outline=a(INK,.3) if not on else None,width=S)
    ln(d,[(kx+82*S,ky+38*S),(kx+120*S,ky+38*S),(kx+140*S,ky+10*S),(kx+180*S,ky+10*S)],.9);dot(d,kx+180*S,ky+10*S,2.5)
    cx,cy,s=kx+235*S,ky+20*S,40*S;top=[(cx,cy-s),(cx+s*.87,cy-s*.5),(cx,cy),(cx-s*.87,cy-s*.5)]
    ln(d,top+[top[0]]);ln(d,[(cx-s*.87,cy-s*.5),(cx-s*.87,cy+s*.5),(cx,cy+s),(cx+s*.87,cy+s*.5),(cx+s*.87,cy-s*.5)]);ln(d,[(cx,cy),(cx,cy+s)])
    lab(d,kx,ky-16*S,'01001011  tasto');lab(d,cx,cy+s+16*S,'modello',anchor='mm')
    return im
for k,f in [('03',c03),('04',c04),('05',c05),('08',c08),('11',c11)]:
    im=f().convert('RGB').resize((600,400),Image.LANCZOS);im.save(OUT+'manuale-'+k+'.webp',quality=86,method=6)
    im.save('/tmp/claude-0/-home-user-mscigliuolo-github-io/3bbcc406-91d1-5415-a43b-de0ade14353b/scratchpad/img/cov-'+k+'.png')
    print(k,os.path.getsize(OUT+'manuale-'+k+'.webp')//1024,'KB')
