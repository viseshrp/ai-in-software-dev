---
title: "Things I've done with AI"
author: "Jerred Shepherd"
published: "2026-03-09" # YYYY-MM-DD if known
captured: "2026-03-13"  # YYYY-MM-DD (when you summarized it)
source_url: "https://sjer.red/blog/2026/built-with-ai/"
source_domain: "sjer.red"
---

# Things I've done with AI

## Core ideas (structured)

- The article is a first-person account of an experienced programmer changing his view of AI coding tools from skepticism to heavy daily use across both personal and professional work.
- Shepherd says the main shift was reframing what matters in software work: for problem-solving contexts, code does not need to be “beautiful,” but it does need to work, and tests, types, and static analysis remain useful for both humans and LLMs.
- He argues that if testing is strong enough, even code that would traditionally be considered messy or substandard can still be workable because LLMs can continue operating on it.
- The author reports that since October 2025 he has not manually written code for work or personal projects, and instead has worked through prompts plus extensive review of model output.
- The article supports that claim with a long list of personal projects and migrations completed with Cursor and Claude Code, ranging from CI migrations and monorepo moves to new apps, bots, developer tools, and package development.
- On the work side, the piece says AI is now used for design documents, bespoke investigation and analysis tools, operational automation, and fast implementation of small feature requests or bug fixes.
- The closing argument is that these tools create enormous leverage for builders, but they also shift the bottleneck toward testing, documentation accuracy, developer experience, and overall engineering workflow.

## What seems to work (per the author)

- Using Cursor and Claude Code heavily across both infrastructure work and feature development appears, in the author’s experience, to unlock a large increase in output volume.
- Types and static analysis still seem valuable in an AI-heavy workflow, and may even help LLMs more than humans by constraining errors and clarifying structure.
- Reviewing AI output instead of writing code directly is presented as a workable operating mode for both hobby and professional projects.
- AI seems especially effective for conceptually straightforward but time-consuming engineering work such as migrations, internal tools, utility programs, and small product requests.
- Generating complex design docs, investigative tools, and operational automations at work is presented as a high-leverage use of these systems.

## Limitations / risks (per the author)

- The author says adopting AI required a fundamental mindset shift and that initial concerns about loss of control, code quality, and architecture were real.
- The article notes that work adoption is tiring and still creates significant problems around testing, developer experience, and velocity.
- For personal projects, the author says testing and documentation have become the bottleneck because someone still has to verify that output is correct and that generated docs are truthful.
- The article is experience-based and does not claim that all code can safely ignore maintainability concerns in every context.

## Claims worth validating

- The claim that the author has not written code manually since October 2025, and has operated instead through prompts plus review, is a striking personal workflow claim.
- The statement that code no longer needs to be maintainable “in the traditional sense” if tests are sufficient is a strong position that likely depends heavily on project type and test quality.
- The claim that small requests from PMs or users are now “essentially free” to implement, with review and manual testing as the main remaining work, is directionally plausible but not quantified here.
- The broader implication that LLMs can successfully operate on “bad” code as long as tests are good should be treated as an interesting hypothesis rather than settled evidence.

## Notes (your interpretation, clearly labeled)

- This source is useful because it is less of a theory piece and more of a lived-experience inventory: it shows what one technically ambitious developer actually chose to build once AI reduced implementation friction.
- It complements the Simon Willison and Steve Krenzel pieces. Those argue that code economics and quality practices are changing; this article shows that shift playing out in a concrete project portfolio.
- It also sharpens a recurring repo theme: AI may not remove the need for engineering rigor, but it can move the bottleneck toward testing, truthful documentation, and review while dramatically increasing the number of projects one person can attempt.

## Source

- https://sjer.red/blog/2026/built-with-ai/
