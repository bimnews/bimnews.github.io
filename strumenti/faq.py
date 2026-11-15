import re,json,html
p='/home/user/mscigliuolo.github.io/index.html'
s=open(p,encoding='utf-8').read()
def rep(a,b,c=1):
    global s
    assert s.count(a)==c,(s.count(a),a[:80]);s=s.replace(a,b)

# lingue: [italiano, nome nella lingua]
MISURATE=[("Arabo","العربية"),("Bulgaro","български"),("Catalano","català"),("Ceco","čeština"),("Cinese","中文"),("Coreano","한국어"),("Curdo sorani","کوردی"),("Danese","dansk"),("Ebraico","עברית"),("Estone","eesti"),("Finlandese","suomi"),("Francese","français"),("Giapponese","日本語"),("Greco","ελληνικά"),("Indonesiano","Bahasa Indonesia"),("Inglese","English"),("Italiano","italiano"),("Lettone","latviešu"),("Lituano","lietuvių"),("Malayalam","മലയാളം"),("Norvegese","norsk"),("Olandese","Nederlands"),("Persiano","فارسی"),("Polacco","polski"),("Portoghese","português"),("Russo","русский"),("Spagnolo","español"),("Svedese","svenska"),("Tagiko","тоҷикӣ"),("Tamil","தமிழ்"),("Tedesco","Deutsch"),("Thai","ไทย"),("Turco","Türkçe"),("Ucraino","українська"),("Ungherese","magyar"),("Vietnamita","Tiếng Việt")]
IN_VERIFICA=[("Afrikaans","Afrikaans"),("Albanese","shqip"),("Amarico","አማርኛ"),("Armeno","հայերեն"),("Azero","azərbaycanca"),("Basco","euskara"),("Bengalese","বাংলা"),("Birmano","မြန်မာ"),("Bosniaco","bosanski"),("Croato","hrvatski"),("Filippino","Filipino"),("Galiziano","galego"),("Georgiano","ქართული"),("Hausa","Hausa"),("Hindi","हिन्दी"),("Irlandese","Gaeilge"),("Islandese","íslenska"),("Kazako","қазақ"),("Khmer","ខ្មែរ"),("Kinyarwanda","Ikinyarwanda"),("Lao","ລາວ"),("Lussemburghese","Lëtzebuergesch"),("Macedone","македонски"),("Malese","Bahasa Melayu"),("Malgascio","malagasy"),("Maltese","Malti"),("Marathi","मराठी"),("Mongolo","монгол"),("Nepalese","नेपाली"),("Rumeno","română"),("Serbo","српски"),("Singalese","සිංහල"),("Slovacco","slovenčina"),("Sloveno","slovenščina"),("Somalo","Soomaali"),("Swahili","Kiswahili"),("Urdu","اردو"),("Uzbeko","oʻzbekcha"),("Yoruba","Yorùbá"),("Zulu","isiZulu")]
def chips(L,cls):return '<ul class="lg-list '+cls+'">'+''.join('<li><b>%s</b><span lang="">%s</span></li>'%(html.escape(a),html.escape(b)) for a,b in L)+'</ul>'

Q=[
("Il sito",[
 ("Chi gestisce questo sito?","Il sito è gestito dall'ingegner Marco Scigliuolo ed è generato tramite Claude, l'assistente di intelligenza artificiale di Anthropic. Nella pagina <a href=\"#chi-sono\">Il curatore</a> trovi profilo, portfolio, manuali e progetti."),
 ("Come vengono aggiornate le notizie e quanto sono attendibili?","Le notizie vengono aggiornate ogni settimana, il lunedì, in modo completamente automatico: la ricerca la svolge Claude seguendo criteri precisi stabiliti dall'autore, cioè quali fonti sono ammesse, quali temi contano, in quali lingue cercare e che cosa verificare prima di pubblicare. Li trovi nelle risposte qui sotto. Ogni notizia riporta il link alla fonte originale: per una decisione importante, fai sempre riferimento a quella."),
 ("Come posso contattare l'autore?","Tramite <a href=\"https://www.linkedin.com/in/marco-scigliuolo/\" target=\"_blank\" rel=\"noopener\">LinkedIn ↗</a>. <b>Nota bene:</b> il sito è curato da una sola persona, quindi l'autore non sempre riesce a rispondere subito alle domande."),
 ("L'autore è aperto a collaborazioni?","Dipende da che cosa si vuole fare insieme. Il sito è completamente automatizzato e l'autore lo ritocca a mano solo di rado, quindi le collaborazioni possibili riguardano la stesura di articoli specifici. All'autore piacerebbe molto ascoltare i problemi tipici che si affrontano nel lavoro, trovare insieme le soluzioni e magari pubblicarle insieme. I collaboratori vengono sempre citati come autori degli articoli; la pubblicazione la fa personalmente l'autore, che non condivide con nessuno l'accesso al sito."),
 ("Chi sovvenziona o sponsorizza il sito?","Nessuno. Il sito non ha sponsor, pubblicità né finanziamenti: tutte le spese sono a carico del curatore, cioè l'abbonamento al piano Pro di Claude con cui il sito viene generato e aggiornato, e il tempo che il curatore dedica a gestirlo. Il sito è ospitato gratuitamente su GitHub Pages."),
 ("Che cos'è BIM News?","Una rassegna settimanale sul BIM (Building Information Modeling, il metodo di progettare e gestire le opere con un modello digitale fatto di oggetti che portano con sé le loro informazioni). Raccoglie le notizie da tutto il mondo, le riassume in italiano, le colloca sulla mappa e mette sempre il link alla fonte. Accanto alle notizie ci sono una guida per chi comincia, le ricerche universitarie tradotte, video, agenda e manuali."),
 ("Devo registrarmi o pagare?","No. Il sito è gratuito e senza registrazione."),
]),
("Le notizie",[
 ("Da dove arrivano le notizie?","Da tre tipi di fonti. Le <b>fonti istituzionali</b>: governi, ministeri, gazzette ufficiali, enti normativi, sezioni nazionali di buildingSMART, stazioni appaltanti, università, banche di sviluppo; città, regioni e province solo quando danno un contributo concreto, come un obbligo, un regolamento o una grande opera. La <b>stampa autorevole</b>: testate di settore con redazione, grandi quotidiani nazionali, agenzie di stampa. Le <b>grandi aziende</b>, solo per fatti di peso reale e mai per pubblicità. Restano fuori blog personali, siti di singoli studi, rivenditori, cronaca locale e social."),
 ("Come scegliete che cosa pubblicare?","Pubblichiamo un fatto quando cambia qualcosa per chi progetta o costruisce in quel paese: strategie nazionali e obblighi, norme adottate, grandi opere pubbliche in BIM, primi progetti pilota, eventi di riferimento. Il criterio di fondo è l'inclusività: a parità di interesse scegliamo la notizia che aiuta qualcuno a cominciare. I dettagli sono nel riquadro «Come scegliamo le notizie» di <a href=\"#bim-news\">BIM News</a>."),
 ("Perché sulla mappa alcuni paesi sono ancora vuoti?","Perché la ricerca non li ha ancora raggiunti, non perché lì il BIM manchi. È in corso una ricerca a tappeto, area per area, nella lingua di ogni paese; ogni settimana una parte del lavoro va ai paesi ancora vuoti."),
 ("Che cosa indicano i numeri sulla mappa?","Quante notizie ci sono per continente, paese o regione. Tocca un continente, poi un paese e una regione per vedere le notizie di quel luogo."),
 ("Perché alcune notizie hanno l'etichetta «Archivio»?","Sono notizie che abbiamo raccolto più di sette giorni dopo la loro uscita, per completare la storia di un paese o di una norma."),
 ("Perché non ci sono notizie prima del 2015?","Il 2015 è l'anno in cui è uscita la prima parte della UNI 11337, la serie di norme italiane sul BIM. Lo usiamo come punto di partenza comune per tutto il mondo."),
 ("Che cosa trovo in BIM & AI?","Le notizie in cui il tema principale è l'intelligenza artificiale applicata al BIM e alle costruzioni, con la stessa mappa e gli stessi filtri di BIM News."),
]),
("Le lingue della ricerca",[
 ("In che lingue cercate le notizie?","Cerchiamo ogni notizia nella lingua del paese in cui nasce, non solo in inglese. Qui sotto trovi le lingue in cui cerchiamo e quelle che stiamo verificando.<h4 class=\"lg-h\">Lingue in cui cerchiamo ("+str(len(MISURATE))+")</h4>"+chips(MISURATE,"lg-yes")+"<h4 class=\"lg-h\">Lingue in verifica ("+str(len(IN_VERIFICA))+")</h4><p>Sono le lingue nazionali di paesi in cui ci aspettiamo attività sul BIM. Le cerchiamo una per una: se dopo ricerche serie non troviamo fonti adatte, la lingua esce dall'elenco; se le troviamo, passa tra quelle qui sopra.</p>"+chips(IN_VERIFICA,"lg-test")),
 ("Come avete scelto queste lingue?","Nel mondo si parlano circa 7.100–7.200 lingue: è l'ordine di grandezza indicato da Ethnologue, il catalogo di riferimento. Solo una piccola parte ha contenuti digitali su temi tecnici. Per misurarlo abbiamo usato un indicatore pubblico e verificabile: le edizioni di Wikipedia. Wikipedia ha 348 edizioni linguistiche attive; la voce sull'intelligenza artificiale c'è in 185, quella sul BIM in 38. Le lingue con la voce sul BIM (tolto l'esperanto, che non ha un paese di riferimento) sono il punto di partenza della ricerca. A queste aggiungiamo, in verifica, le lingue nazionali dei paesi dove ci aspettiamo attività. Dati rilevati a novembre 2026."),
]),
("Le altre pagine",[
 ("Non conosco il BIM: da dove parto?","Da <a href=\"#bim-5-minuti\">BIM in 5 minuti</a>: che cos'è, a che cosa serve, le norme, le sigle, le dimensioni dal 3D al 10D e i risultati concreti misurati dalle ricerche."),
 ("Che cos'è BIM Accademia? Chi traduce gli abstract?","<a href=\"#bim-accademia\">BIM Accademia</a> raccoglie articoli scientifici sul BIM in accesso aperto, con licenza Creative Commons BY, che permette di riprodurre e tradurre l'abstract. Le traduzioni sono nostre e sono indicate come tali; per citare un articolo vale sempre il testo originale, a un clic."),
 ("Dove trovo eventi, webinar e scadenze?","Nell'<a href=\"#agenda\">Agenda</a> e nella striscia in fondo alla home. Con «La tua area», nelle impostazioni in alto, vedi prima gli appuntamenti del tuo continente."),
 ("Che cosa sono i manuali nella pagina del curatore?","Guide pratiche per chi progetta: Property Set per l'IFC, Dynamo, AutoCAD, progettazione elettrica, linguaggi di programmazione. Le trovi in <a href=\"#studio\">Nello studio</a>, da leggere online o scaricare in PDF."),
 ("Dove trovo video e lezioni universitarie?","Nella pagina <a href=\"#video\">Video</a>: webinar e conferenze registrati, canali gratuiti e lezioni di università."),
]),
("Usare il sito",[
 ("Che differenza c'è tra versione completa ed essenziale?","La versione completa ha mappa interattiva, foto, animazioni e caratteri del sito. L'essenziale scarica solo testi e notizie: è pensata per connessioni lente e per chi preferisce meno movimento. Si cambia con il tasto in alto a destra."),
 ("Come passo dal tema scuro a quello chiaro?","Con il tasto «Tema chiaro» o «Tema scuro» in alto a destra. Il sito ricorda la scelta."),
 ("Il sito è molto grande: c'è una guida?","Sì, tre. La <b>Guida al sito</b>, dal tasto in alto nella home, mostra passo per passo le parti principali. La <a href=\"#mappa\">Mappa del sito</a> elenca tutte le pagine con una breve descrizione. E questa pagina risponde alle domande più frequenti."),
 ("Come segnalo un errore o una notizia?","Scrivi all'autore su <a href=\"https://www.linkedin.com/in/marco-scigliuolo/\" target=\"_blank\" rel=\"noopener\">LinkedIn ↗</a>, con il link alla fonte: ogni segnalazione viene verificata prima di essere pubblicata."),
]),
]
body=''
for g,items in Q:
    body+='<div class="faq-g"><h3>'+g+'</h3>'
    for q,a in items:
        body+='<details class="faq-q"><summary>'+q+'</summary><div class="faq-a"><p>'+a+'</p></div></details>'
    body+='</div>'
body=body.replace('<p><h4','<h4').replace('</ul></p>','</ul>')
PAGE='''  <section id="faq">
    <div class="content">
      <h2>Domande frequenti</h2>
      <p class="lead">Le domande che ci si pone esplorando BIM News: che cosa trovi nelle varie pagine, come scegliamo le notizie, in che lingue cerchiamo, come si usa il sito.</p>
      <label class="faq-search"><span class="f-lab">Cerca tra le domande</span><input type="search" id="faq-q" placeholder="per esempio: lingue, mappa, traduzioni"></label>
      <div class="faq-list" id="faq-list">'''+body+'''</div>
      <p class="faq-none" id="faq-none" hidden>Nessuna domanda trovata. Prova con un'altra parola, oppure apri la <a href="#mappa">Mappa del sito</a>.</p>
    </div>
  </section>

'''
if '<section id="faq">' in s:
    i=s.index('  <section id="faq">');j=s.index('  </section>\n\n',i)+len('  </section>\n\n');s=s[:i]+s[j:]
rep('  <section id="mappa">',PAGE+'  <section id="mappa">')
if 'href="#faq">FAQ</a>' not in s:
    rep('      <a href="#mappa">Mappa del sito</a>\n    </nav>','      <a href="#faq">FAQ</a>\n      <a href="#mappa">Mappa del sito</a>\n    </nav>')
    rep('"video","agenda","mappa"],SUB=','"video","agenda","faq","mappa"],SUB=')
    rep(':root[data-view="agenda"] #agenda,',':root[data-view="agenda"] #agenda,:root[data-view="faq"] #faq,')
    # mappa del sito
    m=re.search(r'var SITEMAP=(\{.*?\});\n',s);S=json.loads(m.group(1))
    S['c'].append({"t":"FAQ","k":"k-faq","d":"Le domande frequenti di chi esplora il sito, con le lingue della ricerca","h":"#faq","c":[{"t":g,"d":"Domande: "+", ".join(q for q,_ in items[:2]).replace("?","")+"…","h":"#faq"} for g,items in Q]})
    s=s[:m.start(1)]+json.dumps(S,ensure_ascii=False)+s[m.end(1):]
    # guida al sito: nuovo passo
    rep('il tasto blu «BIM News» in alto a sinistra ti riporta sempre qui."}];','il tasto blu «BIM News» in alto a sinistra ti riporta sempre qui."},\n {t:["faq"],h:"Le domande frequenti",p:"Il sito è grande e cresce ogni settimana. Nelle FAQ trovi le risposte alle domande che ci si pone esplorandolo: che cosa c\'è nelle varie pagine, come scegliamo le notizie, in che lingue cerchiamo e come si usa il sito."}];') if 'il tasto blu «BIM News»' in s else rep('Il bottone blu «BIM News» in alto a sinistra ti riporta sempre qui."}];','Il bottone «BIM News» in alto a sinistra ti riporta sempre qui."},\n {t:["faq"],h:"Le domande frequenti",p:"Il sito è grande e cresce ogni settimana. Nelle FAQ trovi le risposte alle domande che ci si pone esplorandolo: che cosa c\'è nelle varie pagine, come scegliamo le notizie, in che lingue cerchiamo e come si usa il sito."}];')
    rep('k==="topnav"?document.querySelector(".top nav"):null','k==="topnav"?document.querySelector(".top nav"):k==="faq"?document.querySelector(\'.top nav a[href="#faq"]\'):null')
    JS='''// FAQ: ricerca tra le domande e apertura dal link
(function(){var q=$("faq-q");if(!q)return;var L=[].slice.call(document.querySelectorAll(".faq-q"));
function norm(t){return t.toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g,"")}
q.addEventListener("input",function(){var v=norm(q.value.trim()),n=0;L.forEach(function(d){var ok=!v||norm(d.textContent).indexOf(v)>=0;d.hidden=!ok;if(ok)n++;if(v&&ok)d.open=true});
  document.querySelectorAll(".faq-g").forEach(function(g){g.hidden=!g.querySelector(".faq-q:not([hidden])")});$("faq-none").hidden=n>0})})();
'''
    rep('// «Grafici della veste C»',JS+'// «Grafici della veste C»')
CSS='''
/* FAQ */
:root{--k-faq:#3f5a73;--k-faq-2:#2f4659;--k-faq-s:#e7edf2;--k-faq-h:#eef2f6;--k-faq-bg:#f1f3f5;--k-faq-on:#fff}
:root[data-theme="dark"]{--k-faq:#9db4c8;--k-faq-2:#bccbd8;--k-faq-s:#1b2530;--k-faq-h:#202b37;--k-faq-bg:#0e1216;--k-faq-on:#0d1115}
:root[data-view="faq"]{--accent:var(--k-faq);--accent-2:var(--k-faq-2);--accent-soft:var(--k-faq-s);--hi:var(--k-faq-h);--bg:var(--k-faq-bg);--on-accent:var(--k-faq-on)}
.k-faq{--accent:var(--k-faq);--accent-2:var(--k-faq-2);--accent-soft:var(--k-faq-s);--hi:var(--k-faq-h);--on-accent:var(--k-faq-on)}
.top nav a[href="#faq"]{--dotc:var(--k-faq)}
#faq .content{display:grid;gap:1.2rem;max-width:62rem}
.faq-search{display:grid;gap:.3rem;max-width:30rem}
.faq-search input{font:inherit;padding:.55rem .8rem;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.faq-list{display:grid;gap:1.6rem}
.faq-g{display:grid;gap:.5rem}
.faq-g h3{font-family:var(--mono);font-size:.74rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin:0 0 .2rem}
.faq-q{border:1px solid var(--line);border-radius:10px;background:var(--surface);transition:border-color .2s}
.faq-q[open]{border-color:color-mix(in srgb,var(--accent) 55%,var(--line))}
.faq-q summary{cursor:pointer;list-style:none;padding:.85rem 2.6rem .85rem 1rem;font-family:var(--display);font-weight:600;font-size:1.05rem;position:relative}
.faq-q summary::-webkit-details-marker{display:none}
.faq-q summary::after{content:"+";position:absolute;right:1rem;top:50%;transform:translateY(-50%);font-family:var(--mono);color:var(--accent);font-size:1.1rem}
.faq-q[open] summary::after{content:"−"}
.faq-q summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:10px}
.faq-a{padding:0 1rem 1rem;color:var(--muted)}
.faq-a p{margin:0 0 .6rem;max-width:72ch}
.faq-a b{color:var(--ink);font-weight:600}
.faq-a a{color:var(--accent)}
.lg-h{font-family:var(--mono);font-size:.7rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);margin:1rem 0 .5rem}
.lg-list{list-style:none;margin:0 0 .6rem;padding:0;display:flex;flex-wrap:wrap;gap:.35rem}
.lg-list li{display:inline-flex;align-items:baseline;gap:.4rem;padding:.3rem .6rem;border:1px solid var(--line);border-radius:8px;background:var(--bg);font-size:.84rem}
.lg-list li b{color:var(--ink);font-weight:600}
.lg-list li span{color:var(--muted)}
.lg-yes li{border-color:color-mix(in srgb,var(--accent) 40%,var(--line))}
.lg-test li{border-style:dashed}
.faq-none{color:var(--muted)}
'''
M='/* FAQ */'
if M in s:
    i=s.index(M);j=s.index('</style>',i);s=s[:i]+s[j:]
i=s.index('</style>');s=s[:i]+CSS+s[i:]
open(p,'w',encoding='utf-8').write(s);print('ok',sum(len(x) for _,x in Q),'domande')
