# Run 20260725T031257Z-e4-cmcp-biased-injection-smoke: e4-cmcp-biased-injection-smoke

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T03:12:57Z`
- Finished: `2026-07-25T03:13:03Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can the current CMCP Schur-complement score detect and downweight a
systematically one-bit-flipped packet as information-redundant, independently
of provenance deduplication?

## Hypothesis or expected behavior

The biased packet was expected to have a near-zero raw conditional-information
ratio, while naive accumulation would amplify its bias.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed: `61001`
- Biased factor index: `0`
- Raw artifact:
  `../../artifacts/e4-cmcp-biased-injection-smoke-v1.json`

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

At episode 6:

| Arm | Effective precision | Bias amplification |
|---|---:|---:|
| naive | 15.000 | 6.258 |
| CMCP | 8.188 | 0.000 |
| direction-only | 1.000 | 0.000 |
| oracle | 7.500 | 0.000 |

All model hashes were unchanged. The raw conditional-information ratio of the
biased packet against its clean source was `0.946071`, not near zero.

## Interpretation

**Observed:** CMCP assigned the biased packets zero weight and naive amplified
the measured bias. However, CMCP removed them before Schur residualization
because they reused the clean packets' `innovation_id`.

**Decision:** This smoke falsifies the proposed Schur-complement mechanism
test. It validates provenance deduplication, not score-space detection of
systematic bias. The reserved confirmation seeds remain sealed.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Redesign the score representation or construct a genuinely score-collinear
but provenance-distinct packet fixture. Require the raw conditional-information
ratio—not an innovation-ID shortcut—to pass before any scientific campaign.
