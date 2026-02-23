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

## 2026-02-23 — Repo docs read + experience-capture operating mode

- What I did: Read all markdown docs currently in-repo to establish operating context, then aligned on a standing workflow: you provide experience entries and I place them in the most appropriate repo location.
- Files created/modified:
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Use doc intent to route new content:
    - Experience tied to an external source/article goes in `articles/<year>/...` using the summary template and required `source_url`.
    - Cross-source patterns and framework changes go in `docs/` synthesis/process docs.
    - Session-level traceability and operational notes go in [`AGENT_LOG.md`](AGENT_LOG.md).
  - Keep updates incremental and commit-friendly to preserve reviewability and historical traceability.
- Assumptions:
  - “Read all the docs” refers to all tracked markdown docs currently present in this repository.
  - Future “experience” entries may be either source-backed observations or first-person workflow notes; placement will depend on which type you provide.
- Commands run (if any):
  - `pwd && rg --files -g '*.md'`
  - `ls -la`
  - `cat AGENTS.md`
  - `cat README.md`
  - `cat CONTRIBUTING.md`
  - `cat INDEX.md`
  - `cat docs/PROJECT_PROMPT.md`
  - `cat docs/SUMMARY_GUIDE.md`
  - `cat docs/SYNTHESIS_GUIDE.md`
  - `cat docs/SEED_MAP.md`
  - `cat SEED.md`
  - `cat AGENT_LOG.md`
  - `cat articles/README.md`
  - `cat templates/article-summary.md`
- Test results (if relevant):
  - N/A (documentation read/log update only).
- Open questions / ambiguities:
  - For pure first-person experience entries without external sources, should the primary long-form home be `docs/` (new dedicated experience log) or remain only in [`AGENT_LOG.md`](AGENT_LOG.md) plus occasional synthesis updates?
- Areas needing clarification:
  - Preferred granularity for each experience entry (quick bullet vs structured mini-report).
- Improvements to your own workflow:
  - Continue logging each processing session immediately after context-read or content-write to keep assumptions and routing decisions explicit.

## 2026-02-23 — Experience entry: agents harden after bugfix

- What I did: Captured a first-person experience note about agent behavior during bug fixing (fix + preventative improvements).
- Files created/modified:
  - Created: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Placed first-person experiences in `docs/` (not `articles/`) since they are not external sources and do not have a `source_url`.
  - Used a dated entry format so later synthesis can reference stable timestamps.
- Assumptions:
  - These first-person entries may be distilled later into synthesis docs once patterns accumulate.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A
- Open questions / ambiguities:
  - Should experience entries also include minimal context fields (tool, repo type, language, failure mode) to improve later synthesis?
- Areas needing clarification:
  - None.
- Improvements to your own workflow:
  - Keep experience notes concise and dated; add context fields only when they materially help retrieval.

## 2026-02-23 — Distill similar experiences from seed into experience log

- What I did: Scanned [`SEED.md`](SEED.md) for experience-style observations similar to “bugfix plus hardening” and distilled them into additional entries in the experience log.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Marked entries as “From seed context” to preserve provenance and avoid implying they came from external sources.
  - Kept the new entries short and adjacent to the original bugfix-hardening entry to keep the log scannable.
- Assumptions:
  - Seed content reflects prior first-person experience and is acceptable to distill into the experience log as long as provenance is labeled.
- Commands run (if any):
  - `rg -n "bug|debug|fix|refactor|safe refactor|adds tests|harden|prevent|failure|risk|iterate|tests pass|tech debt|liquid|self-improving|document" SEED.md`
  - `nl -ba SEED.md | sed -n '60,120p'`
  - `nl -ba SEED.md | sed -n '240,340p'`
- Test results (if relevant):
  - N/A (docs-only changes).
- Open questions / ambiguities:
  - If the experience log grows, do you want a lightweight tag line per entry (e.g., `tags: bugfix, refactor, ci`) for later synthesis?

## 2026-02-23 — Experience entry: offload context to disk (agent-written artifacts)

- What I did: Captured a first-person experience note that agents work better when context is stored in repo files (specs/notes/decisions) that the agent can read and update, including using the agent to author those context files.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Kept this as an experience entry (not synthesis) since it’s a direct workflow observation rather than a cross-source claim.
- Assumptions:
  - “Context offloading” refers to storing durable project constraints and decisions in files on disk rather than relying on chat-only memory.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A
