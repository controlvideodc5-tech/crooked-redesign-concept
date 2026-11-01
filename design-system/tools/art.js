const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:1200},deviceScaleFactor:2});
await p.goto('file://'+process.cwd()+'/art.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
for(const id of ['jersey','turnout','build']){const el=await p.$('#'+id);await el.screenshot({path:'art-'+id+'.png',omitBackground:true});}
await b.close()})();
