# Run 20260715T154938Z-epc-distillation-gate-v2: epc-distillation-gate-v2

- Project: `relaleap`
- Started: `2026-07-15T15:49:38Z`
- Finished: `2026-07-15T15:49:46Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

On untouched seeds, does batch-consistent local-error normalization make a
genuine ePC depth beat matched BP and ordinary KD while preserving invariants?

## Hypothesis or expected behavior

Expected: corrected normalization materially increases earlier-block credit;
promotion still requires a `T>1` arm to beat both controls in every seed.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Untouched seeds: `73,89,107`; corpus hash and complete configuration are in
  the JSON artifact.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: the correction materially restored local credit. For seed 73 at
lambda 0.05, block-1 ePC/KD norm ratio increased from about `1e-4` in v1 to
0.050/0.136/0.265 at depths 2/4/8; block-0 credit became nonzero at depths 4
and 8 (0.0071 and 0.0404). Cosines stayed near one and all energy/finite-gradient
invariants passed. Nevertheless, every nontrivial arm again failed promotion.
Mean BP perplexity was 75.1650; KD means were 75.1622, 75.1405, and 75.1299.
At lambda 0.05, ePC means were 75.1577/75.1551/75.1503 for depths 2/4/8:
better than BP, but worse than matched KD. Depth 8 cost about 0.232 s versus
0.033 s for KD.

Decision: fail closed again. The software defect was real and is fixed, but
corrected local credit still does not outperform ordinary KD at this scale.
Longer training and columnar/crown/SLT-guided heads remain blocked.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it. Artifact:
`artifacts/epc_distillation_gate_v2_20260715.json`.

## Follow-up

Do not tune the same grid. The next distinct hypothesis should address why
near-collinear but attenuated local gradients lose to KD--for example, a
layerwise target/feedback formulation or compute-matched update scaling--and
must first beat a synthetic known-credit benchmark.
