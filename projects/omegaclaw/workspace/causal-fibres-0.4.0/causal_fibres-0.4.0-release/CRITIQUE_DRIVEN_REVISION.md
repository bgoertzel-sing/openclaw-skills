# Critique-driven revision in 0.4

Version 0.4 changes the scientific centre of gravity of `causal-fibres`.
Earlier releases treated a fixed orthogonal fibre decomposition as the main
representation hypothesis and placed learned causal highways relatively early
in the experimental ladder. The revised package treats those as hypotheses to
be compared and falsified.

## What the existing evidence established

The earlier toy experiments established conditional mechanics:

- supplied context-local supports can preserve unrelated function exactly;
- energy descent and task improvement do not imply correct causal credit;
- teacher-clamped settlement can be much better than predictor-only deployment;
- repeated isomorphic modules may be numerically fit but not identifiable;
- robust joint block diagonalization can recover exact common blocks when they
  genuinely exist.

They did not establish that realistic Transformer states naturally admit a
small, multiplicity-free orthogonal causal decomposition.

## Changes in 0.4

### Orthogonal fibres are one representation class

The package now compares:

- dense residual bottlenecks;
- sparse autoencoders;
- grouped overcomplete sparse dictionaries;
- orthogonal fibres;
- context-conditioned fibre bundles.

`SAE + steering` is a mandatory baseline for Transformer work.

### Frozen backbones are diagnostic

The first question is whether the selected frozen reads expose the teacher
correction. `FrozenReadProbe`, layerwise observability audits, and capacity
curves make this a formal gate. Low-rank substrate co-adaptation is available
once the frozen control is recorded.

### Exact gradients remain the default

The default credit mode is `oracle_gated`: exact residual autograd combined
with responsibility-conditioned persistent plasticity. A learned highway is an
optional later experiment and must show a locality, cost, or held-out-context
transfer advantage.

### PC settlement is evaluated honestly

The package names four distinct modes:

1. predictor-only;
2. free settlement without new information;
3. constrained settlement with retrieval, recurrence, or rules;
4. teacher-clamped oracle diagnostic.

A clamped result is never a deployment result.

### Finite curriculum loops complement local commutators

Pairwise Hessian or Lie-bracket diagnostics remain useful, but the package now
measures actual finite training orders and repeated context sequences.

### Certification claims are graded

Modules progress through:

```text
candidate -> functional -> intervention_aligned
          -> causally_identified -> consolidated
```

An explicit `underidentified` status is available.

## Revised hypothesis ladder

- H0: the proposed interface is observable;
- H1: some structured representation beats or complements dense and SAE
  baselines at matched budget;
- H2: selective plasticity reduces unrelated drift;
- H3: support estimates generalize to held-out contexts;
- H4: PC/ePC adds sample, robustness, representation, or compute value;
- H5: constrained settlement adds deployment value through new information;
- H6: a learned highway improves locality, transfer, or cost over exact gated
  credit.

Later hypotheses should not be tested as if earlier ones had already passed.
