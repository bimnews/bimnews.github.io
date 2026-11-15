# Aggiunge titolo (te) e sintesi (xe) in inglese alle notizie, leggendo i file strumenti/notizie_en_*.tsv
# (id<TAB>titolo<TAB>sintesi). Nelle lingue diverse dall'italiano il sito mostra te/xe al posto di t/x.
import json,glob
P='assets/notizie.json'
d=json.load(open(P,encoding='utf-8'))
en={}
for f in sorted(glob.glob('strumenti/notizie_en_*.tsv')):
    for l in open(f,encoding='utf-8'):
        l=l.rstrip('\n')
        if not l: continue
        i,t,x=l.split('\t')
        en[i]=(t,x)
n=0
for a in d['arts']:
    if a['id'] in en:
        a['te'],a['xe']=en[a['id']];n+=1
open(P,'w',encoding='utf-8').write('{"weeks":'+json.dumps(d['weeks'],ensure_ascii=False)+',\n"arts":[\n'+',\n'.join(json.dumps(a,ensure_ascii=False) for a in d['arts'])+'\n]}\n')
print(n,'notizie con inglese su',len(d['arts']))
