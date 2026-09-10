# Notes

## 2026-07-09 paper implementation anchors

From the HDPC draft appendix:

- Error tensors and energy accumulation should be fp32 even if block compute is bf16.
- Error optimizer should initially be plain SGD with fixed `lambda = 0.05`.
- Weight-update phase recomputes the forward at final errors, forms energy, and calls `E.backward()`; detach discipline is the highest-risk silent corruption point.
- Use gradient checkpointing across blocks.
- Default homotopy schedule: `T = {1, 2, 4, 8}`; first paid pilot should likely stop at `{1,2}`.
- During distillation use KD with `alpha = 0` until annealing completes; do not blend CE early.
- Metrics: PC-vs-BP gradient cosine/norm ratio, tracking residual, per-layer equilibrium energy profile, held-out perplexity delta, update-sparsity/surprisal-gating histogram.
- Tests T1-T7 are required before trainer runs.

Runpod CLI check on 2026-07-09: `runpodctl 2.6.1-32e9aec`; `runpodctl doctor` healthy for API connectivity and SSH key. No pod/resource started.
