# Run 20260724T221117Z-e4-non-label-equivalent-confirmation

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T22:11:17Z`
- Finished: `2026-07-24T22:12:00Z`
- Status: `succeeded with one frozen auxiliary threshold failed`
- Local or remote: `local CPU`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the calibration-selected, non-label-equivalent three-factor source clear
the frozen `G_loss > 0.20` deployment gate on five disjoint seeds?

## Frozen acceptance

Thresholds were committed before this run at Git commit
`90be2a9cf59d2d557932d4349f520124f6944058`:

- Primary: `partial3_123`, leaving exactly two labels possible.
- Mean defined-seed CS `G_loss > 0.20`.
- At least three confirmation seeds individually exceed `0.20`.
- Mean CS task accuracy at least `0.95`.
- Every measured source admits at least two labels.

All 28 conditions are measured for family/noise interpretation, but only the
frozen primary decides the deployment gate.

## Inputs and provenance

- Calibration:
  `../20260724T220707Z-e4-non-label-equivalent-calibration/`
- Confirmation seeds: `27449,28559,29669,30781,31891`
- Calibration seeds: `24109,25219,26339` (disjoint)
- Git branch: `agent/e1-guarded-homotopy`
- Git commit: `90be2a9cf59d2d557932d4349f520124f6944058`
- Pre-existing untracked files remain untouched.
- Python `3.10.12`; Torch `2.12.1+cpu`; Intel i7-1165G7.
- Focused tests before freeze: `12 passed`.

## Exact command

See `command.sh`. Output, error, timing, exit status, and raw JSON are captured
in this directory.

## Results

The command exited `0` in `23.21s` wall time with peak RSS `296536 KiB`.
All five per-seed artifacts and the aggregate are complete.

### Frozen primary

| Metric | FF | TC diagnostic | `partial3_123` |
|---|---:|---:|---:|
| CS task loss | 0.87155 ± 0.24080 | 0.85702 ± 0.23698 | 0.81786 ± 0.22026 |
| CS task accuracy | 0.82188 ± 0.22395 | 0.83906 ± 0.21513 | 0.88906 ± 0.13991 |

Four seeds had a defined denominator and all four individually cleared the
`G>0.20` deployment gate: `1.75881, 5.29518, 3.50062, 4.41861`; mean
`G=3.74330 ± 1.51233`. Seed `28559` had perfect FF/TC/SC accuracy and a
`|TC_loss-FF_loss|=0.009585`, below the frozen `0.01` denominator floor, so
its raw metrics remain present but its G is undefined.

Frozen checks:

- C1 primary mean `G>0.20`: **pass** (`3.74330`).
- C2 at least 3 seed passes: **pass** (`4/4` defined seeds).
- C3 mean CS task accuracy at least `0.95`: **fail** (`0.88906`).
- C4 all sources admit at least two labels: **pass** (minimum `2`).

Thus the user-specified deployment headroom gate passes strongly, while the
additional frozen absolute-accuracy auxiliary does not. The failure is not
retuned away. Confirmation FF accuracy was unusually heterogeneous, ranging
from `0.4531` to `1.0`; the primary raised the low seed from `0.4531` to
`0.6641` and raised mean accuracy by `0.06719`.

### Constraint-family results

- Partial-factor mean G scales nearly linearly with width:
  one factor `1.29059`, two factors `2.58537`, three factors `3.88416`.
- Best parity (`parity_03`) leaves 8 labels possible:
  `G=3.65700`, CS accuracy `0.90938`.
- Best implication (`implication_2_1`) leaves 12 labels possible:
  `G=0.44743`, CS accuracy `0.82188`.
- Three-factor noisy curve (realized flip fractions in raw JSON):
  `p=0: G=2.78810`, `p=0.1: G=1.34936`,
  `p=0.2: G=0.11016`, `p=0.5: G=-3.44628`.
  The material gate survives 10% noise, falls below it at 20%, and becomes
  harmful at chance-level noise.
- Every one of the 28 conditions passed the non-label-equivalence audit on
  every seed.

## Interpretation

Non-label-equivalent symbolic information is sufficient for material direct-
logit recovery on this substrate. Label-equivalent four-factor information is
not required: a frozen three-factor source leaving two labels possible and a
parity source leaving eight labels possible both exceed `G=0.20`; even a
single implication leaving twelve labels possible exceeds it.

This confirms the Stage-4 inversion as an information-sink result. It does
not by itself supply a real deployment-time upstream extractor: these
messages are generated from known synthetic factors. Source provenance and
availability remain a separate engineering/scientific requirement.

## Verification and artifacts

- Focused preflight: `12 passed`.
- Full suite in project venv with `PYTHONPATH=src:.`: `197 passed in 17.73s`.
- A system-Python full-suite attempt failed collection because it lacked
  project-only `causal_fibres` and repository-root imports; no assertions ran.
- Aggregate: `artifacts/result.json`
- Aggregate SHA-256:
  `6793c744ddc23bd5657ba580e2ff0a19f63c9454703e27e85a4f477da9ad6f06`
- Raw per-seed JSON, stdout, stderr, and `/usr/bin/time -v` output are retained.
