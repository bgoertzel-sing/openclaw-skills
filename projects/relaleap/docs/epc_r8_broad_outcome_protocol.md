# ePC r8: multi-seed robustness, plasticity, and representation protocol

Date: 2026-07-20
Status: frozen before remote execution

## Scientific question

Across matched initializations and training batches, does ePC produce a
reproducible functional advantage over BP+CE and ordinary BP+KD in robustness,
out-of-distribution behavior, or continual adaptation? What representation and
weight-geometry differences accompany any functional difference?

Structural difference alone is descriptive. An ePC advantage requires a
functional endpoint with uncertainty excluding zero and no material
in-distribution regression.

## A. r7 replication

- Seeds: `1729, 3253, 6421, 8191, 10103`.
- Student: random six-layer GPT-2-width transformer; common initialization per
  seed. Teacher: pinned `openai-community/gpt2`.
- Source: pinned WikiText-103 revision and identical batches within seed.
- 200 updates, context 256, effective batch 32, AdamW, lr 1e-4, bf16.
- Arms: BP+CE; BP+KD; ePC-original (T=4, lambda=.05); ePC-deep (T=12,
  lambda=.05); and a genuine BP+KD wall-clock control that runs until the
  ePC-original elapsed-time budget.
- Fixed deterministic evaluation segments; separate training/evaluation RNGs.
- Preserve final checkpoints and per-update loss, gradient, clipping, Adam,
  update/weight, energy, accepted-step, backtracking, and block-credit data.

Primary replication contrasts are ePC-original minus BP+KD for validation CE,
teacher KD gap, and wall-clock-normalized CE. ePC-deep is a mechanism ablation,
not the primary arm.

## B. Functional outcome battery

Run the same post-training rules on every seed/arm.

### Clean OOD and corruption robustness

- Clean loss on WikiText-103, TinyStories, and Penn Treebank.
- Random token replacement at 5%, 10%, and 20%, using fixed masks shared across
  arms within seed/domain.
- Contiguous-span replacement at matched corrupted-token mass.
- Residual-block skip sensitivity and hidden-state Gaussian-noise sensitivity
  at fixed relative scales.
- Matched relative weight perturbations at `1e-4, 3e-4, 1e-3` of parameter
  RMS; report loss-increase curves, not a single selected scale.

Primary robustness statistic: corruption-area-under-delta-loss across the
frozen severities, paired by seed and evaluation segment.

### Plasticity and continual learning

Attach the same zero-output rank-8 adapters to attention input and MLP input
projections, freeze every backbone, and use the same optimizer/batches.

1. Phase B: adapt to TinyStories for 50 updates; evaluate source, B, and C at
   updates 0, 10, 25, and 50.
2. Phase C: continue the same adapters on Penn Treebank for 50 updates; evaluate
   source, B, and C at phase-C updates 10, 25, and 50.

Report target adaptation AUC, forward transfer, source forgetting, B forgetting
after phase C, and final average loss. As a secondary check, repeat a 25-update
full-model CE adaptation; it cannot replace the frozen-backbone primary result.

### Representation and optimization style

- Corrected centered linear CKA, independently cross-checked in feature and
  Gram form, between arms on identical source/B/C tokens.
- Centered entropy effective rank, participation ratio, stable rank, and mean
  cosine anisotropy by layer/domain.
- Representation drift CKA before versus after each adaptation phase.
- Layerwise weight spectral/Frobenius norms and distance from the common init.
- Layerwise CE and KD gradient norms and cosine alignment on a fixed probe.
- Block skip/noise sensitivity profiles.

## Evaluation and uncertainty

- Fixed 64 segments per domain and seed; save indices and hashes.
- Report each seed and a hierarchical bootstrap over seeds and segments.
- Primary ePC claim compares ePC-original with both BP controls.
- A functional advantage requires: 95% paired interval favoring ePC on either
  continual-adaptation AUC or robustness AUC; pre-adaptation source loss no more
  than .02 nats worse; source forgetting no more than .02 nats worse; all five
  seeds and all instrument gates complete.
- Multiple secondary measurements are descriptive and reported without
  cherry-picking a winner.

## Validity gates

- Exact common initialization and training batches within seed.
- Bitwise-stable evaluation masks/indices across arms.
- Corrected CKA controls and known-rank spectral fixtures pass.
- Perturbation severity is parameter-RMS relative and independently tested.
- No non-finite metric, missing arm, checkpoint/hash drift, or silent fallback.
- ePC energy is monotone under the implemented backtracking contract.

## Research-rule focus

Rules 1, 2, 5, and 7: validate every estimator, freeze the behavioral contract,
record exact reproducibility, and keep training, evaluation, perturbation, and
adaptation behind separate interfaces.
