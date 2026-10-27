#!/bin/bash
# Gera assets/fumaca.webp a partir de fumaca.svg.
#
# O pulo do gato esta na costura: feTurbulence com stitchTiles ladrilha
# sem emenda, mas o desfoque final quebra isso, porque nas bordas ele
# nao tem vizinho pra amostrar. Entao o desfoque e aplicado sobre tres
# copias lado a lado e recortamos a do meio, que ja nasce casando.
set -e
cd "$(dirname "$0")"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PERFIL="${TMPDIR:-/tmp}/chrome-fumaca"
shot(){ "$CH" --headless --disable-gpu --hide-scrollbars --user-data-dir="$PERFIL" \
         --default-background-color=00000000 --window-size="$2" --screenshot="$3" "file://$PWD/$1" 2>/dev/null; }

shot fumaca.svg   820,305 tile-cru.png
shot costura.html 820,305 tile-costurado.png
cwebp -q 82 -alpha_q 100 -m 6 tile-costurado.png -o ../assets/fumaca.webp
rm -f tile-cru.png tile-costurado.png
echo "assets/fumaca.webp: $(stat -f%z ../assets/fumaca.webp) bytes"
