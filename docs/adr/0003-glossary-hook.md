---
search:
  exclude: true
---

# Glossary tooltips come from a build hook, not the `abbr` extension

Each page shows a hover tooltip on every glossary term. The terms live in
`includes/glossary.md` and `includes/glossary.zh.md`, one `*[term]: definition` line each.
`hooks/glossary.py` reads them when the build starts and wraps each term on a page in
`<abbr>`, using the glossary in the page's own language.

Python-Markdown's `abbr` extension reads the same syntax, and we do not use it. It matches a
term with `\b…\b`, and every CJK character is a word character, so a Chinese term inside
Chinese text never sits on a word boundary. It silently fails to match, and so does
`Transformer` in `建立在Transformer之上`. The hook matches with lookarounds that test for
an ASCII letter or digit instead.

## What it costs

- **A regex rewrites every page.** A bug here corrupts prose site-wide and a strict build
  still passes. The hook is in the gate (ruff and pyright) for that reason. After changing
  it, compare the built pages with a build from before the change.
- **The hook skips regions by pattern**: code, inline code, links, raw HTML and headings.
  Anything else a term must not touch goes between `<!-- noglossary -->` and
  `<!-- /noglossary -->`.
- **Two glossaries, one name.** These tooltip files are for readers. `GLOSSARY.md` at the
  repo root is the words this repo uses, for agents and maintainers.
