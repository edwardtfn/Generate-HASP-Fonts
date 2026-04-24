from fontTools.ttLib import TTFont

f = TTFont("MaterialDesignIconsDesktop-7.4.47.ttf")
glyf = f["glyf"]
hmtx = f["hmtx"]
cmap = f["cmap"].getBestCmap()

for cp in [0xF0425, 0xF02DC, 0xF0079]:  # power, home, battery
    gname = cmap[cp]
    g = glyf[gname]
    adv, lsb = hmtx[gname]
    print(f"U+{cp:05X} {gname}: xMin={g.xMin} xMax={g.xMax} advance={adv} lsb={lsb}")
