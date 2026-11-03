exec(open("/home/claude/dcbiz2/build.py").read())
import os
os.chdir("/home/claude/dcbiz2")
names={"bb":"Big Balls Demolition tee","hl":"Hard Letters Signage tee","lb":"Lincoln Blue Pool tee","te":"Triumphal Erection tee"}
specs={"bb":"Safety orange · black ink · chest + back","hl":"Hi-vis yellow · black ink · chest + back","lb":"Heather navy · white + light blue · chest + back","te":"Black · gold ink · chest + back"}
cards=""
for k,i,n,cw,tag,col,bg in P:
    svg=tee(col, fo(155,130,290,300,B[k]), id=i.replace("-","")+"t")
    cards+=f'''<section class="card" id="{i}"><div class="stage" style="background:#E9ECF4"><span class="tag">Crooked merch concept · DC Small Business</span>{svg}<span class="unoff">Unofficial parody concept · Not affiliated with Crooked Media</span></div>
<div class="lab"><div><h3>{names[k]}</h3><p>{specs[k]}</p></div><div class="mono">"{tag}"</div></div></section>'''
open("tiles.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{cards}</body></html>")
import json; json.dump({i:[names[k],specs[k]] for k,i,*_ in P},open("tiles.json","w"))
