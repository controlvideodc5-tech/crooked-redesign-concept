
(function(){
function fit(f){try{var d=f.contentDocument;if(!d||!d.body)return;var box=f.parentNode,W=box.clientWidth;
f.style.width=W+'px';f.style.transform='';var sw=d.documentElement.scrollWidth;
if(sw>W+2){var s=W/sw;f.style.width=sw+'px';f.style.transform='scale('+s+')';var h=d.documentElement.scrollHeight;f.style.height=h+'px';box.style.height=Math.ceil(h*s)+'px'}
else{var h2=Math.max(80,d.documentElement.scrollHeight);f.style.height=h2+'px';box.style.height=h2+'px'}}catch(e){}}
var frames=[].slice.call(document.querySelectorAll('.frame iframe'));
frames.forEach(function(f){f.addEventListener('load',function(){fit(f);setTimeout(function(){fit(f)},600)})});
var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(function(){frames.forEach(fit)},150)});
if(window.matchMedia('(max-width: 700px)').matches){document.querySelectorAll('details.doc').forEach(function(d){d.removeAttribute('open')})}
var links=[].slice.call(document.querySelectorAll('nav.toc a[href^="#"]')),map={};
links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){a.removeAttribute('aria-current')});var a=map[e.target.id];if(a){a.setAttribute('aria-current','true');a.scrollIntoView({block:'nearest',inline:'center'})}}})},{rootMargin:'-45% 0px -50% 0px'});
Object.keys(map).forEach(function(id){var s=document.getElementById(id);if(s)io.observe(s)})}
var top=document.querySelector('.totop');window.addEventListener('scroll',function(){top.classList.toggle('show',window.scrollY>1200)},{passive:true});
})();
(function(){
var m=document.querySelector('meta[name="build"]');if(!m)return;var cur=m.content,shown=false;
var bar=document.createElement('div');bar.className='update-bar';bar.setAttribute('role','status');bar.hidden=true;
bar.innerHTML='<span>A newer version of this page is live.</span><button type="button">Refresh</button>';
document.body.appendChild(bar);bar.querySelector('button').onclick=function(){location.reload()};
function check(){if(shown)return;fetch('version.json?t='+Date.now(),{cache:'no-store'}).then(function(r){return r.json()}).then(function(j){if(j.v&&j.v!==cur){shown=true;bar.hidden=false}}).catch(function(){})}
document.addEventListener('visibilitychange',function(){if(document.visibilityState==='visible')check()});
window.addEventListener('focus',check);window.addEventListener('pageshow',function(e){if(e.persisted)check()});
setInterval(check,120000);setTimeout(check,4000);
})();
