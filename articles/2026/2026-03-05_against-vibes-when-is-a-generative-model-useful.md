---
title: "Against Vibes: When is a Generative Model Useful"
author: "William J. Bowman"
published: "2026-03-05" # YYYY-MM-DD if known
captured: "2026-03-12"  # YYYY-MM-DD (when you summarized it)
source_url: "https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/?utm_source=tldrdev"
source_domain: "www.williamjbowman.com"
---

# Against Vibes: When is a Generative Model Useful

## Core ideas (structured)

- The author argues that discussion of generative models is too often driven by subjective impressions, hype, or “vibes” rather than by a clear model of when such systems are technically useful.
- He proposes a three-part framework for judging usefulness:
- `1.` Relative encoding cost: how expensive it is to specify the task to the model versus doing the work directly.
- `2.` Relative verification cost: how expensive it is to determine whether the generated output actually satisfies requirements.
- `3.` Artifact versus process dependence: whether the task is mainly about the produced artifact or whether the process of producing it matters intrinsically.
- The author claims usefulness often drops as task complexity rises, because probabilistic generation is less likely to satisfy subtle or unusual requirements and harder to verify reliably.
- In contrast, generative models can be useful when a task is tedious to perform directly, easy to express in a prompt, and trivial to verify afterward.
- The post also argues that user expertise remains necessary: novices are especially poorly positioned to verify complex outputs or judge whether a generated artifact actually meets domain requirements.
- A recurring theme is that models produce plausible output, not guaranteed useful output, and that plausibility can actually raise verification costs by making errors subtler and easier to trust.

## What seems to work (per the author)

- Generative models are useful, in the author’s view, when the prompt is cheap to write relative to the effort of doing the task directly.
- They are especially promising for tedious, low-stakes, easily checkable tasks where the user recognizes the right answer quickly once it appears.
- The author’s concrete positive example is using an agent to identify and install a forgotten X11 package: the prompt was simple, the direct work would have involved annoying cross-referencing, and the resulting shell command was easy to validate.
- He also describes using a generative model to draft a policy document, where the generated draft functioned more like a template that could then be manually revised.
- More generally, he suggests that strong utility may exist where artifacts are hard or time-consuming to assemble directly but straightforward to check once produced, or where generation is embedded in formal verification systems with highly reliable automated checks.

## Limitations / risks (per the author)

- The author argues that many software-engineering tasks involve semantically dense requirements that are easier to implement directly than to encode into a prompt.
- As outputs become larger and more complex, verification becomes more expensive and more likely to be skipped or weakened.
- Because generated output is optimized for plausibility, errors may become subtle rather than obvious, which can increase verification cost and risk.
- Some tasks are effectively unverifiable without redoing the underlying work; the author gives internet search summaries as an example.
- Process-driven tasks, such as education, research writing, or engineering practices where the process itself builds knowledge or guarantees properties, are poor fits for generative substitution.
- The author’s own experience with complex code generation was negative: after many hours and millions of tokens, the model still produced unusable code that superficially passed the prompted tests but was structurally unsound.

## Claims worth validating

- The claim that subjective feelings of productivity with agents have been refuted by objective studies is asserted here but not cited in detail in this post.
- The prediction that relative verification cost may rise as models become more capable, because their errors become subtler, is plausible but speculative.
- The claim that generative models are essentially useless for highly process-dependent tasks is a strong generalization from the author’s framework.
- The example that eight hours and several million tokens of Claude Opus 4.6 still failed to produce a useful implementation is anecdotal, though valuable as a case study.

## Notes (your interpretation, clearly labeled)

- This is highly useful for the repo because it supplies an explicit evaluative framework that can cut across both pro- and anti-AI articles without collapsing into general sentiment.
- It complements the more operational posts in the repo by asking a prior question: before optimizing an AI workflow, is this even a task where generation is likely to help?
- It may be especially useful in future synthesis as a counterweight to capability narratives: it pushes the repo toward distinguishing plausible output, useful output, and process-preserving work.

## Source

- https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/?utm_source=tldrdev
