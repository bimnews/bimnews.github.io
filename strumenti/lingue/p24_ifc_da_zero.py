# Pacchetto p24: la scheda «Un IFC scritto a mano» (#man-pro-14) e il link aggiornato in «Il mondo oltre noi».
# Uso: python3 strumenti/lingue/p24_ifc_da_zero.py <estratto.json>  (estratto = uscita di extract.js)
import json,sys,os,re,glob
B=os.path.dirname(os.path.abspath(__file__))
L=['en','fr','de','es','pt','ru','ar','zh','ja','ko']
N=json.load(open(sys.argv[1],encoding='utf-8'))
TIT=['A hand-written IFC','Un IFC écrit à la main','Eine von Hand geschriebene IFC-Datei','Un IFC escrito a mano','Um IFC escrito à mão','IFC, написанный вручную','ملف IFC مكتوب يدويًا','手写的 IFC','手書きの IFC','손으로 쓴 IFC']
T={
'Un IFC scritto a mano':TIT,
'Una casetta di due piani scritta riga per riga in un file di testo, senza nessun software BIM, che si apre in Revit e passa la validazione.':[
 'A small two-storey house written line by line in a text file, without any BIM software, that opens in Revit and passes validation.',
 "Une petite maison de deux étages écrite ligne par ligne dans un fichier texte, sans aucun logiciel BIM, qui s'ouvre dans Revit et passe la validation.",
 'Ein kleines zweigeschossiges Haus, Zeile für Zeile in einer Textdatei geschrieben, ohne BIM-Software, das sich in Revit öffnen lässt und die Validierung besteht.',
 'Una casita de dos plantas escrita línea a línea en un archivo de texto, sin ningún software BIM, que se abre en Revit y supera la validación.',
 'Uma pequena casa de dois pisos escrita linha a linha num ficheiro de texto, sem qualquer software BIM, que abre no Revit e passa a validação.',
 'Небольшой двухэтажный дом, написанный строка за строкой в текстовом файле без какого-либо BIM-софта; он открывается в Revit и проходит валидацию.',
 'منزل صغير من طابقين مكتوب سطرًا سطرًا في ملف نصي، من دون أي برنامج BIM، يُفتح في Revit ويجتاز التحقق.',
 '一栋两层小房子，在文本文件中逐行写成，不借助任何 BIM 软件，可在 Revit 中打开并通过校验。',
 'BIM ソフトを使わず、テキストファイルに1行ずつ書いた2階建ての小さな家。Revit で開け、検証にも合格します。',
 'BIM 소프트웨어 없이 텍스트 파일에 한 줄씩 쓴 2층 집. Revit에서 열리고 검증도 통과합니다.'],
"Il codice IFC4 spiegato pattern per pattern: unità, struttura spaziale, posizioni a catena, profili ed estrusioni, fori e serramenti, relazioni, proprietà e GlobalId. Con un modello 3D da girare, i riferimenti tra le righe da seguire con un clic e una tabella per capire dove cercare l'errore quando un modello arriva sbagliato.":[
 'The IFC4 code explained pattern by pattern: units, spatial structure, chained placements, profiles and extrusions, openings and windows, relationships, properties and GlobalId. With a 3D model to rotate, references between lines to follow with a click, and a table showing where to look when a model arrives wrong.',
 "Le code IFC4 expliqué motif par motif : unités, structure spatiale, positionnements en chaîne, profils et extrusions, ouvertures et menuiseries, relations, propriétés et GlobalId. Avec une maquette 3D à faire tourner, des références entre lignes à suivre d'un clic et un tableau pour savoir où chercher l'erreur quand une maquette arrive fausse.",
 'Der IFC4-Code Muster für Muster erklärt: Einheiten, räumliche Struktur, verkettete Platzierungen, Profile und Extrusionen, Öffnungen und Fenster, Beziehungen, Eigenschaften und GlobalId. Mit einem drehbaren 3D-Modell, Verweisen zwischen den Zeilen, denen man per Klick folgt, und einer Tabelle, wo man suchen muss, wenn ein Modell fehlerhaft ankommt.',
 'El código IFC4 explicado patrón por patrón: unidades, estructura espacial, posiciones encadenadas, perfiles y extrusiones, huecos y carpinterías, relaciones, propiedades y GlobalId. Con un modelo 3D para girar, referencias entre líneas que se siguen con un clic y una tabla para saber dónde buscar el error cuando un modelo llega mal.',
 'O código IFC4 explicado padrão a padrão: unidades, estrutura espacial, posicionamentos em cadeia, perfis e extrusões, vãos e caixilharias, relações, propriedades e GlobalId. Com um modelo 3D para rodar, referências entre linhas para seguir com um clique e uma tabela para saber onde procurar o erro quando um modelo chega errado.',
 'Код IFC4, разобранный по шаблонам: единицы, пространственная структура, цепочки размещений, профили и выдавливания, проёмы и окна, связи, свойства и GlobalId. С 3D-моделью, которую можно вращать, ссылками между строками, по которым можно перейти одним щелчком, и таблицей, где искать ошибку, если модель пришла неверной.',
 'شيفرة IFC4 مشروحة نمطًا بنمط: الوحدات، والبنية المكانية، والمواضع المتسلسلة، والمقاطع والبثق، والفتحات والنوافذ، والعلاقات، والخصائص وGlobalId. مع نموذج ثلاثي الأبعاد يمكن تدويره، ومراجع بين الأسطر تُتتبَّع بنقرة، وجدول يبيّن أين تبحث عن الخطأ عندما يصل نموذج خاطئ.',
 '逐个模式讲解 IFC4 代码：单位、空间结构、链式定位、轮廓与拉伸、洞口与门窗、关系、属性和 GlobalId。附可旋转的 3D 模型、点击即可追踪的行间引用，以及一张帮助查找模型出错位置的表格。',
 'IFC4 のコードをパターンごとに解説：単位、空間構造、連鎖する配置、プロファイルと押し出し、開口と建具、関係、プロパティ、GlobalId。回せる 3D モデル、クリックでたどれる行どうしの参照、モデルがおかしく届いたときにどこを見ればよいかの表付き。',
 'IFC4 코드를 패턴별로 설명합니다: 단위, 공간 구조, 연쇄 배치, 프로파일과 돌출, 개구부와 창호, 관계, 속성, GlobalId. 돌려 볼 수 있는 3D 모델, 클릭으로 따라가는 줄 사이 참조, 모델이 잘못 도착했을 때 어디를 봐야 하는지 알려 주는 표가 있습니다.'],
'7 pubblicati · 14 voci':['7 published · 14 entries','7 publiés · 14 entrées','7 veröffentlicht · 14 Einträge','7 publicados · 14 entradas','7 publicados · 14 entradas','7 опубликовано · 14 пунктов','7 منشورة · 14 بندًا','已发布 7 份 · 共 14 项','公開済み 7 · 全 14 項目','7개 공개 · 총 14개'],
'6 voci':['6 entries','6 entrées','6 Einträge','6 entradas','6 entradas','6 пунктов','6 بنود','共 6 项','全 6 項目','총 6개'],
'12 voci':['12 entries','12 entrées','12 Einträge','12 entradas','12 entradas','12 пунктов','12 بندًا','共 12 项','全 12 項目','총 12개'],
'2 voci':['2 entries','2 entrées','2 Einträge','2 entradas','2 entradas','2 пункта','بندان','共 2 项','全 2 項目','총 2개'],
'1 voce':['1 entry','1 entrée','1 Eintrag','1 entrada','1 entrada','1 пункт','بند واحد','共 1 项','全 1 項目','총 1개'],
}
BTN=[['Published','Read the article','3D model','Download casetta.ifc'],['Publié',"Lire l'article",'Maquette 3D','Télécharger casetta.ifc'],['Veröffentlicht','Artikel lesen','3D-Modell','casetta.ifc herunterladen'],['Publicado','Leer el artículo','Modelo 3D','Descargar casetta.ifc'],['Publicado','Ler o artigo','Modelo 3D','Descarregar casetta.ifc'],['Опубликовано','Читать статью','3D-модель','Скачать casetta.ifc'],['منشور','اقرأ المقال','النموذج ثلاثي الأبعاد','نزّل casetta.ifc'],['已发布','阅读文章','3D 模型','下载 casetta.ifc'],['公開済み','記事を読む','3D モデル','casetta.ifc をダウンロード'],['공개됨','글 읽기','3D 모델','casetta.ifc 내려받기']]
IT=['Pubblicato',"Leggi l'articolo",'Modello 3D','Scarica casetta.ifc']
# vecchie traduzioni del paragrafo «Il mondo oltre noi» (v0556): si cambia solo il link
OLD={}
for l in L:
  for fn in glob.glob(B+'/tr/%s/*.txt'%l):
    for r in open(fn,encoding='utf-8'):
      if r.startswith('v0556\t'): OLD[l]=r.rstrip('\n').split('\t',1)[1]
V=json.load(open(B+'/src/voci.json',encoding='utf-8'))
old={o['k'] for o in V}; nid=max(int(o['id'][1:]) for o in V)
src=[];tr={l:[] for l in L}
for o in N:
  if o['k'] in old: continue
  if o['k'] in T: vals=T[o['k']]
  elif o['m']=='html' and 'manuali/ifc-da-zero.html' in o['h']:
    vals=[]
    for b in BTN:
      h=o['h']
      for a,c in zip(IT,b): h=h.replace('>'+a+'<','>'+c+'<')
      vals.append(h)
  elif o['m']=='html' and 'data-goto-art="man-pro-14"' in o['h']:
    vals=[re.sub(r'<a href="#wip" data-goto-art="art-ifc-zero">[^<]*</a>','<a href="#studio" data-goto-art="man-pro-14">'+TIT[i]+' →</a>',OLD[l]) for i,l in enumerate(L)]
  else: continue
  nid+=1; o=dict(o); o['id']='v%04d'%nid; V.append(o); old.add(o['k'])
  src.append(o['id']+'\t'+o['h'])
  for i,l in enumerate(L): tr[l].append(o['id']+'\t'+vals[i])
json.dump(V,open(B+'/src/voci.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
open(B+'/src/p24.txt','w',encoding='utf-8').write('\n'.join(src)+'\n')
for l in L: open(B+'/tr/%s/p24.txt'%l,'w',encoding='utf-8').write('\n'.join(tr[l])+'\n')
print(len(src),'voci nuove')
