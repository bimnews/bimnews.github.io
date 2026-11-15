const {chromium}=require("playwright");
(async()=>{const b=await chromium.launch();const sizes=(process.argv[2]||"1836x776,1920x960,1920x1080,1536x730,1440x800,1366x768,1280x720").split(",");
for(const s of sizes){const [w,h]=s.split("x").map(Number);const ctx=await b.newContext({viewport:{width:w,height:h}});await ctx.addInitScript(()=>{localStorage.setItem("versione","completa")});const p=await ctx.newPage();
await p.goto("http://127.0.0.1:8765/#home");await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const g=q=>{const e=document.querySelector(q);if(!e)return null;const r=e.getBoundingClientRect();return [Math.round(r.top),Math.round(r.bottom),Math.round(r.height)]};return {strip:g("#fc-strip"),map:g("#fc-map .map-wrap"),nav:g(".fc-nav"),head:g("header.top"),util:g(".util")}});
console.log(s,JSON.stringify(r),r.strip&&r.strip[1]<=h?"OK":"FUORI");if(process.argv[3])await p.screenshot({path:"img/fit-"+s+".png"});await ctx.close()}
await b.close()})();
