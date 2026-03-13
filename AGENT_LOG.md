# AGENT_LOG

This is a running log of work performed in this repository so future agents can see what was processed and why.

## 2026-02-23 — Seed + logging requirements wired in

- What I did: Read [`SEED.md`](SEED.md) and updated agent instructions to treat it as non-authoritative seed context.
- Files created/modified:
  - Modified: [`AGENTS.md`](AGENTS.md)
  - Created: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made:
  - Added explicit “seed is not source of truth” guidance so future work can evolve structure without anchoring on the brain dump.
  - Added mandatory logging checklist to reduce repeated work and capture assumptions/ambiguities.
- Assumptions:
  - The seed file is named [`SEED.md`](SEED.md) in this repo (user referenced `seed.md`), but the intent is the same seed document.
- Commands run:
  - `ls -la`
  - `nl -ba SEED.md | sed -n '1,240p'`
  - `nl -ba AGENTS.md | sed -n '1,200p'`
  - `nl -ba docs/PROJECT_PROMPT.md | sed -n '1,60p'`
- Test results: N/A (doc-only changes).
- Open questions:
  - Should we distill [`SEED.md`](SEED.md) into a smaller “working outline” doc (separate from article summaries) to guide early capture?
  - Do you prefer the seed file to be renamed to `seed.md` for consistency, or keep [`SEED.md`](SEED.md) as-is?
  - [`SEED.md`](SEED.md) is currently untracked in git (`git status` shows it as `??`); should it be added to version control?

## 2026-02-23 — Seed distillation map added

- What I did: Created a lightweight mapping doc that turns seed themes into actionable capture questions without freezing structure.
- Files created/modified:
  - Created: [`docs/SEED_MAP.md`](docs/SEED_MAP.md)
  - Modified: [`AGENTS.md`](AGENTS.md)
- Decisions made:
  - Kept [`SEED.md`](SEED.md) intact; added a separate “map” doc so we can evolve structure incrementally.
- Assumptions:
  - The themes listed are intended as guidance and will be revised as external sources are captured.
- Commands run:
  - `rg -n '^#' SEED.md | head -n 80`
  - `nl -ba SEED.md | sed -n '220,520p'`
- Test results: N/A (doc-only changes).
- Open questions:
  - Do you want the “claims to validate” list extracted now (verbatim phrasing), or wait until the first batch of external sources is captured?

## 2026-02-23 — Seed file decision

- Decision: Keep the filename as [`SEED.md`](SEED.md) (uppercase) and treat it as a repo-tracked artifact going forward.
- Why:
  - It’s already present with that name, and uppercase makes it prominent as “seed context”.
  - Tracking it in git preserves the initial baseline for future refinement and prevents drift/forgetting.
- Commands run:
  - `git add SEED.md AGENTS.md AGENT_LOG.md docs/SEED_MAP.md`

## 2026-02-23 — Reposition docs: research first, slides optional

- What I did: Updated repo documentation to emphasize the primary purpose as research/synthesis and treat slides as a secondary derivative output.
- Files modified:
  - [`README.md`](README.md)
  - [`AGENTS.md`](AGENTS.md)
  - [`docs/PROJECT_PROMPT.md`](docs/PROJECT_PROMPT.md)
  - [`docs/SYNTHESIS_GUIDE.md`](docs/SYNTHESIS_GUIDE.md)
  - [`SEED.md`](SEED.md)
- Summary of changes:
  - Removed “slide deck project” framing from the project plan title; reframed slide generation as an optional derivative artifact.
  - Added a consistent one-line statement in key entrypoints that research/synthesis is the primary goal and slides are optional.
  - Added a short note at the top of [`SEED.md`](SEED.md) to prevent readers from treating seed content as authoritative.
- Rationale (wording decisions):
  - Kept “field report” language but made the primary/secondary outputs explicit to avoid misreading the repo as a deck-building effort.
  - Avoided broad rewrites; made small, local edits to reduce churn and keep diffs reviewable.
- Ambiguities / gaps:
  - The task referenced `OUTLINE.md`, `SLIDES_SKELETON.md`, `TODO.md`, etc.; these files do not exist in the repo at this time.
- Commands run:
  - `rg -n "slide|deck|presentation" -S .`
  - `git diff --stat`
  - `git add -A`
- Test results: N/A.

## 2026-02-23 — Convert doc references to relative links

- What I did: Converted doc-to-doc file references from absolute filesystem paths to relative markdown links for GitHub-friendly navigation.
- Files modified:
  - [`README.md`](README.md)
  - [`AGENTS.md`](AGENTS.md)
  - [`AGENT_LOG.md`](AGENT_LOG.md)
  - [`CONTRIBUTING.md`](CONTRIBUTING.md)
  - [`docs/SEED_MAP.md`](docs/SEED_MAP.md)
  - [`articles/README.md`](articles/README.md)
- Decisions made:
  - Kept commands as code (no linking inside command snippets); only converted cross-document references.
- Commands run:
  - `rg -n "/Users/|\\.md:1" -S .`

## 2026-03-01 — Summarize external article: Mia Heidenstedt on writing quality code with AI

- What I did: Read the article at `https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/?utm_source=hackernewsletter&utm_medium=email&utm_term=code`, created a new article summary, and captured the main workflow recommendations plus unsupported-but-important claims.
- Files created/modified:
  - Created: [`articles/2026/2026-02-06_how-to-effectively-write-quality-code-with-ai.md`](articles/2026/2026-02-06_how-to-effectively-write-quality-code-with-ai.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Kept the summary operational and concrete because the article is structured as 12 practical recommendations rather than a narrative essay.
  - Put test-cheating, prompt-local context, and complexity-cost language into "Claims worth validating" because the article argues for them strongly without providing empirical evidence.
  - Kept the notes section short and interpretive, limited to how the article maps to this repo's research themes.
- Assumptions:
  - Used the article's publication date (`2026-02-06`) from the page metadata and `2026-03-01` as the capture date.
  - Preserved the user-provided URL, including UTM parameters, as the `source_url`.
- Commands run (if any):
  - `find articles -maxdepth 2 -type f | sort`
  - `nl -ba docs/SUMMARY_GUIDE.md | sed -n '1,200p'`
  - `nl -ba templates/article-summary.md | sed -n '1,200p'`
  - `python3 scripts/new_article.py --title "How to effectively write quality code with AI" --url "https://heidenstedt.org/posts/2026/how-to-effectively-write-quality-code-with-ai/?utm_source=hackernewsletter&utm_medium=email&utm_term=code" --author "Mia Heidenstedt" --published 2026-02-06 --captured 2026-03-01`
  - `nl -ba articles/2026/2026-02-06_how-to-effectively-write-quality-code-with-ai.md | sed -n '1,220p'`
  - `python3 scripts/build_index.py`
- Test results (if relevant):
  - N/A (content addition only).
- Open questions / ambiguities:
  - For future article captures, do you want `source_url` normalized to the canonical URL without tracking parameters, or should we continue preserving the exact input URL for provenance?

## 2026-03-01 — Summarize external article: Hellerstein on coding agents and distributed systems

- What I did: Read the article at `https://jhellerstein.github.io/blog/codegen-reality/?utm_source=tldrnewsletter`, created a structured summary, and captured the central thesis about aiming AI code generation at languages/frameworks that make distributed contracts explicit and constrain nondeterminism.
- Files created/modified:
  - Created: [`articles/2026/2026-02-11_coding-agents-meet-distributed-reality.md`](articles/2026/2026-02-11_coding-agents-meet-distributed-reality.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Treated Hydro as an example rather than a conclusion; summarized the argument without endorsing Hydro’s claims beyond what the author states.
  - Put “AI will write most code” and “eliminates whole classes of bugs” into “Claims worth validating” since this post argues them without presenting data.
- Assumptions:
  - Publication date taken from the post metadata (“February 11, 2026”) and recorded as `2026-02-11`.
  - Preserved the user-provided URL (including UTM) as `source_url`.
- Commands run (if any):
  - `curl -L --silent --show-error --fail -o /tmp/codegen-reality.html "https://jhellerstein.github.io/blog/codegen-reality/?utm_source=tldrnewsletter"`
  - `curl -L --show-error --fail "https://jhellerstein.github.io/blog/page-data/codegen-reality/page-data.json" -o /tmp/codegen-reality.page-data.json`
  - `python3 scripts/new_article.py --title "Coding Agents Meet Distributed Reality" --url "https://jhellerstein.github.io/blog/codegen-reality/?utm_source=tldrnewsletter" --author "Joseph M. Hellerstein" --published 2026-02-11 --captured 2026-03-01`
  - `python3 scripts/build_index.py`
- Test results (if relevant):
  - N/A (content addition only).

## 2026-03-01 — Summarize external article: Boris Tane on using Claude Code

- What I did: Read the article at `https://boristane.com/blog/how-i-use-claude-code/?utm_source=tldrnewsletter`, created a structured summary of the research-plan-annotate-implement workflow, and captured the key control mechanisms (written artifacts, plan gating, scope cuts, revert-and-rescope).
- Files created/modified:
  - Created: [`articles/2026/2026-02-10_how-i-use-claude-code.md`](articles/2026/2026-02-10_how-i-use-claude-code.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Treated token savings and “single long sessions don’t degrade” as claims worth validating, since the article presents them as experience-based.
  - Focused the “what works” section on the mechanics (artifacts, gating, reference-based feedback, revert behavior) rather than the specific prompt wording.
- Assumptions:
  - Publication date taken from JSON-LD `datePublished` (`2026-02-10T08:00:00.000Z`) and recorded as `2026-02-10`.
  - Preserved the user-provided URL (including UTM) as `source_url`.
- Commands run (if any):
  - `curl -L --show-error --fail "https://boristane.com/blog/how-i-use-claude-code/?utm_source=tldrnewsletter" -o /tmp/how-i-use-claude-code.html`
  - `python3 scripts/new_article.py --title "How I Use Claude Code" --url "https://boristane.com/blog/how-i-use-claude-code/?utm_source=tldrnewsletter" --author "Boris Tane" --published 2026-02-10 --captured 2026-03-01`
  - `python3 scripts/build_index.py`
- Test results (if relevant):
  - N/A (content addition only).

## 2026-02-23 — Repo docs read + experience-capture operating mode

- What I did: Read all markdown docs currently in-repo to establish operating context, then aligned on a standing workflow: you provide experience entries and I place them in the most appropriate repo location.
- Files created/modified:
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Use doc intent to route new content:
    - Experience tied to an external source/article goes in `articles/<year>/...` using the summary template and required `source_url`.
    - Cross-source patterns and framework changes go in `docs/` synthesis/process docs.
    - Session-level traceability and operational notes go in [`AGENT_LOG.md`](AGENT_LOG.md).
  - Keep updates incremental and commit-friendly to preserve reviewability and historical traceability.
- Assumptions:
  - “Read all the docs” refers to all tracked markdown docs currently present in this repository.
  - Future “experience” entries may be either source-backed observations or first-person workflow notes; placement will depend on which type you provide.
- Commands run (if any):
  - `pwd && rg --files -g '*.md'`
  - `ls -la`
  - `cat AGENTS.md`
  - `cat README.md`
  - `cat CONTRIBUTING.md`
  - `cat INDEX.md`
  - `cat docs/PROJECT_PROMPT.md`
  - `cat docs/SUMMARY_GUIDE.md`
  - `cat docs/SYNTHESIS_GUIDE.md`
  - `cat docs/SEED_MAP.md`
  - `cat SEED.md`
  - `cat AGENT_LOG.md`
  - `cat articles/README.md`
  - `cat templates/article-summary.md`
- Test results (if relevant):
  - N/A (documentation read/log update only).
- Open questions / ambiguities:
  - For pure first-person experience entries without external sources, should the primary long-form home be `docs/` (new dedicated experience log) or remain only in [`AGENT_LOG.md`](AGENT_LOG.md) plus occasional synthesis updates?
- Areas needing clarification:
  - Preferred granularity for each experience entry (quick bullet vs structured mini-report).
- Improvements to your own workflow:
  - Continue logging each processing session immediately after context-read or content-write to keep assumptions and routing decisions explicit.

## 2026-02-23 — Experience entry: agents harden after bugfix

- What I did: Captured a first-person experience note about agent behavior during bug fixing (fix + preventative improvements).
- Files created/modified:
  - Created: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Placed first-person experiences in `docs/` (not `articles/`) since they are not external sources and do not have a `source_url`.
  - Used a dated entry format so later synthesis can reference stable timestamps.
- Assumptions:
  - These first-person entries may be distilled later into synthesis docs once patterns accumulate.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A
- Open questions / ambiguities:
  - Should experience entries also include minimal context fields (tool, repo type, language, failure mode) to improve later synthesis?
- Areas needing clarification:
  - None.
- Improvements to your own workflow:
  - Keep experience notes concise and dated; add context fields only when they materially help retrieval.

## 2026-02-23 — Distill similar experiences from seed into experience log

- What I did: Scanned [`SEED.md`](SEED.md) for experience-style observations similar to “bugfix plus hardening” and distilled them into additional entries in the experience log.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Marked entries as “From seed context” to preserve provenance and avoid implying they came from external sources.
  - Kept the new entries short and adjacent to the original bugfix-hardening entry to keep the log scannable.
- Assumptions:
  - Seed content reflects prior first-person experience and is acceptable to distill into the experience log as long as provenance is labeled.
- Commands run (if any):
  - `rg -n "bug|debug|fix|refactor|safe refactor|adds tests|harden|prevent|failure|risk|iterate|tests pass|tech debt|liquid|self-improving|document" SEED.md`
  - `nl -ba SEED.md | sed -n '60,120p'`
  - `nl -ba SEED.md | sed -n '240,340p'`
- Test results (if relevant):
  - N/A (docs-only changes).
- Open questions / ambiguities:
  - If the experience log grows, do you want a lightweight tag line per entry (e.g., `tags: bugfix, refactor, ci`) for later synthesis?

## 2026-02-23 — Experience entry: offload context to disk (agent-written artifacts)

- What I did: Captured a first-person experience note that agents work better when context is stored in repo files (specs/notes/decisions) that the agent can read and update, including using the agent to author those context files.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Kept this as an experience entry (not synthesis) since it’s a direct workflow observation rather than a cross-source claim.
- Assumptions:
  - “Context offloading” refers to storing durable project constraints and decisions in files on disk rather than relying on chat-only memory.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A

## 2026-02-24 — Experience entry: Codex for long-running refactors (typing migration example)

- What I did: Captured a first-person comparative note that Codex performs better (for you) on long-running refactors/rewrites/implementations, with an example of attempting to add static types across an entire codebase (Copilot failed, Gemini degraded, Claude hit credits, Codex succeeded).
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Kept it as an experience entry with a concrete example to preserve “what happened” rather than turning it into a generalized claim.
- Assumptions:
  - “Static types across an entire codebase” refers to a repo-wide migration (e.g., adding type annotations and fixing downstream errors) rather than a single-file change.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A

## 2026-03-02 — Experience entry: prefer repo markdown plans over built-in plan mode

- What I did: Added a first-person experience note that I prefer maintaining my own Markdown planning files in-repo rather than using Claude Code/Codex built-in plan mode.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Captured it as an experience entry (not synthesis) because it’s a personal workflow preference rather than a multi-source claim.
  - Kept the wording direct to preserve the original sentiment and rationale (editor control, inline notes, durable artifact).
- Assumptions:
  - “Built-in plan mode” refers to tool-specific UI planning features, distinct from keeping a persistent `.md` file in the repo.
- Commands run (if any):
  - `ls`
  - `rg -n "experience log" -S .`
  - `rg -n "EXPERIENCE" -S .`
  - `find docs -maxdepth 2 -name AGENTS.md -print`
  - `sed -n '1,200p' docs/EXPERIENCE_LOG.md`
  - `tail -n 80 AGENT_LOG.md`
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: why repo plans beat chat steering

- What I did: Edited the existing “prefer repo markdown plans” experience entry to add a clarification: a plan file is a holistic, structured spec that’s easier to review than reconstructing decisions from a long chat scrollback.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended to the existing plan-mode entry (rather than creating a new standalone entry) because it’s a direct elaboration of the same preference and rationale.
- Assumptions:
  - “Steer implementation through chat messages” refers to incrementally guiding design/decisions via conversational context rather than a single durable spec artifact.
- Commands run (if any):
  - `rg -n "Prefer My Own Markdown Plans" -n docs/EXPERIENCE_LOG.md`
  - `rg -n "prefer repo markdown plans" AGENT_LOG.md`
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: annotation cycle injects product judgement

- What I did: Edited the existing plan-mode experience entry to add a note about why a plan + annotation cycle matters: Copilot can write solid code, but the human uses annotations to inject product priorities, user pain points, and acceptable engineering trade-offs.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended to the same plan-mode entry because it reinforces the “plan as spec” theme by explaining how judgement enters the loop.
- Assumptions:
  - “Annotation cycle” refers to reviewing/editing the plan/spec (and/or PR feedback) to communicate non-obvious priorities and constraints back to the agent/tool.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: add phased todo list; defer implementation

- What I did: Edited the plan-mode experience entry to add a workflow pattern: I include a detailed, phased todo list with individual tasks, and explicitly defer implementation until after the plan is reviewed.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended to the same plan-mode entry because it’s part of the “plan as spec + review gate” workflow, not a separate theme.
- Assumptions:
  - “Don’t implement yet” is an explicit gating instruction to prevent premature coding before priorities/trade-offs are annotated.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: checklist plan as progress tracker

- What I did: Edited the plan-mode experience entry to add that the detailed todo list becomes a checklist/progress tracker during long implementation sessions, with Claude marking items complete as it goes.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended to the same plan-mode entry because it’s a direct benefit of the phased todo list pattern (visibility into progress during hours-long sessions).
- Assumptions:
  - “Claude marks items as completed” means the agent updates the Markdown checklist/plan file as part of the workflow.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience entry: choose phase-by-phase review vs run-to-completion

- What I did: Added a first-person experience note that after planning, I can explicitly choose whether the agent should stop after each phase for review or continue through all phases/tasks without stopping.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Captured as a new experience entry because it’s a distinct workflow control pattern (execution pacing) separate from “plan as spec” and “checklist tracking”.
- Assumptions:
  - “Stop after a phase” means pausing implementation at a defined milestone for human review/approval before continuing.
  - “Do not stop until all tasks and phases are completed” means the agent continues iterating until the full checklist is done (within practical time/tooling limits).
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: phase-by-phase helps PR review

- What I did: Edited the existing “phase-by-phase review vs run-to-completion” experience entry to add that stopping after each phase makes PR review easier.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended to the existing entry because it’s a direct clarification of the same execution pacing pattern.
- Assumptions:
  - “PR review” refers to reviewing smaller, phase-scoped diffs rather than a single large all-phases change.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: phases + per-phase todo lists (often automatic)

- What I did: Edited the plan-mode experience entry to add that you can ask the agent to split work into phases and generate both per-phase todo lists and a global todo list, and that it often does this automatically.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Added it before the “detailed todo list” paragraph to keep the experience flow: phase structure → todo lists → review gate → progress tracking.
- Assumptions:
  - “Usually does by itself” means the agent tends to naturally propose phased work breakdowns without being explicitly prompted, especially for larger tasks.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: creativity in annotation; implementation is mechanical

- What I did: Edited the plan-mode experience entry to add that the creative work happens in the annotation cycles (human judgement/decision-making), and that by the time I say “implement it all,” decisions are validated and implementation is intentionally mechanical.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Placed the note adjacent to the “annotation cycle” paragraph to preserve the causal link: annotations drive decisions; implementation executes them.
- Assumptions:
  - “Plan mode” here refers to the plan/spec + annotation loop, not a specific product feature requirement.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: terse implementation corrections and high-iteration frontend loops

- What I did: Edited the plan-mode experience entry to add that implementation feedback is often terse (single-sentence corrections) because Claude retains the plan + session context, and that frontend work tends to be highly iterative with rapid visual corrections and occasional screenshots.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Added it to the same plan-mode entry because it describes the downstream execution loop (plan-driven implementation + corrections), not a separate theme.
  - Preserved the short quoted examples to keep the “terse correction” pattern concrete.
- Assumptions:
  - “Attach screenshots” refers to providing images to communicate UI/layout issues faster than prose.
  - “Reference existing code constantly” includes pointing to canonical components/pages as UI/behavior baselines.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: ask agent to run app and screenshot UI issues

- What I did: Edited the plan-mode experience entry to add that for UI changes, I sometimes instruct the agent to start the app and take screenshots to observe UI problems directly when they’re hard to describe.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended near the existing screenshot paragraph to keep UI-iteration notes grouped together.
- Assumptions:
  - “Start up the app” means running the local dev server and navigating relevant screens (as feasible within tooling/session constraints).
  - “Take screenshots” can include automated screenshot tooling or manual capture provided back to the agent, depending on environment.
- Commands run (if any):
  - `git status --porcelain`
  - `git diff --stat`
  - `git diff -- INDEX.md`
  - `ls -l articles/2026/2026-02-10_how-i-use-claude-code.md`
  - `sed -n '1,80p' articles/2026/2026-02-10_how-i-use-claude-code.md`
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: run lint/tests after each phase

- What I did: Edited the “phase-by-phase review vs run-to-completion” experience entry to add that you can ask the agent to run the full lint/test suite after each phase.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended to the same phase-by-phase entry because it’s a concrete operationalization of “phase boundaries” (validation gates).
- Assumptions:
  - “Entire lint/test suite” means whatever the repo’s standard validation commands are (formatter/linter/unit tests/integration tests as applicable).
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience entry: share OSS reference implementations for contained features

- What I did: Added a first-person experience note that for well-contained features, sharing a known-good open source reference implementation alongside the plan request improves outcomes.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
- Decisions made (and why):
  - Captured it as an experience entry (not synthesis) because it’s a workflow tactic you apply when you already have a trusted reference.
  - Kept it narrowly scoped to “well-contained features” to avoid implying it’s always the best approach for ambiguous, exploratory work.
- Assumptions:
  - “Share that code” means linking or providing relevant excerpts as a reference (respecting licensing/attribution), not copying entire repos verbatim.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-02 — Experience edit: Claude benefits from concrete reference implementations

- What I did: Edited the existing “share OSS reference implementations” experience entry to add an explicit observation that Claude works dramatically better when given a concrete reference implementation rather than designing from scratch.
- Files created/modified:
  - Modified: [`docs/EXPERIENCE_LOG.md`](docs/EXPERIENCE_LOG.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
- Decisions made (and why):
  - Appended the Claude-specific note to the existing entry (instead of creating a new dated entry) because it’s a direct elaboration of the same workflow pattern.
- Assumptions:
  - “Concrete reference implementation” means code that is close enough in shape/constraints to be directly adapted, not a high-level description.
- Commands run (if any):
  - N/A
- Test results (if relevant):
  - N/A (docs-only change).
- Open questions / ambiguities:
  - None.

## 2026-03-10 — Summarize external article: lr0 on avoiding LLMs for research

- What I did: Read the blog post at `https://lr0.org/blog/p/gpt/?utm_source=tldrdev`, created a new article summary, and captured the post’s main argument that LLM-assisted information retrieval can erode the judgment-building value of doing research yourself.
- Files created/modified:
  - Created: [`articles/2026/2026-01-30_i-m-not-consulting-an-llm.md`](articles/2026/2026-01-30_i-m-not-consulting-an-llm.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Used `lr0` as the author field because the article page exposes no fuller personal byline and the site consistently identifies itself that way.
  - Kept the summary focused on epistemic and intellectual-development claims rather than trying to force a software-engineering workflow angle onto a broader essay.
  - Put the strongest assertions about LLM inadequacy and “intellect-rot” into “Claims worth validating” because the post is argumentative and experience-based rather than empirical.
- Assumptions:
  - Publication date taken from the page markup (`January 30, 2026`) and recorded as `2026-01-30`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `pwd && rg --files`
  - `sed -n '1,220p' AGENTS.md`
  - `sed -n '1,220p' docs/SUMMARY_GUIDE.md`
  - `sed -n '1,220p' CONTRIBUTING.md`
  - `sed -n '1,220p' INDEX.md`
  - `sed -n '1,220p' AGENT_LOG.md`
  - `curl -L --show-error --fail "https://lr0.org/blog/p/gpt/?utm_source=tldrdev" -o /tmp/lr0-gpt.html`
  - `sed -n '1,220p' /tmp/lr0-gpt.html`
  - `rg -n "author|published|date|og:|description|ld\\+json|<article|<main|<time|substack|title" /tmp/lr0-gpt.html`
  - `sed -n '1,220p' templates/article-summary.md`
  - `sed -n '1,220p' articles/2026/2026-02-10_how-i-use-claude-code.md`
  - `sed -n '1,220p' scripts/new_article.py`
  - `curl -L --show-error --fail "https://lr0.org/blog/h/rss/" -o /tmp/lr0-rss.xml`
  - `sed -n '1,220p' /tmp/lr0-rss.xml`
  - `curl -L --show-error --fail "https://lr0.org/" -o /tmp/lr0-home.html`
  - `rg -n "author|about|github|larrasket|lr0|La Vita Nouva" /tmp/lr0-home.html`
  - `python3 scripts/new_article.py --title "I'm not consulting an LLM" --url "https://lr0.org/blog/p/gpt/?utm_source=tldrdev" --author "lr0" --published 2026-01-30 --captured 2026-03-10`
  - `python3 scripts/build_index.py`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: Justin Jackson on Claude Code and team dynamics

- What I did: Read the article at `https://justinjackson.ca/claude-code-ruin?utm_source=tldrdev`, created a new article summary, and extracted the parts most relevant to this repo: role-boundary erosion, the shift toward judgment/accountability, generalist-vs-specialist hiring effects, and AI-mediated cross-functional collaboration.
- Files created/modified:
  - Created: [`articles/2026/2026-03-04_will-claude-code-ruin-our-team.md`](articles/2026/2026-03-04_will-claude-code-ruin-our-team.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Kept the summary centered on organizational and workflow implications rather than repeating every named example, because the post’s core value for this repo is its argument about team structure under AI.
  - Captured the Matt Stauffer example in “What seems to work” because it is the clearest concrete collaboration pattern in the article.
  - Put “generalists win” and similar forward-looking conclusions into “Claims worth validating” because the article relies on anecdotal input from founders/operators.
- Assumptions:
  - Publication date taken from the page (`Published on March 4th, 2026`) and recorded as `2026-03-04`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `sed -n '1,220p' templates/article-summary.md`
  - `tail -n 80 AGENT_LOG.md`
  - `git status --short`
  - `curl -L --show-error --fail "https://justinjackson.ca/claude-code-ruin?utm_source=tldrdev" -o /tmp/claude-code-ruin.html`
  - `ls /tmp | rg "claude-code-ruin|justin|jackson"`
  - `python3 - <<'PY' ... Path('/tmp').glob('*claude*') ... PY`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline" /tmp/claude-code-ruin.html`
  - `sed -n '1,260p' /tmp/claude-code-ruin.html`
  - `python3 scripts/new_article.py --title "Will Claude Code ruin our team?" --url "https://justinjackson.ca/claude-code-ruin?utm_source=tldrdev" --author "Justin Jackson" --published 2026-03-04 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: Kyle Corbitt on preparing for AI disruption

- What I did: Read the article at `https://corbt.com/posts/a-pocket-guide-to-surviving-the-robot-apocalypse`, created a new article summary, and extracted the elements most relevant to this repo: direct frontier-model capability calibration, implications for developer career resilience, and the broader framing of software automation as part of a larger knowledge-work shift.
- Files created/modified:
  - Created: [`articles/2026/2026-02-16_a-pocket-guide-to-surviving-the-robot-apocalypse.md`](articles/2026/2026-02-16_a-pocket-guide-to-surviving-the-robot-apocalypse.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Structured the summary around the author’s `learn / earn / return` framework because that is the article’s organizing idea.
  - Kept the notes section explicit that this is more of a career/adaptation essay than a development-workflow article, while still connecting it to this repo’s themes.
  - Flagged the health, taxes, and investing examples as risky/high-stakes use cases rather than treating them as straightforward best practices.
- Assumptions:
  - Publication date taken from the page (`February 16, 2026`) and recorded as `2026-02-16`.
  - Used the canonical page URL as `source_url`.
- Commands run (if any):
  - `curl -L --show-error --fail "https://corbt.com/posts/a-pocket-guide-to-surviving-the-robot-apocalypse" -o /tmp/robot-apocalypse.html`
  - `git status --short`
  - `tail -n 60 AGENT_LOG.md`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline|time datetime" /tmp/robot-apocalypse.html`
  - `sed -n '1,320p' /tmp/robot-apocalypse.html`
  - `python3 scripts/new_article.py --title "A Pocket Guide to Surviving the Robot Apocalypse" --url "https://corbt.com/posts/a-pocket-guide-to-surviving-the-robot-apocalypse" --author "Kyle Corbitt" --published 2026-02-16 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: Laurie Voss on AI-enabled companies and headcount

- What I did: Read the article at `https://seldo.com/posts/do-ai-enabled-companies-need-fewer-people/?utm_source=tldrai`, created a new article summary, and captured the core argument that startups, especially AI-native ones, appear to be scaling with fewer people while the expected offsetting wave of new tech jobs has not yet arrived.
- Files created/modified:
  - Created: [`articles/2026/2026-03-08_do-ai-enabled-companies-need-fewer-people.md`](articles/2026/2026-03-08_do-ai-enabled-companies-need-fewer-people.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Kept the summary focused on the post’s company- and market-level implications rather than reproducing every funding statistic, because the durable signal for this repo is the labor-vs-compute substitution argument.
  - Treated the cited metrics (40% smaller teams, 6x revenue per employee, smaller teams at $10M ARR) as “Claims worth validating” because the article relies on third-party source synthesis.
  - Connected the notes explicitly to adjacent repo themes: org design, hiring compression, and whether AI creates new demand fast enough to offset efficiency gains.
- Assumptions:
  - Publication date taken from the page (`March 8, 2026`) and recorded as `2026-03-08`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `curl -L --show-error --fail "https://seldo.com/posts/do-ai-enabled-companies-need-fewer-people/?utm_source=tldrai" -o /tmp/seldo-ai-fewer-people.html`
  - `git status --short`
  - `tail -n 60 AGENT_LOG.md`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline|time datetime|class=author|rel=author" /tmp/seldo-ai-fewer-people.html`
  - `sed -n '1,360p' /tmp/seldo-ai-fewer-people.html`
  - `python3 scripts/new_article.py --title "Do AI-enabled companies need fewer people?" --url "https://seldo.com/posts/do-ai-enabled-companies-need-fewer-people/?utm_source=tldrai" --author "Laurie Voss" --published 2026-03-08 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
  - `python3 -c "import os; p='scripts/__pycache__/build_index.cpython-314.pyc'; os.remove(p) if os.path.exists(p) else None"`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: Addie Foote on open weights versus open training

- What I did: Read the article at `https://www.workshoplabs.ai/blog/open-weights-open-training?utm_source=tldrai`, created a new article summary, and captured the core argument that open model weights do not automatically imply workable, affordable post-training infrastructure.
- Files created/modified:
  - Created: [`articles/2026/2026-03-09_open-weights-isn-t-open-training.md`](articles/2026/2026-03-09_open-weights-isn-t-open-training.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Focused the summary on the article’s main distinction between open weights and open training, rather than enumerating every debugging step in equal detail.
  - Kept the concrete failure modes in the summary because they are the evidence underlying the article’s broader claim about infrastructure debt.
  - Treated cost comparisons and broader generalizations about open-source ML infrastructure as “Claims worth validating” because they come from one detailed case study.
- Assumptions:
  - Publication date taken from the page (`March 9, 2026`) and recorded as `2026-03-09`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `git diff -- AGENT_LOG.md INDEX.md`
  - `curl -L --show-error --fail "https://www.workshoplabs.ai/blog/open-weights-open-training?utm_source=tldrai" -o /tmp/open-weights-open-training.html`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline|time datetime|<h1|<article|Workshop Labs|open weights|open training" /tmp/open-weights-open-training.html`
  - `sed -n '1,360p' /tmp/open-weights-open-training.html`
  - `python3 - <<'PY' ... text.find(...) ... PY`
  - `python3 scripts/new_article.py --title "Open Weights isn't Open Training" --url "https://www.workshoplabs.ai/blog/open-weights-open-training?utm_source=tldrai" --author "Addie Foote" --published 2026-03-09 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
  - `python3 -c "import os; p='scripts/__pycache__/build_index.cpython-314.pyc'; os.remove(p) if os.path.exists(p) else None"`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: Bassim Eledath on levels of agentic engineering

- What I did: Read the article at `https://www.bassimeledath.com/blog/levels-of-agentic-engineering?utm_source=tldrdev`, created a new article summary, and captured the post as a staged maturity model for AI-assisted software work, from tab complete through background agents and autonomous multi-agent teams.
- Files created/modified:
  - Created: [`articles/2026/2026-03-10_the-8-levels-of-agentic-engineering.md`](articles/2026/2026-03-10_the-8-levels-of-agentic-engineering.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Preserved the “levels” structure in the summary because it is the article’s main contribution and a potentially useful synthesis lens for this repo.
  - Focused the “what seems to work” section on operational patterns that recur across levels: codified context, shared skills, automated feedback, orchestration, and reviewer/implementer separation.
  - Treated the more forward-looking claims about plan mode fading and code review being replaced as “Claims worth validating” because the article argues from experience and examples rather than benchmarks.
- Assumptions:
  - Publication date taken from the page (`March 10, 2026`) and recorded as `2026-03-10`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `curl -L --show-error --fail "https://www.bassimeledath.com/blog/levels-of-agentic-engineering?utm_source=tldrdev" -o /tmp/levels-of-agentic-engineering.html`
  - `tail -n 40 AGENT_LOG.md`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline|time datetime|<h1|Agentic|Bassim|levels" /tmp/levels-of-agentic-engineering.html`
  - `sed -n '1,360p' /tmp/levels-of-agentic-engineering.html`
  - `python3 scripts/new_article.py --title "The 8 Levels of Agentic Engineering" --url "https://www.bassimeledath.com/blog/levels-of-agentic-engineering?utm_source=tldrdev" --author "Bassim Eledath" --published 2026-03-10 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
  - `python3 -c "import os; p='scripts/__pycache__/build_index.cpython-314.pyc'; os.remove(p) if os.path.exists(p) else None"`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: Vivek Trivedy on agent harnesses

- What I did: Read the article at `https://blog.langchain.com/the-anatomy-of-an-agent-harness/?utm_source=tldrai`, created a new article summary, and captured its main contribution: a system-level definition of an agent as `model + harness`, plus a derivation of the main harness primitives needed for useful autonomous work.
- Files created/modified:
  - Created: [`articles/2026/2026-03-10_the-anatomy-of-an-agent-harness.md`](articles/2026/2026-03-10_the-anatomy-of-an-agent-harness.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Used `Vivek Trivedy` as the author because the body explicitly says “By Vivek Trivedy” even though site metadata is attributed to `LangChain Accounts`.
  - Kept the summary organized around the article’s derived harness primitives rather than following the page section-by-section verbatim.
  - Treated leaderboard/performance comparisons as “Claims worth validating” because the post references external evidence rather than reproducing it in full.
- Assumptions:
  - Publication date taken from page metadata (`2026-03-10` in the rendered page and `2026-03-11T02:41:22.000Z` in OG metadata) and recorded as `2026-03-10` to match the page’s displayed date.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `curl -L --show-error --fail "https://blog.langchain.com/the-anatomy-of-an-agent-harness/?utm_source=tldrai" -o /tmp/langchain-agent-harness.html`
  - `tail -n 40 AGENT_LOG.md`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline|time datetime|harness|LangChain|<h1" /tmp/langchain-agent-harness.html`
  - `sed -n '1,360p' /tmp/langchain-agent-harness.html`
  - `python3 scripts/new_article.py --title "The Anatomy of an Agent Harness" --url "https://blog.langchain.com/the-anatomy-of-an-agent-harness/?utm_source=tldrai" --author "Vivek Trivedy" --published 2026-03-10 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
  - `python3 -c "import os; p='scripts/__pycache__/build_index.cpython-314.pyc'; os.remove(p) if os.path.exists(p) else None"`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: William J. Bowman on when generative models are useful

- What I did: Read the article at `https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/?utm_source=tldrdev`, created a new article summary, and captured the post’s main contribution: a three-part framework for evaluating generative-model usefulness in terms of encoding cost, verification cost, and process dependence.
- Files created/modified:
  - Created: [`articles/2026/2026-03-05_against-vibes-when-is-a-generative-model-useful.md`](articles/2026/2026-03-05_against-vibes-when-is-a-generative-model-useful.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Preserved the author’s three-factor model because it is the article’s central contribution and the part most reusable for this repo.
  - Treated the post as an evaluative framework rather than a general anti-AI rant, even though the tone is skeptical, because the useful signal here is the decision model.
  - Flagged claims about objective productivity studies and rising verification cost as items worth validating because the article argues them conceptually rather than demonstrating them in detail.
- Assumptions:
  - Publication date taken from the page (`2026-03-05`) and recorded as `2026-03-05`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `curl -L --show-error --fail "https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/?utm_source=tldrdev" -o /tmp/against-vibes.html`
  - `tail -n 40 AGENT_LOG.md`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline|time datetime|<h1|William|Bowman|vibes|generative model" /tmp/against-vibes.html`
  - `sed -n '1,360p' /tmp/against-vibes.html`
  - `python3 scripts/new_article.py --title "Against Vibes: When is a Generative Model Useful" --url "https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/?utm_source=tldrdev" --author "William J. Bowman" --published 2026-03-05 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
  - `python3 -c "import os; p='scripts/__pycache__/build_index.cpython-314.pyc'; os.remove(p) if os.path.exists(p) else None"`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-12 — Summarize external article: Jim Yagmin on docs directories and context management

- What I did: Read the article at `https://yagmin.com/blog/your-docs-directory-is-doomed/?utm_source=tldrdev`, created a new article summary, and captured the core argument that ad hoc markdown context systems (`CLAUDE.md`, `AGENTS.md`, `/docs`, specs) are a temporary stage that will break down without better context architecture.
- Files created/modified:
  - Created: [`articles/2026/2026-03-05_your-docs-directory-is-doomed.md`](articles/2026/2026-03-05_your-docs-directory-is-doomed.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Focused the summary on the article’s structural argument about context management rather than treating it as a generic anti-docs piece.
  - Preserved the author’s four design properties for better context systems: organization-owned, navigable, composable, and code-aware.
  - Treated context-driven development (CDD) as an interpretive proposal rather than an established method, so its strongest promises are in “Claims worth validating.”
- Assumptions:
  - Publication date taken from the page (`05 Mar 2026`) and recorded as `2026-03-05`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `curl -L --show-error --fail "https://yagmin.com/blog/your-docs-directory-is-doomed/?utm_source=tldrdev" -o /tmp/your-docs-directory-is-doomed.html`
  - `tail -n 40 AGENT_LOG.md`
  - `rg -n "title|author|published|date|og:|description|ld\\+json|application/ld\\+json|article:published_time|byline|time datetime|<h1|docs|directory|Yagmin|yagmin" /tmp/your-docs-directory-is-doomed.html`
  - `sed -n '1,360p' /tmp/your-docs-directory-is-doomed.html`
  - `python3 scripts/new_article.py --title "Your Docs Directory Is Doomed" --url "https://yagmin.com/blog/your-docs-directory-is-doomed/?utm_source=tldrdev" --author "Jim Yagmin" --published 2026-03-05 --captured 2026-03-12`
  - `python3 scripts/build_index.py`
  - `python3 -c "import os; p='scripts/__pycache__/build_index.cpython-314.pyc'; os.remove(p) if os.path.exists(p) else None"`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-13 — Summarize external article: Jina Yoon on product-management skills for engineers

- What I did: Read the article at `https://newsletter.posthog.com/p/an-engineers-guide-to-product-management?utm_source=tldrdev`, created a new article summary, and captured the post’s central argument that engineers should borrow three PM skills as implementation gets easier: gathering context, operating feedback loops, and communicating toward action.
- Files created/modified:
  - Created: [`articles/2026/2026-03-11_wtf-does-a-product-manager-do-and-why-engineers-should-care.md`](articles/2026/2026-03-11_wtf-does-a-product-manager-do-and-why-engineers-should-care.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Used the article’s on-page title, `WTF does a product manager do? (and why engineers should care)`, rather than the URL slug text because the summary files follow published titles.
  - Kept the summary centered on the article’s three-skill framework because that is the clearest reusable structure in the source.
  - Treated the Duolingo, Canva, Figma, and PostHog metrics as “Claims worth validating” because the article uses them as evidence but does not reproduce their full underlying methodology.
- Assumptions:
  - Publication date taken from page metadata (`2026-03-11T21:11:01+00:00`) and recorded as `2026-03-11`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `pwd && rg --files .`
  - `sed -n '1,220p' AGENTS.md`
  - `sed -n '1,220p' CONTRIBUTING.md`
  - `sed -n '1,240p' docs/SUMMARY_GUIDE.md`
  - `sed -n '1,240p' INDEX.md`
  - `sed -n '1,240p' AGENT_LOG.md`
  - `sed -n '1,240p' templates/article-summary.md`
  - `sed -n '1,240p' articles/2026/2026-03-08_do-ai-enabled-companies-need-fewer-people.md`
  - `python3 scripts/new_article.py --help`
  - `git status --short`
  - `curl -L --show-error --fail 'https://newsletter.posthog.com/p/an-engineers-guide-to-product-management?utm_source=tldrdev' -o /tmp/posthog_pm.html`
  - `rg -n 'author|datePublished|og:title|twitter:title|Product|engineer|PM|JTBD|trade|roadmap|prototype|interview|metric' /tmp/posthog_pm.html | head -n 120`
  - `rg -n 'body_html|truncated_body_text|bodyHtml|bodyJson' /tmp/posthog_pm.html | head -n 20`
  - `python3 scripts/new_article.py --title 'WTF does a product manager do? (and why engineers should care)' --url 'https://newsletter.posthog.com/p/an-engineers-guide-to-product-management?utm_source=tldrdev' --author 'Jina Yoon' --published 2026-03-11 --captured 2026-03-13`
  - `python3 - <<'PY' ... PY` (parsed `window._preloads` from `/tmp/posthog_pm.html` to extract article body text for summarization)
  - `sed -n '1,220p' articles/2026/2026-03-11_wtf-does-a-product-manager-do-and-why-engineers-should-care.md`
  - `tail -n 80 AGENT_LOG.md`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-13 — Summarize external article: Tomasz Tunguz on AI and the “marginal hire”

- What I did: Read the article at `https://tomtunguz.com/marginal-hire/?utm_source=tldrnewsletter`, created a new article summary, and captured the main thesis that AI’s employment impact may show up first as canceled future hires rather than visible layoffs.
- Files created/modified:
  - Created: [`articles/2026/2026-03-11_the-marginal-hire.md`](articles/2026/2026-03-11_the-marginal-hire.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Treated the piece as a framing/background source rather than a data-heavy analysis because the post is short and primarily advances a thesis.
  - Preserved “marginal hire” as the organizing concept because it is the article’s main contribution and the clearest reusable lens for later synthesis.
  - Put the job-openings numbers and restructuring forecast into “Claims worth validating” because the article asserts them with limited methodological detail in the post itself.
- Assumptions:
  - Publication date taken from page metadata (`2026-03-11T00:00:00Z`) and recorded as `2026-03-11`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `sed -n '1,200p' templates/article-summary.md`
  - `tail -n 60 AGENT_LOG.md`
  - `curl -L --show-error --fail 'https://tomtunguz.com/marginal-hire/?utm_source=tldrnewsletter' -o /tmp/marginal-hire.html`
  - `rg -n 'title|author|datePublished|article:published_time|og:title|twitter:title|<h1|Tom|hire|employee|AI|marginal|software engineer|revenue' /tmp/marginal-hire.html | head -n 80`
  - `sed -n '470,530p' /tmp/marginal-hire.html`
  - `python3 scripts/new_article.py --title 'The Marginal Hire' --url 'https://tomtunguz.com/marginal-hire/?utm_source=tldrnewsletter' --author 'Tomasz Tunguz' --published 2026-03-11 --captured 2026-03-13`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-13 — Summarize external article: Steve Krenzel on agentic coding and “good code”

- What I did: Read the article at `https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code?utm_source=tldrdev`, created a new article summary, and captured its central argument that agentic coding raises the value of software engineering disciplines like tests, types, naming, and fast environment automation.
- Files created/modified:
  - Created: [`articles/2025/2025-12-29_ai-is-forcing-us-to-write-good-code.md`](articles/2025/2025-12-29_ai-is-forcing-us-to-write-good-code.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Recorded the publication date as `2025-12-29` because the page metadata explicitly lists `datePublished` on that date, even though the user added it on March 13, 2026.
  - Kept the summary organized around the article’s concrete engineering investments instead of following the essay section-by-section verbatim.
  - Treated the stronger claims about 100% coverage, file-size effects, and TypeScript superiority as “Claims worth validating” because the article is mostly experience-based.
- Assumptions:
  - Publication date taken from page metadata (`2025-12-29T18:30:28+00:00`) and recorded as `2025-12-29`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `tail -n 50 AGENT_LOG.md`
  - `sed -n '1,180p' templates/article-summary.md`
  - `curl -L --show-error --fail 'https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code?utm_source=tldrdev' -o /tmp/logic-good-code.html`
  - `rg -n 'title|author|datePublished|article:published_time|og:title|twitter:title|<h1|good code|AI|Logic|Substack|maintain|test|abstraction|documentation|type' /tmp/logic-good-code.html | head -n 120`
  - `python3 - <<'PY' ... PY` (parsed `window._preloads` from `/tmp/logic-good-code.html` to extract article body text for summarization)
  - `python3 scripts/new_article.py --title 'AI Is Forcing Us To Write Good Code' --url 'https://bits.logic.inc/p/ai-is-forcing-us-to-write-good-code?utm_source=tldrdev' --author 'Steve Krenzel' --published 2025-12-29 --captured 2026-03-13`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed under `2025`.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-13 — Summarize guide chapter: Simon Willison on code becoming cheap

- What I did: Read the guide chapter at `https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/`, created a new article summary, and captured its main framing argument that agentic engineering changes software economics by making code production cheap while leaving “good code” expensive.
- Files created/modified:
  - Created: [`articles/2026/2026-02-23_writing-code-is-cheap-now.md`](articles/2026/2026-02-23_writing-code-is-cheap-now.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Used the chapter title `Writing code is cheap now` rather than the broader guide title, because the summary files should track the specific page being summarized.
  - Recorded the publication date as `2026-02-23` based on the page’s explicit “Created” date; the page also notes a last modification on `2026-02-24`.
  - Treated the piece as a framing chapter rather than a detailed workflow guide because it is short and conceptual.
- Assumptions:
  - Publication date taken from the page’s “Created: 23rd February 2026” marker and recorded as `2026-02-23`.
  - Preserved the user-provided canonical URL as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `tail -n 60 AGENT_LOG.md`
  - `sed -n '1,180p' templates/article-summary.md`
  - `curl -L --show-error --fail 'https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/' -o /tmp/code-is-cheap.html`
  - `rg -n 'title|author|datePublished|article:published_time|og:title|twitter:title|<h1|Simon|code is cheap|agentic|LLM|generated code|maintain' /tmp/code-is-cheap.html | head -n 120`
  - `rg -n 'pubdate|date|datetime|Published|Updated|202[0-9]|time' /tmp/code-is-cheap.html | head -n 80`
  - `sed -n '52,95p' /tmp/code-is-cheap.html`
  - `python3 scripts/new_article.py --title 'Writing code is cheap now' --url 'https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/' --author 'Simon Willison' --published 2026-02-23 --captured 2026-03-13`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.

## 2026-03-13 — Summarize guide chapter: Simon Willison on using AI to produce better code

- What I did: Read the guide chapter at `https://simonwillison.net/guides/agentic-engineering-patterns/better-code/?utm_source=tldrnewsletter`, created a new article summary, and captured its core argument that teams should use AI to reduce technical debt, explore more options, and improve quality rather than accept lower standards.
- Files created/modified:
  - Created: [`articles/2026/2026-03-10_ai-should-help-us-produce-better-code.md`](articles/2026/2026-03-10_ai-should-help-us-produce-better-code.md)
  - Modified: [`AGENT_LOG.md`](AGENT_LOG.md)
  - Modified: [`INDEX.md`](INDEX.md)
- Decisions made (and why):
  - Used the chapter title `AI should help us produce better code` rather than the broader guide title because the summary files should map to the specific page summarized.
  - Recorded the publication date as `2026-03-10` based on the page’s explicit “Created” date; the page also notes a last modification on `2026-03-11`.
  - Focused the summary on three actionable themes from the chapter: cheap refactors, exploratory prototyping, and the compound-engineering feedback loop.
- Assumptions:
  - Publication date taken from the page’s “Created: 10th March 2026” marker and recorded as `2026-03-10`.
  - Preserved the user-provided URL, including the UTM parameter, as `source_url`.
- Commands run (if any):
  - `git status --short`
  - `tail -n 50 AGENT_LOG.md`
  - `sed -n '1,180p' templates/article-summary.md`
  - `curl -L --show-error --fail 'https://simonwillison.net/guides/agentic-engineering-patterns/better-code/?utm_source=tldrnewsletter' -o /tmp/better-code.html`
  - `rg -n 'title|author|og:title|twitter:title|<h2 class=\"archive-h2\"|Created:|Last modified:|pubdate|date|better code|AI should help us produce better code' /tmp/better-code.html | head -n 120`
  - `sed -n '52,118p' /tmp/better-code.html`
  - `python3 scripts/new_article.py --title 'AI should help us produce better code' --url 'https://simonwillison.net/guides/agentic-engineering-patterns/better-code/?utm_source=tldrnewsletter' --author 'Simon Willison' --published 2026-03-10 --captured 2026-03-13`
- Test results (if relevant):
  - `python3 scripts/build_index.py` completed successfully and regenerated [`INDEX.md`](INDEX.md) with the new article listed.
- Open questions / ambiguities:
  - None at capture time.
