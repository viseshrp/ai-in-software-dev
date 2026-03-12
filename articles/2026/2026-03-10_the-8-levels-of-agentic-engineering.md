---
title: "The 8 Levels of Agentic Engineering"
author: "Bassim Eledath"
published: "2026-03-10" # YYYY-MM-DD if known
captured: "2026-03-12"  # YYYY-MM-DD (when you summarized it)
source_url: "https://www.bassimeledath.com/blog/levels-of-agentic-engineering?utm_source=tldrdev"
source_domain: "www.bassimeledath.com"
---

# The 8 Levels of Agentic Engineering

## Core ideas (structured)

- The author argues that the main bottleneck in AI-assisted software development is no longer raw model capability alone, but teams’ ability to use that capability effectively.
- He presents an eight-level progression for “agentic engineering,” framed as an imperfectly sequential maturity model for how individuals and teams work with coding agents.
- Levels 1 and 2 cover the familiar starting point: tab-complete tools and chat-enabled agent IDEs, often paired with explicit plan mode for human control.
- Level 3 is context engineering: improving the information density, timing, and relevance of what the model sees, including rules files, tool descriptions, and conversation management.
- Level 4 is compounding engineering: a loop of plan, delegate, assess, and codify, where lessons from one session are written into durable context such as `CLAUDE.md` or structured docs so future sessions improve.
- Level 5 is capability expansion through MCPs and skills, giving the model access to external systems, specialized review flows, and reusable team knowledge.
- Level 6 is harness engineering plus automated feedback loops: equipping agents with tooling, observability, tests, and other forms of “backpressure” so they can validate and correct work without constant human intervention.
- Level 7 is background agents: asynchronous agents that can plan, execute, and iterate without a human in the chair, often with orchestrators, specialized models, and CI-triggered automation.
- Level 8 is autonomous agent teams: multiple agents coordinating directly with one another on shared work, which the author treats as an active frontier rather than a solved practice.
- Across the model, the author’s main point is that later-stage leverage depends on building clean context, strong constraints, reliable tools, and automated feedback before adding more autonomy.

## What seems to work (per the author)

- Using plan mode is described as a solid entry point at earlier levels, especially while practitioners are still learning how to scope and constrain tasks.
- Maintaining concise rules files and discoverable documentation helps the model recover useful context without overloading prompts.
- Codifying hard-won lessons into shared artifacts makes AI-assisted work compound across sessions instead of resetting each time.
- Shared skills and MCP-enabled tools can turn one-off workflows into reusable team capabilities, such as PR review routines that launch specialized subagents.
- Harnesses that expose tests, logs, browser tooling, and validation loops let agents verify their own work and iterate more reliably.
- Constraints and automated feedback are presented as more effective than detailed step-by-step prompting once teams move beyond beginner use.
- Background-agent setups benefit from orchestration: different models can be assigned different roles, and reviewer models should be separated from implementer models to reduce biased self-evaluation.
- CI-triggered AI jobs such as docs updates, dependency upgrades, or security review are presented as a strong use case once the surrounding context and feedback loops are mature.

## Limitations / risks (per the author)

- Teams at different “levels” can create coordination drag; a more advanced practitioner can still be bottlenecked by teammates or repo processes that remain earlier-stage.
- Noisy context, weak prompts, poor tool descriptions, or missing feedback loops do not merely reduce quality; at higher autonomy levels they amplify failure.
- Overloading rules files with too many instructions can backfire, making the model less effective rather than more reliable.
- Human review can become the bottleneck as agent-generated PR volume rises, which creates pressure to automate review without necessarily solving all quality risks.
- Fire-and-forget background-agent patterns can fail badly when product requirements or task descriptions are underspecified.
- The author says multi-agent coordination is still hard and immature; current systems can churn, break existing functionality, or require hierarchy and CI safeguards to make progress.
- He explicitly argues that Level 8 autonomy is not yet ready or economical for most day-to-day work, even if it may become important later.

## Claims worth validating

- The claim that each higher level produces a “huge leap in output” is plausible but not quantified in the article.
- The claim that plan mode as a separate human review step is fading may be directionally true for some teams, but it is presented here as a judgment call rather than a measured trend.
- The claim that code review “as we know it is dead” is attributed to an external argument and should be treated as provocative rather than settled.
- The examples of Anthropic and Cursor using large parallel-agent systems are useful signals, but they do not by themselves establish that multi-agent operation is broadly effective or economical.

## Notes (your interpretation, clearly labeled)

- This is one of the more directly useful articles in the repo because it offers a concrete maturity model that can organize many of the recurring themes already appearing across other sources.
- It maps cleanly onto several patterns already captured here: context quality, durable docs and rules, planner/executor separation, automated validation, background execution, and reviewer/implementer separation.
- It is also useful as synthesis material rather than just source capture: the “levels” framing could become a helpful lens for grouping other articles, experience notes, and future observations without freezing the repo into a rigid taxonomy too early.

## Source

- https://www.bassimeledath.com/blog/levels-of-agentic-engineering?utm_source=tldrdev
