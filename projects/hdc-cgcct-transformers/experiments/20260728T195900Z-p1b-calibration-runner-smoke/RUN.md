# P1B calibration runner and raw-artifact smoke

- Date: 2026-07-28T19:59Z
- Nested repository commit: `6a807b186a7fa4be69e1ba4fddb99a2f33bdeccc`
- Scope: CPU-local implementation and reduced replay tests
- Remote resources: none

Implemented the frozen decoder training schedule (AdamW, clipping, evaluation,
early stopping, earliest-best checkpoint), deterministic sample ordering,
batched residual extraction, fresh per-dimension/per-arm ridge readouts,
feature thresholds and error/closure metrics, hashed raw `.npy` artifacts,
artifact verification, calibration-seed allowlisting, and a fail-closed
criteria freezer.

Verification:

```text
python3 -m pytest -q
26 passed in 3.62s
python3 -m py_compile \
  src/hdc_cgcct/p1b_calibration.py scripts/run_p1b_calibration.py
git diff --check
```

The reduced test executes one update twice and verifies byte-identical
scientific JSON and artifact hashes. It is explicitly gate-ineligible. The
confirmation-seed test verifies that seed `15313` is rejected.

Remote launch remains blocked. Before a full smoke can clear precondition 3,
the runner still needs per-`H` metric partitioning, independent logistic
representation probes, shuffled-label controls, coherence diagnostics, peak
GPU-memory recording, and tests of those fields. No live offer was queried
and no pod was provisioned.
