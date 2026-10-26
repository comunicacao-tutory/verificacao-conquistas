# Como o palco foi montado

- `ref.webp` — arte de referência original (quadro + pódio + fumaça).
- `corte.html` — recorta dela a faixa do pódio, sem o quadro, que vira
  `assets/palco.webp`. O quadro é elemento separado na página justamente
  para poder descer depois da verificação.
- `fumaca.svg` — gera `assets/fumaca.webp`, a textura de fumaça animada
  por cima. É `feTurbulence` com `stitchTiles="stitch"` (ladrilha sem
  emenda) e uma curva de alfa íngreme, que separa novelos densos de
  vazios em vez de produzir névoa uniforme.

Para regerar a textura:

    chrome --headless --default-background-color=00000000 \
      --window-size=820,305 --screenshot=f.png fumaca.svg
    cwebp -q 82 -alpha_q 100 -m 6 f.png -o ../assets/fumaca.webp

O custo do ruído é pago uma vez aqui. Na página a fumaça só anda com
`translate` e `scale`, que o compositor resolve sem repintar.
