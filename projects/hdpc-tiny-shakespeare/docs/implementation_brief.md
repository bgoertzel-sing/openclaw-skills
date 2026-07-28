# HDPC Tiny Shakespeare — MVP Implementation Brief

## Scope and constraints

Build a local-first MVP of homotopy-distilled predictive coding (HDPC) on Tiny Shakespeare. Do **not** start Runpod or any paid resources for this phase. The MVP should prioritize catching silent implementation bugs before any scale-up: dropout/cache mistakes, fp32 error handling, detach discipline, and BP-vs-PC endpoint behavior.

Primary sources:
- HDPC draft, especially Appendix A implementation guidance and tests T1-T7.
- ePC paper: error-based predictive coding reparameterizes PC over prediction errors, avoids sPC exponential signal decay in digital simulation, preserves PC equilibria, and reduces to BP at `T=1` or sufficiently small `lambda*T`.

## Minimal model and dataset choice

Use the smallest HuggingFace decoder-only path that still exercises transformer residual streams:

- **Default smoke model:** `sshleifer/tiny-gpt2` or an equivalent 2-layer GPT-2-compatible fixture for CPU/local correctness tests.
- **Tiny Shakespeare pilot model:** GPT-2-small-compatible architecture initialized from open weights if local GPU is available; otherwise keep `sshleifer/tiny-gpt2` until tests pass. Sequence length `S <= 256` for MVP; increase only after T1-T7 pass.
- **Dataset:** Tiny Shakespeare character/text corpus tokenized with the selected model tokenizer. Use fixed train/held-out splits and deterministic dataloader seeds.
- **Training mode:** LoRA by default for homotopy (`rank 8-16` is enough for MVP); full-rank only for toy/local tests or a short consolidation experiment.

## Proposed module layout

```text
hdpc_tiny_shakespeare/
  config.py          # dataclasses; validates alpha=0 during homotopy, use_cache=False, dropout off
  data.py            # Tiny Shakespeare download/load, tokenizer, deterministic train/val batches
  wrap.py            # explicit HF block re-drive; no hooks; zero-error vanilla identity path
  energy.py          # KD-KL, CE for eval only, energy E = 0.5*sum||eps||^2 + loss
  relax.py           # ePC inner loop; toy sPC loop for T7; fp32 errors; detach-local weight pass
  homotopy.py        # lambda/T schedule, hold rule, tracking residual monitor
  crown.py           # zero-init residual crown; identity and detached-relax smoke only in MVP
  metrics.py         # gradient cosine/norm, energy profiles, residuals, ppl deltas, sparsity histograms
  train_distill.py   # Tiny Shakespeare homotopy driver; local only by default
  eval.py            # held-out loss/ppl and teacher delta
  tests/
    test_t1_zero_error_identity.py
    test_t2_anchor.py
    test_t3_energy_monotonicity.py
    test_t4_bp_endpoint.py
    test_t5_pc_endpoint_distinctness.py
    test_t6_crown_identity.py
    test_t7_spc_epc_equivalence.py
```

Keep project artifacts outside source modules, e.g. `artifacts/local-smoke-*`, with configs, logs, and metric JSONL.

## Core implementation rules / numerical invariants

1. **Explicit block re-drive, no forward hooks.** Extract embeddings, transformer blocks, final norm, and LM head. Recompute each block every relaxation step.
2. **Zero-error identity:** with all errors zero, `y_pred(x, zeros)` must match vanilla model logits.
3. **Errors are the only inner-loop optimization variables.** Create per-batch leaf tensors `eps[i]` with shape `(B, S, d)` and `requires_grad=True`.
4. **fp32 errors and energy accumulation.** Even if block compute uses bf16/fp16 later, keep `eps` and energy sums in fp32.
5. **Dropout off, autograd on.** Use eval/dropout-disabled semantics during relaxation and weight-update passes.
6. **KV cache disabled everywhere.** Always pass/configure `use_cache=False`; cached keys/values are stale after error perturbations.
7. **ePC relaxation:** initialize `eps=0`; for `t in 1..T`, compute states sequentially as `s_i = f_i(s_{i-1}) + eps_i`, logits, energy, then SGD-update errors with learning rate `lambda` and no momentum.
8. **Weight-gradient phase:** after relaxation, recompute forward at final errors, form energy, and backprop to weights. Apply detach discipline required by the ePC local rule so gradients are local PC gradients, not accidental end-to-end BP.
9. **Homotopy defaults:** `lambda = 0.05`; stages `T = {1, 2}` for Tiny Shakespeare MVP. Only consider `{4, 8}` after metrics show stability. Do not use CE during annealing (`alpha=0`); use KD from frozen teacher with temperature `beta=2` and the `beta^2` scale factor.
10. **Anchor invariant:** student initialized equal to frozen teacher should have near-zero KD loss and near-zero PC weight gradient.
11. **Tiny numerical tolerances:** prefer fp32 for tests. Typical tolerances: logits max-abs `<1e-4`; KD anchor `<1e-8`; monotonic energy slack `1e-6`; BP endpoint cosine `>0.999`, norm ratio within `1%`.

## Exact tests T1-T7

Write these before trainers and make them pass on the tiny local model.

- **T1 Zero-error identity:** `y_pred(x, zeros)` equals vanilla HF forward logits within fp32 tolerance (`<1e-4` max abs) for 16 random Tiny Shakespeare batches. Verifies PC wrapper / Proposition 1.
- **T2 Anchor:** with `student == teacher`, KD loss `<1e-8`, and PC weight-gradient norm at `T in {1, 4, 16}` is `<1e-6 * typical_finetune_gradient_norm`. Verifies the self-distillation anchor.
- **T3 Energy monotonicity:** on a fixed batch with dropout off, inner-loop energy is non-increasing over error steps for `lambda <= 0.1`, allowing `1e-6` fp slack.
- **T4 BP endpoint:** at `T=1`, ePC weight gradient equals `lambda * BP_gradient` for the same loss: per-layer cosine `>0.999` and norm ratio within `1%`. This catches detach/local-gradient bugs.
- **T5 PC endpoint distinctness:** at large `T` such as `64`, on a perturbed student one SGD step away from teacher, per-layer cosine to BP is measurably `<1` and stable when doubling `T`. This catches “backprop in disguise.”
- **T6 Crown identity at init:** inserting a zero-initialized crown changes no logits; detached crown relaxation with coupling/loss scale `gamma=0` leaves crown residual state `delta=0`.
- **T7 Equilibrium equivalence smoke test:** on a 4-layer toy MLP, long-horizon sPC and ePC reach the same states within tolerance. This rechecks the ePC paper’s core equivalence on a cheap controlled model.

## MVP training/evaluation loop

1. Freeze teacher checkpoint.
2. Initialize student from teacher.
3. Run local correctness tests T1-T7.
4. Run a tiny overfit batch at `T=1` to verify gradients, logs, and checkpointing.
5. Run Tiny Shakespeare KD homotopy with `T={1,2}`, `lambda=0.05`, `beta=2`, `alpha=0`, LoRA enabled.
6. Evaluate against teacher and baseline fine-tune side pass; save metric JSONL and small diagnostic tensors only.

## Metrics to log

Every fixed number of steps:

- Held-out cross-entropy/perplexity and `delta_ppl` vs frozen teacher.
- KD loss vs teacher.
- Per-layer PC-vs-BP gradient cosine and norm ratio on the same batch.
- Tracking residual: EMA over ~100 steps of `||grad_theta E||` at current `tau=lambda*T`.
- Equilibrium energy profile per layer and over relaxation steps.
- Inner-loop energy monotonicity counters / violations.
- Update-sparsity histogram over token positions using per-token output-loss gradient magnitude (surprisal-gating signature).
- Optional: sampled equilibrium errors `(layer, token_position, eps*)` for later steering/vector audits.

## Risks and mitigations

- **Accidental BP instead of PC:** most likely via detach mistakes or too-small `lambda*T`. Mitigate with T4 and T5, and log terminal cosine signatures.
- **Stale KV cache:** causes inconsistent energies. Force `use_cache=False` in config and wrapper.
- **Dropout stochasticity:** corrupts equilibrium tests. Use dropout-disabled eval semantics while preserving autograd.
- **Precision loss:** fp16/bf16 errors can reintroduce signal-decay-like artifacts. Keep errors and energy fp32.
- **Tiny Shakespeare too small:** may hide or exaggerate homotopy behavior. Treat it as an implementation smoke test, not evidence of large-scale validity.
- **Tied embedding / LM-head gradients:** GPT-2 weight tying can double-count or misroute gradients, especially with LoRA. Avoid LoRA on tied tensors or handle both paths explicitly.
- **Cost creep:** any Runpod/GPU pilot must be separately specified and approved with resource, time, and cost caps.
