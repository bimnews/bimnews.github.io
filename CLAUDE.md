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

1. **Globo 3D: anteprima fatta e inviata il 15/11/2026, si aspetta il sì di Marco. Non pubblicare prima.**
   - **Dove sta il codice:** `strumenti/globo/anteprima/`, con `globo.js`, `mondo.json` (world-atlas 110m con i nomi italiani nella proprietà `it`), `citta.json` (5479 città di Natural Earth, terne lon, lat, luminosità 0–9), le librerie d3-array, d3-geo e topojson-client, e `LICENZE.txt`. Le modifiche a `index.html` sono in `integrazione-index.patch`: CSS `.globe`, `loadGlobe()` chiamata dopo `loadMap()` e i crediti nel figcaption.
   - **Per pubblicare:**
     - spostare i file in `assets/globo/`;
     - applicare la patch, a mano se il contesto è cambiato;
     - aumentare la revisione.
   - **Cosa fa:**
     - canvas ortografico sopra `.map-wrap` solo in home e nella versione completa, con sfondo di stelle, alone e galleggiamento;
     - rotazione lenta, trascinabile con il mouse;
     - asse inclinato di 23,44°;
     - giorno e notte reali calcolati dalla data e dall'ora (declinazione ed equazione del tempo), con il crepuscolo;
     - luci delle città nella parte in ombra;
     - un punto blu sui paesi con notizie.
   - **Orientamento iniziale:** sul continente di chi guarda, dedotto dal fuso orario del browser (nessuna geolocalizzazione); il paese di chi guarda resta un po' sotto il centro, per non finire sotto la barra di ricerca.
   - **Clic su un paese:** lancia due clic su `#ctrs .ctry` come la ricerca; un MutationObserver su `#map-where` fa volare il globo sul paese, con zoom fino a vederlo intero (parte principale, senza territori lontani), poi lo dissolve sulla mappa piatta. Con «← Mondo» il globo torna.
   - **Già pubblicato da questa anteprima:** `.fc-search` ha `pointer-events:none` (solo box e lista restano cliccabili), perché il blocco «Dove andiamo oggi?» copriva i clic sulla mappa.
   - **Abbinamenti corretti:** Figi, Russia e Francia; Stati Uniti e Norvegia erano già giusti.
   - **Scelta da confermare con Marco:** la rotazione è continua, partendo dal suo continente; in alternativa si può fare un'oscillazione attorno al suo continente.
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
3. **Pulsanti 3D «a LED incassati»** (richiesta del 15/11/2026: anche le scritte dei pulsanti devono accendersi come LED al passaggio del cursore e al clic): pulsanti in rilievo con un LED luminoso, eleganti. Fare un'anteprima.
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
6. **Tai Chi e Kung Fu (nuova scheda in «Fuori dallo studio», `#fuori`).**
   - **Cosa vuole Marco:**
     - le immagini dell'artefatto sul Tai Chi con le 5 virtù del Kung Fu, creato in un'altra conversazione;
     - la descrizione delle 5 virtù secondo il sito che aveva dato in quella conversazione;
     - perché per lui è diventata una cosa importante.
   - **Bloccato:** l'artefatto non compare nell'elenco degli artefatti di Marco e il sito non lo conosciamo. Bisogna chiedergli il link dell'artefatto (o le immagini) e l'indirizzo del sito.

7. **Statistiche delle visite dentro il sito (domanda di Marco del 15/11/2026, in attesa della sua scelta).**
   - Il sito usa già GoatCounter (`mscigliuolo.goatcounter.com`).
   - **Strada proposta:** contatore con `goatcounter.visit_count` o con `/counter/TOTAL.json`.
   - **Prima serve un'azione di Marco:** attivare in GoatCounter «Allow adding visitor counts on your website». Oggi l'endpoint risponde 403.
   - **Alternativa:** dashboard pubblica incorporata in un frame. GoatCounter ha una pagina di aiuto apposita, da verificare.

8. **Timeline doppia «Il BIM nel tempo: il mondo e l'Italia» (anteprima del 15/11/2026, non pubblicare prima del sì).**
   - **Cosa è:** due linee sullo stesso asse dal 1975 a oggi, il mondo sopra e l'Italia sotto. I collegamenti gialli uniscono una norma italiana a quella internazionale che recepisce; quelli tratteggiati uniscono BS 1192 e PAS 1192-2 alla ISO 19650. Ci sono i filtri Entrambe, Solo mondo e Solo Italia e un dettaglio con le fonti.
   - **Dove andrà:** in BIM in 5 minuti, dopo la lisca delle norme (id `b5-t2`).
   - **Il codice:** `strumenti/timeline/tl2.py`, da lanciare sulla `index.html` di main dopo aver corretto i percorsi. Inserisce HTML, CSS e JS e la voce dell'indice. Ritocchi già fatti a mano dopo lo script: corsia con `LW`/`LI` a ±40 px dall'asse, etichette Mondo/Italia in `.t2-box` fuori dallo scorrimento, `.t2-box{min-width:0}`.
   - **Dati:** la linea italiana è `UNI 11337:2009` + l'array `NORME`. La linea del mondo ha 18 tappe, tutte verificate: Eastman 1975 (AIA Journal), van Nederveen e Tolman 1992, IAI 1995, IFC 1.0 1996, buildingSMART 2005, ISO/PAS 16739:2005, BS 1192:2007, ISO 29481-1:2010, Government Construction Strategy 31/05/2011, ISO 16739:2013, PAS 1192-2:2013, Dir. 2014/24/UE art. 22 par. 4, EU BIM Handbook 06/07/2017, ISO 19650-1/2 07/12/2018, ISO 19650-3/-5 2020, -4 2022, 16739-1 e 7817-1 2024, 19650-6 2025.
9. **Selettore delle lingue in alto (richiesta del 15/11/2026).**
   - **Lingue:** quelle della proposta multilingue (it, en, de, fr, es, zh, ja) più l'**arabo standard** (fuṣḥā), con `dir="rtl"`.
   - **Scopo:** Marco vuole controllare che le scritte principali del sito siano tradotte.
   - Fa parte del punto 4.

## Fatto di recente

- **15/11/2026, revisione 100:**
  - **BIM in 5 minuti:** sezione «09 · Le certificazioni nel mondo» (`#b5-cert`) con 6 schede verificate: Hong Kong (obbligatoria, DEVB TC(W) 2/2021), Italia (volontaria, All. I.9 art. 1 c. 3 D.Lgs. 36/2023, UNI 11337-7, UNI/PdR 78:2020), Spagna (Plan BIM 2023), Regno Unito (BRE e UKAS, ISO 19650-2), Germania (VDI/bS 2552 Blatt 8.1), buildingSMART. Altri paesi da aggiungere con la ricerca a tappeto: Cina, Corea, Singapore, Francia, paesi nordici…
  - **Scautismo** (`#fuori-scout`): testo di Marco (dall'AGESCI al CNGEI, scout laici, a Bolzano) e citazione di Baden-Powell da *Aids to Scoutmastership*, ed. 1930, «The Aim of Scouting», tradotta da noi. Marco aveva scritto «CNGI»: il nome corretto è CNGEI. Niente articoli: solo questa descrizione.
- **15/11/2026, revisione 101:**
  - **FAQ:** la policy di Marco. Niente collaborazioni economiche né esterne sul sito (gestito con il suo piano Pro di Claude); sì a sponsorizzazioni per passare a un piano con più token, «parliamone». Aggiornato anche `strumenti/faq.py`.
  - **BIM News:** il riquadro «Tutte le notizie» è su una colonna da bordo a bordo; criterio, scelta delle notizie, fonti e lingue sono in un `<details class="ai-more">` richiudibile.
  - **BIM News:** il disclaimer «Che cos'è BIM News, e che cosa non è» (`.bn-what`), sempre aperto, da non chiudere mai: è una richiesta esplicita di Marco.
