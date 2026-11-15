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
- **I due task puntano a `bimnews/bimnews.github.io`** (testi aggiornati il 15/11/2026).
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
     - **Nuova scheda «Ispirazioni»:** i canali YouTube che segue Marco. Lo screenshot con i 34 canali non è più leggibile nella sessione: Marco deve rimandarlo.
     - **Portfolio:** la grafica è rimasta quella vecchia, va resa coerente con il resto della sezione. Poi le anteprime dei progetti affrontati, poi l'elenco dei modelli fatti con Guadagnuolo. Servono materiali da Marco.
     - Il manuale «Suoni per chitarra con il modeler» (man-pers-03) non è pubblicato: è la sintesi di una playlist di terzi, valutare con Marco.
   - **BIM in breve, agenda a calendario e giornate della tecnologia: PUBBLICATI in revisione 120** dopo il sì di Marco (15/11/2026).
     - **BIM in breve** (`#bim-5-minuti`): linea del tempo `.evo-tl` sopra i tre passi (1570, 1963, 1982, 1996, 2002, oggi; fonti Wikipedia in inglese), approfondimento `.evo-deep` su attributi e parametri (codice CAD/BIM, grafo delle dipendenze, IfcWall/IfcExtrudedAreaSolid/Pset_WallCommon/IfcRelVoidsElement), sezione `#b5-futuro` «10 · Cosa ci riserva il futuro?» (3 schede «sta già succedendo» legate alle notizie n10, n100, n36 e 3 «domande aperte»). I due blocchi di codice `.evo-code` restano in italiano in tutte le lingue.
     - **Agenda a calendario** `#agc` in `#agenda`, sopra le tre colonne: griglia del mese con scadenze, eventi (filtri area e costo), webinar e giornate della tecnologia (array `TECH`, `window.TECH_DAYS`, `techDate()` per il 4° giovedì di aprile e il 1° lunedì di ottobre). Clic su un giorno → elenco con i link. I nomi delle giornate e degli appuntamenti restano in italiano, come il resto dell'agenda.
     - **Date delle giornate verificate:** 11/2, 13/2, 4/3, 14/3, 12/4, 21/4, 4° giovedì di aprile (Girls in ICT, ITU), 26/4 (WIPO), 16/5 (luce, UNESCO), 17/5, 28/9, 1° lunedì di ottobre (Habitat), 14/10 (normazione ISO/IEC/ITU), 31/10, 10/11.
     - **Da fare se Marco lo chiede:** un'etichetta in home nel giorno stesso di una giornata della tecnologia (come `.fest-chip`).

## Fatto di recente

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
