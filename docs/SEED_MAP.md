# SEED Map (working, evolves)

This file exists to turn the raw seed document into actionable, evolving structure *without* treating it as final.

## What `SEED.md` is

- A structured brain dump from an initial kickoff conversation.
- Useful as a *starting context*, not an authoritative framework.

## Major themes already present (from `SEED.md`)

- Agentic dev is already practical: agents can implement, run tests, debug, refactor, and open PRs.
- Long-running sessions matter: context management/compaction enables multi-file work.
- Workflow beats model choice: spec-first development, explicit constraints, and small PRs.
- Role separation: “planner” vs “executor” models/agents.
- Async paradox: agents promise async progress but create frequent interruptions unless defaults/gates exist.
- Tech debt shift: legacy work becomes more tractable when agents can map and refactor safely.
- DevOps friction drops: CI/YAML/bash glue work becomes lower-leverage toil.
- Corporate expectations can distort reality: throughput goes up, but specs/review/validation still dominate.
- Overhype patterns: “replaces engineers”, “kills SaaS”, “you never code”.
- Identity/skill shift: from typing to thinking; from syntax recall to constraint articulation.

## How this maps to the repo (practical)

- Use `articles/` for *external sources* (each summary must include `source_url`).
- Use `docs/` for *our evolving synthesis and process* (like this file).
- Use `AGENT_LOG.md` to record what’s been processed and why.

## Research questions to drive capture (initial, not exhaustive)

- What *evidence* supports/contradicts “agents can ship PRs end-to-end” (and where does it fail)?
- What workflows consistently reduce interruptions (defaults, gates, batching questions)?
- How do teams quantify productivity changes (throughput vs review burden vs quality/security)?
- What’s the real impact on tech debt and refactoring (repeatable vs anecdotal)?
- What org changes are emerging (expectations, hiring, code review, QA)?
- Which market narratives recur, and what do credible counterpoints say?

## Next small refinements (suggested)

- Add a “claims to validate” list extracted from `SEED.md` (with wording preserved) and track evidence as sources come in.
- Create one evolving “Narrative Outline” doc once 10–20 sources are summarized.

