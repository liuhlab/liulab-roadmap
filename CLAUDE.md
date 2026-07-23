# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

A documentation website for the Liu Lab: curated **roadmaps**, **tutorials**,
and **learning materials**. Content only — no application code, no installable
packages. Built with MkDocs + Material for MkDocs and deployed to GitHub Pages.

The site is **bilingual** (English + 简体中文) with an in-page language switcher.

## Toolchain

Managed with [pixi](https://pixi.sh) (`pixi.toml` + `pixi.lock`). Do not add a
`requirements.txt` or a separate venv workflow — pixi is the single source of
truth.

```bash
pixi run serve   # live preview at http://127.0.0.1:8000
pixi run build   # strict build into site/ (what CI runs)
pixi run lint    # markdownlint over docs/
```

Always run `pixi run build` (it uses `--strict`) before considering a change
done — strict mode is what CI enforces.

## Content conventions

- All content lives under `docs/`. Assets go in `docs/assets/`.
- Bilingual pages use the **suffix** convention (`mkdocs-static-i18n`):
  - `docs/foo.md` → English (default locale)
  - `docs/foo.zh.md` → 简体中文
  - Both share one URL; missing translations fall back to English.
- New pages must be added to `nav:` in `mkdocs.yml`. Chinese nav labels are set
  under the `zh` locale's `nav_translations` in the same file.
- Prose is not hard-wrapped to a column limit (`MD013` is disabled) — Chinese
  text has no spaces to wrap on.

## Gotchas

- The `navigation.instant` theme feature is intentionally omitted — it breaks
  the language switcher. Don't re-add it.
- `mkdocs-static-i18n` is PyPI-only (not on conda-forge), so it lives under
  `[pypi-dependencies]` in `pixi.toml`.
- The repo lives at `liuhlab/liulab-roadmap` (public); the site publishes to
  <https://liuhlab.github.io/liulab-roadmap/>. `site_url`/`repo_url`/`repo_name`
  in `mkdocs.yml` reflect this.

## Versioning

`pixi.toml` uses CalVer (`YYYY.M.D`).
