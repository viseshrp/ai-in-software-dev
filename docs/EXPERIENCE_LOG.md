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

## 2026-02-24 — Codex Feels Best For Long-Running Refactors And Rewrites

Codex seems far superior (in my experience) for long-running refactors/rewrites/implementations that require sustained coherence over time.

One concrete example: I tried adding static types to an entire codebase. Copilot failed. Gemini became hacky and the approach deteriorated over time. Claude ran out of credits. Codex shined on this kind of long-running, repo-wide change.

## 2026-03-02 — I Prefer My Own Markdown Plans Over Built-In Plan Mode

I use my own `.md` plan files rather than Claude Code’s or Codex's built-in plan mode. The built-in plan mode sucks. My markdown file gives me full control.

I can edit it in my editor, add inline notes, and it persists as a real artifact in the project.

This is fundamentally different from trying to steer implementation through chat messages. The plan is a structured, complete specification I can review holistically. A chat conversation is something I’d have to scroll through to reconstruct decisions. The plan wins every time.

Copilot is excellent at understanding code, proposing solutions, and writing implementations. But it doesn’t know my product priorities, my users’ pain points, or the engineering trade-offs I’m willing to make. The annotation cycle is how I inject that judgement.

The creative work happened in the annotation cycles in plan mode. That’s where humans use our brains. By the time I say “implement it all,” every decision has been made and validated. The implementation becomes mechanical, not creative. This is deliberate.

You can ask it to split work into phases and then make a todo list for each phase, plus a global todo list as well. It usually does this by itself.

I also add a detailed todo list to the plan, with all the phases and individual tasks necessary to complete the plan — don’t implement yet.

This creates a checklist that serves as a progress tracker during implementation. Claude marks items as completed as it goes, so I can glance at the plan at any point and see exactly where things stand. Especially valuable in sessions that run for hours.

Where a planning note might be a paragraph, an implementation correction is often a single sentence:

“You didn’t implement the `deduplicateByTitle` function.”
“You built the settings page in the main app when it should be in the admin app, move it.”

Claude has the full context of the plan and the ongoing session, so terse corrections are enough.

Frontend work is the most iterative part. I test in the browser and fire off rapid corrections:

“wider”
“still cropped”
“there’s a 2px gap”

For visual issues, I sometimes attach screenshots. A screenshot of a misaligned table communicates the problem faster than describing it.

If there are UI changes, sometimes I give it instructions to start up the app and ask it to take screenshots and see for itself what the problem is with the UI, which can be hard to explain.

I also reference existing code constantly:

“this table should look exactly like the users table, same header, same pagination, same row density.”

## 2026-03-02 — For Contained Features, Sharing A Reference Implementation Helps

For well-contained features where I’ve already seen a good implementation in an open source repo, I’ll share that code as a reference alongside the plan request.

Claude works dramatically better when it has a concrete reference implementation to work from rather than designing from scratch.

## 2026-03-02 — After Planning, Choose Whether The Agent Stops Per Phase Or Runs To Completion

When done with planning, you can either ask it to stop after a phase and let yourself review, or ask it to not stop until all tasks and phases are completed.

The former makes a PR review easier.

You can also ask it to run the entire lint/test suite after every phase.
