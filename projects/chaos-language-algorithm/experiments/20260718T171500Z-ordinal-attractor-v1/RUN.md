# Ordinal-pattern attractor calibration v1

- Status: completed; all integrity gates passed; frozen detector rule failed.
- Freeze time: 2026-07-18T10:15:00-07:00 / 2026-07-18T17:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/ordinal-pattern-symbolization-v1` at
  `17a0778a2a332c8a857fa6ccc7716e850d2cf572` (clean).
- Protocol: `docs/ordinal-attractor-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

The frozen gate uses new Mackey--Glass initial 1.1 and Lorenz--96 x6 scalar
observations, causal order-3/delay-1 ordinal patterns, a 1,024-symbol prefix,
an untouched 4,096-symbol suffix, matched shuffled nulls, complete compact/JSON
CLA, literal, unigram, Markov-1/2, and canonical LZ78 accounting. Both positive
fixtures must beat every external control, neither null may be promoted, and
all integrity gates must pass. Ties fail. This is a coding calibration only,
not chaos, attractor, source-law, or semantic-grammar evidence.

Pre-run checks: focused 10 tests / 10 subtests passed; full 227 tests / 10
subtests passed; `py_compile` and `git diff --check` passed. Exact fixture and
split hashes are frozen in `manifest.json`. Decisive command: `bash command.sh`.

Protocol SHA-256: `80127d070fc5a87eda36239995af2e20982dd741da6b298022d79cc1c98f0dd0`.
Benchmark SHA-256: `085eceed241baad6fb14f476f687f98a6b16f1302db01a61d12bed49ae5b0869`.
Declaration-test SHA-256: `722d3a246ef638560969045e5c96c718a5dd12d9be501f76c662081b75e3952e`.

Frozen manifest SHA-256: `8e63d5ccab934dc0e67c7eb47803e971141c46d5752258ff24dcf6dcfd8b01cd`.
Frozen command SHA-256: `da6294784d5945c2cd3bec9bb04b6dcf23a89084fb2a2706f736338e3ad50c37`.

## Results

Every integrity gate passed, compact CLA beat its JSON continuity control on
all fixtures, and neither shuffled null was promoted. The required positives
both lost to canonical LZ78, however: Mackey--Glass used 9,235.184 versus
2,872.000 bits, and Lorenz--96 x6 used 10,224.372 versus 3,928.000 bits. The
strict all-positive rule therefore failed.

The first orchestration call returned before its still-running child populated
the artifacts, so a diagnostic `bash -x command.sh` invocation duplicated the
deterministic run. This is recorded as an execution-ledger deviation. The
second invocation produced the retained byte-stable JSON result; it did not
change configuration, inspect an intermediate outcome, or tune any fixture.

Post-run focused checks passed 10 tests / 10 subtests; the full suite passed
227 tests / 10 subtests; `py_compile` and `git diff --check` passed. The code
worktree remained clean at `17a0778`. Runtime was 68.04 seconds with 27,172 KiB
maximum RSS. Artifact SHA-256 values:

- `results.json`: `924caf8a0f21d0cdeab1dd6e7f36f2997abde9a592ef2622e519663e81250fd0`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `179d2bdb220212d947fcec027bbe54d3d0998aa84395a545423102030608d1e4`

This is an ordinal-representation coding null, not evidence against chaos and
not attractor or semantic-grammar evidence. No order, delay, trajectory,
coordinate, split, suffix, learner, or codec tuning is authorized. A further
detector gate requires a new outcome-independent hypothesis and untouched data.
