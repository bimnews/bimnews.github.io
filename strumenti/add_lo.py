# Lingua della fonte principale (lo) e titolo/sintesi in quella lingua (tl/xl) per le notizie
# con fonte in fr, de, es, pt, ru, ar, zh, ja, ko. Regola di Marco (15/11/2026):
# sito in italiano -> t/x; sito nella lingua della fonte -> tl/xl (o te/xe se la fonte è inglese); altrimenti -> te/xe.
import json,glob
P='assets/notizie.json'
d=json.load(open(P,encoding='utf-8'))
L={}
for f in sorted(glob.glob('strumenti/notizie_lo_*.tsv')):
    for l in open(f,encoding='utf-8'):
        l=l.rstrip('\n')
        if l:
            i,lo,t,x=l.split('\t');L[i]=(lo,t,x)
IT=('bimportale','ibimi','lavoripubblici','ance.it','biblus','infobuild','ediltecnico','ingenio-web','archiproducts','assolombarda','certifico','segretaricomunali')
for a in d['arts']:
    if a['id'] in L:
        a['lo'],a['tl'],a['xl']=L[a['id']]
    elif 'lo' not in a:
        u=a['src'][0][1]
        a['lo']='it' if any(k in u for k in IT) else 'en'
open(P,'w',encoding='utf-8').write('{"weeks":'+json.dumps(d['weeks'],ensure_ascii=False)+',\n"arts":[\n'+',\n'.join(json.dumps(a,ensure_ascii=False) for a in d['arts'])+'\n]}\n')
from collections import Counter
print(Counter(a['lo'] for a in d['arts']))
