# Pacchetto p23: la scheda «La libreria IFC 4.3» (#man-pro-13).
# Uso: python3 strumenti/lingue/p23_libreria_ifc.py <estratto.json>  (estratto = uscita di extract.js)
import json,sys,os
B=os.path.dirname(os.path.abspath(__file__))
L=['en','fr','de','es','pt','ru','ar','zh','ja','ko']
N=json.load(open(sys.argv[1],encoding='utf-8'))
T={
'La libreria IFC 4.3':['The IFC 4.3 library','La bibliothèque IFC 4.3','Die IFC-4.3-Bibliothek','La biblioteca IFC 4.3','A biblioteca IFC 4.3','Библиотека IFC 4.3','مكتبة IFC 4.3','IFC 4.3 库','IFC 4.3 ライブラリ','IFC 4.3 라이브러리'],
'Tutte le classi IFC degli oggetti di un modello, con i loro PredefinedType, spiegate in italiano e in inglese.':[
 'All the IFC classes for the objects of a model, with their PredefinedType values, explained in Italian and English.',
 "Toutes les classes IFC des objets d'une maquette, avec leurs PredefinedType, expliquées en italien et en anglais.",
 'Alle IFC-Klassen für die Objekte eines Modells, mit ihren PredefinedType-Werten, auf Italienisch und Englisch erklärt.',
 'Todas las clases IFC de los objetos de un modelo, con sus PredefinedType, explicadas en italiano y en inglés.',
 'Todas as classes IFC dos objetos de um modelo, com os seus PredefinedType, explicadas em italiano e em inglês.',
 'Все классы IFC для объектов модели с их значениями PredefinedType, с пояснениями на итальянском и английском.',
 'جميع فئات IFC لعناصر النموذج، مع قيم PredefinedType الخاصة بها، مشروحة بالإيطالية والإنجليزية.',
 '模型中各类对象的全部 IFC 类及其 PredefinedType，附意大利语和英语说明。',
 'モデルのオブジェクトに使うすべての IFC クラスとその PredefinedType を、イタリア語と英語で解説。',
 '모델 객체에 쓰이는 모든 IFC 클래스와 그 PredefinedType을 이탈리아어와 영어로 설명합니다.'],
'214 classi e 1422 combinazioni di classe e sottotipo dallo schema IFC 4.3 ADD2 (ISO 16739-1:2024), con la gerarchia, le classi deprecate e i valori pronti per IfcExportAs e IfcExportType. Si esplorano come una mappa mentale apribile e si scaricano gratis in Excel o in JSON.':[
 '214 classes and 1422 class and subtype combinations from the IFC 4.3 ADD2 schema (ISO 16739-1:2024), with the hierarchy, deprecated classes and values ready for IfcExportAs and IfcExportType. Explore them as an expandable mind map and download them free in Excel or JSON.',
 "214 classes et 1422 combinaisons de classe et de sous-type issues du schéma IFC 4.3 ADD2 (ISO 16739-1:2024), avec la hiérarchie, les classes obsolètes et les valeurs prêtes pour IfcExportAs et IfcExportType. On les explore comme une carte mentale dépliable et on les télécharge gratuitement en Excel ou en JSON.",
 '214 Klassen und 1422 Kombinationen aus Klasse und Untertyp aus dem Schema IFC 4.3 ADD2 (ISO 16739-1:2024), mit Hierarchie, veralteten Klassen und Werten für IfcExportAs und IfcExportType. Als aufklappbare Mindmap zu erkunden und kostenlos als Excel oder JSON herunterzuladen.',
 '214 clases y 1422 combinaciones de clase y subtipo del esquema IFC 4.3 ADD2 (ISO 16739-1:2024), con la jerarquía, las clases obsoletas y los valores listos para IfcExportAs e IfcExportType. Se exploran como un mapa mental desplegable y se descargan gratis en Excel o JSON.',
 '214 classes e 1422 combinações de classe e subtipo do esquema IFC 4.3 ADD2 (ISO 16739-1:2024), com a hierarquia, as classes obsoletas e os valores prontos para IfcExportAs e IfcExportType. Exploram-se como um mapa mental expansível e descarregam-se gratuitamente em Excel ou JSON.',
 '214 классов и 1422 сочетания класса и подтипа из схемы IFC 4.3 ADD2 (ISO 16739-1:2024), с иерархией, устаревшими классами и готовыми значениями для IfcExportAs и IfcExportType. Их можно изучать в виде раскрывающейся интеллект-карты и бесплатно скачать в Excel или JSON.',
 '214 فئة و1422 تركيبة من الفئة والنوع الفرعي من مخطط IFC 4.3 ADD2 (ISO 16739-1:2024)، مع التسلسل الهرمي والفئات المهملة وقيم جاهزة لـ IfcExportAs وIfcExportType. تُستكشف كخريطة ذهنية قابلة للفتح وتُنزَّل مجانًا بصيغة Excel أو JSON.',
 '来自 IFC 4.3 ADD2 架构（ISO 16739-1:2024）的 214 个类和 1422 个类与子类型组合，包含层级、已弃用的类以及可直接用于 IfcExportAs 和 IfcExportType 的值。可以像可展开的思维导图一样浏览，并免费下载 Excel 或 JSON 文件。',
 'IFC 4.3 ADD2 スキーマ（ISO 16739-1:2024）の 214 クラスと、クラスとサブタイプの 1422 の組み合わせ。階層、非推奨クラス、IfcExportAs・IfcExportType にそのまま使える値付き。展開できるマインドマップで探索でき、Excel または JSON で無料ダウンロードできます。',
 'IFC 4.3 ADD2 스키마(ISO 16739-1:2024)의 214개 클래스와 클래스·하위 유형 조합 1422개. 계층 구조, 사용 중단된 클래스, IfcExportAs와 IfcExportType에 바로 쓸 수 있는 값을 담았습니다. 펼칠 수 있는 마인드맵으로 살펴보고 Excel이나 JSON으로 무료로 내려받을 수 있습니다.'],
'6 pubblicati · 13 voci':['6 published · 13 entries','6 publiés · 13 entrées','6 veröffentlicht · 13 Einträge','6 publicados · 13 entradas','6 publicados · 13 entradas','6 опубликовано · 13 пунктов','6 منشورة · 13 بندًا','已发布 6 份 · 共 13 项','公開 6 件 · 全 13 件','공개 6건 · 전체 13건'],
'Cerca una classe: muro, damper, IfcSlab…':['Search a class: wall, damper, IfcSlab…','Rechercher une classe : mur, registre, IfcSlab…','Klasse suchen: Wand, Klappe, IfcSlab…','Busca una clase: muro, compuerta, IfcSlab…','Pesquisar uma classe: parede, registo, IfcSlab…','Найти класс: стена, клапан, IfcSlab…','ابحث عن فئة: جدار، مخمد، IfcSlab…','搜索类：墙、风阀、IfcSlab…','クラスを検索：壁、ダンパー、IfcSlab…','클래스 검색: 벽, 댐퍼, IfcSlab…'],
'Cerca nella libreria IFC':['Search the IFC library','Rechercher dans la bibliothèque IFC','In der IFC-Bibliothek suchen','Buscar en la biblioteca IFC','Pesquisar na biblioteca IFC','Поиск в библиотеке IFC','ابحث في مكتبة IFC','在 IFC 库中搜索','IFC ライブラリを検索','IFC 라이브러리에서 검색'],
}
BTN=[['Published','Open the library','Mind map','Download the Excel file'],['Publié','Ouvrir la bibliothèque','Carte mentale',"Télécharger l'Excel"],['Veröffentlicht','Bibliothek öffnen','Mindmap','Excel herunterladen'],['Publicado','Abrir la biblioteca','Mapa mental','Descargar el Excel'],['Publicado','Abrir a biblioteca','Mapa mental','Descarregar o Excel'],['Опубликовано','Открыть библиотеку','Интеллект-карта','Скачать Excel'],['منشور','افتح المكتبة','الخريطة الذهنية','نزّل ملف Excel'],['已发布','打开库','思维导图','下载 Excel'],['公開済み','ライブラリを開く','マインドマップ','Excel をダウンロード'],['게시됨','라이브러리 열기','마인드맵','Excel 내려받기']]
IT=['Pubblicato','Apri la libreria','Mappa mentale',"Scarica l'Excel"]
V=json.load(open(B+'/src/voci.json',encoding='utf-8'))
old={o['k'] for o in V}; nid=max(int(o['id'][1:]) for o in V)
src=[];tr={l:[] for l in L}
for o in N:
  if o['k'] in old: continue
  if o['k'] in T: vals=T[o['k']]
  elif o['m']=='html' and 'libreria-ifc.html' in o['h']:
    vals=[]
    for b in BTN:
      h=o['h']
      for a,c in zip(IT,b): h=h.replace('>'+a+'<','>'+c+'<')
      vals.append(h)
  else: continue
  nid+=1; o=dict(o); o['id']='v%04d'%nid; V.append(o); old.add(o['k'])
  src.append(o['id']+'\t'+o['h'])
  for i,l in enumerate(L): tr[l].append(o['id']+'\t'+vals[i])
json.dump(V,open(B+'/src/voci.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
open(B+'/src/p23.txt','w',encoding='utf-8').write('\n'.join(src)+'\n')
for l in L: open(B+'/tr/%s/p23.txt'%l,'w',encoding='utf-8').write('\n'.join(tr[l])+'\n')
print(len(src),'voci nuove')
