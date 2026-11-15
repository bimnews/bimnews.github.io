# BIM News: istruzioni per Claude

Sito di Marco Scigliuolo (ingegnere civile, provincia di Bolzano), pubblicato con GitHub Pages dal branch `main` su https://mscigliuolo.github.io/. Rassegna mondiale sul BIM, in italiano, con la fonte di ogni notizia.

**Alla fine di ogni richiesta** aggiorna questo file (stato dei lavori, decisioni, dove sta il codice) e pubblicalo su main, così una nuova sessione riparte da qui senza ricominciare da zero.

**Con Marco:** scrivi in italiano e dagli del tu. Parti dalla risposta, senza premesse né complimenti. Non inventare mai fatti: ogni notizia, data, numero o link va verificato aprendo la pagina. Prima di cambiamenti grandi alla grafica mostragli un'anteprima (screenshot o GIF) e pubblica solo dopo il suo sì.

## Com'è fatto il sito

- **`index.html`**: pagina unica (circa 390 KB) con CSS, HTML e JS.
  - Navigazione a hash, con `view()` e l'array `VIEWS`. Viste: home, bim-news, bim-ai, bim-accademia, bim-5-minuti, video, chi-sono (sottopagine profilo, portfolio, studio, proposte, wip, fuori, libri), agenda, faq, mappa.
  - Restano dentro la pagina: `AGENDA`, `SCADENZE`, `VIDEOS`, `VIDEOS_UNI`, `CHANNELS`, `NORME`, `SITEMAP`.
  - Il codice principale è in `function __boot()`, che parte quando è arrivato `assets/notizie.json`.
- **`assets/notizie.json`**: `{"weeks":{…},"arts":[…]}`, una notizia per riga. Modificalo solo con script, per esempio `strumenti/add_news.py`.
- **`assets/accademia.json`**: gli articoli di BIM Accademia (abstract CC BY tradotti). Si carica solo sulla pagina `#bim-accademia`.
- **`assets/mappa.svg`**: confini dei paesi (`data-n` è il nome italiano, `data-c` il continente) e regioni (`data-r` dentro `<g class="rgc" data-p="Paese">`). Proiezione Equal Earth, scala 130, traslazione (360,175), viewBox 720×350.
- **Altri file:**
  - `assets/foto/` (foto CC0 per scheda, solo versione completa);
  - `assets/copertine/` (copertine dei manuali);
  - `assets/gif/appload.gif`;
  - `fonts/` (Inter, Inter Tight, JetBrains Mono, Atkinson per i manuali);
  - `manuali/` (manuali HTML e PDF);
  - `privacy.html`.
- **Tasto Home:** `a.brand` e `#home-link` ricaricano tutta la pagina (`location.reload()` su `#home`), così si vedono sempre gli ultimi aggiornamenti; `notizie.json` e `accademia.json` si scaricano con `cache:"no-cache"`. Richiesta di Marco del 15/11/2026: non toglierlo.
- **Revisione:** `<meta name="revisione" content="N · GG/MM/AAAA">`. Il cartiglio a piè di pagina è stato tolto di proposito.
- **Due versioni:**
  - **completa:** foto, mappa, nuvola di punti, copertine e GIF;
  - **essenziale:** classe `lite` su `<html>`; non scarica foto, mappa, font, copertine né GIF.
- **Veste grafica C, «Cantiere di notte»:**
  - tema scuro predefinito, con chiave `tema-2026` in localStorage;
  - un colore per ogni scheda (`--k-news`, `--k-ai`, `--k-acc`, `--k-b5`, `--k-vid`, `--k-cur`, `--k-ag`, `--k-pf`, `--k-faq`).
- **Home versione B:** titolo, mappa a tutta larghezza con la ricerca «Dove andiamo oggi?» (`#fc-search`) e la striscia degli eventi `#fc-strip`. La striscia deve restare intera nello schermo da 1280×650 in su: controlla con `strumenti/fit.js`.
- **Il curatore, regola di Marco:** ogni articolo della pagina «Il curatore» è una finestra che si apre e si chiude (triangolo ▶ a destra, script «I miei libri: categorie e schede a scomparsa», esteso a `#chi-sono .st-item`). Si vedono il titolo e la prima riga; le schede con solo «Work in progress» restano aperte perché non c'è altro. I link con la classe `hl` aprono da soli l'articolo. Ogni nuovo articolo segue questa struttura: `h4`, prima riga `p`, poi il resto.
- **Inoltre:** la guida al sito (array `STEPS`), la FAQ (`#faq`, generabile con `strumenti/faq.py`) e i crediti delle foto in fondo alla Mappa del sito.

## Come si pubblica

1. Lavora sul ramo indicato dalla sessione, partendo da `origin/main` aggiornato. Prima fai sempre `git fetch origin main`: una volta si è rischiato di pubblicare su una copia vecchia.
2. Controlla con Playwright tramite un server locale (`python3 -m http.server 8765` nella cartella del sito). Gli script di controllo sono in `strumenti/`: i loro percorsi puntano a una vecchia cartella temporanea e vanno adattati.
3. Aumenta la revisione nel meta.
4. Fai commit, apri la pull request e uniscila su main (squash).
5. Il task settimanale invece scrive direttamente su main.

## Attività programmate (account di Marco)

- **Task settimanale** `trig_015jCaF6QnEXfgYXfYEkz2L5`, ogni lunedì alle 7:41 (ora di Roma):
  - notizie, agenda, scadenze, video e circa 20 articoli di BIM Accademia;
  - fonti in tre livelli (istituzionali, stampa autorevole, grandi aziende);
  - lingue della ricerca: 36 lingue più 40 in verifica, elencate nella FAQ, che è la fonte unica: la tendina di BIM News le copia da lì.
- **Backup mensile** `trig_01JYeJLDBXhzrernU5qSRte7`, il 1° del mese alle 19:23: invia a Marco uno zip con il sito, la cronologia (git bundle) e il testo del task settimanale.
- **Se cambi la struttura dei dati, aggiorna il testo dei task con `update_trigger`.**

## Regole fisse

- **Principi etici NON negoziabili (Marco, 15/11/2026):** tutto deve essere gratis per chi visita il sito; nessun cookie di tracciamento (GoatCounter va bene perché non usa cookie). Gli eventi a pagamento si segnalano come tali, senza assumersene la responsabilità. Sono scritti nel riquadro `.bn-rules` di BIM News.
- **Notizie:**
  - solo dal 2015 in poi;
  - la mappa resta neutra;
  - nessun logo o immagine protetta: foto solo CC0 (Wikimedia Commons), icone disegnate da noi.
- **Accesso e dati:**
  - niente email di Marco nelle richieste a servizi esterni;
  - niente servizi che chiedono di registrare un'email: per esempio OpenAlex no, Crossref sì.
- **Fonti:**
  - città, regioni e province valgono come fonti solo se danno un contributo concreto al BIM;
  - mai lanci di prodotti, blog, social o cronaca locale.
- **Bozze:** la bozza «La prima routine» per AutoCAD è in attesa di revisione da parte di Marco e non va pubblicata. Una copia è nel backup zip.
- **File che Marco deve ancora mandare:** gli originali di `SOSTXRIF.lsp` e `RETINITRASP.lsp` (quelli nel sito sono riscritti e «da provare») e i file `.dyn` di Dynamo.

## Lavori in sospeso, in ordine di priorità

1. **Globo 3D: PUBBLICATO il 15/11/2026 (revisione 106) dopo il sì di Marco.**
   - **Codice:** `assets/globo/` (`globo.js`, `mondo.json`, `citta.json`, le librerie, `LICENZE.txt`); `loadGlobe()` parte dopo `loadMap()`, solo nella versione completa.
   - **Cosa fa:** orientamento iniziale dal fuso orario; asse inclinato di 23,44°; giorno e notte reali; luci delle città; clic su un paese → volo sul paese, poi passaggio alla mappa piatta; «← Mondo» → torna il globo.
   - **Movimento:** il globo ruota soltanto, senza oscillare in su e in giù: Marco l'ha trovato brutto (15/11/2026). Rotazione continua.
2. **Animazioni stagionali (solo anteprime per ora):** effetti leggeri e trasparenti sulla fascia della ricerca, attivati da soli nel periodo giusto.
   - **Natale:** neve e simboli natalizi dall'8 dicembre al 6 gennaio (Marco ha scritto «6 dicembre», ma intende la Befana).
   - **Altre grandi religioni**, ciascuna con un tema suo:
     - Ramadan ed Eid: mezzaluna e lanterne;
     - Hanukkah: luci della menorah;
     - Diwali: lampade diya;
     - Vesak: lanterne e loto;
     - Capodanno lunare: lanterne rosse;
     - Pasqua.
   - **Calcolo delle date:** usare `Intl.DateTimeFormat` con i calendari `islamic-umalqura`, `hebrew` e `chinese`, così le date si calcolano da sole. Diwali e Vesak vanno in una tabella verificata anno per anno.
   - **Anteprime:** GIF da mostrare a Marco prima di pubblicare.
3. **Pulsanti 3D «a LED incassati»: PUBBLICATI il 15/11/2026 (revisione 111) dopo il sì di Marco.**
   - **Dove si applicano:** barra in alto, schede di BIM News, impostazioni, «Vedi le notizie», «Tutti gli appuntamenti».
   - **Il codice:** il CSS è in fondo allo `<style>`, blocco «pulsanti 3D a LED incassati».
   - **Come funziona:** il LED, del colore della sezione (`--led`), è spento a riposo; si accende con la scritta al passaggio del cursore; al clic il pulsante scende; nella pagina attuale resta acceso.
   - **Ingombro:** tra 901 e 1420 px i pulsanti sono più stretti, così la barra resta su una riga e la striscia `#fc-strip` entra a 1280×650 (verificato con `fit.js`).
4. **Sito multilingue, proposta 2, scelta da Marco.**
   - Interfaccia in 7 lingue: it, en, de, fr, es, zh (semplificato), ja.
   - Pagine separate per lingua (`/en/`, `/de/`…) con `hreflang`.
   - Titoli delle notizie nelle 7 lingue, sintesi anche in inglese.
   - BIM Accademia: abstract tradotto in italiano solo nella versione italiana; altrove abstract inglese con `lang="en"`, così il browser propone la traduzione nella lingua del lettore.
   - Segnare con `translate="no"` i nomi propri e le sigle.
   - Il widget di Google Traduttore non è più disponibile: non usarlo.
5. **Ricerca a tappeto per paesi.**
   - **Fatto:**
     - America Latina: Messico, Costa Rica (3), Uruguay, Colombia (3), Perù (2);
     - Africa: Etiopia e Sudafrica.
   - **Cercati senza fonti istituzionali valide:** Ruanda, Nigeria, Ghana, Kenya (solo un discorso), Marocco, Algeria e Tunisia (nessun obbligo BIM), Egitto (il codice BIM esiste ma la fonte non era raggiungibile).
   - **Restano:** Africa francofona ed Egitto in arabo; poi l'Europa scoperta (prima la Svizzera, poi Paesi Bassi, nordici, Belgio, Grecia, Romania…); poi Asia e Medio Oriente (con Singapore, India, Arabia Saudita, Turchia, Vietnam, Taiwan) e Oceania (Nuova Zelanda); infine l'approfondimento dei paesi già presenti.
   - **Strumenti:** `strumenti/ver.py` (scarica una pagina e mostra le frasi con le parole chiave) e `strumenti/add_news.py` (aggiunge le notizie calcolando id e settimana).
6. **Tai Chi e Kung Fu: PUBBLICATO il 15/11/2026 (revisione 107), `#fuori-taichi` in Fuori dallo studio.**
   - **Immagine:** le cinque virtù (智 仁 信 勇 忍) ricostruite in HTML e CSS (`.kf-fig`), con caratteri veri in font kaishu di sistema, non come immagine.
   - **Testi:** riassunti con parole nostre dalla pagina https://www.kungfuetaichi.com/5-virt%C3%B9, con due brevi citazioni.
   - **«Perché per me è importante»:** scritto il 15/11/2026 dal racconto di Marco (valvola di sfogo, equilibrio, bene e male, «scegliere le proprie battaglie» anche nel lavoro).
7. **Statistiche delle visite: sezione PUBBLICATA il 15/11/2026 (revisione 110), «Le visite del sito» (`#visite`) nella pagina Mappa del sito.**
   - **Cosa mostra:** il totale, gli ultimi 30 giorni e le 10 pagine più visitate. Legge `https://mscigliuolo.goatcounter.com/counter/<path>.json`, dove i path sono `/`, `/bim-news` e così via, come in `count()`; `TOTAL` dà il totale del sito.
   - **Quando si carica:** solo quando si apre la vista `mappa`. Nel piè di pagina, «Statistiche anonime» porta lì.
   - **Contatore pubblico:** Marco l'ha acceso il 15/11/2026 («Allow adding visitor counts» in GoatCounter); i numeri arrivano. `TOTAL` comprende anche gli eventi, come i clic sulle fonti, quindi è più alto della somma delle pagine.
8. **Timeline doppia «Il BIM nel tempo: il mondo e l'Italia»: PUBBLICATA il 15/11/2026 (revisione 109) dopo il sì di Marco.**
   - **Dove:** in BIM in 5 minuti, `#b5-t2`, dopo la lisca; c'è anche la voce «05 Mondo e Italia» nell'indice e nella mappa del sito.
   - **Codice:** HTML, CSS (`.t2-*`) e JS (IIFE dopo il filtro `.tl-filter`) dentro `index.html`.
   - **Linea italiana:** `UNI 11337:2009` + l'array `NORME`. Una nuova norma aggiunta a `NORME` compare da sola.
   - **Linea del mondo:** sta nell'array `W` dentro la IIFE, con le fonti verificate.
   - **Collegamenti Italia → mondo:** sono nell'oggetto `LINK`, con chiave il campo `n` della norma italiana.
9. **Selettore delle lingue: PUBBLICATO il 15/11/2026 (revisione 113), in alto a sinistra nella barra `.util`, prima di «La tua area».**
   - **Lingue:** 11 (it, en, fr, de, es, pt, ru, ar, zh in caratteri semplificati, ja, ko). La scelta resta nel browser (`localStorage` «lingua»).
   - **Come traduce:** sul posto, senza ricaricare la pagina.
     - Scritte brevi: il dizionario `D` (chiave = testo italiano esatto) sui nodi di testo di `.util`, `.top`, `.facade`, `.bn-hero`, `.bn-what` e `footer`. Un MutationObserver ritraduce le scritte che cambiano da sole (tema, versione, striscia degli eventi).
     - Blocchi con markup: `data-tr="chiave"` e il dizionario `B` (il disclaimer di BIM News).
     - Arabo: `dir="rtl"` sui testi tradotti, ma l'impaginazione resta da sinistra a destra.
   - **I file:** il dizionario sta in `strumenti/lingue/dizionario.py`; per aggiornarlo dentro `index.html` si sostituisce l'oggetto `D`/`B` (vedi `applica.py`, che serve per il primo inserimento).
   - **Non tradotti per ora:** notizie, sintesi, articoli, FAQ, l'etichetta «Mondo» della mappa (il codice confronta il testo «Mondo») e «Ultimo aggiornamento».
   - **Prossimi passi possibili:** pagine separate per lingua (`/en/`…) con `hreflang` per i motori di ricerca, la FAQ tradotta, i titoli delle notizie.
   - **Revisione delle traduzioni:** le ha scritte Claude; serve la revisione di un madrelingua, soprattutto per arabo, cinese, giapponese e coreano.
10. **Articoli da scrivere con Marco (impostati il 15/11/2026; testi da fare insieme):**
   - **In `#wip` → «Articoli in preparazione»** (`.wip-art`), ogni scheda con «Cosa conterrà»:
     - `art-hoover`: lo script «Hoover», che legge un Excel con materiali, parametri e informazioni di sistema;
     - `art-ifc-zero`: come costruire un IFC da zero (esperimento riuscito, mancano le considerazioni finali; si lega a «Il mondo oltre noi»);
     - `art-10-tips`: i 10 consigli, di cui 6 scritti (salvataggi automatici, gestione del tempo, template, gruppo di continuità, straordinari, riflessione) e 4 da definire;
     - `art-ifc-excel`: la biblioteca IFC in Excel;
     - `art-ifc-versioni`: le versioni di esportazione IFC a confronto;
     - `art-ifc-dialogo`: far dialogare i software con l'IFC e il modello federato;
     - `art-img-lingua`: manuali con immagini SVG, con le scritte che seguono la lingua.
   - **In `#studio` → Riflessioni:** `studio-oltre-noi`, «Il mondo oltre noi» (che ne sarà dei nostri modelli tra 200 anni; da fare una ricerca sul più antico disegno di progetto arrivato fino a noi).
   - **Collegamenti tra sottopagine:** usare `data-goto-art="id"`.
   - **Da verificare:** il proverbio «Ciò che cresce lentamente mette radici profonde» è indicato come «attribuito alla tradizione africana»; l'origine non è verificata.

11. **BIM in 5 minuti, «01 · Che cos'è» riscritto: PUBBLICATO il 15/11/2026 (revisione 112).** Tre passi: a mano (Palladio, 1570, MET CC0, `assets/foto/palladio-rotonda.jpg`, con credito nella Mappa del sito), il CAD (linee con attributi) e il BIM (oggetti con parametri, muro interattivo `#bim-demo`); poi «Perché cambia tutto» e «Attributo o parametro?».

## Fatto di recente

- **15/11/2026, revisione 100:**
  - **BIM in 5 minuti:** sezione «09 · Le certificazioni nel mondo» (`#b5-cert`) con 6 schede verificate: Hong Kong (obbligatoria, DEVB TC(W) 2/2021), Italia (volontaria, All. I.9 art. 1 c. 3 D.Lgs. 36/2023, UNI 11337-7, UNI/PdR 78:2020), Spagna (Plan BIM 2023), Regno Unito (BRE e UKAS, ISO 19650-2), Germania (VDI/bS 2552 Blatt 8.1), buildingSMART. Altri paesi da aggiungere con la ricerca a tappeto: Cina, Corea, Singapore, Francia, paesi nordici…
  - **Scautismo** (`#fuori-scout`): testo di Marco (dall'AGESCI al CNGEI, scout laici, a Bolzano) e citazione di Baden-Powell da *Aids to Scoutmastership*, ed. 1930, «The Aim of Scouting», tradotta da noi. Marco aveva scritto «CNGI»: il nome corretto è CNGEI. Niente articoli: solo questa descrizione.
- **15/11/2026, revisione 101:**
  - **FAQ:** la policy di Marco. Niente collaborazioni economiche né esterne sul sito (gestito con il suo piano Pro di Claude); sì a sponsorizzazioni per passare a un piano con più token, «parliamone». Aggiornato anche `strumenti/faq.py`.
  - **BIM News:** il riquadro «Tutte le notizie» è su una colonna da bordo a bordo; criterio, scelta delle notizie, fonti e lingue sono in un `<details class="ai-more">` richiudibile.
  - **BIM News:** il disclaimer «Che cos'è BIM News, e che cosa non è» (`.bn-what`), sempre aperto, da non chiudere mai: è una richiesta esplicita di Marco.
- **15/11/2026, revisione 102:** principi non negoziabili nel disclaimer di BIM News (gratis, nessun cookie di tracciamento, eventi a pagamento senza responsabilità).
  - **Missioni nel disclaimer:** quella del sito è far conoscere la cultura del BIM al mondo intero; quella personale di Marco è diffonderla in Italia, perché il BIM non sia solo un «certificato» per le gare ma uno strumento legato al metodo di progettazione.
- **15/11/2026, revisione 104:** nella FAQ sulle collaborazioni Marco aggiunge che il sito è una passione, un piccolo hobby, e va avanti finché è sostenibile in soldi e tempo.
- **15/11/2026, revisione 105:** il tasto Home ricarica tutto il sito.
- **15/11/2026, revisione 106:** pubblicato il globo 3D della home.
- **15/11/2026, revisione 107:** scheda Tai Chi e Kung Fu con le cinque virtù.
- **15/11/2026, revisione 108:** il globo non oscilla più, ruota soltanto.
- **15/11/2026, revisione 109:** pubblicata la timeline doppia mondo e Italia.
- **15/11/2026, revisione 110:** la sezione «Le visite del sito» nella Mappa del sito.
- **15/11/2026, revisione 111:** pulsanti 3D a LED incassati.
- **15/11/2026, revisione 112:**
  - **Il curatore:** tutti gli articoli si aprono e si chiudono.
  - **Tai Chi e Kung Fu:** il racconto di Marco.
  - **BIM in 5 minuti:** «Che cos'è» riscritto.
  - **Le mie proposte:** la frase «aperte ai commenti» è sostituita dal rimando a LinkedIn, per coerenza con il disclaimer.
- **15/11/2026, revisione 113:** selettore delle lingue (11 lingue) con le scritte principali tradotte.
