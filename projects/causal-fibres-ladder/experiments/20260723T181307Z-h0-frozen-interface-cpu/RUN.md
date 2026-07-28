# Run 20260723T181307Z-h0-frozen-interface-cpu: h0-frozen-interface-cpu

- Project: `causal-fibres-ladder`
- Started: `2026-07-23T18:13:07Z`
- Finished: `2026-07-23T18:13:32Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent`

## Question

Can the configured local CPU toy interface produce an admissible H0 record?

## Hypothesis or expected behavior

At least one held-out teacher-gap denominator is positive, allowing the
capacity curve and confidence interval to be evaluated.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seed: `1729`; generator train/validation seeds: `1739`, `1749`.

## Results

- Exit status: 1
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Failed pilot, not H0 evidence. The 180-step student exceeded the oracle
teacher's task loss and matched its perfect accuracy, so both closure
denominators were nonpositive and all task Γ values were correctly undefined.
The serializer then raised `ValueError` while summarizing an empty set of
defined point estimates. Calibration measurements after this run found that 30
student steps yielded held-out loss `0.967670` and accuracy `0.927734`, leaving
a substantive positive gap to the oracle. The production config was changed
to 30 steps and the empty-estimate report path was made explicit.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Rerun as a new immutable experiment after focused tests.
