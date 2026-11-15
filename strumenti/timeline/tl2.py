import json
p='index.html';s=open(p,encoding='utf-8').read()
W=[
 {"d":"mar 1975","n":"Charles M. Eastman, «The Use of Computers Instead of Drawings in Building Design»","t":"L'idea: descrivere l'edificio con il computer, non con i disegni","x":"Sull'AIA Journal Eastman presenta il Building Description System, sviluppato alla Carnegie-Mellon University: un database dell'edificio da cui ricavare piante e sezioni. È considerato il primo antenato del BIM.","l":[["AIA Journal, marzo 1975 (sommario, p. 46)","https://www.usmodernist.org/AJ/AJ-1975-03.pdf"]],"id":"eastman"},
 {"d":"dic 1992","n":"G.A. van Nederveen, F.P. Tolman, «Modelling multiple views on buildings»","t":"Compare il termine «Building Information Model»","x":"Nell'articolo sulla rivista Automation in Construction (vol. 1, n. 3) compare per la prima volta l'espressione «Building Information Model». Si diffonderà davvero solo una decina d'anni dopo.","l":[["Automation in Construction, vol. 1 n. 3","https://structurae.net/en/literature/periodicals/automation-in-construction/18784-1-3"],["Wikipedia, storia del BIM (inglese)","https://en.wikipedia.org/wiki/Building_information_modeling"]],"id":"term"},
 {"d":"set 1995","n":"Industry Alliance for Interoperability","t":"Nasce l'alleanza per l'interoperabilità","x":"Partita nel 1994 come consorzio di 12 aziende statunitensi, nel settembre 1995 l'alleanza si apre a tutti; nel maggio 1996 diventa International Alliance for Interoperability (IAI), con l'obiettivo di un formato di scambio non proprietario.","l":[["Wikipedia, buildingSMART (inglese)","https://en.wikipedia.org/wiki/BuildingSMART"]],"id":"iai"},
 {"d":"giu 1996","n":"IFC 1.0","t":"La prima versione del formato IFC","x":"Esce la prima versione delle Industry Foundation Classes, il formato aperto con cui software diversi si scambiano i modelli.","l":[["Wikipedia, Industry Foundation Classes (inglese)","https://en.wikipedia.org/wiki/Industry_Foundation_Classes"]],"id":"ifc1"},
 {"d":"2005","n":"buildingSMART","t":"L'IAI diventa buildingSMART","x":"L'alleanza cambia nome per rendere più chiaro che cosa fa: da allora buildingSMART sviluppa e mantiene l'IFC e gli altri standard openBIM.","l":[["Wikipedia, buildingSMART (inglese)","https://en.wikipedia.org/wiki/BuildingSMART"]],"id":"bs"},
 {"d":"ott 2005","n":"ISO/PAS 16739:2005","t":"L'IFC entra in ISO","x":"Il nucleo stabile di IFC2x viene pubblicato dall'ISO come specifica disponibile al pubblico (PAS). Sarà sostituita dalla ISO 16739:2013.","l":[["Scheda ISO","https://committee.iso.org/standard/38056.html"]],"id":"pas16739"},
 {"d":"2007","n":"BS 1192:2007","t":"Regno Unito: come si produce l'informazione in collaborazione","x":"La norma britannica sulla produzione collaborativa delle informazioni (nomi dei file, stati, ambiente di condivisione) è una delle due basi della futura ISO 19650.","l":[["CDBB, passaggio dalle 1192 alle ISO 19650 (inglese)","https://www.cdbb.cam.ac.uk/news/2018AugBSI_ISOTransition"]],"id":"bs1192"},
 {"d":"apr 2010","n":"ISO 29481-1:2010","t":"Information Delivery Manual","x":"Il metodo per descrivere quali informazioni servono, a chi e quando: la base dei processi di scambio.","l":[["Scheda ISO","https://committee.iso.org/standard/45501.html"]],"id":"idm"},
 {"d":"31 mag 2011","n":"Government Construction Strategy","t":"Il Regno Unito fissa l'obbligo al 2016","x":"Il governo britannico chiede il BIM 3D pienamente collaborativo su tutti i contratti di costruzione appaltati centralmente entro il 2016: è la spinta che porterà alle norme PAS 1192.","l":[["GOV.UK, la strategia","https://www.gov.uk/government/publications/government-construction-strategy"],["Designing Buildings, sintesi (inglese)","https://www.designingbuildings.co.uk/wiki/Government_Construction_Strategy_2011_2015"]],"id":"gcs"},
 {"d":"mar 2013","n":"ISO 16739:2013","t":"L'IFC diventa norma internazionale","x":"L'IFC4 è pubblicato come norma ISO a tutti gli effetti.","l":[["Scheda ISO","https://committee.iso.org/standard/51622.html"]],"id":"iso16739"},
 {"d":"2013","n":"PAS 1192-2:2013","t":"Regno Unito: la gestione informativa nella fase di consegna","x":"La specifica britannica sulla gestione delle informazioni nella fase di progetto e costruzione. Con la BS 1192 è la base della ISO 19650-2.","l":[["CDBB, passaggio dalle 1192 alle ISO 19650 (inglese)","https://www.cdbb.cam.ac.uk/news/2018AugBSI_ISOTransition"]],"id":"pas1192"},
 {"d":"26 feb 2014","n":"Direttiva 2014/24/UE, art. 22, par. 4","t":"L'Europa apre al BIM negli appalti","x":"Per lavori e concorsi di progettazione gli Stati membri possono richiedere «strumenti elettronici specifici, quali gli strumenti di simulazione elettronica per le informazioni edilizie».","l":[["Testo della direttiva (Gazzetta UE, PDF)","https://uc-cal.camcom.gov.it/download/897.html"]],"id":"dir"},
 {"d":"6 lug 2017","n":"EU BIM Task Group, Handbook","t":"Il manuale europeo per il settore pubblico","x":"Il gruppo di lavoro europeo, con enti pubblici di 21 paesi, pubblica un quadro comune per introdurre il BIM negli appalti pubblici.","l":[["NBS, presentazione (inglese)","https://www.thenbs.com/knowledge/eu-bim-task-group-launches-handbook-for-the-strategic-implementation-of-bim"],["Il manuale","https://eubim.eu/handbook/"]],"id":"eubim"},
 {"d":"7 dic 2018","n":"ISO 19650-1 e -2:2018","t":"Nasce lo standard internazionale","x":"La gestione informativa con il BIM diventa norma ISO. È l'internazionalizzazione delle norme britanniche BS 1192:2007 e PAS 1192-2:2013, che sostituisce.","l":[["Scheda ISO 19650-1","https://committee.iso.org/standard/68078.html"],["Scheda ISO 19650-2","https://committee.iso.org/standard/68080.html"]],"id":"iso19650","from":["bs1192","pas1192"]},
 {"d":"2020","n":"ISO 19650-3 e -5:2020","t":"La fase di gestione e la sicurezza","x":"Parte 3: gestione informativa nella fase di esercizio. Parte 5: sicurezza delle informazioni.","l":[["Wikipedia, ISO 19650 (inglese)","https://en.wikipedia.org/wiki/ISO_19650"]],"id":"iso19650-35"},
 {"d":"2022","n":"ISO 19650-4:2022","t":"Lo scambio di informazioni","x":"Come si scambiano e si verificano le informazioni tra le parti.","l":[["Wikipedia, ISO 19650 (inglese)","https://en.wikipedia.org/wiki/ISO_19650"]],"id":"iso19650-4"},
 {"d":"2024","n":"ISO 16739-1:2024 e ISO 7817-1:2024","t":"IFC 4.3 e il livello di fabbisogno informativo","x":"La nuova edizione dell'IFC, estesa alle infrastrutture, e la norma su quante informazioni servono davvero.","l":[],"id":"iso2024"},
 {"d":"2025","n":"ISO 19650-6:2025","t":"Salute e sicurezza","x":"Le informazioni su salute e sicurezza lungo tutta la vita dell'opera.","l":[["Wikipedia, ISO 19650 (inglese)","https://en.wikipedia.org/wiki/ISO_19650"]],"id":"iso19650-6"}
]
I0={"d":"2009","k":"UNI","n":"UNI 11337:2009","t":"La prima norma italiana sulla codifica","x":"Criteri per identificare e descrivere opere, attività e risorse in modo univoco: il primo passo verso l'interoperabilità, prima ancora della serie BIM del 2015.","b":[],"l":[["Catalogo UNI","https://store.uni.com/uni-11337-2009"]]}
# collegamenti Italia -> Mondo (nome norma italiana -> id mondo, tipo)
LINK={"D.Lgs. 50/2016, art. 23, c. 13":["dir","recepisce la direttiva"],"UNI EN ISO 19650-1 e -2:2019":["iso19650","adotta la norma ISO"],"UNI EN ISO 19650-5:2020":["iso19650-35","adotta la norma ISO"],"UNI EN ISO 19650-3:2021":["iso19650-35","adotta la norma ISO"],"UNI EN ISO 19650-4:2022":["iso19650-4","adotta la norma ISO"],"UNI EN ISO 16739-1:2024":["iso2024","adotta la norma ISO"],"UNI EN ISO 7817-1:2024":["iso2024","adotta la norma ISO"],"UNI EN ISO 19650-6:2025":["iso19650-6","adotta la norma ISO"],"D.Lgs. 36/2023, art. 43 e Allegato I.9":["iso19650","rimanda alla serie UNI EN ISO 19650"]}
html_block='''
      <div class="t2-wrap" id="b5-t2">
        <span class="label">05 · Il BIM nel tempo: il mondo e l'Italia</span>
        <p class="tl-intro">Dove nasce il BIM e come arriva da noi. Sopra il mondo, dalla prima idea del 1975 alle norme ISO; sotto l'Italia, dalla prima norma sulla codifica del 2009 all'obbligo di oggi. Le linee collegano una norma italiana a quella internazionale che recepisce. Tocca una tappa per il dettaglio e le fonti.</p>
        <div class="t2-bar"><div class="tl-filter t2-f" role="group" aria-label="Linee da mostrare"><button type="button" class="chip" data-v="" aria-pressed="true">Entrambe</button><button type="button" class="chip" data-v="w" aria-pressed="false">Solo mondo</button><button type="button" class="chip" data-v="i" aria-pressed="false">Solo Italia</button></div><label class="t2-tog"><input type="checkbox" id="t2-links" checked> Mostra i collegamenti</label></div>
        <div class="t2-scroll" id="t2-scroll" tabindex="0" aria-label="Timeline mondo e Italia, scorrevole in orizzontale"><div class="t2-canvas" id="t2"></div></div>
        <div class="fb-det" id="t2-det" aria-live="polite"><p class="fb-hint">Tocca una tappa per leggerne il dettaglio.</p></div>
      </div>
'''
css='''/* 05 · timeline doppia mondo e Italia */
.t2-wrap{display:grid;gap:.7rem;margin-top:1.4rem}
.t2-bar{display:flex;flex-wrap:wrap;align-items:center;gap:.6rem 1.2rem}
.t2-tog{font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:.35rem;cursor:pointer}
.t2-scroll{overflow-x:auto;overflow-y:hidden;border:1px solid var(--line);border-radius:var(--r);background:var(--surface);scrollbar-width:thin;cursor:grab}
.t2-scroll.drag{cursor:grabbing;user-select:none}
.t2-canvas{position:relative}
.t2-canvas svg{position:absolute;inset:0;pointer-events:none}
.t2-lane{position:absolute;left:0;font:700 .62rem var(--mono);letter-spacing:.14em;text-transform:uppercase;padding:.25rem .55rem;border-radius:0 6px 6px 0;z-index:2;position:sticky}
.t2-lab{position:absolute;left:.6rem;font:700 .64rem var(--mono);letter-spacing:.14em;text-transform:uppercase;padding:.2rem .5rem;border-radius:6px;z-index:3}
.t2-lab.w{color:var(--k-news);background:var(--k-news-s)}.t2-lab.i{color:var(--k-b5);background:var(--k-b5-s)}
.t2-ev{position:absolute;width:9.6rem;transform:translateX(-50%);text-align:left;font:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:.32rem .45rem;cursor:pointer;color:var(--ink);z-index:2;line-height:1.25}
.t2-ev b{display:block;font:700 .62rem var(--mono);letter-spacing:.04em;color:var(--muted)}
.t2-ev span{display:block;font-size:.74rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.t2-ev.w{border-top:3px solid var(--k-news)}.t2-ev.i{border-bottom:3px solid var(--k-b5)}
.t2-ev:hover,.t2-ev.on{border-color:var(--accent);box-shadow:0 0 0 2px color-mix(in srgb,var(--accent) 35%,transparent)}
.t2-ev.dim{opacity:.35}
.t2-yr{position:absolute;transform:translateX(-50%);font:600 .62rem var(--mono);color:var(--muted)}
.t2-wrap .t2-hide{display:none}
@media (prefers-reduced-motion:reduce){.t2-scroll{scroll-behavior:auto}}
'''
js=r'''
// 05 · timeline doppia: mondo sopra, Italia sotto, sullo stesso asse; le linee uniscono una norma italiana a quella internazionale che recepisce
(function(){var box=$("t2"),sc=$("t2-scroll");if(!box)return;
var W=__W__,I=[__I0__].concat(NORME),LINK=__LINK__,VIEW="",SHOW=true,OPEN=null;
var MM={gen:0,feb:1,mar:2,apr:3,mag:4,giu:5,lug:6,ago:7,set:8,ott:9,nov:10,dic:11};
function yr(d){var p=d.split(" "),y=+p[p.length-1],m=p.length>1?MM[p[p.length-2]]:6,g=p.length>2?+p[0]:15;return y+(m+(g-1)/31)/12}
// scala a tratti: gli anni lontani compressi, gli ultimi vent'anni larghi
function X(t){var a=Math.min(t,2005)-1973,b=Math.max(0,t-2005);return 40+a*30+b*150}
var E=[];W.forEach(function(e){E.push({s:"w",e:e,t:yr(e.d)})});I.forEach(function(e){E.push({s:"i",e:e,t:yr(e.d)})});
function draw(){var wv=VIEW!=="i",iv=VIEW!=="w",RW=50,ROW=[],h='',sv='',maxRow={w:0,i:0},CW=164;
  var END=X(2026.9)+90,AX=0;
  // righe senza sovrapposizioni, separate per linea
  var P={};["w","i"].forEach(function(s){var last=[];E.filter(function(o){return o.s===s}).sort(function(a,b){return a.t-b.t}).forEach(function(o){var x=X(o.t),r=0;while(last[r]!==undefined&&x-last[r]<CW)r++;last[r]=x;o.x=x;o.r=r;if(r>maxRow[s])maxRow[s]=r})});
  var top=34,hw=wv?(maxRow.w+1)*RW:0;AX=top+hw+26;var hi=iv?(maxRow.i+1)*RW:0,H=AX+26+hi+20;
  box.style.width=END+"px";box.style.height=H+"px";
  for(var y=1975;y<=2026;y++){if(y<2005&&y%5)continue;var x=X(y);h+='<span class="t2-yr" style="left:'+x+'px;top:'+(AX-8)+'px">'+y+'</span>';sv+='<line x1="'+x+'" y1="'+(AX-12)+'" x2="'+x+'" y2="'+(AX+12)+'" stroke="var(--line)"/>'}
  sv+='<line x1="20" y1="'+(AX-14)+'" x2="'+END+'" y2="'+(AX-14)+'" stroke="var(--k-news)" stroke-width="2"/><line x1="20" y1="'+(AX+14)+'" x2="'+END+'" y2="'+(AX+14)+'" stroke="var(--k-b5)" stroke-width="2"/>';
  if(wv)h+='<span class="t2-lab w" style="top:6px">Mondo</span>';if(iv)h+='<span class="t2-lab i" style="top:'+(H-26)+'px">Italia</span>';
  var pos={};
  E.forEach(function(o,k){if((o.s==="w"&&!wv)||(o.s==="i"&&!iv))return;
    var y=o.s==="w"?AX-14-26-o.r*RW-34:AX+14+26+o.r*RW,ly=o.s==="w"?AX-14:AX+14;o.cy=o.s==="w"?y+34:y;
    sv+='<line x1="'+o.x+'" y1="'+ly+'" x2="'+o.x+'" y2="'+o.cy+'" stroke="'+(o.s==="w"?"var(--k-news)":"var(--k-b5)")+'" stroke-opacity=".55"/><circle cx="'+o.x+'" cy="'+ly+'" r="4" fill="'+(o.s==="w"?"var(--k-news)":"var(--k-b5)")+'"/>';
    var lab=o.e.t;h+='<button type="button" class="t2-ev '+o.s+(OPEN===o?" on":"")+'" data-k="'+k+'" style="left:'+o.x+'px;top:'+y+'px" title="'+esc(o.e.n)+'"><b>'+esc(o.e.d)+'</b><span>'+esc(o.e.n)+'</span></button>';
    if(o.e.id)pos[o.e.id]=o});
  if(SHOW&&wv){ // dentro il mondo: le norme britanniche da cui nasce la ISO 19650
    W.forEach(function(e){(e.from||[]).forEach(function(f){var a=pos[f],b=pos[e.id];if(a&&b)sv+='<path d="M'+a.x+' '+(AX-14)+' C'+a.x+' '+(AX-40)+' '+b.x+' '+(AX-40)+' '+b.x+' '+(AX-14)+'" fill="none" stroke="var(--k-news)" stroke-width="1.6" stroke-dasharray="4 3"/>'})})}
  if(SHOW&&wv&&iv)E.forEach(function(o){if(o.s!=="i")return;var L=LINK[o.e.n];if(!L||!pos[L[0]])return;var a=pos[L[0]],on=OPEN&&(OPEN===o||OPEN===a);
    sv+='<path d="M'+a.x+' '+(AX-14)+' C'+a.x+' '+AX+' '+o.x+' '+AX+' '+o.x+' '+(AX+14)+'" fill="none" stroke="var(--mark)" stroke-width="'+(on?3:1.6)+'" stroke-opacity="'+(OPEN&&!on?.25:.9)+'"/>'});
  box.innerHTML='<svg width="'+END+'" height="'+H+'" aria-hidden="true">'+sv+'</svg>'+h}
function det(o){var e=o.e,L=o.s==="i"?LINK[e.n]:null,rel=[];
  if(L){var w=W.filter(function(x){return x.id===L[0]})[0];if(w)rel.push('<p class="t2-rel"><b>Mondo:</b> '+esc(L[1])+' · '+esc(w.n)+'</p>')}
  if(o.s==="w"){I.forEach(function(x){var l=LINK[x.n];if(l&&l[0]===e.id)rel.push('<p class="t2-rel"><b>Italia:</b> '+esc(x.n)+' ('+esc(x.d)+')</p>')});
    (e.from||[]).forEach(function(f){var w=W.filter(function(x){return x.id===f})[0];if(w)rel.push('<p class="t2-rel"><b>Nasce da:</b> '+esc(w.n)+'</p>')})}
  $("t2-det").innerHTML='<div class="tl-det fb-open"><div class="fb-dh"><span class="big">'+esc(e.d)+'</span><span class="fbk '+(o.s==="w"?"ISO":e.k)+'">'+(o.s==="w"?"Mondo":"Italia")+'</span></div><h4>'+esc(e.t)+'</h4><p><strong>'+esc(e.n)+'.</strong> '+esc(e.x)+'</p>'+(e.b&&e.b.length?'<ul>'+e.b.map(function(x){return"<li>"+esc(x)+"</li>"}).join("")+'</ul>':'')+rel.join("")+(e.l&&e.l.length?'<div class="tl-links">'+e.l.map(function(z){return'<a href="'+z[1]+'" target="_blank" rel="noopener">'+esc(z[0])+' ↗</a>'}).join("")+'</div>':'')+'</div>'}
box.addEventListener("click",function(e){var b=e.target.closest(".t2-ev");if(!b||sc.classList.contains("moved"))return;var o=E[+b.dataset.k];OPEN=OPEN===o?null:o;draw();if(OPEN)det(OPEN);else $("t2-det").innerHTML='<p class="fb-hint">Tocca una tappa per leggerne il dettaglio.</p>'});
document.querySelector(".t2-f").addEventListener("click",function(e){var b=e.target.closest(".chip");if(!b)return;VIEW=b.dataset.v;document.querySelectorAll(".t2-f .chip").forEach(function(c){c.setAttribute("aria-pressed",c===b)});draw()});
$("t2-links").addEventListener("change",function(){SHOW=this.checked;draw()});
(function(){var down=false,x0=0,s0=0;sc.addEventListener("pointerdown",function(e){if(e.pointerType!=="mouse")return;down=true;x0=e.clientX;s0=sc.scrollLeft;sc.classList.remove("moved")});
  addEventListener("pointermove",function(e){if(!down)return;var dx=e.clientX-x0;if(Math.abs(dx)>4){sc.classList.add("drag","moved")}sc.scrollLeft=s0-dx});
  addEventListener("pointerup",function(){down=false;sc.classList.remove("drag");setTimeout(function(){sc.classList.remove("moved")},0)})})();
draw();
// si apre sugli ultimi anni, dove le due linee si intrecciano
var seen=false;new IntersectionObserver(function(en){if(en[0].isIntersecting&&!seen){seen=true;sc.scrollLeft=X(2013)-40}}).observe(sc);
})();
'''
js=js.replace('__W__',json.dumps(W,ensure_ascii=False)).replace('__I0__',json.dumps(I0,ensure_ascii=False)).replace('__LINK__',json.dumps(LINK,ensure_ascii=False))
# inserimenti
anchor='\n      <div class="dm-wrap" id="b5-dim">'
assert s.count(anchor)==1;s=s.replace(anchor,html_block+anchor)
k=s.index('/* 09 certificazioni');s=s[:k]+css+s[k:]
a='document.querySelectorAll(".tl-filter .chip").forEach(function(c){c.setAttribute("aria-pressed",c===b)});tl()});'
assert s.count(a)==1;s=s.replace(a,a+js)
s=s.replace('<button type="button" data-go="norme">05 Le norme</button>','<button type="button" data-go="norme">05 Le norme</button><button type="button" data-go="b5-t2">05 Mondo e Italia</button>',1)
s=s.replace('.t2-ev.dim{opacity:.35}','.t2-ev.dim{opacity:.35}\n.t2-rel{margin:.3rem 0 0;font-size:.86rem}.t2-rel b{color:var(--mark)}')
open(p,'w',encoding='utf-8').write(s);print('ok')
