# Run 20260727T213214Z-p0-g1-v2-authorized-grid: p0-g1-v2-authorized-grid

- Project: `hdc-cgcct-transformers`
- Started: `2026-07-27T21:32:14Z`
- Finished: `2026-07-27T21:33:37Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes`

## Question

Does the owner-authorized P0-v2 grid restore capacity resolution under the
unchanged P0-G1 gate?

## Hypothesis or expected behavior

The lower-D/higher-load grid should avoid v1 ceiling saturation and show
positive `D/k`--accuracy association for every `(k,M)` curve.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed: `12011`; 2,048 independent trials/cell.
- Grid: `D={32,64,128,256,512,1024}`, `k={32,64,128}`, `M={32,256}`.
- The runner is repository commit `ce7616d`; captured pre-commit source is
  identical to that commit.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Raw artifacts: `../20260727T213117Z-p0-grid-scout/artifacts/v2-smoke/`
  (the output target is recorded verbatim in `command.sh`).
- Payload SHA-256 (both):
  `96f3a7142111828cffa458a59ac35699c6ce0077748a14361063ecc4b4dd14f7`.
- Validator SHA-256:
  `26555155b76fa9312344a6dc4e64827e1ad51efddd0f5fc073b4584e7dbd7558`.
- Tests: 13/13 passed. P0-G1 passed; all six Spearmans are 1.0.

## Interpretation

**Observed:** v2 passes exact replay and the unchanged qualitative gate.
**Inference:** v1 failed due to ceiling saturation, not implementation error.
This is P0 wiring calibration only, not a P1 law or hierarchy result.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Begin CPU-local P1A oracle-code preflight under the frozen P1 plan.
