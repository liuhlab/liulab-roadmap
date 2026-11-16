r"""Glossary hover tooltips.

Wraps *every* occurrence of each glossary term on a page in ``<abbr>``, which
Material renders as a hover tooltip (theme feature ``content.tooltips``).

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
from typing import Any

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
    r"""Match ``term``, plus an English plural ``s`` where that makes sense.

    Deliberately lookarounds over ``\b``: a word boundary never fires between
    a CJK character and a Latin one, which is the bug this hook exists to fix.
    """
    left = r"(?<![A-Za-z0-9_])" if _ASCII_WORD.match(term[0]) else ""
    right = r"s?(?![A-Za-z0-9_])" if _ASCII_WORD.match(term[-1]) else ""
    return f"{left}{re.escape(term)}{right}"


# The mkdocs objects are `Any`: the gate's environment holds no mkdocs to type them with.
def on_config(config: Any) -> Any:
    """Load both glossaries once per build, longest term first."""
    for locale, path in GLOSSARIES.items():
        if not path.exists():
            raise FileNotFoundError(f"glossary hook: missing {path}")
        entries = DEFINITION.findall(path.read_text(encoding="utf-8"))
        _terms[locale] = dict(sorted(entries, key=lambda kv: len(kv[0]), reverse=True))
    return config


def _wrap(text: str, terms: dict[str, str]) -> str:
    if not terms or not text.strip():
        return text
    pattern = re.compile("|".join(_pattern_for(term) for term in terms))

    def repl(match: re.Match) -> str:
        matched = match.group(0)
        key = matched if matched in terms else matched[:-1]  # drop plural "s"
        definition = terms.get(key)
        if definition is None:
            return matched
        return f'<abbr title="{escape(definition, quote=True)}">{matched}</abbr>'

    return pattern.sub(repl, text)


def on_page_markdown(markdown: str, page: Any, config: Any, files: Any) -> str:
    """Wrap glossary terms in the page's own language, outside code, links, HTML and headings."""
    locale = "zh" if page.file.src_uri.endswith(".zh.md") else "en"
    terms = _terms.get(locale, {})
    out, pos = [], 0
    for skipped in SKIP.finditer(markdown):
        out.append(_wrap(markdown[pos : skipped.start()], terms))
        out.append(skipped.group(0))
        pos = skipped.end()
    out.append(_wrap(markdown[pos:], terms))
    return "".join(out)
