---
title: "How I Use Claude Code"
author: "Boris Tane"
published: "2026-02-10" # YYYY-MM-DD if known
captured: "2026-03-01"  # YYYY-MM-DD (when you summarized it)
source_url: "https://boristane.com/blog/how-i-use-claude-code/?utm_source=tldrnewsletter"
source_domain: "boristane.com"
---

# How I Use Claude Code

## Core ideas (structured)

- The author uses a strict pipeline for AI-assisted development: research the existing codebase, produce a written plan, annotate/refine the plan, then allow the agent to implement.
- Central rule: do not let the AI write code until a human has reviewed and approved a written plan artifact.
- “Research” means deep reading of the relevant codebase area, with findings written to a persistent markdown file (used as the human review surface).
- The “annotation cycle” is where architectural and scope decisions are made: accept/modify/remove plan items until the plan matches human intent and project constraints.
- During implementation, the author uses terse feedback and points to existing patterns in the codebase rather than describing requirements from scratch.
- When the agent goes off-track, the author prefers reverting changes and re-scoping rather than incremental patching of a bad approach.
- The author favors single long sessions so the agent accumulates context, and relies on the plan document as an anchor artifact that survives context compaction.

## What seems to work (per the author)

- Use “deep-read” prompts that explicitly demand thoroughness; require a written `research.md` artifact instead of relying on chat summaries.
- Write a detailed `plan.md` that includes approach, file paths to change, code snippets, and trade-offs; keep it as an editable project artifact rather than relying on built-in plan modes.
- Iterate on the plan through explicit annotations until the implementation should be “boring” and mechanical.
- Provide reference-based guidance: point to existing tables/pages/components and instruct the AI to match them (“make it look exactly like X”) to capture implicit requirements.
- Shift to short, direct corrections during execution because the agent already has context from the approved plan.
- Cut scope actively (remove nice-to-haves) and protect interfaces by setting non-negotiable constraints (e.g., function signatures must not change).
- When work drifts, discard the git changes and restate a narrower goal rather than trying to salvage an overly complex direction.

## Limitations / risks (per the author)

- Without an upfront research phase, the agent may implement “reasonable” changes that break surrounding system conventions (caching layers, ORM rules, duplicated logic, wrong app surface), creating expensive rework.
- Without an approved plan, the agent may make a plausible but wrong early assumption and build a long chain of changes that must be unwound.
- Frontend work remains iterative; visual correctness often requires tight feedback loops and sometimes screenshots.
- The workflow assumes the developer can evaluate architectural trade-offs and make judgment calls the AI cannot reliably infer (product direction, engineering culture, acceptable complexity).

## Claims worth validating

- The claim that this workflow yields better results with fewer tokens than “prompt then fix errors” is plausible but unquantified here.
- The claim that single long sessions do not degrade performance materially (and that compaction preserves enough context) is user-experience based and not benchmarked.
- The claim that reverting and re-scoping beats incremental patching for off-track work is plausible but may vary by codebase and task type.

## Notes (your interpretation, clearly labeled)

- This is a concrete instantiation of “planner/executor separation” with durable artifacts: `research.md` and `plan.md` act as the shared contract between human intent and agent execution.
- It maps closely to this repo’s recurring themes: small, reviewable steps; explicit constraints; avoiding accidental architecture drift; and using repo docs as durable context.

## Source

- https://boristane.com/blog/how-i-use-claude-code/?utm_source=tldrnewsletter
