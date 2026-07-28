# Full-vector recurrence attractor calibration v1

- Status: completed; exit 0; all integrity gates passed; frozen rule failed.
- Freeze time: 2026-07-19T00:15:00-07:00 / 2026-07-19T07:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at `c667c02` (clean).
- Protocol: `docs/vector-recurrence-attractor-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

The frozen gate uses fresh Mackey--Glass initial 1.5 as an explicit scalar
calibration control and a fresh full-state 8D Lorenz--96 trajectory initialized
with x0=8.05. Prefix-only adjacent-distance q0.10 radii, causal lag bins through
64, 1,024-symbol prefixes, untouched 4,096-symbol suffixes, matched exact-
marginal shuffles, compact/JSON CLA, literal, unigram, Markov-1/2, and canonical
LZ78 are fixed. Both positives must beat every external control, neither null
may be promoted, and every integrity gate must pass. Ties fail.

Pre-outcome checks: focused 7 tests / 10 subtests passed; full 244 tests / 33
subtests passed; `py_compile` and `git diff --check` passed.

- Protocol SHA-256: `1fca200434f29a43ccf342afc429cfc72d41c4db0eaf0d16dc124891fdf79810`.
- Benchmark SHA-256: `9f9d726589984a92a6d24dfeea3c80bceb80f87024e199d78f0639d7043168db`.
- Declaration-test SHA-256: `3a70e2d4c3a44187af4d983c23b714316f1e92dcdaf79c61ea2be2e60abcb3ef`.
- Canonical frozen manifest SHA-256: `4efa7334b58acb3f4d05f1792e2ffb65c6f22094c059421752aea7189c7487e2`.
- Frozen command SHA-256: `fb929b306824a713b9e4b51bd37f36dd4ba55539ef8b659ee24912eccaf64749`.
- Positive suffix SHA-256: Mackey--Glass `a5ee1d066f73a4e31279190b1590bc774eed13a5812d587e35b7c5e1f411cb1e`; Lorenz--96 `02a7ee5a4801ca5a1387935a66b47b790f0dcee086487793a4d6b5eeb7bf6dd4`.
- Decisive command: exactly `bash command.sh` from this ledger directory.

No benchmark outcome was produced or inspected before this freeze. This is a
complete-code calibration only, not chaos, attractor, source-law, or semantic-
grammar evidence. No inspected configuration or suffix may be tuned or rescored,
and proxy compression cannot replace the frozen comparison.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 46.05 seconds
wall time and 25,616 KiB maximum RSS. Every integrity gate passed. Compact CLA
beat its JSON continuity control throughout, and neither shuffled null was
promoted. Both required positives lost to canonical LZ78, however:

| fixture | compact CLA bits | strongest control | control bits |
|---|---:|---|---:|
| Mackey--Glass initial 1.5 positive | 9,933.113 | LZ78 | 5,304.000 |
| Mackey--Glass shuffled | 12,317.070 | unigram | 6,332.716 |
| Lorenz--96 full 8D positive | 5,522.398 | LZ78 | 2,000.000 |
| Lorenz--96 full 8D shuffled | 8,533.637 | unigram | 3,207.815 |

The strict all-positive rule **failed**. Full-vector recurrence did not make
the frozen CLA code competitive on this fresh Lorenz--96 calibration, while
the explicit Mackey--Glass calibration also remained negative. This is a
coding null, not evidence against chaos and not attractor or semantic-grammar
evidence. No tuning or rescoring is authorized.

Post-run focused checks passed 7 tests / 10 subtests; the full suite passed 244
tests / 33 subtests; `py_compile` and `git diff --check` passed. The code
worktree remained clean at `c667c02`.

- `results.json`: `9f5acb1cf2d8162e418a2b3d1ee422b4a9b42320090c7edb64c43766c8a76f8b`.
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `timing.txt`: `e02842cb344568056d47b48e185e6260153e5c6b0b1eedac327f2dae776ab42a`.
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.

## Next gate

Do not tune the vector radius, Lorenz--96 state, Mackey--Glass control, lag
classes, split, suffix, learner, or codecs. Another measurement requires a new
outcome-independent detector hypothesis and untouched data, retaining complete
external controls. Proxy compression cannot substitute for this result.
