# Five-arm causal-coding ePC local CPU experiment

- Experiment ID: `20260726T003000Z-causal-coding-epc-5arm`
- Project: `relaleap`
- Status: `complete_negative`
- Frozen: `2026-07-26T00:27:09Z` (filesystem timestamp; 16 seconds before execution)
- Execution: local CPU only
- Repository worktree: `projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-causal-coding`
- Branch: `agent/cmcp-epc-kd-bridge`
- Implementation commit: `4b0a425`

## Question and theoretical target

On the complementary-teacher Tiny Shakespeare fixture, can intervention-based
module support, causal gradient gates, clarity pressure, and a commutator proxy
jointly improve the plasticity/retention tradeoff of matched-mass ePC? This is a
small causal-coding implementation test motivated by the theorem's modularity
and small-commutator conditions; it is not a test of the theorem itself.

Research Rules 1, 2, 3, 5, and 7 govern the run: validate the support estimator,
freeze behavior before execution, reuse existing ePC/probes, preserve exact
evidence, and separate estimation, routing, regularization, and measurement.

## Frozen design

- Architecture/data: Phase-1 two-block Tiny Shakespeare
  `CausalCharTransformerLM` (`d_model=32`, two heads/block, FF=64, sequence
  length 32, dropout 0) and deterministic decreasing-arithmetic Task B.
- Seeds: `1729, 3253, 6421`.
- Teachers: 2,000-update Shakespeare teacher A and increasing-arithmetic
  complementary teacher, frozen per seed.
- Every arm starts from the identical per-seed student state and sees identical
  batches, optimizer, learning rates, 2,000 student updates, two teacher
  packets, two-step ePC, and normalized KD mass `0.5 + 0.5 = 1.0`.
- Arms: ordinary ePC; estimated-support gated ePC; gated+clarity ePC;
  gated+clarity+commutator ePC; true-label oracle-support ePC.
- Modules: two residual blocks and each block's two actual attention heads.
  A head do-intervention zeros its Q/K/V parameter rows and output-projection
  columns; a block intervention zeros its full residual transform.
- Estimated support: increase in temperature-2 teacher KL under intervention.
  Oracle support replaces teacher KL with true Task-A/Task-B CE labels.
  A module enters a task support when its nonnegative influence is at least
  `tau=0.35` times the maximum module influence for that task.
- Gates zero block/head gradients for `S_A \ S_B`; global embeddings, final
  normalization, and LM head remain shared.
- Clarity: coefficient `0.001` on squared block-parameter cosine similarity
  for blocks with different support labels.
- Full-arm commutator proxy: coefficient `0.001` on normalized squared inner
  product of Task-A/Task-B gradient fields, every 50 updates, using the CPU math
  attention kernel for double backward.
- Evaluation: Task-A loss/perplexity before and after common 200-update Task-B
  CE adaptation, Task-B loss/perplexity and adaptation AUC, accuracy retention,
  teacher CKA, centered entropy effective rank and participation ratio,
  block-skip losses, corruption p=0.1/0.3, direct one-step finite A→B versus
  B→A parameter commutator, off-support pre-gate gradient mass, per-module
  do-influence, and block credit wavefront.

## Frozen numerical promotion gate

Arm 4 is promoted only if all six aggregate three-seed checks pass:

1. mean Task-A loss forgetting is strictly lower than ordinary ePC;
2. mean final Task-B loss is no more than `1.05 ×` ordinary ePC;
3. mean finite-update commutator is strictly lower;
4. mean off-support gradient leakage is strictly lower;
5. mean hidden-state entropy effective rank is at least `0.90 ×` ordinary ePC;
6. mean number of blocks with gradient norm above `1e-12` is not lower.

Any non-finite metric, KD mass other than 1.0, non-monotone ePC trace, missing
record, or failed test invalidates the run. Directional thresholds are strict;
the 5% Task-B and 90% rank tolerances operationalize “materially” and “rank
collapse” before seeing results.

## Pre-run validation

- Focused suite: 20 passed.
- Full repository suite: 424 passed, 1 skipped.
- One-update/seed five-arm smoke: 5/5 records, exit 0.

## Planned evidence

- Exact command: `command.sh`
- Raw metrics: `artifacts/results.json`
- Checkpoints: `artifacts/checkpoints/`
- Logs/status/environment/git state: to be captured at execution.

## Results

### Execution and validity

- Scientific runner exit status: 0 (`status.json`); 15/15 arm/seed records and
  15 checkpoints were produced in 56:05 wall time.
- The surrounding tool transport surfaced exit 1 after completion, but the
  persisted wrapper status, `/usr/bin/time` report, complete JSON, and terminal
  event all independently record exit 0. This is a capture-transport anomaly,
  not a runner failure.
- Peak resident memory: 9,032,048 KiB; aggregate CPU utilization: 391%.
- Every record had applied KD mass exactly 1.0, and every two-step ePC trace
  was monotone. Both blocks received nonzero gradient credit in every record.
- Post-run complete suite: 424 passed, 1 skipped in 22.05 s.

Three-seed means:

| arm | A ppl | B AUC | B loss | A forgetting | retention | entropy rank | CKA |
|---|---:|---:|---:|---:|---:|---:|---:|
| ordinary ePC | 9.9702 | 1.9944 | 1.2481 | 4.8678 | .1044 | 12.2351 | .6525 |
| gated ePC | 10.2554 | 2.0265 | 1.2527 | 4.9516 | .1191 | 13.2783 | .6231 |
| gated + clarity | 10.2566 | 2.0266 | 1.2527 | 4.9527 | .1194 | 13.2820 | .6229 |
| full causal stack | 10.2564 | 2.0267 | 1.2528 | 4.9536 | .1194 | 13.2823 | .6229 |
| oracle support | 10.2368 | 2.0173 | 1.2498 | 4.9681 | .1182 | 13.3732 | .6200 |

Primary causal diagnostics:

| arm | finite commutator | off-support pre-gate leakage | credit blocks |
|---|---:|---:|---:|
| ordinary ePC | 9.9462e-7 | .8551 | 2.0 |
| gated ePC | 8.8243e-7 | .8572 | 2.0 |
| gated + clarity | 8.7762e-7 | .8572 | 2.0 |
| full causal stack | 8.7687e-7 | .8572 | 2.0 |
| oracle support | 8.1006e-7 | .3431 | 2.0 |

Mean corruption losses at p=.1/.3 were ordinary 2.6496/3.3074, gated
2.6618/3.2982, gated+clarity 2.6619/3.2979, full 2.6619/3.2979, and oracle
2.6611/3.2977. Per-state CKA/rank, block-skip losses, accuracies, perplexities,
curves, per-module influences, and seed-level values remain in
`artifacts/results.json`.

### Support-estimator behavior

- Seed 1729 estimated block 0 as A-only; seed 3253 estimated only head 0 of
  block 0 as A-only; seed 6421 estimated no A-only module. Consequently seed
  6421 ordinary/gated/clarity records were identical.
- Estimated off-support pre-gate leakage was 1.0 for seeds 1729 and 6421 and
  about .57 for seed 3253. The full stack did not reduce it.
- True-label oracle support reduced mean pre-gate leakage to .3431, but still
  worsened forgetting. Thus even the positive control did not show the
  predicted functional advantage on this tiny non-planted architecture.

### Frozen promotion gate

| check | threshold | observed | pass |
|---|---|---:|---|
| forgetting | full < ordinary | 4.9536 vs 4.8678 | no |
| Task-B loss | full <= 1.05x ordinary | 1.2528 <= 1.3105 | yes |
| commutator | full < ordinary | 8.7687e-7 < 9.9462e-7 | yes |
| leakage | full < ordinary | .8572 vs .8551 | no |
| entropy rank | full >= .90x ordinary | 13.2823 >= 11.0116 | yes |
| credit wavefront | full >= ordinary | 2.0 = 2.0 | yes |

`promotion_gate=false` (4/6 checks passed; the joint gate requires 6/6).

## Interpretation

This is a valid negative result for the implemented causal-coding stack.
Gating modestly raised representation rank and accuracy retention, and the full
stack reduced the direct commutator by about 11.8%, but it worsened mean
Task-A loss forgetting by about .0858, slightly worsened Task-B adaptation,
and did not reduce attempted off-support gradient mass. Clarity and commutator
regularization at the frozen coefficients were almost behaviorally inert beyond
gating.

The strongest limitation is identification. The estimated support partition
varied sharply by seed and was empty of protected modules in one seed. The
oracle was only an observational true-label intervention oracle on the same
two-block network, not a planted architectural ground truth; it reduced
leakage and commutator but did not improve forgetting. Therefore this run does
not establish that causal modularity is ineffective. It shows that this
small-fixture estimator/routing construction does not produce the theorem's
desired functional conditions, and it falsifies the prediction that the
implemented full arm approaches a useful oracle.

Do not promote or scale this configuration. A revisit should first use a
synthetic planted modular task where true `S_A/S_B` is known by construction
and verify support recovery, gate action, mixed-Hessian shrinkage, and a
functional oracle advantage before another Tiny Shakespeare run.

## Artifacts and hashes

- `artifacts/results.json`: `1601680e46390815a0c76e9ddb496094307e81874461768155a438c474bc003e`
- `command.sh`: `9facb9dfd396e8488dff629cd0f774ea2cd4318b1dcbc19a4f3c9553ceb6b4ec`
- `stdout.log`: `48423174fb8e2a51435d3af89d97bf1c3b52f1161f85ca2c5fae2b1ed9e6ae12`
- `stderr.log`: `63c510a3e537636c92d59bc78479bf2f18d0f12a7bd4a545f1518a863ceb5b33`
- checkpoint manifest: `checkpoint_hashes.sha256`, manifest SHA-256
  `14203fd36cd6d3e1dda291a1a6f6cd15c52b9b7c6b6229f06ba735028a1ec49c`
- post-run test log SHA-256:
  `46e97611ba0d35868018225723f1e88806e8f403d58384b10bdc4ee580ac0ae6`

## Reproduction

Review and run `command.sh` in the captured environment. The command points to
the immutable experiment path and implementation commit `4b0a425`.
