# Agent Instructions (ai-in-software-dev)

Use this repo to build a grounded, markdown-first field report on how AI is changing software development (2023–2026).

## Ground rules

- Don’t hallucinate: only summarize what a source actually says; label interpretation separately.
- Preserve traceability: every summary must include the original `source_url`.
- Keep changes incremental and commit-friendly (prefer one source per commit plus updated [`INDEX.md`](INDEX.md)).
- Let themes emerge; don’t impose rigid taxonomies too early.
- Treat slides/presentations as optional outputs derived from research (not the primary goal).

## Canonical project brief

- See [`docs/PROJECT_PROMPT.md`](docs/PROJECT_PROMPT.md) for the full plan (phases, constraints, end goal).

## Seed context (non-authoritative)

- Read [`SEED.md`](SEED.md) before starting work.
- Treat it as raw initial research and thinking, not a finalized structure or “source of truth”.
- You are expected to refine, question, and evolve it over time.

## Key repo docs

- Summary guidance: [`docs/SUMMARY_GUIDE.md`](docs/SUMMARY_GUIDE.md)
- Synthesis guidance: [`docs/SYNTHESIS_GUIDE.md`](docs/SYNTHESIS_GUIDE.md)
- Seed distillation map: [`docs/SEED_MAP.md`](docs/SEED_MAP.md)
- Workflow: [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Required behavior (always)

Maintain a running log in [`AGENT_LOG.md`](AGENT_LOG.md).

For every task/blog processed, log:
- What you did
- Files created/modified
- Decisions made (and why)
- Assumptions
- Commands run (if any)
- Test results (if relevant)
- Open questions / ambiguities
- Areas needing clarification
- Improvements to your own workflow
