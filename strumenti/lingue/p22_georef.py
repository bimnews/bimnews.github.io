# Pacchetto p22: la scheda del manuale «Georeferenziazione BIM tra software diversi» (#man-pro-12).
# Uso: python3 strumenti/lingue/p22_georef.py <estratto.json>  (estratto = uscita di extract.js)
import json,sys,os
B=os.path.dirname(os.path.abspath(__file__))
L=['en','fr','de','es','pt','ru','ar','zh','ja','ko']
N=json.load(open(sys.argv[1],encoding='utf-8'))
T={
'Georeferenziazione BIM tra software diversi':['BIM georeferencing across different software','Géoréférencement BIM entre logiciels différents','BIM-Georeferenzierung zwischen verschiedenen Programmen','Georreferenciación BIM entre software distintos','Georreferenciação BIM entre softwares diferentes','Геопривязка BIM между разными программами','الإسناد الجغرافي في BIM بين برامج مختلفة','不同软件之间的 BIM 地理配准','異なるソフトウェア間の BIM ジオリファレンス','서로 다른 소프트웨어 간 BIM 지오레퍼런싱'],
'Perché in federazione un modello finisce a chilometri dagli altri: coordinate, rotazione, unità di misura, nord di rete e nord geografico, caso per caso tra Revit, Archicad, Allplan e IFC 2x3, 4 e 4.3, con un caso reale di errore 1:1000.':[
 'Why a model ends up kilometres away from the others in federation: coordinates, rotation, units of measurement, grid north and true north, case by case across Revit, Archicad, Allplan and IFC 2x3, 4 and 4.3, with a real case of a 1:1000 error.',
 "Pourquoi, lors de la fédération, un modèle se retrouve à des kilomètres des autres : coordonnées, rotation, unités de mesure, nord du quadrillage et nord géographique, cas par cas entre Revit, Archicad, Allplan et IFC 2x3, 4 et 4.3, avec un cas réel d'erreur 1:1000.",
 'Warum ein Modell in der Federation kilometerweit von den anderen entfernt landet: Koordinaten, Drehung, Maßeinheiten, Gitternord und geografisch Nord, Fall für Fall zwischen Revit, Archicad, Allplan und IFC 2x3, 4 und 4.3, mit einem realen Fall eines Fehlers 1:1000.',
 'Por qué, en la federación, un modelo acaba a kilómetros de los demás: coordenadas, rotación, unidades de medida, norte de cuadrícula y norte geográfico, caso por caso entre Revit, Archicad, Allplan e IFC 2x3, 4 y 4.3, con un caso real de error 1:1000.',
 'Porque, na federação, um modelo acaba a quilómetros dos outros: coordenadas, rotação, unidades de medida, norte da quadrícula e norte geográfico, caso a caso entre Revit, Archicad, Allplan e IFC 2x3, 4 e 4.3, com um caso real de erro 1:1000.',
 'Почему при федерации модель оказывается в километрах от остальных: координаты, поворот, единицы измерения, сеточный и географический север, случай за случаем для Revit, Archicad, Allplan и IFC 2x3, 4 и 4.3, с реальным примером ошибки 1:1000.',
 'لماذا ينتهي نموذج على بُعد كيلومترات من النماذج الأخرى عند الدمج: الإحداثيات والدوران ووحدات القياس والشمال الشبكي والشمال الجغرافي، حالة بحالة بين Revit وArchicad وAllplan وIFC 2x3 و4 و4.3، مع حالة حقيقية لخطأ بنسبة 1:1000.',
 '为什么在模型整合时，一个模型会落在离其他模型几公里远的地方：坐标、旋转、计量单位、坐标网北与真北，逐一分析 Revit、Archicad、Allplan 以及 IFC 2x3、4 和 4.3，并附一个 1:1000 误差的真实案例。',
 '統合（フェデレーション）の際、なぜモデルが他のモデルから何キロも離れた位置に現れるのか。座標、回転、単位、図北と真北を、Revit、Archicad、Allplan、IFC 2x3・4・4.3 についてケースごとに解説し、1:1000 の誤差の実例も紹介します。',
 '통합(페더레이션) 과정에서 왜 한 모델이 다른 모델들과 수 킬로미터 떨어진 곳에 나타나는지: 좌표, 회전, 측정 단위, 도북과 진북을 Revit, Archicad, Allplan, IFC 2x3·4·4.3별로 사례마다 설명하고, 1:1000 오류의 실제 사례도 다룹니다.'],
'Con un convertitore gratuito: dai valori di un software a quelli di un altro, il controllo con punti noti e la diagnosi degli spostamenti. Si usa online o si scarica: è un unico file che funziona anche senza internet.':[
 'With a free converter: from the values of one software to those of another, a check with known points and the diagnosis of displacements. Use it online or download it: it is a single file that also works without internet.',
 "Avec un convertisseur gratuit : des valeurs d'un logiciel à celles d'un autre, le contrôle par points connus et le diagnostic des décalages. Il s'utilise en ligne ou se télécharge : c'est un fichier unique qui fonctionne aussi sans internet.",
 'Mit einem kostenlosen Umrechner: von den Werten eines Programms zu denen eines anderen, Kontrolle mit bekannten Punkten und Diagnose von Verschiebungen. Online nutzbar oder zum Herunterladen: eine einzige Datei, die auch ohne Internet funktioniert.',
 'Con un conversor gratuito: de los valores de un software a los de otro, el control con puntos conocidos y el diagnóstico de los desplazamientos. Se usa en línea o se descarga: es un único archivo que funciona también sin internet.',
 'Com um conversor gratuito: dos valores de um software para os de outro, o controlo com pontos conhecidos e o diagnóstico de deslocamentos. Usa-se online ou descarrega-se: é um único ficheiro que funciona também sem internet.',
 'С бесплатным конвертером: от значений одной программы к значениям другой, проверка по известным точкам и диагностика смещений. Работает онлайн или скачивается: это один файл, который работает и без интернета.',
 'مع محوّل مجاني: من قيم برنامج إلى قيم برنامج آخر، والتحقق بنقاط معروفة، وتشخيص الإزاحات. يُستخدم عبر الإنترنت أو يُنزَّل: إنه ملف واحد يعمل أيضًا دون إنترنت.',
 '附免费转换器：把一个软件的数值换算成另一个软件的数值，用已知点进行检查，并诊断偏移。可在线使用，也可下载：只有一个文件，离线也能运行。',
 '無料の変換ツール付き：あるソフトウェアの値を別のソフトウェアの値に変換し、既知点で確認し、位置ずれを診断します。オンラインで使うことも、ダウンロードすることもできます。インターネットなしでも動く単一のファイルです。',
 '무료 변환기 포함: 한 소프트웨어의 값을 다른 소프트웨어의 값으로 변환하고, 알려진 점으로 검사하며, 위치 이동을 진단합니다. 온라인으로 쓰거나 내려받을 수 있습니다. 인터넷 없이도 작동하는 단일 파일입니다.'],
'5 pubblicati · 12 voci':['5 published · 12 entries','5 publiés · 12 entrées','5 veröffentlicht · 12 Einträge','5 publicados · 12 entradas','5 publicados · 12 entradas','5 опубликовано · 12 пунктов','5 منشورة · 12 بندًا','已发布 5 份 · 共 12 项','公開 5 · 全 12 項目','게시 5 · 전체 12개'],
}
BTN=[['Published','Read online','Open the converter','Download the converter'],['Publié','Lire en ligne','Ouvrir le convertisseur','Télécharger le convertisseur'],['Veröffentlicht','Online lesen','Umrechner öffnen','Umrechner herunterladen'],['Publicado','Leer en línea','Abrir el conversor','Descargar el conversor'],['Publicado','Ler online','Abrir o conversor','Descarregar o conversor'],['Опубликовано','Читать онлайн','Открыть конвертер','Скачать конвертер'],['منشور','اقرأ على الإنترنت','افتح المحوّل','نزّل المحوّل'],['已发布','在线阅读','打开转换器','下载转换器'],['公開済み','オンラインで読む','変換ツールを開く','変換ツールをダウンロード'],['게시됨','온라인으로 읽기','변환기 열기','변환기 내려받기']]
IT=['Pubblicato','Leggi online','Apri il convertitore','Scarica il convertitore']
V=json.load(open(B+'/src/voci.json',encoding='utf-8'))
old={o['k'] for o in V}; nid=max(int(o['id'][1:]) for o in V)
src=[];tr={l:[] for l in L}
for o in N:
  if o['k'] in old: continue
  if o['k'] in T: vals=T[o['k']]
  elif o['m']=='html' and 'convertitore-georeferenziazione' in o['h']:
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
open(B+'/src/p22.txt','w',encoding='utf-8').write('\n'.join(src)+'\n')
for l in L: open(B+'/tr/%s/p22.txt'%l,'w',encoding='utf-8').write('\n'.join(tr[l])+'\n')
print(len(src),'voci nuove')
