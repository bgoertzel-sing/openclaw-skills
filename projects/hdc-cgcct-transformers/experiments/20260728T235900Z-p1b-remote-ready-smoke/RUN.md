# P1B remote-ready CPU smoke

- Date: 2026-07-28T23:59Z
- Nested repository commit: `8dad854`
- Scope: final local calibration-runner gate; no remote resource used

The reduced deterministic replay covers the frozen six-layer decoder, one
update, residual extraction, per-H linear-readout and oracle metrics,
independent logistic representation probes, deterministically shuffled-label
probes, target/prediction hashes, planted/independent coherence diagnostics,
peak-device-memory reporting, raw-array hashing, artifact verification, and
confirmation-seed rejection.

Verification:

```text
python3 -m pytest -q
26 passed in 4.20s
python3 -m py_compile src/hdc_cgcct/p1b_calibration.py scripts/run_p1b_calibration.py
git diff --check
```

The replay is reduced and explicitly gate-ineligible. It validates the
execution and artifact path without opening any confirmation seed.
