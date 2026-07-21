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

## Conventions

- **No third-party hosts.** No CDN scripts, no Google Fonts links, no analytics, no embeds. Everything the page needs is served from this origin — that's why the brand font is committed here instead of linked. Local `assets/` files are fine; an external `<link>` or `<script>` is not.
- **Content is bilingual**: Portuguese is the primary text, English follows in a `.en` span with `lang="en"`. Preserve this in new sections.
- The pages carry real legal/corporate identifiers (company legal name, CNPJ, contact address). Do not invent, alter, or "correct" these values — ask before touching them.
- `privacy.html` is a legal document. Restyle its markup freely; do not reword its text without the owner asking.

## Images

`assets/img/*` are generated from the app repo's own resources (`app/src/main/res/drawable-nodpi/wallpaper_*.png`, `mipmap-xxxhdpi/ic_launcher.png`), resized and re-encoded — the originals are 941×1672 PNGs weighing ~2.5 MB each. The script that produced them is not committed; regenerate with Pillow (`py -c` / a throwaway script) rather than committing multi-MB PNGs.

Write alt text by **looking at the image**, not by trusting the filename — `beach.png` is a tropical street scene with a taxi, `iceland.png` has an aurora and Portuguese trail signs.

## Known gaps

Tracked in [ROADMAP.md](ROADMAP.md) — read it before starting work, and add findings there rather than here so there's one list. The one worth knowing up front: **`privacy.html` claims the app requests location and gallery permissions, which it does not**, and that text has to be corrected before the privacy URL goes into Play Console.
