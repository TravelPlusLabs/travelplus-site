# Site Travel+ — pendências

O que falta no site (`usetravelplus.com`). As pendências do **app** ficam no
`ROADMAP.md` do outro repo (`C:\dev\app\travel`); aqui só o que é do site.

> ⚠️ `main` é produção. Um push publica direto no GitHub Pages, sem staging.

---

## 🚨 Antes de submeter o app à Play Store

- **Publicar as páginas.** A landing (`index.html`) e a política
  (`privacy.html`) estão escritas mas **nunca foram ao ar** — falta o push para
  `main`. Até lá, `https://usetravelplus.com/privacy.html` responde 404, e é
  essa a URL que o Play Console vai receber.

- **Corrigir as permissões descritas na política.** O texto afirma que o app
  pede acesso à localização e à galeria. Não pede nenhum dos dois: as fotos
  usam o photo picker do sistema e o "Como chegar" abre o app de mapas por
  intent — hoje o app nem tem permissão de `INTERNET`. Precisa bater com o
  formulário de Data Safety, senão a Play reprova. Detalhes no ROADMAP do app.
  **Texto legal — não reescrever sem o dono pedir.**

- **Data de "última atualização" na política.** Não existe nenhuma; o texto
  original só trazia "© 2024". Revisores da Play procuram esse carimbo.

---

## Antes de divulgar a landing

- **Screenshots reais do app.** A galeria hoje mostra as artes de capa
  (`assets/img/*.jpg`), porque não existe captura nenhuma ainda. As mesmas
  capturas são bloqueador da Play Store — gerar uma vez, usar nos dois lugares.
  A seção já está dimensionada para receber imagens 9:16.

- **`OFL.txt` da Caveat Brush.** A SIL Open Font License exige que o texto da
  licença acompanhe o arquivo redistribuído, e `assets/fonts/` só tem o `.ttf`.
  Baixar do pacote original — ver [NOTICE.md](assets/fonts/NOTICE.md).

- **Conferir o preview social.** O `og:image` aponta para
  `https://usetravelplus.com/assets/img/og.jpg`, que é URL absoluta e só resolve
  depois da publicação. Validar num depurador de link (WhatsApp, Telegram,
  LinkedIn) assim que estiver no ar.

---

## Melhorias

- **Subsetar a fonte de marca.** `caveat_brush.ttf` são 288 KB dos 593 KB que a
  home carrega — quase metade do peso, para o wordmark e dois títulos. Subsetar
  para os caracteres usados e converter para woff2 derruba para ~20 KB. Precisa
  de `fonttools` + `brotli` (`py -m pip install fonttools brotli`), que não
  estão instalados.

- **Botão real da Play Store.** Hoje o CTA é "Em breve" apontando para o e-mail,
  porque o app não está publicado. Quando a ficha existir, trocar pelo badge
  oficial — o badge do Google **não pode ser redesenhado**, tem que ser o
  asset oficial, o que quebra a regra de "nada de host externo" só se for
  linkado; baixar e servir localmente.

- **Tema escuro do site.** Hoje é tema único (fundo claro, hero e rodapé
  escuros). O app tem tema escuro pendente na v1; se ele sair, vale espelhar
  com `prefers-color-scheme`.

- **Escopo do [SECURITY.md](SECURITY.md).** Cobre só o site. Se o app passar a
  ter backend (v3), a política precisa ser reescrita para incluir os dois.

---

*Documento vivo — mesmo espírito do ROADMAP do app.*
