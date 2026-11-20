# BIM News: istruzioni per Claude

Sito di Marco Scigliuolo (ingegnere civile, provincia di Bolzano), pubblicato con GitHub Pages dal branch `main` su **https://bimnews.github.io/**. Il repository è `bimnews/bimnews.github.io`, nell'organizzazione GitHub «bimnews» di Marco (trasferito il 15/11/2026 da `mscigliuolo/mscigliuolo.github.io`, per avere un indirizzo senza nome personale e senza comprare un dominio). Il vecchio indirizzo `mscigliuolo.github.io` non risponde più. Rassegna mondiale sul BIM, in italiano, con la fonte di ogni notizia.

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
- **Revisione:** `<meta name="revisione" content="N · GG/MM/AAAA">`. Dalla revisione 147 la data della revisione compare nel piè di pagina come «Sito aggiornato il …» (script «date del sito nel piè di pagina», `#fd-upd`), accanto a «Online dal 9 novembre 2026» (`#fd-born`, primo commit del repository): aumentare sempre la revisione con la data giusta. Le date seguono la lingua (`Intl`), le due etichette sono in `tr/<lingua>/extra.txt`. Il cartiglio a piè di pagina è stato tolto di proposito.
- **Due versioni:**
  - **completa:** foto, mappa, nuvola di punti, copertine e GIF;
  - **essenziale:** classe `lite` su `<html>`; non scarica foto, mappa, font, copertine né GIF.
- **Veste grafica C, «Cantiere di notte»:**
  - tema scuro predefinito, con chiave `tema-2026` in localStorage;
  - un colore per ogni scheda (`--k-news`, `--k-ai`, `--k-acc`, `--k-b5`, `--k-vid`, `--k-cur`, `--k-ag`, `--k-pf`, `--k-faq`).
- **Home versione B:** titolo, mappa a tutta larghezza con la ricerca «Dove andiamo oggi?» (`#fc-search`) e la striscia degli eventi `#fc-strip`. La striscia deve restare intera nello schermo da 1280×650 in su: controlla con `strumenti/fit.js`.
- **Il curatore, regola di Marco:** ogni articolo della pagina «Il curatore» è una finestra che si apre e si chiude (triangolo ▶ a destra, script «I miei libri: categorie e schede a scomparsa», esteso a `#chi-sono .st-item`). Si vedono il titolo e la prima riga; le schede con solo «Work in progress» restano aperte perché non c'è altro. I link con la classe `hl` aprono da soli l'articolo. Ogni nuovo articolo segue questa struttura: `h4`, prima riga `p`, poi il resto.
- **Inoltre:** la guida al sito (array `STEPS`), la FAQ (`#faq`, generabile con `strumenti/faq.py`) e i crediti delle foto in fondo alla Mappa del sito.

## Figure animate (repository `bimnews/figure`)

- **Dal 20/11/2026** le figure animate e interattive si fanno in una repository a parte, privata: `bimnews/figure`. Contiene la skill «anatomy» (MIT, copiata a versione fissa in `.claude/skills/anatomy/`), i sorgenti in `figure/<nome>/` e i file finiti in `dist/`. Le regole (peso, tema, niente risorse esterne, anteprima a Marco) sono nel suo `CLAUDE.md`.
- **Per lavorarci** collega la repository alla sessione (`add_repo` bimnews/figure). Nel sito si copia solo il file di `dist/`, di solito dentro un manuale con un `iframe` `?embed=1`, mai nella versione essenziale.
- **Figura 1, il coordinatografo della georeferenziazione: PUBBLICATA il 20/11/2026 (revisione 146) dopo il sì di Marco.** File: `manuali/figure/georeferenziazione.html` (copia di `dist/` della repository delle figure: non modificarla qui, si rigenera là). Incorporata nel capitolo 3 di `manuali/georeferenziazione-ifc.html` dentro `#fig-coord`: lo script in fondo all'articolo crea l'iframe `?embed=1` solo fuori dalla versione essenziale (stessa regola di `index.html`: `localStorage` «versione», riduzione del movimento, risparmio dati); nella versione essenziale c'è il link alla pagina. L'altezza arriva con `postMessage({figH})`, il tema segue quello dell'articolo.
- **Revisione 150 (20/11/2026):** figura 1 aggiornata: sul telefono si ruota il foglio trascinando col dito, un tocco cambia l'unità.
- **Figure 2, 3 e 4 in ANTEPRIMA, in attesa del sì di Marco (20/11/2026)** (dettagli nel `CLAUDE.md` di `bimnews/figure`): pressa dell'estrusione e del foro → `manuali/ifc-da-zero.html` («Il foro e il serramento»); catena delle posizioni → `ifc-da-zero.html` («Le posizioni a catena»); schedario classe/PredefinedType → `manuali/libreria-ifc.html`. Dopo il sì: copiarle in `manuali/figure/` e incorporarle come la figura 1 (iframe `?embed=1` creato via script fuori dalla versione essenziale, gestore `postMessage` con `figH` e il nome della figura).

## Come si pubblica

1. Lavora sul ramo indicato dalla sessione, partendo da `origin/main` aggiornato. Prima fai sempre `git fetch origin main`: una volta si è rischiato di pubblicare su una copia vecchia.
2. Controlla con Playwright tramite un server locale (`python3 -m http.server 8765` nella cartella del sito). Gli script di controllo sono in `strumenti/`: i loro percorsi puntano a una vecchia cartella temporanea e vanno adattati.
3. Aumenta la revisione nel meta.
4. Fai commit, apri la pull request e uniscila su main (squash).
5. Il task settimanale invece scrive direttamente su main.

## Attività programmate (account di Marco)

- **Task settimanale** `trig_015jCaF6QnEXfgYXfYEkz2L5`, nella notte tra domenica e lunedì alle 0:13 (ora di Roma; spostato da Marco il 16/11/2026 per non consumare i token del lunedì mattina). **Le istruzioni sono nel repository: `strumenti/task-settimanale.md`** (fonte unica: per cambiare il lavoro del task si modifica quel file; il testo del task dice solo di collegare il repository ed eseguirlo):
  - SOLO le notizie della settimana passata (decisione di Marco del 15/11/2026: niente ricerca storica il lunedì), più agenda, scadenze, video e circa 20 articoli di BIM Accademia;
  - fonti in tre livelli (istituzionali, stampa autorevole, grandi aziende);
  - lingue della ricerca: 36 lingue più 40 in verifica, elencate nella FAQ, che è la fonte unica: la tendina di BIM News le copia da lì.
- **I due task puntano a `bimnews/bimnews.github.io`** (testi aggiornati il 16/11/2026).
- **16/11/2026:** il primo giro del task non ha potuto pubblicare (push 403). Causa: l'ambiente del task («BIM News: rassegna settimanale dal mondo», `env_01PKTScVCapzPJdy5JcKsLsj`) aveva ancora il vecchio repository `mscigliuolo/mscigliuolo.github.io`. Marco l'ha sostituito con `bimnews/bimnews.github.io` lo stesso giorno (verificato con get_environment). Prima verifica vera: il giro del 23/11 alle 0:13. Se il push fallisse ancora, il task manda la patch a Marco. NON lanciare il task a mano per provarlo: ignora l'istruzione «solo prova» e rifà tutta la rassegna.
- **Backup mensile** `trig_01JYeJLDBXhzrernU5qSRte7`, il 1° del mese alle 19:23: invia a Marco uno zip con il sito, la cronologia (git bundle) e il testo del task settimanale.
- **Se cambi la struttura dei dati, aggiorna il testo dei task con `update_trigger`.**

## Google (Search Console)

- **16/11/2026:** aggiunti `robots.txt` e `sitemap.xml` (home, manuali HTML, privacy). Le viste con `#` non sono pagine per Google: si indicizza solo la home.
- **16/11/2026, revisione 130–131:** inserito il tag di verifica di Marco (`google-site-verification`, nella testa di `index.html`, accanto alla revisione): NON toglierlo. In revisione 131 il codice è stato sostituito con quello giusto del metodo «Tag HTML» (`bjOU_7z5…`): il primo (`Dn1I…`) era il record DNS, che su github.io non si può usare. Il 16/11/2026 Marco ha verificato la proprietà e inviato `sitemap.xml` (7 URL, tutti 200). Subito dopo l'invio Search Console può scrivere «Impossibile recuperare»: è normale nelle prime ore; se resta così per più giorni, ricontrollare.
- **Procedura:** proprietà «Prefisso URL» `https://bimnews.github.io/` in Search Console, verifica con il metodo «Tag HTML» (Marco manda il codice, Claude aggiunge `<meta name="google-site-verification" content="…">` nella testa di `index.html`), poi invio di `sitemap.xml`. Se si aggiungono manuali, aggiornare la sitemap.

## Regole fisse

- **Principi etici NON negoziabili (Marco, 15/11/2026):** tutto deve essere gratis per chi visita il sito; nessun cookie di tracciamento (GoatCounter va bene perché non usa cookie). Gli eventi a pagamento si segnalano come tali, senza assumersene la responsabilità. Sono scritti nel riquadro `.bn-rules` di BIM News.
- **Notizie:**
  - NESSUN limite di data (decisione di Marco del 16/11/2026): l'archivio parte dall'«anno zero» del nome, dicembre 1992 (G.A. van Nederveen e F.P. Tolman, «Modelling multiple views on buildings», Automation in Construction 1(3), DOI 10.1016/0926-5805(92)90014-B), e va avanti fino a oggi senza salti. L'idea più antica (Eastman, Building Description System, 1975) resta nella timeline di BIM in breve, non tra le notizie. L'etichetta «Storico» e il campo `st` sono stati tolti. Testi: criteri (v0050), archivio (v0084), FAQ «Da quando partono le notizie?» (v0149, v0150, `strumenti/faq.py`), Mappa del sito «Archivio dal 1992» (v1206). Le date senza giorno usano il 1° del mese o dell'anno, spiegato nel memo `m`.
  - la mappa resta neutra;
  - nessun logo o immagine protetta: foto solo CC0 (Wikimedia Commons), icone disegnate da noi.
- **Accesso e dati:**
  - niente email di Marco nelle richieste a servizi esterni;
  - niente servizi che chiedono di registrare un'email: per esempio OpenAlex no, Crossref sì.
- **Fonti:**
  - città, regioni e province valgono come fonti solo se danno un contributo concreto al BIM;
  - mai lanci di prodotti, blog, social o cronaca locale.
- **Niente frasi sul nostro lavoro dentro il sito (Marco, 17/11/2026):** il sito è un posto pubblico. Non scrivere nelle pagine frasi che raccontano i nostri processi interni o i lavori futuri («altri paesi arriveranno con la ricerca a tappeto», «la aggiungeremo quando arriverà», «non abbiamo ancora trovato…», «la mappa cresce con la ricerca…»). Si scrive solo quello che è vero oggi per chi legge. Così si risparmiano anche traduzioni inutili. Vale anche per il memo `m` delle notizie, che sul sito si vede: solo fatti utili a chi legge, in forma impersonale (19 memo ripuliti in revisione 135). Restano ammesse le parti volute da Marco: le schede «Work in progress» del curatore, la FAQ su come si aggiorna il sito e le lingue «in verifica».
- **Mai pubblicare:** l'articolo «Suoni per chitarra con il modeler» (sintesi della playlist Fractal) resta privato di Marco (15/11/2026).
- **Bozze:** la bozza «La prima routine» per AutoCAD è in attesa di revisione da parte di Marco e non va pubblicata. Una copia è nel backup zip.
- **File che Marco deve ancora mandare:** gli originali di `SOSTXRIF.lsp` e `RETINITRASP.lsp` (quelli nel sito sono riscritti e «da provare») e i file `.dyn` di Dynamo.

## Lavori in sospeso, in ordine di priorità

1. **Globo 3D: PUBBLICATO il 15/11/2026 (revisione 106) dopo il sì di Marco.**
   - **Codice:** `assets/globo/` (`globo.js`, `mondo.json`, `citta.json`, le librerie, `LICENZE.txt`); `loadGlobe()` parte dopo `loadMap()`, solo nella versione completa.
   - **Cosa fa:** orientamento iniziale dal fuso orario; asse inclinato di 23,44°; giorno e notte reali; luci delle città; clic su un paese → volo sul paese, poi passaggio alla mappa piatta; «← Mondo» → torna il globo.
   - **Movimento:** il globo ruota soltanto, senza oscillare in su e in giù: Marco l'ha trovato brutto (15/11/2026). Rotazione continua.
2. **Feste (animazioni stagionali): PUBBLICATE il 15/11/2026 (revisione 115) dopo il sì di Marco; Pasqua (cestino e coniglio) approvata e attivata in revisione 117.**
   - **Codice:** in fondo a `index.html`, blocco «feste» (CSS `.fest-*` e script). Canvas `.fest-cv` nella fascia alta della mappa della home (non nella versione essenziale), simbolo `.fest-orn` sulla «B» di `.fc-h`, pulsante `.fest-chip` in alto a destra con «Nome · Che cos'è ↗» che porta a Wikipedia nella lingua del sito (`Special:Search`).
   - **Per tutti, ovunque:** Marco ha deciso di non legarle all'area geografica né alla religione (discorso inclusivo). Se due feste coincidono si alternano un giorno l'una e un giorno l'altra.
   - **Periodi (calcolati da soli):** Natale 8/12–6/1 (neve geometrica, cappellino); Hanukkah 24 Kislev + 8 giorni (menorah, `Intl` calendario `hebrew`); Capodanno lunare dalla vigilia al 15° giorno (lanterne rosse, calendario `chinese`); Ramadan (mese 9), Eid al-Fitr (1–3 Shawwal), Eid al-Adha (10–13 Dhu al-Hijja) con mezzaluna e lanterne (`islamic-umalqura`); Pasqua cattolica e ortodossa, dalla Domenica delle Palme al Lunedì dell'Angelo (computo nel codice; rametto d'ulivo sulla «B», cestino di uova e coniglietto che ruba un uovo, richiesta di Marco).
   - **Tabelle da aggiornare ogni anno:** `DIWALI` (2026: 8/11, 2027: 29/10; si vede ±2 giorni) e `VESAK` (2027: 20/5, ±3 giorni; varia da paese a paese). Senza la riga dell'anno la festa non compare.
   - **Anteprima di una festa:** `?stagione=natale|hanukkah|lunare|ramadan|eid|adha|pasqua|vesak|diwali`. L'elenco `OK` nello script dice quali si attivano da sole (ora tutte, Pasqua compresa: sì di Marco del 15/11/2026).
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
5. **Ricerca a tappeto per paesi e per anni: la fa Claude nelle sessioni con Marco, non il task del lunedì.**
   - **Fatto:**
     - America Latina: Messico, Costa Rica (3), Uruguay, Colombia (3), Perù (2);
     - Africa: Etiopia e Sudafrica.
     - Europa (15/11/2026, revisione 122): Svizzera (7: KBOB 2018, piano d'azione «Svizzera digitale» con BIM obbligatorio 2021/2025, strategia BLO/ASTRA 2021 e 2024, dati nel BIM 2022, ISO 19650 2023, passaporto digitale dei prodotti 2025), Paesi Bassi (NLCS e COINS obbligatori, 2018), Lituania (BIM obbligatorio a tappe dal 2021), Estonia (requisiti BIM di RKAS 2018 e 2020). Danimarca: aggiunta la norma IKT del 2013.
   - **Cercati senza fonti istituzionali valide:** Ruanda, Nigeria, Ghana, Kenya (solo un discorso), Marocco, Algeria e Tunisia (nessun obbligo BIM), Egitto (il codice BIM esiste ma la fonte non era raggiungibile).
   - **Storia mondiale 1992–2014 (revisione 124):** nome «Building Information Model» (1992), IAI (1995), IFC 1.0 (1996), «Building Information Modeling» si diffonde (2002), GSA (2003), buildingSMART e ISO/PAS 16739 (2005), BS 1192 e Senaatti (2007), ISO 29481-1 (2010), Government Construction Strategy (2011), PAS 1192-2, ISO 16739 e obbligo danese (2013), direttiva 2014/24/UE (2014). Da aggiungere, verificando: NBIMS-US v1 (2007), Statsbygg, Corea (PPS), Singapore (BCA e-submission), Paesi Bassi (IFC nella lista del Forum Standaardisatie), Germania (Stufenplan 2015), Francia (PTNB 2015), Italia prima del 2015.
   - **16/11/2026, revisione 132:** tappe storiche NBIMS-US v1 (2007), Paesi Bassi IFC «applica o spiega» (15/11/2011), Singapore 2013, Corea PPS (2013/2016); Svezia (Trafikverket 2015), Ucraina (strategia 2021), Romania (ordine 2221/2023), Grecia (strategia 2024 e linea guida TEE 2026) e la proposta UE di Public Procurement Act (9/9/2026, art. 65: BIM obbligatorio nei lavori da 25 milioni). Statsbygg (Norvegia) ancora senza fonte datata; UNI 11337:2009 non aggiunta (è una norma di codifica, già nella timeline).
   - **17/11/2026, revisione 135:** tolte dal sito le frasi sul nostro modo di lavorare (certificazioni: «Altri paesi arriveranno con la ricerca a tappeto»; roadmap: «La mappa cresce con la ricerca…», «se una fonte non spiega il perché, lo scriviamo…», Colombia «non abbiamo ancora una fonte…», Etiopia «non sappiamo se è partito»; dimensioni BIM: «la aggiungeremo quando arriverà» → «Nessuna notizia dedicata nella rassegna.»; video universitari: «Dal MIT e da Harvard non abbiamo trovato, per ora…»), con le traduzioni nelle 10 lingue. Nuova regola fissa (vedi Regole fisse).
- **16/11/2026, revisione 134:** Taiwan (piano PCC 2014 e rilievi della Corte dei conti), Nuova Zelanda (guida appalti 2019), Slovenia (GZ-1, 2022), Islanda (requisiti FSRE 2023), Lettonia (obbligo dal 2025), Finlandia (permesso su modello dal 2026), Slovacchia (roadmap 2026: obbligo per lo Stato, non per i progettisti), Turchia (regolamento 5/8/2026, IFC per i permessi dal 2029), Croazia (hrBIM, 2026).
   - **Cercati il 16/11/2026 senza fonti istituzionali utili:** India (solo siti di formazione), Arabia Saudita, Belgio (nessuna legge, solo siti privati), Bulgaria (la modifica della legge urbanistica del 2023 non parla di BIM), Serbia (la riforma del 2023 non parla di BIM), Lussemburgo (solo la guida volontaria del CRTI-B, senza data), Africa francofona (niente).
   - **Restano:** Egitto in arabo, il resto dell'Asia e del Medio Oriente, e l'approfondimento dei paesi già presenti (per esempio la Danimarca dopo il 2013).
   - **Strumenti:** `strumenti/sweep_add.py` (aggiunge notizie complete di te/xe/lo/tl/xl, data di raccolta 15/11/2026: aggiornala), `strumenti/ver.py` (scarica una pagina e mostra le frasi con le parole chiave) e `strumenti/add_news.py` (aggiunge le notizie calcolando id e settimana).
6. **Tai Chi e Kung Fu: PUBBLICATO il 15/11/2026 (revisione 107), `#fuori-taichi` in Fuori dallo studio.**
   - **Immagine:** le cinque virtù (智 仁 信 勇 忍) ricostruite in HTML e CSS (`.kf-fig`), con caratteri veri in font kaishu di sistema, non come immagine.
   - **Testi:** riassunti con parole nostre dalla pagina https://www.kungfuetaichi.com/5-virt%C3%B9, con due brevi citazioni.
   - **«Perché per me è importante»:** scritto il 15/11/2026 dal racconto di Marco (valvola di sfogo, equilibrio, bene e male, «scegliere le proprie battaglie» anche nel lavoro).
7. **Statistiche delle visite: sezione PUBBLICATA il 15/11/2026 (revisione 110), «Le visite del sito» (`#visite`) nella pagina Mappa del sito.**
   - **Cosa mostra:** il totale, gli ultimi 30 giorni e le 10 pagine più visitate. Legge `https://mscigliuolo.goatcounter.com/counter/<path>.json`, dove i path sono `/`, `/bim-news` e così via, come in `count()`; `TOTAL` dà il totale del sito.
   - **Quando si carica:** solo quando si apre la vista `mappa`. Nel piè di pagina, «Statistiche anonime» porta lì.
   - **Contatore pubblico:** Marco l'ha acceso il 15/11/2026 («Allow adding visitor counts» in GoatCounter); i numeri arrivano. `TOTAL` comprende anche gli eventi, come i clic sulle fonti, quindi è più alto della somma delle pagine.
8. **Timeline doppia «Il BIM nel tempo: il mondo e l'Italia»: PUBBLICATA il 15/11/2026 (revisione 109) dopo il sì di Marco.**
   - **Dove:** in BIM in breve, `#b5-t2`, dopo la lisca; c'è anche la voce «05 Mondo e Italia» nell'indice e nella mappa del sito.
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
   - **Revisione delle traduzioni:** non ci sarà (Marco non può farla). Al suo posto c'è l'avviso «tradotto con AI, può contenere imprecisioni» (`#ai-tr`, revisione 121). Task chiuso.
10. **Articoli da scrivere con Marco (impostati il 15/11/2026; testi da fare insieme):**
   - **In `#wip` → «Articoli in preparazione»** (`.wip-art`), ogni scheda con «Cosa conterrà»:
     - `art-hoover`: lo script «Hoover», che legge un Excel con materiali, parametri e informazioni di sistema;
     - ~~`art-ifc-zero`~~: pubblicato come manuale «Un IFC scritto a mano» (punto 18);
     - `art-10-tips`: i 10 consigli, di cui 6 scritti (salvataggi automatici, gestione del tempo, template, gruppo di continuità, straordinari, riflessione) e 4 da definire;
     - `art-ifc-excel`: la biblioteca IFC in Excel;
     - `art-ifc-versioni`: le versioni di esportazione IFC a confronto;
     - `art-ifc-dialogo`: far dialogare i software con l'IFC e il modello federato;
     - `art-img-lingua`: manuali con immagini SVG, con le scritte che seguono la lingua.
   - **In `#studio` → Riflessioni:** `studio-oltre-noi`, «Il mondo oltre noi» (che ne sarà dei nostri modelli tra 200 anni; da fare una ricerca sul più antico disegno di progetto arrivato fino a noi).
   - **Collegamenti tra sottopagine:** usare `data-goto-art="id"`.
   - **Proverbio** «Ciò che cresce lentamente mette radici profonde»: origine non trovata in nessuna fonte, ora scritto «proverbio di origine incerta» (revisione 125).
   - **Tutti gli articoli in preparazione sono in fase «Bozza»** (decisione di Marco del 16/11/2026: non si aspetta, i testi arriveranno col tempo).

11. **BIM in breve, «01 · Che cos'è» riscritto: PUBBLICATO il 15/11/2026 (revisione 112).** Tre passi: a mano (Palladio, 1570, MET CC0, `assets/foto/palladio-rotonda.jpg`, con credito nella Mappa del sito), il CAD (linee con attributi) e il BIM (oggetti con parametri, muro interattivo `#bim-demo`); poi «Perché cambia tutto» e «Attributo o parametro?».

12. **Traduzione di TUTTE le scritte fisse: COMPLETA in 11 lingue (revisione 115, 15/11/2026).**
   - **Esclusi:** notizie, agenda, video e articoli di BIM Accademia, perché cambiano ogni settimana.
   - **Estrazione:** `strumenti/lingue/extract.js` (Playwright su tutte le viste) → `strumenti/lingue/src/voci.json` (1198 voci, circa 105.000 caratteri) e 14 pacchetti `src/pNN.txt` («id<TAB>testo o HTML»).
   - **Traduzioni:** `strumenti/lingue/tr/<lingua>/pNN.txt`, stesso formato. Nelle voci HTML si traducono solo i testi; tag e attributi restano identici, e `compila.py` scarta le righe in cui cambiano.
   - **Compilazione:** `python3 strumenti/lingue/compila.py` → `assets/lingue/<lingua>.json` (`t` testi, `h` blocchi HTML, `a` attributi), con il vecchio `dizionario.py` come riserva.
   - **Il motore** (in `index.html`, «lingue: traduce tutte le scritte fisse»):
     - scarica il file della lingua scelta;
     - traduce i blocchi interi, poi i testi sciolti, poi `placeholder`, `title` e `aria-label`;
     - le parti che cambiano (mesi, «N notizie», «Ultimo aggiornamento») le traduce a pezzi;
     - ritraduce le parti generate dal JS (MutationObserver, con `takeRecords` per non creare cicli);
     - con l'italiano rimette i testi originali.
   - **Pacchetti:** ora sono 16 (`p15` = voci della Mappa del sito, `p16` = la guida) e 1284 voci; in `tr/<lingua>/extra.txt` ci sono i modelli delle frasi con numeri (`§conteggio`, `§pagina`, `§articoli`, `§anno`, `§passo`, `§vedi`) e qualche voce fuori pacchetto.
   - **Stato:** tutte le 11 lingue complete (en e fr in revisione 114; de, es, pt, ru, ar, zh, ja, ko in revisione 115). Le 8 voci in meno (1221/1284) sono le domande FAQ tolte. I titoli dei libri: originali o titoli pubblicati noti; quando non ero sicuro del titolo tradotto ho lasciato l'originale. Serve comunque una revisione di madrelingua.
   - **Nelle lingue diverse dall'italiano** BIM Accademia mostra l'abstract originale inglese e le scritte della scheda in inglese (`siteIt()`).
   - **Se si cambiano testi del sito:** rilanciare `extract.js`, tradurre le voci nuove e ricompilare.

13. **Appunti di Marco del 15/11/2026, da fare dopo le traduzioni** (riordinati per area):
   - **Il curatore:**
     - **Tai Chi:** fatto in revisione 119. Il «maestro dei maestri» di Marco è Shin Dae Woung (Marco l'aveva scritto «Schin Dae wuong»; grafia corretta dal sito ufficiale shindaewoung.com): scomparso nel 2016, in Italia dal 1975, libri *Scuola di kung fu* vol. 1 (1988) e vol. 2 (1997), Edizioni Mediterranee (verificati su Libraccio). Nessun link a librerie: si cita solo il titolo. La scuola di Bolzano è citata con la scheda del Registro CONI; il legale rappresentante del registro non va scritto come maestro.
     - **«Ispirazioni»: PUBBLICATA in revisione 125** (`#fuori-ispirazioni`, 06 in Fuori dallo studio): 29 canali YouTube verificati (handle @… aperti su YouTube) in 6 gruppi (in revisione 128 aggiunto «La vera interpretazione dei Sogni», @SaraLunaris, confermato da Marco). Tolti su richiesta di Marco: Alle Cuoghi, Beyond Ordinary World, RGN. Da chiarire con Marco: «Comunicazione …» (nome troncato, non trovato).
     - **Via Lattea dietro il globo della home:** codice pronto in `assets/globo/globo.js` (`mwBuild()`, `MWON`), ACCESA SOLO con `?vialattea=1`. La versione «migliorata per il computer» (revisione 127) NON è piaciuta a Marco: in revisione 128 è tornata quella della revisione 126. Per attivarla per tutti: `MWON=true`.
     - **Portfolio:** la grafica è rimasta quella vecchia, va resa coerente con il resto della sezione. Poi le anteprime dei progetti affrontati, poi l'elenco dei modelli fatti con Guadagnuolo. Servono materiali da Marco.
   - **BIM in breve, agenda a calendario e giornate della tecnologia: PUBBLICATI in revisione 120** dopo il sì di Marco (15/11/2026).
     - **BIM in breve** (`#bim-5-minuti`): linea del tempo `.evo-tl` sopra i tre passi (1570, 1963, 1982, 1996, 2002, oggi; fonti Wikipedia in inglese), approfondimento `.evo-deep` su attributi e parametri (codice CAD/BIM, grafo delle dipendenze, IfcWall/IfcExtrudedAreaSolid/Pset_WallCommon/IfcRelVoidsElement), sezione `#b5-futuro` «10 · Cosa ci riserva il futuro?» (3 schede «sta già succedendo» legate alle notizie n10, n100, n36 e 3 «domande aperte»). I due blocchi di codice `.evo-code` restano in italiano in tutte le lingue.
     - **Agenda a calendario** `#agc` in `#agenda`, sopra le tre colonne: griglia del mese con scadenze, eventi (filtri area e costo), webinar e giornate della tecnologia (array `TECH`, `window.TECH_DAYS`, `techDate()` per il 4° giovedì di aprile e il 1° lunedì di ottobre). Clic su un giorno → elenco con i link. I nomi delle giornate e degli appuntamenti restano in italiano, come il resto dell'agenda.
     - **Date delle giornate verificate:** 11/2, 13/2, 4/3, 14/3, 12/4, 21/4, 4° giovedì di aprile (Girls in ICT, ITU), 26/4 (WIPO), 16/5 (luce, UNESCO), 17/5, 28/9, 1° lunedì di ottobre (Habitat), 14/10 (normazione ISO/IEC/ITU), 31/10, 10/11.
     - **Da fare se Marco lo chiede:** un'etichetta in home nel giorno stesso di una giornata della tecnologia (come `.fest-chip`).

14. **«Roadmap dell'obbligatorietà» in BIM in breve: PUBBLICATA il 16/11/2026 (revisione 133) dopo il sì di Marco.** Sezione «11 · La strada verso l'obbligo» (`#b5-obbligo`): linea degli anni di partenza dell'obbligo e tre colonne (Obbligatorio 18, In arrivo 6, Non ancora 11), ogni riga con le notizie che la provano; per i paesi «non ancora» il perché solo se la fonte lo dice, altrimenti «la fonte non lo spiega». In revisione 134 salita a Obbligatorio 20, In arrivo 7, Non ancora 16. Le righe «Notizie:» hanno l'etichetta separata dai link (`.ob-lab` e `.ob-src`, escluso in `extract.js`): il motore delle traduzioni sostituisce i blocchi HTML in base al testo, e due righe con lo stesso testo («Notizie: 2020») si sarebbero scambiate i link. Generata da `strumenti/roadmap_obbligo.py` (dati in testa al file: aggiornarli quando arrivano notizie nuove, poi rilanciare; il blocco sta tra `<!-- obbligo:inizio -->` e `<!-- obbligo:fine -->`, il CSS tra `/* obbligo: roadmap` e `/* obbligo:fine-css */`; aggiunge anche il bottone «11 L'obbligo nel mondo» nell'indice e la voce in `SITEMAP`). Traduzioni nel pacchetto `p21` (125 voci, generate da `strumenti/lingue/p21_roadmap.py`, che contiene i nomi dei paesi e le frasi nelle 10 lingue): se si cambiano i dati della roadmap, aggiornare anche quel file, rilanciare `extract.js` per gli id nuovi e ricompilare. Servirà poi come base per un articolo di riflessione di Marco.

15. **Georeferenziazione BIM: articolo e convertitore PUBBLICATI il 18/11/2026 (revisione 136) dopo il sì di Marco.**
   - **File:** `manuali/georeferenziazione-ifc.html` (articolo, stile dei manuali, 9 capitoli + fonti; il convertitore è incorporato con un iframe `?embed=1` che comunica l'altezza con `postMessage`) e `manuali/convertitore-georeferenziazione.html` (file unico autonomo, scaricabile, funziona offline; 5 schede: converti parametri, converti un punto, parametri da punti noti con Helmert ai minimi quadrati, diagnosi di uno spostamento, nord e scala UTM). Scheda `#man-pro-12` in `#studio` → «I manuali di Claude»; i due URL sono in `sitemap.xml`. L'articolo e il convertitore sono solo in italiano; la scheda è tradotta nel pacchetto `p22` (`strumenti/lingue/p22_georef.py`).
   - **Formati:** Revit, Archicad, Allplan, «Altro software» (definizione geometrica), IFC 4/4.3 (IfcMapConversion), IFC 2x3 (ePSet_MapConversion ed ePSet_ProjectedCRS, più RefLatitude/RefLongitude e TrueNorth con la convergenza). Rappresentazione comune = formula IfcMapConversion (θ antiorario da Est all'asse x).
   - **Convenzioni e fonti:** Revit «Ovest» → θ = −angolo (dalla lettura del campo «dal nord di progetto al nord reale»); Archicad θ = 90° − North Angle (Graphisoft Community 2022); Allplan senza verso documentato (definizione geometrica). Calcoli UTM con le serie di Karney, confrontati con PROJ (pyproj 3.8: differenze < 0,04 mm, convergenza identica); 30 coppie andata e ritorno, errore massimo 0,04 mm. La convergenza a E 680000 / N 5150000 (EPSG:25832) vale +1,7009° (nord geografico a ovest di quello di rete).
   - **Caso reale anonimizzato** dal PDF di Marco (errore 1:1000 tra un modello in mm e modelli in m): nomi del progetto e coordinate vere tolti, numeri inventati (E 680 000, N 5 150 000, quota 250, angolo 12°30′ Ovest). Il PDF non va pubblicato.
   - **Unità nel dialogo di Revit, chiarito con Marco il 18/11/2026 (revisione 137):** nel suo modello in mm (template MEP; l'architetto modella in m), «Specifica coordinate in un punto» accetta i valori in metri; digitando i millimetri Revit avvisa che il modello supera la distanza ammessa (li legge come metri). Il convertitore, con Revit come arrivo, dà solo i valori in metri. Non provati: le proprietà del Punto base progetto e altre versioni. Resta ignoto quale valore causò il primo errore 1:1000.
   - **Struttura dell'articolo dalla revisione 138 (richiesta di Marco: «niente supposizioni, prima la corretta impostazione del modello iniziale per tutti i BIM specialist, poi tutto il resto»):** 1 Impostare il modello iniziale (coordinatore: punto comune, coordinate in metri, angolo, EPSG, scheda nel capitolato e nel pGI; BIM specialist: unità dichiarata, geometria vicino all'origine, coordinate per Revit/Archicad/Allplan, mai spostare la geometria, export comune; controllo: punto noto e federazione), 2 Perché i modelli non coincidono, 3 Matematica, 4 IFC 2x3/4/4.3, 5 I software nel dettaglio (solo verificato; i limiti in un unico riquadro), 6 Caso 1:1000, 7 Nord e scala, 8 Convertitore. Tolti «Come ho lavorato» (ora riassunto nel riquadro finale) e la checklist (assorbita nel capitolo 1).
   - **Se si cambiano le convenzioni:** rilanciare i controlli (confronto con pyproj e andata e ritorno su tutte le coppie) prima di pubblicare.

16. **Libreria IFC 4.3: PUBBLICATA il 19/11/2026 (revisione 139) dopo il sì di Marco.**
   - **Origine:** l'Excel di Marco `IFC_4x3_COMPLETE_LIBRARY_rev.xlsx` (ramo IfcProduct di IFC 4.3 ADD2), controllato con IfcOpenShell 0.9.0: 214 classi (22 astratte), 1422 righe classe + PredefinedType, nessuna differenza dallo schema.
   - **Licenza (decisione di Marco):** i testi ufficiali buildingSMART sono CC BY-ND 4.0 (niente traduzioni o versioni tagliate pubblicate). Per questo nomi e descrizioni IT/EN sono **scritti da noi**, non tradotti; la definizione ufficiale è solo un link. Le traduzioni di lavoro e le definizioni dell'Excel originale NON vanno pubblicate.
   - **Dati:** `strumenti/ifc/struttura_classi.tsv` e `struttura_valori.tsv` (nomi IT di Marco, deprecazioni). Testi nostri: `testi/classi.tsv` (214 classi), `testi/valori.tsv` e `valori_a…d.tsv` (PredefinedType; 6ª colonna facoltativa = nome IT corretto, per esempio COPING → Copertina, PARAPET → Parapetto, STATION → Progressiva), `valori_e.tsv` generato da `ripeti.py` (distribuzioni strutturali, classi «Varying», IfcWallStandardCase = IfcWall). USERDEFINED e NOTDEFINED hanno testi automatici in `genera.py`.
   - **Generazione:** `python3 strumenti/ifc/ripeti.py`, poi `strumenti/ifc/genera.py` (serve openpyxl) → `manuali/libreria-ifc/ifc-4.3-map.json` e `IFC-4.3-library.xlsx` (in inglese: Read me, Library, Classes). `genera.py` segnala classi o valori senza testo.
   - **Pagina:** `manuali/libreria-ifc.html` (ricerca con `?q=`, scheda della classe con IfcExportAs/IfcExportType da copiare, mappa mentale apribile con rami allineati in alto, link diretto `#ifc=Classe.VALORE`). Scheda `#man-pro-13` in `#studio` → I manuali di Claude, con il campo di ricerca nella prima riga (il clic su campo e pulsante non apre la scheda: eccezione aggiunta nello script delle schede a scomparsa). Tolta la bozza WIP `art-ifc-excel`. URL in `sitemap.xml`. Traduzione della scheda nel pacchetto `p23` (`strumenti/lingue/p23_libreria_ifc.py`); la pagina della libreria è solo in italiano, i file in inglese.
   - **Altre lingue delle descrizioni:** solo IT ed EN; nella pagina e nel Read me c'è l'invito «Ti servono in un'altra lingua? Scrivimi su LinkedIn» (scelta di Marco).
   - **Possibili sviluppi:** le stesse librerie per IFC 2x3 e IFC 4 (bozza WIP `art-ifc-versioni`), i tipi (IfcWallType…) e i Pset.

17. **«Le mie proposte», proposta 1 «Un dizionario nazionale dei dati BIM pubblici»: PUBBLICATA il 20/11/2026 (revisione 145) dopo il sì di Marco.**
   - **Dove:** `manuali/dati-pubblici.html` (articolo in 9 capitoli + prototipo con ricerca, filtri livello/gruppo/fase, scheda, equivalenze, link diretto `#p=CODICE`) e `manuali/dati-pubblici/` (dizionario.json, dizionario-dati-pubblici.xlsx, IT-nucleo.ids, IT-BZ-estensione.ids). Scheda `#prop-01` in `#proposte` (al posto di «Work in progress: le prime proposte sono in preparazione»; resta la riga LinkedIn). URL in `sitemap.xml`. Traduzioni della scheda nel pacchetto `p25` (`strumenti/lingue/p25_dati_pubblici.py`); la pagina è solo in italiano.
   - **Generatore:** `strumenti/proposta/genera.py` (dati in testa al file; controlla ogni mappatura sullo schema IFC 4.3 ADD2 con IfcOpenShell 0.9 e rilegge gli IDS con l'XSD; serve `pip install ifcopenshell xmlschema pystache` e `pip install --no-deps ifctester`). 36 parametri: 28 nel nucleo IT, 8 nell'estensione IT-BZ. In IDS 1.0 l'entità non include le sottoclassi: per «tutti gli elementi» si elencano le 143 classi concrete. IDS provati su un IFC di prova.
   - **Excel della Provincia di Bolzano: NON è pubblico** (il capitolato della gara Fallmerayer, §2.6–2.7, dice che la struttura dati completa «sarà condivisa con l'affidatario»). L'estensione IT-BZ usa solo gli estratti pubblici delle tabelle 5–8. Errori di traduzione nel PDF segnalati a Marco in chat, NON nel sito.
   - **Capitolo 6, la famiglia di Marco** «15.08.02.02_Punto luce», tipo «da 0 a 5m» (screenshot del 20/11/2026, sì di Marco a usarla): 16 parametri di dato, 14 con un posto in IFC (classificazione 7.1.9, relazione col piano, Name, tipo, materiale, Qto_JunctionBoxBaseQuantities / geometria), 2 restano nell'estensione (Bestandsaufnahme_Consistenza e Descrizione). Esce come IfcJunctionBox NOTDEFINED: nel testo il consiglio POWER. Nel testo «Unità» scritto corretto (nella famiglia è «Unitá»); citata l'ambiguità Durchmesser (diametro) / Perimetro.
   - **Corretto anche:** `manuali/manuale.css`, nel tema scuro i pulsanti `.btn.ghost` avevano il testo scuro su fondo scuro (valeva per tutti i manuali).

## Fatto di recente

- **20/11/2026, revisione 150:** figura del coordinatografo ruotabile anche col dito; figure 2–4 in anteprima.

- **20/11/2026, revisione 148, PUBBLICATA dopo il sì di Marco:** «I manuali di Claude» riordinati: tolti il 02 «Manuale parametri Revit», il 07 «Promemoria avvio progetto MEP» (unito alla Checklist BIM-MEP) e il 10 «Programma di studio: c.a.» (tornerà forse in una futura sezione «Strutture»). Numeri visibili rifatti 01–11; gli id `man-pro-NN` restano quelli vecchi (non rinominarli: servono a copertine e collegamenti). Tre articoli nuovi, scritti dagli artefatti di Marco (documenti Claude Docs «Manuale famiglie Revit 2026», «Checklist BIM-MEP» con i dati JSON dell'artefatto, «Promemoria avvio progetto MEP», «Guida alla progettazione antincendio»):
  - `manuali/famiglie-revit.html` (`#man-pro-01`): metodo, non tutorial; host con aiuto interattivo (quiz), piani di riferimento, vincoli, parametri, MEP, IFC, checklist in localStorage `famiglie-revit-ck`.
  - `manuali/checklist-bim-mep.html` (`#man-pro-06`, ora n. 05): domande d'avvio, template MEP passo per passo (master e template), checklist per disciplina (dati ripuliti dai riferimenti interni), revisione di fine progetto; localStorage `checklist-bim-mep-v1`.
  - `manuali/antincendio.html` (`#man-pro-09`, ora n. 07): percorso guidato (committente → destinazione → dimensioni → DPR 151 categoria, regola tecnica, classificazione RTV con le tabelle V.4 e V.7 lette sulle pagine del testo coordinato VVF in vigore dal 1/1/2023, Les/Lcc), locale per locale, esodo, materiali, REI, mappa del workflow con Property Set IFC 4.3 verificati con IfcOpenShell 0.9, UNI 9795, checklist. Regole provinciali BZ dalla pagina Brandschutzbestimmungen (scuole DPP 51/2006 e 10/2009, alberghi DPGP 11/1989 e DPP 2/2017, spettacolo, impianti termici prevalgono). Premessa corretta a Marco: le regole tecniche non cambiano tra pubblico e privato.
  - Traduzioni delle tre schede nel pacchetto `p26` (`strumenti/lingue/p26_manuali_mep.py`); i tre URL in `sitemap.xml`.
  - **Stessa revisione, dopo la prima anteprima:** la guida antincendio dichiara che segue le norme italiane (riquadro iniziale, pill, scheda nel sito) e ha un primo passo «Dove si trova l'edificio?» (Alto Adige / altre regioni / fuori dall'Italia): le note provinciali (campo `bz` di ogni destinazione) compaiono solo per l'Alto Adige; per le altre regioni l'obbligo BIM è quello del D.Lgs. 36/2023 art. 43 (D.Lgs. 209/2024, oltre 2 milioni dal 1/1/2025); fuori dall'Italia la guida lo dice e non dà valori. Idea di Marco: un progetto a parte con le norme antincendio del mondo (da valutare insieme).
- **20/11/2026, revisione 149:** guida antincendio, «altre regioni»: verificato e precisato che in Trentino la prevenzione incendi la gestisce il Servizio antincendi e protezione civile della Provincia di Trento e in Valle d'Aosta l'Ufficio prevenzione incendi del Corpo valdostano; fonti aggiunte.
- **Prossimo lavoro chiesto da Marco (20/11/2026):** una sezione «MEP» del sito, separando la parte «Didattica» dagli articoli di esempio, con una serie di articoli che spieghino passo passo un impianto termosanitario fino nel dettaglio, con figure animate fatte con la skill Anatomy (repository `bimnews/figure`). Decisioni di Marco del 20/11/2026: la «Didattica» in due sottopagine distinte dagli articoli di esempio; la serie parte dal fabbisogno (che cosa c'è e che cosa serve), poi la linea d'azione e gli impianti da usare. Prima di scrivere, proporgli il piano della serie. Piano proposto il 20/11/2026: 11 articoli (1 fabbisogno, 2 linea d'azione, 3 generazione, 4 accumulo e separazione, 5 distribuzione, 6 emissione, 7 regolazione, 8 ACS e Legionella, 9 idrico, 10 scarichi, 11 dal progetto al modello), ognuno con una figura Anatomy. Marco ha detto «facciamo il pilota» (articolo 1). Regole di Marco: usare la sua guida termosanitaria (link ancora da ricevere: tra gli artefatti c'è solo la figura «Vaso di espansione», Fig L2, da usare nell'articolo 4) e togliere ogni riferimento personale e dello studio, con esempi molto generici.

- **20/11/2026, nessuna revisione:** proposta una nuova veste grafica «D» (carta da lucido, titoli serif Newsreader, linee di quota CAD come separatori, poi uno strato «umano» con note a penna in Caveat e nuvole di revisione), provata solo in anteprima con CSS iniettato da Playwright. **Marco l'ha scartata: si resta con la veste C.** Non riproporla; se tornerà sul tema, chiedergli prima quale direzione vuole.

- **20/11/2026, revisione 147:** nel piè di pagina «Online dal 9 novembre 2026 · Sito aggiornato il …», approvato da Marco.
- **20/11/2026, revisione 146:** prima figura animata, il coordinatografo della georeferenziazione, nel capitolo 3 dell'articolo sulla georeferenziazione (repository `bimnews/figure`, skill anatomy).

- **20/11/2026, revisione 145:** pubblicata la proposta 1 «Un dizionario nazionale dei dati BIM pubblici» (punto 17): articolo, prototipo, Excel, JSON e IDS; scheda in «Le mie proposte» tradotta nelle 11 lingue.

- **19/11/2026, revisione 144:** pubblicato «Un IFC scritto a mano» (punto 18): casetta IFC4 scritta a mano, articolo per pattern con modello 3D e riferimenti cliccabili.

- **19/11/2026, revisione 143:** Work in progress, «Verifiche automatiche da checklist» passa da «Idea» a «Sviluppo» e «Test» insieme (tutte e due `now`), senza «Rilascio» (`.ph3`). Traduzione v0636 in `p08`, nuova voce v1677 (aria-label) in `p13`. Ora nessuna delle quattro schede del Work in progress ha la fase «Rilascio».

- **19/11/2026, revisione 142:** Work in progress, «Dalle superfici del disegno al calcolo CasaClima» passa da «Idea» a «Test» senza «Rilascio» (`.ph3`): funziona e ha ridotto sensibilmente il lavoro, restano da migliorare i dettagli (Marco). Traduzione v0638 in `p08`.

- **19/11/2026, revisione 141:** Work in progress, anche «Automazione dei disegni» (AutoCAD · AutoLISP) passa a fase «Test» senza «Rilascio» (`.ph3`): gli script funzionano e migliorano molto il lavoro, affinati di continuo «come nel kaizen» (parole di Marco). Traduzione v0634 in `p08`.

- **19/11/2026, revisione 140:** Work in progress, scheda «Libreria di famiglie con struttura dati provinciale»: fase «Test» (Idea e Sviluppo fatti), testo «già funzionanti, ma ci sto ancora lavorando: le sto testando e migliorando». Tolta la fase «Rilascio» solo da questa scheda (classe `.phases.ph3`, 3 colonne): Marco per ora non vuole condividere le famiglie, quindi non promettere un rilascio. Traduzioni: v0628 aggiornata in `p08`, nuova voce v1676 (aria-label «Fase attuale: test») in `p13`.

- **19/11/2026, revisione 139:** pubblicata «La libreria IFC 4.3» (punto 16): ricerca, mappa mentale, Excel e JSON, descrizioni nostre in italiano e inglese.

- **18/11/2026, revisione 138:** articolo sulla georeferenziazione ristrutturato: si apre con la procedura per impostare il modello iniziale.
- **18/11/2026, revisione 137:** georeferenziazione, regola delle unità in Revit (valori in metri nel dialogo anche nei progetti in mm), dalla prova di Marco.
- **18/11/2026, revisione 136:** articolo «Georeferenziazione BIM tra software diversi» con il convertitore gratuito e scaricabile (punto 15), scheda man-pro-12 tradotta nelle 11 lingue.

- **15/11/2026, revisione 100:**
  - **BIM in breve:** sezione «09 · Le certificazioni nel mondo» (`#b5-cert`) con 6 schede verificate: Hong Kong (obbligatoria, DEVB TC(W) 2/2021), Italia (volontaria, All. I.9 art. 1 c. 3 D.Lgs. 36/2023, UNI 11337-7, UNI/PdR 78:2020), Spagna (Plan BIM 2023), Regno Unito (BRE e UKAS, ISO 19650-2), Germania (VDI/bS 2552 Blatt 8.1), buildingSMART. Altri paesi da aggiungere con la ricerca a tappeto: Cina, Corea, Singapore, Francia, paesi nordici…
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
  - **BIM in breve:** «Che cos'è» riscritto.
  - **Le mie proposte:** la frase «aperte ai commenti» è sostituita dal rimando a LinkedIn, per coerenza con il disclaimer.
- **15/11/2026, revisione 113:** selettore delle lingue (11 lingue) con le scritte principali tradotte.
- **16/11/2026, revisione 134:** ricerca a tappeto, 9 notizie nuove (n220–n228) e roadmap dell'obbligo aggiornata con 9 paesi; corretto lo scambio dei link «Notizie:» nelle traduzioni.
- **16/11/2026, revisione 133:** pubblicata la sezione «11 · La strada verso l'obbligo» in BIM in breve, tradotta nelle 11 lingue (punto 14).
- **16/11/2026, revisione 132:** ricerca a tappeto, 10 notizie nuove (n210–n219, vedi punto 5); anteprima della roadmap dell'obbligatorietà (punto 14).
- **16/11/2026:** istruzioni del task settimanale spostate in `strumenti/task-settimanale.md`; il task ora parte lunedì alle 0:13.
- **16/11/2026, revisione 129 (rassegna del task del lunedì, settimana 9–15/11, pubblicata da Claude dalla patch):** 10 notizie (Italia, Germania 2, Belgio, Corea del Sud, Malesia, Vietnam, Indonesia, Marocco, Brasile/Paraná); nuovi sulla mappa Belgio, Vietnam, Indonesia. 20 articoli in BIM Accademia (79), 19 appuntamenti, 4 scadenze (Irlanda 2, Singapore, Perù), 7 video, 2 video universitari, 3 canali. Malese spostato tra le lingue della ricerca (37/39). n87 ora ha `n` vuoto. Il push dal task era fallito con 403: la patch è stata applicata in una sessione con Marco. Difetto noto: in FAQ i titoli «Lingue in cui cerchiamo (N)» e «Lingue in verifica (N)» non si traducono per intero perché il numero è nel testo (es. «Lingue under review (39)»).
- **16/11/2026, revisione 128:** tornata la prima Via Lattea (sempre solo con `?vialattea=1`); aggiunto il canale «La vera interpretazione dei Sogni».
- **16/11/2026, revisione 127:** Via Lattea migliorata per il computer (fascia più larga e continua, nucleo caldo a destra fuori dalla ricerca, polvere a strisce allungate); sempre solo con `?vialattea=1`.
- **16/11/2026, revisione 126:** Via Lattea dietro il globo, visibile solo in anteprima con `?vialattea=1`.
- **16/11/2026, revisione 125:** articolo «Ispirazioni» (28 canali, 11 lingue, pacchetto `p20`); tutti gli articoli in preparazione in fase «Bozza»; la notizia n87 (Singapore) ora ha `n` vuoto; proverbio con «origine incerta».
- **16/11/2026, revisione 124:** tolto ogni limite di data: l'archivio parte dal dicembre 1992, primo uso documentato di «Building Information Model». 11 notizie storiche 1992–2014 (dalla timeline del mondo, fonti già verificate) e tolta l'etichetta «Storico».
- **15/11/2026, revisione 123:** tappe fondative prima del 2015 (opzione 2 scelta da Marco): Danimarca (BEK 118/2013, BIM e IFC obbligatori nelle opere pubbliche), Finlandia (Senaatti-kiinteistöt, requisiti BIM 2007), Regno Unito (Government Construction Strategy, 31/5/2011), Stati Uniti (programma GSA 3D-4D-BIM, 2003). Le date del 1° gennaio di Finlandia e Stati Uniti sono convenzionali (spiegato nel memo). Da cercare ancora: Norvegia (Statsbygg, non verificato), Paesi Bassi (IFC nella lista «applica o spiega», data da verificare), Corea del Sud, Singapore, Svezia.
- **15/11/2026, revisione 122:** ricerca a tappeto, primo giro sull'Europa vuota: 11 notizie (Svizzera 7, Paesi Bassi 1, Lituania 1, Estonia 2), tutte con fonte aperta e verificata.
- **15/11/2026, revisione 121:** eliminato del tutto l'articolo «Suoni per chitarra con il modeler» (playlist Fractal): resta solo a Marco, non va mai pubblicato. Avviso «tradotto con AI, può contenere imprecisioni» nelle 10 lingue diverse dall'italiano (`#ai-tr` sopra il `main`, script in fondo alla pagina; in home da 900 px in su è sovrapposto a destra, per non spingere fuori la striscia degli eventi a 1280×650). Il task del lunedì ora cerca solo le notizie della settimana passata.
- **15/11/2026, revisione 120:** pubblicate le anteprime approvate da Marco: agenda a calendario con 15 giornate mondiali della tecnologia; BIM in breve con linea del tempo, approfondimento su attributi e parametri e «Cosa ci riserva il futuro?». Traduzioni nel pacchetto `p19` (giorni della settimana con l'iniziale maiuscola per non confonderli con «mar» = marzo). Tolta la patch da `strumenti/anteprime/`.
- **15/11/2026, revisione 119:** Tai Chi: il maestro dei maestri di Marco, Shin Dae Woung, con il sito ufficiale e i due volumi di *Scuola di kung fu*; traduzione nel pacchetto `p18`.
- **15/11/2026, revisione 118:** «BIM in 5 minuti» diventa «BIM in breve» (11 lingue, nuova frase iniziale); minuti di lettura in fondo a ogni articolo del curatore (`.st-rt`, circa 200 parole al minuto, etichetta nelle 11 lingue in `rtLabel()`); il curatore descritto come «blog personale con articoli utili»; scautismo con AGESCI di Triggiano e Aquile Randagie (film di Gianni Aureli, 2019); Tai Chi con la Scuola di Kung-fu Mien Ch'uan di Bolzano; pubblicati in PDF i manuali «Il suono» e «Libreria effetti per chitarra e basso» (`manuali/il-suono.pdf`, `manuali/effetti-chitarra-basso.pdf`, esportati dai documenti di Marco) e collegati alla scheda «La musica». Traduzioni nuove nel pacchetto `p17`.
- **15/11/2026, revisione 117:** regola di Marco sulla lingua delle notizie: sito in italiano → `t`/`x`; sito nella stessa lingua della fonte principale (`lo`) → `tl`/`xl` scritti in quella lingua (oppure `te`/`xe` se la fonte è inglese); altrimenti inglese `te`/`xe`. Dati in `strumenti/notizie_lo_*.tsv`, script `strumenti/add_lo.py`; al cambio di lingua la pagina si ricarica (`NEWS_L`). Attivata anche la Pasqua (sì di Marco). Il testo del task del lunedì è aggiornato: `lo` sempre, `tl`/`xl` solo se la fonte è in fr, de, es, pt, ru, ar, zh, ja o ko.
- **15/11/2026, revisione 116:** notizie in inglese nelle lingue diverse dall'italiano: campi `te` (titolo) e `xe` (sintesi) in `assets/notizie.json`, aggiunti con `strumenti/add_en.py` dai file `strumenti/notizie_en_*.tsv`; al cambio tra italiano e un'altra lingua la pagina si ricarica (`NEWS_EN`). Il task del lunedì ora scrive anche `te` e `xe`. Frasi «in italiano» corrette nelle traduzioni (v0022, v0083).
- **15/11/2026, revisione 115:** sito tradotto in tutte le 11 lingue; feste stagionali (Natale, Hanukkah, Capodanno lunare, Ramadan, Eid, Vesak, Diwali) con link a Wikipedia.
- **15/11/2026, revisione 114:** nuovo motore delle traduzioni, tutto il sito in inglese e francese; FAQ: riscritte «collaborazioni» e «paesi vuoti», tolte quattro domande (BIM & AI, BIM Accademia, eventi, video); la guida ha un passo per ogni scheda in alto (`nav:#…` in `STEPS`).
- **Post LinkedIn:** testo preparato il 15/11/2026; consigliato martedì 17/11 alle 8:00–8:30. Marco vuole tutto pronto per martedì (traduzioni, ricerca a tappeto, appunti).
- **«Ispirazioni»:** Marco ha mandato l'elenco dei suoi canali YouTube (screenshot, 34 canali): da verificare uno per uno e trasformare in un articolo nel curatore.
- **15/11/2026:** il sito passa all'organizzazione «bimnews» e all'indirizzo https://bimnews.github.io/; aggiornati README, CLAUDE.md, i percorsi negli script di `strumenti/` e i testi dei due task. Niente pagina di rinvio dal vecchio indirizzo: Marco non la vuole, perché il sito l'hanno visto ancora in pochi. Prossimo passo: Marco fa un controllo finale, dice che cosa aggiungere, poi diffonde il sito.
