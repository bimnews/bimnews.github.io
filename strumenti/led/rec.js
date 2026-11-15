const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch();const O=process.argv[2],theme=process.argv[3]||'dark';
const p=await b.newPage({viewport:{width:1440,height:900}});await p.addInitScript(t=>{try{localStorage.setItem('tema-2026',t)}catch(e){}},theme);
await p.goto('http://localhost:8765/#bim-news');await p.waitForTimeout(1800);await p.addStyleTag({path:O+'/led.css'});await p.waitForTimeout(300);
const hdr=await p.evaluate(()=>{const r=document.querySelector('.top').getBoundingClientRect();return {x:0,y:0,width:1440,height:Math.round(r.bottom)}});
const tabs=await p.evaluate(()=>{const r=document.querySelector('.news-tabs').getBoundingClientRect();return {x:0,y:Math.round(r.top-30),width:1440,height:Math.round(r.height+60)}});
let n=0;const T=[];async function cap(clip,ms){const end=Date.now()+ms;do{await p.screenshot({path:`${O}/f/${String(n++).padStart(4,'0')}.png`,clip});T.push(Date.now())}while(Date.now()<end)}
fs.mkdirSync(O+'/f',{recursive:true});for(const f of fs.readdirSync(O+'/f'))fs.unlinkSync(O+'/f/'+f);
await p.mouse.move(700,600);await cap(hdr,600);
for(const sel of ['.top nav a[href="#bim-news"]','.top nav a[href="#bim-ai"]','.top nav a[href="#bim-accademia"]','.top nav a[href="#bim-5-minuti"]','.top nav a[href="#video"]','.top nav a[href="#agenda"]']){const e=await p.$(sel);if(!e)continue;const bb=await e.boundingBox();await p.mouse.move(bb.x+bb.width/2,bb.y+bb.height/2);await cap(hdr,420)}
const e=await p.$('.top nav a[href="#agenda"]');const bb=await e.boundingBox();await p.mouse.down();await cap(hdr,500);await p.mouse.up();await p.mouse.move(700,600);
await p.evaluate(()=>location.hash='#bim-news');await p.waitForTimeout(400);
for(const sel of ['.news-tabs a[data-ai="1"]','.news-tabs a[href="#bim-accademia"]']){const e=await p.$(sel);const bb=await e.boundingBox();await p.mouse.move(bb.x+bb.width/2,bb.y+bb.height/2);await cap(tabs,500)}
{const e=await p.$('.news-tabs a[href="#bim-accademia"]');await p.mouse.down();await cap(tabs,450);await p.mouse.move(10,880);}
fs.writeFileSync(O+'/f/t.json',JSON.stringify(T));await p.screenshot({path:O+'/still-'+theme+'.png',clip:{x:0,y:0,width:1440,height:Math.round(tabs.y+tabs.height)}});await b.close()})()
