---
search:
  exclude: true
---

# Serve our own copy of Mermaid

mkdocs-material draws Mermaid diagrams with a copy of `mermaid.js` it loads from unpkg.com
when a page needs one. The Great Firewall blocks unpkg, so readers in mainland China see a blank
figure where each diagram should be.

So the site ships its own copy, `docs/assets/javascripts/mermaid.min.js`, listed in
`extra_javascript:` with `defer: true`. Material fetches from the CDN only while
`window.mermaid` is undefined. A deferred script runs before `DOMContentLoaded`, which is
when Material mounts the diagrams, so our copy is always there first and the CDN is never
asked.

## What it costs

- **The copy does not update itself.** A new Material release may expect a newer
  Mermaid, and nothing will say so. Replace the file by hand and check a diagram page in
  both colour schemes.
- **Do not drop it to save weight.** Removing the file or its `extra_javascript:` entry
  builds green and passes every check, and breaks every diagram for the readers it exists
  for.
