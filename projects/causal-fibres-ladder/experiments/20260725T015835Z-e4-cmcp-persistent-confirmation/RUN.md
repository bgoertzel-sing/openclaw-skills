# Run 20260725T015835Z-e4-cmcp-persistent-confirmation: e4-cmcp-persistent-confirmation

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T01:58:35Z`
- Finished: `2026-07-25T01:59:13Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Do the persistent CMCP precision and calibration effects reproduce on five
sealed seeds under gates frozen after the corrected three-seed calibration?

## Hypothesis or expected behavior

CMCP should remain within `1.25` effective-precision units of the oracle,
improve mean ECE and Brier relative to naive counting, and lose no more than
`0.02` accuracy to naive on any seed.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Confirmation seeds: `64311, 65439, 66543, 67649, 68757`.
- Frozen thresholds:
  `configs/e4_cmcp_persistent_confirmation_frozen_v1.json`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

All nine frozen checks passed. At episode 8, CMCP versus naive mean task
accuracy was `0.83281` versus `0.74844`; mean task loss was `0.43899` versus
`0.59725`; mean ECE was `0.07797` versus `0.12309`; and mean multiclass Brier
was `0.22596` versus `0.32489`. Effective precision was CMCP `8.89433`, oracle
`9.0`, naive `26.0`, and direction-only `1.0`. CMCP weights were invariant to
within-episode presentation order and all model hashes remained unchanged.

## Interpretation

**Observed:** On this stable-cohort protocol, CMCP prevents duplicate
precision inflation, closely matches the oracle accounting total, and
outperforms naive accumulation on mean loss, accuracy, ECE, and Brier.

**Inferred:** Exactly-once/conditional-information accounting has a practical
same-cohort calibration benefit here, not merely an algebraic idempotence
property.

**Boundary:** No model parameters change. The result does not establish
continual-learning retention, forgetting prevention, learned mechanism
alignment, or a deployable MORK store.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Implement cohort/example identities in a typed persistent store before testing
parameter-learning or cross-episode retention.
