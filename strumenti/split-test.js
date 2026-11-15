const {chromium}=require("playwright");
(async()=>{const b=await chromium.launch();const e=[];const ctx=await b.newContext({viewport:{width:1440,height:900}});
const p=await ctx.newPage();p.on("pageerror",x=>e.push(x.message));p.on("console",m=>{if(m.type()==="error"&&!/goatcounter|gc.zgo|ERR_NAME/.test(m.text()))e.push("console "+m.text())});
const reqs=[];p.on("request",r=>reqs.push(r.url().replace("http://127.0.0.1:8765/","")));
await p.goto("http://127.0.0.1:8765/#home");await p.waitForTimeout(1800);
console.log("home: strip",await p.evaluate(()=>document.querySelectorAll("#fc-strip .fs-it").length),"pins",await p.evaluate(()=>document.querySelectorAll(".map-wrap text, .pin, .mk").length),"accademia scaricata?",reqs.some(u=>u.includes("accademia.json")));
console.log("ultimo agg.",await p.evaluate(()=>{const x=[...document.querySelectorAll("*")].find(n=>n.children.length===0&&/Ultimo aggiornamento/.test(n.textContent));return x&&x.textContent.trim()}));
await p.goto("http://127.0.0.1:8765/#bim-news");await p.waitForTimeout(1200);console.log("news cards",await p.evaluate(()=>document.querySelectorAll(".art").length));
await p.goto("http://127.0.0.1:8765/#bim-ai");await p.waitForTimeout(800);console.log("ai cards",await p.evaluate(()=>document.querySelectorAll(".art").length));
const wk=await p.evaluate(()=>Object.keys(WEEKS).sort().pop());await p.goto("http://127.0.0.1:8765/#settimana-"+wk);await p.waitForTimeout(900);console.log("lettore",wk,await p.evaluate(()=>document.querySelectorAll("[id^=art-]").length));
await p.goto("http://127.0.0.1:8765/#bim-accademia");await p.waitForTimeout(1500);console.log("accademia",await p.textContent("#ac-count"),"barre",await p.evaluate(()=>document.querySelectorAll(".ac-hist .bar").length),"scaricata",reqs.some(u=>u.includes("accademia.json")));
await p.selectOption("#ac-year","2023");await p.waitForTimeout(200);console.log("filtro 2023",await p.textContent("#ac-count"));
await p.goto("http://127.0.0.1:8765/#agenda");await p.waitForTimeout(600);await p.goto("http://127.0.0.1:8765/#mappa");await p.waitForTimeout(600);
await p.goto("http://127.0.0.1:8765/#home");await p.waitForTimeout(800);await p.click("#tour-btn");await p.waitForTimeout(600);console.log("tour",await p.evaluate(()=>!document.getElementById("tour").hidden));
// accesso diretto ad Accademia
const q=await ctx.newPage();q.on("pageerror",x=>e.push("diretto "+x.message));await q.goto("http://127.0.0.1:8765/#bim-accademia");await q.waitForTimeout(1500);console.log("diretto accademia",await q.textContent("#ac-count"));
console.log("err",e);await b.close()})();
