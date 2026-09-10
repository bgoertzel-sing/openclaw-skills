# Tasks

## Next

- [x] Extract HDPC implementation requirements into an executable repository scaffold.
- [x] Build tests before trainers: T1 zero-error identity, T2 anchor, T3 energy monotonicity, T4 BP endpoint, T5 endpoint distinctness, T6 crown identity, T7 toy MLP sPC/ePC equivalence.
- [x] Create Tiny Shakespeare data prep path and a tiny/local smoke config.
- [x] Run the two-step local pretrained-model/data trainer smoke and record inference, perplexity, and per-layer PC/BP metrics.
- [ ] Sweep local ePC error step sizes at `T=2` and confirm strict energy descent before longer training.
- [ ] Verify Runpod account/CLI health and current GPU price/availability before requesting approval.
- [ ] Prepare `experiments/runpod-pilot-001/RUN.md` with exact resource, image, cost/time bound, transfer plan, commands, artifact path, and cleanup plan.

## Later

- [ ] Run bounded Runpod pilot for LoRA homotopy stages `T={1,2}`.
- [ ] Evaluate held-out perplexity delta, PC-vs-BP gradient cosine/norm, tracking residual, equilibrium energy profile, and surprisal-gating histogram.
- [ ] Decide whether evidence justifies stages `T={4,8}`.
- [ ] Prototype detached crown only after base-path diagnostics are sane.
