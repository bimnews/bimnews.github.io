# BIM News: istruzioni per Claude

Sito di Marco Scigliuolo (ingegnere civile, provincia di Bolzano), pubblicato con GitHub Pages dal branch `main` su https://mscigliuolo.github.io/. Rassegna mondiale sul BIM, in italiano, con la fonte di ogni notizia.

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
- **Revisione:** `<meta name="revisione" content="N · GG/MM/AAAA">`. Il cartiglio a piè di pagina è stato tolto di proposito.
- **Due versioni:**
  - **completa:** foto, mappa, nuvola di punti, copertine e GIF;
  - **essenziale:** classe `lite` su `<html>`; non scarica foto, mappa, font, copertine né GIF.
- **Veste grafica C, «Cantiere di notte»:**
  - tema scuro predefinito, con chiave `tema-2026` in localStorage;
  - un colore per ogni scheda (`--k-news`, `--k-ai`, `--k-acc`, `--k-b5`, `--k-vid`, `--k-cur`, `--k-ag`, `--k-pf`, `--k-faq`).
- **Home versione B:** titolo, mappa a tutta larghezza con la ricerca «Dove andiamo oggi?» (`#fc-search`) e la striscia degli eventi `#fc-strip`. La striscia deve restare intera nello schermo da 1280×650 in su: controlla con `strumenti/fit.js`.
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

1. **Globo 3D (anteprima richiesta, non pubblicare prima del sì).**
   - **Cosa vuole Marco:**
     - nella home, al posto della mappa piatta, un globo stilizzato che galleggia e ruota, su uno sfondo di stelle;
     - quando si sceglie un paese, uno zoom dinamico fino a vederlo intero.
   - **Piano:**
     - d3-geo con proiezione ortografica su canvas, confini `world-atlas@2.0.2/countries-110m.json` (licenza ISC; d3-geo ISC; topojson-client);
     - salvare le librerie in `assets/` e caricarle solo nella versione completa;
     - fermare la rotazione con `prefers-reduced-motion`.
   - **Abbinamento ai nomi italiani della mappa:** è in `strumenti/globo/abbinamenti.json`, calcolato da `strumenti/globo/match.js`. Da correggere a mano: Figi, Stati Uniti, Russia, Norvegia e Francia, abbinati male per isole e territori lontani.
   - **Collegamento con la mappa attuale:** il clic sul globo può lanciare il clic sul paese corrispondente in `#ctrs` (come fa la ricerca), così filtri, numeri e regioni restano quelli della mappa piatta. Dopo lo zoom si può passare alla mappa piatta per vedere le regioni.
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
3. **Pulsanti 3D «a LED incassati»:** pulsanti in rilievo con un LED luminoso, eleganti. Fare un'anteprima.
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
