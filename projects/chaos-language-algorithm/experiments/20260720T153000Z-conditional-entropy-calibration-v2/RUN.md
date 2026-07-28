# Conditional transition-entropy Stage-A calibration v2

- Status: completed; exit 0; frozen rule failed.
- Freeze time: 2026-07-20T08:30:00-07:00 / 2026-07-20T15:30:00Z.
- Repository/commit: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`,
  `ba510c36710d6ce511765976b9b4a0fad790c5d5` (clean).
- Protocol: unchanged `docs/conditional-transition-entropy-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only.

V1 produced no score because of a result-field typo. V2 changes only that field
reference and adds a synthetic end-to-end schema test; fixtures, representation,
thresholds, seeds, command, and all-positive/no-control rule are unchanged.
Stage B remains prohibited.

Pre-outcome checks: focused 6 tests / 5 subtests; full pytest 274 tests / 80
subtests; stdlib discovery 196 tests; `compileall`; `git diff --check`.

- Protocol SHA-256: `4f3c8aec137411019c1b4a0e180741a336a854d4b4eccf86a34d45fbb0ed4359`.
- Benchmark SHA-256: `71d1acae4f45e0e2c658de9c10ac8aa134a36aacea110c0e4fc08821ad4c85fc`.
- Declaration-test SHA-256: `4c541f6ece364e2f24e3b88f992db67f0aa6dc016d9236e2351d4c5a071d98f2`.
- Command SHA-256: `25c1a3c52db54ba8dbe92144c491392564e757d08aa12b36cc4e7f3fccf2f45f`.
- Dynamics seeds none; shuffle seeds 731921/731922.
- Initial-state hashes: MG `ad78cfa0ead35ff9d0d6de11ae996a470b257a7342d2a53073df0ce8cda04c4d`;
  L96 `2584f06356fcc4b6e18701f8ade5df492ba98fd0c6e00a73a6112ed3fa75f85c`.
- Exact command: `bash command.sh`.

No score was produced or inspected before this freeze. No tuning or rescoring
is permitted. This is only a bounded detector calibration, never chaos,
attractor/source-law, CLA/compression, or semantic-grammar evidence.

## Results

Both positives were promoted: Mackey--Glass `0.0642205952` and full-state
Lorenz--96 `0.1119047699`. Mackey--Glass stable (`0`) and shuffled
(`0.9999092930`) controls were rejected. Stable Lorenz--96 (`0.0250289065`)
and shuffled Lorenz--96 (`0.5845559857`) were false positives, so the gate
failed. No tuning or rescoring; Stage B remains prohibited. Exit 0, 0.22 s,
19,856 KiB maximum RSS, empty stderr; clean worktree and diff check.

- Results SHA-256: `141145e6df21df3908290b6a549af7062470ce1ba283faf91a2c5f961f1bef5e`.
- Stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Timing SHA-256: `cd2223fec4e553501eee4ec18939396951749c2c46c87ddc7369566e58677b26`.
- Exit-status SHA-256: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
