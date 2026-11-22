# Genera gli articoli della serie «L'impianto termosanitario, passo per passo» (sezione MEP, Didattica).
# Ogni articolo sta in testi/NN.html: una riga JSON di testa (titolo, sottotitolo, indice, figura) e poi il corpo HTML (le <section>).
# Uso: python3 strumenti/serie_ts/genera.py   →   manuali/termosanitario-NN-slug.html
import json, os, re
B = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(B, '../..'))
SERIE = [(1,'fabbisogno','Fabbisogno'),(2,'linea-d-azione',"Linea d'azione"),(3,'generazione','Generazione'),(4,'accumulo','Accumulo'),
         (5,'distribuzione','Distribuzione'),(6,'emissione','Emissione'),(7,'regolazione','Regolazione'),(8,'acqua-calda','Acqua calda'),
         (9,'idrico','Idrico'),(10,'scarichi','Scarichi'),(11,'nel-modello','Nel modello')]
def file_of(n, slug): return 'termosanitario-%02d-%s.html' % (n, slug)
def esiste(n, slug): return os.path.exists(os.path.join(R, 'manuali', file_of(n, slug))) or os.path.exists(os.path.join(B, 'testi', '%02d.html' % n))

def serie_nav(cur):
    out = []
    for n, slug, t in SERIE:
        lab = '%d %s' % (n, t)
        if n == cur: out.append('<span class="on">%s</span>' % lab)
        elif esiste(n, slug): out.append('<a href="%s">%s</a>' % (file_of(n, slug), lab))
        else: out.append('<span>%s</span>' % lab)
    return '<div class="series" aria-label="La serie">' + ''.join(out) + '</div>'

def prev_next(cur):
    p = [s for s in SERIE if s[0] == cur - 1 and esiste(s[0], s[1])]
    n = [s for s in SERIE if s[0] == cur + 1 and esiste(s[0], s[1])]
    a = '<a class="btn ghost" href="%s">← %d · %s</a>' % (file_of(p[0][0], p[0][1]), p[0][0], p[0][2]) if p else '<span></span>'
    b = '<a class="btn" href="%s">%d · %s →</a>' % (file_of(n[0][0], n[0][1]), n[0][0], n[0][2]) if n else '<span></span>'
    return '<nav class="pn noprint" aria-label="Articoli della serie">' + a + b + '</nav>'

CSS = '''.btn.ghost,:root[data-theme="dark"] .btn.ghost{color:var(--accent)}
.formula{font-family:var(--mono);background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:.9rem 1.1rem;margin:.6rem 0 1rem;font-size:.95rem;line-height:1.75;overflow-x:auto}
.fig-frame{width:100%;border:0;min-height:640px;display:block;background:transparent;margin:.4rem 0 1rem}
.fig-alt{margin:.4rem 0 1rem}
.series{display:flex;flex-wrap:wrap;gap:.35rem;margin:.4rem 0 0}
.series span,.series a{font-family:var(--mono);font-size:.72rem;border:1px solid var(--line);border-radius:999px;padding:.15rem .55rem;color:var(--muted);text-decoration:none}
.series a{color:var(--accent);border-color:color-mix(in srgb,var(--accent) 45%,var(--line))}
.series span.on{background:var(--accent);border-color:var(--accent);color:#fff}
:root[data-theme="dark"] .series span.on{color:#10141b}
.num td:nth-child(n+2){font-family:var(--mono);white-space:nowrap}
.pn{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 .6rem}'''

def pagina(n, slug, meta, corpo):
    toc = ''.join('<li><a href="#%s">%s</a></li>' % (a, t) for a, t in meta['indice'])
    fig = meta.get('figura')
    script = ''
    if fig:
        script = ('<script>\nwindow.addEventListener("message",function(e){ if(e.data&&e.data.figH&&e.data.fig===%s){ var g=document.getElementById("fig-frame"); if(g)g.style.height=(e.data.figH+4)+"px"; } });\n'
          '(function(){ var box=document.getElementById("fig-box"); if(!box)return; var lite=false; try{ var m=localStorage.getItem("versione"),c=navigator.connection,a=matchMedia("(prefers-reduced-motion: reduce)").matches||(c&&(c.saveData||/(^|-)2g$/.test(c.effectiveType||""))); lite=m?m==="essenziale":a; }catch(x){}\n'
          '  if(lite){ box.innerHTML=\'<p class="fig-alt"><a href="figure/%s.html">Apri la figura interattiva</a> (pagina a parte).</p>\'; return; }\n'
          '  var f=document.createElement("iframe"); f.id="fig-frame"; f.className="fig-frame"; f.title=%s; f.loading="lazy"; f.src="figure/%s.html?embed=1"; box.appendChild(f); })();\n</script>') % (json.dumps(fig['nome']), fig['nome'], json.dumps('Figura interattiva: ' + fig['titolo']), fig['nome'])
    return f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{meta['titolo']} · I manuali di BIM News</title>
<meta name="description" content="{meta['descrizione']}">
<link rel="stylesheet" href="manuale.css">
<script>try{{var t=localStorage.getItem("tema-2026");if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<style>
{CSS}
</style>
</head>
<body>
<div class="topbar"><div class="in"><a class="back" href="../#mep">← BIM News · MEP</a><span class="sp"></span>{('<a class="btn ghost noprint" href="#%s">La figura</a>' % meta['ancora_figura']) if fig else ''}<a class="btn noprint" href="#{meta['ancora_chiave']}">{meta['etichetta_chiave']}</a></div></div>
<div class="layout">
<nav class="toc" aria-label="Indice">
  <b>Indice</b>
  <ol>{toc}<li><a href="#fonti">Fonti</a></li></ol>
</nav>
<main>
<header class="cover">
  <div>
    <span class="kick">L'impianto termosanitario, passo per passo · {n}</span>
    <h1>{meta['titolo']}</h1>
    <p>{meta['sommario']}</p>
    {serie_nav(n)}
  </div>
  {meta['copertina']}
</header>
{corpo}
{prev_next(n)}
<p class="foot">BIM News · L'impianto termosanitario, passo per passo · {n} · {meta['titolo']} · edizione novembre 2026</p>
</main>
</div>
{script}
</body>
</html>
'''

if __name__ == '__main__':
    for f in sorted(os.listdir(os.path.join(B, 'testi'))):
        if not re.match(r'\d\d\.html$', f): continue
        txt = open(os.path.join(B, 'testi', f), encoding='utf-8').read()
        head, corpo = txt.split('\n', 1)
        meta = json.loads(head)
        n = int(f[:2]); slug = SERIE[n - 1][1]
        open(os.path.join(R, 'manuali', file_of(n, slug)), 'w', encoding='utf-8').write(pagina(n, slug, meta, corpo))
        print('scritto', file_of(n, slug))
    # articolo 1 (scritto a mano): aggiorna i rimandi alla serie e la navigazione in fondo
    p1 = os.path.join(R, 'manuali', file_of(1, 'fabbisogno'))
    s = open(p1, encoding='utf-8').read()
    s = re.sub(r'<div class="series" aria-label="La serie">.*?</div>', serie_nav(1), s, flags=re.S)
    if '.series a{' not in s:
        s = s.replace('.series span.on{', '.series a{font-family:var(--mono);font-size:.72rem;border:1px solid color-mix(in srgb,var(--accent) 45%,var(--line));border-radius:999px;padding:.15rem .55rem;color:var(--accent);text-decoration:none}\n.pn{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;margin:1.4rem 0 .6rem}\n.series span.on{')
    s = re.sub(r'<nav class="pn noprint".*?</nav>\n?', '', s, flags=re.S)
    s = s.replace('  <p class="foot">BIM News · L\'impianto termosanitario', prev_next(1) + '\n  <p class="foot">BIM News · L\'impianto termosanitario')
    open(p1, 'w', encoding='utf-8').write(s)
