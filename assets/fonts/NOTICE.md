# Fontes

**Caveat Brush** — fonte de marca do Travel+ (nomes de viagem, wordmark e
títulos manuscritos). Desenhada por Pablo Impallari, © Google Inc., distribuída
sob a **SIL Open Font License 1.1** — texto completo em [OFL.txt](OFL.txt).

Servida como subconjunto (apenas os caracteres usados: Latim + acentos PT/ES +
pontuação), em dois formatos:

- `caveat_brush.woff2` — principal (~64 KB)
- `caveat_brush.woff` — fallback (~83 KB)

Gerados a partir do `caveat_brush.ttf` original (do Google Fonts, ~288 KB) com
`fontTools`:

```sh
py -m pip install fonttools brotli
U="U+0020-00FF,U+2010-2014,U+2018-201D,U+2026"
py -m fontTools.subset caveat_brush.ttf --unicodes=$U --flavor=woff2 --output-file=caveat_brush.woff2
py -m fontTools.subset caveat_brush.ttf --unicodes=$U --flavor=woff  --output-file=caveat_brush.woff
```

⚠️ O subconjunto cobre PT/EN/ES. Se entrar um idioma com outros caracteres
(ex.: cirílico, grego), regenerar com o range ampliado a partir do `.ttf`
original — que **não** é versionado aqui; baixe de
https://fonts.google.com/specimen/Caveat+Brush quando precisar.
