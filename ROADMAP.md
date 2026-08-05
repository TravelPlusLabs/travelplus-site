# Site Travel+ — pendências

O que falta no site (`usetravelplus.com`). As pendências do **app** ficam no
`ROADMAP.md` do outro repo (`C:\dev\app\travel`); aqui só o que é do site.

> ⚠️ `main` é produção. Um push publica direto no GitHub Pages, sem staging.

---

## ✅ Antes de submeter à Play Store — parte do site, concluída

Os itens do **site** que travavam a submissão estão resolvidos e no ar
*(fechado em 30/07/2026)*:

- **Páginas publicadas.** Landing + política estão no ar em `usetravelplus.com`
  (GitHub Pages a cada merge em `main`). A URL para o Play Console é
  `https://usetravelplus.com/privacy.html`.
- **Permissões corrigidas na política.** O texto **não cita mais localização
  nem galeria**: descreve o photo picker do sistema (sem permissão de galeria),
  o mapa por intent (sem localização) e a ausência de permissão de internet —
  batendo com o Data Safety. ⚠️ Se a previsão do tempo da v2 / a IA de roteiro
  da v2.5 entrarem, o texto muda (aí há rede) — há um comentário no topo do
  `privacy.html` avisando.
- **Data de "última atualização"** presente na política.

> O ROADMAP do **app** ainda pode listar "corrigir a política" como pendente —
> está desatualizado nesse ponto; o site já resolveu. O que resta para a
> submissão é material do app (capturas, descrição, banner, Data Safety).

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

## Monetização e crescimento *(definido em 30/07/2026)*

O modelo de cobrança do app está no [ROADMAP do app](../travel/ROADMAP.md). O que
cabe ao site:

- **O site não cobra nada.** Todo o pagamento acontece dentro do app, via Google
  Play Billing. Vender no site e destravar no app é *out-of-app purchase* e
  motivo de remoção da loja — e obrigaria a construir conta, autenticação,
  backend e sincronização de direito, que o app hoje não tem. O CTA leva à ficha
  da Play Store, nunca a um checkout.

- 🚫 **Nada de AdSense.** A página tem uma função só: gerar instalação. Cada
  anúncio é uma porta de saída, e com o tráfego inicial o site trocaria
  instalações por alguns reais por mês. Mesma decisão tomada para o app.

- **Seção de preços na landing.** Faz sentido existir (qualifica o tráfego e
  ajuda na busca), desde que o botão aponte para a Play Store. Espelhar os
  valores do app: grátis com 1 viagem · R$ 24,90 por 5 · R$ 44,90 ilimitado.
  ⚠️ Não escrever "todos os recursos" nem sugerir que a nuvem futura está
  incluída — a v3 é assinatura separada.

- **Conteúdo de busca — o principal movimento de crescimento.** Páginas do tipo
  "roteiro de 4 dias em Campos do Jordão" ou "o que fazer em Gramado no inverno"
  capturam gente exatamente no momento de planejar, que é quem instala e quem
  compra. Cada página termina no mesmo lugar: baixar o roteiro pronto no app.
  Bônus: esse mesmo material alimenta depois a IA de roteiro (v2.5) e o catálogo
  de roteiros (v3) — escreve uma vez, usa três. Só faz sentido investir em
  tráfego pago depois que essas páginas tiverem número de conversão.

- **Página de suporte.** O Play Console exige contato de suporte público, e o
  link de gerenciamento de compra do usuário costuma cair no site. Definir onde
  mora antes da submissão.

- **Hospedar os pacotes de viagem** *(decidido em 30/07/2026)* — roteiros prontos
  em JSON estático + capas, servidos daqui para o app baixar e instalar com um
  toque. **São gratuitos e não são vendidos**: existem para puxar instalação, e o
  dinheiro vem da vaga de viagem dentro do app. O conteúdo sai do prompt em
  `images/json.txt` do outro repo, que já gera no schema exato do app.

  ⚠️ **Isso transforma parte deste repo numa API.** Assim que uma versão do app
  publicada apontar para esses caminhos, renomear ou mover um arquivo quebra
  quem já instalou — e não dá para reverter com um push, porque a versão antiga
  do app continua nos aparelhos. Definir a estrutura de pastas e um manifesto
  versionado **antes** do primeiro app em produção consumir.

- **Instagram** — canal principal para os pacotes: roteiro pronto é formato
  nativo de carrossel e Reels, e cada post termina no mesmo lugar que as páginas
  de destino, que é a instalação. Ainda sem perfil criado.

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

- **Escopo do [SECURITY.md](SECURITY.md).** Cobre só o site. O app ganha o
  primeiro endpoint próprio já na **v2.5** (proxy da IA de roteiro), e backend
  completo na v3 — a política precisa ser reescrita para incluir os dois antes
  disso.

---

*Documento vivo — mesmo espírito do ROADMAP do app.*
