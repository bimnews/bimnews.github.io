"""Esporta la geometria di manuali/ifc-da-zero/casetta.ifc per il visualizzatore dell'articolo.

La geometria la calcola IfcOpenShell dal file IFC scritto a mano (fori compresi):
python3 strumenti/ifc/casetta_json.py  ->  manuali/ifc-da-zero/casetta-3d.json
"""
import json, math, os
import numpy as np
import ifcopenshell, ifcopenshell.geom

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'manuali', 'ifc-da-zero')
f = ifcopenshell.open(os.path.join(BASE, 'casetta.ifc'))
st = ifcopenshell.geom.settings(); st.set('use-world-coords', True)
it = ifcopenshell.geom.iterator(st, f); it.initialize()

def piano(e):
    for r in getattr(e, 'ContainedInStructure', []) or []:
        return r.RelatingStructure.Name
    for r in getattr(e, 'Decomposes', []) or []:
        p = r.RelatingObject
        if p.is_a('IfcBuildingStorey'): return p.Name
        return piano(p)
    for r in getattr(e, 'VoidsElements', []) or []:
        return piano(r.RelatingBuildingElement)
    return ''

out = []
while True:
    sh = it.get(); e = f.by_guid(sh.guid)
    v = np.array(sh.geometry.verts).reshape(-1, 3)
    fa = np.array(sh.geometry.faces).reshape(-1, 3)
    mats, ids = sh.geometry.materials, sh.geometry.material_ids
    col = [0.85, 0.3, 0.3, 0.35]
    if len(ids) and ids[0] >= 0:
        m = mats[ids[0]]; c = m.diffuse
        try: rgb = [c.r(), c.g(), c.b()]
        except Exception: rgb = list(c)[:3]
        tr = m.transparency if (m.transparency == m.transparency) else 0
        col = [round(x, 3) for x in rgb] + [round(1 - (tr or 0), 2)]
    if e.is_a('IfcOpeningElement'):
        col = [0.86, 0.25, 0.25, 0.35]
    # spigoli veri: lati tra triangoli con normali diverse (o lati di bordo)
    nrm = []
    for t in fa:
        a, b, c = v[t]; n = np.cross(b - a, c - a); l = np.linalg.norm(n); nrm.append(n / l if l else n)
    ed = {}
    for k, t in enumerate(fa):
        for i in range(3):
            p, q = sorted((int(t[i]), int(t[(i + 1) % 3])))
            ed.setdefault((p, q), []).append(k)
    edges = []
    for (p, q), ts in ed.items():
        if len(ts) == 1 or abs(float(np.dot(nrm[ts[0]], nrm[ts[1]]))) < 0.985:
            edges.append([p, q])
    out.append({
        'id': e.id(), 'c': e.is_a(), 'n': e.Name, 'p': piano(e), 'col': col,
        'v': [round(float(x), 4) for x in v.flatten()],
        'f': [int(x) for x in fa.flatten()], 'e': [x for pq in edges for x in pq],
    })
    if not it.next(): break
json.dump(out, open(os.path.join(BASE, 'casetta-3d.json'), 'w'), separators=(',', ':'))
print(len(out), 'oggetti')
