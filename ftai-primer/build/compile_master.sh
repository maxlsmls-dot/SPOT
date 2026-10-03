#!/usr/bin/env bash
# Compile the master PDF: cover + Spine + Parts I–XII. Run from ftai-primer/build.
set -e
cd "$(dirname "$0")"
P=../parts
FILES="master-front.md $P/spine.md $P/part01-cfm56-machine.md $P/part02-money-mechanics.md $P/part03-context.md $P/part04-shop-visit-market.md $P/part05-usm-teardown.md $P/part06-pma-der.md $P/part07-aerospace-products.md $P/part08-leasing-sci.md $P/part09-ftai-power.md $P/part10-company.md $P/part11-markets-peers.md $P/part12-reference.md"
for f in $FILES; do [ -f "$f" ] || { echo "missing $f"; exit 1; }; done
python3 render.py $FILES --out "../FTAI Deep Primer.pdf" --master --toc-depth 2
python3 validate.py "../FTAI Deep Primer.pdf"
