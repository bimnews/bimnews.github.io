// Abbina i paesi di world-atlas ai nomi italiani della mappa del sito, confrontando gli ingombri proiettati
const fs=require("fs"),vm=require("vm");const D=__dirname+"/";
const ctx={};ctx.globalThis=ctx;ctx.self=ctx;vm.createContext(ctx);
for(const f of ["d3-array.min.js","d3-geo.min.js","topojson-client.min.js"])vm.runInContext(fs.readFileSync(D+f,"utf8"),ctx);
const d3=ctx.d3,topo=ctx.topojson;
const world=JSON.parse(fs.readFileSync(D+"countries-110m.json"));const feats=topo.feature(world,world.objects.countries).features;
const svg=fs.readFileSync("/home/user/bimnews.github.io/assets/mappa.svg","utf8");
const S=[...svg.matchAll(/data-c="([a-z]+)" data-n="([^"]+)" data-b="([^"]+)"/g)].map(m=>({c:m[1],n:m[2].replace(/&#x27;/g,"'"),b:m[3].split(",").map(Number)}));
function test(proj){let err=0;const P=feats.map(f=>{const b=d3.geoPath(proj).bounds(f);return{f,b}});
  const out=[];for(const s of S){let best=null,bd=1e9;for(const p of P){const d=Math.abs(p.b[0][0]-s.b[0])+Math.abs(p.b[0][1]-s.b[1])+Math.abs(p.b[1][0]-s.b[2])+Math.abs(p.b[1][1]-s.b[3]);if(d<bd){bd=d;best=p}}out.push([s.n,best.f.properties.name,best.f.id,+bd.toFixed(1),s.c]);err+=Math.min(bd,40)}return{err,out}}
// prova proiezioni: adatta su Italia e Australia
const cand={NaturalEarth1:d3.geoNaturalEarth1,EqualEarth:d3.geoEqualEarth,Equirect:d3.geoEquirectangular,Mercator:d3.geoMercator};
let bestAll=null;
for(const [nm,fn] of Object.entries(cand)){
  for(const sc of [110,112,114,116,118,120,122,124,126,128,130,135,140]){for(const tx of [355,358,360,362,365]){for(const ty of [160,165,170,175,180,185,190,195]){
    const p=fn().scale(sc).translate([tx,ty]);const it=feats.find(f=>f.properties.name==="Italy");const b=d3.geoPath(p).bounds(it);
    const e=Math.abs(b[0][0]-371.3)+Math.abs(b[1][0]-391.9)+Math.abs(b[0][1]-58.8)+Math.abs(b[1][1]-82.2);
    if(!bestAll||e<bestAll.e)bestAll={nm,sc,tx,ty,e}}}}}
console.log("migliore",bestAll);
const p=cand[bestAll.nm]().scale(bestAll.sc).translate([bestAll.tx,bestAll.ty]);
const r=test(p);console.log("errore",r.err.toFixed(0));
const bad=r.out.filter(x=>x[3]>6);console.log("dubbi",bad.length,JSON.stringify(bad));
fs.writeFileSync(D+"abbinamenti.json",JSON.stringify(r.out));
