import json,re,os,html,markdown,sys
SRC='../ds/project'
t=json.load(open(SRC+'/tokens.json'))
def hexof(c,th):
    x=c['value'][th] if isinstance(c['value'],dict) else c['value']
    m=re.fullmatch(r'\{(.+)\}',x)
    return hexof(next(k for k in t['color']['tokens'] if k['name']==m.group(1)),th) if m else x
md=lambda p: re.sub(r'<h1>.*?</h1>','',markdown.markdown(open(p).read(),extensions=['tables']),count=1)
secs=[('Overview','The visual rules',md(SRC+'/README.md')),('Voice and tone','How it sounds',md(SRC+'/1-voice-and-tone.md')),('Putting it into practice','From brief to piece',md(SRC+'/2-putting-it-into-practice.md')),('Midterm messaging','Nov 2026 campaign layer',md(SRC+'/3-midterm-messaging.md'))]
prim=[c for c in t['color']['tokens'] if c['name'].startswith('c-')]
sem=[c for c in t['color']['tokens'] if not c['name'].startswith('c-')]
sw=''.join(f'<div class="sw"><i style="background:{hexof(c,"light")}"></i><div><b>{c["name"]}</b><code>{hexof(c,"light")}</code><span>{html.escape(c["usage"])}</span></div></div>' for c in prim)
semrows=''.join(f'<tr><td><code>{c["name"]}</code></td><td><span class="dot" style="background:{hexof(c,"light")}"></span>{hexof(c,"light")}</td><td><span class="dot" style="background:{hexof(c,"dark")}"></span>{hexof(c,"dark")}</td><td>{html.escape(c["usage"])}</td></tr>' for c in sem)
ty=''.join(f'<div class="ty"><code>{s["name"]} · {s["fontSize"]}/{s["lineHeight"]} · {s["fontWeight"]}</code><div class="{s["name"]}" style="font-size:min({s["fontSize"]},72px)">{html.escape(s.get("sample",""))}</div></div>' for g in t['type']['groups'] for s in g['styles'])
def rows(f): return ''.join(f'<tr><td><code>{c["name"]}</code></td><td><code>{html.escape(c["value"])}</code></td><td>{html.escape(c.get("usage",""))}</td></tr>' for c in t[f]['tokens'])
order=['Actions','Status','Media','Crooked Con','Motion','Collateral']
comps=[]
for n in os.listdir(SRC+'/components'):
    p=f'{SRC}/components/{n}/preview.html'
    if n=='Cover' or not os.path.isfile(p): continue
    g=re.search(r'group="([^"]+)"',open(p).read().split('\n')[0]); g=g.group(1) if g else ''
    r=f'{SRC}/components/{n}/README.md'; d=re.sub(r'<h1>.*?</h1>','',markdown.markdown(open(r).read(),extensions=['tables']),count=1) if os.path.exists(r) else ''
    comps.append((order.index(g) if g in order else 9,n,g,d))
comps.sort()
def vis(n):
    if n=='MerchLine':
        h=open(SRC+'/components/MerchLine/preview.html').read()
        body=h[h.index('<div class="mk">'):h.rindex('</div>')+6]
        parts=body.split('<h3 class="mh">'); body=parts[0]+''.join('<div class="cat"><h3 class="mh">'+x.replace('</div>\n</div>','</div></div>\n</div>') if x.rstrip().endswith('</div>\n</div>') or x.endswith('</div>\n</div>') else '<div class="cat"><h3 class="mh">'+x+'</div>' for x in parts[1:])
        return '<div class="merchbook">'+h[h.index('<style>'):h.index('</style>')+8]+body+'</div>'
    return f'<img src="shots/{n}.jpg" alt="{n}">'
cmp=''.join(f'<section class="cmp"><span class="eyebrow">Components · {g}</span><h2>{n}</h2><div class="doc">{d}</div>{vis(n)}</section>' if n=='MerchLine' else f'<section class="cmp"><span class="eyebrow">Components · {g}</span><h2>{n}</h2><img src="shots/{n}.jpg" alt="{n}"><div class="doc">{d}</div></section>' for _,n,g,d in comps)
groups=['DC Small Business','Merch Round 2','Merch Lookbook','Everybody In Hats','Let Them Eat','Round 2 Posters']
ast=''.join(f'<section class="gal"><span class="eyebrow">08 · Concept collateral</span><h2>{g}</h2><div class="ag">'+''.join(f'<img src="site/assets/{g}/{f}">' for f in sorted(os.listdir(f'{SRC}/assets/{g}')) if f.endswith('.webp'))+'</div></section>' for g in groups)

DCG='DC Small Business'; dcf=sorted(os.listdir(f'{SRC}/assets/{DCG}'))
ww=[f for f in dcf if f.endswith('-workwear.webp')]; nv=[f for f in dcf if f.endswith('-novelty.webp')]
img=lambda f:f'<img src="site/assets/{DCG}/{f}">'
dcs=(f'<section class="dcs"><span class="eyebrow">07 · DC Small Business series</span><h2>Four fake contractors</h2>'
 '<p class="lede">Deadpan workwear named for four Washington landmark projects. Each shirt is shown beside the place it points at: the East Wing, the Kennedy Center facade, the Reflecting Pool, and the arch with the regilded bridge horses. The joke is only the company name.</p>'
 '<table><thead><tr><th>Brand</th><th>Landmark</th><th>Tagline</th><th>Blank and ink</th></tr></thead><tbody>'
 '<tr><td><b>Big Balls Demolition &amp; Remodel</b></td><td>The East Wing</td><td>Tear it down. Build it better.</td><td>Safety orange · black</td></tr>'
 '<tr><td><b>Hard Letters Signage Co.</b></td><td>The Kennedy Center</td><td>Banners · Signs · Wraps</td><td>Hi-vis yellow · black</td></tr>'
 '<tr><td><b>Lincoln Blue Pool &amp; Paint</b></td><td>The Reflecting Pool</td><td>Keep it blue.</td><td>Heather navy · white + light blue</td></tr>'
 '<tr><td><b>Triumphal Erection Co.</b></td><td>The arch + the gold horses</td><td>Raise the standard.</td><td>Black · metallic gold</td></tr></tbody></table>'
 f'{img(ww[0])}</section>'
 f'<section class="dcs"><span class="eyebrow">07 · DC Small Business series</span><h2>Workwear edition</h2>{"".join(img(f) for f in ww[1:3])}</section>'
 f'<section class="dcs"><span class="eyebrow">07 · DC Small Business series</span><h2>Workwear edition</h2>{img(ww[3])}'
 '<h3>Rules for the series</h3><ul><li>Play it straight: left-chest logo, clean back print, one or two inks, a sincere trade tagline.</li><li>Show every shirt beside its landmark, drawn flat. No photos.</li><li>Aim at the projects, never at a named person. No names, faces or likenesses.</li><li>Every factual premise is true and dated in the caption.</li><li>Print: Triumphal gold is metallic ink; check workwear blank shades with the vendor.</li></ul></section>'
 f'<section class="dcs"><span class="eyebrow">07 · DC Small Business series</span><h2>Novelty edition</h2><p class="lede">The louder cartoon version: mascots, ribbon banners and innuendo service lines. A limited drop, not the line.</p><div class="grid2">{"".join(img(f) for f in nv)}</div></section>')
toc=''.join(f'<li><span>{i+1:02d}</span>{a}<em>{b}</em></li>' for i,(a,b,_) in enumerate(secs))+'<li><span>05</span>Tokens<em>Color, type, space, shape</em></li><li><span>06</span>Components<em>UI and collateral, with rules</em></li><li><span>07</span>DC Small Business series<em>Four landmark shirts, workwear and novelty</em></li><li><span>08</span>Concept collateral<em>Posters, merch and hats from the rounds</em></li>'
doc=f'''<!doctype html><html lang="en" data-theme="light"><head><meta charset="utf-8"><title>Crooked Concept Brand Book</title>
<link rel="stylesheet" href="site/tokens.css"><link rel="stylesheet" href="book.css"></head><body>
<section class="cover"><span class="eyebrow">Crooked homepage concept · Brand and design system · v1.2 · Nov 2026</span>
<div><div class="wm">Crooked</div><h1>Less doom.<br>More doing.</h1><p>Reference book: voice, tone, color, type, tokens, components and the concept collateral built from them.</p></div>
<p class="note">Unofficial design exploration. Not affiliated with, endorsed by or connected to Crooked Media. Names, show art and marks belong to their owners. The wordmark is a typeset stand-in, not the official logo.</p></section>
<section class="toc"><span class="eyebrow">Contents</span><h2>What's inside</h2><ol>{toc}</ol></section>
{''.join(f'<section class="prose"><span class="eyebrow">{i+1:02d} · {b}</span><h2>{a}</h2>{c}</section>' for i,(a,b,c) in enumerate(secs))}
<section class="prose"><span class="eyebrow">05 · Tokens</span><h2>Color primitives</h2><div class="sws">{sw}</div></section>
<section class="prose"><span class="eyebrow">05 · Tokens</span><h2>Semantic and component color</h2><table><thead><tr><th>Token</th><th>Light</th><th>Dark</th><th>Use</th></tr></thead><tbody>{semrows}</tbody></table></section>
<section class="prose"><span class="eyebrow">05 · Tokens</span><h2>Type</h2><div class="tys">{ty}</div><h3>Spacing</h3><table><tbody>{rows("spacing")}</tbody></table><h3>Radius</h3><table><tbody>{rows("radius")}</tbody></table><h3>Shadow, sizes, layers</h3><table><tbody>{rows("shadow")}{rows("size")}{rows("zIndex")}</tbody></table></section>
{cmp}{dcs}{ast}
<section class="back"><div class="wm">Crooked</div><p>Crooked homepage concept · Brand and design system reference book · v1.2 · Nov 3, 2026.</p><p>Unofficial concept. Not affiliated with Crooked Media.</p></section>
</body></html>'''
open('book.html','w').write(doc)
