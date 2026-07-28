# Run 20260724T181654Z-e2-calibration-3seed-v1-1-frozen-rerun: e2-calibration-3seed-v1-1-frozen-rerun

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T18:16:54Z`
- Finished: `2026-07-24T18:17:36Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the frozen E2 M0--M5 pipeline run reproducibly on all three calibration
seeds without changing criteria or inspecting confirmation seeds?

## Hypothesis or expected behavior

All seeds should complete on the residual substrate, retain aligned
settled-error/adjoint fields, and produce converged JBD fits.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seeds: `2111, 3253, 4517`.
- Frozen criteria SHA-256:
  `d896798d73052fb327efadfe451c55bd3fe64e4a2f42259a7a3348bc8f1f9720`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/campaign/`; aggregate manifest:
  `artifacts/campaign/aggregate.json`.

## Interpretation

**Observed:** all three seeds completed, all 36 JBD fits converged, and every
seed retained its config, M0 report, shared field NPZ, M1--M5 battery, logs,
and SHA-256 manifest. The output occupied approximately 620 KiB.

**Inferred:** the frozen campaign pipeline is operational. These outcomes did
not alter thresholds; the five confirmation seeds remained untouched.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run the exact frozen five-seed confirmation set and classify only that set.
