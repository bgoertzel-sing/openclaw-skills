# Nearest-neighbor divergence Stage-A calibration v1

- Status: executed once; exit 1 before any detector score; frozen gate not
  evaluated.
- Freeze time: 2026-07-20T14:15:00-07:00 / 2026-07-20T21:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at
  `ee0485c18d77a02d4ee718d5760ade25e4d39793` (clean).
- Protocol: `docs/nearest-neighbor-divergence-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

The frozen representation is a causal six-coordinate delay vector for fresh
Mackey--Glass initial 3.1 and the complete eight-coordinate state for fresh
Lorenz--96 initial perturbation 8.11.  Each coordinate is standardized from a
1,024-state prefix that is excluded from scoring.  Fresh tau=17/F=8 positives,
tau=2/F=1 stable controls, and state-shuffled controls are fixed.  Promotion
requires slope strictly above 0.005; both positives and no control must be
promoted.  Stage B remains prohibited.

Pre-outcome checks passed: focused pytest 6 tests / 4 subtests; full pytest 280
tests / 84 subtests; stdlib discovery 202 tests; `compileall`; and
`git diff --check`.

- Protocol SHA-256: `c2e5d512715d3b7fbbbe449a4bbd99a2026acf8b4112f82faee6c11906993e68`.
- Benchmark SHA-256: `bece1f2047bface2cfad8ae2b7b79b03962c432b1e98b19dbb9737be40bcba8b`.
- Declaration-test SHA-256: `09abcee35c511e3c403bfe14183c249d6f04259319068df8d93f5c0b41e17fee`.
- Command SHA-256: `f901c1f2f33825b0b580b87d036c98f0446e90142c597444177e1a8620520dcc`.
- Serialized initial-state SHA-256: Mackey--Glass
  `08423c1ee488176f64566989e4dddd157093b0294c16e0c906f1cbd23bacaa11`;
  Lorenz--96 `63428b686126b3604fb06f29bc662d83b3a09e864a46e277b8c7343749b01947`.
- Shuffle seeds: 842021 and 842022; dynamics have no random seed.
- Decisive command: exactly `bash command.sh` from this directory.

At freeze time `run()` and the decisive command had not been executed.  This
can establish only bounded finite-protocol discrimination, never chaos proof,
attractor/source-law identification, CLA/compression validation, or semantic
grammar.  Failure may not be tuned or rescored on these fixtures.

## Execution result

The exact decisive command was executed once on 2026-07-20 at approximately
16:15 PDT. It exited 1 after about 13.5 seconds, before JSON or any detector
score was emitted. `nearest_neighbor_divergence` raised
`ValueError: no eligible positive-distance neighbor pair exists` while
processing a frozen stable fixture. Because `command.sh` uses `set -e`, no
results, stderr, timing, or exit-status artifact file was created; the captured
traceback is preserved in the cron execution record. The active repository
remained clean and `git diff --check` passed.

This is a preregistered harness/protocol failure, not a failed or passed
scientific calibration. Do not change the frozen fixture, neighbor rule, or
other scientific choices and rerun this v1 ledger. Stage B remains prohibited;
any corrective runner behavior requires a separately frozen v2 that preserves
the scientific choices and adds an end-to-end stable-fixture schema test before
execution.
