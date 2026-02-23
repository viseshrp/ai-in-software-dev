# Articles

This folder holds one markdown file per source article/post, summarized into structured bullets.

## Naming

- Files are created under `articles/<year>/` and named like: `YYYY-MM-DD_<slug>.md`
- Prefer using the publication date (`published`) when known; otherwise use the capture date.

## Required fields

For a file to show up in [`INDEX.md`](../INDEX.md), it must include frontmatter keys:

- `title`
- `source_url`

## Creating a new stub

Use:

`python3 scripts/new_article.py --title "..." --url "https://..." --published 2025-10-01`

Then fill in the sections based strictly on the source.
