# Run 20260820T075200Z-p1-terminal-integrity-r40

- Project: `hdc-cgcct-transformers`
- Started: `2026-08-20T07:52:00Z`
- Status: `succeeded`
- Local or remote: `local`

## Question

Does the completed P1 implementation at nested commit `b34b6f1` still pass
its complete local suite and reproduce the frozen contract-v2 interpretation
without reopening P0, criteria, seeds, or remote work?

## Results

- Exit status: 0
- Test result: `31 passed` (3.82s)
- Recorded result SHA-256 (raw file bytes of stored result-v2.json):
  `40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`
- Regenerated replay JSON content: identical to stored result-v2.json
- Classification: `instrument_failed`

## Interpretation

The scheduled payload is stale. All three priorities listed in the current
worker directive are already complete:

1. **P1A full-grid metrics and calibration** — completed 2026-07-28 at nested
   commit `e4e1d65`. Payload SHA-256
   `b7fabae33494ed090fe1cd73b85fff0ad3f36fe7f3c6f986ed1a30ab0197195b`.
   60/60 F0/F1 curves interior; 31/60 missed the frozen Spearman 0.90
   monotonicity threshold. Calibration evidence, not a confirmation verdict.

2. **P1B planted-PCFG six-layer causal decoder, manifest, residual/readout,
   and CPU smoke** — completed at nested commit `b4593f4`; 22 tests passed.
   Extended to full calibration runner at `8dad854`; 26 tests passed including
   byte-identical replay and confirmation-seed rejection.

3. **P1B three calibration seeds on GPU** — completed on one Community RTX
   3090 at USD 0.22/hour. All raw artifacts verified locally; criteria frozen
   in `artifacts/criteria.json` before any confirmation seed was opened. Pod
   `qy0rbiqrd3xvbf` deleted and provider absence confirmed.

The five-seed confirmation subsequently completed on a Secure RTX 4090; the
post-hoc contract-v2 evaluator at `b34b6f1` classifies P1-G2 as
`instrument_failed`. This result has now been reproduced identically 40
times.

P0-v1 was not rerun. No P0 run, seed opening, criterion or hyperparameter
change, provider query, provisioning, remote resource, or paid compute
occurred.

## Follow-up

Do not reopen P1 or provision compute. Further scientific work requires a new,
explicitly authorized programme beyond the terminal `instrument_failed`
result.
