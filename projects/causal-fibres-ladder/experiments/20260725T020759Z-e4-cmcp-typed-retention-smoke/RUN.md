# E4/CMCP Typed Retention Smoke

- Project: `causal-fibres-ladder`
- Status: succeeded operationally; scientific protocol superseded
- Started: 2026-07-25T02:07:59Z
- Local or remote: local CPU
- Protocol: `docs/e4_cmcp_typed_retention_protocol.md`
- Config: `configs/e4_cmcp_typed_retention_calibration_v1.json`
- Seed: `61001` (calibration)

## Question

Does the typed store fail closed on identity errors, and does the first
parameter-learning run produce finite, nontrivial retention/plasticity
differences under exactly matched updates?

## Acceptance

- 20 focused CMCP/store tests pass.
- All arms share one initial model hash and equal optimizer-update counts.
- Cohort and example identities are recorded.
- All reported losses/calibration values are finite.
- Results are exploratory calibration evidence only.

## Command

See `command.sh`, frozen before execution.

## Result

All 20 focused tests passed and every runtime invariant held. The original
four-bit reversal was too severe: CMCP and oracle learned Task B better than
naive, but both lost all Task-A exact accuracy. This smoke selected a
one-constrained-factor reversal for calibration; it is not scientific evidence
for or against retention.
