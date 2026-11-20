# -*- coding: utf-8 -*-
"""Proposta 1 · Dizionario dei dati BIM pubblici (prototipo).

Genera, da questi dati:
  manuali/dati-pubblici/dizionario.json
  manuali/dati-pubblici/dizionario-dati-pubblici.xlsx
  manuali/dati-pubblici/IT-nucleo.ids        (requisiti controllabili, buildingSMART IDS 1.0)
  manuali/dati-pubblici/IT-BZ-estensione.ids

Controlla ogni mappatura IFC sullo schema IFC 4.3 ADD2 (IfcOpenShell 0.9):
entità, attributi, Pset e proprietà standard devono esistere.

Uso:  python3 strumenti/proposta/genera.py
Serve: ifcopenshell, ifctester (pip install ifcopenshell; pip install --no-deps ifctester; pip install xmlschema), openpyxl
"""
import json, os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
SITO = os.path.normpath(os.path.join(QUI, "..", ".."))
OUT = os.path.join(SITO, "manuali", "dati-pubblici")
VERSIONE = "0.1"
DATA = "2026-11-19"

# ---------------------------------------------------------------------------
# Livelli
LIVELLI = {
    "IT":    {"it": "Nucleo nazionale (proposta)", "de": "Nationaler Kern (Vorschlag)", "en": "National core (proposal)"},
    "IT-BZ": {"it": "Estensione Provincia di Bolzano (dal capitolato pubblico)", "de": "Erweiterung Provinz Bozen (aus den öffentlichen AIA)", "en": "Bolzano Province extension (from the public EIR)"},
}
GRUPPI = {
    "PRJ": "Progetto e territorio", "BLD": "Edificio", "STO": "Piani", "SPC": "Locali",
    "ELM": "Tutti gli elementi tecnici", "WIN": "Finestre",
}
FASI = {"PFTE": "Progetto di fattibilità tecnico-economica", "PE": "Progetto esecutivo",
        "AB": "Come costruito (as built)", "GES": "Gestione"}

# Mappatura IFC: tipo
#   pset  -> Pset_X.Prop (standard buildingSMART, controllato sullo schema)
#   qto   -> Qto_X.Q (standard)
#   attr  -> attributo dell'entità (controllato)
#   cpset -> property set nazionale (prefisso IT_, perché Pset_ è riservato a buildingSMART)
#   class -> IfcClassificationReference (IfcRelAssociatesClassification)
#   rel   -> relazione (nessun parametro da compilare)
#   mat   -> materiale (IfcRelAssociatesMaterial)
#   crs   -> IfcProjectedCRS.Name (georeferenziazione, IFC4+)

P = []
def par(**k):
    P.append(k)

# ---- Nucleo nazionale (proposta) -------------------------------------------
par(code="IT.PRJ.001", lv="IT", g="PRJ", it="Codice unico di progetto (CUP)", de="Projektcode (CUP)", en="Unique project code (CUP)",
    d="Il codice di 15 caratteri che lo Stato assegna a ogni progetto di investimento pubblico. Lega il modello ai dati economici e di monitoraggio già pubblici su OpenCUP.",
    t="IfcIdentifier", u="", v="15 caratteri alfanumerici", rx="[A-Z0-9]{15}", ex="(15 caratteri)", ent="IfcProject",
    m=("cpset", "IT_Progetto", "CUP"), f=["PFTE"], chi="Ente", src="L. 3/2003, art. 11 · opencup.gov.it", url="https://www.opencup.gov.it/portale/web/opencup/cos-%C3%A8-il-cup")
par(code="IT.PRJ.002", lv="IT", g="PRJ", it="Codice IPA dell'ente", de="IPA-Code der Körperschaft", en="Public body code (IPA)",
    d="Il codice che identifica l'ente proprietario nell'Indice dei domicili digitali delle pubbliche amministrazioni (IPA). Dice di chi è l'opera senza scrivere il nome a mano.",
    t="IfcIdentifier", u="", v="codice IPA esistente", rx="", ex="p_bz (Provincia autonoma di Bolzano)", ent="IfcProject",
    m=("cpset", "IT_Progetto", "CodiceIPA"), f=["PFTE"], chi="Ente", src="IndicePA, dataset «Enti», campo Codice_IPA", url="https://indicepa.gov.it/ipa-dati/dataset/enti")
par(code="IT.PRJ.003", lv="IT", g="PRJ", it="Comune (codice ISTAT)", de="Gemeinde (ISTAT-Kennziffer)", en="Municipality (ISTAT code)",
    d="Il codice ISTAT a 6 cifre del comune in cui si trova l'opera: le prime tre indicano la provincia. Esiste già, è pubblico e copre tutto il territorio.",
    t="IfcIdentifier", u="", v="6 cifre", rx="[0-9]{6}", ex="021008 (Bolzano)", ent="IfcSite",
    m=("cpset", "IT_Localizzazione", "ComuneISTAT"), f=["PFTE"], chi="Ente", src="ISTAT, codici statistici delle unità amministrative territoriali", url="https://www.istat.it/classificazione/codici-dei-comuni-delle-province-e-delle-regioni/")
par(code="IT.PRJ.004", lv="IT", g="PRJ", it="Data dell'elenco ISTAT usato", de="Stand des ISTAT-Verzeichnisses", en="ISTAT list date",
    d="I codici dei comuni cambiano (fusioni, nuove province): senza la data dell'elenco un codice di oggi può indicare un altro comune tra dieci anni.",
    t="IfcDate", u="", v="data AAAA-MM-GG", rx="", ex="2026-01-01", ent="IfcSite",
    m=("cpset", "IT_Localizzazione", "ElencoISTAT"), f=["PFTE"], chi="Ente", src="ISTAT (le variazioni sono pubblicate nella stessa pagina)", url="https://www.istat.it/classificazione/codici-dei-comuni-delle-province-e-delle-regioni/")
par(code="IT.PRJ.005", lv="IT", g="PRJ", it="Suddivisione ISO 3166-2", de="Gebietseinheit ISO 3166-2", en="ISO 3166-2 subdivision",
    d="Il codice internazionale della regione o provincia (IT-BZ, IT-25…). È lo stesso sistema in tutti i paesi: è il ponte tra un dizionario italiano e quelli degli altri paesi.",
    t="IfcIdentifier", u="", v="codice ISO 3166-2", rx="IT-[A-Z0-9]{2}", ex="IT-BZ", ent="IfcSite",
    m=("cpset", "IT_Localizzazione", "ISO3166_2"), f=["PFTE"], chi="Ente", src="ISO 3166-2:IT", url="https://www.iso.org/obp/ui/#iso:code:3166:IT")
par(code="IT.PRJ.006", lv="IT", g="PRJ", it="Sistema di riferimento (EPSG)", de="Koordinatenreferenzsystem (EPSG)", en="Coordinate reference system (EPSG)",
    d="Il sistema di coordinate in cui il modello è georeferenziato. In IFC 4 e 4.3 è il nome del sistema proiettato; in IFC 2x3 va nei Pset aggiuntivi (vedi l'articolo sulla georeferenziazione).",
    t="IfcLabel", u="", v="EPSG:nnnn", rx="EPSG:[0-9]{4,5}", ex="EPSG:25832", ent="IfcProjectedCRS",
    m=("crs", "IfcProjectedCRS", "Name"), f=["PFTE"], chi="Coordinatore BIM", src="ISO 16739-1:2024 (IfcProjectedCRS)", url="georeferenziazione-ifc.html")

par(code="IT.BLD.001", lv="IT", g="BLD", it="Codice dell'edificio nell'inventario", de="Gebäudekennung im Inventar", en="Building ID in the asset register",
    d="Il codice con cui l'ente conosce l'edificio nel suo inventario. Si usa la proprietà standard di IFC, non un parametro nuovo.",
    t="IfcIdentifier", u="", v="", rx="", ex="(codice dell'ente)", ent="IfcBuilding",
    m=("pset", "Pset_BuildingCommon", "BuildingID"), f=["PFTE"], chi="Ente", src="IFC 4.3, Pset_BuildingCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingCommon.htm")
par(code="IT.BLD.002", lv="IT", g="BLD", it="Anno di costruzione", de="Baujahr", en="Year of construction",
    d="Anno di costruzione dell'edificio esistente, o di fine lavori per un edificio nuovo.",
    t="IfcLabel", u="", v="AAAA", rx="[0-9]{4}", ex="1972", ent="IfcBuilding",
    m=("pset", "Pset_BuildingCommon", "YearOfConstruction"), f=["PFTE", "AB"], chi="Progettista", src="IFC 4.3, Pset_BuildingCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingCommon.htm")
par(code="IT.BLD.003", lv="IT", g="BLD", it="Bene tutelato", de="Denkmalgeschützt", en="Listed building",
    d="Vero se l'edificio è un bene culturale tutelato. Cambia chi deve approvare il progetto e come si interviene.",
    t="IfcLogical", u="", v="vero / falso / sconosciuto", rx="", ex="falso", ent="IfcBuilding",
    m=("pset", "Pset_BuildingCommon", "IsLandmarked"), f=["PFTE"], chi="Ente", src="IFC 4.3, Pset_BuildingCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingCommon.htm")
par(code="IT.BLD.004", lv="IT", g="BLD", it="Numero di piani", de="Anzahl der Geschosse", en="Number of storeys",
    d="Numero dei piani dell'edificio.",
    t="IfcCountMeasure", u="", v="intero", rx="", ex="4", ent="IfcBuilding",
    m=("pset", "Pset_BuildingCommon", "NumberOfStoreys"), f=["PFTE"], chi="Progettista", src="IFC 4.3, Pset_BuildingCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingCommon.htm")
par(code="IT.BLD.005", lv="IT", g="BLD", it="Destinazione d'uso dell'edificio", de="Nutzungsart des Gebäudes", en="Building occupancy type",
    d="La destinazione principale, scelta da un elenco nazionale unico (scuola, ufficio, ospedale…) invece che scritta a mano.",
    t="IfcLabel", u="", v="elenco nazionale", rx="", ex="Scuola", ent="IfcBuilding",
    m=("pset", "Pset_BuildingCommon", "OccupancyType"), f=["PFTE"], chi="Ente", src="IFC 4.3, Pset_BuildingCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingCommon.htm")

par(code="IT.STO.001", lv="IT", g="STO", it="Codice del piano", de="Geschosscode", en="Storey code",
    d="Il codice breve del piano, uguale in tutti i modelli del progetto (architettonico, strutture, impianti).",
    t="IfcIdentifier", u="", v="", rx="", ex="P01", ent="IfcBuildingStorey",
    m=("pset", "Pset_BuildingStoreyCommon", "Reference"), f=["PFTE"], chi="Coordinatore BIM", src="IFC 4.3, Pset_BuildingStoreyCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingStoreyCommon.htm")
par(code="IT.STO.002", lv="IT", g="STO", it="Fuori terra", de="Oberirdisch", en="Above ground",
    d="Vero se il piano è fuori terra, falso se è interrato.",
    t="IfcLogical", u="", v="vero / falso / sconosciuto", rx="", ex="vero", ent="IfcBuildingStorey",
    m=("pset", "Pset_BuildingStoreyCommon", "AboveGround"), f=["PFTE"], chi="Progettista", src="IFC 4.3, Pset_BuildingStoreyCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingStoreyCommon.htm")

par(code="IT.SPC.001", lv="IT", g="SPC", it="Codice del locale", de="Raumnummer", en="Space number",
    d="Il numero del locale. In IFC va nell'attributo Name del locale; il nome descrittivo va in LongName.",
    t="IfcLabel", u="", v="", rx="", ex="108", ent="IfcSpace",
    m=("attr", "IfcSpace", "Name"), f=["PFTE"], chi="Progettista", src="ISO 16739-1:2024 (IfcSpace)", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcSpace.htm")
par(code="IT.SPC.002", lv="IT", g="SPC", it="Nome del locale", de="Raumbezeichnung", en="Space name",
    d="Il nome per esteso del locale (Aula, Ufficio, Bagno accessibile…).",
    t="IfcLabel", u="", v="", rx="", ex="Aula", ent="IfcSpace",
    m=("attr", "IfcSpace", "LongName"), f=["PFTE"], chi="Progettista", src="ISO 16739-1:2024 (IfcSpace)", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcSpace.htm")
par(code="IT.SPC.003", lv="IT", g="SPC", it="Destinazione d'uso del locale", de="Nutzungsart des Raums", en="Space use",
    d="La destinazione del locale, presa da una classificazione unica e collegata come riferimento di classificazione, non scritta a mano.",
    t="IfcIdentifier", u="", v="classificazione nazionale", rx="", ex="(codice della classificazione)", ent="IfcSpace",
    m=("class", "IfcClassificationReference", "Identification"), f=["PFTE"], chi="Progettista", src="ISO 16739-1:2024 (IfcClassificationReference)", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcClassificationReference.htm")
par(code="IT.SPC.004", lv="IT", g="SPC", it="Superficie netta", de="Netto-Grundfläche", en="Net floor area",
    d="La superficie netta del pavimento, calcolata dal software come quantità, non scritta a mano.",
    t="IfcAreaMeasure", u="m²", v="", rx="", ex="52,40", ent="IfcSpace",
    m=("qto", "Qto_SpaceBaseQuantities", "NetFloorArea"), f=["PFTE", "PE", "AB"], chi="Progettista", src="IFC 4.3, Qto_SpaceBaseQuantities", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Qto_SpaceBaseQuantities.htm")
par(code="IT.SPC.005", lv="IT", g="SPC", it="Accessibile a persone con disabilità", de="Barrierefrei", en="Accessible",
    d="Vero se il locale è accessibile secondo le regole sull'abbattimento delle barriere architettoniche.",
    t="IfcBoolean", u="", v="vero / falso", rx="", ex="vero", ent="IfcSpace",
    m=("pset", "Pset_SpaceCommon", "HandicapAccessible"), f=["PE", "AB"], chi="Progettista", src="IFC 4.3, Pset_SpaceCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_SpaceCommon.htm")
par(code="IT.SPC.006", lv="IT", g="SPC", it="Aperto al pubblico", de="Öffentlich zugänglich", en="Publicly accessible",
    d="Vero se il locale è aperto al pubblico.",
    t="IfcBoolean", u="", v="vero / falso", rx="", ex="falso", ent="IfcSpace",
    m=("pset", "Pset_SpaceCommon", "PubliclyAccessible"), f=["PFTE"], chi="Ente", src="IFC 4.3, Pset_SpaceCommon", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_SpaceCommon.htm")

par(code="IT.ELM.001", lv="IT", g="ELM", it="Classificazione dell'elemento", de="Klassifikation des Bauteils", en="Element classification",
    d="Il codice dell'elemento in una classificazione nazionale unica, collegato come riferimento di classificazione. Le classificazioni regionali si agganciano a questa.",
    t="IfcIdentifier", u="", v="classificazione nazionale", rx="", ex="(codice della classificazione)", ent="IfcElement",
    m=("class", "IfcClassificationReference", "Identification"), f=["PFTE", "PE"], chi="Progettista", src="ISO 16739-1:2024 (IfcRelAssociatesClassification)", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelAssociatesClassification.htm")
par(code="IT.ELM.002", lv="IT", g="ELM", it="Locale di appartenenza", de="Zugehöriger Raum", en="Containing space",
    d="In IFC non serve un parametro: l'elemento è contenuto nel piano e riferito al locale con una relazione. Si chiede che la relazione ci sia, invece di ricopiare il codice del locale in ogni oggetto.",
    t="", u="", v="relazione", rx="", ex="—", ent="IfcElement",
    m=("rel", "IfcRelContainedInSpatialStructure", ""), f=["PE"], chi="Progettista", src="ISO 16739-1:2024 (IfcRelContainedInSpatialStructure)", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelContainedInSpatialStructure.htm")
par(code="IT.ELM.003", lv="IT", g="ELM", it="Codice del bene (asset)", de="Anlagenkennzeichen", en="Asset identifier",
    d="Il codice con cui l'elemento entra nel sistema di gestione e manutenzione dell'ente.",
    t="IfcLabel", u="", v="", rx="", ex="(codice dell'ente)", ent="IfcElement",
    m=("pset", "Pset_ConstructionOccurence", "AssetIdentifier"), f=["AB", "GES"], chi="Impresa", src="IFC 4.3, Pset_ConstructionOccurence", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ConstructionOccurence.htm")
par(code="IT.ELM.004", lv="IT", g="ELM", it="Produttore", de="Hersteller", en="Manufacturer",
    d="Il nome del produttore dell'elemento installato.",
    t="IfcLabel", u="", v="", rx="", ex="(produttore)", ent="IfcElement",
    m=("pset", "Pset_ManufacturerTypeInformation", "Manufacturer"), f=["AB"], chi="Impresa", src="IFC 4.3, Pset_ManufacturerTypeInformation", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ManufacturerTypeInformation.htm")
par(code="IT.ELM.005", lv="IT", g="ELM", it="Modello", de="Modellbezeichnung", en="Model label",
    d="Il nome commerciale del modello installato.",
    t="IfcLabel", u="", v="", rx="", ex="(modello)", ent="IfcElement",
    m=("pset", "Pset_ManufacturerTypeInformation", "ModelLabel"), f=["AB"], chi="Impresa", src="IFC 4.3, Pset_ManufacturerTypeInformation", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ManufacturerTypeInformation.htm")
par(code="IT.ELM.006", lv="IT", g="ELM", it="Numero di serie", de="Seriennummer", en="Serial number",
    d="Il numero di serie del singolo pezzo installato.",
    t="IfcIdentifier", u="", v="", rx="", ex="(numero di serie)", ent="IfcElement",
    m=("pset", "Pset_ManufacturerOccurrence", "SerialNumber"), f=["AB"], chi="Impresa", src="IFC 4.3, Pset_ManufacturerOccurrence", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ManufacturerOccurrence.htm")
par(code="IT.ELM.007", lv="IT", g="ELM", it="Data di installazione", de="Einbaudatum", en="Installation date",
    d="Il giorno in cui l'elemento è stato installato: da qui partono garanzia e manutenzione.",
    t="IfcDate", u="", v="data AAAA-MM-GG", rx="", ex="2027-05-14", ent="IfcElement",
    m=("pset", "Pset_ConstructionOccurence", "InstallationDate"), f=["AB"], chi="Impresa", src="IFC 4.3, Pset_ConstructionOccurence", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ConstructionOccurence.htm")
par(code="IT.ELM.008", lv="IT", g="ELM", it="Vita utile", de="Nutzungsdauer", en="Service life",
    d="La durata attesa dell'elemento, per programmare le sostituzioni.",
    t="IfcDuration", u="durata ISO 8601", v="", rx="", ex="P25Y (25 anni)", ent="IfcElement",
    m=("pset", "Pset_ServiceLife", "ServiceLifeDuration"), f=["PE", "AB"], chi="Progettista", src="IFC 4.3, Pset_ServiceLife", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ServiceLife.htm")
par(code="IT.ELM.009", lv="IT", g="ELM", it="Durata della garanzia", de="Gewährleistungsdauer", en="Warranty period",
    d="La durata della garanzia del produttore o dell'impresa.",
    t="IfcDuration", u="durata ISO 8601", v="", rx="", ex="P2Y (2 anni)", ent="IfcElement",
    m=("pset", "Pset_Warranty", "WarrantyPeriod"), f=["AB"], chi="Impresa", src="IFC 4.3, Pset_Warranty", url="https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_Warranty.htm")

# ---- Estensione Provincia di Bolzano (estratti pubblici del capitolato informativo) ----
CI_URL = "https://concorsiawn.it/uploads/concorsi/scuola-fallmerayer-bressanone/documentazione-di-gara/capitolato-informativo-ci-bim.00.pdf"
CI = "Provincia autonoma di Bolzano, capitolato informativo (gara scuola Fallmerayer, Bressanone), tabelle 6 e 7 (estratti pubblici)"
par(code="IT-BZ.SPC.001", lv="IT-BZ", g="SPC", it="Codice livello", de="Kodex Ebene", en="Storey code",
    d="Codice del piano a cui è collegato il locale (dal capitolato). In IFC il locale appartiene al piano con una relazione: il codice si legge dal piano (codice del piano del nucleo) senza ricopiarlo nel locale.",
    t="IfcIdentifier", u="", v="", rx="", ex="OG1", ent="IfcSpace",
    m=("rel", "IfcRelAggregates", ""), f=["PFTE"], chi="Progettista", src=CI, url=CI_URL, eq="IT.STO.001")
par(code="IT-BZ.SPC.002", lv="IT-BZ", g="SPC", it="Codice vano", de="Raumkodex", en="Room code",
    d="Codice che identifica ciascun vano (dal capitolato). Coincide con il codice del locale del nucleo.",
    t="IfcLabel", u="", v="", rx="", ex="108", ent="IfcSpace",
    m=("attr", "IfcSpace", "Name"), f=["PFTE"], chi="Progettista", src=CI, url=CI_URL, eq="IT.SPC.001")
par(code="IT-BZ.SPC.003", lv="IT-BZ", g="SPC", it="Codice DIN277", de="Kodex DIN277", en="DIN 277 use code",
    d="Codice di destinazione d'uso del locale secondo le regole di gestione dei locali del committente (dal capitolato). È una classificazione: si collega come riferimento, e nel bSDD esiste già un dizionario delle destinazioni d'uso secondo la DIN 277-2.",
    t="IfcIdentifier", u="", v="classificazione DIN 277", rx="", ex="5.2", ent="IfcSpace",
    m=("class", "IfcClassificationReference", "Identification"), f=["PFTE"], chi="Progettista", src=CI, url=CI_URL, eq="IT.SPC.003")
par(code="IT-BZ.ELM.001", lv="IT-BZ", g="ELM", it="Disciplina", de="Fachbereich", en="Discipline",
    d="Primo livello della struttura dati del committente (dal capitolato).",
    t="IfcIdentifier", u="", v="struttura dati del committente", rx="", ex="5_Aperture", ent="IfcElement",
    m=("class", "IfcClassificationReference", "Identification"), f=["PFTE"], chi="Progettista", src=CI, url=CI_URL, eq="IT.ELM.001")
par(code="IT-BZ.ELM.002", lv="IT-BZ", g="ELM", it="Unità tecnologiche", de="Technologische Einheiten", en="Technological units",
    d="Secondo livello della struttura dati del committente (dal capitolato).",
    t="IfcIdentifier", u="", v="struttura dati del committente", rx="", ex="5.1_Serramenti", ent="IfcElement",
    m=("class", "IfcClassificationReference", "Identification"), f=["PFTE"], chi="Progettista", src=CI, url=CI_URL, eq="IT.ELM.001")
par(code="IT-BZ.ELM.003", lv="IT-BZ", g="ELM", it="Classi di elementi tecnici", de="Klassen der technischen Elemente", en="Technical element classes",
    d="Terzo livello della struttura dati del committente (dal capitolato). I tre livelli sono un'unica classificazione ad albero.",
    t="IfcIdentifier", u="", v="struttura dati del committente", rx="", ex="5.1.2_Finestre", ent="IfcElement",
    m=("class", "IfcClassificationReference", "Identification"), f=["PFTE"], chi="Progettista", src=CI, url=CI_URL, eq="IT.ELM.001")
par(code="IT-BZ.WIN.001", lv="IT-BZ", g="WIN", it="Materiale telaio", de="Material des Rahmens", en="Frame material",
    d="Materiale di cui è composto il telaio della finestra (dal capitolato). In IFC il materiale si associa all'oggetto, non si scrive in un parametro di testo.",
    t="IfcLabel", u="", v="", rx="", ex="Legno", ent="IfcWindow",
    m=("mat", "IfcRelAssociatesMaterial", ""), f=["PE"], chi="Progettista", src=CI, url=CI_URL)
par(code="IT-BZ.WIN.002", lv="IT-BZ", g="WIN", it="Nr. ante", de="Anz. Flügel", en="Number of sashes",
    d="Numero di ante della finestra (dal capitolato). IFC descrive la suddivisione con l'attributo PartitioningType (anta singola, doppia, tripla…), ma non ha un numero intero di ante: qui serve un parametro dell'estensione.",
    t="IfcCountMeasure", u="", v="intero", rx="", ex="2", ent="IfcWindow",
    m=("cpset", "IT_BZ_Finestra", "NumeroAnte"), f=["PE"], chi="Progettista", src=CI, url=CI_URL)

# ---------------------------------------------------------------------------
def verifica():
    import ifcopenshell.util.pset as PS
    import ifcopenshell.ifcopenshell_wrapper as W
    sc = W.schema_by_name("IFC4X3_ADD2")
    tpl = PS.get_template("IFC4X3")
    err = []
    codes = set()
    for p in P:
        if p["code"] in codes: err.append("codice doppio " + p["code"])
        codes.add(p["code"])
        try: sc.declaration_by_name(p["ent"])
        except Exception: err.append(p["code"] + ": entità " + p["ent"])
        k, a, b = p["m"]
        if k in ("pset", "qto"):
            x = tpl.get_by_name(a)
            if not x: err.append(p["code"] + ": manca " + a); continue
            pr = [q for q in x.HasPropertyTemplates if q.Name == b]
            if not pr: err.append(p["code"] + ": manca " + a + "." + b); continue
            if k == "pset" and p["t"] and getattr(pr[0], "PrimaryMeasureType", None) not in (p["t"], None):
                err.append("%s: tipo %s, lo schema dice %s" % (p["code"], p["t"], pr[0].PrimaryMeasureType))
        elif k in ("attr", "crs", "class"):
            d = sc.declaration_by_name(a)
            if b and b not in [x.name() for x in d.all_attributes()]: err.append(p["code"] + ": attributo " + a + "." + b)
        elif k in ("rel", "mat"):
            sc.declaration_by_name(a)
        elif k == "cpset":
            if a.startswith("Pset_"): err.append(p["code"] + ": Pset_ è riservato")
        if p.get("eq") and p["eq"] not in codes and p["eq"] not in [q["code"] for q in P]:
            err.append(p["code"] + ": equivalente inesistente " + p["eq"])
    return err

def ifc_txt(p):
    k, a, b = p["m"]
    return {"pset": a + "." + b, "qto": a + "." + b, "attr": a + "." + b, "crs": a + "." + b,
            "cpset": a + "." + b, "class": "IfcClassificationReference (IfcRelAssociatesClassification)",
            "rel": a, "mat": a}[k]

def scrivi_json():
    out = {"nome": "Dizionario dei dati BIM pubblici · prototipo", "versione": VERSIONE, "data": DATA,
           "stato": "Proposta di BIM News, non è uno standard", "livelli": LIVELLI, "gruppi": GRUPPI, "fasi": FASI,
           "parametri": []}
    for p in P:
        out["parametri"].append({"code": p["code"], "lv": p["lv"], "g": p["g"], "it": p["it"], "de": p["de"], "en": p["en"],
            "d": p["d"], "t": p["t"], "u": p["u"], "v": p["v"], "rx": p["rx"], "ex": p["ex"], "ent": p["ent"],
            "mk": p["m"][0], "ifc": ifc_txt(p), "f": p["f"], "chi": p["chi"], "src": p["src"], "url": p["url"],
            "eq": p.get("eq", ""), "ver": VERSIONE, "st": "proposta"})
    with open(os.path.join(OUT, "dizionario.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))

def scrivi_xlsx():
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment
    from openpyxl.worksheet.table import Table, TableStyleInfo
    wb = Workbook(); ws = wb.active; ws.title = "Leggimi"
    righe = [["Dizionario dei dati BIM pubblici · prototipo " + VERSIONE + " · " + DATA],
             ["Proposta di BIM News (https://bimnews.github.io/), non è uno standard né un documento ufficiale."],
             ["Livelli: IT = nucleo nazionale proposto; IT-BZ = estensione della Provincia di Bolzano, ricostruita solo dagli estratti pubblici del capitolato informativo."],
             ["Mappatura IFC: controllata sullo schema IFC 4.3 ADD2 (ISO 16739-1:2024) con IfcOpenShell. I property set con prefisso IT_ sono proposti qui: Pset_ è riservato a buildingSMART."],
             ["Fasi: PFTE = progetto di fattibilità tecnico-economica; PE = progetto esecutivo; AB = come costruito; GES = gestione."],
             ["I file .ids nella stessa cartella contengono gli stessi requisiti in formato IDS 1.0 (buildingSMART), leggibili dai programmi di controllo dei modelli."]]
    for r in righe: ws.append(r)
    ws["A1"].font = Font(bold=True, size=13); ws.column_dimensions["A"].width = 140
    ws2 = wb.create_sheet("Parametri")
    head = ["Codice", "Livello", "Gruppo", "Nome IT", "Name DE", "Name EN", "Definizione", "Tipo IFC", "Unità", "Valori ammessi",
            "Regola (regex)", "Esempio", "Si applica a", "Mappatura IFC", "Fasi", "Chi lo compila", "Equivalente nel nucleo", "Fonte", "Link", "Versione", "Stato"]
    ws2.append(head)
    for p in P:
        ws2.append([p["code"], p["lv"], GRUPPI[p["g"]], p["it"], p["de"], p["en"], p["d"], p["t"], p["u"], p["v"], p["rx"], p["ex"],
                    p["ent"], ifc_txt(p), ", ".join(p["f"]), p["chi"], p.get("eq", ""), p["src"], p["url"], VERSIONE, "proposta"])
    ref = "A1:U%d" % (len(P) + 1)
    tb = Table(displayName="Parametri", ref=ref); tb.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws2.add_table(tb); ws2.freeze_panes = "B2"
    for col, w in zip("ABCDEFGHIJKLMNOPQRSTU", [15, 8, 22, 30, 30, 30, 70, 18, 10, 22, 16, 22, 18, 42, 14, 16, 14, 50, 40, 8, 10]):
        ws2.column_dimensions[col].width = w
    for row in ws2.iter_rows(min_row=2):
        row[6].alignment = Alignment(wrap_text=True, vertical="top")
    wb.save(os.path.join(OUT, "dizionario-dati-pubblici.xlsx"))

def elementi_concreti():
    """Classi concrete sotto IfcElement, senza aperture/virtuali/feature."""
    import ifcopenshell.ifcopenshell_wrapper as W
    sc = W.schema_by_name("IFC4X3_ADD2")
    out = []
    def giu(d):
        for x in d.subtypes():
            n = x.name()
            if n in ("IfcFeatureElement", "IfcVirtualElement", "IfcSurfaceFeature"):
                continue
            if not x.is_abstract() and not n.endswith("StandardCase"):
                out.append(n.upper())
            giu(x)
    giu(sc.declaration_by_name("IfcElement"))
    return sorted(set(out))

def scrivi_ids():
    from ifctester import ids
    global ELEMENTI
    ELEMENTI = elementi_concreti()
    for lv, nome, file in (("IT", "Nucleo nazionale dei dati BIM pubblici (proposta)", "IT-nucleo.ids"),
                           ("IT-BZ", "Estensione Provincia di Bolzano (dagli estratti pubblici del capitolato)", "IT-BZ-estensione.ids")):
        doc = ids.Ids(title=nome, version=VERSIONE, date=DATA,
                      description="Prototipo di BIM News, non è uno standard. https://bimnews.github.io/",
                      purpose="Proposta", milestone="")
        for p in [q for q in P if q["lv"] == lv]:
            k, a, b = p["m"]
            if k in ("rel", "mat", "crs"):
                continue  # non esprimibili qui come requisito su una proprietà: restano nel dizionario
            ent = p["ent"].upper()
            s = ids.Specification(name=p["code"] + " · " + p["it"], ifcVersion=["IFC4X3_ADD2"],
                                  identifier=p["code"], description=p["d"])
            if p["ent"] == "IfcElement":
                # IDS 1.0 confronta la classe esatta, senza sottoclassi: si elencano le classi concrete
                s.applicability.append(ids.Entity(name=ids.Restriction(options={"enumeration": ELEMENTI}, base="string")))
            else:
                s.applicability.append(ids.Entity(name=ent))
            if k in ("pset", "cpset"):
                val = ids.Restriction(options={"pattern": p["rx"]}, base="string") if p["rx"] else None
                s.requirements.append(ids.Property(propertySet=a, baseName=b, value=val, dataType=(p["t"] or None).upper() if p["t"] else None, cardinality="required"))
            elif k == "qto":
                s.requirements.append(ids.Property(propertySet=a, baseName=b, dataType=p["t"].upper(), cardinality="required"))
            elif k == "attr":
                s.requirements.append(ids.Attribute(name=b, cardinality="required"))
            elif k == "class":
                sysr = ".*DIN ?277.*" if "DIN" in p["it"] else ".+"
                s.requirements.append(ids.Classification(system=ids.Restriction(options={"pattern": sysr}, base="string"), cardinality="required"))
            doc.specifications.append(s)
        doc.to_xml(os.path.join(OUT, file))
        # rilettura con lo schema XSD ufficiale incluso in ifctester
        ids.open(os.path.join(OUT, file), validate=True)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    e = verifica()
    if e:
        print("ERRORI:"); [print(" -", x) for x in e]; sys.exit(1)
    scrivi_json(); scrivi_xlsx(); scrivi_ids()
    print("OK:", len(P), "parametri;", sum(1 for p in P if p["lv"] == "IT"), "nel nucleo,", sum(1 for p in P if p["lv"] == "IT-BZ"), "nell'estensione IT-BZ")
