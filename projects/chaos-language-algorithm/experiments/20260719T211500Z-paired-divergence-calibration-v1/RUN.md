# Paired-divergence Stage-A calibration v1

- Status: completed; exit 0; frozen rule failed.
- Freeze time: 2026-07-19T14:15:00-07:00 / 2026-07-19T21:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at
  `4cc2441810f518f563a46eb63d4b2d352022dfd6` (clean).
- Protocol: `docs/paired-divergence-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

This separately frozen Stage-A gate compares fixed paired log-separation slopes
for fresh Mackey--Glass and full-state 8D Lorenz--96 chaotic regimes against
matched stable regimes. Perturbation `1e-8`, 256 samples, fit window `[32:256]`,
and strict threshold `1e-4` per sample are fixed. Both positives and no stable
controls must be promoted; ties fail. Stage B remains separate and prohibited.

Pre-outcome checks: focused 4 tests / 4 subtests passed; full pytest passed 257
tests / 49 subtests; `py_compile` and `git diff --check` passed.

- Protocol SHA-256: `d70a35d783e043caa15a9941af94ab68854c1c1f710eb840c5b484030ac29531`.
- Benchmark SHA-256: `ca4946cae38d16b1ba5351528bc367fc8ac06912050c3174a2e9ee33e770564e`.
- Declaration-test SHA-256: `9a40a4d5ff5a3d14a76a41c1304f07266c6150bdc09ea35111fea4c3a14a5e45`.
- Frozen command SHA-256: `cc478dd06d1c9bc696b40ff765a0c4036aa934ea3fd1b53bd91d7e8a4285d278`.
- Environment: Python 3.10.12; Linux x86_64 kernel 7.0.11-76070011-generic.
- Decisive command: exactly `bash command.sh` from this ledger directory.

No slope result was produced or inspected before this freeze. A pass is bounded
finite-window discrimination evidence only, not a validated Lyapunov estimator,
proof of chaos, attractor/source-law identification, CLA validation, or semantic
grammar evidence. Failure may not be tuned or rescored on these fixtures.

## Results

The exact command exited 0 with empty stderr in 0.06 seconds and 17,312 KiB
maximum RSS. Mackey--Glass tau=17 was a false negative (slope `-0.0067585072`
per sample), and stable full-state Lorenz--96 F=1 was a false positive
(`0.0106747962`). Chaotic full-state Lorenz--96 was promoted (`0.0391790379`),
while stable Mackey--Glass was rejected (`-0.0297402265`). Every fit used 224
finite positive separations. The strict gate failed; Stage B remains prohibited.
No perturbation, window, threshold, initial state, or regime may be tuned or
rescored on these fixtures.

This is a finite-window detector-calibration null, not evidence against chaotic
dynamics and not attractor, source-law, CLA, or semantic-grammar evidence.
Post-run focused checks passed 4 tests / 4 subtests; full pytest passed 257
tests / 49 subtests; stdlib discovery passed 179 tests; `py_compile` and
`git diff --check` passed. The worktree remained clean at `4cc2441`.

- `results.json`: `1d3996c126c3b6ba114849b4a32034d198747ff2b743b3d2c8bc0a4c4449ec9b`.
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `timing.txt`: `7014c392e0a8889302537e48e3b04cb145518284d27cb2b7b4880d164be7fa78`.
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
