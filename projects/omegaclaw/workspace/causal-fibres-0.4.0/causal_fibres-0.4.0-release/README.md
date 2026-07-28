# causal-fibres

`causal-fibres` is a PyTorch-first research toolkit for **comparing and
building structured adaptation systems** on top of existing neural networks.
It supports predictive-coding or error-PC-like residual states, but it no
longer assumes that orthogonal causal fibres are the right representation for
a given model.

The package is designed around a falsifiable sequence:

1. test whether the proposed frozen read interface is observable at all;
2. compare dense adapters, LoRA, SAE-style overcomplete dictionaries,
   orthogonal fibres, grouped sparse dictionaries, and context-dependent
   fibre bundles at matched budgets;
3. test exact-gradient plasticity gates before learning a credit highway;
4. permit controlled low-rank substrate co-adaptation when frozen features are
   the bottleneck;
5. test PC/ePC settlement only after the representation and support-routing
   controls pass;
6. treat learned highways and symbolic caps as later hypotheses that must show
   held-out transfer or genuine test-time inference value.

The initial application remains **partial Transformer distillation**: keep a
competent backprop-trained Transformer intact or nearly intact, learn a small
structured residual system, and evaluate whether that residual is a useful
substrate for continual learning and neural-symbolic caps.

> Status: `0.4.0` is an alpha research release. The conservative terminal
> sidecar, representation contests, observability controls, exact-gradient
> plasticity gates, controlled LoRA co-adaptation, deployment-honest settlement
> evaluation, finite curriculum-order tests, operator audits, and software
> infrastructure are tested. Large-model distributed training, native
> intermediate writes for every model family, automatic structural tensor
> mutation, and a production Hyperon/MORK plugin remain engineering work.

## Scientific stance

The package distinguishes the following claims:

```text
architectural slot          != functional module
functional module           != intervention-aligned module
intervention alignment      != causal identification
causal identification       != long-horizon consolidation
energy descent              != correct causal credit
teacher-clamped settlement  != deployment performance
```

A clean orthogonal common invariant decomposition is one possible model. Real
Transformer representations may instead be overcomplete, superposed, or
context-dependent. Accordingly, the package provides competing representation
classes:

- dense bottleneck residuals;
- sparse autoencoders;
- grouped, possibly overlapping SAE dictionaries;
- orthogonal fibre decompositions;
- context-conditioned fibre bundles with local coordinate charts.

The honest output of an experiment may be:

```text
orthogonal fibres supported
an overcomplete grouped dictionary fits better
context-dependent transports are required
functional modules found but not causally identified
frozen interface is unobservable
operator family is repeated or underidentified
no useful modular decomposition found
```

## Main capabilities

### Representation comparison

- `DenseResidualRepresentation`
- `SparseAutoencoder`
- `GroupedSparseDictionary`
- `OrthogonalFibreRepresentation`
- `ContextualFibreBundle`
- `RepresentationContest`
- `RepresentationSteeringContest`
- SAE feature steering baseline
- matched interpretability-budget reports

### Frozen-interface falsification

- `FrozenReadProbe`
- layerwise observability reports
- teacher-gap capacity curves
- mandatory ordinary BP residual control

### Controlled substrate plasticity

- dependency-free LoRA wrappers
- selected-module low-rank base plasticity
- anchor trust regions
- alternating residual/base training

### PC/ePC residual mechanics

- state-gradient PC
- generic preconditioned PC
- adaptive damped LM/ePC-style settlement
- matrix-free conjugate gradient
- exact predictor-only, free, constrained, and teacher-clamped evaluation modes

### Causal adaptation and continual learning

- exact autograd credit as the conservative default
- responsibility-conditioned gradient gates
- known-support and influence routers
- optional causal error highways
- factor-error encoders, novelty filtering, and coordinate transport
- finite curriculum-order evaluation
- held-out-context routing evaluation
- replay and parameter-isolation baselines

### Structural and causal audits

- Hessian, empirical-Fisher, and Gauss-Newton operators
- robust joint block diagonalization
- overcomplete dictionary-coordinate operator audits
- context signatures and emergence ratios
- intervention engines and causal fingerprints
- repeated-copy and underidentification diagnostics
- conservative module certification ladder

### Symbolic-cap support

- architecture-neutral `TemplateStore` protocol
- static and mutable template stores
- per-fibre symbolic query and feedback head
- explicit separation between API smoke tests and scientific registration tests

## Installation

From the wheel:

```bash
python -m pip install causal_fibres-0.4.0-py3-none-any.whl
```

From source:

```bash
python -m pip install -e .
```

Useful extras:

```bash
python -m pip install -e '.[config]'
python -m pip install -e '.[hf]'
python -m pip install -e '.[dev]'
```

Verify the installation:

```bash
causal-fibres doctor
causal-fibres smoke-test
causal-fibres list-representations
```

## First step: observability, not PC

Before introducing fibres or settlement, train a plain residual on exactly the
proposed frozen features:

```python
from causal_fibres.observability import FrozenReadProbe

probe = FrozenReadProbe(
    input_dim=hidden_size,
    output_dim=vocab_size,
    kind="low_rank",
    capacity=32,
    steps=500,
)

result = probe.fit(
    train_hidden,
    train_base_logits,
    train_teacher_logits,
    validation_hidden,
    validation_base_logits,
    validation_teacher_logits,
)

print(result.teacher_gap_closure)
```

If this control cannot close a meaningful fraction of the teacher gap, change
the read sites, write path, or substrate-plasticity policy before interpreting
PC or causal-routing failures.

## Mandatory representation contest

```python
from causal_fibres.representations import (
    DenseResidualRepresentation,
    SparseAutoencoder,
    GroupedSparseDictionary,
    OrthogonalFibreRepresentation,
    RepresentationSteeringModel,
    RepresentationSteeringContest,
)

models = {
    "dense": RepresentationSteeringModel(
        DenseResidualRepresentation(hidden_size, 64),
        code_width=64,
        output_dim=vocab_size,
    ),
    "sae": RepresentationSteeringModel(
        SparseAutoencoder(hidden_size, 256, top_k=16),
        code_width=256,
        output_dim=vocab_size,
    ),
    "orthogonal": RepresentationSteeringModel(
        OrthogonalFibreRepresentation(hidden_size, 8, 8),
        code_width=64,
        output_dim=vocab_size,
    ),
}

contest = RepresentationSteeringContest(models)
report = contest.fit(
    train_hidden,
    train_base_logits,
    train_teacher_logits,
    validation_hidden,
    validation_base_logits,
    validation_teacher_logits,
)
```

`SAE + steering` is a required rival baseline, not an optional extra.
Orthogonal fibres should advance only if they win, add complementary value, or
provide a continual-learning advantage at a comparable budget.

## Exact gradients plus responsibility gates

A learned credit highway is no longer the default. On a small residual, use
exact autograd credit and apply causal or context responsibility to persistent
plasticity:

```python
from causal_fibres.fibres import ResponsibilityGradientGate

gate = ResponsibilityGradientGate(
    [parameters_for_fibre_0, parameters_for_fibre_1, parameters_for_fibre_2]
)

loss.backward()
metrics = gate.apply(responsibility)
optimizer.step()
```

This directly tests whether learned support estimates protect unrelated
parameters. A highway should be introduced only when exact gradients are
unavailable or expensive, locality itself is a goal, or held-out-context credit
transfer is the hypothesis.

## Controlled base co-adaptation

Freezing is an observability and safety control, not a doctrine:

```python
from causal_fibres.substrate import (
    LowRankBasePlasticity,
    AnchorTrustRegion,
    AlternatingResidualBaseTrainer,
)

plasticity = LowRankBasePlasticity(
    base_model,
    rank=8,
    module_names=["transformer.h.3.mlp.c_proj"],
)

anchor = AnchorTrustRegion(kind="symmetric_kl", radius=0.01, weight=0.1)
```

Use low-rank substrate changes only after recording the frozen observability
baseline. Compare frozen, low-rank co-adaptive, LoRA-only, and ordinary
fine-tuning conditions.

## Deployment-honest settlement evaluation

```python
from causal_fibres.evaluation import FreeSettlementEvaluator

evaluator = FreeSettlementEvaluator(loss_fn)
report = evaluator.evaluate(
    predictor_fn=predictor_output,
    free_fn=free_settlement_output,
    constrained_fn=retrieval_or_rule_constrained_output,
    clamped_fn=teacher_clamped_output,
)
```

The modes have different meanings:

- `predictor_only`: deployable feed-forward sidecar;
- `free_settlement`: no extra test-time information;
- `constrained_settlement`: retrieval, memory, recurrence, or symbolic rules add
  information;
- `teacher_clamped_diagnostic`: oracle analysis only.

PC settlement has no information-theoretic deployment advantage when it sees
only the same frozen features as a sufficiently expressive predictor. A claimed
test-time benefit must come from additional constraints, state, memory, or a
measurable compute/parameter tradeoff.

## Finite curriculum-order evaluation

Local commutators remain useful diagnostics, but long-horizon claims require
actual finite updates:

```python
from causal_fibres.evaluation import FiniteCurriculumLoopEvaluator

report = FiniteCurriculumLoopEvaluator(
    model,
    update_fn=update_one_context,
    output_fn=evaluate_on_fixed_probes,
).evaluate({
    "ABC": ["A", "B", "C"],
    "CBA": ["C", "B", "A"],
    "BAC": ["B", "A", "C"],
})
```

Measure whether local leakage and commutator estimates predict the actual
finite order sensitivity.

## Overcomplete operator audits

The common-block operator model is now complemented by sparse-dictionary
coordinates:

```python
from causal_fibres.operators import audit_dictionary_operators

report = audit_dictionary_operators(
    context_operators,
    sae.dictionary,
    group_membership=grouped_sae.group_membership,
)
```

This reports operator reconstruction, coordinate sparsity, and off-group
coupling without pretending that the overcomplete chart is uniquely
identified.

## Conservative module certification

```python
from causal_fibres.certification import (
    CertificationEvidence,
    ModuleCertifier,
)

result = ModuleCertifier().certify(
    CertificationEvidence(
        unique_ablation_value=0.2,
        intervention_selectivity=4.0,
        intervention_repeatability=0.9,
        routing_precision=0.9,
        routing_recall=0.9,
        off_support_mass=0.05,
        fingerprint_condition=0.2,
        finite_order_distance=0.02,
        context_stability=0.9,
        retention_score=0.9,
    )
)
print(result.status)
```

The certification levels are:

```text
candidate
functional
intervention_aligned
causally_identified
consolidated
underidentified
```

## Recommended Transformer programme

1. **Frozen observability falsifier.** Dense BP residual, LoRA, probes, and
   teacher-gap capacity curves.
2. **Representation contest.** Dense, SAE + steering, grouped SAE, orthogonal
   fibres, and contextual bundles at matched parameters, activity, and compute.
3. **Exact-gradient plasticity.** Known support upper bound, then learned gates,
   replay, and isolation controls. Include held-out contexts.
4. **Controlled substrate plasticity.** Low-rank co-adaptation with anchor trust
   regions.
5. **PC/ePC test.** Compare feed-forward, recurrent, state-PC, and damped ePC at
   matched deployment compute.
6. **Optional highway.** Proceed only if it transfers to novel contexts or
   solves a real locality or cost constraint.
7. **Symbolic cap.** Use large, hard-negative template sets and test whether
   symbolic inference causes selective, correct neural and behavioral effects.

Starting configurations are in `configs/transformer_stage*.yaml`.

## Package map

```text
causal_fibres.core             Types, config, checkpoints, reproducibility
causal_fibres.architectures    Generic, hooked, functional, and HF adapters
causal_fibres.representations  Dense, SAE, grouped, orthogonal, and bundle models
causal_fibres.baselines        LoRA, dense, SAE steering, replay, isolation
causal_fibres.observability    Frozen-read controls and capacity curves
causal_fibres.substrate        Controlled low-rank base co-adaptation
causal_fibres.fibres           Predictors, writers, gauges, plasticity gates
causal_fibres.solvers          State-PC and ePC-like state solvers
causal_fibres.credit           Optional routers, factor errors, highways, transport
causal_fibres.operators        Block and overcomplete operator audits
causal_fibres.interventions    Counterfactual probes and fingerprint tracking
causal_fibres.evaluation       Settlement, matched compute, finite curricula, routing
causal_fibres.certification    Conservative module evidence ladder
causal_fibres.lifecycle        Stable IDs and lifecycle event policies
causal_fibres.training         Distillation, callbacks, schedules, continual tools
causal_fibres.symbolic         Template stores and symbolic heads
causal_fibres.recipes          Stage gates and reference builders
```

## Examples

```bash
python examples/representation_contest_superposition_demo.py
python examples/observability_control_demo.py
python examples/low_rank_coadaptation_demo.py
python examples/finite_curriculum_order_demo.py
python examples/settlement_modes_demo.py
python examples/toy_partial_distill.py
python examples/robust_joint_diagonalization_demo.py
```

## Testing

```bash
python -m pip install -e '.[dev]'
pytest
python -m compileall src
causal-fibres smoke-test
```

## Known limitations

- No software can causally identify modules from insufficient observational
  variation. The package reports underidentification rather than inventing a
  decomposition.
- SAE and dictionary coordinates are not unique causal explanations; they are
  competing functional representation models.
- Contextual bundles currently use small dense Cayley transports and are not
  intended for huge latent dimensions without structured transport plugins.
- Dynamic spawn, split, and merge events are proposed and tracked, but automatic
  tensor resizing with optimizer-state migration remains experimental.
- The generic hook adapter cannot express every model family's cache and suffix
  semantics. Use native adapters for serious intermediate writes.
- Large Transformer LM/ePC runs require practical Fisher, Gauss-Newton, K-FAC,
  or learned metric approximations.
- Local commutators do not replace finite curriculum-order tests.
- Small static symbolic stores verify plumbing, not neural-symbolic scientific
  validity.

## License

Apache License 2.0. See `LICENSE`.
