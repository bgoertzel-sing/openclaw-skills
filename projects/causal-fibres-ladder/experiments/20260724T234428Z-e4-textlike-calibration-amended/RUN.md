# Run 20260724T234428Z-e4-textlike-calibration-amended

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T23:44:28Z`
- Finished: `2026-07-24T23:45:10Z`
- Status: `inconclusive denominator`
- Local or remote: `local CPU`

## Question

After rejecting the inherited homotopy/KD training recipe for failing the
non-ceiling lower bound, does a 75-update supervised six-block text student
reach the specified regime, and which eligible subset condition should be
frozen for confirmation?

## Inputs

- Protocol: `docs/e4_textlike_external_validity_protocol.md`.
- Amended config: `configs/e4_textlike_bridge_calibration_v1.json`.
- Calibration seeds: `42013,43117,44221`.
- Reserved untouched confirmation seeds:
  `45329,46433,47543,48649,49757`.
- Exact command: `command.sh`.
- Focused validation before run: `15 passed`; compileall and
  `git diff --check` passed.

## Expected behavior

Mean CS FF task accuracy should lie in `[0.70,0.92]`, preferably near
`0.85--0.90`. Surface-only extraction should remain near 96%. Rank subset
conditions at mean extraction fidelity no greater than 92% by mean defined CS
G and freeze the winner before confirmation.

## Results

- Exit status: `0`.
- Raw artifacts: `artifacts/`.

## Interpretation

The amended student met the target: mean CS FF accuracy was `85.94%`, with
seed values `89.06%,82.03%,86.72%`; surface extraction fidelity was `96.09%`.
However, hidden-state TC improved loss by only `0.00810`, below the frozen
`0.01` denominator floor, leaving all G values undefined. The student was
accepted, but the run could not select or test a G primary. A channel-matched
direct-logit TC diagnostic was therefore calibrated before confirmation.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.
