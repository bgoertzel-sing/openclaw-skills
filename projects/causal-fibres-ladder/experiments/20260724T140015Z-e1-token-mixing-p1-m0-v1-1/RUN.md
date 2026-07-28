# Run 20260724T140015Z-e1-token-mixing-p1-m0-v1-1: e1-token-mixing-p1-m0-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T14:00:15Z`
- Finished: `2026-07-24T14:00:24Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does a reduced transformer-like substrate with residual self-attention and
MLP token mixing reproduce Mesto's early-to-middle P1 profile under the same
seed-1729 grammar, probe set, and P1/M0 sweep?

## Hypothesis or expected behavior

Token mixing plus residual paths should distribute settled-field mass farther
upstream than the serial and residual-MLP controls.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed `1729`; identical deterministic grammar/probe construction.
- Six pre-norm residual self-attention/MLP blocks over four virtual tokens.
- KD and teacher-free CE, `T = [1,2,4,8,16,32,64,128]`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/e1_token_mixing_p1_m0_v1_1.{json,npz}` and manifest.
- Focused tests: 16 passed.
- Result SHA-256:
  `037e8c33050b8819af20ee15325a33dd2cd55e4f3ae316c98ec09b963451c633`.
- Fields SHA-256:
  `6e95cca3a73a0d46a9d876eace1b5abe095dec60760a1050c514a775aa63e113`.

## Interpretation

**Observed:** KD and CE again placed 100% of global top-5% squared field mass
in block 6 at every depth. At `T=128`, KD block norms were approximately
`[0, 2.82e-8, 7.03e-6, 3.28e-4, 5.37e-3, 5.72e-2]`; blocks 3--6
epsilon/descent cosines were `[0.487, 0.994, 0.998, 1.000]`.

**Inferred:** this minimal architectural similarity is insufficient to
recover Mesto's profile. The plain residual substrate has slightly better
upstream observability and is selected for the next M0 fast-path check, but
neither substrate is a profile match.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Implement and persist plain teacher-free CE adjoints on the residual substrate,
then complete M0 including explicit depth-profile agreement/null metrics.
