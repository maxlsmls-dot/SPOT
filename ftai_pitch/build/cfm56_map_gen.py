W,H=635,250
bx0,by0,bw,bh=5,26,625,180
def X(ix): return bx0+(ix-235)/1588*bw
def Y(iy): return by0+(iy-147)/940*bh
sty={'OEM':('#FBE5D6','#A0522D'),'AIR':('#ECEBFB','#5B4FC4'),'IND':('#DDF1E8','#2E8B57'),'OVF':('#EFEFEC','#7F7F7F')}
def marker(t,x,y):
    f,l=sty[t]
    if t=='OEM': return f'<rect x="{x-6}" y="{y-6}" width="12" height="12" rx="2" fill="{f}" stroke="{l}" stroke-width="0.9"/>'
    if t=='IND': return f'<ellipse cx="{x}" cy="{y}" rx="9" ry="6" fill="{f}" stroke="{l}" stroke-width="0.9"/>'
    return f'<circle cx="{x}" cy="{y}" r="6" fill="{f}" stroke="{l}" stroke-width="0.9"/>'
pts=[("GE / CFM","OEM",411,264),("Safran","OEM",600,365),("Lufthansa","AIR",499,470),("AFI KLM","AIR",1088,322),("Delta","AIR",941,441),
("Iberia (planned)","AIR",941,661),("Turkish (exploring)","AIR",882,852),("Korean Air","AIR",882,999),("MTU","IND",1367,279),("StandardAero","IND",1529,381),
("ST Engineering","IND",1441,499),("SR Technics","IND",1500,631),("FTAI","OVF",1587,940)]
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W*3}" height="{H*3}" font-family="Liberation Serif" fill="#262626" style="display:block">',f'<rect width="{W}" height="{H}" fill="#fff"/>']
for t,lab,x in [("OEM","OEM network",60),("AIR","Airline-owned shop",175),("IND","Independent",320),("OVF","Overflow receiver",435)]:
    o.append(marker(t,x,13)); o.append(f'<text x="{x+13}" y="17" font-size="12">{lab}</text>')
o.append(f'<rect x="{bx0}" y="{by0}" width="{bw}" height="{bh}" fill="none" stroke="#BFBFBF" stroke-width="0.8"/>')
for k in (1,2):
    x=bx0+k*bw/3; o.append(f'<line x1="{x}" y1="{by0}" x2="{x}" y2="{by0+bh}" stroke="#BFBFBF" stroke-width="0.8" stroke-dasharray="3,3"/>')
o.append(f'<text x="{bx0+6}" y="{by0+13}" font-size="10.5" font-style="italic" fill="#7F7F7F">More LEAP</text>')
o.append(f'<text x="{bx0+6}" y="{by0+bh-6}" font-size="10.5" font-style="italic" fill="#7F7F7F">Less LEAP</text>')
for n,t,ix,iy in pts:
    x,y=X(ix),Y(iy); o.append(marker(t,x,y))
    dx=13 if t=='IND' else 10
    b=' font-weight="bold"' if t=="OVF" else ""
    o.append(f'<text x="{x+dx}" y="{y+4.2}" font-size="12.5"{b}>{n}</text>')
for k,lab in enumerate(["Pulling back on CFM56","Holding CFM56","Adding CFM56"]):
    o.append(f'<text x="{bx0+(k+0.5)*bw/3}" y="{by0+bh+15}" font-size="12.5" font-weight="bold" fill="#404040" text-anchor="middle">{lab}</text>')
ay=by0+bh+33
o.append(f'<line x1="70" y1="{ay}" x2="300" y2="{ay}" stroke="#E8702A" stroke-width="1.6"/><path d="M293,{ay-4} L300,{ay} L293,{ay+4}" fill="none" stroke="#E8702A" stroke-width="1.6"/>')
o.append(f'<text x="312" y="{ay+4.3}" font-size="12.5" font-weight="bold" fill="#E8702A">CFM56 work flows from OEMs to independents</text>')
o.append('</svg>')
open('map.html','w').write('<html><body style="margin:0">'+'\n'.join(o)+'</body></html>')
