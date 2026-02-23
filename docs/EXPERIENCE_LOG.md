# Experience Log

First-person notes from working with AI tools/agents while building software. These entries may later be distilled into synthesis docs once enough patterns accumulate.

## 2026-02-23 — Agents Fix The Bug, Then Improve The System

When I ask an agent (especially Codex) to fix a bug, it often re-evaluates the surrounding implementation and makes additional improvements so the same class of bug is less likely to recur, after it applies the direct fix. This feels similar to how a careful human would fix the immediate issue and then harden the design to prevent repeat failures.

## 2026-02-23 — (From seed context) Agents Trend Toward Safer Refactors

In my experience, agents don’t just patch a line: they can map legacy code, summarize dependencies, propose safer refactors, add tests before changing behavior, and keep multi-file changes (types/imports) consistent. This changes how “tech debt work” feels day-to-day, because the agent can help reduce the risk of the next similar bug as part of the same pass.

## 2026-02-23 — (From seed context) Debug Loops Become Tighter And More Mechanical

Agents can run the test suite, debug failing tests, and iterate until tests pass. Practically, this makes the fix cycle feel more like a tight, mechanical loop where the agent can keep pushing forward until the system is green again.

## 2026-02-23 — (From seed context) CI/CD Failure Modes Become Less Blocking

CI/CD and YAML/bash glue work becomes less of a blocker because agents can debug pipeline failures and accelerate config iteration. This reduces the “friction tax” that often turns small fixes into multi-hour distractions.

## 2026-02-23 — Context Offloading To Disk Makes Agents Work Better

Agents work best when important context is offloaded from their chat memory into files on disk (specs, constraints, decisions, checklists, notes). The agent can then read and update those files as part of the workflow, and you can even use the agent itself to write and maintain the context artifacts it needs to operate effectively.
