---
search:
  exclude: true
---

# Build the site with mkdocs-material, not zensical

The lab template builds its sites with zensical. This site stays on mkdocs plus
mkdocs-material, because zensical would not build it: zensical has no hook or plugin system,
and this site needs three.

- `mkdocs-static-i18n` builds the English and Chinese sites from the `foo.md` /
  `foo.zh.md` suffix pairs and gives the top bar its language switcher.
- `git-revision-date-localized` stamps each page's footer with its file's last commit date.
- `hooks/glossary.py` turns glossary terms into hover tooltips
  (see [0003](0003-glossary-hook.md)).

Only the docs tasks and the deploy differ from the template. `docs` and `docs-build` call
mkdocs, and `deploy.yml` publishes with `mkdocs gh-deploy` through the `docs-deploy` task.
The template hand-writes a two-step publish only because zensical has no `gh-deploy`.

## What it costs

- **`navigation.instant` stays off.** It breaks the language switcher's links to the
  same page in the other language.
- **Two plugins come from PyPI.** `mkdocs-static-i18n` is not on conda-forge, and
  conda-forge's revision-date plugin stopped at 1.2.9, before the locale fix i18n needs.
  Both sit in `[tool.pixi.feature.docs.pypi-dependencies]`.
- **Plugin order matters.** `git-revision-date-localized` must come after `i18n` in
  `plugins:`. It reads the locale that i18n attaches to each file, and the build fails
  otherwise.
- **Every checkout that builds needs full history.** The footer date comes from `git log`
  on each file, so CI checks out with `fetch-depth: 0`. A shallow clone dates every page
  the same and still exits 0.
- **Agent-facing pages are kept out of the site twice.** `exclude_docs:` in `mkdocs.yml`
  keeps `docs/adr/` and `docs/agents/` out of the build, which zensical cannot do. The
  `search: exclude: true` front matter stays too, because conformance checks for it.
