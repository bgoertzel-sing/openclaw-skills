# Long Distillation Absolute-Floor Follow-up

- Run ID: `20260715T043800Z-long-distill-l001-T4-abs-floor`
- Project: `hdpc-tiny-shakespeare`
- Local or remote: local
- Artifact completion observed: `2026-07-14 21:37:46 PDT`
- Status: aborted by the configured energy-increase guard
- Process state at ledger repair: no matching process running

## Question

Does adding a `1e-12` absolute floor prevent the copied `sshleifer/tiny-gpt2` long-distillation run from tripping the relative energy-monotonicity guard?

## Recorded configuration

- Model: `sshleifer/tiny-gpt2`
- Seed: `0`
- Planned training steps: `300`
- `T=4`, `lambda_lr=0.01`, `beta=2`
- `weight_lr=0.0001`, batch size `4`, sequence length `256`
- Relative early-abort threshold: `0.05`
- Absolute floor reported by the abort diagnostic: `1e-12`

## Observed result

The artifact reports `aborted=true`. The run reached two recorded training steps and then reported:

> Step 2: energy increase `2.78e-08` exceeds threshold `1.93e-08` (`5%` of `|e0|=3.86e-07`, absolute floor `1e-12`).

Initial perplexity was `50186.9921875`; final recorded perplexity was `50192.11328125` (`delta_ppl=5.12109375`). The absolute floor therefore did not resolve the previously observed long-run monotonicity failure at this scale.

## Artifact

- `artifacts/results.json`
- SHA-256: `2dcfb85607dc066748ea9404920be3a4d450636344ea1cb9d9de1b2fda05ee15`

## Provenance limitations

This record was repaired by the 2026-07-14 heartbeat from the surviving JSON artifact after the run had ended. The exact invocation, repository commit/dirty state, environment capture, stdout/stderr, wall-clock start time, and shell exit status were not preserved in this directory and are therefore unknown. The JSON reports `total_time_seconds=9.258249044418335`; this is artifact data, not an independently reproduced measurement.

## Interpretation

Observed: a `1e-12` absolute floor was far below the reported `1.93e-08` relative threshold at the abort point, so it could not change the gate decision. This follow-up supports the existing conclusion that the current tiny copied-student setup needs a materially different guard or model/student initialization before sustained training. It is not evidence about larger models or randomly initialized students.
