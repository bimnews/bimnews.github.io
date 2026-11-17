# Genera la sezione «11 · La strada verso l'obbligo» di BIM in breve (#b5-obbligo)
# dai dati qui sotto: ogni riga cita le notizie (id) che la provano.
# Uso: python3 strumenti/roadmap_obbligo.py  -> riscrive il blocco tra i marcatori in index.html
import json,re,html
R='/home/user/bimnews.github.io/'
A={a['id']:a for a in json.load(open(R+'assets/notizie.json',encoding='utf-8'))['arts']}

SI=[ # paese, anno di partenza, per che cosa, notizie
('Danimarca','2013',"Opere pubbliche dello Stato: modelli a oggetti e consegna in IFC (regolamento IKT).",['n185']),
('Singapore','2013',"Pratiche edilizie in BIM per i nuovi edifici oltre 5.000 m²: prima l'architettura, dal 2015 tutto. Dal 2026 passano da CORENET X.",['n212','n131','n55']),
('Corea del Sud','2013',"Prima le grandi opere dell'agenzia appalti; ora tutte le opere pubbliche da 50 miliardi di won, 30 miliardi nel 2028, tutte nel 2030.",['n214','n26']),
('Regno Unito','2016',"Tutti i contratti del governo centrale, a qualunque importo (BIM Level 2); dal 2021 un mandato sulla gestione informativa.",['n61','n122']),
('Hong Kong','2018',"Opere pubbliche oltre 30 milioni di dollari di Hong Kong, in tutte le fasi.",['n152','n81']),
('Italia','2019',"Calendario a soglie del DM 560/2017; dal 2025 tutte le opere pubbliche oltre 2 milioni di euro (D.Lgs. 36/2023, art. 43).",['n124','n77']),
('Germania','2020',"Solo per lo Stato federale: grandi infrastrutture (Stufenplan 2015) e poi edifici federali (Masterplan 2021).",['n60','n123']),
('Brasile','2021',"Opere federali, a tappe fino al 2028.",['n120','n69']),
('Lituania','2021',"Opere pubbliche, a tappe.",['n182']),
('Svizzera','2021',"Edifici della Confederazione dal 2021, infrastrutture dal 2025.",['n175']),
('Slovenia','2022',"Nuove opere complesse con committente pubblico: progetto in BIM (legge edilizia GZ-1).",['n222']),
('Russia','2022',"Opere finanziate dallo Stato, salvo difesa e sicurezza.",['n114']),
('Giappone','2023',"Opere civili gestite dal ministero delle infrastrutture, salvo le piccole.",['n109']),
('Irlanda','2024',"Progettisti oltre 100 milioni di euro, dal 2025 oltre 20 milioni, dal 2026 anche le imprese oltre 10 milioni.",['n99','n94','n39']),
('Lettonia','2025',"Nuovi edifici del terzo gruppo (i più grandi) finanziati da enti pubblici.",['n224']),
('Dubai','2024',"Permessi di costruire dei grandi edifici e dei progetti pubblici, in IFC.",['n98']),
('Malesia','2024',"Progetti pubblici e privati da 10 milioni di ringgit; nel 2024 esteso a strade e fognature.",['n103']),
('Spagna','2026',"Plan BIM dello Stato (2023): dal 2026 livello BIM «Medio» nei lavori sopra la soglia europea.",['n111','n17']),
('Perù','2026',"Opere del governo nazionale e regionali in 14 tipologie (ospedali, università, strade…).",['n171']),
('Vietnam','2026',"Nuove opere di classe II e superiori, fin dallo studio di fattibilità.",['n206']),
]
ARR=[ # paese, quando, che cosa, notizie
('Unione europea','proposta',"Il nuovo regolamento appalti proposto dalla Commissione chiede il BIM nei lavori da 25 milioni di euro in su. Deve passare da Parlamento e Consiglio.",['n218']),
('Turchia','2029',"Regolamento del 2026: modello BIM in IFC per i permessi dei grandi edifici, a tappe dal 2029 al 2032 a partire dalle città più popolose.",['n227']),
('Repubblica Ceca','2027',"Legge sul BIM: progetti pubblici oltre 135 milioni di corone, per tutta la vita dell'opera. Era previsto prima, poi rinviato.",['n90','n133']),
('Kazakistan','2026-27',"Piano del governo: BIM obbligatorio per i nuovi edifici residenziali e commerciali.",['n38']),
('Colombia','2026',"La strategia del 2020 fissa l'obbligo dal 2026.",['n165']),
('Costa Rica','da decidere',"Un disegno di legge (24587) per l'obbligo progressivo nelle opere pubbliche.",['n166']),
('Etiopia','da decidere',"Un progetto per le opere oltre 250 milioni di birr.",['n172']),
]
NO=[ # paese, che cosa c'è, perché non è obbligatorio (solo dalle fonti), notizie
('Francia',"Piani nazionali dal 2015 (PTNB, Plan BIM 2022).","Il Codice degli appalti permette alle stazioni appaltanti di chiedere il BIM ma non le obbliga, e la generalizzazione tarda; la spinta potrebbe venire dalla revisione europea.",['n37','n150']),
('Grecia',"Strategia nazionale e roadmap (2024); la prima linea guida tecnica (2026).","Manca una soglia oltre la quale il BIM sia obbligatorio. Per la Camera tecnica il nodo è la pubblica amministrazione, che deve saper chiedere, controllare e usare i modelli; pesano anche la resistenza al cambiamento, il BIM visto come un costo e l'incertezza giuridica.",['n217','n219']),
('Romania',"Roadmap del governo (2022) e guida tecnica nazionale (2023).","Per ora la guida vale solo per i progetti pilota; per gli altri progetti pubblici è una raccomandazione. I criteri dell'obbligo sono rinviati alla fase successiva della roadmap.",['n216']),
('Svezia',"I grandi committenti pubblici chiedono il BIM nei loro contratti (Trafikverket dal 2015).","Non c'è un obbligo di legge nazionale: decide ogni committente.",['n213']),
('Paesi Bassi',"Obbligo «applica o spiega» per gli standard aperti: IFC (2011), NLCS e COINS (2018).","L'obbligo riguarda i formati con cui si scambiano i dati, non l'uso del BIM in sé.",['n211','n181']),
('Ucraina',"Strategia del governo (2021) con progetti pilota.","La fonte non lo spiega.",['n215']),
('Portogallo',"Strategia nazionale approvata nel 2026.","La strategia è appena partita; la fonte non fissa un obbligo.",['n46']),
('Polonia',"Mappa per introdurre il BIM negli appalti (2020).","La fonte non lo spiega.",['n160']),
('Stati Uniti',"Programma federale GSA (2003), standard nazionale NBIMS (dal 2007), National BIM Program (2022).","Non c'è un obbligo federale generale: chiedono il BIM singole agenzie e committenti.",['n188','n210','n116']),
('Messico e Argentina',"Strategie nazionali per le opere pubbliche (2019).","Le fonti non lo spiegano.",['n162','n157']),
('Estonia e Islanda',"Requisiti BIM delle agenzie immobiliari dello Stato (RKAS dal 2018, FSRE dal 2023).","Sono regole del committente pubblico, non una legge nazionale.",['n183','n223']),
('Finlandia',"Requisiti BIM dell'agenzia immobiliare dello Stato (Senaatti, dal 2007); dal 2026 il permesso di costruire si può chiedere con il modello.","Il modello per il permesso è una possibilità, non un obbligo; i requisiti di Senaatti valgono per i suoi progetti.",['n186','n225']),
('Slovacchia',"Roadmap nazionale BIM approvata dal governo nel 2026.","È una scelta: l'obbligo è per gli uffici tecnici, che dovranno ricevere e usare i modelli; per i progettisti presentarli sarà una possibilità. La legge è prevista per il 2031-2032.",['n226']),
('Croazia',"Piattaforma nazionale hrBIM; il BIM è nelle nuove leggi su urbanistica e costruzioni (2026).","La fonte parla di una possibilità: dal 2027 si potrà presentare il progetto in IFC per il permesso di localizzazione.",['n228']),
('Nuova Zelanda',"La guida del governo agli appalti (2019) chiede alle agenzie pubbliche di adottare il BIM.","La guida non fissa soglie né scadenze, e la fonte non parla di un obbligo di legge.",['n221']),
('Taiwan',"Piano della Commissione per le opere pubbliche dal 2014, con progetti pilota e una soglia prevista dal 2017.","La Corte dei conti ha trovato risultati sotto le attese, regole BIM diverse da un ente all'altro nei contratti e criteri di costo non uniformi; la fonte non dice se la soglia sia stata fissata.",['n220']),
]

def links(ids):
    out=[]
    for i in sorted(ids,key=lambda i:A[i]['d']):
        a=A[i]
        out.append('<a href="#settimana-%s" data-art="%s">%s</a>'%(a['w'],i,a['d'][:4]))
    return '<div class="ob-srcw"><span class="ob-lab">Notizie:</span> <span class="ob-src">'+' · '.join(out)+'</span></div>'

def e(s):return html.escape(s,quote=False)
h=['<!-- obbligo:inizio -->','<div class="ob-wrap" id="b5-obbligo">',
'  <span class="label">11 · La strada verso l\'obbligo</span>',
'  <p class="tl-intro">Dove il BIM è già obbligatorio, dove sta arrivando e dove non lo è ancora, con il perché quando le fonti lo dicono. Ogni riga rimanda alle notizie di BIM News che la provano.</p>',
'  <div class="ob-line" aria-label="Anno di partenza dell\'obbligo">']
yrs={}
for p,y,_,_ in SI: yrs.setdefault(y,[]).append(p)
for y in sorted(yrs):
    h.append('    <div class="ob-yr"><b>%s</b><span>%s</span></div>'%(y,e(', '.join(yrs[y]))))
h.append('  </div>')
h.append('  <div class="ob-grid">')
h.append('    <section class="ob-col ob-si"><h4><span class="ob-k">●</span> Obbligatorio <small>%d</small></h4>'%len(SI))
for p,y,t,ids in SI:
    h.append('      <div class="ob-row"><div class="ob-h"><b>%s</b><span class="ob-y">dal %s</span></div><p>%s</p>%s</div>'%(e(p),y,e(t),links(ids)))
h.append('    </section>')
h.append('    <section class="ob-col ob-arr"><h4><span class="ob-k">◐</span> In arrivo <small>%d</small></h4>'%len(ARR))
for p,y,t,ids in ARR:
    h.append('      <div class="ob-row"><div class="ob-h"><b>%s</b><span class="ob-y">%s</span></div><p>%s</p>%s</div>'%(e(p),e(y),e(t),links(ids)))
h.append('    </section>')
h.append('    <section class="ob-col ob-no"><h4><span class="ob-k">○</span> Non ancora <small>%d</small></h4>'%len(NO))
for p,c,w,ids in NO:
    h.append('      <div class="ob-row"><div class="ob-h"><b>%s</b></div><p>%s</p><p class="ob-why"><b>Perché non ancora?</b> %s</p>%s</div>'%(e(p),e(c),e(w),links(ids)))
h.append('    </section>')
h.append('  </div>')
h.append('  <p class="ob-note">Aggiornato al 16/11/2026. «Obbligatorio» vuol dire che una legge, un decreto o una regola del governo lo impone almeno in una parte delle opere pubbliche; i dettagli sono nelle notizie. Una proposta o una strategia senza data vincolante resta tra «in arrivo» o «non ancora».</p>')
h.append('</div>')
h.append('<!-- obbligo:fine -->')
BLOCK='\n'.join('      '+l if l else l for l in h)

CSS='''/* obbligo: roadmap dell'obbligatorietà (#b5-obbligo) */
.ob-wrap{display:grid;gap:.9rem;margin-top:2rem}
.ob-line{display:flex;gap:.4rem;overflow-x:auto;padding:.2rem 0 .5rem;scrollbar-width:thin}
.ob-yr{flex:0 0 auto;min-width:7.2rem;max-width:11rem;border-top:3px solid var(--k-b5);padding:.35rem .5rem 0;display:grid;gap:.15rem}
.ob-yr b{font-family:var(--mono);font-size:.85rem;color:var(--k-b5)}
.ob-yr span{font-size:.8rem;color:var(--muted);line-height:1.3}
.ob-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.8rem;align-items:start}
@media (max-width:1000px){.ob-grid{grid-template-columns:1fr}}
.ob-col{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);box-shadow:var(--shadow);padding:.9rem;display:grid;gap:.55rem}
.ob-col h4{margin:0;font-family:var(--display);font-size:1.05rem;display:flex;align-items:center;gap:.4rem}
.ob-col h4 small{font-family:var(--mono);font-size:.75rem;color:var(--muted);margin-left:auto}
.ob-si .ob-k{color:var(--k-b5)}.ob-arr .ob-k{color:var(--k-ag)}.ob-no .ob-k{color:var(--muted)}
.ob-row{border-top:1px solid var(--line);padding-top:.5rem;display:grid;gap:.25rem}
.ob-h{display:flex;justify-content:space-between;gap:.5rem;align-items:baseline}
.ob-y{font-family:var(--mono);font-size:.75rem;color:var(--muted);white-space:nowrap}
.ob-row p{margin:0;font-size:.9rem;line-height:1.45}
.ob-why{color:var(--muted)}.ob-why b{color:var(--ink)}
.ob-srcw{font-size:.78rem;color:var(--muted)}
.ob-note{font-size:.85rem;color:var(--muted);margin:0}
/* obbligo:fine-css */'''

s=open(R+'index.html',encoding='utf-8').read()
if '<!-- obbligo:inizio -->' in s:
    s=re.sub(r'      <!-- obbligo:inizio -->.*?<!-- obbligo:fine -->',lambda m:BLOCK,s,flags=re.S)
else:
    anchor='\n      <a class="btn-next" href="#bim-news">Ora sei pronto per le novità'
    assert s.count(anchor)==1
    s=s.replace(anchor,'\n'+BLOCK+'\n'+anchor,1)
if '/* obbligo: roadmap' in s:
    s=re.sub(r'/\* obbligo: roadmap.*?/\* obbligo:fine-css \*/',lambda m:CSS,s,flags=re.S)
else:
    a='.fu-k.ok{color:var(--k-b5)}.fu-k.q{color:var(--muted)}'
    assert s.count(a)==1
    s=s.replace(a,a+'\n'+CSS,1)
t='<button type="button" data-go="b5-futuro">10 Il futuro</button>'
if 'data-go="b5-obbligo"' not in s:
    assert s.count(t)==1
    s=s.replace(t,t+'<button type="button" data-go="b5-obbligo">11 L\'obbligo nel mondo</button>',1)
m='{"t":"Cosa ci riserva il futuro?","d":"Che cosa sta già cambiando e quali domande restano aperte","h":"#bim-5-minuti","e":"b5-futuro"}'
if '"e":"b5-obbligo"' not in s:
    assert s.count(m)==1
    s=s.replace(m,m+',{"t":"La strada verso l\'obbligo","d":"Dove il BIM è obbligatorio, dove sta arrivando e perché altrove non lo è ancora","h":"#bim-5-minuti","e":"b5-obbligo"}',1)
open(R+'index.html','w',encoding='utf-8').write(s)
print('ok',len(SI),len(ARR),len(NO))
