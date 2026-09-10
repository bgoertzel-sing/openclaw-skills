# Minimal joint chunk/category diagnostic v1

- Status: preregistered; not yet executed.
- Protocol: `../../docs/joint-chunk-category-diagnostic-preregistration-v1.md`.
- Scope: synthetic local diagnostic only; no held-out attractor suffixes.
- Compute boundary: bounded local CPU only; no remote/paid compute, push, or integration.

## Frozen intent

Run the 19-frame fixture and classification exactly as preregistered. This is a
separate diagnostic following the failed frozen held-out benchmark; it cannot
change or rescue that null result.

## Exact command

```bash
bash command.sh
```

Repository commit, fixture and implementation hashes, environment, pre-run
verification, results, artifact hashes, and conclusion will be appended before
and after the decisive command in the order required by the protocol.

## Pre-run freeze

Frozen at 2026-07-16T12:19:48-07:00 (2026-07-16T19:19:48Z), before
`results.json` existed or the diagnostic test/module was executed.

- Repository/worktree: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/frozen-suffix-scoring` at
  `62796045014b8c16b553aadfbc2beb7daa5ac6bc` (clean).
- Fixture: 19 declared frames / 76 tokens; canonical-symbol SHA-256
  `c828bafa0955f0e30ee947865a944e03ac3081203e6bc9e5d34578951310af89`.
- Implementation SHA-256:
  `src/chaoslang/benchmarks/joint_diagnostic.py`
  `e9af73ca356561093f67b9f0d0b09a572a5e8bce19d9cde57bd64178faafa097`.
- Test SHA-256: `tests/test_joint_diagnostic.py`
  `4a4207f7f85f96465739711a1c99be320e1f3d5e060ee0a72d04849c5e2bfe74`.
- Protocol SHA-256:
  `0f233731c175662e6a42eb322a55379b6dc4bf73d1b8be7551fec48638b97cdf`.
- Command SHA-256:
  `a12ae287691b0f32c23177ba9c77fbf966290e213da7651bf1334432ac516651`.
- Environment: Python 3.10.12, GCC 11.4.0; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused verification:
  `python3 -m pytest tests/test_chunk_mvp.py tests/test_core.py tests/test_symbolic_mvp.py tests/test_js_integration.py -q`
  — 30 passed; `python3 -m py_compile` on the new module/test passed;
  `git diff --check` passed.

## Results

The exact `bash command.sh` run exited 0 with empty stderr. All frozen fixture,
formula, reconstruction, and deterministic-repeat gates passed.

| measurement | result |
|---|---:|
| initial / greedy score | 76.0 proxy bits |
| greedy accepted edits | 0 |
| abstract joint score | 75.0 proxy bits |
| abstract joint delta | -1.0 proxy bit |
| intended category proposed initially | no |
| member-agnostic `a M b` chunk available after manual category | no |

Frozen classification: **`greedy_or_representation_blindness`**. The current
learner cannot reach the strictly improving prescribed joint move: singleton
middle symbols do not pass the exact-context inducer's per-token occurrence
gate, and `CategoryOccurrence` mining keys retain the chosen member, so the
chunk miner does not unify `M[m00]` through `M[m18]` as one `M` slot.

This is a synthetic local proxy diagnosis only. It neither rescues the failed
Mackey--Glass/Lorenz--96 held-out code result nor validates chaos, attractor
grammar, semantic structure, or a production coding scheme.

## Post-run verification

- Focused diagnostic: `python3 -m pytest tests/test_joint_diagnostic.py -q`
  — 2 passed.
- Relevant full suite: all 145 collected tests passed in bounded per-file and
  per-node shards. The parameter sweep's seven logistic tests and seven
  Lorenz--96/high-dimensional tests were isolated to release peak memory.
- `git diff --check` passed; the code worktree remained clean at `6279604`.
- Two initial post-run invocations from the experiment directory collected no
  tests because that directory has no `tests/`; they were immediately rerun
  from the repository. A later monolithic/per-file attempt stopped without a
  summary during the memory-heavy parameter sweep, so the suite was rerun in
  the bounded shards above. These were harness-location/resource issues, not
  test failures.

Artifact SHA-256: `results.json`
`01eb96348471c0dd712240f80acd241f135c26f6911d9b6d2513d07f9e6cce8f`;
`stderr.txt`
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Next gate

Specify a replaceable, exact-reconstructing generalized category-slot proposal
seam and test it first on this frozen fixture. Do not run another attractor
benchmark until the learned model has a decodable representation and fair
model-transmission accounting for that joint move.
