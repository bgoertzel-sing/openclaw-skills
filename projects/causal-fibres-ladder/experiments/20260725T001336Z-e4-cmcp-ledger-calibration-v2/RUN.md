# Run 20260725T001336Z-e4-cmcp-ledger-calibration-v2

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T00:13:36Z`
- Finished: `2026-07-25T00:14:12Z`
- Status: `succeeded`
- Operator/agent: ZeroBot
- Local or remote: local CPU

## Question

Can a provenance-first CMCP conditional-information ledger suppress duplicate
and deterministically derived symbolic E4 constraint packets while preserving
useful independent repeated evidence on the confirmed text-like substrate?

## Inputs

- Repository branch: `agent/e1-guarded-homotopy`
- Base commit: `154e5cfb604ffeeca314b22429e34d26b490a61c`
- Configuration: `configs/e4_cmcp_ledger_calibration_v1.json`
- Seeds: `51001, 52103, 53209`
- Protocol: `docs/e4_cmcp_ledger_protocol.md`
- Supersedes operationally failed launch:
  `../20260725T001224Z-e4-cmcp-ledger-calibration/`

## Environment

Captured in `env.txt`; Git state in `git.txt`.

## Command

See `command.sh`.

## Results

- CMCP assigned total effective precision exactly `1.0` to exact duplicates
  and deterministic descendants, matching the oracle; naive accumulation
  assigned `2.0`.
- CMCP retained almost all independent repeated evidence: mean second-packet
  weight `0.998872`, versus `0` for direction-only and `1` for the oracle.
- After known-frame alignment, rotated evidence matched the independent case
  to numerical precision.
- Packet-order RMS was zero.
- Partial redundancy was imperfectly calibrated: mean second-packet weight
  `0.68153` versus the provisional oracle value `0.5`.
- Naive duplicate injection improved immediate task loss by about `0.01181`
  relative to CMCP/single.

Aggregate artifact SHA-256:
`aa205a1775976f2628de31a9a0df5a2afc67c4da352f19fd83a87f2f96f8d46c`.

## Interpretation

Calibration supported freezing exact idempotence, independent-evidence
utilization, coordinate alignment, order invariance, non-ceiling, and a
bounded immediate-loss-cost guard. It did not justify a tight partial-
redundancy precision threshold or a predictive-performance advantage claim.

## Reproduction

Run `command.sh` from the recorded repository and environment.

## Follow-up

Run the frozen five-seed confirmation without changing code or thresholds.
