# Run 20260725T001900Z-e4-cmcp-ledger-confirmation

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T00:19:00Z`
- Finished: `2026-07-25T00:20:04Z`
- Status: `succeeded`
- Operator/agent: ZeroBot
- Local or remote: local CPU
- Frozen code commit: `9ed922d`

## Question

Do the E4/CMCP evidence-ledger contracts reproduce on five disjoint
confirmation seeds under thresholds frozen after calibration?

## Frozen acceptance

- Duplicate and deterministic-descendant effective-precision absolute error
  at most `1e-8`.
- Independent-repeat CMCP task loss no worse than direction-only.
- Rotated-frame aligned weight discrepancy at most `1e-6`.
- Presentation-order RMS logit discrepancy at most `1e-7`.
- Mean redundant-stream CMCP task-loss penalty versus naive at most `0.025`.
- Mean CS FF accuracy in `[0.70,0.90]`.

The primary interpretation concerns evidence multiplicity. Calibration showed
that naive duplicate injection improves one-shot loss slightly, so this run
does not test long-horizon overconfidence or forgetting.

## Inputs

- Calibration:
  `../20260725T001336Z-e4-cmcp-ledger-calibration-v2/`
- Calibration result SHA-256:
  `aa205a1775976f2628de31a9a0df5a2afc67c4da352f19fd83a87f2f96f8d46c`
- Calibration seeds: `51001,52103,53209`
- Confirmation seeds: `54311,55439,56543,57649,58757`
- Thresholds:
  `configs/e4_cmcp_ledger_confirmation_frozen_v1.json`

## Environment

Captured in `env.txt`; Git state in `git.txt`.

## Command

See `command.sh`.

## Results

All seven frozen checks passed.

- Non-ceiling audit: feedforward CS accuracy was `0.8500`.
- Exact duplicates and deterministic descendants: CMCP effective precision
  was exactly `1.0` on all five seeds; naive accumulation was `2.0`.
- Independent repeat: CMCP retained mean second-packet weight `0.997862`.
  Its task loss was `0.432087`, better than direction-only novelty at
  `0.442489` and nearly equal to the oracle at `0.432057`.
- Rotated frame: aligned CMCP weight differed from the unrotated independent
  case by only `1.24e-10`.
- Packet ordering: RMS difference was zero.
- Partial redundancy: CMCP assigned mean second-packet weight `0.657531`
  versus oracle `0.5`; mean absolute precision error was `0.217595`.
- Redundant duplicate packets: CMCP task loss was `0.442489` versus
  `0.434244` for naive double counting, within the frozen `0.025` cost guard.
  CMCP had slightly lower ECE (`0.06321` versus `0.07054`).

Aggregate artifact SHA-256:
`9577a05d5e7b634f5e725d17e156963f7bbf539d3db83022c9c097020a9de6bc`.

Runtime was `33.97s`; peak RSS was `298572 KiB`; exit status was `0`.

## Interpretation

**Observed:** The CMCP ledger provides exact idempotence for duplicates and
deterministic descendants, preserves useful independent evidence that a
direction-only novelty rule discards, is equivariant under the tested known
rotation, and is order invariant.

**Boundary:** This establishes evidence-accounting behavior, not superior
one-shot prediction. Naive double counting slightly improved immediate loss,
and the partial-redundancy estimator remains noisy and positively biased.
Persistent overconfidence, interference, and forgetting were not tested.

## Reproduction

Run `command.sh` from the frozen repository state.

## Follow-up

Run a persistent-ledger stress test with correlated duplicate bursts across
episodes, measuring calibration, effective precision, order sensitivity, and
retention. If positive, map the ledger and provenance graph into MORK before
implementing the typed logit adapter.
