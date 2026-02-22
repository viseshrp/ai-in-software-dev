# ai-in-software-dev

A markdown-first, incrementally-built field report on how AI is changing software development (2023–2026).

## Workflow (high level)

1. Capture an article into `articles/` as a structured summary (signal > fluff).
2. Keep original links for traceability.
3. Avoid hallucinating content not present in the source.
4. Let themes emerge before enforcing rigid categories.

## Common commands

- Create a new summary stub: `python3 scripts/new_article.py --title "..." --url "https://..." --published 2025-10-01`
- Rebuild the index: `python3 scripts/build_index.py`
