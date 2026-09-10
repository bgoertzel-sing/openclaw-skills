# Run 20260724T224751Z-e4-symbolic-extractor-calibration

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T22:47:51Z`
- Finished: `2026-07-24T22:49:20Z`
- Status: `succeeded`
- Local or remote: `local CPU`
- Working directory:
  `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Which input-derived relational constraint at fixed 90% requested extraction
accuracy should be frozen for disjoint confirmation, and how does recovery
degrade over requested accuracy `1.0, 0.95, 0.9, 0.8, 0.7`?

## Hypothesis or expected behavior

Clean one-hot decoding should exactly match the oracle factor reading. Noise
should reduce recovery, but at least one `p=0.9` subset/parity/implication
condition is expected to retain `G>0.20`.

## Inputs and provenance

- Protocol: `docs/e4_symbolic_extractor_protocol.md`.
- Branch: `agent/e1-guarded-homotopy`.
- Base commit: `90be2a9cf59d2d557932d4349f520124f6944058`.
- Dirty state consists of this new implementation plus pre-existing untracked
  artifacts recorded in repository status.
- Calibration seeds: `33013,34123,35227`.
- Reserved confirmation seeds: `36341,37447,38557,39671,40787`.
- Exact command: `command.sh`.
- Focused preflight: `17 passed in 1.31s`.

## Results

- Exit status: `0`; all three per-seed artifacts and aggregate are complete.
- Every per-run provenance audit passed. Clean block decoding exactly matched
  the grammar factors, and factors were used only after constraint construction
  to measure realized extraction fidelity.
- At fixed `p=0.9`, calibration mean defined-seed CS task-loss G was:
  `subset3_123=1.79293`, `parity_03=1.42430`,
  `implication_2_1=0.47118`.
- The selected `subset3_123_acc0p9` primary had three defined denominators,
  per-seed G `2.68211, 1.91993, 0.77675`, mean CS accuracy `0.86719`,
  and left exactly two classes possible.
- The selected family's accuracy curve was:
  `p=1.0: G=3.07079`; `0.95: 2.54088`; `0.9: 1.79293`;
  `0.8: 0.49262`; `0.7: -1.35815`.
- Realized CS extraction accuracies were `1.0000, 0.9512, 0.9063, 0.8027,
  0.6810`, respectively.
- Aggregate: `artifacts/result.json`, SHA-256
  `825ef8a967c370c4c47917b526dca04a3b4312e65576a63c058717c5de7fd261`.

## Interpretation

All three relational forms retain material recovery at 90% requested
extraction accuracy in calibration. The subset constraint ranks first and is
frozen as the confirmation primary. Recovery declines with noise and becomes
harmful at 70% for this subset source. These are calibration observations, not
the final deployment disposition.

## Reproduction

Run `command.sh` in the recorded project environment after reviewing it.
