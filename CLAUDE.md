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

### Working language

- **The user often writes/drafts in Chinese.** That does not change the working
  language of the *project machinery*: commit messages, code, config comments,
  CI, PR descriptions, and any logging/narration are always in **English**.
- **Every doc page must exist in both languages.** When a page is added or
  edited in one language, create/update its counterpart so `foo.md` (English)
  and `foo.zh.md` (简体中文) stay in sync. Don't leave one language stale — if the
  user drafts a page in Chinese, write the English `.md`; if in English, write
  the `.zh.md`.

## Writing guide

This is the most important section for anyone (human or Claude) authoring pages.
Read it before writing content.

### Audience & voice

- **Write for entry-level students** — incoming PhDs, senior undergrads,
  master's students who may be brand new to the topic. Assume curiosity and
  intelligence, but **no prior background** in the specific subject.
- **Use lay language: friendly, plain, human.** Write the way you'd explain
  something to a smart friend over coffee, not the way a paper's methods section
  reads.
- **No unexplained jargon or abbreviations.** The first time a domain term or
  acronym appears, define it in plain words (and, where it helps, register it in
  the glossary — see below). If a sentence only makes sense to someone who
  already knows the field, rewrite it.
- **Don't front-load technical detail.** Give the intuition and the "why it
  matters" before any mechanism. Skip deep technical detail unless the page's
  whole purpose is that detail — and even then, build up to it.

### What a page is: a roadmap, not a textbook

- This site is mostly a **catalog and map**, not the primary content. A typical
  page points readers to the best learning materials and shows how the pieces
  fit: how high-level concepts relate, what the learning stages are, and which
  major resources cover each.
- **Write pages in a blog-like style** — easy to read, easy to follow, a clear
  narrative thread. Not a dense reference dump.
- **Keep pages short.** A page should be comfortable to read in one sitting
  without losing the thread. If it's getting long or dense, split it into
  linked pages rather than growing one.

### Balance information against what a reader can follow

- There is a real tension between **how much you include** and **how much a
  reader can actually follow and remember**. Optimize for the reader keeping the
  thread, not for completeness.
- When a topic runs deep, **link out instead of inlining it.** Prefer a good
  external explainer over reproducing it here.
- **Suggest high-quality outside materials.** It's expected to web-search for the
  best existing writing on a topic and add a **Further reading** section with
  curated links. When drafting, surface candidate resources to the user for
  approval rather than silently picking.

### Figures & visuals

- **Aim for 图文并茂 — text and images working together.** Sometimes one figure
  genuinely is worth a thousand words: a concept diagram, a workflow, a
  before/after comparison, the anatomy of a method. At those moments a figure is
  the fastest path to intuition, and it's exactly what this site should use.
- **But don't overuse or abuse images.** Decorative pictures, stock photos, or a
  figure that just restates the sentence next to it add visual noise and loading
  time without helping the reader.
- **The test:** would removing this figure make the page harder to understand?
  If yes, keep it. If not, cut it.
- Practical points:
  - Store images under `docs/assets/` (add per-section subfolders as it grows).
  - Always write meaningful alt text, and add a short caption when the figure
    needs context.
  - Prefer **language-neutral figures** so one image serves both locales. If a
    figure must contain text, either make a per-language version or keep the
    explanation in the caption (captions are translated anyway).
  - Don't lift figures from papers without attribution — cite the source (see
    citations below).

### Cross-linking, glossary & citations

- **Cross-link aggressively.** Whenever a page mentions a concept covered
  elsewhere, link to that page. Dense internal linking is a feature — it's what
  turns a pile of pages into a navigable map.
- **Glossary via hover tooltips (not click-jumps).** Terms are defined once in a
  central glossary include; matching terms across the site get a dotted
  underline and a **hover tooltip**, so readers get the definition in place
  without being yanked to another page.
  - Mechanism: Python-Markdown's `abbr` extension + `pymdownx.snippets`
    auto-appending `includes/glossary.md` to each page. *(Not yet enabled — wire
    this up when the first real content needs it.)*
- **Citations via a bibliography, not ad-hoc links.** Scientific papers are
  cited professionally: keep a BibTeX `.bib` file (exportable from
  Zotero/PubMed), cite inline with `[@key]`, and render a numbered reference list
  whose entries link out to the DOI / PubMed / publisher page.
  - Mechanism: the `mkdocs-bibtex` plugin. *(Not yet enabled — wire this up when
    the first cited page lands.)*

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
