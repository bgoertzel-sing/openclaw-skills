# Run 20260725T034222Z-e4-quantale-biased-smoke: e4-quantale-biased-smoke

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T03:42:22Z`
- Finished: `2026-07-25T03:42:24Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the quantale-weak information ratio suppress a systematic bit-flip packet
when its innovation identity is deliberately distinct from the source packet?

## Hypothesis or expected behavior

The evidence-novelty term should detect deterministic dependence and assign
the biased packet zero weight without provenance deduplication.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed: `61001`
- Frozen calibration parameter: `p=0.05`
- Raw artifact: `../../artifacts/e4-quantale-biased-smoke-v1.json`

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

The original and biased packets had distinct innovation IDs. Quantale-CMCP
assigned weights `1.0/0.0`, matching the oracle and direction-only arms;
naive assigned `1.0/1.0`. Model weights were unchanged. This one-shot smoke
had identical task accuracy (`0.53125`) across all arms, so it establishes an
accounting mechanism, not a predictive advantage.

## Interpretation

**Observed:** The systematic bit flip was suppressed through the
evidence-space dependence calculation rather than provenance grouping.

**Boundary:** Zero novelty follows because each tested binary factor is either
identical to or the deterministic complement of its stored counterpart.
Natural biases, cross-factor transformations, noisy mechanisms, and
out-of-cohort relationships remain untested.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Add provenance-distinct noisy nonlinear transformations, permutation nulls,
and disjoint confirmation seeds before claiming general redundant-mechanism
detection.
