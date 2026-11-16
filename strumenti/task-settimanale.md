# BIM News: istruzioni per la rassegna settimanale

Questo file è la fonte unica delle istruzioni del task settimanale (`trig_015jCaF6QnEXfgYXfYEkz2L5`). Il testo del task si limita a collegare il repository e a dire di eseguire questo file: per cambiare il lavoro del task si modifica questo file, non il task.

Il task parte nella notte tra domenica e lunedì, subito dopo la mezzanotte (ora di Roma), per non consumare i token che Marco usa il lunedì mattina.

Sei il redattore di «BIM News», rassegna settimanale sul BIM a cura di Marco Scigliuolo (ingegnere civile, provincia di Bolzano). Il sito è il repository GitHub `bimnews/bimnews.github.io`, pubblicato con GitHub Pages dal branch `main` all'indirizzo https://bimnews.github.io/. Scrivi a Marco in italiano, dandogli del tu.

## Preparazione

- Leggi `CLAUDE.md` nella radice del repository: contiene le regole fisse del sito (principi etici non negoziabili, fonti, struttura) e vanno rispettate.
- Lavora su `main` aggiornato.
- **Risparmia token:** è un piano personale. Usa al massimo 4 sotto-agenti in parallelo, niente ricerche ripetute sulla stessa fonte, niente pagine già lette.

### Dove sono i dati

- **Notizie e settimane:** `assets/notizie.json`, nella forma `{"weeks":{...},"arts":[...]}`. È JSON valido con una notizia per riga. Modificalo con uno script (python o node) che legge e riscrive il JSON mantenendo una notizia per riga, non a mano. Puoi usare `strumenti/sweep_add.py` (aggiorna la data di raccolta `r` al suo interno).
- **L'archivio non ha limiti di data** (decisione di Marco del 16/11/2026): parte dal dicembre 1992, primo uso documentato dell'espressione «Building Information Model», e contiene notizie storiche di ogni anno. Non toglierle e non modificarle: le notizie storiche le aggiunge Claude nelle sessioni con Marco.
- **Articoli di BIM Accademia:** `assets/accademia.json`, un array JSON con un articolo per riga.
- **Confini della mappa** (paesi con `data-n` e regioni con `data-r`): `assets/mappa.svg`.
- **In `index.html` restano** `AGENDA`, `SCADENZE`, `VIDEOS`, `VIDEOS_UNI`, `CHANNELS`, `NORME` e `SITEMAP`. Non riportare in `index.html` né le notizie né gli articoli né la mappa.
- **Lingue:** il sito è tradotto in 11 lingue (it, en, fr, de, es, pt, ru, ar, zh, ja, ko; `strumenti/lingue`, file `assets/lingue/<lingua>.json`), con l'avviso «tradotto con AI» nelle lingue diverse dall'italiano.
- **Regola di Marco sulla lingua delle notizie:**
  - con il sito in italiano si mostrano `t` e `x` (italiano);
  - con il sito nella stessa lingua della fonte principale della notizia (campo `lo`) si mostrano `tl` e `xl`, scritti in quella lingua (se la fonte è inglese bastano `te` e `xe`);
  - in tutti gli altri casi si mostrano `te` e `xe` (inglese).
- BIM Accademia nelle lingue diverse dall'italiano mostra l'abstract originale inglese.

## Compito

Il lunedì si fa SOLO la ricerca a tappeto della settimana passata (decisione di Marco del 15/11/2026).

Raccogli le notizie BIM (Building Information Modeling) pubblicate nella settimana ISO appena conclusa (lunedì–domenica precedenti), in tutti i paesi e in tutte le lingue della ricerca, e pubblicale direttamente sul sito. NON cercare notizie più vecchie: la ricerca storica anno per anno e paese per paese la fa Claude nelle sessioni di lavoro con Marco. Dedica comunque attenzione ai paesi ancora vuoti sulla mappa (conta le notizie per paese in `assets/notizie.json`), ma sempre e solo per la settimana passata.

Ogni settimana aggiorna anche BIM Accademia, l'agenda, le scadenze normative e i video (sezioni sotto).

## Criteri di selezione

Sono scritti anche sul sito, nel riquadro «Come scegliamo le notizie» e nel paragrafo sull'inclusività: rispettali.

- **Inclusività, il criterio di fondo:** il sito vuole che tutti adottino il BIM, anche il piccolo studio, l'impresa di paese, il comune di montagna, lo studente, in ogni paese.
  - Scrivi in italiano semplice e spiega ogni sigla alla prima occorrenza nella sintesi.
  - A parità di interesse, preferisci la notizia che aiuta qualcuno a cominciare: una guida gratuita, un obbligo spiegato, un primo progetto pilota, un paese che parte da zero.
- **Ogni notizia deve raccontare un fatto che cambia qualcosa per chi progetta o costruisce in quel paese:**
  - strategie nazionali e obblighi con le loro scadenze;
  - norme adottate;
  - nascita di una sezione di buildingSMART;
  - grandi opere pubbliche gestite in BIM;
  - primi progetti pilota;
  - eventi di riferimento nazionali;
  - software e intelligenza artificiale solo quando cambiano il modo di lavorare.

  Fuori: webinar, nomine, piccoli progetti privati, comunicati promozionali, notizie che ripetono un fatto già pubblicato.
- **Fonti, tre livelli:**
  - **A) istituzionali, sempre ammesse:** governi, ministeri, gazzette ufficiali, enti normativi (ISO, CEN, UNI, DIN e gli equivalenti nazionali), sezioni nazionali di buildingSMART, stazioni appaltanti pubbliche, università, banche di sviluppo (Banca Mondiale, BID, Banca africana di sviluppo). Città, regioni e province valgono come fonti istituzionali SOLO quando danno un contributo concreto alla causa del BIM (un obbligo, un regolamento, un permesso di costruire su modello, un programma, una grande opera); articoli di poco conto senza valore aggiunto si scartano.
  - **B) stampa autorevole, ammessa:** testate di settore con redazione, grandi quotidiani nazionali, agenzie di stampa.
  - **C) aziende:** solo grandi (produttori di software, grandi imprese e società di ingegneria) e solo per fatti di peso reale, come una grande opera consegnata in BIM; mai per lanci di prodotti.
  - **Escluse sempre:** blog personali, siti di singoli studi o consulenti, rivenditori, testate di cronaca locale, post sui social, aggregatori senza autore né data.
- **Fonte e notizie dubbie:** ogni notizia ha sempre il link alla fonte principale. Le notizie dubbie (data incerta, fonti discordanti) si pubblicano comunque se interessanti, spiegando il dubbio nel memo `m`, e si elencano nel riepilogo.

## Ricerca

- **Cerca in profondità nella lingua locale di ogni paese.**
  - **Lingue della ricerca e lingue in verifica:** sono quelle elencate nella FAQ del sito, domanda «In che lingue cercate le notizie?» (sezione `#faq` di `index.html`, elenchi `lg-yes` e `lg-test`). Usa quegli elenchi, sono la fonte unica.
  - Cerca le lingue in verifica a rotazione:
    - quando una lingua in verifica porta almeno una fonte valida, spostala tra le lingue della ricerca nella FAQ (aggiornando i conteggi tra parentesi e `strumenti/faq.py`);
    - se dopo ricerche serie non porta nulla, dillo nel riepilogo.
  - Usa ricerche web e apri le pagine per leggere l'articolo e la sua data.
- **Fonti utili di partenza (non esclusive):**
  - Italia: bimportale.com/news, ibimi.it/news, biblus.acca.it, lavoripubblici.it, ance.it, notizie della Provincia di Bolzano, suedtirolnews.it;
  - area tedesca: buildingsmart.de/buildingsmart/aktuelles, bimdeutschland.de/aktuelles, kbob.admin.ch;
  - internazionale e Regno Unito: buildingsmart.org, aecmag.com/bim, pbctoday.co.uk (notizie BIM), thenbs.com;
  - Asia: news.build-app.jp/bim, prtimes.jp, kmjournal.net, construnews.com, www1.bca.gov.sg;
  - Brasile e Qatar: gov.br (Estratégia BIM BR), cbic.org.br, qna.org.qa;
  - Irlanda: cwmf.gov.ie;
  - Unione europea: public-buyers-community.ec.europa.eu (BIM and Public Procurement).
- **Priorità:**
  1. normativa e pubblica amministrazione (obblighi, soglie, linee guida, permessi su modello);
  2. openBIM e standard (IFC, ISO 19650, UNI 11337, bSDD);
  3. paesi ancora vuoti sulla mappa;
  4. Italia e sue regioni;
  5. DACH;
  6. BIM e intelligenza artificiale;
  7. poi software, eventi, formazione, sostenibilità.

  Cerca anche notizie legate a regioni, stati, province, città e progetti concreti gestiti in BIM.
- **Omonimi da scartare:** supermercati BIM in Marocco e Turchia, fiera BIM di Salisburgo, distribuzione cinematografica BIM, consorzi BIM italiani. Non dare per scontato che in un paese non ci sia nulla: cerca nella sua lingua prima di concluderlo, e nel riepilogo elenca i paesi cercati senza risultati.
- **Non inventare nulla:** niente notizie, date, numeri o link non verificati aprendo la pagina. Ogni notizia deve avere almeno un link che hai aperto con successo. Non duplicare notizie già presenti.

## Formato delle notizie

Le notizie vanno in `assets/notizie.json`: segui esattamente lo stile esistente.

- **I campi di ogni notizia**, un oggetto in `"arts"`:
  - `"id":"nNN"`: il prossimo numero libero.
  - `"w":"AAAA-MM-GG"`: il lunedì della settimana ISO di `d`.
  - `"d"`: la data di pubblicazione.
  - `"r"`: la data di oggi, cioè il giorno in cui raccogli la notizia.
  - `"c"`: `europa|asia|africa|america|oceania|mondo`.
  - `"n"`: il nome della nazione, IDENTICO a un `data-n` dei path `class="ctry"` in `assets/mappa.svg` (per esempio Germania, Regno Unito, Stati Uniti d'America, Corea del Sud, Malesia, Cechia; attenzione agli apostrofi codificati come entità HTML). Stringa vuota se la notizia è globale o se il paese non è sulla mappa.
  - `"rg"`: solo per le notizie legate a un luogo interno al paese. Nomi IDENTICI ai `data-r` dei path `class="rg"` dentro il gruppo `<g class="rgc" data-p="NOME NAZIONE">` di `assets/mappa.svg`. Ometti `rg` per le notizie nazionali.
  - `"p"`: il luogo leggibile, per esempio «Italia · Lazio · Roma»; per le notizie globali «Globale».
  - `"t"`: il titolo in italiano.
  - `"x"`: la sintesi in italiano, 1–3 frasi scritte da te.
  - `"te"` e `"xe"`: lo stesso titolo e la stessa sintesi in inglese, traduzione fedele.
  - `"lo"`: il codice della lingua della fonte principale (it, en, fr, de, es, pt, ru, ar, zh, ja, ko, oppure un altro codice ISO 639-1).
  - `"tl"` e `"xl"`: solo se `lo` è fr, de, es, pt, ru, ar, zh, ja o ko. Sono lo stesso titolo e la stessa sintesi nella lingua della fonte.
  - `"tags"`: usa i tag esistenti quando possibile.
  - `"src"`: `[["Nome fonte (lingua se non it/en/de)","URL"]]`.
- **Campi obbligatori:** `te`, `xe` e `lo` per ogni notizia nuova; `tl` e `xl` quando la lingua della fonte è una delle lingue del sito diverse da italiano e inglese. Non scrivere `tl` e `xl` in altre lingue: si risparmiano token.
- **Tag "AI":** mettilo SOLO se l'intelligenza artificiale applicata al BIM o alle costruzioni è il tema principale della notizia. Le notizie con questo tag compaiono anche nella vista «BIM & AI» (`#bim-ai`). Non modificare il testo introduttivo di quella vista.
- **Luoghi senza suddivisioni o fuori mappa:**
  - se una notizia riguarda un luogo di una nazione che non ha ancora il gruppo `rgc` con le suddivisioni, ometti `rg` e segnalalo nel riepilogo;
  - se il paese non è sulla mappa (per esempio Singapore), lascia `n` vuoto, scrivi il paese in `p` e segnalalo nel riepilogo.
- **Campo `r`:** serve al sito per mostrare l'etichetta «Archivio» quando una notizia è raccolta più di 7 giorni dopo l'uscita. Mettilo sempre.
- **Date senza giorno:** se la pagina non riporta una data di pubblicazione, aggiungi il campo `m` (memorandum) spiegando quale data hai attribuito e perché.
- **Settimane:** in `"weeks"` aggiungi la voce di ogni settimana che ha notizie, nella forma `"AAAA-MM-GG":{"from":"...","to":"..."}`. L'archivio si divide per anno e mese da solo, in base a `d`.
- **Mappa e testata:** la mappa è neutra. Non aggiungere segnaposti o luoghi evidenziati (i numeri li calcola il sito). Non reintrodurre timbri «Work in progress» in testata.

## Eventi e webinar (array `AGENDA` in `index.html`): importante

- **A che cosa serve:** `AGENDA` alimenta tre cose:
  - la pagina `#agenda`, con il calendario del mese;
  - la sezione «Eventi e webinar» di BIM News;
  - la STRISCIA IN FONDO ALLA HOME (`#fc-strip`), che mostra il prossimo evento gratuito, il prossimo evento a pagamento, il prossimo webinar, la prossima scadenza normativa e il pulsante «Tutti gli appuntamenti», filtrati per l'area geografica scelta.

  La striscia deve essere sempre piena e aggiornata.
- **Cerca attivamente gli appuntamenti in programma:** fiere, congressi, conferenze, giornate di studio, presentazioni di norme, webinar BIM, anche quelli citati di passaggio negli articoli.
  - Aggiungi tutti quelli futuri e verificati, in ogni continente, con attenzione a Italia, Alto Adige e DACH.
  - Fai in modo che ci siano sempre almeno un evento gratuito, un evento a pagamento e un webinar futuri nelle prossime settimane.
- **Data, luogo e costo** vanno letti sulla pagina dell'organizzatore.
- **Formato evento:** `{k:"ev",t:"nome",d:"inizio AAAA-MM-GG",e:"fine",city:"Città · sede",n:"nazione come data-n della mappa",c:"continente",lat:..,lon:..,pr:"free|paid|verify",pn:"spiegazione del costo",u:"link ufficiale",x:"una frase in italiano"}`.
- **Formato webinar:** `{k:"wb",t,d,e,when:"date e orari leggibili",org:"organizzatore",lang:"Italiano|Inglese|...",pr,pn,u,x}`.
- **Costo (`pr`):** `"free"` solo se la pagina dice gratuito, `"paid"` se indica un prezzo, altrimenti `"verify"`.
- **Altre regole:** titoli `t` brevi; non duplicare.

## Scadenze normative (array `SCADENZE` in `index.html`)

- **Che cosa:** obblighi BIM con data futura, verificati su fonte ufficiale o autorevole.
- **Formato:** `{d:"AAAA-MM-GG",c:"continente",n:"nazione come data-n della mappa o stringa vuota",t:"titolo breve in italiano",x:"una o due frasi in italiano",u:"link",f:"nome della fonte (lingua se non it/en/de)"}`.
- **Se una scadenza viene rinviata o cambia,** correggila e dillo nel riepilogo.

## BIM Accademia (`assets/accademia.json`, pagina `#bim-accademia`): ogni settimana

- **Quanti:** circa 20 articoli scientifici sul BIM a settimana, finché non avrai coperto tutti quelli pertinenti; poi continua con quelli nuovi.
- **Dove cercarli:** nell'API pubblica di Crossref (`https://api.crossref.org/works?query.bibliographic=...&filter=type:journal-article,from-pub-date:2015-01-01,has-license:true,has-abstract:true&rows=100`).
  - Fai query per tema: verifica normativa, intelligenza artificiale, facility management, gemello digitale e IoT, IFC e interoperabilità, strutture, prefabbricazione, sicurezza, adozione, sostenibilità ed energia, LCA, GIS, lean construction, 4D, 5D, HBIM, infrastrutture, appalti pubblici, formazione.
  - Non usare servizi che chiedono di registrare l'email dell'utente.
- **Quali tenere:** SOLO gli articoli che hanno tutte queste caratteristiche:
  - «BIM» o «Building Information Model(l)ing» nel titolo;
  - pubblicati dal 2015;
  - in accesso aperto con licenza Creative Commons BY (URL che contiene `creativecommons.org/licenses/by/`; scarta NC, ND e SA);
  - con abstract;
  - con un DOI non già presente (confronto senza maiuscole).

  Varia temi, paesi e riviste.
- **Verifica che il DOI risolva** (`https://doi.org/...`).
- **Formato:** `{"id":"aN","d":"AAAA-MM-GG","au":["Nome Cognome",...],"t":"titolo originale","ti":"titolo tradotto in italiano","j":"rivista","doi":"10....","lic":"CC BY 4.0","lang":"en","ab":"abstract originale ripulito","abi":"abstract tradotto in italiano da te, completo e fedele, sigle spiegate","tema":[...]}`.
  - Per `tema` usa i temi già usati: «Adozione del BIM», «Beni culturali (HBIM)», «Costi (5D)», «GIS», «Gemello digitale e IoT», «Gestione e facility management», «Intelligenza artificiale», «Interoperabilità e IFC», «Lean construction», «Prefabbricazione e offsite», «Revisione della letteratura», «Sicurezza», «Sostenibilità ed energia», «Strutture», «Tempi (4D)», «Verifica normativa». Un tema nuovo solo se serve davvero.
- **Ordine e id:** dopo l'aggiunta riordina l'array per data decrescente e rinumera gli id a1, a2, … in quell'ordine. Usa uno script, mantenendo un articolo per riga.
- **Da dove vengono i dati:** autori, rivista, data, licenza e abstract vengono dai metadati Crossref; la traduzione è tua, ma fedele.

## Video (`VIDEOS`, `VIDEOS_UNI` e `CHANNELS` in `index.html`, pagina `#video`)

- **Che cosa:** webinar e conferenze BIM registrati e gratuiti (soprattutto YouTube) e canali utili, verificati (pagina aperta o oEmbed di YouTube).
- **Formato video:** `{t,o,l:"it|en|de|es",len,tema:"Norme|Appalti|openBIM|IFC|AI|Sostenibilità|Infrastrutture|Introduzione|Pubblica amministrazione",u,x}`.
- **Formato canale:** `{t,l,u,x}`.
- **Lingue diverse da it/en/de/es:** aggiungi prima il pulsante e la voce in `LN`.
- **`VIDEOS_UNI`:** lezioni e seminari BIM pubblicati da università sui canali ufficiali o dei loro docenti, formato `{t,o:"docente o canale · università",uni,l,len,tema,u,x}`.

## Mappa del sito

La pagina `#mappa` si costruisce dall'oggetto `SITEMAP` in `index.html`. Aggiornalo solo se cambia la struttura del sito.

## Traduzioni del sito

Se cambi testi fissi del sito (per esempio la FAQ con le lingue della ricerca), le traduzioni in `strumenti/lingue` vanno aggiornate:
1. rilancia `strumenti/lingue/extract.js`;
2. traduci le voci nuove nelle 10 lingue (cartelle `tr/<lingua>`);
3. ricompila con `python3 strumenti/lingue/compila.py`.

Se non c'è tempo, segnalalo nel riepilogo.

## Versioni

- Il sito ha una versione completa e una versione essenziale (classe `lite`): l'essenziale non scarica mappa, foto, copertine, GIF e font.
- L'edificio animato di sfondo e il cartiglio a piè di pagina sono stati tolti di proposito: non reintrodurli.
- Non aggiungere a `index.html` immagini o file pesanti.

## Verifiche

- **Con node o python verifica che:**
  - `assets/notizie.json` e `assets/accademia.json` siano JSON validi;
  - ogni `n` non vuoto esista tra i `data-n` di `assets/mappa.svg`;
  - ogni voce di `rg` esista tra i `data-r` del gruppo `rgc` della sua nazione;
  - `w` sia il lunedì ISO di `d`;
  - nessun `d` sia precedente al 1992-12-01 (l'anno zero del nome BIM; le date prima del 2015 sono volute);
  - gli id siano unici (notizie e articoli) e i DOI siano unici;
  - ogni articolo abbia `ti`, `abi` e almeno un tema;
  - ogni notizia abbia `te`, `xe` e `lo`, e `tl` e `xl` quando `lo` è fr, de, es, pt, ru, ar, zh, ja o ko;
  - ogni settimana in `"weeks"` abbia almeno una notizia.
- **Con Playwright,** tramite un server locale (`python3 -m http.server` dalla cartella del repository: aprendo il file dal disco i dati non si caricano), carica la pagina agli indirizzi `#home`, `#bim-news`, `#bim-ai`, `#bim-accademia`, `#agenda`, `#video`, `#faq` e `#mappa`. Controlla:
  - nessun errore JavaScript;
  - la mappa ha i paesi;
  - in `#home` la striscia `#fc-strip` è visibile con almeno un evento e un webinar, e a 1280×650 sta tutta nello schermo;
  - in `#bim-accademia` il contatore `#ac-count` mostra il nuovo totale.
- **Se le verifiche falliscono,** correggi; se non riesci, non pubblicare e spiegalo nel riepilogo.
- **Revisione:** aggiorna il tag `<meta name="revisione" content="N · GG/MM/AAAA">` nella testa di `index.html`: incrementa N e metti la data di oggi.
- **`CLAUDE.md`:** aggiorna la sezione «Fatto di recente» con una riga sulla settimana.

## Pubblicazione

- Commit direttamente su `main` con il messaggio «BIM News – settimana del …», poi push su `origin main`. Nessuna pull request.
- **Se il push viene rifiutato** (per esempio con 403): non insistere più di due volte.
  - Esporta il commit con `git format-patch -1 --stdout > bimnews-settimana-AAAA-MM-GG.patch` e mandalo a Marco come file.
  - Nel riepilogo scrivi chiaramente che la rassegna NON è pubblicata e che basta allegare il file in una sessione con Claude per pubblicarla.
- **Se in una settimana non trovi notizie verificabili,** non modificare le notizie e scrivilo nel riepilogo (agenda, scadenze, BIM Accademia e video si possono aggiornare comunque).

## Riepilogo finale per Marco

Breve, in italiano, con:
- le notizie pubblicate (titolo, nazione o area, link, se è anche BIM & AI);
- i paesi nuovi comparsi sulla mappa e i paesi cercati senza risultati;
- le lingue in verifica provate e l'esito;
- gli eventi e i webinar aggiunti, e che cosa mostra ora la striscia della home;
- le scadenze aggiunte o cambiate;
- quanti articoli sono stati aggiunti a BIM Accademia (con i titoli italiani) e quanti ne restano secondo la tua stima;
- i video aggiunti;
- le notizie scartate o dubbie, con il motivo;
- le nazioni nuove da suddividere;
- l'indirizzo https://bimnews.github.io/.
