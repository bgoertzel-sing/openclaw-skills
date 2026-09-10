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

## 2026-07-28T07:58Z worker checkpoint

The detached frozen full-grid process remains healthy after 3:58:31 elapsed:
PID `162123`, state `R`, 99.9% CPU, 441,760 KiB RSS. The runner emits only its
final payload, so `run.log` remains empty by design; neither the output payload
nor `exit-status.txt` exists while it is running. This is continuing execution,
not a gate result. P1B implementation and all remote provisioning remain
deferred behind this priority-one run.

## Completion

The detached process exited `0` at 2026-07-28T04:50:16 local
(2026-07-28T11:50:16Z). It wrote 1,275 cells and 75 curves with
`scientific_gate_eligible=true`. The payload is 1,060,830 bytes and has
SHA-256 `b7fabae33494ed090fe1cd73b85fff0ad3f36fe7f3c6f986ed1a30ab0197195b`.
All 18 implementation tests passed after completion.

Calibration fit: 60 F0/F1 curves were interior, 15 F2 pathology curves were
right-censored, `alpha_hat=1.4506361516460744`, and the fitted
`[b0,b_k,b_M]` coefficients were
`[4.6456356439528586,1.1922932291366184,-0.7050253292125505]`.
No F0/F1 curve had a statistically resolved adjacent accuracy decrease
greater than 0.02. However, 31 of 60 F0/F1 calibration curves had Spearman
correlation below the frozen 0.90 monotonicity threshold (minimum
`0.5601120336112039`). This is material calibration evidence and a warning
for P1-G1, but not a confirmation-seed gate verdict. Criteria were not changed
and confirmation seeds were not opened.
