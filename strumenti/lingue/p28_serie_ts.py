# Pacchetto p28: le schede degli articoli 2–11 della serie «L'impianto termosanitario, passo per passo» (#mep-ts-02 … #mep-ts-11).
# Uso: python3 strumenti/lingue/p28_serie_ts.py <estratto.json>  (estratto = uscita di extract.js)
import json,sys,os
B=os.path.dirname(os.path.abspath(__file__))
L=['en','fr','de','es','pt','ru','ar','zh','ja','ko']
N=json.load(open(sys.argv[1],encoding='utf-8'))
PRE=["The heating and plumbing system, step by step","L'installation thermique et sanitaire, pas à pas","Heizung und Sanitär, Schritt für Schritt","La instalación térmica y sanitaria, paso a paso","A instalação térmica e sanitária, passo a passo","Отопление и водоснабжение шаг за шагом","نظام التدفئة والصحي خطوة بخطوة","供暖与给排水系统，一步一步","暖房・給排水設備をステップごとに","난방·위생 설비, 단계별로"]
TIT={
2:["La linea d'azione",["The course of action","La ligne d'action","Die Strategie","La línea de acción","A linha de ação","План действий","خطة العمل","行动路线","方針","실행 방침"]],
3:["La generazione",["Heat generation","La production de chaleur","Die Wärmeerzeugung","La generación","A produção de calor","Теплогенерация","توليد الحرارة","热源","熱源","열원"]],
4:["Accumulo e separazione",["Storage and separation","Stockage et séparation","Speicher und hydraulische Trennung","Acumulación y separación","Acumulação e separação","Аккумуляция и гидравлическое разделение","التخزين والفصل","蓄热与分隔","蓄熱と分離","축열과 분리"]],
5:["La distribuzione",["Distribution","La distribution","Die Verteilung","La distribución","A distribuição","Распределение","التوزيع","输配","配管と搬送","배관과 반송"]],
6:["L'emissione",["Heat emission","L'émission","Die Wärmeabgabe","La emisión","A emissão","Теплоотдача","بث الحرارة","末端散热","放熱","방열"]],
7:["La regolazione",["Controls","La régulation","Die Regelung","La regulación","A regulação","Регулирование","التحكم","调节控制","制御","제어"]],
8:["L'acqua calda sanitaria",["Domestic hot water","L'eau chaude sanitaire","Das Trinkwarmwasser","El agua caliente sanitaria","A água quente sanitária","Горячее водоснабжение","الماء الساخن المنزلي","生活热水","給湯","급탕"]],
9:["La rete idrica",["The water supply network","Le réseau d'eau","Das Trinkwassernetz","La red de agua","A rede de água","Водопроводная сеть","شبكة المياه","给水管网","給水管網","급수 배관망"]],
10:["Gli scarichi",["Drainage","Les évacuations","Die Entwässerung","Los desagües","Os esgotos","Канализация","الصرف","排水","排水","배수"]],
11:["Nel modello",["In the model","Dans la maquette","Im Modell","En el modelo","No modelo","В модели","في النموذج","在模型中","モデルの中で","모델 속으로"]],
}
TXT={
"Dal fabbisogno alle scelte: centrale o autonomo, acqua o aria, e soprattutto la temperatura a cui lavora l'impianto. Con il regolo delle temperature e il COP della pompa di calore.":[
"From needs to choices: central or individual, water or air, and above all the temperature the system works at. With the temperature slide rule and the heat pump COP.",
"Des besoins aux choix : centralisé ou individuel, eau ou air, et surtout la température de fonctionnement de l'installation. Avec la règle des températures et le COP de la pompe à chaleur.",
"Vom Bedarf zu den Entscheidungen: zentral oder dezentral, Wasser oder Luft und vor allem die Temperatur, mit der die Anlage arbeitet. Mit dem Temperaturschieber und der Leistungszahl der Wärmepumpe.",
"De las necesidades a las decisiones: central o individual, agua o aire y, sobre todo, la temperatura de trabajo de la instalación. Con la regla de temperaturas y el COP de la bomba de calor.",
"Das necessidades às escolhas: central ou individual, água ou ar e, sobretudo, a temperatura de trabalho da instalação. Com a régua das temperaturas e o COP da bomba de calor.",
"От потребностей к решениям: централизованная или индивидуальная система, вода или воздух и прежде всего рабочая температура. С «линейкой температур» и COP теплового насоса.",
"من الاحتياجات إلى القرارات: مركزي أو فردي، ماء أو هواء، وقبل كل شيء درجة حرارة تشغيل النظام. مع مسطرة درجات الحرارة ومعامل أداء المضخة الحرارية.",
"从需求到决策：集中还是分户，水还是空气，最重要的是系统的工作温度。附温度标尺和热泵的 COP。",
"必要量から選択へ：中央式か個別式か、水か空気か、そして何より設備の運転温度。温度の目盛りとヒートポンプの COP 付き。",
"필요량에서 선택으로: 중앙식 또는 개별식, 물 또는 공기, 무엇보다 설비의 운전 온도. 온도 눈금자와 히트펌프 COP 포함."],
"Pompa di calore, caldaia a condensazione, teleriscaldamento: come lavorano e come si sceglie la potenza alla temperatura di progetto. Con il bilancio della pompa di calore da provare.":[
"Heat pump, condensing boiler, district heating: how they work and how to size the output at the design temperature. With the heat pump balance to try.",
"Pompe à chaleur, chaudière à condensation, réseau de chaleur : comment ils fonctionnent et comment choisir la puissance à la température de base. Avec le bilan de la pompe à chaleur à essayer.",
"Wärmepumpe, Brennwertkessel, Fernwärme: wie sie arbeiten und wie man die Leistung bei der Auslegungstemperatur wählt. Mit der Bilanz der Wärmepumpe zum Ausprobieren.",
"Bomba de calor, caldera de condensación, calefacción urbana: cómo funcionan y cómo se elige la potencia a la temperatura de proyecto. Con el balance de la bomba de calor para probar.",
"Bomba de calor, caldeira de condensação, aquecimento urbano: como funcionam e como se escolhe a potência à temperatura de projeto. Com o balanço da bomba de calor para experimentar.",
"Тепловой насос, конденсационный котёл, централизованное теплоснабжение: как они работают и как выбрать мощность при расчётной температуре. С интерактивным балансом теплового насоса.",
"المضخة الحرارية، والمرجل التكثيفي، والتدفئة المركزية للأحياء: كيف تعمل وكيف تُختار القدرة عند درجة حرارة التصميم. مع ميزان المضخة الحرارية للتجربة.",
"热泵、冷凝锅炉、区域供热：它们如何工作，如何按设计温度选择功率。附可操作的热泵能量平衡图。",
"ヒートポンプ、潜熱回収ボイラー、地域熱供給：その仕組みと、設計温度での出力の選び方。試せるヒートポンプの収支図付き。",
"히트펌프, 콘덴싱 보일러, 지역난방: 작동 방식과 설계 온도에서 출력을 고르는 법. 직접 해 볼 수 있는 히트펌프 수지 그림 포함."],
"Il volume d'acqua che protegge la macchina, il separatore tra i circuiti e il vaso di espansione, con la sua formula e la figura del vaso.":[
"The water volume that protects the machine, the separator between circuits and the expansion vessel, with its formula and the vessel figure.",
"Le volume d'eau qui protège la machine, la bouteille de découplage entre les circuits et le vase d'expansion, avec sa formule et la figure du vase.",
"Das Wasservolumen, das die Maschine schützt, die hydraulische Weiche zwischen den Kreisen und das Ausdehnungsgefäß, mit seiner Formel und der Abbildung des Gefäßes.",
"El volumen de agua que protege la máquina, el separador entre circuitos y el vaso de expansión, con su fórmula y la figura del vaso.",
"O volume de água que protege a máquina, o separador entre circuitos e o vaso de expansão, com a sua fórmula e a figura do vaso.",
"Объём воды, который защищает машину, гидрострелка между контурами и расширительный бак — с формулой и рисунком бака.",
"حجم الماء الذي يحمي الآلة، والفاصل بين الدوائر، وخزان التمدد، مع معادلته وشكل الخزان.",
"保护机组的水容量、回路之间的分离器和膨胀罐，附计算公式和膨胀罐图示。",
"機械を守る水量、回路間の分離器、膨張タンク。計算式とタンクの図付き。",
"기계를 보호하는 수량, 회로 사이의 분리기, 팽창탱크. 계산식과 팽창탱크 그림 포함."],
"Dalla potenza alla portata, i diametri, la pompa e il circuito che si incontrano nel punto di lavoro, il bilanciamento.":[
"From output to flow rate, pipe sizes, the pump and the circuit meeting at the operating point, balancing.",
"De la puissance au débit, les diamètres, la pompe et le circuit qui se rencontrent au point de fonctionnement, l'équilibrage.",
"Von der Leistung zum Volumenstrom, die Durchmesser, Pumpe und Netz, die sich im Betriebspunkt treffen, der hydraulische Abgleich.",
"De la potencia al caudal, los diámetros, la bomba y el circuito que se encuentran en el punto de trabajo, el equilibrado.",
"Da potência ao caudal, os diâmetros, a bomba e o circuito que se encontram no ponto de funcionamento, o equilíbrio.",
"От мощности к расходу, диаметры, насос и сеть, которые встречаются в рабочей точке, балансировка.",
"من القدرة إلى معدل التدفق، والأقطار، والمضخة والدائرة اللتان تلتقيان عند نقطة التشغيل، والموازنة.",
"从功率到流量、管径、在工作点相遇的水泵与管路，以及水力平衡。",
"出力から流量へ、管径、運転点で出会うポンプと回路、そしてバランス調整。",
"출력에서 유량으로, 관경, 운전점에서 만나는 펌프와 회로, 그리고 밸런싱."],
"Pavimento radiante, radiatori, ventilconvettori: la legge di ogni terminale e la temperatura dell'acqua che serve. Con il pavimento che scalda.":[
"Underfloor heating, radiators, fan coils: the law of each emitter and the water temperature it needs. With the heating floor to try.",
"Plancher chauffant, radiateurs, ventilo-convecteurs : la loi de chaque émetteur et la température d'eau nécessaire. Avec le plancher qui chauffe.",
"Fußbodenheizung, Heizkörper, Gebläsekonvektoren: das Gesetz jedes Heizflächentyps und die nötige Wassertemperatur. Mit dem heizenden Fußboden.",
"Suelo radiante, radiadores, fancoils: la ley de cada emisor y la temperatura de agua que necesita. Con el suelo que calienta.",
"Piso radiante, radiadores, ventiloconvetores: a lei de cada emissor e a temperatura da água necessária. Com o piso que aquece.",
"Тёплый пол, радиаторы, фанкойлы: закон каждого отопительного прибора и нужная температура воды. С интерактивным тёплым полом.",
"التدفئة الأرضية، والمشعات، ووحدات الملف والمروحة: قانون كل وحدة بث ودرجة حرارة الماء اللازمة. مع الأرضية التي تدفئ.",
"地暖、散热器、风机盘管：每种末端的规律及所需的水温。附地暖图示。",
"床暖房、ラジエーター、ファンコイル：各放熱器の法則と必要な水温。床暖房の図付き。",
"바닥 난방, 라디에이터, 팬코일: 각 방열기의 법칙과 필요한 수온. 바닥 난방 그림 포함."],
"Curva climatica, regolazione per ambiente, orari e ventilazione sulla presenza: quanto calore, quando e dove.":[
"Weather compensation curve, room-by-room control, schedules and demand-controlled ventilation: how much heat, when and where.",
"Courbe de chauffe, régulation pièce par pièce, horaires et ventilation selon l'occupation : combien de chaleur, quand et où.",
"Heizkurve, Einzelraumregelung, Zeitprogramme und bedarfsgeführte Lüftung: wie viel Wärme, wann und wo.",
"Curva climática, regulación por estancia, horarios y ventilación según ocupación: cuánto calor, cuándo y dónde.",
"Curva climática, regulação por espaço, horários e ventilação por ocupação: quanto calor, quando e onde.",
"Погодозависимая кривая, регулирование по помещениям, расписания и вентиляция по присутствию: сколько тепла, когда и где.",
"منحنى التعويض المناخي، والتحكم في كل غرفة، والجداول الزمنية، والتهوية حسب الإشغال: كم من الحرارة، ومتى، وأين.",
"气候补偿曲线、分室控制、时间程序和按需通风：多少热量、何时、何处。",
"外気温補償カーブ、室ごとの制御、スケジュール、在室に応じた換気：どれだけの熱を、いつ、どこへ。",
"외기 보상 곡선, 실별 제어, 운전 일정, 재실 기반 환기: 얼마만큼의 열을, 언제, 어디에."],
"Accumulo, ricircolo e produzione istantanea, con le temperature delle linee guida sulla legionellosi e i loro effetti su una pompa di calore.":[
"Storage, recirculation and instantaneous production, with the temperatures of the Italian Legionella guidelines and their effect on a heat pump.",
"Stockage, bouclage et production instantanée, avec les températures des lignes directrices italiennes sur la légionellose et leurs effets sur une pompe à chaleur.",
"Speicher, Zirkulation und Durchflussprinzip, mit den Temperaturen der italienischen Legionellen-Leitlinien und ihren Folgen für eine Wärmepumpe.",
"Acumulación, recirculación y producción instantánea, con las temperaturas de las directrices italianas sobre la legionelosis y sus efectos en una bomba de calor.",
"Acumulação, recirculação e produção instantânea, com as temperaturas das diretrizes italianas sobre a legionelose e os seus efeitos numa bomba de calor.",
"Накопление, рециркуляция и мгновенный нагрев, с температурами из итальянских рекомендаций по легионеллёзу и их влиянием на тепловой насос.",
"التخزين وإعادة التدوير والإنتاج الفوري، مع درجات الحرارة الواردة في الإرشادات الإيطالية بشأن داء الفيالقة وأثرها على المضخة الحرارية.",
"蓄热、循环和即热式制备，以及意大利军团菌防控指南中的温度要求及其对热泵的影响。",
"貯湯、循環、瞬間式の給湯。イタリアのレジオネラ症ガイドラインの温度と、それがヒートポンプに与える影響。",
"저탕, 순환, 순간식 급탕. 이탈리아 레지오넬라증 지침의 온도와 그것이 히트펌프에 미치는 영향."],
"Pressioni dall'allaccio al rubinetto più alto, portate contemporanee, riduttori, pressurizzazione e protezione dal riflusso.":[
"Pressures from the mains connection to the highest tap, simultaneous flow rates, pressure reducers, booster sets and backflow protection.",
"Pressions du branchement au robinet le plus haut, débits simultanés, réducteurs, surpresseurs et protection contre le retour d'eau.",
"Drücke vom Hausanschluss bis zur höchsten Zapfstelle, Spitzendurchfluss, Druckminderer, Druckerhöhung und Rückflussverhinderung.",
"Presiones desde la acometida hasta el grifo más alto, caudales simultáneos, reductores, grupos de presión y protección contra el retorno.",
"Pressões desde a ligação à rede até à torneira mais alta, caudais simultâneos, redutores, grupos de pressurização e proteção contra o refluxo.",
"Давление от ввода до самого высокого крана, одновременные расходы, редукторы, повысительные установки и защита от обратного потока.",
"الضغوط من نقطة التوصيل إلى أعلى صنبور، والتدفقات المتزامنة، ومخفضات الضغط، ومجموعات رفع الضغط، والحماية من الارتداد.",
"从接口到最高水龙头的压力、同时流量、减压阀、增压设备和防回流保护。",
"引込みから最も高い蛇口までの圧力、同時使用流量、減圧弁、加圧ポンプ、逆流防止。",
"인입부에서 가장 높은 수전까지의 압력, 동시 사용 유량, 감압밸브, 가압 장치, 역류 방지."],
"Unità di scarico e portata di progetto secondo la UNI EN 12056-2, colonne, ventilazione e sifoni.":[
"Discharge units and design flow according to EN 12056-2, stacks, venting and traps.",
"Unités de décharge et débit de calcul selon la EN 12056-2, colonnes, ventilation et siphons.",
"Anschlusswerte und Bemessungsabfluss nach EN 12056-2, Fallleitungen, Lüftung und Geruchverschlüsse.",
"Unidades de descarga y caudal de proyecto según la EN 12056-2, bajantes, ventilación y sifones.",
"Unidades de descarga e caudal de projeto segundo a EN 12056-2, tubos de queda, ventilação e sifões.",
"Единицы стока и расчётный расход по EN 12056-2, стояки, вентиляция и сифоны.",
"وحدات التصريف والتدفق التصميمي وفق EN 12056-2، والأعمدة، والتهوية، والسيفونات.",
"按 EN 12056-2 的排水当量和设计流量、立管、通气与存水弯。",
"EN 12056-2 による排水単位と設計流量、立て管、通気、トラップ。",
"EN 12056-2에 따른 배수 단위와 설계 유량, 입상관, 통기, 트랩."],
"Classi IFC 4.3, tipi, Pset, sistemi e collegamenti: dove va ogni pezzo dell'impianto e ogni numero calcolato nella serie.":[
"IFC 4.3 classes, types, Psets, systems and connections: where each part of the system and each number calculated in the series belongs.",
"Classes IFC 4.3, types, Pset, systèmes et connexions : où va chaque élément de l'installation et chaque valeur calculée dans la série.",
"IFC-4.3-Klassen, Typen, Psets, Systeme und Verbindungen: wohin jedes Anlagenteil und jeder in der Serie berechnete Wert gehört.",
"Clases IFC 4.3, tipos, Pset, sistemas y conexiones: dónde va cada pieza de la instalación y cada número calculado en la serie.",
"Classes IFC 4.3, tipos, Pset, sistemas e ligações: onde vai cada peça da instalação e cada número calculado na série.",
"Классы IFC 4.3, типы, Pset, системы и соединения: где место каждой детали системы и каждого числа, рассчитанного в серии.",
"فئات IFC 4.3، والأنواع، ومجموعات الخصائص، والأنظمة، والوصلات: أين يوضع كل جزء من النظام وكل رقم حُسب في السلسلة.",
"IFC 4.3 的类、类型、Pset、系统和连接：系统中的每个部件、系列中计算的每个数字各归何处。",
"IFC 4.3 のクラス、タイプ、Pset、システム、接続：設備の各部品と連載で計算した各数値の置き場所。",
"IFC 4.3 클래스, 타입, Pset, 시스템, 연결: 설비의 각 부품과 연재에서 계산한 각 수치가 들어갈 자리."],
}
T=dict(TXT)
for n,(it,tr) in TIT.items():
  T["L'impianto termosanitario, passo per passo · %d · %s"%(n,it)]=["%s · %d · %s"%(PRE[i],n,tr[i]) for i in range(10)]
V=json.load(open(B+'/src/voci.json',encoding='utf-8'))
old={o['k'] for o in V}; nid=max(int(o['id'][1:]) for o in V)
src=[];tr={l:[] for l in L}
for o in N:
  if o['k'] in old or o['k'] not in T: continue
  vals=T[o['k']]
  nid+=1; o=dict(o); o['id']='v%04d'%nid; V.append(o); old.add(o['k'])
  src.append(o['id']+'\t'+o['h'])
  for i,l in enumerate(L): tr[l].append(o['id']+'\t'+vals[i])
json.dump(V,open(B+'/src/voci.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
open(B+'/src/p28.txt','w',encoding='utf-8').write('\n'.join(src)+'\n')
for l in L: open(B+'/tr/%s/p28.txt'%l,'w',encoding='utf-8').write('\n'.join(tr[l])+'\n')
print(len(src),'voci nuove')
