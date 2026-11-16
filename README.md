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
│   ├── stylesheets/          # extra.css
│   ├── adr/                  # decision records (not published)
│   └── agents/               # rules for coding agents (not published)
├── hooks/glossary.py         # build hook: glossary hover tooltips
├── includes/                 # glossary terms, English and 中文
├── scripts/                  # the check runner and conformance check
├── styles/Lab/               # vale writing rules
├── .github/workflows/        # CI (the checks + build) and Pages deploy
├── mkdocs.yml                # site configuration
├── pyproject.toml            # dev toolchain (pixi) and tool settings
├── pixi.lock                 # exact versions of every tool
├── .markdownlint-cli2.yaml   # Markdown lint rules
└── .vale.ini                 # which writing rules apply to which files
```

## Local preview

The toolchain is managed with [pixi](https://pixi.sh) (`pyproject.toml` +
`pixi.lock`), on Apple-silicon Macs and Linux. Install pixi, then:

```bash
pixi install
pixi run docs         # live-reloading preview at http://127.0.0.1:8000
pixi run docs-build   # strict build into site/ (mirrors CI)
pixi run check        # every check: lint, types, writing rules, conformance
```

CI runs the same tasks from the same lock file. So when `pixi run check` and
`pixi run docs-build` pass locally, CI should pass too.

## Writing bilingual content

This project uses the **suffix** convention. For a page at route `/foo/`:

- `docs/foo.md` — English (the default locale)
- `docs/foo.zh.md` — 简体中文

Both files share the same URL; the language switcher toggles between them. If a
Chinese translation is missing, the English page is shown as a fallback.

Add new pages to the `nav:` section of [mkdocs.yml](mkdocs.yml). Chinese nav
labels are set via `nav_translations` in the same file.

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`. It builds the site and
force-pushes it to the `gh-pages` branch, which GitHub Pages serves at
<https://liuhlab.github.io/liulab-roadmap/>. In the repo's Pages settings, the
source is **Deploy from a branch**, branch `gh-pages`, folder `/ (root)`.

## Contributing

1. Create a branch and add or edit Markdown under `docs/`.
2. Run `pixi run check` and `pixi run docs-build` locally.
3. Open a pull request as a draft, then mark it ready for review. CI runs the
   checks and a strict build once it is ready.
