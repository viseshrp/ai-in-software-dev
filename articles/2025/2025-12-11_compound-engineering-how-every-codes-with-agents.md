---
title: "Compound Engineering: How Every Codes With Agents"
author: "Dan Shipper and Kieran Klaassen"
published: "2025-12-11" # YYYY-MM-DD if known
captured: "2026-03-13"  # YYYY-MM-DD (when you summarized it)
source_url: "https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents"
source_domain: "every.to"
---

# Compound Engineering: How Every Codes With Agents

## Core ideas (structured)

- The article argues that if coding agents write nearly all of a team’s code, the core engineering problem shifts from manual implementation toward designing a system that makes each cycle of development improve the next one.
- Shipper and Klaassen call this system “compound engineering,” contrasting it with traditional engineering where each additional feature often makes future work harder because complexity accumulates faster than shared understanding.
- In their framing, compound engineering makes future work easier by capturing bugs, failed tests, and problem-solving insights so that later agents can reuse them.
- The piece presents a four-step loop: `Plan`, `Work`, `Assess`, and `Compound`.
- In `Plan`, agents research the codebase, commit history, and external best practices, then produce a detailed implementation plan with architecture, sources, and success criteria.
- In `Work`, agents execute against that plan, often using tools such as Playwright or XcodeBuildMCP to interact with products while building them.
- In `Assess`, both humans and agents review the result using tests, linters, manual checks, and parallel review agents that inspect the code from different perspectives.
- In `Compound`, lessons from earlier stages are recorded back into prompts, plugins, or codebase-local guidance so the next run starts smarter than the last one.
- The article presents this loop as the reason a single person can primarily build and run each of Every’s internal products, despite those products serving real users and workflows.

## What seems to work (per the author)

- Investing heavily in planning seems to work well in an environment where agents do the implementation, because a strong plan makes downstream output much closer to what the developer intends.
- Running agents in parallel across planning, coding, and review tasks is presented as a major productivity lever.
- Storing plans as durable artifacts, such as local files or GitHub issues, is presented as useful for creating a shared mental model between the engineer and the agent.
- Using MCP-style tools so the agent can interact with the application while building it is presented as especially effective for design and workflow-heavy work.
- Combining conventional checks like tests and linters with AI review agents is presented as a stronger assessment strategy than relying on either one alone.
- Automatically summarizing code review comments and folding them back into prompts or plugins is presented as the mechanism that turns isolated fixes into team-wide system improvements.

## Limitations / risks (per the author)

- The authors acknowledge that the article is only a high-level overview and does not fully address persistent constraints such as deciding what to build, refining plans, or clearly specifying what “good” looks like.
- The approach appears to rely on strong review discipline; even with better models, the article still emphasizes human and automated assessment before accepting output.
- Several claims are experience-based and tied to Every’s internal setup, tools, and codebases rather than established as generally proven across organizations.
- Some claims about traditional practices becoming unnecessary are stated provocatively and may not generalize cleanly to safety-critical, highly regulated, or poorly-instrumented environments.

## Claims worth validating

- The claim that nobody at Every is writing code manually is a striking organizational claim and should be treated as specific to their reported practice at the time of writing.
- The claim that a single developer can do the work of five developers from a few years ago, if AI is used well, is an important productivity assertion but is not backed here by a formal methodology.
- The statement that roughly 80 percent of compound engineering is in planning and review, versus 20 percent in work and compounding, is useful as a heuristic but appears to be based on internal experience.
- The article’s stronger forecast that manually writing tests, writing human-readable code with lots of documentation, and lengthy onboarding or replatforming costs become unnecessary should be treated as directional rather than settled.

## Notes (your interpretation, clearly labeled)

- This is a central source for the repo because it gives a concrete name and workflow for one of the strongest recurring patterns across many other articles: agentic software work shifts value from typing code toward planning, review, and systematized learning.
- It connects directly to the Simon Willison chapters added earlier. Willison argues that code is cheap and quality must improve; this article offers one operational answer for how a team can organize around that new reality.
- It also complements Boris Tane’s workflow article. Tane describes an individual operating style for controlling an agent; Every describes a broader team process that turns repeated agent use into organizational memory.

## Source

- https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents
