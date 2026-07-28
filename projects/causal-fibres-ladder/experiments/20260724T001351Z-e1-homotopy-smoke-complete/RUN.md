# Run 20260724T001351Z-e1-homotopy-smoke-complete: e1-homotopy-smoke-complete

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T00:13:51Z`
- Finished: `2026-07-24T00:13:54Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the completed reduced six-block synthetic-grammar harness satisfy the E1
operational contract: matched arms, frozen weights during settlement,
structurally teacher-free evaluation, guarded activity inference, persisted
milestones, factor intervention metrics, frontier/rank diagnostics, and
deterministic artifacts?

## Hypothesis or expected behavior

All operational invariants, objective-control identity checks, guard retention,
and constructed diagnostic fixtures should pass. This smoke is not expected to
decide whether homotopy rescues direct ePC.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Code: `agent/e1-guarded-homotopy` commit
  `dd1a6e90665e963ba624d1e040efdcc2557c8f49`, based on R8 `ecf2f79`.
- Config: `configs/e1_homotopy_smoke.json`; seed `1729`; four factors;
  12 matched updates for four arms.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: results JSON/NPZ, deterministic `milestones.jsonl`, and manifest.
- Preflight/regression: 15 tests passed.
- Operational gates all passed: identical arm sample identities, byte-identical
  settlement weights, no teacher slot in the teacher-free evaluator, retained
  divergence-guard evidence, BP-KD/objective-control terminal identity, finite
  outputs, and correct factor schema.
- Deterministic scientific digest replay:
  `115e49f52e782bf020e308f485a0177575810c94d0939d10f04e0c23747f477a`.
- NPZ replay:
  `2a69e5e6a767e5583ecf20d49aa967b20c1faef154f06b6e5c5a2c22238710f3`.
- Milestone JSONL replay:
  `37a03ff644631dde740155568cf95971cda71c1a7470ca09650f7642889f61b7`.
- Wall time `2.39 s`, peak RSS `294,172 KiB`, harness time `1.130 s`,
  throughput `42.48 updates/s`, raw arrays `294,912 bytes`.
- Teacher-free accuracy/loss: BP-KD/objective control
  `0.140625 / 2.75440`; direct ePC `0.0625 / 2.77974`; homotopy ePC
  `0.0625 / 2.78151`.

## Interpretation

**Observed:** the completed reduced harness passes all implemented operational
gates and replays exactly. Factor closure/spill is now emitted per arm, but at
12 updates the values are near chance and not mechanistically interpretable.

**Observed:** direct and homotopy ePC remain at chance accuracy (`1/16`), while
BP-KD is only modestly above chance. This is not an E1 disposition.

**Decision:** the reduced E1 implementation is complete enough for a
calibration-scale local run. The main acceptance JSON remains deliberately
unfrozen because this smoke cannot justify the provisional frontier/rank bars.
No paid run is warranted yet.

At identical smoke scale, eight disjoint seeds project to roughly `2.36 MB` of
raw arrays and `9.0 s` harness time. This is not a GPT-2 resource estimate.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Freeze disjoint 3/5 seed lists and run a larger local calibration campaign with
enough updates to establish a direct-ePC pathology positive control. Only then
freeze numerical bars or consider confirmation.
