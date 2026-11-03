# "DC Small Business" novelty-shirt series — four fake-business back prints.
import os, base64
os.chdir("/home/claude/round2")
exec(open("/home/claude/round2/merch.py").read().split("\nA = {}")[0])   # tee() helper, fonts, colors
os.chdir("/home/claude/dcbiz")
F = "/home/claude/kit/fonts/"
def b64(f): return base64.b64encode(open(F + f, "rb").read()).decode()
css += f'''
@font-face{{font-family:"LOB";src:url(data:font/ttf;base64,{b64("Lobster-Regular.ttf")}) format("truetype")}}
@font-face{{font-family:"ALFA";src:url(data:font/ttf;base64,{b64("AlfaSlabOne-Regular.ttf")}) format("truetype")}}
'''
GOLDDEF = '''<defs><linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBE88A"/><stop offset=".45" stop-color="#E0B23A"/><stop offset=".7" stop-color="#9C7016"/><stop offset="1" stop-color="#F3D163"/></linearGradient></defs>'''

# ---------- 1. Big Balls Demolition & Remodel (East Wing)
ball_svg = '''<svg viewBox="0 0 300 175" width="300" height="175">
<path d="M0 6 L150 14" stroke="#111" stroke-width="7" stroke-linecap="round"/><path d="M0 6 L150 14" stroke="#F2C230" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M140 14 L112 64" stroke="#333" stroke-width="4" stroke-dasharray="5 3"/>
<g transform="translate(176 72)"><path d="M0 30 L58 4 L116 30Z" fill="#fff" stroke="#111" stroke-width="3"/><rect x="2" y="30" width="112" height="70" fill="#fff" stroke="#111" stroke-width="3"/>
<g fill="#E9E4D8" stroke="#111" stroke-width="2"><rect x="12" y="36" width="10" height="58"/><rect x="38" y="36" width="10" height="58"/><rect x="64" y="36" width="10" height="58"/><rect x="90" y="36" width="10" height="58"/></g>
<path d="M2 50 L20 58 L8 72 L26 84" fill="none" stroke="#111" stroke-width="3"/><rect x="2" y="96" width="112" height="6" fill="#111"/></g>
<g fill="#fff" stroke="#111" stroke-width="2"><path d="M168 70 l10 -6 l4 9z"/><path d="M160 96 l12 2 l-6 9z"/><path d="M172 124 l9 -3 l2 9z"/></g>
<g fill="#F7D046" stroke="#111" stroke-width="1.5"><path d="M182 52 l3 -8 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3z"/><path d="M270 50 l2 -6 l2 6 l6 2 l-6 2 l-2 6 l-2 -6 l-6 -2z"/></g>
<circle cx="104" cy="108" r="54" fill="#3A3D44" stroke="#111" stroke-width="5"/>
<ellipse cx="84" cy="86" rx="16" ry="10" fill="#fff" opacity=".22" transform="rotate(-30 84 86)"/>
<path d="M54 74 Q104 18 154 74 Z" fill="#F2C230" stroke="#111" stroke-width="4"/><rect x="44" y="70" width="120" height="10" rx="5" fill="#F2C230" stroke="#111" stroke-width="4"/>
<rect x="98" y="34" width="12" height="38" fill="#E0A81E" stroke="#111" stroke-width="2"/>
<ellipse cx="86" cy="100" rx="11" ry="13" fill="#fff" stroke="#111" stroke-width="3"/><circle cx="89" cy="102" r="5" fill="#111"/>
<path d="M112 100 Q122 92 132 100" fill="none" stroke="#111" stroke-width="4" stroke-linecap="round"/>
<path d="M76 122 Q104 150 136 120 Q106 132 76 122Z" fill="#7A1010" stroke="#111" stroke-width="3"/><path d="M96 134 Q106 128 118 134 Q108 142 96 134Z" fill="#E5383B"/>
</svg>'''
A1 = f'''<div class="art art1">
<div class="scr" style="font-size:70px;color:#fff;-webkit-text-stroke:3px #111;paint-order:stroke fill;text-shadow:5px 5px 0 #C8102E;line-height:1.1;white-space:nowrap">Big Balls</div>
<div class="rib dark">⬢&nbsp; DEMOLITION &amp; REMODEL &nbsp;⬢</div>
{ball_svg}
<div class="rib light scr" style="font-size:19px">“We bust out the old wing and put in something huge.”</div>
<div class="svc" style="color:#111">Historic demolition · Review optional · Gold fixtures on request · Donors welcome</div></div>'''

# ---------- 2. Hard Letters Signage Co. (Kennedy Center)
t_svg = '''<svg viewBox="0 0 130 210" width="124" height="200">
<g stroke="#8A5A2B" stroke-width="6" stroke-linecap="round"><path d="M18 205 L72 6"/><path d="M52 210 L106 12"/></g>
<g stroke="#8A5A2B" stroke-width="5"><path d="M26 176 L60 182"/><path d="M36 140 L70 146"/><path d="M46 104 L80 110"/><path d="M56 68 L90 74"/><path d="M66 32 L100 38"/></g>
<g transform="rotate(-14 66 112)">
<path d="M26 64 L106 64 L106 86 L78 86 L78 168 L54 168 L54 86 L26 86Z" fill="#F2B530" stroke="#111" stroke-width="4" stroke-linejoin="round"/>
<path d="M40 64 Q66 34 92 64Z" fill="#F7D046" stroke="#111" stroke-width="3"/><rect x="34" y="60" width="64" height="7" rx="3" fill="#F7D046" stroke="#111" stroke-width="3"/>
<ellipse cx="58" cy="100" rx="6" ry="8" fill="#fff" stroke="#111" stroke-width="2"/><ellipse cx="74" cy="100" rx="6" ry="8" fill="#fff" stroke="#111" stroke-width="2"/>
<circle cx="58" cy="102" r="3" fill="#111"/><circle cx="74" cy="102" r="3" fill="#111"/>
<ellipse cx="66" cy="122" rx="7" ry="5" fill="#7A1010" stroke="#111" stroke-width="2"/>
<path d="M88 92 q4 6 0 10 q-4 -4 0 -10z" fill="#5FB6F0" stroke="#111" stroke-width="1.5"/>
<path d="M54 120 L30 140" stroke="#111" stroke-width="4"/><circle cx="28" cy="142" r="7" fill="#fff" stroke="#111" stroke-width="3"/>
<path d="M78 120 L102 104" stroke="#111" stroke-width="4"/><circle cx="104" cy="102" r="7" fill="#fff" stroke="#111" stroke-width="3"/>
<path d="M60 168 L52 194 M72 168 L80 194" stroke="#111" stroke-width="4"/>
<path d="M40 196 q10 -8 20 0 l-2 6 h-20z" fill="#C8102E" stroke="#111" stroke-width="2.5"/><path d="M74 196 q10 -8 20 0 l2 6 h-20z" fill="#C8102E" stroke="#111" stroke-width="2.5"/>
</g>
<g transform="rotate(32 108 22)"><rect x="96" y="2" width="30" height="16" rx="3" fill="#7A4A1E" stroke="#111" stroke-width="3"/><rect x="108" y="18" width="6" height="26" fill="#7A4A1E" stroke="#111" stroke-width="2.5"/></g>
<g stroke="#111" stroke-width="2.5" stroke-linecap="round"><path d="M76 34 l-6 -6 M84 30 l-2 -9 M90 32 l4 -7"/></g>
</svg>'''
A2 = f'''<div class="art art2">
<div class="blk" style="font-size:58px;color:#111;-webkit-text-stroke:5px #C8102E;paint-order:stroke fill;letter-spacing:.02em;white-space:nowrap">Hard Letters</div>
<div class="scr" style="font-size:44px;color:#C8102E;-webkit-text-stroke:2px #111;paint-order:stroke fill;text-shadow:3px 3px 0 #111;margin:-2px 0 6px 40px;line-height:1.1;white-space:nowrap">Signage Co.</div>
<div style="display:flex;align-items:center;gap:6px">{t_svg}
<div style="text-align:left"><div class="alfa" style="font-size:18px;line-height:1.05;color:#111;white-space:nowrap">WE GET IT UP<br>OVERNIGHT.</div>
<div class="alfa" style="font-size:18px;line-height:1.05;color:#111;margin-top:8px;white-space:nowrap">JUDGES GET IT<br>DOWN BY NOON.</div>
<div style="height:5px;background:#C8102E;margin-top:10px;border-radius:2px"></div></div></div>
<div class="svc" style="color:#111;font-size:9.5px;margin-top:8px">– Facade lettering · Same-day removal · Performance issues? Ask your arts center</div></div>'''

# ---------- 3. Lincoln Blue Pool & Paint (Reflecting Pool)
pool_svg = '''<svg viewBox="0 0 300 300" width="270" height="270">
<defs><path id="topArc" d="M42 150 A108 108 0 0 1 258 150"/><path id="botArc" d="M38 150 A112 112 0 0 0 262 150"/>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB86B"/><stop offset=".55" stop-color="#FFE3A3"/><stop offset="1" stop-color="#FFF5D6"/></linearGradient>
<clipPath id="inner"><circle cx="150" cy="150" r="98"/></clipPath></defs>
<circle cx="150" cy="150" r="140" fill="#0A1A44" stroke="#111" stroke-width="4"/>
<circle cx="150" cy="150" r="102" fill="#FFF5D6" stroke="#E5383B" stroke-width="5"/>
<g clip-path="url(#inner)">
<rect x="40" y="40" width="220" height="220" fill="url(#sky)"/>
<circle cx="214" cy="140" r="24" fill="#E5383B" opacity=".9"/>
<path d="M70 172 L74 82 L76 74 L78 82 L82 172Z" fill="#fff" stroke="#0A1A44" stroke-width="2.5"/>
<rect x="40" y="168" width="220" height="10" fill="#6E8B3D"/>
<rect x="40" y="176" width="220" height="90" fill="#1F5BFF"/>
<g stroke="#9CC2FF" stroke-width="2.5" fill="none" stroke-linecap="round"><path d="M60 194 q10 -5 20 0 t20 0"/><path d="M188 208 q10 -5 20 0 t20 0"/><path d="M70 230 q10 -5 20 0 t20 0"/></g>
<g transform="translate(96 108)">
<rect x="0" y="0" width="74" height="40" rx="18" fill="#F7D046" stroke="#111" stroke-width="3.5"/>
<g stroke="#C9A12A" stroke-width="2"><path d="M14 4 v32 M28 4 v32 M42 4 v32 M56 4 v32"/></g>
<ellipse cx="26" cy="18" rx="10" ry="8" fill="#9FD8FF" stroke="#111" stroke-width="3"/><ellipse cx="48" cy="18" rx="10" ry="8" fill="#9FD8FF" stroke="#111" stroke-width="3"/>
<path d="M36 18 h2" stroke="#111" stroke-width="3"/><circle cx="27" cy="19" r="3" fill="#111"/><circle cx="49" cy="19" r="3" fill="#111"/>
<path d="M62 22 q14 -2 14 -24" fill="none" stroke="#E5383B" stroke-width="5" stroke-linecap="round"/><rect x="70" y="-30" width="10" height="8" rx="2" fill="#E5383B" stroke="#111" stroke-width="2"/>
<path d="M28 32 q9 6 18 0" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round"/>
<path d="M37 40 L37 54" stroke="#111" stroke-width="5"/>
<rect x="20" y="52" width="34" height="18" rx="4" fill="#E5383B" stroke="#111" stroke-width="3"/><path d="M37 52 v18" stroke="#111" stroke-width="2"/>
<path d="M28 70 L24 82 M46 70 L50 82" stroke="#111" stroke-width="4"/>
<path d="M2 20 L-14 4" stroke="#111" stroke-width="4"/><circle cx="-16" cy="2" r="6" fill="#fff" stroke="#111" stroke-width="3"/>
</g>
<rect x="40" y="186" width="220" height="80" fill="#1F5BFF" opacity=".55"/>
</g>
<text font-family="ALFA" font-size="30" fill="#FFF5D6" letter-spacing="3"><textPath href="#topArc" startOffset="50%" text-anchor="middle">LINCOLN BLUE</textPath></text>
<text font-family="ALFA" font-size="17" fill="#F7D046" letter-spacing="2"><textPath href="#botArc" startOffset="50%" text-anchor="middle" dominant-baseline="hanging">POOL &amp; PAINT · EST. 2026</textPath></text>
<g fill="#F7D046"><circle cx="34" cy="150" r="5"/><circle cx="266" cy="150" r="5"/></g>
</svg>'''
A3 = f'''<div class="art art3">{pool_svg}
<div class="rib navy scr" style="font-size:24px;margin-top:-6px">It’s not how deep it is.<br>It’s what color.</div>
<div class="svc" style="color:#0A1A44">Drain · Paint · Refill · Flag blue, one coat or two · Shallow work since 2026</div></div>'''

# ---------- 4. Triumphal Erection Co. (arch + gold horses)
def horse(x, flip=False):
    t = f'translate({x} 70)' + (' scale(-1 1) translate(-60 0)' if flip else '')
    return f'''<g transform="{t}">
<rect x="6" y="84" width="48" height="16" fill="url(#gold)" stroke="#111" stroke-width="2.5"/>
<path d="M14 84 L14 64 Q4 54 8 38 Q12 22 26 14 L30 2 L38 13 Q50 17 56 32 L58 46 Q52 54 42 48 L36 46 Q34 58 46 66 L46 84 Z" fill="url(#gold)" stroke="#111" stroke-width="3" stroke-linejoin="round"/>
<path d="M14 40 q-6 -4 -4 -12 M16 54 q-8 -2 -8 -10" fill="none" stroke="#111" stroke-width="2"/>
<rect x="30" y="24" width="22" height="9" rx="3" fill="#111"/><path d="M30 28 h-6" stroke="#111" stroke-width="2.5"/>
<path d="M44 42 q6 2 10 -2" fill="none" stroke="#111" stroke-width="2.5" stroke-linecap="round"/>
</g>'''
arch_svg = f'''<svg viewBox="0 0 300 190" width="300" height="190">{GOLDDEF}
{horse(4)}{horse(236, True)}
<g transform="translate(78 0)">
<path d="M70 2 l5 10 l11 1 l-8 7 l3 11 l-11 -6 l-11 6 l3 -11 l-8 -7 l11 -1z" fill="url(#gold)" stroke="#111" stroke-width="2"/>
<rect x="6" y="30" width="132" height="16" fill="url(#gold)" stroke="#111" stroke-width="3"/>
<path fill-rule="evenodd" d="M12 46 H132 V160 H12 Z M50 160 V108 A22 22 0 0 1 94 108 V160 Z" fill="url(#gold)" stroke="#111" stroke-width="3"/>
<g stroke="#8C6512" stroke-width="2"><path d="M22 52 v100 M122 52 v100"/></g>
<ellipse cx="58" cy="70" rx="8" ry="6" fill="#fff" stroke="#111" stroke-width="2.5"/><ellipse cx="86" cy="70" rx="8" ry="6" fill="#fff" stroke="#111" stroke-width="2.5"/>
<path d="M52 64 l12 3 M92 64 l-12 3" stroke="#111" stroke-width="3" stroke-linecap="round"/>
<circle cx="60" cy="71" r="3" fill="#111"/><circle cx="88" cy="71" r="3" fill="#111"/>
<path d="M58 88 Q72 98 88 86" fill="none" stroke="#111" stroke-width="3.5" stroke-linecap="round"/>
<path d="M12 100 Q-10 98 -12 76 Q-14 60 -2 58" fill="none" stroke="#111" stroke-width="13" stroke-linecap="round"/><path d="M12 100 Q-10 98 -12 76 Q-14 60 -2 58" fill="none" stroke="url(#gold)" stroke-width="8" stroke-linecap="round"/>
<circle cx="-2" cy="54" r="9" fill="#fff" stroke="#111" stroke-width="3"/>
<path d="M132 100 Q154 98 156 76 Q158 60 146 58" fill="none" stroke="#111" stroke-width="13" stroke-linecap="round"/><path d="M132 100 Q154 98 156 76 Q158 60 146 58" fill="none" stroke="url(#gold)" stroke-width="8" stroke-linecap="round"/>
<circle cx="146" cy="54" r="9" fill="#fff" stroke="#111" stroke-width="3"/>
<path d="M30 160 L28 176 M114 160 L116 176" stroke="#111" stroke-width="5"/>
<path d="M14 178 q12 -10 26 0 l-2 7 h-24z" fill="#fff" stroke="#111" stroke-width="2.5"/><path d="M104 178 q12 -10 26 0 l2 7 h-24z" fill="#fff" stroke="#111" stroke-width="2.5"/>
</g></svg>'''
A4 = f'''<div class="art art4">
<div class="alfa goldtxt" style="font-size:43px;letter-spacing:.03em;white-space:nowrap">TRIUMPHAL</div>
<div class="scr goldtxt" style="font-size:52px;margin-top:-4px;line-height:1.15;white-space:nowrap">Erection Co.</div>
{arch_svg}
<div class="rib goldrib scr" style="font-size:19px;white-space:nowrap">World’s biggest. Still compensating.</div>
<div class="svc" style="color:#E0B23A">Erections up to 250 ft · Gold-plated stallions · Taxpayer financed · Foot of the bridge</div></div>'''

ORANGE = "#F26A21"; HIVIS = "#D6EE3A"; HEATHER = "#BFC2C8"; BLACK = "#16171B"
P = [
 ("dc-big-balls", "Big Balls Demolition & Remodel", "Safety orange tee · back print", "The East Wing", ORANGE, A1),
 ("dc-hard-letters", "Hard Letters Signage Co.", "Hi-vis yellow tee · back print", "The Kennedy Center", HIVIS, A2),
 ("dc-lincoln-blue", "Lincoln Blue Pool & Paint", "Heather grey tee · back print", "The Reflecting Pool", HEATHER, A3),
 ("dc-triumphal", "Triumphal Erection Co.", "Black tee · metallic gold back print", "The arch + the gold horses", BLACK, A4),
]
css += f'''
.scr{{font-family:LOB;font-weight:400}}.alfa{{font-family:ALFA;font-weight:400}}.blk{{font-family:BSD;font-weight:900;text-transform:uppercase;line-height:.9}}
.art{{width:300px;text-align:center;display:flex;flex-direction:column;align-items:center}}
.rib{{display:inline-block;padding:5px 16px;border-radius:6px;margin:6px 0}}
.rib.dark{{background:#1A1A1A;color:#fff;font:400 15px/1.2 ALFA;letter-spacing:.06em;box-shadow:0 0 0 3px #fff,0 0 0 5px #111;margin:10px 0 6px}}
.rib.light{{background:#fff;color:#111;box-shadow:0 0 0 3px #111;border-bottom:4px solid #C8102E;line-height:1.15;padding:6px 12px}}
.rib.navy{{background:#0A1A44;color:#FFF5D6;box-shadow:0 0 0 3px #FFF5D6,0 0 0 5px #0A1A44;line-height:1.1;padding:8px 16px}}
.rib.goldrib{{background:#111;color:#F3D163;box-shadow:0 0 0 2px #E0B23A,0 0 0 5px #111,0 0 0 7px #E0B23A}}
.goldtxt{{background:linear-gradient(180deg,#FBE88A,#E0B23A 45%,#9C7016 70%,#F3D163);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-stroke:1px rgba(0,0,0,.25)}}
.svc{{font:400 9px/1.35 ALFA;letter-spacing:.04em;text-transform:uppercase;margin-top:6px;max-width:290px}}
.sheet{{width:1700px;height:1000px;background:#fff;border-radius:22px;overflow:hidden;display:grid;grid-template-columns:860px 1fr;flex:none;position:relative}}
.sheet .left{{background:#E9ECF4;display:grid;place-items:center;position:relative}}
.sheet .left .g{{width:780px}}
.sheet .right{{display:flex;flex-direction:column}}
.sheet .swatch{{flex:1;display:grid;place-items:center}}
.sheet .swatch .zoom{{transform:scale(var(--z,1.5));transform-origin:center}}
.sheet .lab2{{padding:24px 34px;border-top:1px solid #D5DBEA;display:flex;justify-content:space-between;align-items:flex-end;gap:16px}}
.sheet .lab2 h3{{margin:0;font:900 44px/.9 BSD;text-transform:uppercase;color:#0A1A44}}
.sheet .lab2 p{{margin:8px 0 0;font:600 17px/1.3 PS;color:#56618A}}
.sheet .lab2 .mono{{font-size:12px;color:#56618A;text-align:right}}
.sheet .tag{{position:absolute;top:24px;left:30px;font:500 12px PM;letter-spacing:.1em;text-transform:uppercase;color:#56618A;z-index:2}}
.sheet .unoff{{position:absolute;bottom:18px;left:30px;font:500 11px PM;letter-spacing:.08em;text-transform:uppercase;color:#56618A;opacity:.85}}
.sheet .vlab{{position:absolute;bottom:18px;right:24px;font:500 11px PM;letter-spacing:.1em;text-transform:uppercase;color:#56618A}}
'''
def card(i, n, cw, ref, col, art):
    zoom = 1.42
    shirt = tee(col, fo(150, 106, 300, 470, f'<div style="transform:scale(.88);transform-origin:top center">{art}</div>'), id=i.replace("-", ""))
    return f'''<section class="sheet" id="{i}"><span class="tag">Crooked merch concept · DC Small Business series</span>
<div class="left">{shirt}<span class="vlab">Back view</span><span class="unoff">Unofficial parody concept · Not affiliated with Crooked Media</span></div>
<div class="right"><div class="swatch" style="background:{col}"><div class="zoom" style="--z:{zoom}">{art}</div></div>
<div class="lab2"><div><h3>{n}</h3><p>{cw}</p></div><div class="mono">Inspired by:<br>{ref}</div></div></div></section>'''
cards = "".join(card(*p) for p in P)
open("dc.html", "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}body{{gap:40px}}</style></head><body>{cards}</body></html>")
ps = "".join(f'<div class="artwrap" id="art-{i}" style="display:inline-block;padding:24px">{art}</div>' for i, n, cw, ref, col, art in P)
open("art.html", "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}body{{background:transparent}}</style></head><body>{ps}</body></html>")
