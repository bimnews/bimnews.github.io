import sys,os
SK='/root/.claude/skills/synced/bbb5bd2f-7dc1-479e-935c-6bde90469bb2_c4d8bf62-0236-4cd2-a06c-5eb4266d5188/slack-gif-creator'
sys.path.insert(0,SK)
from core.gif_builder import GIFBuilder
from core.easing import interpolate
from PIL import Image,ImageDraw,ImageFont
F='/root/.claude/skills/synced/bbb5bd2f-7dc1-479e-935c-6bde90469bb2_c4d8bf62-0236-4cd2-a06c-5eb4266d5188/canvas-design/canvas-fonts/'
W,H=480,300
BG=(13,17,21);PAN=(20,26,32);LINE=(36,45,54);INK=(232,236,239);MUT=(141,152,163);ACC=(231,154,120);OK=(124,196,143)
mono=ImageFont.truetype(F+'JetBrainsMono-Regular.ttf',13);monob=ImageFont.truetype(F+'JetBrainsMono-Bold.ttf',13)
sm=ImageFont.truetype(F+'JetBrainsMono-Regular.ttf',10);tt=ImageFont.truetype(F+'InstrumentSans-Bold.ttf',15)
STEPS=['APPLOAD','Scegli .lsp','Carica','Comando']
def frame(step,t):
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    # passi in alto
    for i,s in enumerate(STEPS):
        x=16+i*114;on=i==step;done=i<step
        d.rounded_rectangle([x,14,x+106,40],radius=6,fill=PAN if not on else (40,30,26),outline=ACC if on else LINE,width=2)
        d.text((x+10,27),str(i+1),font=monob,fill=ACC if on else (OK if done else MUT),anchor='lm')
        d.text((x+24,27),s if len(s)<14 else s[:13]+'…',font=sm,fill=INK if on else MUT,anchor='lm')
    # area disegno con griglia leggera
    d.rounded_rectangle([16,52,W-16,H-52],radius=8,fill=PAN,outline=LINE,width=2)
    for x in range(36,W-16,24):d.line([(x,54),(x,H-54)],fill=(24,31,38))
    # riga di comando
    d.rounded_rectangle([16,H-44,W-16,H-14],radius=6,fill=(9,12,15),outline=LINE,width=2)
    d.text((28,H-29),'Comando:',font=mono,fill=MUT,anchor='lm')
    def typed(txt,t):n=int(len(txt)*min(1,t*1.6));cur='▌' if (int(t*20)%2==0) else ' ';d.text((104,H-29),txt[:n]+cur,font=monob,fill=INK,anchor='lm')
    if step==0:typed('APPLOAD',t)
    if step in(1,2):
        # finestra di dialogo schematica
        y=interpolate(H,72,min(1,t*3) if step==1 else 1,'ease_out')
        d.rounded_rectangle([96,y,W-96,y+150],radius=8,fill=(26,33,40),outline=MUT,width=2)
        d.text((110,y+16),'Carica/Scarica applicazioni',font=sm,fill=INK,anchor='lm')
        files=['RETINITRASP.lsp','SOSTXRIF.lsp']
        for i,f in enumerate(files):
            fy=y+38+i*24;sel=(i==1 and (step==2 or t>.55))
            d.rounded_rectangle([110,fy,W-110,fy+20],radius=4,fill=(60,40,32) if sel else (20,26,32),outline=ACC if sel else LINE,width=2 if sel else 1)
            d.text((120,fy+10),f,font=mono,fill=INK if sel else MUT,anchor='lm')
        bx=W-196;press=step==2 and .3<t<.5
        d.rounded_rectangle([bx,y+108,bx+90,y+134],radius=5,fill=ACC if press or (step==2 and t>=.5) else (40,30,26),outline=ACC,width=2)
        d.text((bx+45,y+121),'Carica',font=monob,fill=BG if (step==2 and t>=.3) else ACC,anchor='mm')
        if step==1 and t>.55:  # puntatore sul file
            px=interpolate(W-120,W-150,min(1,(t-.55)*3),'ease_out');py=y+38+24+12;d.polygon([(px,py),(px,py+16),(px+5,py+11),(px+11,py+12)],fill=INK)
        if step==2 and t>.5:d.text((W//2,y+166),'SOSTXRIF.lsp caricato correttamente',font=sm,fill=OK,anchor='mm')
    if step==3:
        typed('SOSTXRIF',t)
        if t>.6:
            k=min(1,(t-.6)*3);w=int((W-160)*k)
            d.rounded_rectangle([80,90,80+max(10,w),190],radius=6,outline=ACC,width=2)
            for j,(lab,val) in enumerate([('xrif','sostituito'),('allineamento','verificato'),('report completo','tasto F2')]):
                if w>200:d.text((96,112+j*26),lab,font=mono,fill=MUT,anchor='lm');d.text((W-96,112+j*26),val,font=monob,fill=OK if j else INK,anchor='rm')
    return im
b=GIFBuilder(width=W,height=H,fps=10)
for step,n in [(0,16),(1,20),(2,20),(3,26)]:
    for i in range(n):b.add_frame(frame(step,i/(n-1)))
for i in range(8):b.add_frame(frame(3,1))
out='/home/user/mscigliuolo.github.io/assets/gif/appload.gif';os.makedirs(os.path.dirname(out),exist_ok=True)
b.save(out,num_colors=48,remove_duplicates=True)
print(os.path.getsize(out)//1024,'KB')
frame(2,.8).save('/tmp/claude-0/-home-user-mscigliuolo-github-io/3bbcc406-91d1-5415-a43b-de0ade14353b/scratchpad/img/gif-f2.png')
frame(3,1).save('/tmp/claude-0/-home-user-mscigliuolo-github-io/3bbcc406-91d1-5415-a43b-de0ade14353b/scratchpad/img/gif-f3.png')
