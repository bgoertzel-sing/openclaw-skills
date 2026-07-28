# RelaLeap SLT Residual-Layer Causal Factors

- Slug: `relaleap`
- Status: `active` (HDPC/ePC Tiny Shakespeare prototype is current first track; SLT and columnar upgrades follow)
- Created: `2026-07-03`
- Last reviewed: `2026-07-27`
- Owner: Benjamin Goertzel

## Purpose

Develop and evaluate adaptive residual-layer learning methods for transformer failure modes. The current first track is an **HDPC/ePC Tiny Shakespeare prototype**: test homotopy-distilled predictive-coding learners and identity-initialized PC crowns as ongoing-learning mechanisms. If this technical track works, later upgrades should add (1) SLT inputs to the process and (2) columnar models for the residual layer.

## Success criteria

- A preregistered train-time design exists with hypothesis, architecture, training procedure, synthetic ground-truth plan, causal audit gates, null controls, and fail-closed criteria.
- Later implementation recovers expected behavior on synthetic regimes: `exact_factorized`, `shared_core_redundant`, `synergistic_pair`, `low_rank_trap`, `oblique_dictionary`, and `random_null`.
- Any promoted residual factorization beats matched flat/SVD/dense controls, beats dependency-aware nulls, passes exact ablation and commutator gates, and shows sparse interpretable LLC interaction structure.
- Reports distinguish prediction, reconstruction, causal modularity, and SLT/free-energy evidence instead of collapsing them into one handcrafted score.
- SLT evidence is considered meaningful only after calibrated finite-sample WBIC/SGLD proxy estimation over actual trained parameter blocks, with sampler diagnostics, explicit WBIC temperature accounting, MAP-reference validation, gauge policy checks, sample-size sensitivity, interaction/null normalization, and finite-sample caveats.

## Scope

### In scope

- Local design and preregistration under `projects/relaleap/`.
- SLT estimator validation package: SGLD/WBIC core, analytic calibration registry, sample-size sweeps, MAP/prior checks, gauge canonicalization, interaction protocols, RelaLeap-shaped benchmarks, nulls, minibatch/preconditioning diagnostics, reporting/CI gates, integration orchestrator, and adversarial reviewer.
- Synthetic ground-truth regimes with known causal structure.
- Train-time residual-column learners with identity initialization, sparse supports, SLT-informed regularizers, and auditable split/merge/transfer events.
- Causal audits: exact ablation calibration, pair synergy, support regret, commutator leakage, off-support leakage, and LLC interaction information.
- Fail-closed decision criteria and null controls.
- Tiny Shakespeare corpus as the first real-text validation target for SLT estimators.
- Tiny Shakespeare corpus as the first HDPC/ePC homotopy-distillation and PC-crown validation target.
- Bounded Runpod GPU execution for HDPC/ePC only after explicit resource/time/cost approval and a remote-job record.

### Out of scope for now

- Unapproved paid or remote compute.
- Pushing branches or opening PRs.
- Claiming real transformer causal columns before synthetic and audit gates pass.

## Current state

On 2026-07-27 Ben supplied a C4′ companion note connecting the V4
commutator critic to Mesto's reported function-pinned PC--GPT-2 homotopy. It
is preserved at `../../library/commutator-critic-c4prime-2026/`. The proposal
is not yet executable: a later Mesto pointer to the public GPL
`MesTTo/metta-on-mork` repository revealed genuine toy `2-2-2` XOR ePC/MORK
settle and local-update code, but inspection of both visible branches/history
found no committed production PC--GPT-2 trainer or checkpoints. The exact
production path/assets therefore remain unidentified. In addition, the
Torch optimizer-replica admission gate remains failed, JAX exact-D is
unreproduced, and no 45-A100-hour run is approved.

The causal-critic persistent-agent plan is now explicitly staged as V4-0
backend admission, V4-1 target-asset/T=1 adapter validation, V4-2 frozen C4′
preregistration and measured microprofile, then a separately approved V4-3
deployment.  This preserves the C4′ conceptual opportunity without treating
author-reported homotopy results as a runnable substrate or opening C2/policy
work prematurely.  See `docs/causal_critic_v4_c4prime_execution_plan_20260727.md`.

Earlier RelaLeap phases did not justify promotion:

1. `v0` seven-arm posthoc pregate was a reproducible smoke scaffold only: small toy data, handcrafted LLC proxy, and no arm beat required null controls.
2. `v2` parameterized arms fitted to cached residuals improved engineering realism but deployable mechanisms failed winner recovery, lost to controls, and failed null specificity.

Ben's 2026-07-03 directive is to **try a new train-time causal factor approach**. The preregistration is recorded at `docs/train_time_causal_factor_preregistration.md`.

Ben's 2026-07-04 directive: make SLT estimator validation the current focus for RelaLeap. Once all estimators are validated on a Tiny Shakespeare level corpus, proceed with the prior idea of using SLT to help guide the residual layer on top of the transformer.

Ben's 2026-07-09 directive supersedes the sequencing, not the validity requirements: try the HDPC/ePC plan first on Tiny Shakespeare, using Runpod compute resources after explicit bounded approval; afterwards consider upgrades using (1) SLT inputs to the process and (2) columnar models for the residual layer.

2026-07-07 implementation status: first-wave SLT estimator sub-branches had already been created by ProtoCosmoBot / related subagents. They were integrated locally into `agent/slt-integration` at commit `6dca8eb`, with 66 tests passing and 7 adversarial-review xfails. The integration includes SGLD/WBIC core, analytic calibration registry, prior/MAP sensitivity helpers, RelaLeap-shaped benchmark fixtures, and adversarial review tests/docs. This is still validation infrastructure, not validated Tiny Shakespeare SLT evidence.

The isolated `agent/tinyshakespeare-hdpc` worktree now contains the original CPU
toy scaffold plus a tested block-state transformer ePC objective and matched
Tiny Shakespeare diagnostic runner. Current head is `65666f9`; 110 full tests
pass at the normalized-objective commit. Two diagnostic-scale three-seed gates
have failed scientific promotion against ordinary KD, so this is implementation
and null-result evidence, not HDPC/ePC efficacy.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Active RelaLeap implementation | not pushed from this workspace | `projects/relaleap/repos/relaleap`; integration worktree `projects/relaleap/worktrees/slt-integration` | `agent/slt-integration` | `6dca8eb` |
| Tiny Shakespeare ePC diagnostic | not pushed from this workspace | `projects/relaleap/worktrees/tinyshakespeare-hdpc` | `agent/tinyshakespeare-hdpc` | `65666f9` (v2 preregistration; normalized objective `cbe4c08`) |

## Environments

No local implementation environment is required for this preregistration. No GPU, paid compute, or remote resources were used.

## Key results

- 2026-07-28: The separately approved RTX 4090 engineering smoke for
  `clean_room_transformer_epc_v1` succeeded and the pod was terminated after
  verified artifact retrieval. A six-layer GPT-2-width student (81.3M
  parameters) and frozen GPT-2 teacher (124.4M) completed one T=1 step using
  3.14 GB peak CUDA allocation; frozen settlement and byte-identical
  snapshot/restore replay both passed. This is an execution/VRAM result only,
  not training-efficacy or Mesto-compatibility evidence. Source commit:
  `b86e156`; evidence:
  `experiments/20260728T195248Z-clean-room-transformer-epc-gpu-smoke/`.

- 2026-07-28: Completed the local transformer-scale PCStep engineering
  preflight at commit `19e1022` on `agent/v4-gpt2-pcstep`. The packaged seam verifies frozen
  weights during GPT-2 block-state settlement, applies exact Boolean block
  gates only at the update phase, and captures/restores model, AdamW, RNG,
  step, and batch-cursor state with deterministic replay. Eleven focused
  adapter tests, 30 broader GPT-2/pilot tests, and the complete 155-test suite
  passed. This is explicitly `clean_room_transformer_epc_v1`: settlement is
  followed by global autograd/AdamW, not a claimed reconstruction of Mesto's
  absent transformer-local rules. Evidence:
  `experiments/20260728T184216Z-v4-1-gpt2-pcstep-preflight/` and
  `experiments/20260728T184406Z-v4-1-gpt2-pcstep-full-suite/`.

- 2026-07-28: The frozen V4-0 nonlinear Torch functional gate completed but
  is INCONCLUSIVE. The >=5-sigma family-admission precheck passed B1 input
  permutation (5.741) but failed B2 output shift (3.033) and B1 high-LR
  stress (0.868). Descriptively, `approximate_full_state_AD` Spearman was
  .969-.9999 across nonlinear cells and non-inferior to frozen-D throughout;
  the high-LR h25 comparison was .969 versus .196. The aligned zero-gradient
  control produced 0% false beneficials. This is not Torch admission.
  Evidence:
  `experiments/20260728T162149Z-v4-functional-gate-nonlinear-torch/`.
  Ben subsequently accepted the result as sufficient to enter V4-1 exact-asset
  intake and `T=1` adapter validation. This is an authorized progression
  decision, not a revision of the preregistered INCONCLUSIVE verdict; no Mesto
  production assets are locally available yet. Contract:
  `docs/v4-1_asset_intake_contract_20260728.md`.

- 2026-07-27: Ben supplied *The Commutator Critic* v1.1, sandbox, and
  `comcrit` skeleton/patch package. The local CPU audit reproduced the complete
  quadratic JSON byte-for-byte, including the per-state truth, synergy,
  insufficient-statistics, and margin-decay demonstrations. The package is not
  yet integration-ready: JAX-dependent exact-D claims remain supplied-only,
  and all four PyTorch optimizer-replica bit-exactness gates failed on Torch
  2.12.1 (`5 passed, 4 failed, 1 skipped`). This supports the V4 conceptual
  pivot but blocks the Torch backend and any C2/policy claim. Evidence:
  `experiments/20260727T080552Z-commutator-critic-v1-1-audit/` and
  `../../library/commutator-critic-v1-1/`.

- 2026-07-25: The frozen co-learned global causal critic Phase-0
  confirmation failed estimation and stopped before policy interpretation.
  Spearman and randomized coverage passed in all four analytic families, the
  synergy global critic reduced pair-action MAE by 21.0% versus the
  independent critic, and the null false-benefit rate was 0%. However, ECE was
  .222-.287 in every family, synergy sign AUROC was .223, and strict baseline
  dominance failed in the exactly linear local/null fixtures. The null family
  also has no positive labels, making its frozen AUROC gate unidentified, and
  the analytic fixture exposes no gradient/activation state for the policy
  credit/rank gate. Do not interpret policy summaries or run Shakespeare.
  Evidence:
  `worktrees/colearned-causal-critic-v1/experiments/20260726T063000Z-colearned-causal-critic-phase0/`.

- 2026-07-25: Implemented the co-learned global causal critic v1 core at
  commit `690c8f7` on `agent/colearned-causal-critic-v1`. The implementation
  includes decision-time feature validation, randomized logged interventions,
  exact learner/optimizer/Python/NumPy/Torch RNG paired restoration, bounded
  training/audit replay, joint module-token and independent critics,
  uncertainty-aware conservative fallback, counterfactual coverage/calibration
  reports, and local/downstream/synergy/null fixtures. Sixteen focused tests
  and the full 448-test suite passed (1 skipped). This is implementation
  evidence only; critic calibration, policy value, and Shakespeare remain
  untested. Evidence:
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/`.

- 2026-07-25: Drafted a preregistered co-learned global causal critic v1
  protocol in response to the v3 support-routing null. The critic is trained
  online from randomized, common-RNG paired update interventions and predicts
  held-out retention/plasticity outcomes over the whole module set. Support,
  curvature, and commutator diagnostics are features rather than imposed
  utility labels. Synthetic local, downstream, synergy, and null fixtures gate
  a contingent local Shakespeare phase; no implementation or execution has
  occurred. Evidence:
  `docs/colearned_global_causal_critic_protocol_v1.md` and
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/`.

- 2026-07-26: Corrected curvature confirmation v3 passed all seven planted
  Phase-0 gates on untouched seeds. Support AUC was 1.0, every module had
  nonzero squared Hutchinson overlap and nonzero `H_B g_A - H_A g_B`, own-task
  pathways were load-bearing, and oracle forgetting was .0697 versus .2010.
  Signed curvature included both cooperative and antagonistic interactions,
  while cross-task ablations were facilitative/suppressive classifications.
  The contingent 15-arm local Shakespeare run then failed its promotion gate:
  full-causal forgetting and finite-update commutator were both worse than
  ordinary ePC. This validates the planted estimator diagnostics but does not
  justify real-text promotion or scale-up. Evidence:
  `experiments/20260726T025745Z-online-causal-epc-v3/`.

- 2026-07-26: The overlapping-vocabulary planted fixture v2 stopped
  fail-closed. It repaired exact architectural disjointness: both tasks had
  nonzero gradients through both paths, support AUC was 1.0, dominant
  own-task ablations were load-bearing, and oracle forgetting improved from
  .2935 to .1172. However, signed mixed-Hessian traces were negative for some
  modules/seeds and the minority block's Task-A ablation effect exceeded .05
  nat. Phase 0 failed; Shakespeare was not run. Evidence:
  `experiments/20260726T023651Z-online-causal-epc-v2/`.

- 2026-07-26: The online multi-signal/soft-gate planted Phase 0 stopped
  fail-closed. Support AUC was 1.0 and oracle gates acted correctly, but the
  protected-block mixed Hessian was already identically zero and exact
  ablations showed the trained planted pathways were not reliably
  load-bearing. The full suite passed 429 tests (1 skipped); Shakespeare was
  not run. Evidence:
  `experiments/20260726T080000Z-online-causal-epc/`.

- 2026-07-26: A preregistered five-arm, three-seed local CPU experiment added
  exact block/head interventions, estimated and true-label support, causal
  gradient gates, clarity pressure, and a differentiable commutator proxy to
  matched-mass complementary-teacher ePC. All 15 records and invariants
  completed, with 424 post-run tests passing. The full arm reduced the direct
  finite commutator by about 11.8% and preserved Task-B loss, rank, and the
  two-block credit wavefront, but worsened Task-A forgetting and did not reduce
  pre-gate off-support leakage. The 6/6 joint promotion gate failed 4/6.
  Estimated supports were seed-unstable, and the true-label oracle did not
  yield a functional advantage. Require a planted modular support fixture
  before another Shakespeare routing run. Evidence:
  `experiments/20260726T003000Z-causal-coding-epc-5arm/`.

- 2026-07-25: A preregistered three-seed, five-arm local CPU experiment tested
  CMCP-guided distillation with and without two-step ePC using 2,000-update
  Tiny Shakespeare students and a frozen CL/representation/robustness battery.
  All normalized-mass and ePC-monotonicity invariants passed. CMCP-ePC improved
  arithmetic adaptation AUC over ordinary ePC (1.994 vs 2.288; lower better)
  but worsened Shakespeare forgetting in every seed (mean 4.868 vs 3.670).
  It had higher rank than ordinary KD but lower rank than ePC and the lowest
  teacher CKA. It beat CMCP-KD only on participation ratio, not any functional
  CL endpoint, so the frozen GPT-2 promotion gate failed and no paid compute is
  justified. Evidence:
  `experiments/20260725T231807Z-cmcp-epc-cl-phase1/`.

- 2026-07-25: The five-step CMCP/ePC identification repair completed locally.
  Fixed KD mass collapsed the original contradictory-fixture arms, confirming
  zero selection-quality identification. A complementary-teacher fixture made
  independent evidence useful. Response novelty beat parameter-gradient
  novelty in calibration and, frozen before disjoint evaluation, improved
  Task-B loss over ordinary by `0.00402` while increasing Task-A forgetting.
  Two-step ePC improved plastic Task-B loss but worsened retention and doubled
  runtime, so direct KD is retained for fast calibration. Existing CAROM E2/E3
  evidence does not yet support a shared novelty-mass ledger. Evidence:
  `experiments/20260725T222650Z-cmcp-mass-normalized/` through
  `experiments/20260725T231500Z-cmcp-carom-bridge/`.

- 2026-07-21: Independent Fable and Sol R9 reviews converged on a three-stage,
  fail-closed representation battery. Low rank, low CKA, or sparsity do not
  establish disentanglement; ePC must show reduced conditional factor leakage
  and selective causal intervention effects without collapse, plus a paired
  functional benefit under an identical adaptation rule. Stage A uses the 20
  saved R8 checkpoints; new training is gated on its success. Evidence:
  `docs/reviews/2026-07-21-r9-representation-battery-synthesis.md`.

- 2026-07-19 16:40: Real-teacher no-update scale audit on seed 3253 found a
  finite credit wavefront: historical T4/lambda.05 ePC gives zero parameter
  gradient to blocks 0-3 and a total gradient norm 4.81 versus 444.38 for
  ordinary KD. T12 technically reaches all blocks, but block-0 credit remains
  negligible. Lambda 5/50 amplifies credit but causes large nonstationarity and
  poor or negative alignment, so naive high-lambda training is rejected.
  Evidence: `experiments/20260719T233948Z-epc-real-teacher-depth-scale-audit/`.

- 2026-07-19 16:33: Corrected real-data representation audit rejected the old
  D3 CKA implementation/claim. Standard centered linear CKA passed symmetry
  and feature-vs-Gram equivalence checks on identical WikiText, TinyStories,
  and random-OOD token matrices. BP checkpoints are highly similar across
  seeds on real data (within-arm mean CKA about 0.84-0.93), while ePC seed 3253
  is a late-layer geometry outlier. The robust descriptive signal is ePC's
  low centered entropy effective rank (about 2.7-3.8 in middle/final layers vs
  23-42 for BP controls). Causation remains unestablished. Evidence:
  `experiments/20260719T233244Z-epc-correctness-audit-v2/`.

- 2026-07-19 14:00: CPU diagnostic battery on 9 saved checkpoints revealed
  low random-probe rank, layer-5 weight explosion (20-40x spectral norms vs
  BP), and a U-shaped post-training CE-gradient profile. Its D3 CKA and D4
  self-teacher sweep are rejected; its causal/configuration interpretation is
  superseded by the Fable/Sol audit ladder. Evidence:
  `experiments/20260719T135900Z-gpt2-diagnostic-cpu-battery/`.

- 2026-07-19: Produced an ASCII-only reproducibility and analysis report that
  separates the six-layer source-distillation result from the independently
  completed outcome battery, summarizes the 9 raw outcome rows and bootstrap,
  provides frozen inputs/reproduction command/artifact hashes, and documents
  interpretation limits. Source/PDF:
  `docs/relaleap_gpt2_six_layer_outcome_report.tex` / `.pdf`.

- 2026-07-19: Run-4 failure-path repairs landed locally at commit `dc61f31`.
  GPT-2 evaluation now restores the explicit batch dimension, outcome loading
  resolves and validates absolute local checkpoint directories, and a versioned
  `set -euo pipefail` launcher gates Stage 2 on Stage-1 success. Focused smoke
  passed 17 tests and the complete suite passed 141 tests with compilation and
  diff checks. This is local systems evidence only; retry compute is unapproved.

- 2026-07-17: Ben selected a six-layer outcome gate followed by a contingent
  twelve-layer confirmation. Commit `7d4d4dc` makes the production runner save
  hash-manifested BP/KD/ePC checkpoints and adds the frozen scalable battery:
  WikiText-103 to TinyStories low-rank adaptation AUC/forgetting, paired
  seed/segment bootstrap, CKA, spectral rank, block skip, and corruption.
  Clean preflight `20260717T154506Z-epc-outcome-6layer-preflight` passed 138
  tests, compilation, and diff check. No RunPod resource has been provisioned;
  the bounded six-layer job awaits explicit approval.

- 2026-07-17: Following Ben's shift toward subtler outcome measures, added a
  deterministic ePC network-outcome battery at clean commit `e398876`:
  common-rule adaptation/forgetting, layerwise linear CKA, effective rank,
  block-skip sensitivity, and token-corruption robustness. All 132 tests passed.
  Local run `20260717T145830Z-epc-outcome-probe-local-v1` reproduced exactly
  (artifact SHA-256 `416bc975...5ae90`). The Tiny Shakespeare chronological
  halves were not a meaningful shift: all arms improved on both domains and
  CKA was approximately 1. Treat as an instrumentation pass and inconclusive
  effect-size pilot, not an efficacy result.

- 2026-07-16: Fail-closed audit after the aborted RunPod attempt found that the
  nominal wall-clock BP+KD control was still capped at 1,000 updates and could
  not consume the ePC time budget. Local commit `d400c15` removes that cap,
  restores preflight-hash/local-only model loading, records deterministic eval
  indices/hashes, and rejects non-finite matched-control metrics and ePC
  energies. Targeted tests passed 11/11 and the full suite 129/129. No accepted
  scientific result exists; another pod requires a fresh job record and Ben's
  explicit bounded approval. A subsequent cleanup audit found and deleted
  out-of-contract retry pod `jnjc7d7y80pxx5`; repeat provider state was empty.

- 2026-07-16: Fail-closed review of the production runner landed locally at
  `e4f2f58`. It corrected a non-time-bounded wall-clock control and two unsafe
  promotion checks, added exact matched-record and public-artifact provenance
  gates, and passed 126 full tests. A spurious automation-authored approval
  claim was withdrawn; the RunPod job remains unapproved and unprovisioned.
  This is implementation/validation evidence only.

- 2026-07-16: Production Hugging Face GPT-2 block-state ePC adaptation landed
  at local commit `0cdc70a`. A two-block GPT-2 configuration matched native
  logits and the exact depth-one KD endpoint; genuine four-state relaxation
  was monotone and produced finite earlier-block gradients. Targeted tests
  passed 19/19 and the full suite 121/121. This is implementation evidence only;
  the production runner/environment/image/runtime/approval gates remain open.

- 2026-07-16: The frozen pilot's two-layer CPU interface gate passed at local
  commit `c310230`: all three frozen seeds and BP+CE/BP+KD/ePC+KD arms ran twice,
  producing nine structured records identical outside elapsed timing. Energy
  and two-block credit diagnostics passed, and 118 full tests passed. This is
  implementation evidence only; the production Hugging Face block-state runner,
  environment lock, GPU smoke/runtime estimate, and approval are still absent.

- 2026-07-16: Frozen the minimum GPT-2-small pilot protocol with pinned public
  model/tokenizer/data provenance, a six-layer GPT-2-width student, explicit
  CE/KD/ePC and separate hidden-match arms, three fixed seeds, structured JSON
  metrics, matched update/time controls, and a pre-run promotion criterion.
  Added validation tests; 113 full tests pass. The RunPod job is an approval
  draft only; protocol commit `886acdc` is local, while the CPU same-interface
  dry-run and immutable deployment pins are
  still incomplete, so this is spec/implementation evidence only.
- 2026-07-15: Implemented a block-state transformer ePC objective and a
  matched-state BP/KD/ePC diagnostic runner (`941b8b3`; 109 full tests passed).
  The first three-seed local gate preserved the exact `T=1` KD endpoint and
  monotone energy/finite-gradient invariants, but no `T>1` arm beat matched KD
  in every seed. Mean BP perplexity was 76.2118; matched KD at lambda 0.05 was
  76.1809; ePC depths 2/4/8 at lambda 0.05 were about 76.1906. Promotion failed
  closed; longer training and crown/head stages remain blocked.
- 2026-07-15 follow-up: gradient diagnostics identified and commit `cbe4c08`
  corrected a batch-normalization mismatch that suppressed hidden local credit
  by `seq_len*d_model`. The synthetic credit invariant and 110 full tests pass.
  A separately preregistered v2 on untouched seeds increased block-1 norm ratios
  to 0.05--0.27 and produced nonzero block-0 credit at deeper inference, but
  still lost to matched KD. At lambda 0.05, mean KD perplexity was 75.1299 versus
  ePC 75.1577/75.1551/75.1503 for depths 2/4/8. The scientific gate remains
  closed.
- 2026-07-14: Added a reusable step-size sweep and diagonal gradient-variance preconditioner for SGLD tuning. Local CPU validation passed 4 focused tests and the complete 97-test suite. Production is gated on a non-divergent pilot with R-hat < 1.2 and mean ESS > 50; see `docs/sgld_tuning_plan.md` and experiment records `20260714T182809Z-sgld-step-size-sweep-targeted` / `20260714T182834Z-sgld-step-size-sweep-full-suite`.

- 2026-07-03: Created local project notebook and preregistered the train-time causal factor learner design: `projects/relaleap/docs/train_time_causal_factor_preregistration.md`.
- 2026-07-03: Drafted SLT estimation validation checklist (`docs/slt_estimation_validation_checklist.md`) with 10 operational gates: parameter block coverage, SGLD sampler diagnostics (ESS ≥ 200, CV < 0.25, ≥ 4 chains), WBIC temperature protocol (β = 1/n log n), known-singularity calibration suite (6 benchmarks with analytical RLCT), regime discriminability, null-normalized uncertainty, finite-sample wording, and promotion decision integration.
- 2026-07-03: Wrote ASCII-only LaTeX/PDF explainer `docs/slt_estimator_implementation_guide.tex` / `.pdf` describing the full estimator implementation pipeline: block masks, WBIC/SGLD sampling, diagnostics, calibration benchmarks, input coverage, module-vs-joint estimates, null-normalized uncertainty, and fail-closed promotion gates.
- 2026-07-04: Preserved Ben's uploaded `Validation of SLT Parameter Estimation for RelaLeap` plan at `docs/relaleap_slt_estimator_validation_plan.pdf` and `library/relaleap-slt-estimator-validation-plan/SOURCE.md` (SHA-256 `0c5a59f2911f1f8cafaf8aa1e3b03d5cb424a0085f4dabf3c2661a2e2707295d`). Added `docs/slt_estimator_validation_plan_summary.md`.
- 2026-07-07: Integrated first-wave SLT implementation branches into `projects/relaleap/worktrees/slt-integration` branch `agent/slt-integration` at commit `6dca8eb`: SGLD/WBIC core, analytic calibration registry, prior/MAP sensitivity, RelaLeap-shaped benchmarks, and adversarial review. Verified locally with `PYTHONPATH=src python3 -m pytest tests/ -q` (66 passed, 7 xfailed) and `git diff --check`.
- 2026-07-09: Implemented the first local HDPC/ePC invariant scaffold in `worktrees/tinyshakespeare-hdpc`: all seven planned test families are represented on a toy MLP/crown reference path; `PYTHONPATH=src python3 -m pytest tests/test_hdpc_scaffold.py -q` gave 9 passed and the full suite gave 102 passed. No remote/paid compute and no push were used.
- Source context: `library/slt-residual-layers/SOURCE.md`, `library/slt-hyperseed-synthesis/`, `library/relaleap-slt-estimator-validation-plan/SOURCE.md`, and `scratch/relaleap_gpt55_pro_final_plan.md`.

- 2026-07-10: Wrote ASCII-only LaTeX/PDF interpretation report for Tiny Shakespeare transformer SLT runs: `docs/slt_tiny_shakespeare_transformer_analysis.tex` / `.pdf`. It explains WBIC/SGLD finite-sample proxy meaning, calibration, lambda-hat, SE, ESS, Rhat, diagnostic-only blocks, per-block results, limitations, and next measurements.

## Open questions

- Where should the eventual implementation live: local `projects/relaleap/repos/`, the Mac-side RelaLeap worktree, or a new coordinated branch?
- What minimal transformer or synthetic-only harness should be used for the first train-time implementation slice?
- What Tiny Shakespeare corpus version and tokenization should be used for the first real-text SLT estimator validation runs?
- What input-count schedule and stopping rule should be used for the first WBIC/SGLD sample-size sensitivity curves? Ben's 2026-07-04 plan proposes `n = {256,512,1024,2048,4096,8192}` and slope-fitting `Delta E_n = a log n + b log log n + c`.
- Which finite-sample WBIC/LLC calibration suite should be implemented first? The 2026-07-04 plan expands the suite to include exact Gaussian posterior, product singularity, nonzero product ridge, cusp/crossing singularities, composition benchmarks, and RelaLeap-shaped cases.

## Related projects and concepts

- SLT and residual layers library record: `library/slt-residual-layers/SOURCE.md`.
- Broader SLT/Hyperseed synthesis material: `library/slt-hyperseed-synthesis/`.
- RelaLeap Mac-side prior work referenced in memory entries from 2026-07-02 and 2026-07-03.

## Risks

- Reconstruction or task-loss gains may be mistaken for causal factorization.
- Sparse columns may merely encode capacity, router frequency, or low-rank structure unless matched controls are strict.
- LLC/WBIC estimates are finite-sample proxies and require calibration before interpretation; never clip negative lambda estimates, and fail/downgrade if MAP reference, sampler target, or Monte Carlo consistency is suspect.
- Uncalibrated, under-sampled, or frozen-parameter SLT proxies could recreate the earlier failure mode; code and preregistration now block scientific promotion without a calibrated SLT evidence contract including input coverage and sample-size sensitivity.
- Synthetic success may not transfer to real transformer residual streams.
- Hidden posthoc leakage into train-time structural decisions would invalidate claims.
- Frontier-model API access may be topic-sensitive: Claude Fable, GPT-5.6-class, or similar controlled models could throttle, downgrade, or refuse advanced neural-network/LLM-development work. Treat this as an empirical operations risk for RelaLeap; record model behavior by task type; keep prompts truthful while deliberately framing work by the immediate legitimate subgoal / nearest safe category (for example SLT estimator validation rather than generic frontier-model optimization); and avoid relying on a single proprietary model for critical estimator or architecture decisions.
