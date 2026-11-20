# Pacchetto p25: la scheda «Un dizionario nazionale dei dati BIM pubblici» (#prop-01 in #proposte) e la riga LinkedIn.
# Uso: python3 strumenti/lingue/p25_dati_pubblici.py <estratto.json>  (estratto = uscita di extract.js)
import json,sys,os
B=os.path.dirname(os.path.abspath(__file__))
L=['en','fr','de','es','pt','ru','ar','zh','ja','ko']
N=json.load(open(sys.argv[1],encoding='utf-8'))
T={
'Un dizionario nazionale dei dati BIM pubblici':[
 'A national dictionary of public BIM data',
 'Un dictionnaire national des données BIM publiques',
 'Ein nationales Wörterbuch der öffentlichen BIM-Daten',
 'Un diccionario nacional de los datos BIM públicos',
 'Um dicionário nacional dos dados BIM públicos',
 'Национальный словарь публичных данных BIM',
 'قاموس وطني لبيانات BIM العامة',
 '公共 BIM 数据的国家词典',
 '公共 BIM データの全国辞書',
 '공공 BIM 데이터 국가 사전'],
"Ogni committente pubblico chiede i suoi parametri, con i suoi nomi: propongo un nucleo comune per tutta l'Italia, con le estensioni di regioni ed enti agganciate sopra.":[
 'Every public client asks for its own parameters, with its own names: I propose a common core for the whole of Italy, with the extensions of regions and public bodies attached on top.',
 "Chaque maître d'ouvrage public demande ses propres paramètres, avec ses propres noms : je propose un noyau commun pour toute l'Italie, auquel se rattachent les extensions des régions et des organismes.",
 'Jeder öffentliche Auftraggeber verlangt eigene Parameter mit eigenen Namen: Ich schlage einen gemeinsamen Kern für ganz Italien vor, an den die Erweiterungen der Regionen und Körperschaften angehängt werden.',
 'Cada cliente público pide sus propios parámetros, con sus propios nombres: propongo un núcleo común para toda Italia, con las extensiones de regiones y organismos enganchadas encima.',
 'Cada dono de obra público pede os seus próprios parâmetros, com os seus próprios nomes: proponho um núcleo comum para toda a Itália, com as extensões de regiões e entidades ligadas por cima.',
 'Каждый государственный заказчик требует свои параметры со своими названиями: я предлагаю общее ядро для всей Италии, к которому подключаются расширения регионов и ведомств.',
 'كل جهة عامة مالكة تطلب معاملاتها الخاصة بأسمائها الخاصة: أقترح نواة مشتركة لكل إيطاليا، تُربط بها امتدادات الأقاليم والهيئات.',
 '每个公共业主都要求自己的参数和自己的名称：我建议为全意大利建立一个共同核心，各大区和机构的扩展挂接在其上。',
 '公共発注者はそれぞれ独自のパラメータを独自の名前で求めている。私はイタリア全土に共通の中核を提案し、州や機関の拡張をその上に接続する。',
 '공공 발주처마다 자기만의 이름으로 자기만의 파라미터를 요구합니다. 저는 이탈리아 전체에 공통 핵심을 두고, 그 위에 주와 기관의 확장을 연결하자고 제안합니다.'],
"Codici che esistono già (CUP, ISTAT, IPA, ISO 3166-2), prima le proprietà standard di IFC e poi quelle nuove, una scheda per ogni parametro e requisiti che i software controllano da soli (IDS). Con un prototipo da consultare, l'estensione della Provincia di Bolzano, una famiglia MEP vera e una domanda: e il resto del mondo?":[
 'Codes that already exist (CUP, ISTAT, IPA, ISO 3166-2), standard IFC properties first and new ones only after, one data sheet per parameter and requirements that software checks on its own (IDS). With a prototype to browse, the extension of the Province of Bolzano, a real MEP family and one question: what about the rest of the world?',
 "Des codes qui existent déjà (CUP, ISTAT, IPA, ISO 3166-2), d'abord les propriétés standard d'IFC puis les nouvelles, une fiche par paramètre et des exigences que les logiciels vérifient seuls (IDS). Avec un prototype à consulter, l'extension de la Province de Bolzano, une vraie famille MEP et une question : et le reste du monde ?",
 'Codes, die es schon gibt (CUP, ISTAT, IPA, ISO 3166-2), zuerst die Standardeigenschaften von IFC und erst dann neue, ein Datenblatt pro Parameter und Anforderungen, die die Software selbst prüft (IDS). Mit einem Prototyp zum Nachschlagen, der Erweiterung der Provinz Bozen, einer echten MEP-Familie und einer Frage: Und der Rest der Welt?',
 'Códigos que ya existen (CUP, ISTAT, IPA, ISO 3166-2), primero las propiedades estándar de IFC y después las nuevas, una ficha por parámetro y requisitos que el software comprueba solo (IDS). Con un prototipo para consultar, la extensión de la Provincia de Bolzano, una familia MEP real y una pregunta: ¿y el resto del mundo?',
 'Códigos que já existem (CUP, ISTAT, IPA, ISO 3166-2), primeiro as propriedades padrão do IFC e depois as novas, uma ficha por parâmetro e requisitos que o software verifica sozinho (IDS). Com um protótipo para consultar, a extensão da Província de Bolzano, uma família MEP real e uma pergunta: e o resto do mundo?',
 'Уже существующие коды (CUP, ISTAT, IPA, ISO 3166-2), сначала стандартные свойства IFC и лишь потом новые, карточка для каждого параметра и требования, которые программы проверяют сами (IDS). С прототипом для просмотра, расширением провинции Больцано, настоящим MEP-семейством и вопросом: а остальной мир?',
 'رموز موجودة بالفعل (CUP وISTAT وIPA وISO 3166-2)، أولًا خصائص IFC القياسية ثم الجديدة، وبطاقة لكل معامل ومتطلبات تتحقق منها البرامج بنفسها (IDS). مع نموذج أولي للاطلاع، وامتداد مقاطعة بولتسانو، وعائلة MEP حقيقية، وسؤال: وماذا عن بقية العالم؟',
 '使用已有的编码（CUP、ISTAT、IPA、ISO 3166-2），先用 IFC 标准属性再加新属性，每个参数一张卡片，需求由软件自动检查（IDS）。附可查询的原型、博尔扎诺省的扩展、一个真实的 MEP 族，以及一个问题：世界其他地方呢？',
 '既存のコード（CUP、ISTAT、IPA、ISO 3166-2）、まず IFC の標準プロパティ、新しいものはその後、パラメータごとに 1 枚のシート、ソフトウェアが自動でチェックする要件（IDS）。閲覧できるプロトタイプ、ボルツァーノ自治県の拡張、実際の MEP ファミリ、そして問い：世界のほかの国は？',
 '이미 있는 코드(CUP, ISTAT, IPA, ISO 3166-2), IFC 표준 속성을 먼저 쓰고 새 속성은 그다음, 파라미터마다 한 장의 시트, 소프트웨어가 스스로 검사하는 요구사항(IDS). 살펴볼 수 있는 프로토타입, 볼차노 자치주의 확장, 실제 MEP 패밀리, 그리고 질문 하나: 나머지 세계는?'],
}
BTN=[['Published','Read the proposal','The prototype','Download the Excel file'],
     ['Publié','Lire la proposition','Le prototype',"Télécharger l'Excel"],
     ['Veröffentlicht','Vorschlag lesen','Der Prototyp','Excel herunterladen'],
     ['Publicado','Leer la propuesta','El prototipo','Descargar el Excel'],
     ['Publicado','Ler a proposta','O protótipo','Descarregar o Excel'],
     ['Опубликовано','Читать предложение','Прототип','Скачать Excel'],
     ['منشور','اقرأ المقترح','النموذج الأولي','تنزيل ملف Excel'],
     ['已发布','阅读提案','原型','下载 Excel'],
     ['公開済み','提案を読む','プロトタイプ','Excel をダウンロード'],
     ['게시됨','제안 읽기','프로토타입','Excel 다운로드']]
IT=['Pubblicato','Leggi la proposta','Il prototipo',"Scarica l'Excel"]
LI=['To discuss it, we meet on ','Pour en discuter, on se retrouve sur ','Zum Diskutieren treffen wir uns auf ','Para hablar de ello, nos vemos en ','Para discutir, encontramo-nos no ','Обсудить можно в ','للنقاش، نلتقي على ','欢迎在 ','議論は ','논의는 ']
LE=['.','.','.','.','.','.','.',' 上讨论。',' で。',' 에서 합니다.']
V=json.load(open(B+'/src/voci.json',encoding='utf-8'))
old={o['k'] for o in V}; nid=max(int(o['id'][1:]) for o in V)
src=[];tr={l:[] for l in L}
for o in N:
  if o['k'] in old: continue
  if o['k'] in T: vals=T[o['k']]
  elif o['m']=='html' and 'dati-pubblici.html' in o['h']:
    vals=[]
    for b in BTN:
      h=o['h']
      for a,c in zip(IT,b): h=h.replace('>'+a+'<','>'+c+'<')
      vals.append(h)
  elif o['m']=='html' and o['h'].startswith('Per discuterne, ci si ritrova su <a'):
    a=o['h'][len('Per discuterne, ci si ritrova su '):]
    a=a[:-1] if a.endswith('.') else a
    vals=[LI[i]+a+LE[i] for i in range(len(L))]
  else: continue
  nid+=1; o=dict(o); o['id']='v%04d'%nid; V.append(o); old.add(o['k'])
  src.append(o['id']+'\t'+o['h'])
  for i,l in enumerate(L): tr[l].append(o['id']+'\t'+vals[i])
json.dump(V,open(B+'/src/voci.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
open(B+'/src/p25.txt','w',encoding='utf-8').write('\n'.join(src)+'\n')
for l in L: open(B+'/tr/%s/p25.txt'%l,'w',encoding='utf-8').write('\n'.join(tr[l])+'\n')
print(len(src),'voci nuove')
