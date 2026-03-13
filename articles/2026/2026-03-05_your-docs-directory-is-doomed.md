---
title: "Your Docs Directory Is Doomed"
author: "Jim Yagmin"
published: "2026-03-05" # YYYY-MM-DD if known
captured: "2026-03-12"  # YYYY-MM-DD (when you summarized it)
source_url: "https://yagmin.com/blog/your-docs-directory-is-doomed/?utm_source=tldrdev"
source_domain: "yagmin.com"
---

# Your Docs Directory Is Doomed

## Core ideas (structured)

- The author argues that the common pattern of accumulating `CLAUDE.md`, `AGENTS.md`, architecture docs, specs, and a growing `/docs` tree is a temporary and ultimately inadequate way to manage context for AI-assisted software development.
- In the author’s view, this pattern emerges naturally as teams try to feed more context to coding agents, but it accumulates hidden costs over time.
- The post identifies several failure modes in a large markdown-doc context system: poor discoverability, unclear ownership, doc rot, mismatched update velocities, lack of hierarchy, and inconsistent document structure.
- A central argument is that better models will not solve the core problem, because context production and management are distinct from code generation.
- The author treats context as a blueprint of product intent, usage, and real-world constraints, not something that can simply be inferred from code after the fact.
- The proposed direction is a richer context system where context is organization-owned, navigable, composable, and code-aware.
- This leads to what the author calls Context-Driven Development (CDD): a development style where context documents are tightly coupled to code and become an abstraction layer and source of truth for why the product is designed the way it is.

## What seems to work (per the author)

- Starting with lightweight files such as `CLAUDE.md`, `AGENTS.md`, and a few core docs is presented as a natural and initially useful evolution.
- The author argues that context becomes much more powerful when it is explicitly structured rather than treated as a loose pile of markdown.
- Organization-owned context is presented as a better model than relying on engineers to maintain all contextual knowledge, especially when important product context originates with non-engineering stakeholders.
- Context should be navigable: documents need relationships and architecture so humans and LLMs can discover relevant information deterministically.
- Context should be composable: higher-level process context should be built from lower-level concept context in a hierarchy the model can traverse.
- Context should be code-aware: mapping context directly to code creates a feedback loop that can surface inconsistencies and enable automatic updates.
- In the author’s framing, CDD works by making docs and code mutually inspectable so humans can move between abstraction and implementation without losing the underlying source of truth.

## Limitations / risks (per the author)

- A simple `/docs` directory becomes less reliable as more files accumulate and the codebase changes underneath them.
- LLM-managed documentation can still drift or “lose the plot” if consistency is maintained blindly rather than observably.
- Different categories of context evolve at different speeds, making uniform maintenance policies difficult.
- LLMs do not inherently know which document to read when, so relevant information may be missed during planning or generation.
- Without explicit structure, linked docs remain only loosely related from the model’s perspective.
- The article implies that moving toward organization-owned, navigable, code-aware context is a significant change in process and coordination, not just a tooling tweak.

## Claims worth validating

- The claim that a growing markdown docs directory is fundamentally temporary or “doomed” is persuasive in the article, but still a strong prediction rather than a demonstrated inevitability.
- The claim that context management is now the biggest blocker to progress is a plausible practitioner judgment, not a quantified result here.
- The suggestion that linked, code-aware context can support automatic updates and inconsistency detection is compelling, but the post presents it more as direction than a validated production pattern.
- The implication that CDD is “almost the antithesis” of vibe coding is interpretive and depends on how tightly the proposed context-code linkage can actually be maintained.

## Notes (your interpretation, clearly labeled)

- This article is highly relevant to the repo because it pushes directly on one of the repo’s most active themes: durable context, rules files, docs freshness, and how AI systems navigate codebase knowledge.
- It acts as a useful counterpoint to posts that recommend ever-richer docs and rules files without dwelling on their long-run maintenance cost.
- It may be especially valuable for future synthesis because it reframes “better prompting” as a context-architecture problem, not just a wording problem.

## Source

- https://yagmin.com/blog/your-docs-directory-is-doomed/?utm_source=tldrdev
