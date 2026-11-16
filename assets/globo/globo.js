// Globo della home: proiezione ortografica su canvas, stelle sullo sfondo, rotazione lenta.
// Il clic su un paese passa alla mappa piatta (#ctrs) come fa la ricerca: filtri, numeri e regioni restano quelli.
window.GLOBO=function(wrap,world,citta){
"use strict";
var d3=window.d3,R=document.documentElement,$=function(i){return document.getElementById(i)};
var cv=document.createElement("canvas");cv.className="globe";cv.setAttribute("aria-hidden","true");wrap.appendChild(cv);
var tip=document.createElement("div");tip.className="globe-tip";tip.setAttribute("aria-hidden","true");wrap.appendChild(tip);
var cx=cv.getContext("2d"),W=0,H=0,DPR=1,r0=100;
var feats=topojson.feature(world,world.objects.countries).features.filter(function(f){return f.properties.it});
LIGHTS=citta||[];feats.forEach(function(f){f.b=d3.geoBounds(f);f.c=d3.geoCentroid(main(f))});
var sphere={type:"Sphere"},grat=d3.geoGraticule10();
var proj=d3.geoOrthographic().clipAngle(90).precision(.4),path=d3.geoPath(proj,cx);
var HOME=homeView(),TILT=-23.44,rot=[-HOME[0],-Math.max(-45,Math.min(62,HOME[1]+15)),TILT],k=1,t0=performance.now(),last=t0,hold=0,hover=null,mode="idle",fade=1,raf=0,mx=-1,my=-1;
// Via Lattea: fascia diagonale di luce diffusa, nucleo caldo, stelline fitte e polvere scura; disegnata una volta per dimensione
var MWON=/[?&]vialattea=1/.test(location.search)||window.VIALATTEA===true,MW=null;
function rnd(seed){return function(){seed=(seed*16807)%2147483647;return (seed-1)/2147483646}}
function mwBuild(){var c=document.createElement("canvas"),w=Math.max(1,Math.round(W*DPR)),h=Math.max(1,Math.round(H*DPR));c.width=w;c.height=h;
  var g=c.getContext("2d"),R1=rnd(7),L=Math.hypot(w,h),wide=w/h>1.6,ang=wide?-0.30:-0.42,cs=Math.cos(ang),sn=Math.sin(ang),cx0=w*.5,cy0=h*(wide?.56:.52),
    B=wide?Math.min(h*.30,L*.09):h*.10,UC=wide?L*.26:L*.12; // larghezza della fascia e posizione del nucleo (sul computer: a destra, fuori dalla ricerca)
  function pt(u,v){return[cx0+u*cs-v*sn,cy0+u*sn+v*cs]}
  g.globalCompositeOperation="lighter";
  // bagliore diffuso lungo la fascia, più intenso verso il nucleo
  var NG=wide?240:140;
  for(var i=0;i<NG;i++){var u=(R1()-.5)*L*1.1,v=((R1()+R1())/2-.5)*B*1.3,core=Math.exp(-Math.pow((u-UC)/(L*.32),2)),q=pt(u,v),rad=B*(.55+.9*R1())*(.7+core*.7);
    var gr=g.createRadialGradient(q[0],q[1],0,q[0],q[1],rad),warm=core>.45;
    gr.addColorStop(0,warm?"rgba(255,226,190,"+(.014+.022*core)+")":"rgba(170,195,255,"+(.016+.012*core)+")");gr.addColorStop(1,"rgba(0,0,0,0)");
    g.fillStyle=gr;g.beginPath();g.arc(q[0],q[1],rad,0,6.283);g.fill()}
  // nucleo: un alone caldo più marcato
  var qc=pt(UC,0),rc=B*(wide?2.2:1.6),gc=g.createRadialGradient(qc[0],qc[1],0,qc[0],qc[1],rc);
  gc.addColorStop(0,"rgba(255,224,180,.10)");gc.addColorStop(.5,"rgba(255,210,170,.035)");gc.addColorStop(1,"rgba(0,0,0,0)");g.fillStyle=gc;g.beginPath();g.arc(qc[0],qc[1],rc,0,6.283);g.fill();
  // stelline fitte, concentrate al centro della fascia
  var NS=Math.round((wide?5200:2600)*Math.min(1.6,Math.max(.7,w*h/(2560*1300))));
  for(i=0;i<NS;i++){var u2=(R1()-.5)*L*1.1,v2=((R1()+R1()+R1())/3-.5)*B*3.2,core2=Math.exp(-Math.pow((u2-UC)/(L*.28),2)),q2=pt(u2,v2);
    if(R1()>.5+.45*core2)continue;var br=R1();g.fillStyle=br>.97?"rgba(255,236,210,.95)":"rgba(230,238,255,"+(.2+.5*br)+")";var z=(br>.97?1.3:.35+R1()*.75)*DPR;g.fillRect(q2[0],q2[1],z,z)}
  // polvere scura: una banda sottile e irregolare lungo l'asse, più evidente vicino al nucleo
  g.globalCompositeOperation="source-over";
  for(i=0;i<(wide?220:110);i++){var u3=(R1()-.5)*L*.95,v3=Math.sin(u3/L*9)*B*.18+(R1()-.5)*B*.22,near=Math.exp(-Math.pow((u3-UC)/(L*.25),2)),q3=pt(u3,v3),r3=B*(.06+.14*R1());
    g.save();g.translate(q3[0],q3[1]);g.rotate(ang);g.scale(3.2,1);var gd=g.createRadialGradient(0,0,0,0,0,r3);gd.addColorStop(0,"rgba(4,6,12,"+(.07+.08*near)+")");gd.addColorStop(1,"rgba(4,6,12,0)");g.fillStyle=gd;g.beginPath();g.arc(0,0,r3,0,6.283);g.fill();g.restore()}
  return c}
var stars=[];for(var i=0;i<260;i++)stars.push({x:Math.random(),y:Math.random(),s:Math.random()*Math.random()*1.6+.25,p:Math.random()*6.3,v:.4+Math.random()*1.4});
// dove guarda il globo all'apertura: il fuso orario del browser (nessuna posizione chiesta né inviata)
function homeView(){var z="",lon;try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}
  lon=-new Date().getTimezoneOffset()/4;if(lon>180)lon-=360;
  var lat=/^Europe/.test(z)?47:/^Africa/.test(z)?5:/^Australia/.test(z)?-25:/^Pacific\/(Auckland|Chatham)/.test(z)?-40:/^Pacific/.test(z)?-12:/^Antarctica/.test(z)?-60:/^Atlantic\/(Reykjavik|Faroe)/.test(z)?60:/^Indian/.test(z)?-10:
    /^America\/(Sao_Paulo|Argentina|Buenos_Aires|Santiago|Lima|Bogota|La_Paz|Asuncion|Montevideo|Caracas|Guayaquil|Manaus|Recife|Fortaleza|Belem|Cuiaba|Bahia)/.test(z)?-15:/^America/.test(z)?38:/^Asia/.test(z)?30:20;
  if(/^Europe/.test(z))lon=Math.max(-5,Math.min(30,lon));return[lon,lat]}
// sole: punto subsolare dalla data e dall'ora (declinazione ed equazione del tempo, precisione circa mezzo grado)
var SUN=[0,0];function sun(){var d=new Date(),y0=Date.UTC(d.getUTCFullYear(),0,0),n=(d-y0)/864e5,B=2*Math.PI*(n-81)/365,
  eot=9.87*Math.sin(2*B)-7.53*Math.cos(B)-1.5*Math.sin(B),h=d.getUTCHours()+d.getUTCMinutes()/60+d.getUTCSeconds()/3600,
  dec=-23.44*Math.cos(2*Math.PI/365*(n+10)),lon=-15*(h-12+eot/60);lon=((lon+540)%360)-180;SUN=[lon,dec]}
sun();setInterval(sun,60000);
var LIGHTS;
function still(){return matchMedia("(prefers-reduced-motion: reduce)").matches}
function home(){return (R.dataset.view||"home")==="home"&&!R.classList.contains("lite")}
function where(){return (($("map-where")||{}).textContent||"").trim()}
// la parte "principale" di un paese: il poligono più grande e le isole vicine (Francia senza Guyana, USA senza Hawaii)
function main(f){var g=f.geometry;if(g.type!=="MultiPolygon")return f;
  var P=g.coordinates.map(function(c){var p={type:"Polygon",coordinates:c};return{c:c,a:d3.geoArea(p),m:d3.geoCentroid(p)}}).sort(function(a,b){return b.a-a.a});
  var keep=P.filter(function(p){return p===P[0]||d3.geoDistance(p.m,P[0].m)<.3});
  return{type:"Feature",geometry:{type:"MultiPolygon",coordinates:keep.map(function(p){return p.c})}}}
function size(){var b=wrap.getBoundingClientRect();W=b.width;H=b.height;DPR=Math.min(2,devicePixelRatio||1);
  cv.width=Math.round(W*DPR);cv.height=Math.round(H*DPR);MW=null;r0=Math.max(60,Math.min(H*.43,W*.32))}
function css(n,d){var v=getComputedStyle(R).getPropertyValue(n).trim();return v||d}
function has(){var o={};document.querySelectorAll("#ctrs .ctry.has").forEach(function(p){o[p.dataset.n]=1});return o}
var HAS={},SEL="";
function float(t){return 0} // niente oscillazione: il globo resta fermo e ruota soltanto (richiesta di Marco)
function draw(t){
  var dark=R.dataset.theme!=="light",acc=css("--accent","#7fb0ec");
  cx.setTransform(DPR,0,0,DPR,0,0);cx.clearRect(0,0,W,H);
  // cielo
  var g=cx.createRadialGradient(W/2,H/2,0,W/2,H/2,Math.max(W,H)*.75);
  g.addColorStop(0,dark?"#0e1626":"#16233b");g.addColorStop(1,dark?"#05070c":"#0a1222");cx.fillStyle=g;cx.fillRect(0,0,W,H);
  var sp=Math.max(0,1-(k-1)/3);
  if(MWON){if(!MW)MW=mwBuild();cx.globalAlpha=sp*(dark?.95:.85);cx.drawImage(MW,0,0,W,H);cx.globalAlpha=1}
  stars.forEach(function(s){var a=still()?.7:.45+.55*Math.sin(t/1000*s.v+s.p)*.5+.27;cx.globalAlpha=Math.max(.08,a)*sp;cx.fillStyle="#dfe8ff";
    cx.beginPath();cx.arc(s.x*W,s.y*H,s.s,0,6.283);cx.fill()});
  cx.globalAlpha=1;
  var r=r0*k,yy=H/2+float(t);proj.scale(r).translate([W/2,yy]).rotate(rot);
  // alone
  var h=cx.createRadialGradient(W/2,yy,r*.92,W/2,yy,r*1.28);h.addColorStop(0,"rgba(110,170,255,.35)");h.addColorStop(1,"rgba(110,170,255,0)");
  cx.fillStyle=h;cx.beginPath();cx.arc(W/2,yy,r*1.3,0,6.283);cx.fill();
  // mare
  var o=cx.createRadialGradient(W/2-r*.35,yy-r*.4,r*.1,W/2,yy,r);o.addColorStop(0,"#1b3354");o.addColorStop(1,"#08121f");
  cx.beginPath();path(sphere);cx.fillStyle=o;cx.fill();
  cx.beginPath();path(grat);cx.strokeStyle="rgba(150,190,255,.09)";cx.lineWidth=.6;cx.stroke();
  // terre
  feats.forEach(function(f){var n=f.properties.it;cx.beginPath();path(f);
    cx.fillStyle=n===SEL||f===hover?acc:HAS[n]?"#2f4c74":"#1e2b3e";cx.fill();
    cx.strokeStyle=f===hover||n===SEL?acc:"rgba(150,180,220,.35)";cx.lineWidth=f===hover?1.2:.5;cx.stroke()});
  // notte e crepuscolo: cerchi centrati sul punto opposto al sole
  var anti=[SUN[0]+180,-SUN[1]];
  [[96,.10],[93,.12],[90,.14],[87,.16],[84,.2]].forEach(function(z){cx.beginPath();path(d3.geoCircle().center(anti).radius(z[0]).precision(2)());cx.fillStyle="rgba(2,5,14,"+z[1]+")";cx.fill()});
  // luci delle città nella parte in ombra
  var view=[-rot[0],-rot[1]],sz=Math.min(2.2,.55+k*.18);cx.globalCompositeOperation="lighter";
  for(var i=0;i<LIGHTS.length;i+=3){var p=[LIGHTS[i],LIGHTS[i+1]];if(d3.geoDistance(p,view)>1.5)continue;
    var a=d3.geoDistance(p,SUN)*57.2958-90;if(a<-2)continue;a=Math.min(1,(a+2)/10);var q=proj(p);if(!q)continue;
    var m=LIGHTS[i+2],rr=sz*(.5+m*.22);cx.globalAlpha=a*(.25+m*.075);cx.fillStyle=m>6?"#ffe2a6":"#ffc46b";
    cx.beginPath();cx.arc(q[0],q[1],rr,0,6.283);cx.fill();if(m>6){cx.globalAlpha=a*.12;cx.beginPath();cx.arc(q[0],q[1],rr*3,0,6.283);cx.fill()}}
  cx.globalCompositeOperation="source-over";cx.globalAlpha=1;
  // paesi con notizie: un punto che pulsa piano
  feats.forEach(function(f){if(!HAS[f.properties.it])return;if(d3.geoDistance(f.c,view)>1.45)return;
    var p=proj(f.c);if(!p)return;var q=cx.createRadialGradient(p[0],p[1],0,p[0],p[1],7);q.addColorStop(0,"rgba(127,176,236,.95)");q.addColorStop(.35,"rgba(127,176,236,.5)");q.addColorStop(1,"rgba(127,176,236,0)");
    cx.fillStyle=q;cx.beginPath();cx.arc(p[0],p[1],7,0,6.283);cx.fill()});
  // riflesso del sole sul lato illuminato e ombra sul bordo
  var sp=d3.geoDistance(SUN,view)<1.57?proj(SUN):null,sx,sy;
  if(sp){sx=sp[0];sy=sp[1]}else{var a2=Math.atan2(-(SUN[1]-view[1]),SUN[0]-view[0]);sx=W/2+Math.cos(a2)*r*1.4;sy=yy+Math.sin(a2)*r*1.4}
  var e=cx.createRadialGradient(sx,sy,0,sx,sy,r*1.1);e.addColorStop(0,"rgba(255,244,220,.16)");e.addColorStop(1,"rgba(255,244,220,0)");
  cx.beginPath();path(sphere);cx.fillStyle=e;cx.fill();
  var l=cx.createRadialGradient(W/2,yy,r*.8,W/2,yy,r*1.01);l.addColorStop(0,"rgba(0,0,0,0)");l.addColorStop(1,"rgba(0,0,0,.4)");cx.fillStyle=l;cx.fill();
  cx.lineWidth=1;cx.strokeStyle="rgba(140,190,255,.45)";cx.stroke()}
function pick(x,y){var p=proj.invert([x,y]);if(!p||d3.geoDistance(p,[-rot[0],-rot[1]])>1.5707)return null;
  for(var i=0;i<feats.length;i++){var f=feats[i],b=f.b,inLon=b[0][0]<=b[1][0]?p[0]>=b[0][0]&&p[0]<=b[1][0]:p[0]>=b[0][0]||p[0]<=b[1][0];
    if(inLon&&p[1]>=b[0][1]&&p[1]<=b[1][1]&&d3.geoContains(f,p))return f}return null}
function loop(t){raf=0;var dt=Math.min(64,t-last);last=t;
  if(mode==="idle"&&!still()&&t>hold)rot[0]+=dt*.003;
  if(fly)fly(t);
  draw(t);if(home()&&!document.hidden&&(fade>0||mode!=="idle"))raf=requestAnimationFrame(loop)}
function kick(){if(!raf)raf=requestAnimationFrame(loop)}
function ease(x){return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}
// volo verso un paese: rotazione sul grande cerchio e zoom fino a vederlo intero
var fly=null;
function flyTo(f,done){var m=main(f),c=d3.geoCentroid(m),p=d3.geoOrthographic().clipAngle(90).rotate([-c[0],-c[1],TILT]).scale(1).translate([0,0]);
  var b=d3.geoPath(p).bounds(m),w=Math.max(b[1][0]-b[0][0],.02),h=Math.max(b[1][1]-b[0][1],.02);
  var k1=Math.max(1,Math.min(W*.6/w,H*.6/h)/r0),k0=k,from=[-rot[0],-rot[1]],I=d3.geoInterpolate(from,c),D=still()?0:Math.min(1800,900+d3.geoDistance(from,c)*400),s=performance.now();
  mode="fly";SEL=f.properties.it;
  fly=function(t){var x=D?Math.min(1,(t-s)/D):1,e=ease(x),q=I(e);rot=[-q[0],-q[1],TILT];k=Math.exp(Math.log(k0)+(Math.log(k1)-Math.log(k0))*e);
    if(x>=1){fly=null;if(done)done()}};kick()}
function back(){var k0=k,s=performance.now(),D=still()?0:900;mode="fly";SEL="";
  fly=function(t){var x=D?Math.min(1,(t-s)/D):1;k=Math.exp(Math.log(k0)*(1-ease(x)));if(x>=1){fly=null;k=1;mode="idle"}};kick()}
function show(on){fade=on?1:0;cv.classList.toggle("off",!on);wrap.classList.toggle("has-globe",on);if(on)kick()}
// dalla mappa piatta: se si entra in un paese (anche dalla ricerca) il globo ci vola sopra e poi lascia il posto alla mappa
function onWhere(){var w=where();HAS=has();
  if(!w||w==="Mondo"){if(fade===0){show(true);back()}return}
  if(fade===0||mode==="fly")return;
  var sel=document.querySelector("#ctrs .ctry.sel"),n=sel&&sel.dataset.n,f=n&&feats.filter(function(x){return x.properties.it===n})[0];
  if(!f){show(false);mode="idle";return}
  flyTo(f,function(){show(false);mode="idle"})}
function clickEl(e){if(e)e.dispatchEvent(new MouseEvent("click",{bubbles:true}))}
var down=null;
cv.addEventListener("pointerdown",function(e){down={x:e.clientX,y:e.clientY,r:rot.slice(),m:false};cv.setPointerCapture(e.pointerId)});
cv.addEventListener("pointermove",function(e){var b=cv.getBoundingClientRect();mx=e.clientX-b.left;my=e.clientY-b.top;
  if(down){var dx=e.clientX-down.x,dy=e.clientY-down.y;if(Math.abs(dx)+Math.abs(dy)>4)down.m=true;
    if(down.m&&mode==="idle"){var s=90/(r0*k);rot=[down.r[0]+dx*s,Math.max(-80,Math.min(80,down.r[1]-dy*s)),TILT];hold=performance.now()+2500;kick()}return}
  var f=mode==="idle"?pick(mx,my):null;if(f!==hover){hover=f;cv.style.cursor=f?"pointer":"grab";tip.textContent=f?f.properties.it:"";kick()}
  if(f){tip.style.left=mx+"px";tip.style.top=my+"px"}});
cv.addEventListener("pointerleave",function(){hover=null;tip.textContent="";kick()});
cv.addEventListener("pointerup",function(e){var d=down;down=null;if(!d||d.m||mode!=="idle")return;
  var b=cv.getBoundingClientRect(),f=pick(e.clientX-b.left,e.clientY-b.top);if(!f)return;
  hover=null;tip.textContent="";var p=document.querySelector('#ctrs .ctry[data-n="'+f.properties.it.replace(/"/g,"")+'"]');if(!p)return;
  hold=performance.now()+4000;clickEl(p);clickEl(p)});
new ResizeObserver(function(){size();kick()}).observe(wrap);
new MutationObserver(onWhere).observe($("map-where"),{childList:true,characterData:true,subtree:true});
new MutationObserver(function(){HAS=has();if(home()){last=performance.now();kick()}}).observe(R,{attributes:true,attributeFilter:["data-view","data-theme","class"]});
document.addEventListener("visibilitychange",function(){last=performance.now();kick()});
size();HAS=has();show(!where()||where()==="Mondo");
if(fade===0)k=1;kick();
return{flyTo:flyTo,feats:feats,at:function(n){var f=feats.filter(function(x){return x.properties.it===n})[0];var b=cv.getBoundingClientRect(),p=f&&proj(f.c);return p?[b.left+p[0],b.top+p[1]]:null}}};
