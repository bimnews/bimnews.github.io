# Pacchetto p27: la sottosezione «MEP» del curatore (#mep: Didattica ed Esempi) e la scheda della serie termosanitario (#mep-ts-01).
# Uso: python3 strumenti/lingue/p27_mep.py <estratto.json>  (estratto = uscita di extract.js)
import json,sys,os
B=os.path.dirname(os.path.abspath(__file__))
L=['en','fr','de','es','pt','ru','ar','zh','ja','ko']
N=json.load(open(sys.argv[1],encoding='utf-8'))
T={
"MEP":["MEP"]*10,
"Didattica":["Learning","Didactique","Didaktik","Didáctica","Didática","Обучение","تعليمي","教学","学ぶ","학습"],
"Esempi":["Examples","Exemples","Beispiele","Ejemplos","Exemplos","Примеры","أمثلة","示例","実例","예시"],
"L'impianto termosanitario, passo per passo":["The heating and plumbing system, step by step","L'installation thermique et sanitaire, pas à pas","Heizung und Sanitär, Schritt für Schritt","La instalación térmica y sanitaria, paso a paso","A instalação térmica e sanitária, passo a passo","Отопление и водоснабжение шаг за шагом","نظام التدفئة والصحي خطوة بخطوة","供暖与给排水系统，一步一步","暖房・給排水設備をステップごとに","난방·위생 설비, 단계별로"],
"Impianti spiegati passo per passo, ed esempi da usare":["Building services explained step by step, and examples to use","Les installations expliquées pas à pas, et des exemples à utiliser","Gebäudetechnik Schritt für Schritt erklärt, und Beispiele zum Anwenden","Instalaciones explicadas paso a paso, y ejemplos para usar","Instalações explicadas passo a passo, e exemplos para usar","Инженерные системы шаг за шагом и примеры для работы","الأنظمة الهندسية مشروحة خطوة بخطوة، وأمثلة للاستخدام","逐步讲解的建筑设备，以及可直接使用的示例","設備をステップごとに解説、そして使える実例","단계별로 설명한 설비와 바로 쓰는 예시"],
"Gli impianti degli edifici, meccanici, elettrici e idraulici (in inglese MEP: Mechanical, Electrical, Plumbing). Nella Didattica si spiega come funzionano, dal fabbisogno dell'edificio fino ai dati del modello BIM; negli Esempi ci sono guide e strumenti da usare nel lavoro.":[
 "Building services: mechanical, electrical and plumbing (MEP). The Learning part explains how they work, from the building's needs to the data in the BIM model; the Examples hold guides and tools to use at work.",
 "Les installations des bâtiments : mécaniques, électriques et hydrauliques (en anglais MEP : Mechanical, Electrical, Plumbing). La partie Didactique explique leur fonctionnement, des besoins du bâtiment jusqu'aux données de la maquette BIM ; les Exemples réunissent des guides et des outils pour le travail.",
 "Die technischen Anlagen von Gebäuden: Lüftung und Heizung, Elektro, Sanitär (auf Englisch MEP: Mechanical, Electrical, Plumbing). Die Didaktik erklärt, wie sie funktionieren, vom Bedarf des Gebäudes bis zu den Daten im BIM-Modell; die Beispiele enthalten Leitfäden und Werkzeuge für die Arbeit.",
 "Las instalaciones de los edificios: mecánicas, eléctricas y de fontanería (en inglés MEP: Mechanical, Electrical, Plumbing). La Didáctica explica cómo funcionan, desde las necesidades del edificio hasta los datos del modelo BIM; en los Ejemplos hay guías y herramientas para el trabajo.",
 "As instalações dos edifícios: mecânicas, elétricas e hidráulicas (em inglês MEP: Mechanical, Electrical, Plumbing). A Didática explica como funcionam, das necessidades do edifício até aos dados do modelo BIM; nos Exemplos há guias e ferramentas para o trabalho.",
 "Инженерные системы зданий: механические, электрические и сантехнические (по-английски MEP: Mechanical, Electrical, Plumbing). В разделе «Обучение» объясняется, как они работают, от потребностей здания до данных BIM-модели; в «Примерах» — руководства и инструменты для работы.",
 "الأنظمة الهندسية للمباني: الميكانيكية والكهربائية والصحية (بالإنجليزية MEP). يشرح القسم التعليمي كيف تعمل، من احتياجات المبنى حتى بيانات نموذج BIM؛ وفي الأمثلة أدلة وأدوات للعمل.",
 "建筑的设备系统：机械、电气和给排水（英文 MEP：Mechanical, Electrical, Plumbing）。“教学”部分讲解它们如何工作，从建筑的需求到 BIM 模型中的数据；“示例”部分提供工作中可用的指南和工具。",
 "建物の設備：機械・電気・給排水（英語で MEP：Mechanical, Electrical, Plumbing）。「学ぶ」では、建物の必要から BIM モデルのデータまで、その仕組みを説明します。「実例」には仕事で使えるガイドとツールがあります。",
 "건물의 설비: 기계, 전기, 위생(영어로 MEP: Mechanical, Electrical, Plumbing). 「학습」에서는 건물의 필요부터 BIM 모델의 데이터까지 설비가 어떻게 작동하는지 설명하고, 「예시」에는 실무에 쓰는 가이드와 도구가 있습니다."],
"Serie di articoli che spiegano un impianto passo per passo, con un esempio che continua da un articolo all'altro e figure interattive. Gli esempi sono generici e i numeri tondi: servono a capire i meccanismi, non sostituiscono il calcolo di un progetto vero.":[
 "Article series that explain a system step by step, with one example carried from article to article and interactive figures. The examples are generic and the numbers round: they help understand the mechanisms and do not replace the calculation of a real project.",
 "Des séries d'articles qui expliquent une installation pas à pas, avec un exemple qui continue d'un article à l'autre et des figures interactives. Les exemples sont génériques et les chiffres ronds : ils servent à comprendre les mécanismes et ne remplacent pas le calcul d'un vrai projet.",
 "Artikelserien, die eine Anlage Schritt für Schritt erklären, mit einem Beispiel, das von Artikel zu Artikel weitergeht, und interaktiven Abbildungen. Die Beispiele sind allgemein und die Zahlen gerundet: Sie dienen dem Verständnis und ersetzen nicht die Berechnung eines echten Projekts.",
 "Series de artículos que explican una instalación paso a paso, con un ejemplo que continúa de un artículo a otro y figuras interactivas. Los ejemplos son genéricos y las cifras redondas: sirven para entender los mecanismos y no sustituyen el cálculo de un proyecto real.",
 "Séries de artigos que explicam uma instalação passo a passo, com um exemplo que continua de artigo para artigo e figuras interativas. Os exemplos são genéricos e os números redondos: servem para compreender os mecanismos e não substituem o cálculo de um projeto real.",
 "Серии статей, которые шаг за шагом объясняют инженерную систему, с примером, переходящим из статьи в статью, и интерактивными рисунками. Примеры условные, а числа округлены: они помогают понять принципы и не заменяют расчёт реального проекта.",
 "سلاسل مقالات تشرح النظام خطوة بخطوة، مع مثال يستمر من مقال إلى آخر وأشكال تفاعلية. الأمثلة عامة والأرقام مقرّبة: تساعد على فهم الآليات ولا تغني عن حساب مشروع حقيقي.",
 "逐步讲解一个系统的系列文章，同一个示例贯穿各篇，并配有交互式图示。示例是通用的，数字取整：用于理解原理，不能代替真实项目的计算。",
 "設備をステップごとに説明する連載。同じ例が記事から記事へ続き、インタラクティブな図が付きます。例は一般的なもので数値は丸めてあります。仕組みを理解するためのもので、実際のプロジェクトの計算の代わりにはなりません。",
 "설비를 단계별로 설명하는 연재 기사로, 하나의 예시가 기사에서 기사로 이어지고 대화형 그림이 함께 있습니다. 예시는 일반적이고 숫자는 반올림했습니다. 원리를 이해하기 위한 것이며 실제 프로젝트의 계산을 대신하지 않습니다."],
"L'impianto termosanitario, passo per passo · 1 · Il fabbisogno":["The heating and plumbing system, step by step · 1 · The needs","L'installation thermique et sanitaire, pas à pas · 1 · Les besoins","Heizung und Sanitär, Schritt für Schritt · 1 · Der Bedarf","La instalación térmica y sanitaria, paso a paso · 1 · Las necesidades","A instalação térmica e sanitária, passo a passo · 1 · As necessidades","Отопление и водоснабжение шаг за шагом · 1 · Потребности","نظام التدفئة والصحي خطوة بخطوة · 1 · الاحتياجات","供暖与给排水系统，一步一步 · 1 · 需求","暖房・給排水設備をステップごとに · 1 · 必要量","난방·위생 설비, 단계별로 · 1 · 필요량"],
"Prima di scegliere un impianto si capisce di che cosa ha bisogno l'edificio: calore d'inverno, aria, acqua calda e acqua, potenza ed energia.":[
 "Before choosing a system, you work out what the building needs: heat in winter, air, hot water and water, power and energy.",
 "Avant de choisir une installation, on comprend ce dont le bâtiment a besoin : chaleur en hiver, air, eau chaude et eau, puissance et énergie.",
 "Bevor man eine Anlage wählt, klärt man, was das Gebäude braucht: Wärme im Winter, Luft, Warmwasser und Wasser, Leistung und Energie.",
 "Antes de elegir una instalación se entiende qué necesita el edificio: calor en invierno, aire, agua caliente y agua, potencia y energía.",
 "Antes de escolher uma instalação percebe-se do que o edifício precisa: calor no inverno, ar, água quente e água, potência e energia.",
 "Прежде чем выбрать систему, нужно понять, что требуется зданию: тепло зимой, воздух, горячая вода и вода, мощность и энергия.",
 "قبل اختيار النظام يُفهم ما يحتاجه المبنى: الحرارة في الشتاء، والهواء، والماء الساخن والماء، والقدرة والطاقة.",
 "在选择系统之前，先弄清建筑需要什么：冬季的热量、空气、热水和用水、功率和能量。",
 "設備を選ぶ前に、建物が何を必要としているかを把握します。冬の熱、空気、給湯と給水、出力とエネルギー。",
 "설비를 고르기 전에 건물이 무엇을 필요로 하는지 파악합니다. 겨울의 열, 공기, 온수와 물, 출력과 에너지."],
"Un'aula di esempio calcolata passo per passo, con le norme di riferimento, mostra che in una scuola ben isolata il fabbisogno di calore lo decide l'aria più delle pareti. Con una figura interattiva da provare: si cambia la temperatura esterna e si accende o si spegne il recupero di calore.":[
 "An example classroom, calculated step by step with the reference standards, shows that in a well-insulated school the heat demand is set by the air more than by the walls. With an interactive figure to try: change the outdoor temperature and switch heat recovery on or off.",
 "Une salle de classe d'exemple, calculée pas à pas avec les normes de référence, montre que dans une école bien isolée le besoin de chaleur dépend davantage de l'air que des parois. Avec une figure interactive à essayer : on change la température extérieure et on active ou désactive la récupération de chaleur.",
 "Ein Beispiel-Klassenzimmer, Schritt für Schritt mit den maßgebenden Normen berechnet, zeigt: In einer gut gedämmten Schule bestimmt die Luft den Wärmebedarf stärker als die Wände. Mit einer interaktiven Abbildung zum Ausprobieren: Außentemperatur ändern, Wärmerückgewinnung ein- und ausschalten.",
 "Un aula de ejemplo, calculada paso a paso con las normas de referencia, muestra que en una escuela bien aislada la demanda de calor la decide el aire más que los muros. Con una figura interactiva para probar: se cambia la temperatura exterior y se activa o desactiva la recuperación de calor.",
 "Uma sala de aula de exemplo, calculada passo a passo com as normas de referência, mostra que numa escola bem isolada a necessidade de calor é decidida pelo ar mais do que pelas paredes. Com uma figura interativa para experimentar: muda-se a temperatura exterior e liga-se ou desliga-se a recuperação de calor.",
 "Учебный класс, рассчитанный шаг за шагом по нормам, показывает: в хорошо утеплённой школе потребность в тепле определяет воздух больше, чем стены. С интерактивным рисунком: можно менять наружную температуру и включать или выключать рекуперацию тепла.",
 "فصل دراسي مثالي محسوب خطوة بخطوة وفق المعايير المرجعية يبيّن أن الحاجة إلى الحرارة في مدرسة جيدة العزل يحددها الهواء أكثر من الجدران. مع شكل تفاعلي للتجربة: تغيير درجة الحرارة الخارجية وتشغيل استرداد الحرارة أو إيقافه.",
 "一间示例教室按参考标准逐步计算，表明在保温良好的学校里，热负荷更多由空气而不是墙体决定。附可操作的交互图：改变室外温度，开启或关闭热回收。",
 "参照規格に沿って一歩ずつ計算した例の教室が示すのは、断熱のよい学校では熱の必要量を決めるのは壁よりも空気だということです。試せるインタラクティブな図付き：外気温を変え、熱回収をオン・オフできます。",
 "기준 규격에 따라 단계별로 계산한 예시 교실은, 단열이 잘 된 학교에서는 열 수요를 벽보다 공기가 결정한다는 것을 보여 줍니다. 직접 해 볼 수 있는 대화형 그림 포함: 외기 온도를 바꾸고 열회수를 켜고 끌 수 있습니다."],
"Guide, checklist e strumenti per il lavoro sugli impianti, scritti con Claude, l'assistente di intelligenza artificiale di Anthropic.":[
 "Guides, checklists and tools for work on building services, written with Claude, Anthropic's artificial intelligence assistant.",
 "Guides, checklists et outils pour le travail sur les installations, écrits avec Claude, l'assistant d'intelligence artificielle d'Anthropic.",
 "Leitfäden, Checklisten und Werkzeuge für die Arbeit an der Gebäudetechnik, geschrieben mit Claude, dem KI-Assistenten von Anthropic.",
 "Guías, checklists y herramientas para el trabajo en instalaciones, escritas con Claude, el asistente de inteligencia artificial de Anthropic.",
 "Guias, checklists e ferramentas para o trabalho em instalações, escritos com Claude, o assistente de inteligência artificial da Anthropic.",
 "Руководства, чек-листы и инструменты для работы с инженерными системами, написанные с Claude, ИИ-ассистентом компании Anthropic.",
 "أدلة وقوائم تحقق وأدوات للعمل على الأنظمة الهندسية، كُتبت مع Claude، مساعد الذكاء الاصطناعي من Anthropic.",
 "关于设备工作的指南、检查清单和工具，与 Anthropic 的人工智能助手 Claude 一起编写。",
 "設備の仕事のためのガイド、チェックリスト、ツール。Anthropic の AI アシスタント Claude と一緒に書きました。",
 "설비 업무를 위한 가이드, 체크리스트, 도구로, Anthropic의 인공지능 어시스턴트 Claude와 함께 썼습니다."],
"Checklist, progettazione elettrica, antincendio":["Checklist, electrical design, fire safety","Checklist, conception électrique, incendie","Checkliste, Elektroplanung, Brandschutz","Checklist, diseño eléctrico, incendios","Checklist, projeto elétrico, incêndio","Чек-лист, электропроектирование, пожарная безопасность","قائمة تحقق، تصميم كهربائي، الحريق","检查清单、电气设计、消防","チェックリスト、電気設計、防火","체크리스트, 전기 설계, 소방"],
}
IT=['Pubblicato',"Leggi l'articolo",'La figura']
BT=[['Published','Read the article','The figure'],['Publié',"Lire l'article",'La figure'],['Veröffentlicht','Artikel lesen','Die Abbildung'],['Publicado','Leer el artículo','La figura'],['Publicado','Ler o artigo','A figura'],['Опубликовано','Читать статью','Рисунок'],['منشور','اقرأ المقال','الشكل'],['已发布','阅读文章','图示'],['公開済み','記事を読む','図'],['게시됨','기사 읽기','그림']]
V=json.load(open(B+'/src/voci.json',encoding='utf-8'))
old={o['k'] for o in V}; nid=max(int(o['id'][1:]) for o in V)
src=[];tr={l:[] for l in L}
for o in N:
  if o['k'] in old: continue
  if o['k'] in T: vals=T[o['k']]
  elif o['m']=='html' and 'termosanitario-01-fabbisogno.html' in o['h']:
    vals=[]
    for b in BT:
      h=o['h']
      for a,c in zip(IT,b): h=h.replace('>'+a+'<','>'+c+'<')
      vals.append(h)
  else: continue
  nid+=1; o=dict(o); o['id']='v%04d'%nid; V.append(o); old.add(o['k'])
  src.append(o['id']+'\t'+o['h'])
  for i,l in enumerate(L): tr[l].append(o['id']+'\t'+vals[i])
json.dump(V,open(B+'/src/voci.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
open(B+'/src/p27.txt','w',encoding='utf-8').write('\n'.join(src)+'\n')
for l in L: open(B+'/tr/%s/p27.txt'%l,'w',encoding='utf-8').write('\n'.join(tr[l])+'\n')
print(len(src),'voci nuove')
