# Renormalized-separation Stage-A calibration v1

- Status: completed; exit 0; frozen rule failed.
- Freeze time: 2026-07-20T02:15:00-07:00 / 2026-07-20T09:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at
  `793f10c20d3af5139c212ef518341621c50ec749` (clean).
- Protocol: `docs/renormalized-separation-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

The frozen Stage-A gate uses fresh Mackey--Glass delay state 1.7 and full-state
8D Lorenz--96 coordinate-6 perturbation 8.07, with matched tau=2 and F=1 stable
controls. Fixed 2,000-step transients, `1e-8` initial separation, 64 cycles of
25 steps, deterministic first-component perturbation, full-state Euclidean
separation, and strict threshold zero are predeclared. Both positives and no
stable controls must be promoted; ties and numerical collapse fail. Stage B
remains prohibited.

Pre-outcome checks passed: focused 4 tests; full pytest 268 tests / 75 subtests;
stdlib discovery 190 tests; `compileall`; and `git diff --check`.

- Protocol SHA-256: `360eec97c9925152fc8153734f9a4c4c47e706e3b2d65ac23fc8992f7cd7a201`.
- Benchmark SHA-256: `127a4b228bd99bded24722b77c26f95fc410941ab35b478e8b887340bfb5446c`.
- Declaration-test SHA-256: `ce88b4647525c9d04c474818e22be5c4d8285d3cda47a656622e15657899fdde`.
- Frozen command SHA-256: `65a6dc67606b9cf463baa28aa214aa83d74cbbb862beb92cc439b2065c1b74b5`.
- Initial-state hashes: Mackey--Glass positive `84ca9c76d92349cb9adfe0cf2297b9c5af1912749dfdde443842d54817ccf1c3`;
  Mackey--Glass stable `0377b1599a1a88d180422fc1700a2b4f61d32c9aaac034d30c5fc4dacb1a285c`;
  Lorenz--96 positive/stable `02a7b052d795eab5938fec2ce41c7318e635d3458903a689cdd7f05d08897fc5`.
- Seeds: none; all initial states and perturbation directions are explicit.
- Decisive command: exactly `bash command.sh` from this ledger directory.

At freeze time no detector score had been produced or inspected. This can establish only
bounded finite-protocol discrimination, not proof of chaos, a validated
Lyapunov exponent, attractor/source-law identification, CLA validation,
compression evidence, or semantic grammar. A failure may not be tuned or
rescored on these fixtures.

## Results

The exact frozen child command exited 0 with empty stderr in 0.17 seconds and
17,152 KiB maximum RSS. Full-state Lorenz--96 was promoted
(`0.0219147658` mean log growth per step), while stable Lorenz--96
(`-0.0006357785`) and stable Mackey--Glass (`-0.0293053833`) were rejected.
Mackey--Glass tau=17 was a false negative (`-0.0009622967`). Every fixture
reported exactly 64 cycles and 1,600 elapsed steps. The all-positive/no-control
rule therefore failed and Stage B remains prohibited. No transient, direction,
cycle length, count, perturbation, initial state, regime, or threshold may be
tuned or rescored on these fixtures.

Post-run focused checks passed 4 tests and `git diff --check`; the immutable
code worktree remained clean at `793f10c`. The full 268-test / 75-subtest pytest
suite, 190-test stdlib suite, and `compileall` had passed before outcome
inspection against that same clean commit.

- `results.json`: `092ab466c337da8c928d76e7c883d4625a97f7603640ffe99f8251ea9d2a900a`.
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `timing.txt`: `78d061f13da66cc96b93d8168224f51b81643bf64d39865eeaf285980422b657`.
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
