# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The public website for TravelPlus Labs — hand-written static pages, no build system, no package manager, no dependencies, no test suite. Editing the HTML *is* the whole workflow.

- [index.html](index.html) — landing page presenting the **Travel+** Android app.
- [privacy.html](privacy.html) — the app's privacy policy. This is the URL to give Google Play Console.
- [assets/](assets) — `css/site.css` (shared by both pages), `img/` (generated from the app's own resources), `fonts/caveat_brush.ttf` (brand font).

The product it markets lives in a **separate repo** at `C:\dev\app\travel` (Kotlin/Compose, offline-first). Its `README.md`, `ROADMAP.md` and `docs/PROJETO.md` are the source of truth for any product claim made on this site — read them before writing marketing copy, and don't invent features.

## Deployment

Deployed via GitHub Pages from `main` at https://github.com/TravelPlusLabs/travelplus-site, served at the custom domain in [CNAME](CNAME) (`usetravelplus.com`). Consequences to keep in mind:

- **Pushing to `main` publishes to the live public site.** There is no staging environment; treat any push as a production deploy.
- Don't delete or rename `CNAME` — GitHub Pages reads it to keep the custom domain binding.
- Preview changes by opening `index.html` directly in a browser; no server is needed.
- [`_config.yml`](_config.yml) exists only to keep internal docs out of the built site. Anything else added at the repo root **is served publicly** at `usetravelplus.com/<file>` — this is a public repo hosting a public site, so a stray file is both readable in git history and downloadable from the domain.

## Secret protection

A [`.githooks/pre-commit`](.githooks/pre-commit) hook blocks commits containing credential-shaped content. **`core.hooksPath` is per-clone local config, so a fresh clone starts unprotected** — enable it once with:

```sh
git config core.hooksPath .githooks
```

The hook catches common key formats and credential filenames (including `git add -f`), but it is a speed bump, not a guarantee: unusual formats slip through and `--no-verify` bypasses it. A secret that reaches GitHub is not fixed by a follow-up commit — rotate it.

## Working Agreement — Parallel Sessions

The owner runs several Claude Code sessions at once (product decisions, the app
repo, this repo). **They share no context — these files are the only shared
state.** Any decision reached in conversation must be written down in the same
turn: the short enforceable rule here, the reasoning in [ROADMAP.md](ROADMAP.md),
dated. Then tell the owner which sessions need to re-read, since a running
session will not pick up the edit on its own. Full protocol in the workspace
`CLAUDE.md` at `C:\dev\app\CLAUDE.md`.

Product decisions come *from* that session into these files — if work here starts
inventing a price, a plan name, or a policy, stop and reconcile first.

## Monetization (decided 2026-07-30 — see [ROADMAP.md](ROADMAP.md))

- **The site never takes payment.** All billing happens inside the app via Google
  Play Billing. Selling here and unlocking in the app is an out-of-app purchase —
  grounds for removal from the Play Store. Every CTA points at the Play Store
  listing, never at a checkout.
- **No AdSense, no ad slots of any kind.** The page has one job: drive installs.
  Same decision was made for the app.
- A **pricing section is allowed and useful** — mirror the app's real SKUs:
  **free = 1 trip · R$ 24,90 = 5 trips · R$ 44,90 = unlimited on device**, all
  **one-time purchases (no monthly / no subscription)**. What is sold is *how many
  trips you can keep*, not features — everyone has the full app. The purchase
  happens inside the app; the button here points at the Play Store, never a
  checkout. ⚠️ Never frame it as a subscription, never write "all features", never
  imply the future cloud tier is included (v3 cloud is a separate R$ 14,90/mo
  subscription).
- **SEO destination pages** ("roteiro de 4 dias em Campos do Jordão") are the main
  growth play — they capture planning intent and funnel to the install.
- **This repo will also host the app's trip packages** *(decided 2026-07-30)* —
  static JSON plus cover images, fetched by the app so a user can install a
  ready-made itinerary in one tap. They are **free marketing assets, never sold**;
  the revenue comes from the trip slot inside the app. Adding them here means
  paths under this repo become a de facto API for the app: **do not rename or
  move those files once shipped clients depend on them.** The same
  copy later feeds the v2.5 roteiro AI and the v3 catalogue: write once, use thrice.
- **A public support page is required before Play submission** — the Play Console
  needs a support contact, and the purchase-management link tends to land on the
  site. Decide where it lives before submitting.
- 🚨 **The "offline / nothing leaves the device" story has an expiry.** v2.5 adds
  the app's first own endpoint (roteiro-AI proxy) and v3 a full backend, so
  `privacy.html` and `SECURITY.md` — written for today's no-network app — must be
  revisited before v2.5 ships.

## Conventions

- **No third-party hosts.** No CDN scripts, no Google Fonts links, no analytics, no embeds. Everything the page needs is served from this origin — that's why the brand font is committed here instead of linked. Local `assets/` files are fine; an external `<link>` or `<script>` is not.
- **Languages**: `index.html` has a **PT/EN/ES language switcher** — Portuguese is the default text written in the HTML, and English/Spanish come from the `I18N` dictionary in the inline `<script>`. Translatable elements carry `data-i18n="key"` (or `data-i18n-ph` for a placeholder); add both the attribute and the `en`/`es` entries when adding copy. A missing key falls back to the PT text. The EN/ES strings were drafted by the assistant and still need the owner's tone review. `privacy.html` is the exception — it stays inline-bilingual (PT + `.en` span), not switched.
- The pages carry real legal/corporate identifiers (company legal name, CNPJ, contact address). Do not invent, alter, or "correct" these values — ask before touching them.
- `privacy.html` is a legal document. Restyle its markup freely; do not reword its text without the owner asking.

## Images

`assets/img/*` are generated from the app repo's own resources (`app/src/main/res/drawable-nodpi/wallpaper_*.png`, `mipmap-xxxhdpi/ic_launcher.png`), resized and re-encoded — the originals are 941×1672 PNGs weighing ~2.5 MB each. The script that produced them is not committed; regenerate with Pillow (`py -c` / a throwaway script) rather than committing multi-MB PNGs.

Write alt text by **looking at the image**, not by trusting the filename — `beach.png` is a tropical street scene with a taxi, `iceland.png` has an aurora and Portuguese trail signs.

## Known gaps

Tracked in [ROADMAP.md](ROADMAP.md) — read it before starting work, and add findings there rather than here so there's one list. Recently closed: `privacy.html` no longer claims phantom location/gallery permissions (corrected and live), and the landing pricing was realigned to the decided one-time model. The site itself is **live** at `usetravelplus.com` (landing + privacy), on a branch-protected `main` (every change goes through a PR).
