# Run 20260725T031000Z-e4-cmcp-biased-smoke-final: e4-cmcp-biased-smoke-final

- Project: `relaleap`
- Started: `2026-07-25T03:10:00Z`
- Finished: `2026-07-25T03:10:06Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can CMCP downweight deterministic one-factor-flip packets while naive
accumulation amplifies their output direction, and is any suppression actually
caused by the Schur-complement conditional information ratio?

## Hypothesis or expected behavior

Naive weighting should assign every biased packet weight 1 and amplify its
effect. CMCP and the oracle should assign the packets approximately zero
weight. The distinctive Schur-complement hypothesis predicts that the raw
conditional information ratio of a biased packet against its clean source is
approximately zero.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed: `61001`
- Config: `configs/e4_cmcp_biased_injection_v1.json`
- Student updates: 75
- Episodes: 6

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifact: `artifacts/e4-cmcp-biased-smoke.json`
- Artifact SHA-256:
  `f32d872506c6b250c12652c18717a0479e91418221c5bb92d2bcee6aaf79a9cb`
- Schema: `causal_fibres.e4_cmcp_biased.v1`
- Episode count / arm count: 6 / 4
- Episode-6 effective precision: naive 15.0, CMCP 8.187655,
  direction-only 1.0, oracle 7.5.
- Episode-6 bias amplification: naive 6.258445, CMCP 0.0,
  direction-only 0.0, oracle 0.0.
- Episode-6 raw biased-packet conditional information ratio: 0.946071.
- All model weights unchanged: true.

## Interpretation

CMCP suppresses every biased packet in this protocol and naive accumulation
amplifies the isolated bias direction by 6.26 times at episode 6. However,
this is not evidence for the Schur-complement claim: CMCP first canonicalizes
packets by `innovation_id`, so the biased manifestations receive zero weight
through provenance deduplication. When the same clean and biased score vectors
are evaluated directly by `conditional_information_ratio`, the ratio is
0.946071 rather than approximately zero. Therefore this run falsifies the
stated raw-score collinearity expectation for the existing `packet_score`
representation while confirming that the broader ledger suppresses the packet
when correct innovation provenance is supplied.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

To test Schur residualization independently of provenance, use distinct
innovation identifiers and define or learn an explicit nuisance/bias-direction
score basis. The current one-bit flip is not linearly redundant under the
standardized packet score.
