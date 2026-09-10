# Run 20260724T234938Z-e4-textlike-confirmation

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T23:49:38Z`
- Finished: `2026-07-24T23:50:10Z`
- Status: `succeeded`
- Local or remote: `local CPU`
- Frozen code commit: `154e5cfb604ffeeca314b22429e34d26b490a61c`

## Question

Does the natural-surface text-like subset extractor clear the frozen
channel-matched deployment gate on five disjoint seeds, and at what added
extraction noise does material recovery disappear?

## Frozen acceptance

- Primary: `subset3_123_noise0p0`.
- Mean defined-seed CS task-loss `G > 0.20`.
- At least three defined confirmation seeds individually exceed `0.20`.
- Every source leaves at least two labels possible.
- Every provenance audit passes.
- Mean CS FF task accuracy lies in `[0.70,0.92]`.

## Inputs

- Calibration:
  `../20260724T234609Z-e4-textlike-calibration-channel-matched/`.
- Calibration seeds: `42013,43117,44221`.
- Confirmation seeds: `45329,46433,47543,48649,49757`.
- Thresholds:
  `configs/e4_textlike_bridge_confirmation_frozen_v1.json`, committed before
  confirmation.
- Exact command: `command.sh`.

## Results

- Exit status: `0`.
- Raw per-seed JSON and aggregate: `artifacts/`.

## Interpretation

All five frozen checks passed. The primary confirmed mean CS
`G=0.30387 ± 0.08379`; all five per-seed values
(`0.28737,0.43280,0.31560,0.28270,0.20090`) exceeded `0.20`.
Extraction fidelity was `96.09%`; FF/SC task accuracy was
`81.56%/82.50%`; every constraint remained non-label-equivalent; and every
input-only provenance audit passed.

Mean G remained material at 5%, 10%, and 20% added errors
(`0.25694,0.20826,0.22517`) and fell below the gate at 30% (`0.15250`).
Realized extraction fidelity was `77.38%` at 20% errors and `68.32%` at 30%,
placing the observed floor between those levels. The 10%/20% nonmonotonicity
is treated as finite-sample variation.

The text-like bridge therefore preserves the Stage-4 deployment verdict with
less margin. Raw G is not directly comparable to the old `2.32074` because
this run uses a channel-matched direct-logit TC anchor.

Aggregate SHA-256:
`975df588d0b03e4f077f1dd8015dd9ae013998b7a74ebbb41250d542c12f4681`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.
