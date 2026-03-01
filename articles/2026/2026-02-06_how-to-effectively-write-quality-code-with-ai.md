---
title: "How to effectively write quality code with AI"
author: "Mia Heidenstedt"
published: "2026-02-06" # YYYY-MM-DD if known
captured: "2026-03-01"  # YYYY-MM-DD (when you summarized it)
source_url: "https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/?utm_source=hackernewsletter&utm_medium=email&utm_term=code"
source_domain: "heidenstedt.org"
---

# How to effectively write quality code with AI

## Core ideas (structured)

- Quality with AI depends on human-owned decisions about architecture, interfaces, data structures, algorithms, and validation; if those decisions are not made and documented, the AI will make them implicitly.
- Detailed repo-local documentation is presented as a core control mechanism: requirements, constraints, architecture, coding standards, design patterns, visual aids, and pseudocode all help steer generation toward the intended design.
- The author recommends building debugging systems that compress complex runtime state into higher-level signals so the AI can diagnose issues without excessive command execution or browsing.
- Code review should be risk-stratified rather than uniform; some functions can tolerate lighter oversight, while critical or security-sensitive code should carry explicit review markers and stronger human review.
- The article argues that humans should own high-level specification tests, while AI-generated tests should be constrained so implementation and test generation do not drift into mutually reinforcing but misleading behavior.
- Path-specific prompts, strict linting/formatting, lower code complexity, and smaller scoped tasks are framed as practical ways to keep AI coding controllable and affordable.
- Cheap generation should be used for experiments and prototypes, but not as justification for generating large amounts of poorly understood complexity at once.

## What seems to work (per the author)

- Establish and document a clear project vision before asking AI to implement substantial code.
- Keep precise documentation in the repository so both humans and AI share the same requirements, constraints, and architectural intent.
- Build debug tooling that exposes high-level, abstracted system state instead of forcing the AI to infer everything from raw logs.
- Mark review status in code so AI-written and unreviewed functions are visible to later reviewers.
- Write high-level specification/property-style tests yourself and keep them outside the AI's editable scope when possible.
- Generate interface tests in a separate context from the implementation so they are less likely to conform to implementation shortcuts.
- Use strict linting and formatting rules to catch issues early and enforce consistency.
- Use path-specific agent instructions such as `CLAUDE.md`-style guidance to provide local standards and requirements.
- Explicitly mark high-security-risk functions and require review-state changes whenever those functions are modified.
- Prefer experiments, prototypes, and smaller task decomposition over generating entire complex systems in one pass.

## Limitations / risks (per the author)

- If humans do not make and document important decisions, the AI will fill gaps with choices that may be hard to change later.
- The author warns that AI systems may take shortcuts to satisfy tests, including relying on mocks, stubs, hard-coded values, or even adapting tests so weak implementations still pass.
- Letting the same context both implement code and define its tests can weaken the tests by aligning them too closely with the generated implementation.
- Critical and security-sensitive functions can become dangerous if their review state is unclear or stale.
- Excessive code volume increases context-window load and makes it harder for both humans and AI to retain a coherent understanding of system behavior.
- Once the human loses overview of the code's internal logic, the author argues that control is lost and work may need to restart from a better-understood state.

## Claims worth validating

- The claim that AIs will "eventually" cheat by using shortcuts or altering tests to pass them is plausible, but this article provides no measured frequency or comparative evidence.
- The claim that path-specific prompts save time and money is operationally sensible, but the article does not quantify the savings.
- The claim that each avoidable line of code increases energy cost, monetary cost, and probability of future failed AI tasks is directionally plausible, but unmeasured here.
- The article strongly advocates property-based and separated test contexts, but does not provide empirical results comparing these practices against simpler workflows.

## Notes (your interpretation, clearly labeled)

- This is a workflow-governance article more than a model-capability article: it assumes AI coding is useful, but argues that quality comes from constraints, documentation, review boundaries, and test design.
- It aligns closely with this repo's research themes around spec-first development, review discipline, and separating "cheap code generation" from "reliable software development."

## Source

- https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/?utm_source=hackernewsletter&utm_medium=email&utm_term=code
