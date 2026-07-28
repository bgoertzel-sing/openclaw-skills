# Run 20260725T033949Z-e4-quantale-focused-verification: e4-quantale-focused-verification

- Project: `relaleap`
- Started: `2026-07-25T03:39:49Z`
- Finished: `2026-07-25T03:39:51Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the new quantale-weak CMCP implementation pass focused algebra,
distance-correlation, biased-duplicate, order-invariance, and frozen-weight
tests?

## Hypothesis or expected behavior

The biased duplicate with a distinct innovation identity is assigned zero
effective novelty because each raw factor is deterministically related to its
stored counterpart, while an independent repeat retains high weight.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: deterministic unit-test seeds 1, 4--10.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observation: all 9 focused tests passed in 0.89 seconds. In separate
machine-readable calibration and smoke outputs, the selected parameter was
`p=0.05`; mean exact/biased/independent/partial ratios were
`0.0/0.0/0.8709297/0.3630205`, and the seed-61001 biased smoke reported a
distinct innovation identity and biased ratio `0.0`.

Inference: the implementation satisfies the constructed-fixture objective and
the biased smoke invariant. This is local synthetic evidence, not evidence of
performance on naturally occurring duplicate mechanisms.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run broader multi-seed biased experiments before making a scientific efficacy
claim.
