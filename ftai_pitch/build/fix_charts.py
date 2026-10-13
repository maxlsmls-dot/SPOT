"""Reorder pptxgenjs chart XML to the OOXML schema so PowerPoint opens it cleanly.
Usage: python3 fix_charts.py deck.pptx  (rewrites in place)"""
import sys, zipfile, shutil, os, re
from lxml import etree

NS = "http://schemas.openxmlformats.org/drawingml/2006/chart"
q = lambda t: "{%s}%s" % (NS, t)

ORDER = {
    "barSer": "idx order tx spPr invertIfNegative pictureOptions dPt dLbls trendline errBars cat val shape extLst",
    "lineSer": "idx order tx spPr marker dPt dLbls trendline errBars cat val smooth extLst",
    "pieSer": "idx order tx spPr explosion dPt dLbls cat val extLst",
    "barChart": "barDir grouping varyColors ser dLbls gapWidth overlap serLines axId extLst",
    "lineChart": "grouping varyColors ser dLbls dropLines hiLowLines upDownBars marker smooth axId extLst",
    "doughnutChart": "varyColors ser dLbls firstSliceAng holeSize extLst",
    "pieChart": "varyColors ser dLbls firstSliceAng extLst",
    "dLbls": "dLbl delete numFmt spPr txPr dLblPos showLegendKey showVal showCatName showSerName showPercent showBubbleSize separator showLeaderLines leaderLines extLst",
}


def reorder(el, kind):
    order = ORDER[kind].split()
    kids = list(el)
    keep = [k for k in kids if isinstance(k.tag, str) and etree.QName(k).localname in order]
    for k in kids:
        el.remove(k)
    keep.sort(key=lambda k: order.index(etree.QName(k).localname))
    if kind in ("barChart", "lineChart"):  # 2-D charts take exactly two axis ids
        ax = [k for k in keep if etree.QName(k).localname == "axId"]
        for extra in ax[2:]:
            keep.remove(extra)
    for k in keep:
        el.append(k)


def fix(xml):
    root = etree.fromstring(xml)
    for chart, ser in (("barChart", "barSer"), ("lineChart", "lineSer"), ("pieChart", "pieSer"), ("doughnutChart", "pieSer")):
        for c in root.iter(q(chart)):
            if chart == "lineChart" and c.find(q("grouping")) is None:
                g = etree.SubElement(c, q("grouping")); g.set("val", "standard")
            for s in c.findall(q("ser")):
                reorder(s, ser)
            reorder(c, chart)
    for d in root.iter(q("dLbls")):
        reorder(d, "dLbls")
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def main(path):
    tmp = path + ".tmp"
    with zipfile.ZipFile(path) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            data = zi.read(item.filename)
            if re.match(r"ppt/charts/chart\d+\.xml$", item.filename):
                data = fix(data)
            zo.writestr(item, data)
    shutil.move(tmp, path)


if __name__ == "__main__":
    main(sys.argv[1])
