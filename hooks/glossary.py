r"""Glossary hover tooltips.

Wraps the *first* occurrence of each glossary term on a page in ``<abbr>``,
which Material renders as a hover tooltip (theme feature ``content.tooltips``).

Terms live in ``includes/glossary.md`` (English) and ``includes/glossary.zh.md``
(中文) — same suffix convention as ``docs/`` — written in the familiar
Markdown-abbr syntax::

    *[term]: definition

Why a hook instead of Python-Markdown's stock ``abbr`` extension: that extension
matches terms with ``\b…\b``. Every CJK character is a word character, so a
Chinese term surrounded by Chinese text never sits on a word boundary and
silently fails to match — and so does ``Transformer`` in ``建立在Transformer之上``.
"""

from __future__ import annotations

import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARIES = {
    "en": ROOT / "includes" / "glossary.md",
    "zh": ROOT / "includes" / "glossary.zh.md",
}

DEFINITION = re.compile(r"^\*\[(?P<term>[^\]]+)\]:[ \t]*(?P<definition>\S.*?)[ \t]*$", re.M)

# Regions a term must never be rewritten inside. Wrap anything else you want
# left alone in <!-- noglossary --> … <!-- /noglossary -->.
SKIP = re.compile(
    r"""
      ^```.*?^```                                            # fenced code block
    | ^~~~.*?^~~~
    | ^<!--[ \t]*noglossary[ \t]*-->.*?^<!--[ \t]*/noglossary[ \t]*-->
    | `[^`\n]+`                                              # inline code
    | !?\[[^\]]*\]\([^)]*\)                                  # inline link / image
    | !?\[[^\]]*\]\[[^\]]*\]                                 # reference link
    | <[^>]+>                                                # raw HTML tag
    | <https?://[^>]+>                                       # autolink
    | ^\#{1,6}[ ][^\n]*$                                     # heading (not .* — re.S)
    """,
    re.M | re.S | re.X,
)

_ASCII_WORD = re.compile(r"[A-Za-z0-9_]")

# locale -> {term: definition}, longest term first so 注意力机制 beats 注意力.
_terms: dict[str, dict[str, str]] = {}


def _pattern_for(term: str) -> str:
    """Match ``term``, plus an English plural ``s`` where that makes sense.

    Deliberately lookarounds over ``\\b``: a word boundary never fires between
    a CJK character and a Latin one, which is the bug this hook exists to fix.
    """
    left = r"(?<![A-Za-z0-9_])" if _ASCII_WORD.match(term[0]) else ""
    right = r"s?(?![A-Za-z0-9_])" if _ASCII_WORD.match(term[-1]) else ""
    return f"{left}{re.escape(term)}{right}"


def on_config(config):
    for locale, path in GLOSSARIES.items():
        if not path.exists():
            raise FileNotFoundError(f"glossary hook: missing {path}")
        entries = DEFINITION.findall(path.read_text(encoding="utf-8"))
        _terms[locale] = dict(sorted(entries, key=lambda kv: len(kv[0]), reverse=True))
    return config


def _wrap(text: str, unused: dict[str, str]) -> str:
    if not unused or not text.strip():
        return text
    pattern = re.compile("|".join(_pattern_for(term) for term in unused))

    def repl(match: re.Match) -> str:
        matched = match.group(0)
        key = matched if matched in unused else matched[:-1]  # drop plural "s"
        definition = unused.pop(key, None)  # None => already used on this page
        if definition is None:
            return matched
        return f'<abbr title="{escape(definition, quote=True)}">{matched}</abbr>'

    return pattern.sub(repl, text)


def on_page_markdown(markdown, page, config, files):
    locale = "zh" if page.file.src_uri.endswith(".zh.md") else "en"
    unused = dict(_terms.get(locale, {}))
    out, pos = [], 0
    for skipped in SKIP.finditer(markdown):
        out.append(_wrap(markdown[pos : skipped.start()], unused))
        out.append(skipped.group(0))
        pos = skipped.end()
    out.append(_wrap(markdown[pos:], unused))
    return "".join(out)
