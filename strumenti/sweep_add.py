# aggiunge notizie complete (t,x,te,xe,lo,tl,xl) ad assets/notizie.json
import json,sys,datetime,runpy
P='/home/user/bimnews.github.io/assets/notizie.json'
NEW=runpy.run_path(sys.argv[1])['NEW']
d=json.load(open(P,encoding='utf-8'))
srcs={s[1] for a in d['arts'] for s in a['src']}
nid=max(int(a['id'][1:]) for a in d['arts'])
for x in NEW:
    if any(s[1] in srcs for s in x['src']):print('GIÀ PRESENTE',x['t']);continue
    dt=datetime.date.fromisoformat(x['d']);mon=dt-datetime.timedelta(days=dt.weekday());sun=mon+datetime.timedelta(days=6)
    nid+=1;o={'id':'n%d'%nid,'w':mon.isoformat(),'d':x['d'],'r':'2026-11-23','c':x['c'],'n':x['n']}
    if x.get('rg'):o['rg']=x['rg']
    o.update({'p':x['p'],'t':x['t'],'x':x['x']})
    if x.get('m'):o['m']=x['m']
    o.update({'te':x['te'],'xe':x['xe'],'lo':x['lo']})
    if x.get('tl'):o['tl']=x['tl'];o['xl']=x['xl']
    o.update({'tags':x['tags'],'src':x['src']})
    d['arts'].append(o);d['weeks'].setdefault(mon.isoformat(),{'from':mon.isoformat(),'to':sun.isoformat()})
    print('+',o['id'],o['d'],o['n'],o['t'])
d['weeks']=dict(sorted(d['weeks'].items()))
open(P,'w',encoding='utf-8').write('{"weeks":'+json.dumps(d['weeks'],ensure_ascii=False)+',\n"arts":[\n'+',\n'.join(json.dumps(a,ensure_ascii=False) for a in d['arts'])+'\n]}\n')
print('totale',len(d['arts']))
