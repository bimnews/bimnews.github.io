// estrae i blocchi di testo fisso del sito (con il loro HTML interno) da tradurre
const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
const V=['home','bim-news','bim-ai','bim-accademia','bim-5-minuti','video','chi-sono','portfolio','studio','proposte','wip','fuori','libri','agenda','faq','mappa'];
const all=new Map();
for(const v of V){await p.goto('http://localhost:8765/#'+v);await p.waitForTimeout(1600);
 await p.evaluate(()=>{document.querySelectorAll('details').forEach(d=>d.open=true);document.querySelectorAll('.acc-tri').forEach(b=>{if(b.getAttribute('aria-expanded')==='false')b.click()});const a=document.getElementById('mm-all');if(a)a.click()});await p.waitForTimeout(400);
 const r=await p.evaluate(()=>{
  const EX='.art,.latest,#ac-list,.ac-card,.ag-list,.ag-item,.fs-it,.vd-card,.vd-grid,.vu-grid,.ch-grid,.fb-track,.fb-det,#t2,#t2-det,script,style,#oggi,#reader,#tour,.kf-row,.lg-list,#vis-list,.map-hud,#map-where,.cad-card,.bim-card,svg';
  const BL='P,LI,H1,H2,H3,H4,H5,H6,DT,DD,SUMMARY,FIGCAPTION,TH,TD,BUTTON,LABEL,OPTION,CITE,LEGEND';
  const INL='SPAN,A,SMALL,B,I,STRONG,EM,KBD,CODE,TIME';
  const norm=s=>s.replace(/\s+/g,' ').trim();
  const out=[];
  function clean(e){return norm(e.innerHTML)}
  function tnodes(e){const w=document.createTreeWalker(e,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){if(n.parentElement.closest('svg,script,style'))continue;const t=norm(n.nodeValue);if(t&&/[a-zàèéìòù]{2}/i.test(t))out.push({k:t,m:'text',h:t,tag:'#node'})}}
  document.querySelectorAll(BL).forEach(e=>{if(e.closest(EX))return;
    if(e.querySelector('p,li,h1,h2,h3,h4,h5,h6,dt,dd,ul,ol,div,table,section,article'))return;
    const t=norm(e.textContent);if(!t||!/[a-zàèéìòù]{2}/i.test(t))return;
    const risky=e.querySelector('svg,img,input,select,textarea,canvas,button,[id]')||e.id&&e.children.length;
    if(risky){tnodes(e);return}
    const rich=e.children.length?'html':'text';
    out.push({k:t,m:rich,h:rich==='html'?clean(e):t,tag:e.tagName})});
  // testi sciolti dentro DIV/ARTICLE/SECTION (senza un blocco intorno)
  document.querySelectorAll('div,article,section,header,footer,nav,figure,blockquote,aside').forEach(e=>{if(e.closest(EX))return;
    [...e.childNodes].forEach(n=>{if(n.nodeType===3&&norm(n.nodeValue).length>1&&/[a-zàèéìòù]{2}/i.test(n.nodeValue)){const t=norm(n.nodeValue);out.push({k:t,m:'text',h:t,tag:'#text'})}
      else if(n.nodeType===1&&['SPAN','A','SMALL','B','STRONG','EM','I','TIME'].includes(n.tagName)&&!n.closest(BL)&&!n.querySelector('p,li,div')){const t=norm(n.textContent);if(t&&/[a-zàèéìòù]{2}/i.test(t)){if(n.querySelector('svg,img,[id]')||n.id&&n.children.length){tnodes(n)}else{const rich=n.children.length?'html':'text';out.push({k:t,m:rich,h:rich==='html'?clean(n):t,tag:n.tagName})}}}})});
  // attributi visibili
  document.querySelectorAll('[placeholder],[title],[aria-label]').forEach(e=>{if(e.closest('script,style,.art,.ac-card,.ag-item,.vd-card'))return;['placeholder','title','aria-label'].forEach(a=>{const v=e.getAttribute(a);if(v&&/[a-zàèéìòù]{3}/i.test(v)&&!/^https?:/.test(v))out.push({k:norm(v),m:'attr',h:norm(v),tag:'@'+a})})});
  // tutto il resto: ogni testo visibile non ancora raccolto (per esempio le voci della Mappa del sito)
  const seen=new Set(out.map(o=>o.k));const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let x;
  while(x=w.nextNode()){const e=x.parentElement;if(!e||e.closest(EX))continue;const t=norm(x.nodeValue);if(!t||!/[a-zàèéìòù]{2}/i.test(t)||seen.has(t))continue;
    let inBlock=false;for(let q=e;q&&q!==document.body;q=q.parentElement){const k=norm(q.textContent);if(seen.has(k)){inBlock=true;break}}
    if(!inBlock){seen.add(t);out.push({k:t,m:'text',h:t,tag:'#rest'})}}
  return out});
 r.forEach(o=>{if(!all.has(o.k))all.set(o.k,o)})}
const arr=[...all.values()];let w=0;arr.forEach(o=>w+=o.k.split(' ').length);
fs.writeFileSync(process.argv[2],JSON.stringify(arr));const c={};arr.forEach(o=>c[o.m]=(c[o.m]||0)+1);console.log('voci',arr.length,'parole',w,JSON.stringify(c));await b.close()})()
