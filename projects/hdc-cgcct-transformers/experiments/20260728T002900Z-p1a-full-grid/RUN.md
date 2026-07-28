# P1A frozen full-grid calibration

- Started: 2026-07-28T00:30Z
- Repository commit: `e4e1d65`
- Scope: CPU-local, frozen scientific-gate-eligible P1A calibration grid
- Runtime: system `python3`, PyTorch `2.12.1+cpu`, deterministic algorithms,
  one Torch thread
- Command: `python3 scripts/run_p1a_calibration.py --output
  artifacts/p1a-full-grid/p1a-calibration.json`
- Frozen defaults: seeds `12011,13121,14251`; 2,048 trials/cell; all 17
  dimensions and five loads from `docs/p0-p1-spec.md`
- Live outputs: `repos/hdc-cgcct-probes/artifacts/p1a-full-grid/run.log` and
  `p1a-calibration.json` on successful completion

Status at the scheduled-worker checkpoint: running single-threaded locally.
No P0-v1 replay, P1B work, remote provisioning, criteria change, or
hyperparameter search was performed. Final payload hash, schema checks,
metrics, and calibration interpretation must be appended only after the
process exits successfully.

## 2026-07-28T04:00Z worker checkpoint

The earlier foreground execution did not survive to this worker tick: no
`run_p1a_calibration.py` process existed, `run.log` was empty, and no payload
was written. Kernel logs contained no OOM-kill record. This is an interrupted
execution, not a scientific gate result.

The unchanged commit passed all 18 tests. A non-gating 16-trial resource
benchmark over `D={8192,12288,16384}`, `k={32,64}`, one seed took 36.21 seconds
and 688,628 KiB maximum RSS. The frozen full-grid command was then relaunched
detached with unbuffered logging and an exit-status sidecar. No fixture,
criterion, seed, trial count, or hyperparameter changed.
