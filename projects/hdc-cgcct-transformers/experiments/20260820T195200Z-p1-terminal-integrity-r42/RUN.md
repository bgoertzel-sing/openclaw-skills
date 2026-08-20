# P1 terminal integrity replay r42

- Timestamp: `2026-08-20T19:52Z` (2026-08-20 12:52 PDT)
- Nested commit: `b34b6f1`
- Worker priorities: P1A full-grid, P1B CPU smoke, P1B three-seed calibration — all complete
- P1 status: terminal `instrument_failed`

## Actions

1. Ran `python3 -m pytest -v`: **31 passed** in 4.03s.
2. Ran `evaluate_p1g2_contract_v2.py` with the frozen P1A payload, frozen criteria, five confirmation artifacts, and contract-v2 JSON.
3. `git status --short`: clean. `git diff --check`: no errors.

## Result

- Classification: `instrument_failed`
- Replay SHA-256: `40a81f56e18ecedc1ebdde06d63c3c428d1d3ad857f893826274ccb42165c6eb`
- Matches recorded hash: yes (byte-for-byte identical)

## Constraints honored

- No P0-v1 rerun.
- No seed opening.
- No criteria change.
- No hyperparameter search.
- No provider query.
- No remote resource provisioned.
- No paid compute.
