# Run 20260727T1558Z-p0-g1-replay-worker: scheduled P0-G1 replay

- Project: `hdc-cgcct-transformers`
- Started: `2026-07-27T15:58:00Z`
- Finished: `2026-07-27T15:59:47Z`
- Status: `failed_closed`
- Local or remote: `local` (CPU only; no paid/remote compute)
- Working directory: `/home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes`
- Git commit: `fa1172103a5a6bd7a126e1b776232bdf1479ccf0` (`agent/p0-core`, clean)

## Question

Does a fresh local scheduled-worker invocation reproduce the preserved P0-G1
payloads and fail-closed result?

## Command and deterministic settings

```bash
bash scripts/run_p0_gate.sh ../../artifacts/p0-selftest-v2
```

The recorded script sets `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, fixture
seed `12011`, and `2048` trials in each of 36 `(D,k,M)` cells.

## Observed result

- `pytest`: `13 passed in 0.73s`.
- Replay A SHA-256: `e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`.
- Replay B SHA-256: `e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`.
- Validator SHA-256: `719215ee8b08f88ced2847b55eddc277b488d2e21407e1af52f60203ae5c89e1`.
- The validator returns the expected nonzero status because `passed` is
  `false`; this is a gate result, not an execution interruption.

The `k=4, M=32` curve remains accuracy `1.000` at every tested dimension
(`128,256,512,1024,2048,4096`), so its required-positive Spearman association
is `0.0`. The two payload bytes are identical, while P0-G1 is false.

## Disposition

P0-G1 remains failed closed. Section 8 and
`D-20260727-p0-g1-fail-closed` prohibit P1A/P1B work. The next CPU-local
programme action requires Benjamin's explicit authorization of a revised P0
fixture/grid or gate contract; the retained artifacts remain prior evidence.
