# Run 20260724T191338Z-e3-calibration-seed-12011-v1-1-rerun: e3-calibration-seed-12011-v1-1-rerun

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:13:38Z`
- Finished: `2026-07-24T19:13:46Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can metered dense/sparse/DGC/supplied-fibre/random/BP conditions distinguish
ID or compositional-shift quality at matched activity-update count?

## Hypothesis or expected behavior

Fill in before interpreting the result.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

All conditions completed with exact meters. The no-update factor interface was
already 100% exact on ID and CS. DGC-20% remained 100%; supplied fibre and
random-20% each missed one of 128 CS examples. This seed validates machinery
and cost accounting but cannot support a quality ranking.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
