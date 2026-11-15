// «Rilievo lento»: nuvola di punti che si forma come una scansione laser (solo versione completa)
(function(){
var cv=document.querySelector(".bn-cloud");if(!cv||!cv.getContext)return;
var root=document.documentElement,cx=cv.getContext("2d"),still=matchMedia("(prefers-reduced-motion: reduce)").matches;
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gauss(r){var u=r()||1e-9,v=r();return Math.sqrt(-2*Math.log(u))*Math.cos(6.2832*v)}
var IP=3.2,PW=1.35;// interpiano e passo delle finestre, in metri
var VOL=[[0,0,0,26,16,2],[4,2,2,16,11,7]];// [x,y,floor0,lx,ly,piani]
function survey(seed){
  var r=rng(seed),P=[],side=seed%2?1:-1,S=[side>0?40:-14,side>0?-10:30];
  function keep(u,v){var f=v%IP,w=u%PW;if(f<.22)return true;if(f>.85&&f<2.65&&w>.22&&w<1.13)return r()<.05;return true}
  function put(x,y,z){var d=Math.hypot(x-S[0],y-S[1]);if(r()>Math.min(1,(18/d)*(18/d)))return;
    P.push({x:x,y:y,z:z,a:Math.atan2(y-S[1],x-S[0]),gx:gauss(r),gy:gauss(r),gz:gauss(r),t:-1})}
  for(var k=0;k<VOL.length;k++){var V=VOL[k],x0=V[0],y0=V[1],z0=V[2]*IP,lx=V[3],ly=V[4],h=V[5]*IP,n=Math.round((lx+ly)*h*5);
    for(var i=0;i<n;i++){var u,v=r()*h;
      if(r()<.5){u=r()*lx;if(keep(u,v))put(x0+u,y0+ly,z0+v)}else{u=r()*ly;if(keep(u,v))put(x0+lx,y0+u,z0+v)}}
    for(i=0;i<lx*ly*2;i++)put(x0+r()*lx,y0+r()*ly,z0+h);
    for(i=0;i<h*30;i++){v=r()*h;put(x0,y0+ly,z0+v);put(x0+lx,y0+ly,z0+v);put(x0+lx,y0,z0+v)}}
  var amin=1e9,amax=-1e9;P.forEach(function(p){amin=Math.min(amin,p.a);amax=Math.max(amax,p.a)});
  return{P:P,S:S,amin:amin,amax:amax,dir:side,t0:0}
}
var W,H,sc,ox,oy,cur=null,old=null,seed=7,color="#6fa8e8",run=false,vis=false;
function pr(x,y,z){return[ox+(x-y)*.866*sc,oy+((x+y)*.5-z)*sc]}
// ingombro isometrico dei volumi, per adattare il rilievo alla testata
var BX=(function(){var a=[1e9,1e9,-1e9,-1e9];VOL.forEach(function(V){[[0,0],[V[3],0],[0,V[4]],[V[3],V[4]]].forEach(function(c){[V[2]*IP,(V[2]+V[5])*IP].forEach(function(z){var x=V[0]+c[0],y=V[1]+c[1],u=(x-y)*.866,v=(x+y)*.5-z;a[0]=Math.min(a[0],u);a[1]=Math.min(a[1],v);a[2]=Math.max(a[2],u);a[3]=Math.max(a[3],v)})})});return a})();
function fit(){var r=cv.getBoundingClientRect(),d=devicePixelRatio||1;W=cv.width=Math.round(r.width*d);H=cv.height=Math.round(r.height*d);
  var bw=BX[2]-BX[0],bh=BX[3]-BX[1],wide=W>H*1.6;sc=Math.min((wide?W*.42:W*.8)/bw,H*.84/bh);
  ox=(wide?W*.97-bw*sc:(W-bw*sc)/2)-BX[0]*sc;oy=H*.92-BX[3]*sc}
function sweep(s,now){return s.dir>0?s.amin+(s.amax-s.amin)*Math.min(1,(now-s.t0)/7000):s.amax-(s.amax-s.amin)*Math.min(1,(now-s.t0)/7000)}
function draw(s,now,alpha){if(!s)return;var ang=sweep(s,now);cx.fillStyle=color;var d=devicePixelRatio||1,sz=1.6*d;
  for(var i=0;i<s.P.length;i++){var p=s.P[i];
    if(p.t<0){if(still||(s.dir>0?p.a<=ang:p.a>=ang))p.t=now;else continue}
    var e=still?0:.6*Math.exp(-(now-p.t)/1400),q=pr(p.x+p.gx*e,p.y+p.gy*e,p.z+p.gz*e);
    cx.globalAlpha=alpha*(.45+.45*Math.min(1,p.z/20)+(e>.3?.1:0));cx.fillRect(q[0],q[1],sz,sz)}
  if(!still&&now-s.t0<7000&&alpha>.9){var a=pr(s.S[0],s.S[1],1.6),L=70;var b=pr(s.S[0]+Math.cos(ang)*L,s.S[1]+Math.sin(ang)*L,1.6);
    var g=cx.createLinearGradient(a[0],a[1],b[0],b[1]);g.addColorStop(0,color);g.addColorStop(1,"transparent");
    cx.globalAlpha=.5;cx.strokeStyle=g;cx.lineWidth=d;cx.beginPath();cx.moveTo(a[0],a[1]);cx.lineTo(b[0],b[1]);cx.stroke();
    cx.globalAlpha=.9;cx.fillRect(a[0]-2*d,a[1]-2*d,4*d,4*d)}}
function frame(now){if(!run)return;cx.clearRect(0,0,W,H);
  if(!cur){cur=survey(seed);cur.t0=now}
  if(now-cur.t0>12000){old=cur;old.f0=now;seed=seed*7%97+3;cur=survey(seed);cur.t0=now+600}
  if(old){var fa=1-(now-old.f0)/2500;if(fa<=0)old=null;else draw(old,now,fa*.8)}
  draw(cur,now,1);cx.globalAlpha=1;
  if(still){run=false;return}requestAnimationFrame(frame)}
function want(){return vis&&!root.classList.contains("lite")&&!document.hidden&&cv.offsetWidth>0}
function check(){color=getComputedStyle(cv).getPropertyValue("--accent").trim()||color;
  if(want()&&!run){fit();run=true;requestAnimationFrame(frame)}else if(!want())run=false}
new IntersectionObserver(function(e){vis=e[0].isIntersecting;check()}).observe(cv);
new ResizeObserver(function(){if(run)fit()}).observe(cv);
new MutationObserver(check).observe(root,{attributes:true,attributeFilter:["class","data-view","data-theme"]});
document.addEventListener("visibilitychange",check);
})();
