# Causal-fibres Stage 0A/0B GPU experiment matrix

**Status:** approved by Ben 2026-07-23 06:48 PDT; Stage 0A authorized (expected $9.09, hard cap $13.48 / 9 A100-hours); Stage 0B conditional on 0A gate pass
**Project:** CAROM partial-Transformer distillation  
**Target:** `causal-fibres` 0.4.0 on a frozen GPT-2-small backbone  
**RunPod price used below:** A100-SXM4-80GB Secure Cloud at **USD 1.49/hour**

## Decision this experiment must make

Before adding predictive coding, ePC settlement, learned credit highways, or a
symbolic cap, determine:

1. whether the desired teacher correction is observable from frozen GPT-2
   residual-stream reads; and
2. if it is, whether a structured representation adds predictive or
   intervention value beyond dense, LoRA, and SAE controls at a matched budget.

This ordering is deliberately conservative. RelaLeap R9 Stage A
(`projects/relaleap/experiments/20260721T222400Z-r9-stage-a/`) found that ePC
had effective rank only 3.8--3.9 versus 13.9 for BP-CE and lower selectivity on
all four factors. The associated R8 analysis found final-block-only ePC credit
with gradient norm about \(3.3\times10^{-5}\) of ordinary KD. Those results make
credit starvation and representational collapse explicit failure modes.
Likewise, CAROM's GPT-2 12k run
(`projects/carom/experiments/20260722T015200Z-carom-gpt2-12k/`) peaked at step
3,000 and collapsed as the OneCycleLR approached its high-LR region. Stage 0
therefore uses exact backpropagation, a frozen backbone, a fixed low learning
rate with warmup, effective-rank monitoring, and early stability checkpoints.

The most relevant research rules are Rules 1, 2, 3, 5, and 7: validate the
estimator and interventions on constructed controls; freeze the software and
metric specification before training; use the package's contest/probe
interfaces; retain exact reproducibility metadata; and keep representation,
read-site aggregation, and write-head interfaces interchangeable.

## Common task and measurement contract

### Backbone and read/write interface

- Backbone: Hugging Face GPT-2-small, 124M parameters, hidden width 768,
  frozen in `eval()` mode. Record model revision and cached-weight SHA-256.
- Adapter starting point:
  `projects/carom/experiments/20260721T222400Z-carom-gpt2-arm/source/r9_carom_gpt2.py`.
  Reuse its real offset-mapped `GPT2Base`/`span_reps_gpt2` path, not the
  earlier TinyLM path.
- Candidate reads are the post-block residual stream at GPT-2 blocks 0--11.
  A multi-layer read concatenates layer-normalized site vectors and projects
  them to the arm's matched latent budget. “All” therefore does not receive an
  unreported 12-fold capacity advantage.
- Primary write site: additive residual-logit correction at the task head.
  Ordinary LoRA is inserted into the same task-side projection/write path; it
  does **not** update GPT-2 in Stage 0. A later substrate-LoRA experiment is
  Stage 2, not part of this matrix.
- Teacher target: logits from the fully supervised BP-CE teacher on the same
  grammar examples. Student/base logits are the frozen GPT-2 plus the common
  task readout before the tested residual. Freeze and hash both teacher and
  base checkpoints before generating residual targets.

### Synthetic grammar and counterfactuals

Each example is a controlled subject--verb--object clause with four annotated
binary factors:

| Factor | Values | Minimal edit |
|---|---|---|
| subject number | singular / plural | replace subject noun and repair only its agreement morphology |
| object number | singular / plural | replace object noun without changing subject agreement |
| tense | present / past | replace verb morphology while preserving arguments |
| negation | affirmative / negative | insert/remove the canonical negator and required auxiliary morphology |

Lexical identities, templates, and nuisance choices are sampled independently
of the four factors. For every factual sentence, generate four paired
counterfactuals, each flipping exactly one factor, plus a limited set of
multi-factor edits. Store source/edited token IDs, character-to-token offsets,
factor labels, edit mask, teacher logits, base logits, and pair ID.

Use disjoint lexical/template partitions:

- train: 8,192 factual clauses plus their four single-factor edits;
- validation: 1,024 factual clauses plus edits;
- in-support test: 2,048 factual clauses plus edits;
- held-out-combination test: 2,048 clauses from preregistered factor
  combinations withheld as combinations (each marginal factor value remains
  represented in training);
- selectivity controls: 512 paired edits per factor, with the other three
  factors and lexical content matched.

Generate once with data seed `20260723`, serialize without shuffling, and hash
the manifest and every split. Training loaders may shuffle with arm-specific
seeds, but evaluation arrays and their order remain frozen. Assert that the
teacher gap is positive and nontrivial separately for every factor before
launch; otherwise the corresponding closure percentage is uninterpretable.

### Metrics

Let \(L_B\), \(L_R\), and \(L_T\) be frozen-test cross-entropies of the base,
residual arm, and teacher. Report clipped and unclipped

\[
G = \frac{L_B-L_R}{L_B-L_T}
\]

as **teacher-gap closure**. The preregistered decision uses the unclipped
value, aggregated from example-level losses. Report total \(G\), four
single-factor paired closures, and bootstrap 95% confidence intervals. Also
report task accuracy, teacher KL, and the fraction of examples improved.

Intervention selectivity for factor \(f\) is the intended change in the
teacher-aligned factor score under a code intervention, divided by intended
plus absolute off-target changes. Report the full 4-by-4 intervention matrix,
not only its diagonal. Validate sign and scale on constructed one-factor
features before using this metric to rank real representations.

Every arm additionally reports layer/code effective rank, participation ratio,
dead-feature fraction, mean active features, gradient norm by component, and
the first checkpoint at which validation loss or effective rank degrades.
These are diagnostics, not substitutes for teacher-gap closure.

### Shared optimization

- Updates: 200; batch size 64; AdamW; gradient clipping 1.0.
- Schedule: 20-update linear warmup to a fixed, preregistered LR selected by a
  tiny **shared** calibration (`1e-4`, `3e-4`, `1e-3`) on dense `{0,5,11}`;
  then constant LR. The calibration selection rule is lowest validation loss
  at update 50 with no effective-rank drop greater than 25%. It is run once,
  not retuned per arm.
- Checkpoints/evaluation: updates 0, 20, 50, 100, 150, 200. Select the
  checkpoint by total validation teacher-gap closure; evaluate test sets once.
- Primary screen seed: 3253, matching the R8/R9 lineage. Confirmation seeds:
  8191 and 13007 for every arm within 5 percentage points of the stage leader
  or either decision boundary. Final claims use all three seeds.
- Arm order is randomized; the same cached hidden states and targets are used
  for all task-side arms. Deterministic algorithms are enabled where supported,
  and any nondeterministic CUDA operation is recorded.

## Stage 0A — frozen observability

### Read-site configurations

First run a **bundled individual-layer scan**: one job fits independent linear
and rank-32 probes to each of layers 0, 1, ..., 11 from the same cached
activations and emits twelve separately scored/checkpointed models of each
kind. Bundling is only an execution optimization; losses and parameter counts
remain per layer. It costs approximately two ordinary Stage 0A jobs and
satisfies the requirement to inspect every transformer layer before selecting
combinations.

The five capacity-contest configurations are:

1. `{0}` (early lexical/local signal);
2. `{5}` (middle representation);
3. `{11}` (final representation);
4. `{0,5,11}` (sparse depth coverage);
5. `{0,3,5,8,11}` (dense depth coverage).

If the bundled scan identifies another best individual layer, replace the
weakest of `{0}`, `{5}`, or `{11}` in the capacity contest, recording the
selection rule before viewing test results. Run the following diagnostic
additions only after the primary 35-cell screen:

- all layers `{0,...,11}` for the best linear/low-rank family and MLP;
- rerun all twelve individual layers with the best residual family if neither
  linear nor rank-32 is the winning family and no primary configuration passes
  50%.

Thus the approval unit is **35 capacity-contest jobs plus one bundled
individual-layer job**, with 3--4 diagnostic jobs expected (39--40 total).
The bundled job yields 24 separately auditable fits. This preserves the
requested 30--40-job launch envelope without silently treating untested layers
as observed.

### Primary 7-by-5 matrix

| Residual arm | Capacity definition | `{0}` | `{5}` | `{11}` | `{0,5,11}` | `{0,3,5,8,11}` |
|---|---|---:|---:|---:|---:|---:|
| linear | single affine correction | run | run | run | run | run |
| low-rank r=4 | factorized correction rank 4 | run | run | run | run | run |
| low-rank r=8 | factorized correction rank 8 | run | run | run | run | run |
| low-rank r=16 | factorized correction rank 16 | run | run | run | run | run |
| low-rank r=32 | factorized correction rank 32 | run | run | run | run | run |
| low-rank r=64 | factorized correction rank 64 | run | run | run | run | run |
| MLP | GELU bottleneck; width chosen to match r=64 trained parameters | run | run | run | run | run |

LoRA is a required matched control but is evaluated as a matched overlay on
each low-rank cell: same rank, input/output dimensions, trainable parameter
count, initialization, optimizer, and write site; only the parameterization
differs. The result table must show low-rank residual and LoRA side by side.
Implementations that make these algebraically identical must say so and count
them as a validation equivalence test, not as independent evidence.

For each row, report trainable parameters, deployment parameters, output rank,
FLOPs, and wall time. Parameter matching is exact where possible and within
2% otherwise.

### Stage 0A gate

- **Pass:** the best ordinary-BP residual has test teacher-gap closure
  **strictly greater than 50%**, with the three-seed 95% interval lower bound
  above 50%, and no factor closure below 25%.
- **Fail:** no configuration exceeds 50%. Stop representation claims and PC,
  ePC, or highway work. First run the all-layer/best-family diagnostic; then
  change read sites or write interface rather than increasing settlement
  depth.
- **Factor-limited:** total closure passes but one factor is below 25%. Stage
  0B may be run diagnostically, but the interface is not certified for claims
  about that factor.

## Stage 0B — matched representation contest

Use the winning Stage 0A read configuration. Use exact gradients for every arm
and the package entry points `RepresentationSteeringContest`,
`SAEFeatureSteering`, `audit_dictionary_operators`, and
`JointBlockDiagonalizer` as applicable.

### Arms

| Arm | Concrete configuration | Active/deployment constraint |
|---|---|---|
| dense bottleneck | GELU encoder/decoder residual | reference budget |
| LoRA | task-side read/write LoRA | same trained/deployed parameters as dense within 2% |
| SAE + steering | overcomplete code, top-k steering | active `k` matched to dense latent width |
| grouped SAE | same total dictionary width; 8 possibly overlapping groups | same mean active atoms as SAE |
| orthogonal fibres | 8 fibres of equal width; orthogonality penalty | active dimensions matched to dense latent width |
| contextual bundle | canonical code plus low-rank context transport | total deployment parameters matched; transport cost included |

Run two preregistered budgets:

- **B32:** dense latent width/mean active features 32;
- **B64:** dense latent width/mean active features 64.

SAE and grouped-SAE dictionaries may be 4x overcomplete, but their trained and
deployment parameter excess must be offset by reducing steering width so total
parameters remain within 2%; otherwise report them in a separate
capacity-unmatched appendix and do not use them for the win decision.
Contextual transports, biases, normalization parameters, and dictionaries all
count. Report (a) parameters ever trained, (b) deployment parameters, (c) mean
active features, (d) output rank, and (e) training/deployment wall clock.

The core contest is 6 arms x 2 budgets x 3 seeds = **36 runs**. A single-seed
screen (12 runs) may precede confirmation, but it cannot establish the gate.

### Metrics and Stage 0B gate

Rank arms on:

1. residual-target reconstruction MSE and explained variance;
2. total and four factor-specific teacher-gap closure;
3. 4-by-4 intervention selectivity and off-target mass;
4. teacher-gap closure on held-out factor combinations;
5. effective rank, participation ratio, dead fraction, and active features.

A structured arm (grouped SAE, orthogonal fibres, or contextual bundle)
advances only if, at a matched budget and over three seeds, it either:

- beats both dense and SAE controls by at least 3 percentage points of
  held-out-combination closure without losing more than 2 points total closure;
  or
- complements them by improving intervention selectivity by at least 0.10
  absolute with no more than 2 points loss in total and held-out closure.

Otherwise retain the best dense/SAE representation and record that structured
fibres were not supported. Reconstruction alone cannot pass this gate.

The later routing gate remains closed: **held-out support F1 must exceed 0.70**
before any PC/ePC settlement or learned-highway experiment. Stage 0B records
the held-out intervention/support labels needed for that later test but does
not reinterpret representation selectivity as support F1.

## Runtime and cost

### Pod specification

- 1 x RunPod Secure Cloud A100-SXM4-80GB;
- price: USD 1.49/hour;
- PyTorch/CUDA image pinned in the run ledger; persistent volume avoided;
- cache frozen GPT-2 activations once in FP16/BF16 and train probes in FP32
  where numerically necessary;
- automatic stop at process completion/failure and hard termination after
  artifact retrieval and hash verification.

The CAROM 12k GPT-2 record measured 10,582 seconds for 12,000 online updates
(0.882 seconds/update). A 200-update uncached upper bound is therefore about
2.9 minutes of training. Allowing cache construction, six evaluations,
serialization, and contest overhead gives these approval estimates:

| Unit | Expected wall time | Expected cost at $1.49/h | Hard per-run cap |
|---|---:|---:|---:|
| Stage 0A configuration/seed | 6 min | $0.15 | 10 min / $0.25 |
| Stage 0B arm-budget/seed | 10 min | $0.25 | 15 min / $0.37 |
| shared cache + metric validation | 45 min | $1.12 | 60 min / $1.49 |

Projected programme:

| Work | Count | Expected GPU time | Expected compute cost |
|---|---:|---:|---:|
| Stage 0A primary seed, including bundled layer scan | 36 jobs | 3.7 h | $5.51 |
| Stage 0A diagnostics | 4 jobs | 0.4 h | $0.60 |
| Stage 0A confirmation seeds for up to 10 finalists | 20 | 2.0 h | $2.98 |
| Stage 0B, 6 arms x 2 budgets x 3 seeds | 36 | 6.0 h | $8.94 |
| shared cache/validation and 15% operational reserve | — | 2.0 h | $2.98 |
| **Total expected** | **96 jobs** | **14.1 h** | **$21.01** |

The **hard approval envelope is 18 GPU-hours / USD 26.82**. This is not spend
authorization. Provisioning requires Ben's explicit approval under the remote
compute policy. Stop after Stage 0A (expected cumulative cost about $8.95
including setup/reserve) if its gate fails; do not consume the Stage 0B budget.

## Reproducibility and artifact contract

Create separate experiment ledgers for Stage 0A and Stage 0B. Before launch,
each must contain:

- repository remote/branch/commit and dirty-diff hash for the CAROM adapter and
  `causal-fibres` release;
- exact GPT-2 model revision, teacher/base checkpoint hashes, tokenizer hash,
  split-manifest hash, and cached-activation shard hashes;
- exact command, full resolved non-secret config, arm order, seeds, hardware,
  driver/CUDA/PyTorch/Transformers versions, precision, and determinism flags;
- per-checkpoint JSONL metrics, raw example-level losses, intervention
  matrices, gradient/component norms, rank diagnostics, stdout/stderr, exit
  status, and wall time;
- model checkpoints at 0/20/50/100/150/200, final selected checkpoint,
  parameter-count audit, and SHA-256 manifest covering every retrieved
  artifact.

Acceptance requires: all expected arm/seed records present; no NaN/Inf; frozen
backbone hashes unchanged; trainable-parameter audit within the declared
tolerance; metrics recomputable from raw losses; artifact manifest verified
locally; pod stopped/terminated and provider inventory rechecked.

## Approval checklist

Approval should explicitly cover:

1. Stage 0A expected USD 9.09 and conditional Stage 0B expected USD 11.92;
2. total expected USD 21.01, hard cap USD 26.82 / 18 A100-hours;
3. the 50% observability, structured-representation, and 0.70 held-out-support
   gates exactly as stated;
4. termination immediately on Stage 0A failure, non-finite training, repeated
   process failure, missing artifacts, or the hard time/cost cap.

No PC, ePC, learned highway, substrate co-adaptation, or symbolic-cap claim is
authorized by approving this Stage 0 matrix.
