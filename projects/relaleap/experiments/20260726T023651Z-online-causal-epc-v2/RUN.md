# Run 20260726T023651Z-online-causal-epc-v2: online-causal-epc-v2

- Project: `relaleap`
- Started: `2026-07-26T02:36:51Z`
- Finished: `2026-07-26T02:37:02Z`
- Status: `complete; Phase 0 failed closed`
- Local or remote: `local`
- Working directory: `projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1-causal-coding`

## Question

Can a teacher-planted, overlapping-vocabulary two-path fixture provide
identifiable support, controlled nonzero cross-task curvature, reliably
load-bearing paths, and an oracle retention advantage?

## Hypothesis or expected behavior

The 90/10 task-conditioned path mixture should keep all task/module Hessian
interactions positive while making block 0 A-dominant and block 1 B-dominant.
All six frozen Phase 0 gates must pass before Shakespeare is permitted.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seeds: `1729, 3253, 6421`
- Arms: `ordinary, ratio, multi, full, oracle`
- Updates: 150 Task-A plus 150 Task-B updates per arm and seed
- Data: deterministic synthetic token draws from vocabulary `0..11`; A-heavy,
  shared, and B-heavy bands overlap in both tasks.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

Focused tests passed 6/6. The full repository suite passed 430 with 1 skipped.

| Gate | Observation | Pass |
|---|---|---:|
| support recovery | AUC 1.0 in every seed | yes |
| oracle gate specificity | block 0 protected and block 1 unprotected | yes |
| nonzero positive mixed Hessian | block 0 negative in 2/3; block 1 negative in 3/3 | no |
| >=10% protected-trace shrinkage | signed criterion fails when baseline is negative | no |
| load bearing and cross-effect | dominant effects pass; A loss change from block-1 zeroing is -0.056 to -0.071 nat | no |
| oracle advantage | mean forgetting .1172 vs .2935 ordinary | yes |

Mean final Task-B losses were `.0135` ordinary and `.0157` oracle. Mean final
Task-A losses were `.3225` ordinary and `.1462` oracle.

## Interpretation

**Observation:** Both tasks produced gradients through both blocks; support
recovery, gate action, dominant own-task ablations, and oracle retention all
worked. Mixed-Hessian estimates were nonzero in magnitude, fixing the exact
architectural-zero defect, but were not positive for every module and seed.
The minority block's Task-A ablation effect exceeded the frozen absolute
cross-effect tolerance.

**Inference:** The redesign creates real interference and useful planted
specialization, but does not satisfy the stated positive signed-curvature and
selective-ablation conditions. In particular, nonzero cross-path dependence
does not imply positive `tr(H_A H_B)`.

**Hypothesis:** A future positive control needs either a construction whose
per-module task Hessians are provably co-positive, or a preregistered
sign-insensitive curvature-overlap diagnostic. That change must not be tuned
on these seeds.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Stop. Do not run Shakespeare. Treat these seeds as calibration evidence if a
third fixture is designed, and freeze untouched confirmation seeds first.

## Hashes

- `artifacts/results.json`:
  `1869f187e86bd42d0cc2c926e23898f81eeafbc40ccbf5163dcca0630eb886e7`
- `command.sh`:
  `0314f5cd296a5052c0ca6b8b1c051a600c7f087b7f9d793bf83c0ee7454c763e`
