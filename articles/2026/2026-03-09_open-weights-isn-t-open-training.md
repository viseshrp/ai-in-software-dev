---
title: "Open Weights isn't Open Training"
author: "Addie Foote"
published: "2026-03-09" # YYYY-MM-DD if known
captured: "2026-03-12"  # YYYY-MM-DD (when you summarized it)
source_url: "https://www.workshoplabs.ai/blog/open-weights-open-training?utm_source=tldrai"
source_domain: "www.workshoplabs.ai"
---

# Open Weights isn't Open Training

## Core ideas (structured)

- The author argues that releasing open model weights is not the same as making a model practically trainable or adaptable by others.
- The post is organized as a debugging narrative around trying to post-train `Kimi-K2-Thinking`, using success criteria that are both quantitative (loss decreases) and qualitative (behavior changes in the expected direction).
- The author’s main thesis is that the open-source model stack contains too much hidden complexity, leaky abstraction, and infrastructure debt for “open weights” alone to deliver easy downstream customization.
- In the attempt described here, supposedly supported training paths were either buggy, unnecessarily complex, or materially more expensive than managed alternatives.
- The article walks through a chain of concrete failures: repeated quantization/compression of already-quantized weights, allocator behavior that required a non-obvious environment flag, bad automatic device placement, incompatibilities between quantized weights and LoRA tooling, a hard assertion that blocked training mode in a gate implementation, and an OOM bug caused by dequantized weights not being cleaned up properly.
- Although the author eventually gets training to run and loss to fall, the result still cannot train experts and remains much slower and more expensive than desired.
- The concluding argument is that open-source ML infrastructure often fails not because one bug exists, but because every layer of the stack adds another dependency, workaround, and hidden assumption.

## What seems to work (per the author)

- Manual investigation of the stack, including narrowing failures to specific libraries and functions, eventually produced a minimally working post-training setup.
- Skipping unnecessary recompression of already-quantized weights appears to remove one major bottleneck.
- Setting `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` is presented as necessary to get past a long, opaque stall during model loading and dispatch.
- Replacing `device_map='auto'` with an explicit layer-to-GPU mapping helped fix severe memory imbalance across devices.
- Restricting LoRA targets to shared experts and other non-quantized components allowed training to proceed when quantized experts were incompatible with the expected PEFT interfaces.
- Bypassing the non-differentiable `MoEGate` training assertion by using eval mode, while keeping the relevant parameters frozen, allowed the forward path to continue.
- Rewriting the compressed linear forward pass so dequantized weights are used transiently and explicitly discarded fixed the observed OOM behavior and enabled successful training steps.

## Limitations / risks (per the author)

- The training stack still fails to train the experts, which the author says are likely the most important parameters to adapt.
- Even after many fixes, the resulting setup is estimated to be roughly 6-9x more expensive per token than using a training API like Tinker.
- The path to a working result required monkey-patching library internals, environment tuning, and manual infrastructure debugging, which makes reproducibility and maintainability weak.
- “Supported” open-source compatibility did not translate into a turnkey workflow; major abstractions had to be pierced repeatedly to make progress.
- The author implies that deeper optimizations and better parallelization setups might exist, but their attempts to configure them with Hugging Face were unsuccessful.
- The broader risk is strategic: open models may be available in theory while remaining difficult to customize cheaply or reliably in practice.

## Claims worth validating

- The claim that expert parameters are the most important parameters to train is attributed to external work and should be checked in the cited source.
- The estimate that this setup is 6-9x more expensive per token than Tinker is important but based on this author’s experiment and environment.
- The implication that open-source ML infra systematically hides debt “in every layer of the stack” is a strong generalization from a detailed but still bounded case study.
- The argument that open weights do not meaningfully democratize value creation unless the training stack is also workable is persuasive here, but this post presents one technical example rather than a broad survey.

## Notes (your interpretation, clearly labeled)

- This is highly relevant to the repo because it broadens “AI software development” beyond prompting or coding agents into the infrastructure question: how hard is it to adapt frontier open models yourself?
- It complements posts about faster AI-assisted implementation by showing the opposite end of the stack, where velocity collapses under tooling debt, allocator behavior, and incompatible abstractions.
- It also sharpens an important distinction for future synthesis: open inference access, open weights, and open training are materially different capabilities, and the gap between them may shape who can actually build on top of frontier models.

## Source

- https://www.workshoplabs.ai/blog/open-weights-open-training?utm_source=tldrai
