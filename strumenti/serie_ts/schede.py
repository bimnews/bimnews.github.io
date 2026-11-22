# Scrive in index.html (sezione MEP, Didattica) le schede degli articoli 2–11 della serie termosanitario.
# Uso: python3 strumenti/serie_ts/schede.py   (rigenera le schede tra mep-ts-01 e la fine dell'elenco)
import json, os, re
B = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(B, '../..'))
import importlib.util
spec = importlib.util.spec_from_file_location('g', os.path.join(B, 'genera.py')); g = importlib.util.module_from_spec(spec)
TITOLI = {2: "La linea d'azione", 3: 'La generazione', 4: 'Accumulo e separazione', 5: 'La distribuzione', 6: "L'emissione", 7: 'La regolazione', 8: "L'acqua calda sanitaria", 9: 'La rete idrica', 10: 'Gli scarichi', 11: 'Nel modello'}
TESTI = {
 2: "Dal fabbisogno alle scelte: centrale o autonomo, acqua o aria, e soprattutto la temperatura a cui lavora l'impianto. Con il regolo delle temperature e il COP della pompa di calore.",
 3: "Pompa di calore, caldaia a condensazione, teleriscaldamento: come lavorano e come si sceglie la potenza alla temperatura di progetto. Con il bilancio della pompa di calore da provare.",
 4: "Il volume d'acqua che protegge la macchina, il separatore tra i circuiti e il vaso di espansione, con la sua formula e la figura del vaso.",
 5: "Dalla potenza alla portata, i diametri, la pompa e il circuito che si incontrano nel punto di lavoro, il bilanciamento.",
 6: "Pavimento radiante, radiatori, ventilconvettori: la legge di ogni terminale e la temperatura dell'acqua che serve. Con il pavimento che scalda.",
 7: "Curva climatica, regolazione per ambiente, orari e ventilazione sulla presenza: quanto calore, quando e dove.",
 8: "Accumulo, ricircolo e produzione istantanea, con le temperature delle linee guida sulla legionellosi e i loro effetti su una pompa di calore.",
 9: "Pressioni dall'allaccio al rubinetto più alto, portate contemporanee, riduttori, pressurizzazione e protezione dal riflusso.",
 10: "Unità di scarico e portata di progetto secondo la UNI EN 12056-2, colonne, ventilazione e sifoni.",
 11: "Classi IFC 4.3, tipi, Pset, sistemi e collegamenti: dove va ogni pezzo dell'impianto e ogni numero calcolato nella serie.",
}
SLUG = {2:'linea-d-azione',3:'generazione',4:'accumulo',5:'distribuzione',6:'emissione',7:'regolazione',8:'acqua-calda',9:'idrico',10:'scarichi',11:'nel-modello'}
out = []
for n in range(2, 12):
    meta = json.loads(open(os.path.join(B, 'testi', '%02d.html' % n), encoding='utf-8').readline())
    f = 'manuali/termosanitario-%02d-%s.html' % (n, SLUG[n])
    assert os.path.exists(os.path.join(R, f)), f
    out.append('          <article class="st-item" id="mep-ts-%02d"><span class="st-n">%02d</span><div><h4>L\'impianto termosanitario, passo per passo · %d · %s</h4><p>%s</p><p class="man-dl"><span class="tag ok">Pubblicato</span><a class="man-btn" href="%s">Leggi l\'articolo</a><a class="man-btn ghost" href="%s#%s">La figura</a></p></div></article>' % (n, n, n, TITOLI[n], TESTI[n], f, f, meta['ancora_figura']))
p = os.path.join(R, 'index.html'); s = open(p, encoding='utf-8').read()
s = re.sub(r'\n          <article class="st-item" id="mep-ts-(0[2-9]|1[01])">.*?</article>', '', s)
i = s.index('id="mep-ts-01"'); j = s.index('</article>', i) + len('</article>')
s = s[:j] + '\n' + '\n'.join(out) + s[j:]
open(p, 'w', encoding='utf-8').write(s)
print('schede scritte:', len(out))
