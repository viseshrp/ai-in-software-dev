---
title: "Coding Agents Meet Distributed Reality"
author: "Joseph M. Hellerstein"
published: "2026-02-11" # YYYY-MM-DD if known
captured: "2026-03-01"  # YYYY-MM-DD (when you summarized it)
source_url: "https://jhellerstein.github.io/blog/codegen-reality/?utm_source=tldrnewsletter"
source_domain: "jhellerstein.github.io"
---

# Coding Agents Meet Distributed Reality

## Core ideas (structured)

- AI will increasingly generate distributed systems code, and distributed systems are where many of the hardest bugs live (ordering, retries, nondeterminism, long-lived state).
- The article argues that “test harder” is necessary but fundamentally bounded; finite exploration can miss real-world executions, and even found traces often don’t reveal the unstated cross-component assumptions that caused them.
- Core thesis: steer AI toward programming models where large classes of distributed bugs are unrepresentable unless the programmer explicitly opts into nondeterminism.
- The author frames “implicit contracts” as the key failure mode: ordering/delivery/idempotence assumptions sit between high-level intent and imperative procedures, and LLMs will guess unless the framework forces those contracts to be explicit.
- Hydro is presented as one such target framework: determinism by default, explicit ordering/delivery in interfaces, illegal compositions become type errors, and true nondeterminism is quarantined behind an explicit marker (`nondet!`).
- This is positioned as a tradeoff like Rust’s memory safety: it won’t prove your business logic correct, but it can eliminate a broad class of “heisenbugs” caused by accidental nondeterminism.

## What seems to work (per the author)

- Use a framework that makes distributed contracts explicit and machine-checkable, rather than leaving them implicit in imperative code.
- Constrain uncertainty to a small number of clearly marked sites (e.g., `nondet!`) so debugging and verification focus on the true ambiguity.
- Treat model checking and adversarial testing as valuable tools, but recognize they explore a bounded subset of executions and don’t guarantee correctness.
- Shift the question from “did we test enough?” to “did we understand the few places where the program can diverge?”
- In Hydro specifically, avoid introducing order-dependent logic when inputs are explicitly unordered; rely on compile-time checks to prevent silent mismatch.
- Use checkers in a way that targets uncertainty sites (the author cites HydroSim exploring around `nondet!` blocks rather than the whole system).

## Limitations / risks (per the author)

- Bounded checking tools (TLA+, Alloy, Jepsen, Antithesis) are powerful but do not provide a proof of correctness; they show “no bug found” in explored executions.
- Distributed outages often come from mismatched, unstated assumptions across components, and traces alone may not reveal the “wrong assumption” that caused the failure.
- Hydro is not presented as a full semantic verifier: it won’t prove application/business logic correctness or liveness goals.
- Practical adoption friction: models may be less fluent in Hydro (today) than in mainstream imperative code, though the author expects this to improve with training/tooling.

## Claims worth validating

- The claim that most future distributed code will be AI-generated is plausible, but this post does not provide data or forecasts to support it.
- The claim that frameworks like Hydro can eliminate “whole classes” of distributed heisenbugs is the core argument; validating it would require comparative evidence (e.g., defect rates, incident classes, or verification outcomes across similar systems).
- The claim that model checkers spend much of their effort chasing accidental nondeterminism due to hidden ordering/retry assumptions is plausible; verifying it would require case studies or tool output analyses.

## Notes (your interpretation, clearly labeled)

- This is a “language/framework target selection” argument: rather than scaling QA to match AI code volume, change the language surface so AI cannot express common distributed failure modes by default.
- It fits this repo’s “what works” theme as an example of raising the abstraction boundary: put contracts in types/constructs, and push ambiguity into explicit, reviewable escape hatches.

## Source

- https://jhellerstein.github.io/blog/codegen-reality/?utm_source=tldrnewsletter
