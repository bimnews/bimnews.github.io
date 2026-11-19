#!/usr/bin/env python3
"""Genera testi/valori_e.tsv: classi che ripetono gli stessi PredefinedType di un'altra classe.
- distribuzioni dei carichi e delle reazioni (curve e superfici), scritte qui una volta;
- IfcStructuralCurveMemberVarying e IfcStructuralSurfaceMemberVarying copiano la classe madre;
- IfcWallStandardCase copia IfcWall, con l'avviso della classe deprecata."""
import os
H = os.path.dirname(os.path.abspath(__file__))
CURVA = [
 ("CONST","Constant","Valore costante lungo la linea.","Constant value along the line."),
 ("DISCRETE","Discrete","Valori dati in punti scelti lungo la linea.","Values given at chosen points along the line."),
 ("EQUIDISTANT","Equidistant","Valori dati in punti a distanza costante.","Values given at equally spaced points."),
 ("LINEAR","Linear","Variazione lineare tra inizio e fine.","Linear variation from start to end."),
 ("PARABOLA","Parabola","Variazione a parabola, simmetrica.","Symmetric parabolic variation."),
 ("POLYGONAL","Polygonal","Variazione lineare a tratti tra più punti.","Piecewise linear variation between several points."),
 ("SINUS","Sinus","Variazione a semionda sinusoidale.","Half sine-wave variation."),
]
SUPERFICIE = [
 ("BILINEAR","Bilinear","Variazione lineare nelle due direzioni della superficie.","Linear variation in both directions of the surface."),
 ("CONST","Constant","Valore costante su tutta la superficie.","Constant value over the whole surface."),
 ("DISCRETE","Discrete","Valori dati in punti scelti della superficie.","Values given at chosen points of the surface."),
 ("ISOCONTOUR","Isocontour","Valori dati lungo linee di uguale intensità.","Values given along lines of equal intensity."),
]
PRE = {"IfcStructuralCurveAction":("Carico","Load"),"IfcStructuralLinearAction":("Carico","Load"),"IfcStructuralCurveReaction":("Reazione","Reaction"),
       "IfcStructuralSurfaceAction":("Carico","Load"),"IfcStructuralPlanarAction":("Carico","Load"),"IfcStructuralSurfaceReaction":("Reazione","Reaction")}
def leggi(nome):
    out={}
    for f in sorted(os.listdir(os.path.join(H,"testi"))):
        if not f.startswith("valori") or f=="valori_e.tsv": continue
        for l in open(os.path.join(H,"testi",f),encoding="utf-8"):
            if l.startswith("#") or not l.strip(): continue
            x=(l.rstrip("\n").split("\t")+[""]*6)[:6]
            if x[0]==nome: out[x[1]]=x
    return out
righe=["# Generato da ripeti.py: non modificare a mano"]
for c,(pi,pe) in PRE.items():
    for v,en,di,de in (CURVA if "Curve" in c or "Linear" in c else SUPERFICIE):
        righe.append("\t".join([c,v,en,pi+": "+di[0].lower()+di[1:],pe+": "+de[0].lower()+de[1:]]))
for c,m in (("IfcStructuralCurveMemberVarying","IfcStructuralCurveMember"),("IfcStructuralSurfaceMemberVarying","IfcStructuralSurfaceMember")):
    for v,x in leggi(m).items(): righe.append("\t".join([c]+x[1:]))
for v,x in leggi("IfcWall").items():
    righe.append("\t".join([ "IfcWallStandardCase",v,x[2],x[3]+" Classe deprecata: usare IfcWall.",x[4]+" Deprecated class: use IfcWall.",x[5]]))
open(os.path.join(H,"testi","valori_e.tsv"),"w",encoding="utf-8").write("\n".join(righe)+"\n")
print(len(righe)-1,"righe")
