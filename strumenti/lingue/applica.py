# Inserisce in index.html il selettore delle lingue e il dizionario (da dizionario.py)
import json,re,sys,os
sys.path.insert(0,os.path.dirname(__file__));from dizionario import L,NAMES,T,H
p='index.html';s=open(p,encoding='utf-8').read()
D={k:dict(zip(L,v)) for k,v in T.items()};B={k:dict(zip(L,v)) for k,v in H.items()}
for k,v in list(T.items())+list(H.items()):assert len(v)==len(L),k
# 1) selettore
sel='<div class="lang-set" id="lang-set"><label class="set-lab" for="lang-sel"><span aria-hidden="true" class="lang-ico">🌐</span>Lingua</label><select class="set" id="lang-sel">'+''.join('<option value="%s" lang="%s">%s</option>'%(c,c,NAMES[c]) for c in ['it']+L)+'</select></div>\n    '
a='<div class="area-set" id="area-set" hidden>'
assert s.count(a)==1;s=s.replace(a,sel+a)
# 2) blocchi del disclaimer
R=[('<p class="bn-what-h">','<p class="bn-what-h" data-i18n="bn-h">'),('<p><b class="si">È</b>','<p data-i18n="bn-si"><b class="si">È</b>'),('<p><b class="no">Non è</b>','<p data-i18n="bn-no"><b class="no">Non è</b>'),('<div class="bn-rules">','<div class="bn-rules" data-i18n="bn-rules">'),('<p class="bn-what-m">','<p class="bn-what-m" data-i18n="bn-m">')]
for x,y in R:
  assert s.count(x)==1,x;s=s.replace(x,y)
css='''/* selettore delle lingue */
.lang-set{display:flex;align-items:center;gap:.45rem}
.lang-ico{margin-right:.3rem;font-size:.85rem}
.util .wrap{column-gap:1.2rem}
[dir="rtl"]{text-align:right}
'''
k=s.index('/* disclaimer di BIM News');s=s[:k]+css+s[k:]
js='''// lingue: traduce le scritte principali senza ricaricare; la scelta resta nel browser
(function(){var D=__D__,B=__B__,sel=document.getElementById("lang-sel");if(!sel)return;
var ROOTS=[".util",".top",".home-link",".facade","#bim-news .bn-hero",".bn-what","footer"],ORIG=new WeakMap(),BORIG={},cur="it",busy=false;
function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}function load(k){try{return localStorage.getItem(k)}catch(e){return null}}
function walk(root,lang){var w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT),n;while(n=w.nextNode()){if(n.parentNode.closest("[data-i18n],script,style"))continue;
  var o=ORIG.has(n)?ORIG.get(n):n.nodeValue,t=o.trim();if(!t)continue;var tr=lang==="it"?null:(D[t]&&D[t][lang]);
  if(tr){if(!ORIG.has(n))ORIG.set(n,o);var v=o.replace(t,tr);if(n.nodeValue!==v)n.nodeValue=v;n.parentNode.setAttribute("dir",lang==="ar"?"rtl":"auto")}
  else if(ORIG.has(n)){if(n.nodeValue!==o)n.nodeValue=o;n.parentNode.removeAttribute("dir")}}}
function apply(lang){busy=true;cur=lang;document.documentElement.lang=lang==="zh"?"zh-Hans":lang;
  ROOTS.forEach(function(q){document.querySelectorAll(q).forEach(function(r){walk(r,lang)})});
  document.querySelectorAll("[data-i18n]").forEach(function(e){var k=e.dataset.i18n;if(!(k in BORIG))BORIG[k]=e.innerHTML;var h=lang==="it"?BORIG[k]:(B[k]&&B[k][lang])||BORIG[k];if(e.innerHTML!==h)e.innerHTML=h;
    if(lang==="ar")e.setAttribute("dir","rtl");else e.removeAttribute("dir")});
  var q=document.getElementById("fs-q");if(q){if(!q.dataset.ph)q.dataset.ph=q.placeholder;var ph=q.dataset.ph,tp=lang==="it"?ph:((D[ph]||{})[lang]||ph);q.placeholder=tp;q.setAttribute("aria-label",tp);q.dir=lang==="ar"?"rtl":"auto"}
  sel.value=lang;busy=false}
// le scritte che cambiano da sole (tema, versione, striscia degli eventi) vengono ritradotte
var t=0;new MutationObserver(function(){if(busy||cur==="it")return;clearTimeout(t);t=setTimeout(function(){apply(cur)},30)}).observe(document.body,{childList:true,characterData:true,subtree:true});
sel.addEventListener("change",function(){store("lingua",sel.value);apply(sel.value)});
var saved=load("lingua");if(saved&&saved!=="it"&&sel.querySelector('option[value="'+saved+'"]'))setTimeout(function(){apply(saved)},0)})();
'''.replace('__D__',json.dumps(D,ensure_ascii=False)).replace('__B__',json.dumps(B,ensure_ascii=False))
k=s.rindex('</body>');s=s[:k]+'<script>\n'+js+'</script>\n'+s[k:]
m=re.search(r'<meta name="revisione" content="(\d+) · [^"]*">',s);n=int(m.group(1))+1
s=s.replace(m.group(0),'<meta name="revisione" content="%d · 15/11/2026">'%n)
open(p,'w',encoding='utf-8').write(s);print('revisione',n)
