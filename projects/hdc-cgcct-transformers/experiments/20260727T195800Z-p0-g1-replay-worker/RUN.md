# Run 20260727T195800Z-p0-g1-replay-worker: scheduled P0-G1 replay

- Project: `hdc-cgcct-transformers`
- Started: `2026-07-27T19:58:00Z`
- Finished: `2026-07-27T20:04:07Z`
- Status: `failed_closed`
- Local or remote: `local` (CPU only; no paid/remote compute)
- Working directory: `/home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes`
- Git commit: `fa1172103a5a6bd7a126e1b776232bdf1479ccf0` (`agent/p0-core`, clean)

## Question

Does a fresh local CPU-only process reproduce P0-G1 exactly while retaining the
previously preserved artifacts unchanged?

## Command and deterministic settings

```bash
bash scripts/run_p0_gate.sh ../../artifacts/20260727T195800Z-p0-g1-replay-worker
```

`scripts/run_p0_gate.sh` SHA-256 is
`e65fc693201a286509e194b7e4a65d8bb9709260655e7b70b17c028476f69004`.
It fixes `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, fixture seed `12011`, and
2,048 trials in each of 36 `(D,k,M)` cells. Command exit status `1` is
expected when the validator emits `P0-G1 passed=False`.

## Observed result

- `pytest`: `13 passed in 0.74s`.
- Replay A SHA-256: `e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`.
- Replay B SHA-256: `e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`.
- Validator SHA-256: `719215ee8b08f88ced2847b55eddc277b488d2e21407e1af52f60203ae5c89e1`.
- Replay payloads are byte-identical and exactly equal the preserved P0-G1
  payload hash. The new evidence is in
  `artifacts/20260727T195800Z-p0-g1-replay-worker/`; earlier artifacts were
  not overwritten.

The validator remains `passed: false`. Its failed required curve is
`k=4, M=32`: all six dimension points have accuracy `1.000`, producing
required-positive Spearman association `0.0`. This is a valid fail-closed gate
result, not a runtime interruption or integrity failure.

## Disposition

P0-G1 remains failed closed under Section 8 and
`D-20260727-p0-g1-fail-closed`. P1A/P1B may not start. The next recorded
CPU-local programme action is to await Benjamin Goertzel's explicit
authorization of a revised P0 fixture/grid or gate contract; that revision
must retain this evidence as prior failed-gate evidence.
