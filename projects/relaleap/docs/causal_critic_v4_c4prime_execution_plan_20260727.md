# RelaLeap causal-critic V4 / C4′ execution plan

Updated: 2026-07-27

## Scope and status

This plan incorporates *The Commutator Critic* v1.1 and the C4′ companion
note.  C4′ is a proposed measurement deployment on Mesto's reportedly
function-pinned PC--GPT-2 homotopy; it is **not** evidence that the critic,
predictive coding, or a routing policy improves continual learning.

**Observed:** the float64 quadratic sandbox reproduced byte-for-byte.
**Observed:** the packaged PyTorch admission suite failed all four functional
optimizer-replica bit-exactness gates on Torch 2.12.1; JAX nonlinear exact-D
claims have not been reproduced. Ben's 2026-07-28 direction is that this
conformance mismatch is diagnostic, not the primary scientific blocker. The
replacement V4-0 gate is an explicitly approximate empirical validation against
the actual `torch.optim` learner. No C4′ run or policy work is admissible until
that gate passes.

Relevant Research Rules: 1 (validate the estimand/backbone first), 2 (freeze
the step and experiment specifications), 4 (reviewable strategic pivot), 5
(reproducible evidence), and 7 (separable backend/adapter/sparsifier seams).

## Persistent-agent priority queue

### V4-0 — empirical nonlinear-tangent admission, local CPU only

1. Retain the four Torch mismatches as a documented conformance diagnostic,
   but label the functional implementation `approximate_full_state_AD`, never
   `exact-D`. Use float64 CPU, deterministic settings, and no AMP, fused, or
   foreach optimizer paths.
2. On the existing V3 three-branch nonlinear MLP/Adam fixture (B1/B2 planted
   conflicts plus high-learning-rate stress), compare tangent predictions with
   direct common-random-number baseline-versus-gated rollouts of the actual
   `torch.optim` learner. Restore full `(theta,m,v,step,RNG,batch-plan)` state.
   Evaluate actions `{layer1,layer2,pair}`, attenuations `{0.5,0.1}`, and
   horizons `{1,2,5,10,25}` at 30 probe states per family.
3. Estimate noise from 64 independent CRN continuations; retain only effects
   `|tau| >= 3 sigma` and require median strong-action effect `>= 5 sigma`
   before confirmation. Freeze train/calibration/confirmation seeds first.
4. Compare `approximate_full_state_AD` to frozen-D on the same qualified
   states. Report full horizon validity and magnitude error, not rank alone.
   JAX reproduction remains a separate portability/reproduction task.

**Gate V4-0:** per admitted family, selected cells require Spearman >= 0.5,
sign AUROC >= 0.75 where identified, planted-pair synergy Spearman >= 0.6,
null false-benefit <= 5%, and a valid cell at `h <= 5`. Full-state AD must be
non-inferior to frozen-D in every admitted cell and improve Spearman by >= .15
in at least one high-LR stress cell. Passing supports only the claim that a
full-state AD tangent is an empirically valid local-response instrument on this
nonlinear fixture; it is not an exact-D, transformer, or C4′ claim.

### V4-1 — make the C4′ substrate inspectable

Obtain from the Mesto owner, preserve, and hash: the exact PC--GPT-2
checkpoints for the anchor/mid/terminal rungs; settle and local-update code;
configs; dataset identities/splits; telemetry; and applicable access/licence
terms.  Implement a narrow `PCStepAdapter` with a pure
`(theta, optimizer_state, batch, t, gate) -> state` interface and a runtime
assertion that weights are frozen during settling.  Begin with `T=1` only.

**Gate V4-1:** target assets import reproducibly; snapshot/restore is exact;
the frozen-weight assertion and adapter unit tests pass; the T=1 adapter
reproduces the selected admitted C4-class exact-D behavior.  Do not use a
missing checkpoint, reconstructed configuration, or unverified production
claim as a substitute.

### V4-2 — freeze C4′ before observing an E-line outcome

Write a one-page bridge preregistration specifying the Task-B domain, the
three tau rungs, matched seeds, `K_mn(tau)` estimand, action table, horizons,
CRN state-restoration protocol, measured floors, validity maps, effect-size
precheck, strict-envelope rule, deviation log, and budget-cut order.  Keep
weight-step gating as the sole C4′ action; settle-side gating is a future,
separately registered C4′′ action family.

**Gate V4-2:** the document is frozen before opening the first E-line seed;
the anchor microprofile measures memory, JVP/HVP and tangent-column cost, and
artifact volume on the actual substrate.  The note's 45 A100-hour figure is
not a resource authorization.

### V4-3 — contingent C4′ deployment (requires explicit compute approval)

If V4-0 through V4-2 pass and Ben approves a specific remote-compute proposal,
run anchor, mid, then terminal rungs under a 45-A100-hour ceiling.  The anchor
must meet Spearman >= 0.4 against paired truth at h <= 10, per seed.  At
settle-bearing rungs report validity maps; run terminal unrolled-vs-IFT and
compressed-settle comparisons at 30 probe states, with cosine >= .95 and
magnitude ratio in [0.5, 2] required to admit either approximation.  Stop on
anchor failure, no valid h <= 5 cell at both settle rungs, or the cost ceiling.

The output is a measurement package: per-seed `K(tau)` exports, validity
radius versus tau, tangent-mode tables, floors, and a Results record.  It is
not a policy recommendation.  C2/real-learner generalization, any critic
router, and the E-line continual-learning comparison remain downstream,
separately gated work.

## Source and evidence boundaries

- C4′ design: `../../../library/commutator-critic-c4prime-2026/SOURCE.md`.
- V4 package audit: `../../../library/commutator-critic-v1-1/SOURCE.md` and
  `../experiments/20260727T080552Z-commutator-critic-v1-1-audit/RUN.md`.
- Mesto material is a proposed substrate; its function-pinning and production
  results remain author-reported until the exact checkpoint/code bundle is
  independently replayed.
