# Verifica di una fonte: scarica la pagina (o il PDF), estrae il testo e mostra le frasi con le parole chiave
import sys,subprocess,re,html,os,hashlib
D='/tmp/claude-0/-home-user-mscigliuolo-github-io/3bbcc406-91d1-5415-a43b-de0ade14353b/scratchpad/ric/'
os.makedirs(D,exist_ok=True)
url=sys.argv[1];keys=[k.lower() for k in sys.argv[2:]]
f=D+hashlib.md5(url.encode()).hexdigest()
r=subprocess.run(['curl','-sL','--http1.1','--compressed','-A','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36','-H','Accept-Language: es,en;q=0.8','--max-time','60','-o',f,'-w','%{http_code} %{content_type} %{url_effective}',url],capture_output=True,text=True)
print('HTTP',r.stdout)
if not os.path.exists(f) or os.path.getsize(f)==0:print('VUOTO');sys.exit()
b=open(f,'rb').read()
if b[:4]==b'%PDF':
    t=subprocess.run(['pdftotext','-l','12',f,'-'],capture_output=True,text=True).stdout
else:
    t=b.decode('utf-8','ignore')
    m=re.search(r'<title[^>]*>(.*?)</title>',t,re.S|re.I);print('TITOLO:',html.unescape(m.group(1)).strip()[:150] if m else '-')
    for pat in [r'"datePublished"\s*:\s*"([^"]+)"',r'article:published_time"\s+content="([^"]+)"',r'<time[^>]*datetime="([^"]+)"']:
        mm=re.search(pat,t)
        if mm:print('DATA:',mm.group(1));break
    t=re.sub(r'<script.*?</script>|<style.*?</style>',' ',t,flags=re.S|re.I);t=html.unescape(re.sub(r'<[^>]+>',' ',t))
t=re.sub(r'\s+',' ',t)
print('LUNGHEZZA',len(t))
for k in keys:
    for m in list(re.finditer(re.escape(k),t.lower()))[:3]:
        print('['+k+']',t[max(0,m.start()-220):m.start()+260].strip());print()
