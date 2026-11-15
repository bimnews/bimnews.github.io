const {chromium}=require("playwright");
(async()=>{const b=await chromium.launch();const e=[];
const ctx=await b.newContext({viewport:{width:1800,height:800}});await ctx.addInitScript(()=>{localStorage.setItem("tema-2026","dark");localStorage.setItem("versione","completa")});
const p=await ctx.newPage();p.on("pageerror",x=>e.push(x.message));
await p.goto("http://127.0.0.1:8765/#home");await p.waitForTimeout(1800);
const sug=async v=>{await p.fill("#fs-q","");await p.type("#fs-q",v);await p.waitForTimeout(250);return p.$$eval("#fs-list li",l=>l.map(x=>x.textContent.replace(/\s+/g," ").trim()))};
console.log("ital ->",await sug("ital"));
await p.screenshot({path:"img/srch-list.png"});
await p.keyboard.press("Enter");await p.waitForTimeout(900);
console.log("dopo Italia: dove=",await p.textContent("#map-where"),"| sel=",await p.textContent("#fc-sel"),"| away=",await p.evaluate(()=>document.getElementById("fc-search").classList.contains("away")));
await p.screenshot({path:"img/srch-italia.png"});
console.log("bav ->",await sug("bav"));await p.keyboard.press("Enter");await p.waitForTimeout(900);console.log("dopo Baviera: dove=",await p.textContent("#map-where"));
console.log("roma ->",await sug("roma"));
console.log("ifc ->",await sug("ifc"));await p.keyboard.press("Enter");await p.waitForTimeout(900);
console.log("dopo IFC: view=",await p.evaluate(()=>document.documentElement.dataset.view),"q=",await p.inputValue("#q"),"conteggio=",await p.textContent("#count"));
await p.goto("http://127.0.0.1:8765/#home");await p.waitForTimeout(1200);await p.keyboard.press("/");console.log("tasto / mette il fuoco:",await p.evaluate(()=>document.activeElement.id));
// essenziale
const c2=await b.newContext({viewport:{width:1440,height:800}});await c2.addInitScript(()=>{localStorage.setItem("versione","essenziale")});const l=await c2.newPage();l.on("pageerror",x=>e.push("lite "+x.message));
await l.goto("http://127.0.0.1:8765/#home");await l.waitForTimeout(1200);await l.type("#fs-q","german");await l.waitForTimeout(250);console.log("lite german ->",await l.$$eval("#fs-list li",x=>x.length));await l.keyboard.press("Enter");await l.waitForTimeout(700);
console.log("lite dopo Germania: view=",await l.evaluate(()=>document.documentElement.dataset.view),"q=",await l.inputValue("#q"));
await l.goto("http://127.0.0.1:8765/#home");await l.waitForTimeout(900);await l.screenshot({path:"img/srch-lite.png"});
// telefono
const m=await b.newPage({viewport:{width:390,height:844}});m.on("pageerror",x=>e.push("mob "+x.message));await m.goto("http://127.0.0.1:8765/#home");await m.waitForTimeout(1300);
console.log("mob sw",await m.evaluate(()=>document.documentElement.scrollWidth));await m.screenshot({path:"img/srch-mob.png",fullPage:true});
const t=await b.newPage({viewport:{width:900,height:1000}});await t.goto("http://127.0.0.1:8765/#home");await t.waitForTimeout(1300);console.log("tablet sw",await t.evaluate(()=>document.documentElement.scrollWidth));await t.screenshot({path:"img/srch-tab.png",fullPage:true});
console.log("err",e);await b.close()})();
