# Run 20260724T225008Z-e4-symbolic-extractor-confirmation

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T22:50:08Z`
- Finished: `2026-07-24T22:51:24Z`
- Status: `succeeded`
- Local or remote: `local CPU`
- Working directory:
  `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the calibration-selected input-derived subset constraint at 90% requested
extraction accuracy clear the frozen `G_loss > 0.20` deployment gate on five
disjoint seeds?

## Frozen acceptance

Frozen and committed at `5377d1ec9b369c239e87adcf9dfa94af9764fbb7`
before any reserved seed was executed:

- Primary: `subset3_123_acc0p9`, leaving exactly two labels possible.
- Mean defined-seed CS `G_loss > 0.20`.
- At least three defined confirmation seeds individually exceed `0.20`.
- Every emitted source leaves at least two labels.
- Every provenance audit passes.

CS task accuracy and all other accuracy/source conditions are reported but do
not decide the frozen gate.

## Inputs and provenance

- Calibration:
  `../20260724T224751Z-e4-symbolic-extractor-calibration/`.
- Confirmation seeds: `36341,37447,38557,39671,40787`.
- Calibration seeds: `33013,34123,35227` (disjoint).
- Branch: `agent/e1-guarded-homotopy`.
- Git commit: `5377d1ec9b369c239e87adcf9dfa94af9764fbb7`.
- Exact command: `command.sh`.

## Results

- Exit status: `0`; all five per-seed artifacts and aggregate are complete.
- All four frozen checks passed.
- Primary mean defined-seed CS task-loss `G=2.32074 ± 0.87142`; the three
  defined per-seed values were `3.31286, 1.97012, 1.67924`, all above `0.20`.
  Seeds `38557` and `39671` had `|TC_loss-FF_loss|<0.01`, so their raw
  metrics remain but G is undefined under the frozen denominator rule.
- Mean primary CS task accuracy was `0.96094`, versus FF `0.94219` and
  diagnostic TC `0.94375`.
- Every input-derived source remained non-label-equivalent; the primary left
  exactly two labels possible.
- Every provenance audit passed. Clean readings matched ground truth on every
  run, and ground truth was not used in constraint construction.
- Primary subset curve:
  `p=1.0: G=3.86702`; `0.95: 3.19325`; `0.9: 2.32074`;
  `0.8: 1.28460`; `0.7: -0.98495`.
- Realized CS extraction accuracies were `1.0000, 0.9570, 0.9039, 0.8188,
  0.7016`.
- Aggregate: `artifacts/result.json`, SHA-256
  `bacd4a60bf2b5b4688dfed324ab87f8446d5d9cb317bc8d1ec20c8e2349f0c4b`.
- Focused tests: `17 passed`. Full suite from the repository root:
  `203 passed in 16.76s`; compileall and `git diff --check` passed.
- A first full-suite invocation from the workspace root produced `201 passed,
  2 failed` because two tests intentionally resolve repository-relative
  `configs/` and `PYTHONPATH=src`; rerunning from the repository root passed.

## Interpretation

The input-derived 90%-accuracy primary decisively clears the material
deployment gate and retains `60.0%` of its same-seed clean extractor G. The
clean input result (`G=3.8670`) is close to the prior known-factor diagnostic
(`G=3.7433`), with different seed cohorts preventing a paired comparison.
Noise is consequential: the subset remains material at 80%, but all tested
relations are harmful by 70% mean extraction accuracy.

## Reproduction

Run `command.sh` in the recorded project environment after reviewing it.
