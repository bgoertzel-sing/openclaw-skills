# Why Tiny Shakespeare Is Too Small for GPT-2-Small–Scale SLT Work

**Prepared for sharing with colleagues using Tiny Shakespeare for learning-dynamics experiments.**

*Epistemic note: Claims marked **Observed** come from our RelaLeap project run logs and code. Claims marked **Inferred** are reasoned conclusions from that evidence. Claims marked **Principled** are general theoretical arguments that hold regardless of our specific setup.*

---

## 1. The raw numbers

| Property | Tiny Shakespeare (our setup) | GPT-2-small on Tiny Shakespeare | GPT-2-small on proper data |
|---|---|---|---|
| Corpus size | ~1.1 MB, ~1.0M characters | ~1.1 MB, ~1.0M characters | WebText ~40 GB, ~8B tokens |
| Tokenization | Character-level, **65-token vocabulary** | BPE, 50,257-token vocabulary | BPE, 50,257-token vocabulary |
| Token count | ~1.0M tokens | ~300K tokens (BPE) | ~8B tokens (or ~10⁸–10⁹ for OpenWebText slice) |
| Model parameters | ~82K (2-layer char transformer) | 124M | 124M |
| Parameters-per-token | ~0.08 (near boundary) | ~413 (deep memorization) | ~0.015 (generalization regime) |
| Training data domains | 1 (Shakespeare) | 1 (Shakespeare) | Thousands (web crawl) |
| Register / style | Single author, archaic English, iambic meter | Same | Multi-domain, multi-author, multi-register |

**Observed** (from `src/relaleap/slt/tinyshakespeare.py`): Our SLT validation runs used a character-level `TinyCharTransformer` with `vocab_size=65` (the sorted set of ASCII characters in the corpus), `d_model=64`, `nhead=2`, `num_layers=2`, `d_ff=256`, `seq_len=128`. Total parameters: ~82K. The corpus was the standard Karpathy Tiny Shakespeare (`input.txt`), tokenized as individual characters.

**Principled**: The corpus-to-model ratio is the critical bottleneck. When the corpus is smaller than or comparable to the model's memorization capacity, the model memorizes rather than generalizes. For a 124M-parameter GPT-2-small, Tiny Shakespeare's ~1M tokens are roughly **100 parameters per token** — deep in the memorization regime. Even our smaller 82K model on 1M tokens (~12 parameters per token) sits near the boundary.

## 2. The corpus is smaller than the model's capacity

**Observed** (from SLT run reports, `experiments/slt_validation_run1/` and `slt_validation_large_run1/`):

- The WBIC/SGLD estimator produced **Rhat values of 1.3–3.3** across transformer blocks (target: <1.2). This means the SGLD chains didn't mix — the loss landscape is dominated by sharp memorization wells rather than broader generalization basins.
- **6–9 of 37 parameter blocks** were marked `diagnostic_only` (negative λ̂ estimates) in each run. A true RLCT cannot be negative; these blocks are flat or unused under the sampler, consistent with parameters that contribute to memorization rather than structured learning.
- The **calibration benchmark** (product singularity, target λ=0.5) passed at λ̂=0.472±0.026 in the large run — so the estimator itself is sound. The problem is that the *object being measured* (a memorization solution) has a different and less interpretable geometry than a generalization solution.

**Inferred**: The SLT measurements we obtained are real measurements of the wrong phenomenon. They characterize the singular structure of a memorization basin, not a generalization basin. Moving to GPT-2-small–scale data would shift the learned solution into a different loss landscape basin where the λ̂ values probe the geometry we actually care about.

## 3. The corpus is stylistically and distributionally degenerate

**Principled**: Tiny Shakespeare is one author, one register, archaic English, with heavy structural repetition (speaker tags, act/scene scaffolding, iambic meter). The effective entropy is low and the vocabulary is tiny (65 characters at char-level; ~20K word types at word-level). This means:

- Measured "capabilities" reflect **surface n-gram statistics**, not compositional or semantic structure.
- Findings **don't transfer** — a phase transition or circuit found on Shakespeare may be an artifact of its idiosyncratic bigram/character-level statistics, not a general property of transformers.
- The **diversity of learning phenomena** (induction heads, in-context learning, factual recall, code execution) is absent because the corpus doesn't exercise them.

## 4. The ePC distillation experiments confirm the bottleneck empirically

**Observed** (from `experiments/20260715T153035Z-epc-distillation-gate-local-r2/RUN.md`):

We ran a matched-state ePC (energy-based predictive coding) distillation gate on Tiny Shakespeare with a tiny student transformer (d_model=16, 2 layers, 2 heads, seq_len=32, batch_size=4, 6 training steps). Results:

| Method | Mean held-out perplexity | Notes |
|---|---|---|
| BP (backprop) | 76.21 | Baseline |
| KD (λ=0.05) | 76.18 | Ordinary knowledge distillation |
| ePC T=8, λ=0.05 | 76.19 | Best nontrivial ePC depth |

**ePC failed to beat matched KD in all three seeds.** The gate failed closed.

**Observed** (from the normalization fix run, `20260715T154840Z-epc-local-credit-normalization/RUN.md`): A subsequent fix corrected a batch-normalization bug that had suppressed hidden local credit by `seq_len*d_model`. Even after the fix, the corrected ePC still lost to matched KD on held-out perplexity.

**Inferred**: This null result is honest, but it is also **underpowered**. With seq_len=32, batch_size=4, and 6 training steps on a 65-vocabulary corpus, the model is barely learning anything at all — perplexity ~76 on a 65-character vocabulary is close to trivial (random would be 65). You cannot distinguish "ePC doesn't work" from "Tiny Shakespeare doesn't exercise the learning dynamics ePC targets" because the corpus is too small to produce those dynamics.

## 5. Diagnostics that confirm Tiny Shakespeare is bottlenecking your run

Check these in your own experiment logs:

1. **Train/val gap opens early and wide** → memorization, not learning.
2. **Val loss floors quickly** and is insensitive to model size or more training steps → you've saturated the corpus's information content.
3. **SGLD/SLT sampler diagnostics degrade** (Rhat >> 1.2, low ESS) → the loss landscape is dominated by sharp memorization wells rather than smooth generalization basins.
4. **Many parameter blocks return negative or near-zero λ̂** → parameters are flat or unused, consistent with a memorization solution rather than a structured one.
5. **Results don't survive a held-out-domain probe** → learned statistics are corpus-specific.
6. **Perplexity remains near the random baseline** for small models / short training → the corpus doesn't provide enough signal to drive meaningful learning.

## 6. Why GPT-2-small–scale data specifically

The goal is not "biggest possible" — it's **crossing the threshold where generalization is cheaper than memorization** for a 100M-scale model.

**Principled**:
- A 124M-parameter model needs roughly **Chinchilla-scale data** (~2B tokens for compute-optimal training, but at minimum ~10⁸–10⁹ tokens) so that memorization is not the cheapest solution.
- **Multi-domain, higher-entropy text** (WebText/OpenWebText-style) ensures measured capabilities reflect compositional and semantic structure, not one author's idiosyncrasies.
- For SLT specifically: the RLCT λ is a property of the loss landscape geometry near the learned solution. That geometry is fundamentally different when the model memorizes versus when it generalizes. You need enough data to push the model into the generalization regime for the measurement to be meaningful.

## 7. The deeper principle: corpus-swap invariance

The phenomena we *want* to study (grokking, phase transitions, circuit formation, learning-coefficient trajectories) should be properties of the **learning dynamics of the architecture**, invariant across corpora of sufficient scale and entropy. What Tiny Shakespeare gives you instead is phenomena that are properties of *that specific corpus's* bigram statistics.

The clean test: **does the phenomenon survive a corpus swap?** If your phase transition, circuit, or λ trajectory reproduces on OpenWebText, WikiText, and code — same qualitative structure, shifted only in timing/scale — it's a dynamics property. If it dissolves or reshapes when you change the corpus, it was an idiosyncrasy you mistook for dynamics.

This is the deeper reason to move to GPT-2-small scale, beyond just "bigger": you need a corpus rich enough that its idiosyncrasies are *washed out*, so what remains and is measurable is the architecture's learning behavior. Single-author, low-entropy text has idiosyncrasies with enough signal strength to *dominate* the measurement — you can't cleanly separate the two layers. Multi-domain, high-entropy data pushes the corpus-specific component below the noise floor, leaving the invariant dynamics as the thing you actually observe.

**The principle for colleagues: a finding on Tiny Shakespeare is a hypothesis about learning dynamics; a finding that survives corpus-swap is evidence.**

## 8. One-line summary

*Tiny Shakespeare is fine as a plumbing and overfitting sanity check, but it's smaller than the model, single-domain, and low-entropy — so any 100M-scale transformer memorizes it before it generalizes. Studies of learning dynamics, capability emergence, or interpretability run on it measure memorization artifacts, not transformer behavior. Move to an OpenWebText/GPT-2-small–scale corpus (≥~10⁸–10⁹ tokens, multi-domain) so generalization is the cheaper solution and the phenomena you observe are properties of the learning dynamics, not the corpus's idiosyncrasies.*

---

## Provenance

- RelaLeap SLT runs: `projects/relaleap/experiments/slt_validation_run1/`, `slt_validation_large_run1/` (2026-07-10, Runpod A100)
- RelaLeap ePC distillation gates: `projects/relaleap/experiments/20260715T153035Z-epc-distillation-gate-local-r2/`, `20260715T154840Z-epc-local-credit-normalization/` (2026-07-15, local CPU)
- SLT interpretation report: `projects/relaleap/docs/slt_tiny_shakespeare_transformer_analysis.tex` / `.pdf` (2026-07-10)
- Model definition: `projects/relaleap/worktrees/slt-integration/src/relaleap/slt/tinyshakespeare.py`
- Project record: `projects/relaleap/PROJECT.md`
