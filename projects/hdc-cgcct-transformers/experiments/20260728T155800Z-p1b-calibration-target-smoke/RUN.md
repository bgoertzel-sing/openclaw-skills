# P1B target-code/readout calibration smoke

- Date: 2026-07-28T15:58Z
- Nested repository commit: `7f46c5a48ee5420226823250b3affcabc108a7ec`
- Scope: CPU-local, reduced and scientifically gate-ineligible
- Remote resources: none

Implemented the frozen §6.7 P1B dimension guard, canonical atom namespace,
independent and planted path-composite feature codes, complete Eq.-4 frame
targets (including the distractor), atom/target/readout hashes, and a reduced
artifact/replay smoke through residual extraction and fresh per-arm ridge
readouts.

Verification:

```text
python3 -m pytest -q
24 passed

python3 scripts/run_p1b_calibration_smoke.py \
  --output artifacts/p1b-calibration-smoke-a.json
python3 scripts/run_p1b_calibration_smoke.py \
  --output artifacts/p1b-calibration-smoke-b.json
```

Both payload files are byte-identical with SHA-256
`b2a6ee25c6317b9c83f33acc5daa0c8fad144d0c7e4860f7ead0af385df719e8`.
The payload explicitly records `scientific_gate_eligible=false`.

This is material progress but does not clear remote precondition 3. The full
10,000-update/early-stop trainer, complete per-D/per-H metrics, representation
and shuffled-label controls, raw `.npy` manifest/index contract, and
calibration criteria freezer remain to be implemented and tested. No live
offer check or provisioning was attempted, and confirmation seeds remain
sealed.
