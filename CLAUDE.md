# CLAUDE.md

Guidance for Claude Code in this repo. **Keep this file short** — add rules, not
prose. When editing it, prefer rewriting a line over appending a new paragraph.

## What this is

Bilingual (English + 简体中文) documentation site for the Liu Lab: roadmaps,
tutorials, and learning materials. Content only — no application code, no
installable packages. MkDocs + Material → GitHub Pages at
<https://liuhlab.github.io/liulab-roadmap/> (repo `liuhlab/liulab-roadmap`).

## Toolchain

pixi is the single source of truth (`pixi.toml` + `pixi.lock`) — no
`requirements.txt`, no venv.

```bash
pixi run serve   # live preview
pixi run build   # strict build; CI runs this — do it before calling a change done
pixi run lint    # markdownlint
```

## Structure & conventions

- Content in `docs/`; images in `docs/assets/`.
- **Bilingual suffix convention:** `foo.md` = English (default),
  `foo.zh.md` = 中文. Same URL; a missing translation falls back to English.
- **Every page exists in both languages.** Write/update the counterpart in the
  same change — never leave one language stale.
- **Numbered paths:** dirs `1-basics` … `9-journal-club`, leaf pages
  `1.1-…`, `1.2-…`. Numbers never appear in the nav (labels come from each
  page's H1), only in the file tree and URLs.
- Add new pages to `nav:` in `mkdocs.yml`; translate only section labels, via
  `nav_translations`.
- Collection sections keep `index.md` as a clickable section landing page
  (`navigation.indexes`). An overview gains L3 subpages by becoming a folder
  with an `index.md`.
- Prose is not hard-wrapped (`MD013` off) — Chinese has no spaces to wrap on.
- **Working language:** the user often drafts in Chinese; commit messages, code,
  config comments, and narration stay **English**.

## Writing guide

Read this before authoring any page.

**Audience & voice** — Write for entry-level students (incoming PhDs, senior
undergrads, master's) with no background in the topic. Lay, friendly, human.
Define every term and acronym on first use. Lead with intuition and why it
matters, not mechanism.

**A page is a roadmap, not a textbook** — Mostly a catalog and map: point to the
best learning materials and show how concepts, learning stages, and resources
fit together. Blog-like and easy to follow. Keep a page readable in one sitting;
split rather than grow.

**Balance** — Optimize for the reader keeping the thread, not for completeness.
Link out instead of inlining depth. Web-search for the best existing writing and
add **Further reading**; propose candidates to the user rather than picking
silently.

**Figures** — Aim for 图文并茂: a good diagram is often the fastest path to
intuition. But no decorative or redundant images — if removing a figure doesn't
hurt understanding, cut it. Prefer code-authored vectors (inline SVG, HTML/CSS,
Mermaid) over PNGs: editable, diff-able, and theme-aware — use `currentColor` or
CSS variables so dark mode works. Always write alt text, prefer language-neutral
figures, and attribute anything taken from a paper.

**Cross-linking, glossary, citations** — Link internally at every opportunity;
dense linking is what turns pages into a map. Glossary = hover tooltips, not
click-jumps (`abbr` + `pymdownx.snippets` over `includes/glossary.md`).
Citations = BibTeX + `mkdocs-bibtex`, `[@key]` inline, resolving to DOI/PubMed.
*Glossary and citation tooling are not yet enabled — wire up on first need.*

## Gotchas

- Don't re-add `navigation.instant` — it breaks the language switcher.
- `mkdocs-static-i18n` is PyPI-only → `[pypi-dependencies]` in `pixi.toml`.
- Empty dirs need a `.gitkeep`, or `custom_dir`-style config breaks in CI.
- `pixi.toml` version uses CalVer (`YYYY.M.D`).
