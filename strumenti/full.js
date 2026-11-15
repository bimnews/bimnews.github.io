const {chromium}=require("playwright");
(async()=>{const b=await chromium.launch();const e=[];const V=["home","bim-news","bim-ai","bim-accademia","bim-5-minuti","video","agenda","studio","chi-sono","mappa"];
async function run(theme,lite,vp,tag,views){const ctx=await b.newContext({viewport:vp});
 await ctx.addInitScript(([t,l])=>{localStorage.setItem("tema-2026",t);localStorage.setItem("versione",l?"essenziale":"completa")},[theme,lite]);
 const p=await ctx.newPage();p.on("pageerror",x=>e.push(tag+" "+x.message));const reqs=[];p.on("request",r=>reqs.push(r.url()));
 for(const h of views){await p.goto("http://127.0.0.1:8765/#"+h);await p.waitForTimeout(1400);
   const sw=await p.evaluate(()=>document.documentElement.scrollWidth);if(sw>vp.width+1)e.push(tag+" overflow "+h+" "+sw);
   await p.screenshot({path:`img/f-${tag}-${h}.png`});}
 if(tag==="hd"){const s=await p.evaluate(()=>{location.hash="#home";return 0});await p.waitForTimeout(800)}
 await ctx.close();return reqs}
const r1=await run("dark",false,{width:1440,height:900},"dk",V);
const r2=await run("light",false,{width:1440,height:900},"lt",["home","studio","bim-5-minuti"]);
const r3=await run("dark",true,{width:1440,height:900},"lite",["home","bim-news","bim-accademia","studio"]);
console.log("lite heavy reqs",r3.filter(u=>/foto|copertine|gif|woff2|mappa.svg|edificio/.test(u)));
await run("dark",false,{width:390,height:844},"mob",["home","bim-news","bim-accademia","studio"]);
const ctx=await b.newContext({viewport:{width:1366,height:768}});await ctx.addInitScript(()=>localStorage.setItem("tema-2026","dark"));const p=await ctx.newPage();await p.goto("http://127.0.0.1:8765/#home");await p.waitForTimeout(1500);
console.log("strip bottom 1366x768",await p.evaluate(()=>Math.round(document.getElementById("fc-strip").getBoundingClientRect().bottom)));
console.log("err",e);await b.close()})();
