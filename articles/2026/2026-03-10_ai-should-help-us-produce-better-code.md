---
title: "AI should help us produce better code"
author: "Simon Willison"
published: "2026-03-10" # YYYY-MM-DD if known
captured: "2026-03-13"  # YYYY-MM-DD (when you summarized it)
source_url: "https://simonwillison.net/guides/agentic-engineering-patterns/better-code/?utm_source=tldrnewsletter"
source_domain: "simonwillison.net"
---

# AI should help us produce better code

## Core ideas (structured)

- The chapter argues that if coding agents reduce software quality, teams should treat that as a process problem to fix rather than as an unavoidable consequence of using AI.
- Willison frames the issue in terms of technical debt: many teams accept debt because “doing it right” takes too long, but coding agents change that time trade-off.
- He emphasizes that many technical-debt fixes are conceptually simple but laborious, such as renaming concepts consistently, unifying duplicate functionality, correcting awkward APIs, or splitting oversized files.
- The chapter presents those refactoring tasks as a particularly strong use case for asynchronous coding agents running in the background on branches or worktrees.
- Beyond refactoring, the piece argues that AI tools make it cheaper to explore more design and technology options, especially through quick prototypes and simulations that test assumptions directly.
- The final idea is that teams should improve not just the code but also the instructions and process around agents, using retrospectives and documented lessons to compound quality over time.

## What seems to work (per the author)

- Asynchronous coding agents are presented as useful for background refactors that would otherwise interrupt a developer’s main flow.
- The recommended operating pattern is to let the agent work in a branch or worktree, then evaluate the result in a pull request and either accept it, redirect it with another prompt, or discard it.
- Low-cost agentic refactors are presented as enabling a much stricter stance against minor code smells and avoidable inconsistencies.
- LLMs are presented as useful for suggesting familiar, common solutions that teams may have overlooked, especially when selecting “boring” technologies likely to work.
- Exploratory prototyping is presented as another strong use case: agents can cheaply build simulations or spike implementations so teams can compare options before committing.
- The “compound engineering” loop described from Every, where teams document what worked after each project, is presented as a practical way to improve future agent runs.

## Limitations / risks (per the author)

- The chapter assumes teams have review discipline, since agent-generated refactors are only valuable if someone evaluates whether the result is actually good.
- The author notes that if an agent’s output is bad, teams should be willing to discard it entirely rather than force it through.
- LLM suggestions are bounded by their training data and may mainly surface common approaches rather than novel or context-specific ones.
- The chapter is a high-level practice note, not a detailed empirical study of which refactors or prototyping patterns work best across different teams.

## Claims worth validating

- The claim that coding agents reduce the cost of code improvements enough to justify “zero tolerance” for minor code smells is a strong proposition that will vary by codebase and review burden.
- The claim that agents can build useful simulations from a single well-crafted prompt, making technical experiments “almost nothing” in cost, is plausible but highly context-dependent.
- The idea that teams can now “finally have both” quality improvements and new feature delivery depends on surrounding process, test infrastructure, and review capacity, not just model capability.
- The framing that worse code from agents is always a choice is directionally useful, but probably understates the constraints imposed by weak tests, poor observability, or messy legacy systems.

## Notes (your interpretation, clearly labeled)

- This chapter fits well with the repo’s recurring claim that AI should increase the ambition of engineering quality, not relax it.
- It extends the previous `Writing code is cheap now` chapter: once code production is cheap, Willison argues the saved effort should be reinvested into debt reduction, prototyping, and better decision-making.
- It also connects to Steve Krenzel’s article from a different angle. Krenzel emphasizes structural guardrails in the codebase; Willison emphasizes using cheap agent labor to actively pay down debt and improve future choices.

## Source

- https://simonwillison.net/guides/agentic-engineering-patterns/better-code/?utm_source=tldrnewsletter
