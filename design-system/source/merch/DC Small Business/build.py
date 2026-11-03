# Deadpan contractor-workwear versions: left-chest logo + back print.
import os, base64
os.chdir("/home/claude/round2")
exec(open("/home/claude/round2/merch.py").read().split("\nA = {}")[0])
os.chdir("/home/claude/dcbiz2")
F = "/home/claude/kit/fonts/"
def b64(f): return base64.b64encode(open(F + f, "rb").read()).decode()
css += f'''@font-face{{font-family:"LOB";src:url(data:font/ttf;base64,{b64("Lobster-Regular.ttf")}) format("truetype")}}'''

K = "#141414"; GOLD = "#D9A93A"; WAVE = "#7FB3E8"; OFF = "#EEF1F6"

def roof(color, w, chimney=True, window=True):
    return f'''<svg viewBox="0 0 220 60" width="{w}" style="display:block;margin:0 auto">
<path d="M6 56 L110 8 L214 56" fill="none" stroke="{color}" stroke-width="10" stroke-linejoin="miter"/>
{f'<rect x="160" y="14" width="14" height="22" fill="{color}"/>' if chimney else ''}
{f'<g fill="{color}"><rect x="102" y="30" width="7" height="7"/><rect x="111" y="30" width="7" height="7"/><rect x="102" y="39" width="7" height="7"/><rect x="111" y="39" width="7" height="7"/></g>' if window else ''}</svg>'''
def peak(color, w):
    return f'''<svg viewBox="0 0 220 56" width="{w}" style="display:block;margin:0 auto">
<path d="M10 54 L110 6 L210 54 L184 54 L110 20 L36 54Z" fill="{color}"/></svg>'''
def waves(color, w):
    return f'''<svg viewBox="0 0 90 48" width="{w}" style="display:block">
<g fill="none" stroke="{color}" stroke-width="6" stroke-linecap="round">
<path d="M4 10 q10 -8 20 0 t20 0 t20 0 t20 0"/><path d="M4 24 q10 -8 20 0 t20 0 t20 0 t20 0"/><path d="M4 38 q10 -8 20 0 t20 0 t20 0 t20 0"/></g></svg>'''

B = {}  # back prints
C = {}  # left-chest logos
B["bb"] = f'''<div class="lk" style="color:{K}">{roof(K,250)}
<div class="h" style="font-size:52px;margin-top:-2px">BIG BALLS</div>
<div class="sub" style="font-size:16px;border-bottom:3px solid {K};padding-bottom:6px">DEMOLITION &amp; REMODEL</div>
<div class="h" style="font-size:24px;line-height:1.05;margin-top:22px">TEAR IT DOWN.<br>BUILD IT BETTER.</div></div>'''
C["bb"] = f'''<div class="lk" style="color:{K}">{roof(K,70,window=False)}<div class="h" style="font-size:17px;margin-top:-1px">BIG BALLS</div>
<div class="sub" style="font-size:6.4px;border-bottom:1.5px solid {K};padding-bottom:2px">DEMOLITION &amp; REMODEL</div></div>'''

B["hl"] = f'''<div class="lk" style="color:{K}"><div class="box" style="border:6px solid {K};padding:12px 30px 10px">
<div class="h" style="font-size:46px;line-height:.95">HARD<br>LETTERS</div><div class="sub" style="font-size:19px;margin-top:6px">SIGNAGE CO.</div></div>
<div class="h" style="font-size:16px;margin-top:20px;letter-spacing:.04em">BANNERS · SIGNS · WRAPS</div></div>'''
C["hl"] = f'''<div class="lk" style="color:{K}"><div class="box" style="border:3px solid {K};border-radius:8px;padding:4px 8px 3px">
<div class="h" style="font-size:15px;line-height:.95">HARD<br>LETTERS</div><div class="sub" style="font-size:6.5px;margin-top:2px">SIGNAGE CO.</div></div></div>'''

B["lb"] = f'''<div class="lk" style="color:{OFF};align-items:flex-start;text-align:left">
<div class="h" style="font-size:56px;line-height:.92">LINCOLN</div>
<div style="display:flex;align-items:center;gap:10px"><div class="h" style="font-size:56px;line-height:.92">BLUE</div>{waves(WAVE,96)}</div>
<div class="sub" style="font-size:22px;margin-top:6px;color:{OFF}">POOL &amp; PAINT</div>
<div class="scr" style="font-size:40px;color:{OFF};margin:22px 0 0 18px;transform:rotate(-4deg)">Keep It Blue.</div>
<svg viewBox="0 0 200 16" width="180" style="margin:-4px 0 0 40px"><path d="M4 12 Q100 -2 196 6" fill="none" stroke="{OFF}" stroke-width="4" stroke-linecap="round"/></svg></div>'''
C["lb"] = f'''<div class="lk" style="color:{OFF}">{waves(WAVE,40)}<div class="h" style="font-size:16px;line-height:.95;margin-top:2px">LINCOLN<br>BLUE</div>
<div class="sub" style="font-size:7px;margin-top:2px;color:{OFF}">POOL &amp; PAINT</div></div>'''

B["te"] = f'''<div class="lk" style="color:{GOLD}">{peak(GOLD,230)}
<div class="h" style="font-size:38px;line-height:.98;margin-top:4px">TRIUMPHAL<br>ERECTION CO.</div>
<div style="height:4px;background:{GOLD};width:100%;margin:12px 0 10px"></div>
<div class="h" style="font-size:19px;letter-spacing:.03em">RAISE THE STANDARD.</div></div>'''
C["te"] = f'''<div class="lk" style="color:{GOLD}">{peak(GOLD,60)}<div class="h" style="font-size:12.5px;line-height:1;margin-top:1px">TRIUMPHAL<br>ERECTION CO.</div></div>'''

ORANGE = "#F26A21"; HIVIS = "#D6EE3A"; NAVYT = "#24345A"; BLACKT = "#1A1B1F"
P = [("bb", "dc-big-balls", "Big Balls Demolition & Remodel", "Safety orange · black ink", "Tear it down. Build it better.", ORANGE, "#E9ECF4"),
     ("hl", "dc-hard-letters", "Hard Letters Signage Co.", "Hi-vis yellow · black ink", "Banners · Signs · Wraps", HIVIS, "#E9ECF4"),
     ("lb", "dc-lincoln-blue", "Lincoln Blue Pool & Paint", "Heather navy · white + light blue ink", "Keep it blue.", NAVYT, "#E9ECF4"),
     ("te", "dc-triumphal", "Triumphal Erection Co.", "Black · gold ink", "Raise the standard.", BLACKT, "#E9ECF4")]

css += f'''
.h{{font-family:PS;font-weight:900;letter-spacing:.01em;line-height:1;white-space:nowrap}}
.sub{{font-family:PS;font-weight:800;letter-spacing:.08em;white-space:nowrap}}
.scr{{font-family:LOB}}
.lk{{display:flex;flex-direction:column;align-items:center;text-align:center}}
.box{{display:flex;flex-direction:column;align-items:center}}
.pair{{width:1700px;height:900px;background:#fff;border-radius:22px;overflow:hidden;display:flex;flex-direction:column;flex:none}}
.pair .st{{flex:1;display:grid;grid-template-columns:1fr 1fr;align-items:center;justify-items:center;position:relative}}
.pair .st .g{{width:700px}}
.pair .vw{{position:absolute;bottom:14px;font:500 12px PM;letter-spacing:.1em;text-transform:uppercase;color:#56618A}}
.pair .tag{{position:absolute;top:20px;left:30px;font:500 12px PM;letter-spacing:.1em;text-transform:uppercase;color:#56618A}}
.pair .lab2{{padding:22px 34px;border-top:1px solid #D5DBEA;display:flex;justify-content:space-between;align-items:flex-end;gap:16px}}
.pair .lab2 h3{{margin:0;font:900 44px/.9 BSD;text-transform:uppercase;color:#0A1A44}}
.pair .lab2 p{{margin:8px 0 0;font:600 17px/1.3 PS;color:#56618A}}
.pair .lab2 .mono{{font-size:12px;color:#56618A;text-align:right}}
'''
def pair(k, i, n, cw, tag, col, bg):
    front = tee(col, fo(318, 150, 92, 80, C[k]), id=i.replace("-", "") + "f")
    back = tee(col, fo(155, 130, 290, 300, B[k]), id=i.replace("-", "") + "b")
    return f'''<section class="pair" id="{i}"><div class="st" style="background:{bg}"><span class="tag">Crooked merch concept · DC Small Business series · Workwear edition</span>
{front}{back}<span class="vw" style="left:22%">Front · left chest</span><span class="vw" style="left:72%">Back</span></div>
<div class="lab2"><div><h3>{n}</h3><p>{cw}</p></div><div class="mono">"{tag}"<br>Unofficial parody concept · Not affiliated with Crooked Media</div></div></section>'''
open("dc.html", "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}body{{gap:40px}}</style></head><body>{''.join(pair(*p) for p in P)}</body></html>")
arts = "".join(f'<div class="aw" id="art-{i}-back" style="display:inline-block;padding:20px;width:320px">{B[k]}</div><div class="aw" id="art-{i}-chest" style="display:inline-block;padding:8px">{C[k]}</div>' for k, i, *_ in P)
open("art.html", "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}body{{background:transparent}}</style></head><body>{arts}</body></html>")
