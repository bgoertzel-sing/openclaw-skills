# Source: Homotopy Distillation of a Transformer into a Predictive-Coding Network

- Type: `PDF`
- Authors/organization: Ahmad Mesto, UNSW Sydney
- Publication/version date: 2026-07-26; technical report, work in progress
- Retrieved: `2026-07-23`
- Canonical URL or identifier: User-supplied PDF; no canonical URL or DOI stated
- Current source: `report-2026-07-26.pdf`; text: `report-2026-07-26.txt`
- Current SHA-256: `69f243775affbe2e019522ebf86fa26162286737f819c9171134fd2cf7cdb642`
- Current text SHA-256: `3afcea703d6df91ccdf777dcc01bf856c4b10d128f2b6fc65150f6b6bcda71a0`
- Prior July 23 source: `source.pdf` / `source.txt`; SHA-256
  `b7ce36a4327278bde1935669b309030f3f4ae4ae1fc95b4d259ec0f906a8ff35`
- License/access constraints: No license stated; preserve for research review and quote sparingly
- Privacy tier: `local-private`
- Tags: `predictive-coding`, `epc`, `gpt-2`, `homotopy-distillation`, `local-learning`, `mork`, `continual-learning`
- Related projects: `relaleap`, `causal-fibres-ladder`, `morkql`, `hyperseed-formalizations`

## Summary

The report describes an ePC-style re-expression of pretrained GPT-2 124M.
The student begins from teacher weights and follows a geometric settlement-depth
schedule from the backpropagation-equivalent `T=1` anchor to `T=128`,
corresponding to terminal effective relaxation time `tau=6.4`. The author
reports five 5-million-token runs with near-lossless teacher fidelity, a
large increase in explicit block-error magnitude while maintaining output
fidelity, and strong rank concentration of terminal error-update mass.
The July 26 revision adds a completed 50-million-token production run and
more precise teacher-free gradient/frontier diagnostics.

The result is an expressivity and continuation result, not evidence that PC
outperforms backpropagation, improves continual learning, trains GPT-2 from
scratch, or provides a deployable matched-compute advantage. The report states
these boundaries explicitly.

## Key claims or contents

- Across five runs, worst milestone prompt KL is reported as
  `1.3e-5` nats and held-out perplexity remains within `0.4%` of the frozen
  teacher (page 3, section 3.1, Figure 1).
- The added 50-million-token run reportedly used `eta=0.10`, micro-batch 10,
  fp32, seven rungs, and one A100 for 35.7 hours. Across 51 milestones its
  worst KL was `3.1e-5`, final KL `5.8e-6`, and perplexity stayed within
  `0.58%` (page 3, section 3.1).
- Mean per-block error-norm ratio reportedly increases from `0.05` to `0.98`
  as `tau` rises from `0.05` to `6.4`, while minimum per-block cosine to the
  teacher remains above `0.998` (pages 3-4, section 3.2, Figure 2).
- At terminal settlement, the top `5%` of 4.72 million error cells reportedly
  carry about `90%` of squared update mass. A fixed-depth top-5% Hill
  descriptor is `alpha=1.681`; the report explicitly declines to claim a
  limiting power law because the estimate varies strongly with tail depth
  (pages 4-5, section 3.3, Figure 3).
- The revision reports terminal gradient ratio `0.98`, cosine floor `0.9986`,
  66% of frontier cells in blocks 2--5, 0.2% in the final three blocks, and
  top-5% update mass of 91.6% under teacher-free cross-entropy versus 90.0%
  under distillation (pages 3--5).
- The report claims a companion unpublished MORK implementation of the full
  GPT-2 forward pass with maximum relative logit error `6.06e-6`, a 16-fold
  expression-count reduction from blocked tensors, and exact 32-token greedy
  decoding (pages 5-6, section 6). No supporting code or artifacts accompany
  this PDF.

## Methods or implementation details

- Frozen pretrained GPT-2 124M teacher; student initialized from teacher.
- Explicit block-output errors `epsilon_l` are inference variables.
- Settlement minimizes quadratic error energy plus temperature-2
  distillation KL for `T` steps, with weights asserted frozen during
  settlement.
- Weight learning regresses each block on its settled target while treating
  settled states as constants; AdamW applies the resulting block-local
  gradients.
- Geometric depth schedule `T in {1,2,4,...,128}` with fixed step size and a
  stage hold/subdivision rule.
- Five reported 5-million-token runs vary seed and microbatch shape; the
  50-million-token production run is reported complete.

## Limitations and uncertainties

- This is presently author-reported evidence only: the supplied material has
  no code, raw telemetry, checkpoints, exact data identifiers, hardware
  record, or artifact hashes for independent reproduction.
- The production-run additions do not change that status: no checkpoint,
  config, raw milestone table, telemetry hash, or runnable settle code
  accompanied the revised PDF.
- The student starts from the teacher, so the near-lossless result establishes
  path/parameterization expressivity, not acquisition of the teacher function
  by PC or competitive training efficiency.
- Several plotted runs share seed 1729; the five-run set is not five distinct
  seeds. The report also says acceptance envelopes were recalibrated after
  replicate variability was observed, so the final bars are not a wholly
  untouched preregistration.
- The error-norm ratio is an explicit-error-state measure, not by itself a
  general representation-distance or causal-selectivity metric. Output KL and
  perplexity establish functional fidelity; cosine and error norms do not
  establish causal factorization.
- Equation (2) writes settlement as a gradient of the global energy with
  respect to all errors. The report establishes block-local weight objectives,
  but the PDF alone does not demonstrate the implementation-level locality,
  memory profile, or communication cost of settlement.
- The reported concentration is promising for compression, but the PDF does
  not specify enough cross-example, cross-layer, cross-seed, or intervention
  detail to establish that a stable frontier can be predicted cheaply.
- Continual-learning advantage, matched-compute benefit, coupled-objective
  ablation, compressed settlement, and from-scratch training remain planned.

## Relevance to current work

### Mapping onto the causal-fibres H0-H6 ladder

- It supplies strong *candidate* evidence for large-scale PC
  parameterization/path expressivity, adjacent to H0 but not the H0
  frozen-read/write teacher-gap test used in our ladder.
- It does not run the H1 matched dense/SAE/grouped/orthogonal/contextual
  representation contest.
- It does not establish H2 selective persistent plasticity or H3 held-out
  support/fingerprint generalization.
- It does not pass H4: no matched feed-forward or recurrent control shows
  that free PC settlement improves loss, robustness, retention, sample
  efficiency, or representation quality. Energy convergence and faithful
  teacher tracking are insufficient for that gate.
- It does not address H5 deployable constraint exploitation or H6 a learned
  causal highway.

### Relation to RelaLeap R8/R9

The report is not inconsistent with RelaLeap's finding that fixed-depth ePC
produced greater collapse and lower causal selectivity without a functional
advantage. Its method starts at a pretrained teacher identity and increases
settlement depth gradually while continuously distilling. This suggests a
specific new experimental arm: compare fixed-depth ePC against a matched-token,
matched-update, matched-wall-clock homotopy schedule, measuring the existing
R8/R9 loss, effective-rank, factor-selectivity, robustness, and continual
adaptation outcomes. The comparison must distinguish benefits of the
curriculum from benefits of the coupled local objective.

## Quotations or excerpts

> “This is a re-expression of a pretrained model, not from-scratch training.”

> “The motivating advantage is not yet demonstrated.”

## Follow-up questions

1. Can the author provide the repository, pinned commit, configs, raw
   milestone telemetry, checkpoint hashes, data identifiers, and hardware
   details for independent reproduction?
2. How is the global `grad_epsilon E` settlement implemented, and what are its
   measured locality, activation-memory, communication, and wall-clock costs
   relative to ordinary backpropagation?
3. Does a matched fixed-`T` control fail where the homotopy succeeds?
4. Does uncoupling the PC parameterization from the local settled-target
   objective identify which component preserves fidelity?
5. Is the top-5% frontier stable across prompts, tokens, layers, seeds, and
   checkpoints, and can it be predicted without first computing the dense
   error field?
6. Do continual-learning and robustness gains survive matched compute and
   identical information exposure?

## Version note: 2026-07-26 revision

Preserved alongside, rather than replacing, the July 23 original. Visual
inspection of page 4 confirmed Figure 1's five pilot/replicate KL traces and
the textual annotation of the 50-million-token run; the production trajectory
is not plotted as a sixth trace.
