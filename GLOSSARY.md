# Liu Lab Roadmap

The words this repo uses about its own pages and how they are written. Scientific terms for
readers are in the site glossary, not here.

## Language

**Roadmap page**:
A numbered overview page, such as `1.2-linux-git.md`, that maps one topic for an entry-level
student: the learning stages, how the concepts fit together, and the best outside material,
linked rather than taught.
_Avoid_: tutorial, textbook chapter

**How To guide**:
A page under `docs/7-how-to/`: hands-on steps for one specific experiment or analysis, the
layer below a roadmap page.
_Avoid_: tutorial

**Section**:
A numbered top-level directory, `1-basics` to `9-journal-club`. The nav shows it as a group
label, translated through `nav_translations`. A collection section has an `index.md` as its
clickable landing page.

**Numbered path**:
The file naming scheme: directories `1-basics` … `9-journal-club`, pages `1.1-…`, `1.2-…`.
The numbers appear in file paths and URLs only; nav labels come from each page's H1.

**Language pair**:
The two files for one URL: `foo.md` in English and `foo.zh.md` in Chinese. Each is written in
its own language's natural phrasing, and both change in the same commit.
_Avoid_: translation, original

**Draft banner**:
The red `!!! danger` box under the H1 of an agent-drafted page, in both languages, saying no
human has reviewed it yet. Only the user removes it.

**批注**:
A review comment the user leaves on its own line beside a passage, as
`<!-- 批注: ... -->`. Resolved and deleted when asked, and never committed, because it shows
in the built HTML source.
_Avoid_: TODO, note

**Site glossary**:
The reader-facing term definitions in `includes/glossary.md` and `includes/glossary.zh.md`,
which `hooks/glossary.py` turns into hover tooltips. Not this file.
_Avoid_: abbreviations, `abbr`

**New-page issue**:
An issue filed from `.github/ISSUE_TEMPLATE/new-page.yml`. Its fields (placement, the take,
bullets, opinions) are the raw material a page is drafted from, not its outline.
