# Liu Lab Roadmap

Curated roadmaps, tutorials, and learning materials for the Liu Lab, published
as a documentation website via [MkDocs](https://www.mkdocs.org/) +
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and deployed
to GitHub Pages.

The site is **bilingual** (English + 简体中文) with an in-page language switcher,
powered by [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/).

## Repository layout

```text
.
├── docs/                     # all site content (Markdown + assets)
│   ├── index.md              # English page
│   ├── index.zh.md           # 简体中文 page (same route, .zh suffix)
│   ├── assets/               # images and other media
│   └── stylesheets/          # extra.css
├── overrides/                # Material theme overrides (optional)
├── .github/workflows/        # CI (lint + build) and Pages deploy
├── mkdocs.yml                # site configuration
├── pixi.toml                 # dev toolchain (pixi)
├── .markdownlint.yaml        # Markdown lint rules
└── .gitignore
```

## Local preview

The toolchain is managed with [pixi](https://pixi.sh) (`pixi.toml` +
`pixi.lock`). Install pixi, then:

```bash
pixi install
pixi run serve      # live-reloading preview at http://127.0.0.1:8000
pixi run build      # strict build into site/ (mirrors CI)
pixi run lint       # markdownlint over docs/
```

CI uses the same `pixi.toml`, so a clean `pixi run build` locally means CI
should pass too.

## Writing bilingual content

This project uses the **suffix** convention. For a page at route `/foo/`:

- `docs/foo.md` — English (the default locale)
- `docs/foo.zh.md` — 简体中文

Both files share the same URL; the language switcher toggles between them. If a
Chinese translation is missing, the English page is shown as a fallback.

Add new pages to the `nav:` section of [mkdocs.yml](mkdocs.yml). Chinese nav
labels are set via `nav_translations` in the same file.

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the site
and publishes it to GitHub Pages at <https://liuhlab.github.io/liulab-roadmap/>.
Pages is configured with **Source: GitHub Actions** (a one-time repo setting).

## Contributing

1. Create a branch and add or edit Markdown under `docs/`.
2. Run `pixi run lint` and `pixi run build` locally.
3. Open a pull request — CI runs markdownlint and a strict build.
