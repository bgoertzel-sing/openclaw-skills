# CAROM E2/E3 compiled recurrence v1

- Status: completed
- Project: `carom`
- Started: 2026-07-25T17:36:39Z
- Execution: local CPU preflight; remote GPU only after a measured cost plan

## Question

Can whole-graph PyTorch compilation remove Python dispatch from the frozen
70-step CAROM itinerant recurrence without changing its scientific semantics,
seeded stochastic trajectory, gradients, optimizer update, or deterministic
evaluation?

## Frozen implementation contract

The recurrent state update remains sequential because workspace, activity, and
fatigue at step `t+1` depend nonlinearly on step `t`. No time-axis batching,
closed-form replacement, reduced controller depth, reduced model size, changed
noise source, or altered loss is allowed.

The runner may compile one unchanged recurrent transition with `torch.compile`
and reuse it for all 70 sequential calls. Whole-model compilation is not the
implementation target because it unrolls all transitions into one graph.
Before a GPU campaign it must demonstrate, from identical state and RNG:

1. eager and compiled evaluation logits, activities, and diagnostics agree
   within a predeclared floating-point tolerance;
2. eager and compiled training loss and parameter gradients agree;
3. one complete AdamW/OneCycleLR optimizer step agrees;
4. repeated compiled evaluation is exactly deterministic;
5. seeded stochastic training replay is repeatable within each execution mode;
6. the compiled full-shape throughput estimate fits a newly approved remote
   time/cost bound.

Compilation overhead must be reported separately from steady-state throughput.
The local float32 calibration tolerances, frozen before a GPU comparison, are:
maximum absolute error at most `1e-5` for logits, activities, and post-AdamW
parameters, and at most `1e-6` for gradients.

## Initial compiler disposition

A tiny three-step Inductor benchmark passed and measured 3.45x steady-state
CPU speedup after 5.88 seconds compilation. A subsequent 70-step whole-model
probe was killed before emitting an artifact, consistent with compiler graph
explosion from unrolling the recurrence. No scientific result was produced.
The implementation therefore compiles one recurrent transition and reuses it;
this is a performance-seam correction, not a protocol change.

The full-width local CPU probe (`batch=2`, `d=64`, `K=16`, 70 controller
steps) subsequently measured 2.37x steady-state speedup. Maximum eager versus
Inductor errors were `7.45e-8` logits, `5.36e-7` activity, `2.98e-8`
gradients, and `3.86e-6` post-AdamW parameters, all within the frozen float32
tolerances. This is local compiler calibration, not yet a CUDA equivalence or
throughput result.

## Local verification

- Focused E0--E3 and compiler tests: `12 passed`.
- Complete CAROM `test_*.py` suite: `33 passed`, with one existing scheduler
  ordering warning in the v4 regression fixture.
- Five-arm compiled end-to-end smoke: complete for seed 7; scientific
  evaluation ran on the eager reference recurrence and repeated exactly.
- Implementation commit: `4d24f77` (`Compile CAROM E2 E3 recurrent
  transition`).
- Full-width CPU Inductor artifact:
  `artifacts/cpu-fullshape-step-compile-benchmark-v2.json`.
- Repository-local staged diff whitespace check: passed before commit.

The bounded CUDA calibration and campaign proposal is recorded in
`REMOTE_JOB.md`; no remote resource has been provisioned under this run.

## CUDA run disposition

The approved H100 run passed the CUDA equivalence gate and measured 3.50x
steady-state speedup. Its full campaign nevertheless exceeded the real
wall-clock projection because the five-arm runner incurred more per-arm work
than the single-step benchmark represented. At 2h28, 16 of 25 arms were
complete; the remaining work projected beyond the 3-hour/USD 9 hard bound.
The runner was interrupted, partial artifacts were retrieved and hash-matched,
and the pod was terminated. This preserves the budget but leaves E2/E3
scientifically incomplete. See `REMOTE_JOB.md` for exact values and artifact
hash.

## Completion and formal scientific disposition

A second bounded completion run supplied all 25 arm/seed results in
`artifacts/remote/campaign-final/`. The aggregation was recomputed from the
2,048 per-example records under `metrics.rows` in every result, rather than
trusting optional top-level or cached aggregate fields. The observed
seed-averaged endpoints are:

| arm | slot accuracy | exact workspace | revisit fraction | terminal-trapping fraction | integrated activity mass |
|---|---:|---:|---:|---:|---:|
| e2_full | 0.9062 | 0.7484 | 0.6075 | 0.9162 | 24.4957 |
| e2_no_workspace | 0.8503 | 0.6873 | 0.0000 | 1.0000 | 61.9095 |
| e2_no_command | 0.7809 | 0.6355 | 0.4729 | 0.8862 | 28.1601 |
| e2_no_position | 0.8061 | 0.6644 | 0.5355 | 0.8313 | 39.3800 |
| e3_generic_regularized | 0.8789 | 0.7238 | 0.6013 | 0.9195 | 24.5001 |

The numerical gates were already prospectively frozen in
`experiments/20260724T194500Z-e2-e3-gpu-r1/RUN.md` before r2 provisioning:

- E2 full must exceed each ablation by at least 0.010 mean slot accuracy and
  be nonnegative on at least four of five paired seeds.
- E3 may lose at most 0.010 slot accuracy versus E2 full, may not increase
  terminal-trapping or revisit fractions, and may use at most 1.10 times E2
  full's integrated activity mass.

E2 **passes**. Its mean paired advantages over no-workspace, no-command, and
no-position are respectively 0.05583 (4/5 nonnegative), 0.12529 (4/5), and
0.10008 (5/5). E3 **fails**: its accuracy loss is 0.02725, beyond the 0.010
limit, and terminal trapping rises from 0.91621 to 0.91953. Revisit fraction
and activity mass pass their safety checks. The joint E2/E3 gate therefore
**fails and E4 remains closed**. A promotable E3 would need to recover at
least 0.01725 mean slot accuracy while eliminating its 0.00332
terminal-trapping increase, without violating revisit or exposure limits.

Reproducible outputs are in `artifacts/aggregate/`. Command:

```bash
python3 aggregate_e2_e3.py \
  ../../experiments/20260725T173639Z-e2-e3-compiled-recurrence-v1/artifacts/remote/campaign-final \
  --output-dir ../../experiments/20260725T173639Z-e2-e3-compiled-recurrence-v1/artifacts/aggregate
```

## Relevance of research rules

- Rule 1: compilation is an estimator/execution change and receives explicit
  semantic equivalence tests.
- Rule 2: the recurrence-preservation contract above precedes code changes.
- Rule 3: use PyTorch's existing compiler rather than hand-translating the
  nonlinear recurrence.
- Rule 5: preserve exact commands, timing, environment, and artifacts.
- Rule 7: expose compilation as an optional runner seam; eager remains the
  reference implementation.

## Acceptance

Local focused and existing E0--E3 tests pass; an eager/compiled equivalence
artifact records tolerances and maximum errors; a full-shape performance probe
shows enough speedup to define a bounded GPU relaunch. If not, the campaign
remains closed.
