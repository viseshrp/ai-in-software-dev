---
title: "WTF does a product manager do? (and why engineers should care)"
author: "Jina Yoon"
published: "2026-03-11" # YYYY-MM-DD if known
captured: "2026-03-13"  # YYYY-MM-DD (when you summarized it)
source_url: "https://newsletter.posthog.com/p/an-engineers-guide-to-product-management?utm_source=tldrdev"
source_domain: "newsletter.posthog.com"
---

# WTF does a product manager do? (and why engineers should care)

## Core ideas (structured)

- The article argues that product management and engineering are converging, and that LLMs make deciding what to build more important relative to the mechanics of implementation.
- The author reduces the product-manager playbook to three reusable skills for engineers: gathering the right context, tracking success through feedback loops, and communicating in ways that lead directly to action.
- “Context” is framed as the information that helps teams make the right product decisions, including metrics, competitor moves, user research, industry changes, and customer feedback.
- The article uses Duolingo, Instagram, Buffer, Canva, and Linear as examples of teams changing direction or finding better product moves when they uncovered the right form of context.
- The piece argues that recurring review loops matter because context alone is insufficient; teams need explicit mechanisms to check whether hypotheses and shipped work are actually moving key metrics.
- PostHog’s internal example is that a churn problem on Error Tracking was reframed from “missing features” to “trust and product quality,” leading to many reliability fixes rather than a feature push.
- The communication section argues that product work becomes effective when discussions include impact, specifics, relevant context, visible trade-offs, and a clear recommendation instead of vague problem statements.

## What seems to work (per the author)

- Engineers generating context directly, rather than waiting for PMs to hand it over, seems to help teams ship faster and gives developers a less filtered view of the underlying data.
- Lightweight discovery systems such as recurring user interviews, survey reviews, LLM-based struggle detection, and competitor digests are presented as practical ways engineers can build product intuition.
- Regular “growth review” style feedback loops, where teams inspect revenue trends, usage, customer feedback, and goals, are presented as a way to improve product judgment over time.
- Explicitly classifying outcomes as “nailed it,” “scraped it,” or “failed it” is presented as more useful than simply marking work complete, because it forces evaluation and learning.
- Testing ideas through A/B tests, prototype feedback, dogfooding, and direct customer follow-up is presented as a practical way to connect shipped work to outcomes.
- Pull requests are presented as the most actionable communication format when the next step is already clear, because they push discussion toward concrete decisions and shipping.

## Limitations / risks (per the author)

- The author notes that gathering useful context is hard because teams often do not know in advance which information will matter most at a given stage.
- The article warns that teams can spend significant time analyzing the wrong signals, only to discover that the real issue was elsewhere.
- Context without a feedback loop is presented as insufficient; teams may collect information but still fail to learn whether their decisions improved outcomes.
- Vague communication is treated as a risk because it can hide trade-offs, obscure impact, and make it harder for engineering teams to choose the right next action.

## Claims worth validating

- The claim that LLMs make “figuring out what to build” more of a bottleneck than “how to build it” is plausible but argued conceptually rather than evidenced here.
- The article cites a Figma survey saying 64% of designers, developers, and marketers say their work spans multiple product roles; that result should be checked against the original methodology.
- The Duolingo example includes the claims that current user retention rate was 5x more impactful on DAU than other projected metrics and that focusing on retention led to a 4.5x DAU increase over four years.
- The Canva example claims revenue doubled from $1.7B to $3.3B in two years after generative AI became a core feature; that framing and attribution should be checked carefully.
- The PostHog Error Tracking example claims churn improved from 21% to 10% in the following quarter after focusing on trust-related reliability issues; strong internal case study, but still worth validating independently.

## Notes (your interpretation, clearly labeled)

- This piece is useful to this repo less as a statement about PMs and more as a statement about the widening scope of engineering work in the AI era: if code generation gets easier, problem selection, prioritization, and outcome measurement become relatively more important.
- It pairs well with the repo’s emerging “product engineer” theme, where technical leverage increases but so does the need for direct user contact, stronger judgment, and tighter feedback loops.
- The article is only indirectly about AI-assisted software development, but it helps explain one likely downstream effect: engineers taking on more product-shaping work because implementation friction is falling.

## Source

- https://newsletter.posthog.com/p/an-engineers-guide-to-product-management?utm_source=tldrdev
