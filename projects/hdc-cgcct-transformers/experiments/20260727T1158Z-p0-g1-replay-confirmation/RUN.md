# Run 20260727T1158Z-p0-g1-replay-confirmation: P0-G1 replay confirmation

- Project: `hdc-cgcct-transformers`
- Started: `2026-07-27T11:58:00Z`
- Finished: `2026-07-27T12:05:00Z` (approximate; command runtime 293 s)
- Status: `failed_closed`
- Local or remote: `local` (CPU only; no paid/remote compute)
- Working directory: `/home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes`
- Git commit: `fa1172103a5a6bd7a126e1b776232bdf1479ccf0` (`agent/p0-core`, clean)

## Question

Does a new clean local invocation reproduce the previously interrupted P0-G1
payloads and gate result without changing the preserved artifacts?

## Command and deterministic settings

```bash
bash scripts/run_p0_gate.sh ../../artifacts/p0-selftest-v2
```

The script fixes `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, fixture seed
`12011`, and 2,048 trials for each of 36 `(D,k,M)` cells.

## Observed result

- `pytest`: `13 passed in 0.72s`.
- Replay A payload SHA-256: `e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`.
- Replay B payload SHA-256: `e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`.
- Validator SHA-256: `719215ee8b08f88ced2847b55eddc277b488d2e21407e1af52f60203ae5c89e1`.
- Command exit status: `1`, expected because `P0-G1 passed=False`.

The artifact bytes remain exactly the recorded values in
`artifacts/p0-selftest-v2/`; this was not a runtime interruption or an artifact
integrity failure. The validator's only failed required condition remains the
`k=4, M=32` curve: six accuracies of `1.000` produce Spearman association `0.0`.

## Disposition

P0-G1 remains failed closed. Per specification Section 8 and
`D-20260727-p0-g1-fail-closed`, P1A/P1B is not an authorized next step. The
next actionable CPU-local P0/P1 step requires Benjamin's explicit authorization
of a revised P0 fixture/grid or gate contract; it must retain these artifacts
as prior evidence.
