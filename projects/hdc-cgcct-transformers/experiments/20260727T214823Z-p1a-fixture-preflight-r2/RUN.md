# Run 20260727T214823Z-p1a-fixture-preflight-r2: p1a-fixture-preflight-r2

- Project: `hdc-cgcct-transformers`
- Started: `2026-07-27T21:48:23Z`
- Finished: `2026-07-27T21:48:31Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes`

## Question

Does the new P1A fixture implementation execute deterministically across F0,
F1, F2, and F3 at a non-gating preflight size?

## Hypothesis or expected behavior

The deterministic fixture constructors should produce all requested cells and
the planted F3 coherence measurements without setting a scientific gate.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed: `12011`; 256 trials/cell (preflight ceiling).
- Dimensions: `{64,256,1024}`; loads `{4,16}`; F0 M `{32,128,512}`, F1/F2
  M `32`. This is intentionally a subset of the scientific P1A grid.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Payload: repository-local ignored `artifacts/p1a-preflight-r2.json`, SHA-256
  `f355f3eb7b222dc8959691a922f4fde0b29970a307539fa485275cfba9806626`.
- 30 F0/F1/F2 cells plus six F3 planted hierarchy-distance measurements.

## Interpretation

**Observed:** the 30 fixture cells and six F3 rows completed deterministically.
This is a wiring/runtime preflight only: it is not eligible for P1 laws,
calibration, confirmation, or threshold selection.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Complete the full-grid P1A metric implementation, then run only the three
calibration seeds before freezing criteria.
