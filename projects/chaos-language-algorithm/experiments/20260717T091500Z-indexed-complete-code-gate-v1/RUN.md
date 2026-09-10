# Indexed complete-code synthetic decision gate v1

- Status: completed; indexed code accepted the joint state on the frozen
  synthetic fixture.
- Protocol: `../../docs/indexed-complete-code-gate-preregistration-v1.md`.
- Scope: frozen 19-frame synthetic fixture only; no attractor suffixes.
- Compute boundary: bounded local CPU only; no remote/paid compute, push, or integration.

## Frozen intent

Compare the initial literal state against exactly one intended joint
category/generalized-chunk state using the complete indexed state code. The
unchanged canonical JSON v1 code is a continuity control. Classification and
integrity gates are fixed by the protocol. This cannot revise the
Mackey--Glass/Lorenz--96 coding null or establish chaos or semantic grammar.

## Exact command

```bash
bash command.sh
```

Repository commit, hashes, environment, and outcome-independent verification
will be recorded before executing the command. Results and artifact hashes
will be appended only after execution.

## Pre-run freeze

Frozen at 2026-07-17T02:18:26-07:00 (2026-07-17T09:18:26Z), before
`results.json` existed and before the benchmark module was executed.

- Repository/worktree:
  `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/frozen-suffix-scoring` at
  `29a52fd9af1a2558205645442d660e87f00dcd73` (clean).
- Fixture: 19 frames / 76 tokens; frozen canonical-symbol SHA-256
  `c828bafa0955f0e30ee947865a944e03ac3081203e6bc9e5d34578951310af89`.
- Benchmark implementation SHA-256:
  `7b9ad236402448cb26e11396a9824e48a94a277eaf879b257fdaa26dcbf0306d`.
- Indexed codec SHA-256:
  `f466a7c7fecab19ce471668fc59308e0f2b6ae3884b6b9a3a76b37355313a25a`.
- Fixture module SHA-256:
  `e9af73ca356561093f67b9f0d0b09a572a5e8bce19d9cde57bd64178faafa097`.
- Protocol SHA-256:
  `d1178562893059ba4cdb8bf18120620ea93370e2dece4d9d35817c85a461d8de`.
- Command SHA-256:
  `b7ca7ba7cbf250b9e9d0c7d9a1b1301a9434b061348fd2501597484edbc6f6d5`.
- Environment: Python 3.10.12, GCC 11.4.0; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused verification:
  `python3 -m pytest tests/test_indexed_state_code.py tests/test_state_code.py tests/test_category_slot.py -q`
  — 20 passed; benchmark `py_compile` passed; `git diff --check` passed.

No candidate codelength outcome had been produced or inspected at freeze time.

## Results

The exact `bash command.sh` run exited 0 with empty stderr. Every frozen
fixture, proposal-determinism, source-corpus, decode, and canonical byte-stability
gate passed. The canonical JSON v1 continuity control exactly reproduced its
prior totals and direction.

| code / state | model bits | data bits | total bits |
|---|---:|---:|---:|
| canonical v1 initial | 856 | 33,496 | 34,352 |
| canonical v1 joint | 7,152 | 27,264 | 34,416 |
| indexed initial | 5,168 | 5,448 | 10,616 |
| indexed joint | 5,984 | 3,776 | 9,760 |

Under the frozen decisive indexed comparison, the joint state saved 1,672
data bits while adding 816 model bits, for a net delta of **-856 bits**.
Classification: **`indexed_code_accepts_joint`**.

This establishes only that the intended joint move improves this complete,
decodable indexed code on the frozen synthetic fixture. It does not enable the
joint miner automatically, authorize an attractor rerun, revise the failed
Mackey--Glass/Lorenz--96 held-out calibration, or establish chaos or semantic
grammar.

## Post-run verification

- All 165 tests passed in bounded per-file processes.
- Benchmark/indexed-code `py_compile` and `git diff --check` passed.
- The code worktree remained clean at `29a52fd`.
- Artifact SHA-256: `results.json`
  `5adb5910cf6629eaf971045b6a2744837796d6b41a16459627fdbcc6549e8fa2`;
  empty `stderr.txt`
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Next gate

Implement the indexed complete-code delta behind a replaceable joint-search
scoring seam and validate deterministic accept/reject behavior plus exact
reconstruction on synthetic positive and negative controls. Keep attractor
suffixes untouched and do not run a new attractor benchmark until that learner
integration is separately specified and unit-validated.
