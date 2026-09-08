# GPT-2/WikiText BP, distilled-ePC, and direct-ePC protocol v1

Status: draft preregistration; no paid run authorized or launched.

## Question

On one pinned WikiText split and one parameter-matched GPT-2 student
architecture, how do these training routes differ in predictive quality,
compute efficiency, robustness, and internal organization?

1. `BP_CE`: random initialization, ordinary backpropagation on next-token CE.
2. `EPC_KD`: identical student initialization, fixed BP teacher, ePC activity
   settling and weight learning against frozen teacher logits plus the same CE
   mixture.
3. `EPC_CE`: identical student initialization, ePC activity settling and weight
   learning directly on next-token CE, with no teacher signal.

The previous R8/R9 work already compared BP+CE, BP+KD, and ePC+KD. The novel
primary comparison here is direct `EPC_CE`; prior checkpoints/results are
historical evidence, not substitutes for this matched rerun.

## Frozen fairness requirements

- Pin model/tokenizer and WikiText revisions, token matrices, train/validation/
  test indices, seeds, student architecture, initialization tensors, batches,
  optimizer family, precision, and evaluation code before opening outcomes.
- Use at least five seeds. Every arm starts from the byte-identical student
  initialization for its seed.
- Report both update-matched and measured wall-clock/FLOP-matched comparisons.
  Teacher pretraining cost is reported separately and is not hidden from the
  distilled arm's accounting.
- Tune only on a calibration split; freeze all hyperparameters before the
  untouched multi-seed confirmation split.
- Preserve `T=1`/ordinary-gradient equivalence and energy-monotonicity controls;
  any failed invariant invalidates the affected ePC result.

## Primary predictive endpoints

- Untouched WikiText test NLL/perplexity and next-token top-1/top-5 accuracy.
- Teacher-student KL for `EPC_KD`, reported as a secondary endpoint rather than
  a substitute for ground-truth next-token quality.
- Learning curves versus updates, wall time, and estimated FLOPs.

## Internal and functional endpoints

- Layerwise effective/participation/stable rank, anisotropy, activation
  covariance spectrum, sparsity/dead fraction, and inter-layer CKA.
- ePC settlement energy, residual decay, convergence failures, and local-update
  alignment with the exact BP gradient on a frozen diagnostic batch.
- Calibration (ECE/Brier), corruption and contiguous-span robustness, PTB or a
  separately pinned OOD corpus, weight/noise perturbation, and low-rank
  adaptation/forgetting under an identical downstream protocol.
- Representation probes must use frozen preregistered train/test splits and
  compare against label-permutation/null controls. Internal differences are not
  called favorable unless tied to a predeclared functional endpoint.

## Decision rule

No arm is promoted from one favorable metric. A favorable ePC result requires
non-inferior untouched predictive quality within a frozen tolerance plus at
least one reproducible improvement in compute-normalized learning, robustness,
calibration, or adaptation, without invariant failure. Report all arms and
negative results.

## Execution boundary

Run provider-free package, determinism, metric, and tiny-fixture tests first.
Then present one exact RunPod resource/image/region/storage/time/cost envelope
for Ben's explicit approval. Terminate after verified artifact return; do not
leave billable storage or endpoints running.
