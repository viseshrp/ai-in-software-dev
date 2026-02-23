# Contributing

This repo is an incremental knowledge base. Keep changes small and traceable.

## Adding a source (Phase 1)

1. Create a stub:
   - `python3 scripts/new_article.py --title "..." --url "https://..." --published YYYY-MM-DD`
2. Fill in the bullets based strictly on the source.
3. Keep your own interpretation only in the “Notes (your interpretation)” section.
4. Rebuild the index:
   - `python3 scripts/build_index.py`

## Version control

- Prefer one article per commit (plus the updated [`INDEX.md`](INDEX.md)).
- Keep commit messages descriptive (e.g., “Summarize: <title>”).
