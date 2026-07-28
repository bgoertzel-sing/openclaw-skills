# Run 20260724T182929Z-e2-c2-dictionary-5seed-v1-1: e2-c2-dictionary-5seed-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T18:29:29Z`
- Finished: `running`
- Status: `running`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can the mandatory C2 dictionary baseline recover factor/selectivity structure
from the identical frozen E2 confirmation fields?

## Hypothesis or expected behavior

The full five-seed run should finish with 60 deterministic SAE fits and
permutation-calibrated M3/M4 scores.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: pending
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The run was manually interrupted after 18 minutes before sealing its first
seed. CPU utilization remained 100% with no stderr. Audit identified a scalar
Python MI loop over roughly 0.7 million atom/factor evaluations. This is a
runtime implementation pathology, not scientific evidence. No result is used.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Vectorize the exact MI statistic, prove equality to the scalar estimator, and
retain a separate rerun.
