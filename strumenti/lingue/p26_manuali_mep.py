# Pacchetto p26: le schede dei manuali «Manuale famiglie Revit 2026» (#man-pro-01), «Checklist BIM-MEP» (#man-pro-06)
# e «Guida alla progettazione antincendio» (#man-pro-09), pubblicate in revisione 148.
# Uso: python3 strumenti/lingue/p26_manuali_mep.py <estratto.json>  (estratto = uscita di extract.js)
import json,sys,os
B=os.path.dirname(os.path.abspath(__file__))
L=['en','fr','de','es','pt','ru','ar','zh','ja','ko']
N=json.load(open(sys.argv[1],encoding='utf-8'))
T={
"Non è un tutorial ma un metodo: l'ordine delle decisioni per costruire una famiglia che regge nel tempo, nel progetto e nello scambio dei dati.":[
 "Not a tutorial but a method: the order of decisions for building a family that holds up over time, in the project and in data exchange.",
 "Ce n'est pas un tutoriel mais une méthode : l'ordre des décisions pour construire une famille qui tient dans le temps, dans le projet et dans l'échange des données.",
 "Kein Tutorial, sondern eine Methode: die Reihenfolge der Entscheidungen, um eine Familie zu bauen, die auf Dauer hält, im Projekt und beim Datenaustausch.",
 "No es un tutorial sino un método: el orden de las decisiones para construir una familia que resista en el tiempo, en el proyecto y en el intercambio de datos.",
 "Não é um tutorial, mas um método: a ordem das decisões para construir uma família que resista no tempo, no projeto e na troca de dados.",
 "Это не урок, а метод: порядок решений, чтобы построить семейство, которое выдержит время, проект и обмен данными.",
 "ليس درسًا تعليميًا بل منهجًا: ترتيب القرارات لبناء عائلة تصمد مع الوقت، في المشروع وفي تبادل البيانات.",
 "这不是教程，而是一种方法：按什么顺序做决定，才能建出经得起时间、项目和数据交换考验的族。",
 "チュートリアルではなく方法論です。時間がたっても、プロジェクトでもデータ交換でも崩れないファミリを作るための、判断の順序。",
 "튜토리얼이 아니라 방법입니다. 시간이 지나도, 프로젝트와 데이터 교환에서도 버티는 패밀리를 만들기 위한 결정의 순서."],
"Classe di famiglia e host, template, piani di riferimento e vincoli, parametri condivisi, rappresentazione, connettori MEP e IFC, fino alla prova e alla pubblicazione in libreria. Con un aiuto interattivo per scegliere l'host e la checklist finale da spuntare.":[
 "Family class and host, template, reference planes and constraints, shared parameters, representation, MEP connectors and IFC, up to testing and publishing in the library. With an interactive helper to choose the host and a final checklist to tick off.",
 "Classe de famille et hôte, gabarit, plans de référence et contraintes, paramètres partagés, représentation, connecteurs MEP et IFC, jusqu'au test et à la publication en bibliothèque. Avec une aide interactive pour choisir l'hôte et la checklist finale à cocher.",
 "Familienklasse und Host, Vorlage, Referenzebenen und Abhängigkeiten, gemeinsam genutzte Parameter, Darstellung, MEP-Anschlüsse und IFC, bis zum Test und zur Veröffentlichung in der Bibliothek. Mit einer interaktiven Hilfe zur Wahl des Hosts und einer Checkliste zum Abhaken.",
 "Clase de familia y anfitrión, plantilla, planos de referencia y restricciones, parámetros compartidos, representación, conectores MEP e IFC, hasta la prueba y la publicación en la biblioteca. Con una ayuda interactiva para elegir el anfitrión y la checklist final para marcar.",
 "Classe de família e hospedeiro, modelo, planos de referência e restrições, parâmetros partilhados, representação, conectores MEP e IFC, até ao teste e à publicação na biblioteca. Com uma ajuda interativa para escolher o hospedeiro e a checklist final para assinalar.",
 "Класс семейства и основа, шаблон, опорные плоскости и зависимости, общие параметры, отображение, соединители MEP и IFC — вплоть до проверки и публикации в библиотеке. С интерактивной подсказкой для выбора основы и итоговым чек-листом.",
 "فئة العائلة والمضيف، والقالب، والمستويات المرجعية والقيود، والمعاملات المشتركة، والتمثيل، وموصلات MEP وIFC، وصولًا إلى الاختبار والنشر في المكتبة. مع مساعد تفاعلي لاختيار المضيف وقائمة تحقق نهائية.",
 "族类别与主体、样板、参照平面与约束、共享参数、表达、MEP 连接件与 IFC，直到测试并发布到族库。附有选择主体的交互助手和可勾选的最终检查清单。",
 "ファミリの種類とホスト、テンプレート、参照面と拘束、共有パラメータ、表現、MEP コネクタと IFC、テストとライブラリへの公開まで。ホストを選ぶ対話型ヘルプと、チェックできる最終チェックリスト付き。",
 "패밀리 종류와 호스트, 템플릿, 참조 평면과 구속, 공유 매개변수, 표현, MEP 커넥터와 IFC, 테스트와 라이브러리 게시까지. 호스트를 고르는 대화형 도우미와 체크할 수 있는 최종 체크리스트 포함."],
"Dalle domande da fare prima di aprire Revit fino alla consegna: un'unica checklist per i progetti di impianti, da spuntare online.":[
 "From the questions to ask before opening Revit to delivery: a single checklist for building services projects, to tick off online.",
 "Des questions à poser avant d'ouvrir Revit jusqu'à la livraison : une checklist unique pour les projets d'installations techniques, à cocher en ligne.",
 "Von den Fragen vor dem Öffnen von Revit bis zur Abgabe: eine einzige Checkliste für TGA-Projekte, online abzuhaken.",
 "Desde las preguntas antes de abrir Revit hasta la entrega: una única checklist para proyectos de instalaciones, para marcar en línea.",
 "Das perguntas a fazer antes de abrir o Revit até à entrega: uma única checklist para projetos de instalações, para assinalar online.",
 "От вопросов перед запуском Revit до сдачи: единый чек-лист для проектов инженерных систем, который можно отмечать онлайн.",
 "من الأسئلة قبل فتح Revit حتى التسليم: قائمة تحقق واحدة لمشاريع الأنظمة الهندسية، يمكن التأشير عليها عبر الإنترنت.",
 "从打开 Revit 之前要问的问题到交付：一份用于机电项目的统一检查清单，可在线勾选。",
 "Revit を開く前の質問から納品まで：設備プロジェクトのための一つのチェックリスト。オンラインでチェックできます。",
 "Revit을 열기 전에 할 질문부터 납품까지: 설비 프로젝트를 위한 하나의 체크리스트, 온라인으로 체크할 수 있습니다."],
"Come si prepara un template MEP con gli standard del proprio studio, passo per passo, prima di iniziare un nuovo modello; poi i controlli per disciplina (avvio e coordinamento, elettrico, climatizzazione, idrico-sanitario, antincendio) e la revisione di fine progetto. Le spunte restano salvate nel browser.":[
 "How to prepare an MEP template with your office's standards, step by step, before starting a new model; then the checks by discipline (start-up and coordination, electrical, HVAC, plumbing, fire protection) and the end-of-project review. The ticks stay saved in the browser.",
 "Comment préparer un gabarit MEP avec les standards de son bureau, pas à pas, avant de commencer un nouveau modèle ; puis les contrôles par discipline (démarrage et coordination, électricité, CVC, plomberie, incendie) et la revue de fin de projet. Les coches restent enregistrées dans le navigateur.",
 "Wie man Schritt für Schritt eine MEP-Vorlage mit den Standards des eigenen Büros vorbereitet, bevor ein neues Modell beginnt; dann die Prüfungen je Gewerk (Start und Koordination, Elektro, Lüftung und Klima, Sanitär, Brandschutz) und die Rückschau am Projektende. Die Häkchen bleiben im Browser gespeichert.",
 "Cómo preparar una plantilla MEP con los estándares del propio estudio, paso a paso, antes de empezar un nuevo modelo; después los controles por disciplina (inicio y coordinación, electricidad, climatización, fontanería, protección contra incendios) y la revisión de fin de proyecto. Las marcas quedan guardadas en el navegador.",
 "Como preparar um modelo MEP com os padrões do próprio gabinete, passo a passo, antes de iniciar um novo modelo; depois os controlos por disciplina (arranque e coordenação, eletricidade, climatização, águas e esgotos, incêndio) e a revisão de fim de projeto. As marcações ficam guardadas no navegador.",
 "Как шаг за шагом подготовить шаблон MEP со стандартами своего бюро до начала новой модели; затем проверки по разделам (запуск и координация, электрика, ОВиК, водоснабжение и канализация, пожарная защита) и разбор в конце проекта. Отметки сохраняются в браузере.",
 "كيف يُجهَّز قالب MEP بمعايير المكتب خطوة بخطوة قبل بدء نموذج جديد؛ ثم الفحوص حسب التخصص (البدء والتنسيق، الكهرباء، التكييف، الصحي، الحريق) ومراجعة نهاية المشروع. تبقى العلامات محفوظة في المتصفح.",
 "如何在开始新模型之前，按步骤用本事务所的标准准备 MEP 样板；然后是各专业的检查（启动与协调、电气、暖通、给排水、消防）以及项目结束时的回顾。勾选状态保存在浏览器中。",
 "新しいモデルを始める前に、事務所の標準で MEP テンプレートを準備する手順。続いて分野ごとの確認（立ち上げと調整、電気、空調、給排水、防火）とプロジェクト終了時の振り返り。チェックはブラウザに保存されます。",
 "새 모델을 시작하기 전에 사무소의 표준으로 MEP 템플릿을 단계별로 준비하는 방법; 이어서 분야별 점검(착수와 조정, 전기, 공조, 위생, 소방)과 프로젝트 종료 회고. 체크 표시는 브라우저에 저장됩니다."],
"Un percorso guidato: si sceglie il committente, la destinazione d'uso e le dimensioni dell'edificio, e la guida dice quali regole si applicano.":[
 "A guided path: you choose the client, the building's use and size, and the guide tells you which rules apply.",
 "Un parcours guidé : on choisit le maître d'ouvrage, l'usage et la taille du bâtiment, et le guide indique les règles applicables.",
 "Ein geführter Weg: Man wählt Bauherrn, Nutzung und Größe des Gebäudes, und der Leitfaden sagt, welche Regeln gelten.",
 "Un recorrido guiado: se elige el cliente, el uso y el tamaño del edificio, y la guía indica qué normas se aplican.",
 "Um percurso guiado: escolhe-se o dono de obra, o uso e a dimensão do edifício, e o guia diz que regras se aplicam.",
 "Пошаговый маршрут: выбираете заказчика, назначение и размеры здания, и руководство показывает, какие правила применяются.",
 "مسار موجَّه: تختار الجهة المالكة واستخدام المبنى وحجمه، فيبيّن الدليل القواعد المطبقة.",
 "引导式流程：选择业主、建筑用途和规模，指南告诉你适用哪些规定。",
 "ガイド付きの手順：発注者、建物の用途と規模を選ぶと、適用される規則がわかります。",
 "단계별 안내: 발주처, 건물의 용도와 규모를 고르면 어떤 규정이 적용되는지 알려 줍니다."],
"Poi, locale per locale, gli accorgimenti da prevedere; le vie d'esodo, i materiali e che cosa vuol dire davvero REI; infine la mappa del workflow che lega l'antincendio agli impianti e ai dati del modello, dai parametri all'IFC. Segue le norme italiane, con quelle provinciali dell'Alto Adige, e dà il riferimento preciso per ogni valore.":[
 "Then, room by room, the measures to provide; escape routes, materials and what REI really means; finally the workflow map linking fire safety to building services and model data, from parameters to IFC. It follows Italian regulations, together with the provincial rules of South Tyrol, and gives the exact reference for every value.",
 "Puis, local par local, les dispositions à prévoir ; les voies d'évacuation, les matériaux et ce que veut vraiment dire REI ; enfin la carte du workflow qui relie la sécurité incendie aux installations et aux données du modèle, des paramètres à l'IFC. Il suit les normes italiennes, avec celles de la province du Haut-Adige, et donne la référence précise de chaque valeur.",
 "Dann Raum für Raum die vorzusehenden Maßnahmen; Rettungswege, Baustoffe und was REI wirklich bedeutet; schließlich die Workflow-Karte, die Brandschutz mit der TGA und den Modelldaten verbindet, von den Parametern bis zum IFC. Er folgt den italienischen Vorschriften, ergänzt um die Landesbestimmungen Südtirols, und nennt für jeden Wert die genaue Quelle.",
 "Después, local por local, las medidas que prever; las vías de evacuación, los materiales y qué significa de verdad REI; por último el mapa del flujo de trabajo que une la protección contra incendios con las instalaciones y los datos del modelo, de los parámetros al IFC. Sigue la normativa italiana, con la provincial del Alto Adigio, y da la referencia exacta de cada valor.",
 "Depois, compartimento a compartimento, as medidas a prever; as vias de evacuação, os materiais e o que significa realmente REI; por fim o mapa do fluxo de trabalho que liga a segurança contra incêndio às instalações e aos dados do modelo, dos parâmetros ao IFC. Segue as normas italianas, com as provinciais do Alto Ádige, e dá a referência exata de cada valor.",
 "Затем, помещение за помещением, необходимые меры; пути эвакуации, материалы и что на самом деле означает REI; наконец, карта рабочего процесса, связывающая пожарную безопасность с инженерными системами и данными модели, от параметров до IFC. Руководство следует итальянским нормам вместе с провинциальными правилами Южного Тироля и даёт точную ссылку для каждого значения.",
 "ثم، غرفةً غرفة، التدابير الواجب توفيرها؛ ومسارات الإخلاء والمواد وما يعنيه REI فعلًا؛ وأخيرًا خريطة سير العمل التي تربط السلامة من الحريق بالأنظمة الهندسية وبيانات النموذج، من المعاملات إلى IFC. يتبع الدليل القواعد الإيطالية، مع القواعد الإقليمية لجنوب تيرول، ويذكر المرجع الدقيق لكل قيمة.",
 "然后逐个房间说明需要采取的措施；疏散通道、材料以及 REI 的真正含义；最后是把消防与机电系统、模型数据（从参数到 IFC）联系起来的工作流程图。依据意大利法规及南蒂罗尔的省级规定，每个数值都有确切出处。",
 "続いて部屋ごとに講じるべき対策、避難経路、材料、REI の本当の意味。最後に、防火を設備とモデルのデータ（パラメータから IFC まで）に結びつけるワークフローの図。イタリアの法規と南チロルの州規則に基づき、すべての数値に正確な出典を示します。",
 "이어서 실별로 갖춰야 할 조치, 피난 경로, 재료, REI의 진짜 의미. 마지막으로 소방을 설비와 모델 데이터(매개변수부터 IFC까지)에 연결하는 워크플로 지도. 이탈리아 규정과 남티롤 주 규정을 따르며, 모든 값의 정확한 근거를 제시합니다."],
}
BTN={'famiglie-revit.html':(['Pubblicato','Leggi online',"Scegli l'host"],[['Published','Read online','Choose the host'],['Publié','Lire en ligne',"Choisir l'hôte"],['Veröffentlicht','Online lesen','Host wählen'],['Publicado','Leer en línea','Elegir el anfitrión'],['Publicado','Ler online','Escolher o hospedeiro'],['Опубликовано','Читать онлайн','Выбрать основу'],['منشور','اقرأ عبر الإنترنت','اختر المضيف'],['已发布','在线阅读','选择主体'],['公開済み','オンラインで読む','ホストを選ぶ'],['게시됨','온라인으로 읽기','호스트 고르기']]),
 'checklist-bim-mep.html':(['Pubblicato','Leggi online','Il template MEP','La checklist'],[['Published','Read online','The MEP template','The checklist'],['Publié','Lire en ligne','Le gabarit MEP','La checklist'],['Veröffentlicht','Online lesen','Die MEP-Vorlage','Die Checkliste'],['Publicado','Leer en línea','La plantilla MEP','La checklist'],['Publicado','Ler online','O modelo MEP','A checklist'],['Опубликовано','Читать онлайн','Шаблон MEP','Чек-лист'],['منشور','اقرأ عبر الإنترنت','قالب MEP','قائمة التحقق'],['已发布','在线阅读','MEP 样板','检查清单'],['公開済み','オンラインで読む','MEP テンプレート','チェックリスト'],['게시됨','온라인으로 읽기','MEP 템플릿','체크리스트']]),
 'antincendio.html':(['Pubblicato','Apri la guida','La mappa del workflow'],[['Published','Open the guide','The workflow map'],['Publié','Ouvrir le guide','La carte du workflow'],['Veröffentlicht','Leitfaden öffnen','Die Workflow-Karte'],['Publicado','Abrir la guía','El mapa del flujo de trabajo'],['Publicado','Abrir o guia','O mapa do fluxo de trabalho'],['Опубликовано','Открыть руководство','Карта рабочего процесса'],['منشور','افتح الدليل','خريطة سير العمل'],['已发布','打开指南','工作流程图'],['公開済み','ガイドを開く','ワークフローの図'],['게시됨','안내 열기','워크플로 지도']])}
V=json.load(open(B+'/src/voci.json',encoding='utf-8'))
old={o['k'] for o in V}; nid=max(int(o['id'][1:]) for o in V)
src=[];tr={l:[] for l in L}
for o in N:
  if o['k'] in old: continue
  if o['k'] in T: vals=T[o['k']]
  elif o['m']=='html':
    f=[k for k in BTN if 'manuali/'+k+'"' in o['h']]
    if not f: continue
    it,tl=BTN[f[0]]; vals=[]
    for b in tl:
      h=o['h']
      for a,c in zip(it,b): h=h.replace('>'+a+'<','>'+c+'<')
      vals.append(h)
  else: continue
  nid+=1; o=dict(o); o['id']='v%04d'%nid; V.append(o); old.add(o['k'])
  src.append(o['id']+'\t'+o['h'])
  for i,l in enumerate(L): tr[l].append(o['id']+'\t'+vals[i])
json.dump(V,open(B+'/src/voci.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
open(B+'/src/p26.txt','w',encoding='utf-8').write('\n'.join(src)+'\n')
for l in L: open(B+'/tr/%s/p26.txt'%l,'w',encoding='utf-8').write('\n'.join(tr[l])+'\n')
print(len(src),'voci nuove')
