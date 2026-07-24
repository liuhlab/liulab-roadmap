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

A clean build says nothing about how a page *looks*. For anything visual
(Mermaid, CSS figures, tooltips) serve `site/` on a port and check it in a
browser, light and dark, before calling it done. Commit and push only when
asked — not after every edit.

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

**Where a page starts** — A filled-in `.github/ISSUE_TEMPLATE/new-page.yml`
issue. Its fields are raw material, not an outline to transcribe: reorder, cut
what doesn't earn its place, research the gaps. Sparse fields mean drafting
more, not writing less. Always keep the issue's opinions and lab experience —
that is the part no search can supply.

**Draft banner** — Every agent-drafted page ships with a red draft box right
under the H1, in both languages, marking it AI-generated and unreviewed:
`!!! danger "Draft · not yet reviewed by a human"` /
`!!! danger "草稿 · 尚未经过人工审阅"`. Never remove it on your own; take it out
only when the user explicitly says that page can lose it.

**Audience & voice** — Write for entry-level students (incoming PhDs, senior
undergrads, master's) with no background in the topic. Talk to peers, not down
to pupils: share what worked ("多数时候我们…"), don't instruct ("你应该…",
"别跳过…"). Define every term on first use; lead with intuition, not mechanism.
No AI voice: no em dashes (中文破折号同理), no `**bold lead-in:**` bullets, no
rhetorical-question openers, no compulsive rule of three. Vary sentence length,
hold an opinion, and audit with the `avoid-ai-writing` skill before shipping.

**A page is a roadmap, not a textbook** — Mostly a catalog and map: point to the
best learning materials and show how concepts, learning stages, and resources
fit together. Blog-like and easy to follow. Keep a page readable in one sitting;
split rather than grow.

**Balance** — Optimize for the reader keeping the thread, not for completeness.
Link out instead of inlining depth. Web-search for the best existing writing and
add **Further reading**; propose candidates to the user rather than picking
silently.

**Figures** — Aim for 图文并茂, but cut any figure whose removal doesn't hurt
understanding. Prefer code-authored vectors (inline SVG, HTML/CSS, Mermaid) over
PNGs: editable, diff-able, theme-aware — use `currentColor` or CSS variables so
dark mode works. Write alt text, prefer language-neutral figures, attribute
anything taken from a paper.

**Cross-linking, glossary, citations** — Link internally at every opportunity;
dense linking is what turns pages into a map. Glossary = hover tooltips on first
use per page via `hooks/glossary.py` + `includes/glossary{,.zh}.md` (not `abbr`
— its `\b` matching fails on Chinese); a concept with its own page gets a link,
not an entry. Mermaid fences work. Citations (`mkdocs-bibtex`) not yet wired up.

## Gotchas

- Don't re-add `navigation.instant` — it breaks the language switcher.
- Material lazy-loads Mermaid from unpkg; we vendor it (`extra_javascript`,
  `defer`) so readers behind the GFW see diagrams. Don't drop it.
- Mermaid ignores `direction` inside a subgraph that has edges to another
  subgraph. Lay figures out as a spine plus fan-out instead.
- `mkdocs-static-i18n` is PyPI-only → `[pypi-dependencies]` in `pixi.toml`.
  Same for `git-revision-date-localized` (conda-forge froze at 1.2.9), which
  must also sit *after* `i18n` in `plugins:` or the build errors out.
- The page footer date comes from `git log` per file, so CI checkouts need
  `fetch-depth: 0`. A shallow clone dates every page alike and still exits 0.
- Empty dirs need a `.gitkeep`, or `custom_dir`-style config breaks in CI.
- `pixi.toml` version uses CalVer (`YYYY.M.D`).
