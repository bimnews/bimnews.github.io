# Compila le traduzioni in assets/lingue/<lingua>.json
# Fonte: src/voci.json (italiano) + tr/<lingua>/pNN.txt (righe "id<TAB>traduzione").
# In più riprende il vecchio dizionario (dizionario.py) come riserva.
import json,glob,os,re,sys
B=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(os.path.dirname(B))
sys.path.insert(0,B);import dizionario as old
V={o['id']:o for o in json.load(open(B+'/src/voci.json',encoding='utf-8'))}
os.makedirs(R+'/assets/lingue',exist_ok=True)
TAG=re.compile(r'<[^>]+>')
def tags(h):return sorted(re.findall(r'<(/?[a-z0-9]+)',h))
report={}
for lang in old.L:
  T={};H={};A={};miss=[];bad=[]
  # riserva: vecchio dizionario
  for k,v in old.T.items():T[k]=v[old.L.index(lang)]
  for f in sorted(glob.glob(B+'/tr/%s/p*.txt'%lang)):
    for line in open(f,encoding='utf-8'):
      line=line.rstrip('\n')
      if not line.strip():continue
      i,_,tr=line.partition('\t');o=V.get(i)
      if not o or not tr:continue
      if o['m']=='html':
        if tags(o['h'])!=tags(tr):bad.append(i);continue
        H[o['k']]=tr
      elif o['m']=='attr':A[o['k']]=tr
      else:T[o['k']]=tr
  ex=B+'/tr/%s/extra.txt'%lang
  if os.path.exists(ex):
    for line in open(ex,encoding='utf-8'):
      k,_,v=line.rstrip('\n').partition('\t')
      if k and v:T[k]=v
  done={o['k'] for o in V.values()}&(set(T)|set(H)|set(A))
  report[lang]='%d/%d'%(len(done),len(V))+(' · tag diversi: '+','.join(bad) if bad else '')
  json.dump({'t':T,'h':H,'a':A},open(R+'/assets/lingue/%s.json'%lang,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
for k,v in report.items():print(k,v)
