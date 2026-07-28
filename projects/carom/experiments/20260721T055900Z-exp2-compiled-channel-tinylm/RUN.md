# RUN: CAROM Experiment 2 — Compiled Channel (TinyLM screen)

- Experiment ID: `20260721T055900Z-exp2-compiled-channel-tinylm`
- Status: completed; one seed, mechanism screen only
- Observed execution: RunPod pod `sgmngeyziytvbv`; CUDA was available, but the run selected TinyLM, not GPT-2.
- Observed effective configuration: `seed=0`, `steps=4000`, `edges=1.0`, `lm_steps=1500`, batch size 128. The log omits the invocation, so these are reconstructed from its default-only output.

## Question

Can a dependency-language compiler produce a useful inhibition graph and ordered itinerary for short compositional transforms?

## Results

Final logged checkpoint (step 3800; saved at step 3999):

| split | task accuracy | edge accuracy | itinerary Kendall tau |
|---|---:|---:|---:|
| L=2..4 | 0.695 | 0.865 | 0.492 |
| L=5 structural holdout | 0.306 | not logged | 0.387 |

Best logged L=2..4 task accuracy was 0.741 (step 3600); L=5 remained
0.147--0.350. Edge accuracy rose from 0.626 to 0.865, while itinerary tau
peaked early (0.990 at step 400) and declined as endpoint performance improved.

## Interpretation

- **Observed:** compiler supervision learned nontrivial edge labels and moderate short-length task performance.
- **Observed:** it did not structurally generalize: L=5 task accuracy was less than half the L=2..4 score.
- **Inferred:** endpoint improvement does not demonstrate that the intended itinerary is the causal computation, because tau degraded substantially during training.
- **Not established:** a language-compilation result. The base was a 0.4M synthetic TinyLM trained on the same finite paraphrase vocabulary; there are no GPT-2, task-only/null/oracle, calibration, or multi-seed results.

## Evidence

- `artifacts/exp2_tinylm.log` SHA-256 `89020404fbde00deab6aa9f0ff0f52a94cc927df4b83abbecafc14ba2dbae9bd`
- The remote checkpoint `/workspace/exp2_tinylm.pt` existed (4.9 MB), but was not retrieved because it is not needed for this interpretation.

## Next required test

Validate the trajectory metric on known positive/negative controls, then run frozen GPT-2 with paired multi-seed compiler-supervised, task-only, oracle, and null controls.
