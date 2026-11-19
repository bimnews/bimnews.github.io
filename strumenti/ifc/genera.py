#!/usr/bin/env python3
"""Libreria IFC 4.3 di BIM News: genera la mappa JSON e l'Excel in inglese.

Ingressi (in questa cartella):
  struttura_classi.tsv  classi del ramo IfcProduct (dallo schema IFC4X3_ADD2), nome IT, supertipo, astratta, deprecazione
  struttura_valori.tsv  una riga per classe + PredefinedType, nome IT, deprecazione del valore
  testi/classi.tsv      nome EN e descrizioni IT/EN delle classi (testi nostri)
  testi/valori.tsv      nome EN e descrizioni IT/EN dei PredefinedType (testi nostri)
Uscite:
  manuali/libreria-ifc/ifc-4.3-map.json
  manuali/libreria-ifc/IFC-4.3-library.xlsx
Uso: python3 strumenti/ifc/genera.py   (serve openpyxl)
Controllo dello schema: strumenti/ifc/controlla_schema.py (serve ifcopenshell).
"""
import json, os, sys
from collections import OrderedDict

H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(H, "..", ".."))
OUT = os.path.join(ROOT, "manuali", "libreria-ifc")
DOC = "https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/"

DEP_EN = {
    "Mantenuta per compatibilità: usare IfcWall": "Kept for compatibility: use IfcWall",
    "Deprecata in IFC 4.3: usare le sottoclassi specifiche": "Deprecated in IFC 4.3: use the specific subclasses",
    "Deprecata per l'istanza: usare le sottoclassi": "Deprecated for instances: use the subclasses",
    "Deprecata in IFC 4.3: usare IfcDistributionBoard": "Deprecated in IFC 4.3: use IfcDistributionBoard",
    "Deprecata per l'istanza: usare IfcFurniture / IfcSystemFurnitureElement": "Deprecated for instances: use IfcFurniture / IfcSystemFurnitureElement",
    "Valore deprecato": "Deprecated value",
}
DEP_IT = {"Valore deprecato": "Valore deprecato"}

AUTO = {
    "USERDEFINED": ("User defined", "Definito dall'utente",
                    "Tipo che non è nell'elenco: si scrive nell'attributo ObjectType dell'oggetto (o ElementType del tipo).",
                    "Type not in the list: write it in the object's ObjectType attribute (or the type's ElementType)."),
    "NOTDEFINED": ("Not defined", "Non definito",
                   "Tipo non ancora deciso o non noto.",
                   "Type not yet decided or not known."),
}


def tsv(path, n):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        f = line.split("\t")
        rows.append((f + [""] * n)[:n])
    return rows


def main():
    classi = OrderedDict()
    for c, it, sup, ab, enum, dep in tsv(os.path.join(H, "struttura_classi.tsv"), 6):
        classi[c] = dict(n=c, it=it, s=sup if sup != "None" else "", a=1 if ab else 0, e=enum, dep=dep)
    for c, en, di, de in tsv(os.path.join(H, "testi", "classi.tsv"), 4):
        if c not in classi:
            sys.exit("classe sconosciuta in testi/classi.tsv: " + c)
        classi[c].update(en=en, di=di, de=de)
    testi = {(c, v): (en, di, de, itc) for c, v, en, di, de, itc in tsv(os.path.join(H, "testi", "valori.tsv"), 6)}
    valori = OrderedDict()
    for c, v, it, dep in tsv(os.path.join(H, "struttura_valori.tsv"), 4):
        valori.setdefault(c, []).append((v, it, dep))
    for k in testi:
        if k[0] not in valori or k[1] not in [x[0] for x in valori[k[0]]]:
            sys.exit("valore sconosciuto in testi/valori.tsv: %s.%s" % k)

    mancano = [c for c, d in classi.items() if not d.get("di")]
    if mancano:
        print("ATTENZIONE: classi senza descrizione:", len(mancano))

    # albero e livelli
    figli = OrderedDict((c, []) for c in classi)
    for c, d in classi.items():
        if d["s"]:
            figli[d["s"]].append(c)

    def antenati(c):
        out = []
        while classi[c]["s"]:
            c = classi[c]["s"]
            out.append(c)
        return out[::-1]

    # JSON
    js = {"schema": "IFC 4.3 ADD2", "iso": "ISO 16739-1:2024", "doc": DOC, "classes": []}
    righe = []  # per l'Excel
    senza = 0
    for c, d in classi.items():
        o = {"n": c, "s": d["s"], "a": d["a"], "it": d["it"], "en": d.get("en", ""), "di": d.get("di", ""), "de": d.get("de", "")}
        if d["e"]:
            o["e"] = d["e"]
        if d["dep"]:
            o["xi"] = d["dep"]
            o["xe"] = DEP_EN[d["dep"]]
        pt = []
        for v, it, dep in valori.get(c, []):
            if v == "—":
                continue
            if v in AUTO:
                en, it2, di, de = AUTO[v]
                it = it2
            else:
                en, di, de, itc = testi.get((c, v), ("", "", "", ""))
                if itc:
                    it = itc
                if not di:
                    senza += 1
            p = {"v": v, "it": it, "en": en, "di": di, "de": de}
            if dep:
                p["x"] = 1
            pt.append(p)
        if pt:
            o["p"] = pt
        js["classes"].append(o)
        # righe della libreria (solo classi istanziabili)
        if d["a"]:
            continue
        liv = [a for a in antenati(c) if a != "IfcProduct"][:4]
        liv += [""] * (4 - len(liv))
        dep_c = DEP_EN.get(d["dep"], "")
        if not pt:
            righe.append(liv + [c, d.get("en", ""), d["it"], "—", d.get("en", ""), d["it"], d.get("de", ""), d.get("di", ""), c, "", dep_c, DOC + c + ".htm", ""])
        for p in pt:
            dep = dep_c or ("Deprecated value" if p.get("x") else "")
            righe.append(liv + [c, d.get("en", ""), d["it"], p["v"], p["en"], p["it"], p["de"], p["di"], c, p["v"], dep, DOC + c + ".htm", DOC + d["e"] + ".htm" if d["e"] else ""])
    if senza:
        print("ATTENZIONE: PredefinedType senza descrizione:", senza)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "ifc-4.3-map.json"), "w", encoding="utf-8") as f:
        json.dump(js, f, ensure_ascii=False, separators=(",", ":"))

    # Excel
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, PatternFill
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from openpyxl.utils import get_column_letter
    wb = Workbook()
    rd = wb.active
    rd.title = "Read me"
    n_ist = sum(1 for d in classi.values() if not d["a"])
    info = [
        ("IFC 4.3 library · BIM News", ""),
        ("", ""),
        ("What it is", "Every instantiable class of the IfcProduct branch of IFC 4.3 ADD2 (ISO 16739-1:2024), one row per class + PredefinedType, with names and short descriptions in English and Italian."),
        ("Schema", "IFC4X3_ADD2, checked against the EXPRESS schema shipped with IfcOpenShell 0.9.0."),
        ("Rows in Library", len(righe)),
        ("Instantiable classes", n_ist),
        ("Abstract classes (only in Classes)", len(classi) - n_ist),
        ("", ""),
        ("Sheets", ""),
        ("Library", "One row per class + PredefinedType. Filter it like any Excel table."),
        ("Classes", "All 214 classes of the IfcProduct branch, abstract ones included, with supertype and full hierarchy."),
        ("", ""),
        ("Columns", ""),
        ("Level 1–4", "Ancestors of the class below IfcProduct (e.g. IfcElement > IfcBuiltElement)."),
        ("PredefinedType", "Value of the class enumeration. «—» = instantiable class without PredefinedType."),
        ("USERDEFINED", "Write the actual type in the ObjectType attribute of the object (or ElementType of the type)."),
        ("IfcExportAs / IfcExportType", "Values ready for the Revit IFC exporter parameters of the same name."),
        ("Deprecated", "Class or value deprecated in the standard: avoid it in new models."),
        ("", ""),
        ("Texts", "Names and descriptions are written by BIM News in plain words to help choose the right class; they are not the official definitions. The official definition is one click away in the documentation columns, on buildingSMART's site."),
        ("Official documentation", DOC.rsplit("/lexical/", 1)[0] + "/"),
        ("Licence of this file", "Free to use. IFC is a buildingSMART International standard; this file is not an official buildingSMART publication."),
        ("Other languages", "Need the descriptions in another language? Ask on LinkedIn: https://www.linkedin.com/in/marco-scigliuolo/"),
        ("Source", "https://bimnews.github.io/manuali/libreria-ifc.html"),
    ]
    for r in info:
        rd.append(list(r))
    rd["A1"].font = Font(bold=True, size=14)
    for row in rd.iter_rows(min_row=2):
        row[0].font = Font(bold=True)
        row[1].alignment = Alignment(wrap_text=True, vertical="top")
    rd.column_dimensions["A"].width = 34
    rd.column_dimensions["B"].width = 110

    head = ["ID", "Level 1", "Level 2", "Level 3", "Level 4", "IFC class", "Class (EN)", "Class (IT)", "PredefinedType",
            "Name (EN)", "Name (IT)", "Description (EN)", "Description (IT)", "IfcExportAs", "IfcExportType", "Deprecated",
            "Class documentation", "Enumeration documentation"]
    ws = wb.create_sheet("Library")
    ws.append(head)
    for i, r in enumerate(righe, 1):
        ws.append(["IFC-%04d" % i] + r)
    larg = [10, 22, 26, 28, 26, 30, 28, 30, 26, 30, 30, 60, 60, 30, 22, 28, 40, 40]
    for i, w in enumerate(larg, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for col in (17, 18):
        for cell in ws.iter_cols(min_col=col, max_col=col, min_row=2):
            for c in cell:
                if c.value:
                    c.hyperlink = c.value
                    c.style = "Hyperlink"
    t = Table(displayName="Library", ref="A1:%s%d" % (get_column_letter(len(head)), len(righe) + 1))
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws.add_table(t)
    ws.freeze_panes = "G2"
    for c in "BCDE":
        ws.column_dimensions[c].outlineLevel = 1

    wc = wb.create_sheet("Classes")
    hc = ["IFC class", "Class (EN)", "Class (IT)", "Supertype", "Hierarchy", "Level", "Abstract", "PredefinedType enumeration",
          "Values", "Deprecated", "Description (EN)", "Description (IT)", "Class documentation"]
    wc.append(hc)
    for c, d in classi.items():
        an = antenati(c)
        nv = len([p for p in valori.get(c, []) if p[0] != "—"])
        wc.append([c, d.get("en", ""), d["it"], d["s"], " > ".join(an + [c]), len(an), "Yes" if d["a"] else "No", d["e"], nv,
                   DEP_EN.get(d["dep"], ""), d.get("de", ""), d.get("di", ""), DOC + c + ".htm"])
    for i, w in enumerate([34, 34, 34, 30, 70, 7, 9, 34, 8, 40, 60, 60, 40], 1):
        wc.column_dimensions[get_column_letter(i)].width = w
    for cell in wc.iter_cols(min_col=13, max_col=13, min_row=2):
        for c in cell:
            c.hyperlink = c.value
            c.style = "Hyperlink"
    t2 = Table(displayName="Classes", ref="A1:M%d" % (len(classi) + 1))
    t2.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    wc.add_table(t2)
    wc.freeze_panes = "B2"
    wb.properties.creator = "BIM News"
    wb.properties.title = "IFC 4.3 library"
    wb.save(os.path.join(OUT, "IFC-4.3-library.xlsx"))
    print("righe", len(righe), "classi", len(classi))


if __name__ == "__main__":
    main()
