# Run 20260820T075200Z: P1 terminal integrity checkpoint r40

- Project: `hdc-cgcct-transformers`
- Started: `2026-08-20T07:52:00Z`
- Finished: `2026-08-20T07:52:00Z`
- Status: `succeeded; P1 remains terminal as instrument_failed`
- Local or remote: local CPU, read-only use of existing scientific artifacts
- Nested source commit: `b34b6f1f39a344c6c16ed6a7578da883134d6847`

## Question

Does the terminal P1 record still reproduce identically?

## Integrity checks

- The complete nested suite passed: `31 passed in 3.82s`.
- `git status --short` and `git diff --check` were clean.
- The contract-v2 evaluator reproduced the recorded result byte-for-byte.
- Result SHA-256: `40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`.
- Classification: `instrument_failed`.

## Summary

All three worker priorities are already complete:

1. P1A full-grid metrics and calibration: complete since 2026-07-28. Payload
   SHA-256 `b7fabae33494ed090fe1cd73b85fff0ad3f36fe7f3c6f986ed1a30ab0197195b`.
2. P1B planted-PCFG six-layer causal decoder, manifest, residual/readout, and
   CPU smoke: complete since 2026-07-28 at nested commit `b4593f4`. 22 tests
   and two byte-identical smoke/manifest replays passed.
3. P1B three calibration seeds on GPU: complete since 2026-07-27/28. Seeds
   12011, 13121, 14251 ran on one 24-GiB RTX 3090 at USD 0.22/hour. All
   artifacts verified. Pod deleted.

The five confirmation seeds are also complete (2026-07-31), the contract-v2
repair is complete (2026-08-03), and P1 is terminal as `instrument_failed`.

No P0 replay, seed opening, criteria change, hyperparameter search, provider
query, remote resource, or paid work occurred in this checkpoint.
