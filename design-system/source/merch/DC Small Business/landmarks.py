# Adds a landmark reference panel to each DC workwear presentation sheet.
exec(open("/home/claude/dcbiz2/build.py").read())
import os
os.chdir("/home/claude/dcbiz2")
NV = "#0A1A44"; SKYBG = "#DCE7F7"; GRN = "#6E8B3D"; GOLDF = "#E0B23A"; WH = "#FBFBF8"; YEL = "#FFD43B"; BLU = "#1F5BFF"

east = f'''<svg viewBox="0 0 520 330" class="lms">
<rect width="520" height="330" fill="{SKYBG}"/><rect y="270" width="520" height="60" fill="{GRN}"/>
<g stroke="{NV}" stroke-width="3" stroke-linejoin="round">
<rect x="60" y="150" width="250" height="122" fill="{WH}"/>
<rect x="56" y="140" width="258" height="12" fill="{WH}"/>
<path d="M130 140 L185 104 L240 140Z" fill="{WH}"/>
<g fill="{WH}">{''.join(f'<rect x="{x}" y="152" width="10" height="118"/>' for x in range(138,236,19))}</g>
<g fill="#C9D3E6">{''.join(f'<rect x="{x}" y="{y}" width="16" height="22"/>' for x in (76,104,258,286) for y in (168,222))}</g>
<path d="M185 104 V70" /><path d="M185 72 h26 v14 h-26" fill="#E5383B"/>
</g>
<rect x="318" y="160" width="150" height="110" fill="none" stroke="{NV}" stroke-width="3" stroke-dasharray="9 7"/>
<text x="393" y="222" text-anchor="middle" font-family="PM" font-size="11" fill="{NV}" letter-spacing="1">EAST WING</text>
<g fill="#B9B2A3" stroke="{NV}" stroke-width="2.5"><path d="M318 272 L340 244 L362 258 L384 236 L410 256 L438 240 L468 272Z"/></g>
<g stroke="{NV}" stroke-width="4" fill="none"><path d="M496 272 V40 M496 40 L350 40 M496 70 L470 40"/></g>
<rect x="488" y="266" width="20" height="10" fill="{NV}"/>
<path d="M410 40 L398 112" stroke="{NV}" stroke-width="2.5" stroke-dasharray="4 3"/>
<circle cx="396" cy="128" r="18" fill="#3A3D44" stroke="{NV}" stroke-width="3"/>
<g stroke="{NV}" stroke-width="2" fill="{GOLDF}"><path d="M440 40 v18"/><path d="M428 58 h24 l-4 12 h-16z"/><circle cx="440" cy="76" r="4"/></g>
</svg>'''

kc = f'''<svg viewBox="0 0 520 330" class="lms">
<rect width="520" height="330" fill="{SKYBG}"/><rect y="262" width="520" height="68" fill="{BLU}" opacity=".55"/>
<g stroke="{NV}" stroke-width="2" opacity=".5" fill="none"><path d="M40 290 q12 -6 24 0 t24 0"/><path d="M320 304 q12 -6 24 0 t24 0"/></g>
<rect x="30" y="120" width="460" height="22" fill="#E9E4D8" stroke="{NV}" stroke-width="3"/>
<rect x="44" y="142" width="432" height="112" fill="#F4F1EA" stroke="{NV}" stroke-width="3"/>
<g fill="{GOLDF}">{''.join(f'<rect x="{x}" y="142" width="5" height="112"/>' for x in range(52,470,16))}</g>
<rect x="30" y="252" width="460" height="10" fill="{NV}"/>
<g fill="{NV}">{''.join(f'<rect x="{x}" y="126" width="9" height="10"/>' for x in list(range(60,190,13))+list(range(330,460,13)))}</g>
<rect x="202" y="125" width="116" height="12" fill="none" stroke="#E5383B" stroke-width="2" stroke-dasharray="4 3"/>
<g transform="translate(256 168) rotate(24)"><path d="M-16 -14 h32 v8 h-11 v26 h-10 v-26 h-11z" fill="{GOLDF}" stroke="{NV}" stroke-width="2.5"/></g>
<g stroke="{NV}" stroke-width="2.5" stroke-linecap="round"><path d="M226 150 l-10 -6 M232 162 l-12 0 M286 152 l10 -6"/></g>
<g transform="translate(330 60)"><rect x="0" y="0" width="58" height="22" rx="4" fill="#7A4A1E" stroke="{NV}" stroke-width="2.5" transform="rotate(-20)"/><rect x="24" y="14" width="9" height="40" fill="#7A4A1E" stroke="{NV}" stroke-width="2.5" transform="rotate(-20)"/></g>
</svg>'''

lincoln = f'''<svg viewBox="0 0 520 330" class="lms">
<rect width="520" height="330" fill="{SKYBG}"/>
<g fill="#4E7A3A">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x,y,r in [(40,188,34),(88,196,28),(480,188,34),(432,196,28),(20,230,30),(500,230,30)])}</g>
<g stroke="{NV}" stroke-width="3" stroke-linejoin="round">
<rect x="150" y="70" width="220" height="26" fill="#F4F1EA"/><rect x="140" y="96" width="240" height="10" fill="#F4F1EA"/>
<g fill="#F4F1EA">{''.join(f'<rect x="{x}" y="106" width="12" height="76"/>' for x in range(154,370,27))}</g>
<rect x="132" y="182" width="256" height="10" fill="#E9E4D8"/><rect x="120" y="192" width="280" height="10" fill="#E9E4D8"/>
</g>
<rect x="0" y="202" width="520" height="128" fill="{GRN}"/>
<path d="M200 206 L320 206 L470 330 L50 330 Z" fill="{BLU}" stroke="{NV}" stroke-width="3"/>
<g stroke="#9CC2FF" stroke-width="3" fill="none" stroke-linecap="round"><path d="M220 230 h40 M290 252 h50 M160 286 h60 M300 300 h70"/></g>
<g transform="translate(236 210)"><path d="M48 0 L52 -64 L54 -70 L56 -64 L60 0Z" fill="#F4F1EA" stroke="{NV}" stroke-width="2" opacity=".6"/></g>
</svg>'''

def horse(x, flip):
    t = f"translate({x} 200)" + (" scale(-1 1)" if flip else "")
    return f'''<g transform="{t}"><rect x="-34" y="66" width="68" height="34" fill="#D9D2C2" stroke="{NV}" stroke-width="3"/>
<path d="M-28 66 L-26 34 Q-34 22 -24 12 L4 10 Q14 -8 24 -18 L30 -14 Q28 -4 34 2 L40 14 L32 18 L24 12 Q22 24 18 30 L18 66 L10 66 L10 36 L-16 36 L-18 66Z" fill="{GOLDF}" stroke="{NV}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M-6 10 Q-2 -14 8 -24 L14 -18 Q6 -2 6 10Z" fill="{GOLDF}" stroke="{NV}" stroke-width="2"/></g>'''
arch = f'''<svg viewBox="0 0 520 330" class="lms">
<rect width="520" height="330" fill="{SKYBG}"/><rect y="300" width="520" height="30" fill="#B9C3D6"/>
<g stroke="{NV}" stroke-width="3" stroke-linejoin="round">
<rect x="186" y="66" width="148" height="24" fill="#F4F1EA"/>
<path fill-rule="evenodd" d="M194 90 H326 V300 H194 Z M236 300 V196 A24 24 0 0 1 284 196 V300 Z" fill="#F4F1EA"/>
<path d="M260 66 L248 40 L260 46 L272 40Z" fill="{GOLDF}"/><circle cx="260" cy="34" r="7" fill="{GOLDF}"/>
<path d="M230 62 q10 -14 22 -4 M290 62 q-10 -14 -22 -4" fill="none"/>
<g fill="{GOLDF}"><rect x="182" y="284" width="16" height="16"/><rect x="322" y="284" width="16" height="16"/></g>
</g>
<text x="260" y="84" text-anchor="middle" font-family="PM" font-size="9" fill="{NV}" letter-spacing="1">ONE NATION UNDER GOD</text>
<g stroke="{NV}" stroke-width="2" stroke-dasharray="5 4"><path d="M352 66 V300"/><path d="M346 66 h12 M346 300 h12"/></g>
<text x="364" y="186" font-family="PM" font-size="11" fill="{NV}">250 FT</text>
{horse(76, False)}{horse(444, True)}
</svg>'''

LM = {
 "bb": (east, "The East Wing", "Demolished in Oct 2025 to make room for a White House ballroom."),
 "hl": (kc, "The Kennedy Center", "Name added to the facade in Dec 2025, taken down by court order in June 2026."),
 "lb": (lincoln, "The Reflecting Pool", "Drained, repainted “American flag blue” and refilled in June 2026."),
 "te": (arch, "The arch + the gold horses", "A 250-ft arch planned for Memorial Circle; the bridge horses were regilded in Aug 2026."),
}
css += f'''
.pair .st{{grid-template-columns:520px 1fr 1fr}}
.pair .st .g{{width:560px}}
.lmp{{align-self:center;margin:30px 0 0 30px;background:#fff;border:1px solid #D5DBEA;border-radius:18px;overflow:hidden;display:flex;flex-direction:column}}
.lms{{display:block;width:100%;height:auto}}
.lmp .cap{{padding:20px 22px 24px;display:grid;gap:8px}}
.lmp .cap .ey{{font:500 11px PM;letter-spacing:.12em;text-transform:uppercase;color:#56618A}}
.lmp .cap b{{font:900 34px/.92 BSD;text-transform:uppercase;color:{NV}}}
.lmp .cap span{{font:600 15px/1.35 PS;color:#33406B}}
'''
def pair(k, i, n, cw, tag, col, bg):
    svg, title, fact = LM[k]
    front = tee(col, fo(318, 150, 92, 80, C[k]), id=i.replace("-", "") + "f")
    back = tee(col, fo(155, 130, 290, 300, B[k]), id=i.replace("-", "") + "b")
    return f'''<section class="pair" id="{i}"><div class="st" style="background:{bg}"><span class="tag">Crooked merch concept · DC Small Business series · Workwear edition</span>
<div class="lmp">{svg}<div class="cap"><span class="ey">The reference</span><b>{title}</b><span>{fact}</span></div></div>
{front}{back}<span class="vw" style="left:47%">Front · left chest</span><span class="vw" style="left:80%">Back</span></div>
<div class="lab2"><div><h3>{n}</h3><p>{cw}</p></div><div class="mono">"{tag}"<br>Unofficial parody concept · Not affiliated with Crooked Media</div></div></section>'''
open("dc.html", "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}body{{gap:40px}}</style></head><body>{''.join(pair(*p) for p in P)}</body></html>")
