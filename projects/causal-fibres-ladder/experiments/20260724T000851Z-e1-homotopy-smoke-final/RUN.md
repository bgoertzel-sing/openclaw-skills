# Run 20260724T000851Z-e1-homotopy-smoke-final: e1-homotopy-smoke-final

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T00:08:51Z`
- Finished: `2026-07-24T00:08:53Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the reduced six-block synthetic-grammar implementation satisfy the E1
operational contract before calibration or paid compute: matched arms, frozen
weights during settlement, a structurally teacher-free evaluator, guarded
activity inference, frontier/rank diagnostics, and deterministic artifacts?

## Hypothesis or expected behavior

All operational invariants and constructed diagnostic fixtures should pass.
This smoke is not expected to decide whether homotopy rescues direct ePC.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Code: branch `agent/e1-guarded-homotopy`, commit
  `2309babd5319a5bfece995fb901033b0619dadec`, based on historical R8
  `ecf2f79db00365a3921152c19a06c1b54ee34771`.
- Config: `configs/e1_homotopy_smoke.json`, seed `1729`; four factors;
  12 matched updates for each of four arms.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/results.json`, `artifacts/results.npz`, and manifest.
- Preflight/regression: 14 tests passed.
- All arms consumed identical samples; every settlement retained byte-identical
  weights; the teacher-free evaluator has no teacher slot; all output is finite.
- Deterministic scientific-payload replay:
  `f1a8a59604f50233f94afd43227426dd1ba91567df7f51e9e978d91a9d2d734e`.
- Byte-identical NPZ replay:
  `2a69e5e6a767e5583ecf20d49aa967b20c1faef154f06b6e5c5a2c22238710f3`.
- Wall time `2.36 s`; peak RSS `294,508 KiB`; harness time `1.114 s`;
  48 arm-updates at `43.09 updates/s`; raw arrays `294,912 bytes`.
- Teacher-free accuracy/loss: BP-KD and objective control
  `0.140625 / 2.75440`; direct ePC `0.0625 / 2.77974`; homotopy ePC
  `0.0625 / 2.78151`.
- Maximum single-block top-5% frontier share: BP-KD `0.3590`, direct ePC
  `0.3796`, homotopy ePC `0.3362`, objective control `0.3590`.
- Minimum teacher-relative block rank: BP-KD/objective control `0.6077`;
  direct/homotopy ePC approximately `0.8487`.

## Interpretation

**Observed:** every implemented operational gate passes, and the scientific
payload plus arrays replay exactly. Constructed late-block, uniform,
sparse-unstructured, and known-rank diagnostics pass.

**Observed:** after only 12 updates, direct and homotopy ePC remain at chance
accuracy (`1/16`); BP-KD is modestly above chance. These values are not an E1
disposition.

**Inferred:** E1 can advance to calibration scale after adding milestone JSONL,
factor closure/spill, explicit retained guard artifacts, and the final
objective-control identity test. The provisional frontier/rank bars remain
unfrozen.

At identical smoke scale, eight disjoint calibration-plus-confirmation seeds
project to about `2.36 MB` of raw arrays and `8.9 s` harness time. This does
not estimate GPT-2 scale and cannot support a GPU request.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Complete the remaining instrumentation, freeze the objective-control
parameterization and disjoint 3/5 seed sets, then run calibration-scale E1-SG.
