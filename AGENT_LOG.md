# AGENT_LOG

This is a running log of work performed in this repository so future agents can see what was processed and why.

## 2026-02-23 — Seed + logging requirements wired in

- What I did: Read [`SEED.md`](SEED.md) and updated agent instructions to treat it as non-authoritative seed context.
- Files created/modified:
  - Modified: [`AGENTS.md`](AGENTS.md)
  - Created: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made:
  - Added explicit “seed is not source of truth” guidance so future work can evolve structure without anchoring on the brain dump.
  - Added mandatory logging checklist to reduce repeated work and capture assumptions/ambiguities.
- Assumptions:
  - The seed file is named [`SEED.md`](SEED.md) in this repo (user referenced `seed.md`), but the intent is the same seed document.
- Commands run:
  - `ls -la`
  - `nl -ba SEED.md | sed -n '1,240p'`
  - `nl -ba AGENTS.md | sed -n '1,200p'`
  - `nl -ba docs/PROJECT_PROMPT.md | sed -n '1,60p'`
- Test results: N/A (doc-only changes).
- Open questions:
  - Should we distill [`SEED.md`](SEED.md) into a smaller “working outline” doc (separate from article summaries) to guide early capture?
  - Do you prefer the seed file to be renamed to `seed.md` for consistency, or keep [`SEED.md`](SEED.md) as-is?
  - [`SEED.md`](SEED.md) is currently untracked in git (`git status` shows it as `??`); should it be added to version control?

## 2026-02-23 — Seed distillation map added

- What I did: Created a lightweight mapping doc that turns seed themes into actionable capture questions without freezing structure.
- Files created/modified:
  - Created: [`docs/SEED_MAP.md`](docs/SEED_MAP.md)
  - Modified: [`AGENTS.md`](AGENTS.md)
- Decisions made:
  - Kept [`SEED.md`](SEED.md) intact; added a separate “map” doc so we can evolve structure incrementally.
- Assumptions:
  - The themes listed are intended as guidance and will be revised as external sources are captured.
- Commands run:
  - `rg -n '^#' SEED.md | head -n 80`
  - `nl -ba SEED.md | sed -n '220,520p'`
- Test results: N/A (doc-only changes).
- Open questions:
  - Do you want the “claims to validate” list extracted now (verbatim phrasing), or wait until the first batch of external sources is captured?

## 2026-02-23 — Seed file decision

- Decision: Keep the filename as [`SEED.md`](SEED.md) (uppercase) and treat it as a repo-tracked artifact going forward.
- Why:
  - It’s already present with that name, and uppercase makes it prominent as “seed context”.
  - Tracking it in git preserves the initial baseline for future refinement and prevents drift/forgetting.
- Commands run:
  - `git add SEED.md AGENTS.md AGENT_LOG.md docs/SEED_MAP.md`

## 2026-02-23 — Reposition docs: research first, slides optional

- What I did: Updated repo documentation to emphasize the primary purpose as research/synthesis and treat slides as a secondary derivative output.
- Files modified:
  - [`README.md`](README.md)
  - [`AGENTS.md`](AGENTS.md)
  - [`docs/PROJECT_PROMPT.md`](docs/PROJECT_PROMPT.md)
  - [`docs/SYNTHESIS_GUIDE.md`](docs/SYNTHESIS_GUIDE.md)
  - [`SEED.md`](SEED.md)
- Summary of changes:
  - Removed “slide deck project” framing from the project plan title; reframed slide generation as an optional derivative artifact.
  - Added a consistent one-line statement in key entrypoints that research/synthesis is the primary goal and slides are optional.
  - Added a short note at the top of [`SEED.md`](SEED.md) to prevent readers from treating seed content as authoritative.
- Rationale (wording decisions):
  - Kept “field report” language but made the primary/secondary outputs explicit to avoid misreading the repo as a deck-building effort.
  - Avoided broad rewrites; made small, local edits to reduce churn and keep diffs reviewable.
- Ambiguities / gaps:
  - The task referenced `OUTLINE.md`, `SLIDES_SKELETON.md`, `TODO.md`, etc.; these files do not exist in the repo at this time.
- Commands run:
  - `rg -n "slide|deck|presentation" -S .`
  - `git diff --stat`
  - `git add -A`
- Test results: N/A.

## 2026-02-23 — Convert doc references to relative links

- What I did: Converted doc-to-doc file references from absolute filesystem paths to relative markdown links for GitHub-friendly navigation.
- Files modified:
  - [`README.md`](README.md)
  - [`AGENTS.md`](AGENTS.md)
  - [`AGENT_LOG.md`](AGENT_LOG.md)
  - [`CONTRIBUTING.md`](CONTRIBUTING.md)
  - [`docs/SEED_MAP.md`](docs/SEED_MAP.md)
  - [`articles/README.md`](articles/README.md)
- Decisions made:
  - Kept commands as code (no linking inside command snippets); only converted cross-document references.
- Commands run:
  - `rg -n "/Users/|\\.md:1" -S .`
