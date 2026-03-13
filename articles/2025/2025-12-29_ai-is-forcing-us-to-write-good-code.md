---
title: "AI Is Forcing Us To Write Good Code"
author: "Steve Krenzel"
published: "2025-12-29" # YYYY-MM-DD if known
captured: "2026-03-13"  # YYYY-MM-DD (when you summarized it)
source_url: "https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code?utm_source=tldrdev"
source_domain: "bits.logic.inc"
---

# AI Is Forcing Us To Write Good Code

## Core ideas (structured)

- The article argues that many longstanding “good code” practices become much more valuable when teams use coding agents, because agents depend heavily on explicit structure and guardrails.
- Krenzel’s central claim is that agents are poor at making a mess and cleaning it up later, so codebases need stronger up-front constraints if teams want reliable agentic development.
- The post highlights several specific investments his six-person team made for agentic coding: 100% code coverage, thoughtful directory structure and small files, fast ephemeral concurrent dev environments, strict automation, and end-to-end types.
- The coverage argument is not framed mainly as bug prevention; instead, tests are described as an executable proof that every changed line’s behavior has been checked.
- File organization is treated as a machine-facing interface because agents navigate primarily through filenames, directories, search, and file reads rather than a holistic human mental model of the codebase.
- Fast, isolated development environments are presented as necessary because teams using agents tend to run many parallel worktrees or processes, each of which needs quick setup and cheap repeated verification.
- Strong typing and automated checks are presented as ways to reduce the search space available to the model and to make illegal states or invalid transitions harder to express in the first place.

## What seems to work (per the author)

- Requiring 100% line coverage seems, in the author’s experience, to make coverage reports act like a precise to-do list for agent-written tests and reduces ambiguity about what still needs verification.
- Keeping files small, well-scoped, and semantically named appears to improve agent navigation and reduce the chance that important context gets truncated or summarized away.
- Fast guardrails such as tests, hooks, linters, and formatters seem to work best when they are cheap enough to run constantly throughout an agent loop rather than only at the end.
- One-command creation of fresh worktrees with copied local config, installed dependencies, and an agent-ready prompt is presented as a practical way to make ephemeral environments routine rather than burdensome.
- Concurrent, isolated environments with configurable ports, databases, caches, and jobs are presented as important for running several agentic workstreams at once without cross-talk.
- End-to-end typing via TypeScript, OpenAPI-generated clients, and typed database/application boundaries is presented as a strong way to communicate intent and catch invalid actions early.

## Limitations / risks (per the author)

- The article is experience-based and team-specific; it does not claim that every team needs exactly the same tooling or standards to benefit from agents.
- The author acknowledges that some of these investments are controversial or feel like an up-front tax, even if he argues the tax is worth paying.
- Several recommendations depend on substantial engineering discipline and infrastructure work, which may be harder for larger legacy systems to adopt quickly.
- The piece argues strongly for typed languages and against Python in this context, but that recommendation is presented as opinionated guidance rather than a comparative study.

## Claims worth validating

- The claim that 100% coverage creates a qualitative “phase change” in leverage, compared with 95% or 99.99%, is a strong experience-based assertion that would benefit from broader validation.
- The claim that agents degrade significantly on large files because of summarization or truncation risk is plausible, but the article does not quantify how often this materially affects outcomes.
- The team’s reported setup of 10,000+ assertions finishing in about a minute, versus 20 to 30 minutes without caching, is a concrete operational claim but only for this specific environment.
- The stronger language that teams struggling with agentic coding are often seeing AI “amplify” their codebase’s worst tendencies is a useful hypothesis, but not demonstrated systematically here.
- The argument that TypeScript is categorically better suited than Python for agentic coding is presented forcefully but without controlled evidence in the post.

## Notes (your interpretation, clearly labeled)

- This is one of the stronger repo sources on a recurring theme: AI coding systems increase the payoff of software engineering discipline rather than making discipline optional.
- It pairs well with the Boris Tane and Jim Yagmin pieces. Tane emphasizes process control around agents, Yagmin focuses on context architecture, and Krenzel focuses on codebase shape and guardrails.
- The article is also notable for reframing “best practices” as machine-compatibility infrastructure. In that framing, tests, types, naming, and environment automation are not just for humans maintaining code later; they are part of making autonomous coding viable now.

## Source

- https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code?utm_source=tldrdev
