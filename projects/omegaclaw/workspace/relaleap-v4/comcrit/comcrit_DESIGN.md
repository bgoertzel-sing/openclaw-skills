# comcrit — a grey-box commutator critic as a library

**Status:** design draft v0.1 + working skeleton. Companion to *The
Commutator Critic* (RelaLeap V4 proposal, v1.1) and its sandbox
(`quadratic_demo.py`, `mlp_demo_jax.py`), whose validated logic this
skeleton ports.

**Naming/placement:** the package is written standalone-shaped as `comcrit`,
but is intended to *incubate* as `relaleap.critic` (identical layout, one
namespace prefix) and be extracted to its own repo the week Stage C2 passes,
with the C-stage runners as its integration tests and `RESULTS.md` as launch
evidence. If C2 fails, the extraction is renamed in spirit: same code,
shipped as a *measurement instrument* for CCL/CGCCT confusion structure
rather than as a critic.

---

## 1. Purpose and positioning

`comcrit` measures, for a modular learner mid-training, the causal effect of
gating a module's (or module pair's) incoming-task gradient for one update:

    tau_h^A(S_t, a),  tau_h^B(S_t, a)   — retained / incoming outcome vector

via a **measured analytic backbone** (exact injected perturbation of the
full optimizer state; forward-mode linear-response propagation along the CRN
baseline; cross-curvature synergy terms), with gates, noise floors, and
validity radii as first-class citizens, and a deliberately thin, optional
learned residual.

It is an **instrument, not a framework**: it never owns the training loop,
never routes gradients on its own authority, and always returns a *named
decomposition* of its prediction (first-order alignment, drift,
self-curvature, cross-curvature, propagated response) rather than an opaque
score. The decision layer stays with the host system.

## 2. Scope

**v0.1 (this skeleton):**
- module partitions over arbitrary parameter pytrees / named-parameter dicts
- backbone modes: **exact-D** (default; differentiates through optimizer
  moments), frozen-D (probe-gated optimization), decision-time **preview**
- JAX backend (working, ported from the validated sandbox)
- PyTorch backend draft via `torch.func` + functional optimizer replicas,
  with a mandatory bit-exactness test against `torch.optim` (skeleton
  includes the AdamW replica and the test; marked experimental until the
  test has run on a torch install)
- statistics: Spearman, measured noise floors, 5-sigma effect-size precheck,
  margin qualification, validity-radius maps
- gate suite: backbone-validity, synergy, null, residual-skill (interfaces)
- the block-quadratic fixture with per-state closed-form truth, shipped
  **inside** the library as its own positive control
- `comcrit.selftest()` — reruns C0/C1-style checks on the user's install
- confusion-graph accumulation and export (plain dict; consumers: CGCCT
  commutator loss, HDC footprint sparsifier, later Atomspace typed links)

**Explicitly out of scope for v0.1:** DDP/FSDP, AMP/tf32 (they break CRN
bit-exactness and are excluded on principle for Phase 0), fused/foreach
optimizers, gradient-accumulation schedules, any routing/policy logic, the
residual head's training loop (interface only), fixed-point/IFT semantics
(v0.3, for DEQ/PC-CAROM/FabricPC equilibrium models), GGN/K-FAC surrogates
(v0.3, gated by probe agreement).

## 3. The four portability requirements

The backbone is architecture-blind. A host system integrates by supplying
exactly four things; everything else is comcrit's job.

**R1 — a module partition.** A named map from module -> parameter leaves.
`ModulePartition` produces gate pytrees (leaf -> scalar multiplier) and flat
index masks; dense projector matrices are banned by construction.

**R2 — task oracles.** `loss_A/loss_B(params)`, gradients, and HVPs on the
evaluation objectives. In JAX/torch.func these derive mechanically from the
loss closures; comcrit provides `oracles_from_loss(loss_fn)` helpers.

**R3 — a pure, gated update step.** The single genuine intrusion into user
code:

```python
def step(state, batch, t, gate):        # state: params + optimizer moments
    g = grad(loss_B)(params_of(state), batch)
    g = apply_gate(g, gate)             # after backward, before the optimizer
    return optimizer_apply(state, g, t)
```

The step must be a pure function of `(state, batch, t, gate)` — no global
RNG, no in-place hidden state. This is what makes exact-D possible: the
backbone `jvp`s **through the entire step**, moments included. The sandbox
stress test is the justification: at 10x learning rate, frozen-D collapsed
to Spearman ~0.16/-0.05/0.20 at h=5/10/25 while exact-D held >= 0.997.
Exact-D is therefore the default, and a differentiable, *exactly matching*
optimizer implementation is a first-class deliverable, not a convenience.

**R4 — CRN rollout control.** A `BatchPlan` (deterministic batch sequence
per decision state) and snapshot/restore of the full state. Both arms of
every paired comparison share batches, RNG, and optimizer state at the
snapshot; determinism is a test, not an aspiration.

## 4. The measurement pipeline

```
inject      u = state_gated(t0) - state_base(t0)          # EXACT, full state
propagate   tan_{k+1} = J_k tan_k  via jvp(step)          # exact-D default
project     tau_hat^X_h = < grad L_X (theta_base_{t0+h}), tan_theta_h >
decompose   first_order / drift / self_curv / cross_curv  # named terms
```

- **exact-D**: tangent lives in the full `(theta, m, v)` state; `jvp`
  through the whole step. Cost ~2x a rollout per action; tangents batch.
- **frozen-D**: theta-only tangent, `tan <- tan - lr * D_k * HVP_B(tan)`.
  Admitted only after passing probe acceptance (cosine >= 0.95, magnitude
  ratio in [0.5, 2] vs exact-D at >= 50 states, per stage protocol).
- **preview**: deployment-legal mode; a deterministic preview rollout
  (fixed preview batch) replaces the realized future baseline. Matched
  validation mode to three decimals in the quadratic sandbox; must be
  re-validated per learner (C2 comparison arm).
- **synergy**: `u_m' H_A u_n` (one HVP + one dot), the exact one-step
  pair-minus-singles identity; the additive comparator is *defined* as this
  term deleted.

The contract: `Backbone.measure(...)` returns `BackboneTerms` per
(action, horizon) with every named term populated — the anti-black-box
contract. Gates, residual features, confusion export, and reports all
consume the same decomposition.

## 5. Backends

**JAX (first-class, working).** Steps built from optax or hand-rolled pure
updates satisfy R3 natively; `jax.jvp` + `tree_map` do the rest. The
skeleton ships a reference Adam step and the full backbone.

**PyTorch (draft).** Strategy: `torch.func.functional_call` for the model,
`torch.func.jvp` for propagation, and a small library of **functional
optimizer replicas** (`adamw_step`, `sgd_step`) that must match
`torch.optim` *bit-for-bit* on float64 random problems before use — the
exactness test ships in `tests/test_torch_exactness.py` and is the
admission gate for the backend. Known hazards, handled explicitly:
dropout/data-order RNG capture (require eval-mode or explicit generators in
Phase 0), `.grad` side effects (banned; grads via `torch.func.grad`),
schedule state (fold into `t`).

**Exclusions** (both backends): anything that breaks purity or
bit-determinism — see Scope.

## 6. Statistics and gates as first-class objects

`comcrit.stats`: Spearman; `noise_floor()` from replicate CRN pairs
(>= 64 pairs, >= 20 probe states — *measured, never assumed*);
`effect_size_precheck()` implementing the 5-sigma rule with the bounded
strengthen-and-retry loop (the sandbox caught a live 0.1x-floor synergy
plant with exactly this rule; it is the library's most important function);
margin qualification; validity-radius maps over (h, alpha).

`comcrit.gates`: `validity_gate` (rho >= 0.8, e <= 0.25 inside the declared
region), `synergy_gate`, `null_gate` (analytic nonnegativity in the aligned
family — any violation is a *defect*, halting), `residual_skill_gate`
(do-no-harm inside the radius; earn-your-keep outside). Thresholds are
constructor arguments frozen at instantiation and logged — never module
globals an experiment can quietly edit.

## 7. Built-in positive control and selftest

The quadratic fixture is part of the library, not the experiments: families
(provably-aligned null / local / chain / aligned-rank-1 synergy), closed-form
per-state truth, margin and floor calculators. `comcrit.selftest()` runs in
under a minute on CPU and checks, on the user's actual install:

1. CRN rollout == closed form (<= 1e-8 rel., float64)
2. backbone Spearman >= 0.99 and median rel. err <= 2% on the local family
3. synergy identity exact at h=1; control pairs at numerical zero
4. null family: analytic nonnegativity at every generated state
5. (if JAX present) exact-D backbone >= 0.95 Spearman at h=5 on a miniature
   MLP+Adam run, and frozen-D degradation reported

A failing selftest means the install, not the science, is broken — the same
inversion the fixture performs for the research programme.

## 8. Ecosystem hooks

`comcrit.confusion` accumulates per-state module-level terms into a
confusion-graph estimate `{(m, n): stats}` — first-order conflict on the
diagonal-ish entries, cross-curvature on edges — exportable as a plain dict.
Consumers, in order of adjacency: the CGCCT commutator loss (this graph is
its training signal), the HDC footprint machinery (ANN over footprint codes
proposes edges; measured terms weight them; pair actions instantiate only on
edges), and later a typed-link Atomspace export for MeTTa/PLN-level
reasoning about what to protect. v0.1 ships dict export only.

## 9. Repository layout

```
comcrit/
  DESIGN.md                     this document
  pyproject.toml
  src/comcrit/
    __init__.py                 public API surface
    protocols.py                StepFunction/StateView/Oracles protocols; BackboneTerms
    partition.py                ModulePartition (masks + gate pytrees)
    stats.py                    spearman, floors, precheck, margins, radius maps
    gates.py                    the gate suite
    fixture_quadratic.py        built-in positive control (numpy, float64)
    backbone_jax.py             working backbone: exact-D / frozen-D / preview
    backbone_torch.py           draft backend + functional optimizer replicas
    confusion.py                confusion-graph accumulation/export
    selftest.py                 comcrit.selftest()
  tests/
    test_core.py                fixture + partition + stats + jax backbone
    test_torch_exactness.py     replica-vs-torch.optim bit test (skipped w/o torch)
  examples/
    mlp_jax_example.py          the sandbox MLP demo, re-expressed via the API
```

## 10. Numerical hygiene policy (binding)

float64 for fixture and validity arithmetic; float32 + float64 reductions
for large learners; no AMP/tf32; explicit generators everywhere; eta *
lambda_max <= 0.5 enforced via power-method check; paired statistics only;
per-(family, horizon) train-only standardization for any learned component;
noise floors measured before thresholds are consulted. These duplicate the
V4 doc's Section 9.3 deliberately: the library is where the policy becomes
enforceable rather than advisory.

## 11. Roadmap

- **v0.1** this skeleton hardened; JAX path + selftest green in CI.
- **v0.2** torch backend admitted via the exactness gate; Transformer
  per-head partitions + a GPT-2-small-scale cost profile; preview-mode
  validation on real learners (C2 arm).
- **v0.3** fixed-point semantics (IFT sensitivities with CG solves,
  validated vs nudged finite differences — DEQ / PC-CAROM / FabricPC
  equilibrium models); GGN/empirical-Fisher and K-FAC surrogates behind
  probe gates; HDC-footprint edge proposal.
- **v0.4** residual head reference implementation + calibration; Atomspace
  export.

## 12. Risks

(1) torch functionalization friction — mitigated by the exactness gate and
by shipping JAX-first; (2) exact-D cost at scale — mitigated by tangent
batching and the frozen-D/preview probe path; (3) the deepest one is
scientific, not engineering: if C2 finds no validity radius on real
learners, the "critic" framing dies — the instrument framing, and hence
most of this library, survives.
