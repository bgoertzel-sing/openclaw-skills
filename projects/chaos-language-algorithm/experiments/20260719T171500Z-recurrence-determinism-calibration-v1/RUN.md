# Recurrence-determinism Stage-A calibration v1

- Status: completed; exit 0; frozen rule failed.
- Freeze time: 2026-07-19T10:15:00-07:00 / 2026-07-19T17:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at `9aca50b34b92477706dc96a6616556e5d6f7551b` (clean).
- Protocol: `docs/recurrence-determinism-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

This separately frozen Stage-A gate scores fresh Mackey--Glass and full-state
8D Lorenz--96 chaotic regimes, matched stable-regime controls, and exact-
marginal shuffled nulls. Radius calibration uses only a 256-sample prefix; the
512-sample evaluation is untouched until `bash command.sh`. The fixed detector
threshold is 0.20, recurrence fraction must lie in `[0.01, 0.20]`, and all
positives/no controls must be promoted. Ties pass. Stage B remains separate.

Pre-outcome checks: focused 9 tests passed; full pytest passed 253 tests / 45
subtests; `py_compile` and `git diff --check` passed.

- Protocol SHA-256: `77fd284cfe86430c38587fcbdd695000a4035b168d42bbbd438a72ac64f7233e`.
- Benchmark SHA-256: `ee1231f59848ec51011ea52bab6399e3a5d1f5b5bdcaea67aaef0c2fa716f558`.
- Declaration-test SHA-256: `3b707a832630bf14623b2cb876eed2fabd5253a6a2129c3d89a4efd18eeb79e1`.
- Environment: Python 3.10.12; Linux x86_64 kernel 7.0.11-76070011-generic.
- Decisive command: exactly `bash command.sh` from this ledger directory.

No detector result was produced or inspected before this freeze. A pass would
be bounded discrimination evidence only, not proof of chaos, attractor/source-
law identification, CLA validation, or semantic grammar evidence. A failure
may not be tuned or rescored on these fixtures.

## Results

The exact command exited 0 with empty stderr in 0.29 seconds. Both positives
were promoted and both shuffles rejected. Stable Mackey--Glass was degenerate
and failed closed, but stable full-state Lorenz--96 was a nondegenerate false
positive (`DET=1.0`). False negatives: none; false positives:
`lorenz96-stable-full-state`. The strict Stage-A gate failed and Stage B is not
authorized. No tuning or rescoring is permitted.

Post-run focused 9 tests, full pytest 253 tests / 45 subtests, `py_compile`, and
`git diff --check` passed; worktree clean at `9aca50b`. `results.json` SHA-256:
`473a16da63d1350476a84e3baa631e9a47e1339069651d9774d4d9c13568f4f9`.
