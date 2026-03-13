---
title: "Writing code is cheap now"
author: "Simon Willison"
published: "2026-02-23" # YYYY-MM-DD if known
captured: "2026-03-13"  # YYYY-MM-DD (when you summarized it)
source_url: "https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/"
source_domain: "simonwillison.net"
---

# Writing code is cheap now

## Core ideas (structured)

- The chapter argues that the biggest conceptual shift in agentic engineering is accepting that writing code itself has become cheap relative to the surrounding work of deciding what to build and ensuring the result is good.
- Willison says many engineering habits were formed around code being expensive, both at the macro level of planning and estimation and at the micro level of everyday trade-offs about refactors, tests, documentation, and tooling.
- Coding agents disrupt those habits because they dramatically reduce the cost of producing code, and parallel agents amplify that shift by letting one engineer explore multiple implementation paths at once.
- The chapter stresses that “good code” is still expensive, even if raw code generation is cheap.
- Willison defines good code broadly: it works, solves the right problem, handles errors well, is simple, tested, documented, change-friendly, and satisfies the relevant non-functional quality attributes.
- The author’s conclusion is that teams need new personal and organizational habits that match these new economics, rather than reusing intuitions from an era when developer typing time was the scarce resource.

## What seems to work (per the author)

- The chapter suggests it is increasingly worthwhile to try ideas that older cost intuitions would have rejected, because the downside may now be only a small amount of token spend and review time.
- Coding agents can help with many parts of producing good code, provided the developer actively drives the process and checks whether the output meets the project’s quality bar.
- A practical habit the author recommends is to challenge the instinct that something is “not worth building” and instead test that intuition by prompting an asynchronous agent session.

## Limitations / risks (per the author)

- The author is explicit that the industry is still figuring out these best practices, and presents this chapter as an evolving perspective rather than a settled framework.
- Cheap code generation does not remove the cost of making code good; developers still carry substantial responsibility for validation, design, and quality control.
- The chapter is intentionally high level and does not provide a detailed process for turning this mindset shift into concrete team practices.

## Claims worth validating

- The core claim that coding agents “dramatically” reduce the cost of producing code is directionally plausible, but this chapter does not quantify that reduction.
- The suggestion that parallel agents substantially change micro-level engineering trade-offs is compelling, but the chapter offers it as a conceptual argument rather than measured evidence.
- The practical heuristic that it is often worth trying an idea in an async agent session because the worst-case cost is just tokens and review time will vary significantly by codebase, tooling, and governance constraints.

## Notes (your interpretation, clearly labeled)

- This is a concise framing piece for the repo because it names a core economic shift behind several other sources: when implementation gets cheaper, more effort can move toward evaluation, quality, and opportunity selection.
- It pairs especially well with Steve Krenzel’s “AI Is Forcing Us To Write Good Code.” Willison argues that code is cheap but good code is not; Krenzel provides one concrete response to that distinction.
- It is also useful as a bridge between product-oriented sources and code-quality sources, because it explains why planning intuitions, feature triage, testing, and documentation all change together under agentic development.

## Source

- https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/
