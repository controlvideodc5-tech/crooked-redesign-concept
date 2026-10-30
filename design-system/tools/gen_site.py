import json,re,os,shutil,sys,html
import markdown
SRC=sys.argv[1]; OUT=sys.argv[2]
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT+'/components'); 
shutil.copytree(SRC+'/fonts',OUT+'/fonts'); shutil.copytree(SRC+'/assets',OUT+'/assets',ignore=shutil.ignore_patterns('README.md'))
shutil.copy(SRC+'/components/bundle.css',OUT+'/bundle.css')
t=json.load(open(SRC+'/tokens.json'))
def v(c,th):
    x=c['value'][th] if isinstance(c['value'],dict) else c['value']
    m=re.fullmatch(r'\{(.+)\}',x); return f'var(--{m.group(1)})' if m else x
def hexof(c,th,seen=0):
    x=c['value'][th] if isinstance(c['value'],dict) else c['value']
    m=re.fullmatch(r'\{(.+)\}',x)
    if m: return hexof(next(k for k in t['color']['tokens'] if k['name']==m.group(1)),th)
    return x
L='/* Crooked Concept — generated from tokens.json */\n'
L+=''.join(f"@font-face{{font-family:'{f['family']}';src:url(fonts/{os.path.basename(f['file'])}) format('truetype');font-weight:{f['weight']};font-display:swap}}\n" for f in t['type']['fonts'])
L+=':root{\n'+''.join(f"  --{c['name']}:{v(c,'light')};\n" for c in t['color']['tokens'])
for fam in ['spacing','radius','shadow','size','zIndex']: L+=''.join(f"  --{c['name']}:{c['value']};\n" for c in t[fam]['tokens'])
L+=''.join(f"  --font-{k}:{s};\n" for k,s in t['type']['families'].items())+'  color-scheme:light;\n}\n'
dark=''.join(f"--{c['name']}:{v(c,'dark')};" for c in t['color']['tokens'] if v(c,'dark')!=v(c,'light'))
L+=f'@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{{dark}color-scheme:dark}}}}\n:root[data-theme="dark"]{{{dark}color-scheme:dark}}\n'
for g in t['type']['groups']:
    for s in g['styles']:
        L+=f".{s['name']}{{font-family:var(--font-{s.get('family',g['family'])});font-size:{s['fontSize']};line-height:{s['lineHeight']};font-weight:{s['fontWeight']};"+(f"letter-spacing:{s['letterSpacing']};" if 'letterSpacing' in s else '')+(f"text-transform:{s['textTransform']};" if 'textTransform' in s else '')+"}\n"
open(OUT+'/tokens.css','w').write(L)
# components
comps=[]
for name in sorted(os.listdir(SRC+'/components')):
    p=f'{SRC}/components/{name}/preview.html'
    if not os.path.isfile(p): continue
    h=open(p).read(); first=h.split('\n',1)[0]
    meta=dict(re.findall(r'(\w+)=(?:"([^"]*)"|(\d+))',first) and [(k,a or b) for k,a,b in re.findall(r'(\w+)=(?:"([^"]*)"|(\d+))',first)])
    h=h.replace('<head>','<head><link rel="stylesheet" href="../tokens.css"><link rel="stylesheet" href="../bundle.css">',1)
    open(f'{OUT}/components/{name.lower()}.html','w').write(h)
    rd=f'{SRC}/components/{name}/README.md'
    md=open(rd).read() if os.path.exists(rd) else ''
    md=re.sub(r'^# .*\n','',md)
    comps.append((name,meta,markdown.markdown(md,extensions=['tables'])))
order=['Actions','Status','Media','Crooked Con','Collateral']
comps=[c for c in comps if c[0]!='Cover']
comps.sort(key=lambda c:(order.index(c[1].get('group','Collateral')) if c[1].get('group') in order else 9))
def md(path):
    return markdown.markdown(open(path).read(),extensions=['tables'])
secs=[('overview','Overview',md(SRC+'/README.md')),('voice','Voice and tone',md(SRC+'/1-voice-and-tone.md')),('practice','Putting it into practice',md(SRC+'/2-putting-it-into-practice.md')),('midterms','Midterm messaging',md(SRC+'/3-midterm-messaging.md'))]
for i,(a,b,c) in enumerate(secs): secs[i]=(a,b,re.sub(r'<h1>.*?</h1>','',c,1))
# token tables
sw=''.join(f'<figure class="sw"><div class="chip"><i style="background:{hexof(c,"light")}"></i><i style="background:{hexof(c,"dark")}"></i></div><figcaption><b>{c["name"]}</b><code>{hexof(c,"light")}'+(f' · {hexof(c,"dark")}' if hexof(c,"dark")!=hexof(c,"light") else '')+f'</code><span>{html.escape(c.get("usage",""))}</span></figcaption></figure>' for c in t['color']['tokens'])
ty=''.join(f'<div class="ty"><code>{s["name"]}<br>{s["fontSize"]} / {s["lineHeight"]} · {s["fontWeight"]}</code><span class="{s["name"]}" style="font-size:min({s["fontSize"]},14vw)">{html.escape(s.get("sample",""))}</span></div>' for g in t['type']['groups'] for s in g['styles'])
def rows(fam): return ''.join(f'<tr><td><code>{c["name"]}</code></td><td class="num">{html.escape(c["value"])}</td><td>{html.escape(c.get("usage",""))}</td></tr>' for c in t[fam]['tokens'])
tok=f'<h2>Color</h2><p class="muted">Left half light theme, right half dark.</p><div class="sws">{sw}</div><h2>Type</h2><div class="tys">{ty}</div>'+''.join(f'<h2>{n}</h2><div class="tbl"><table><thead><tr><th>Token</th><th>Value</th><th>Use</th></tr></thead><tbody>{rows(f)}</tbody></table></div>' for n,f in [('Spacing','spacing'),('Radius','radius'),('Shadow','shadow'),('Sizes','size'),('Z-index','zIndex')])
cmp=''.join(f'<article class="cmp" id="c-{n}"><header><span class="eyebrow">{html.escape(m.get("group",""))}</span><h3>{n}</h3>{f"<p class=muted>{html.escape(m.get(chr(115)+chr(117)+chr(98)+chr(116)+chr(105)+chr(116)+chr(108)+chr(101),''))}</p>" if m.get("subtitle") else ""}</header><iframe src="components/{n.lower()}.html" title="{n} preview" style="height:{m.get("height","200")}px"></iframe><div class="doc">{d}</div></article>' for n,m,d in comps)
groups=['Merch Round 2','Merch Lookbook','Everybody In Hats','Round 2 Posters']
ast=''.join(f'<h2>{g}</h2><div class="ag">'+''.join(f'<a href="assets/{g}/{f}" target="_blank"><img src="assets/{g}/{f}" alt="{f[:-5].replace("-"," ")}"></a>' for f in sorted(os.listdir(f'{SRC}/assets/{g}')) if f.endswith('.webp'))+'</div>' for g in groups)
nav=''.join(f'<a href="#{a}">{b}</a>' for a,b,_ in secs)+'<a href="#tokens">Tokens</a><a href="#components">Components</a><a href="#assets">Assets</a><a href="Crooked-Concept-Brand-Book.pdf" download>Download PDF</a>'
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Crooked Concept Design System</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="site.css"></head><body>
<header class="top"><div class="wrap"><span class="eyebrow">Crooked homepage concept · Design system</span><h1>Less doom.<br>More doing.</h1><p>Voice, tone, color, type, tokens, components and collateral for the Crooked redesign concept, in one place.</p><p class="cta"><a class="ck-btn ck-btn-primary" href="Crooked-Concept-Brand-Book.pdf" download>Download the brand book (PDF, 10 MB)</a><a class="ck-btn ck-btn-ghost" href="Crooked-Concept-Brand-Book.pdf" target="_blank" rel="noopener">Open in browser</a></p><p class="note">Unofficial design exploration. Not affiliated with, endorsed by or connected to Crooked Media. Names, show art and marks belong to their owners; the wordmark here is a typeset stand-in.</p></div></header>
<nav class="toc"><div class="wrap">{nav}</div></nav><main class="wrap">
{''.join(f'<section id="{a}" class="prose"><span class="eyebrow">{b}</span><h2 class="sec">{b}</h2>{c}</section>' for a,b,c in secs)}
<section id="tokens"><span class="eyebrow">Tokens</span><h2 class="sec">Tokens</h2><p class="muted">Source of truth: <a href="tokens.json">tokens.json</a>. Compiled CSS: <a href="tokens.css">tokens.css</a>. Component styles: <a href="bundle.css">bundle.css</a>.</p>{tok}</section>
<section id="components"><span class="eyebrow">Components</span><h2 class="sec">Components and collateral</h2>{cmp}</section>
<section id="assets"><span class="eyebrow">Assets</span><h2 class="sec">Mockups from the PDFs</h2>{ast}</section>
</main><footer><div class="wrap"><p><a class="ck-btn ck-btn-primary" href="Crooked-Concept-Brand-Book.pdf" download>Download the brand book (PDF)</a></p>Crooked homepage concept · Design system · Unofficial concept, not affiliated with Crooked Media.</div></footer>
<script>document.querySelectorAll('iframe').forEach(f=>f.addEventListener('load',()=>{{try{{const d=f.contentDocument;f.style.height=Math.max(80,d.documentElement.scrollHeight)+'px'}}catch(e){{}}}}));</script>
</body></html>'''
open(OUT+'/index.html','w').write(page)
shutil.copy(SRC+'/tokens.json',OUT+'/tokens.json')
print(len(comps),'components')
