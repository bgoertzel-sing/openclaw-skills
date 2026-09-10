# Representation contest

A representation contest is mandatory before making claims about causal fibre
emergence in a pretrained model.

## Candidate classes

### Dense residual

A feed-forward bottleneck or LoRA adapter establishes raw task capacity.

### Sparse autoencoder

An overcomplete dictionary

```math
h \approx D z, \qquad \dim z > \dim h, \qquad z \text{ sparse}
```

models superposition directly and is the main rival baseline.

### Grouped sparse dictionary

Atoms are assigned to possibly overlapping groups. Groups are candidates for
functional or causal modules without requiring orthogonality.

### Orthogonal fibres

A direct-sum representation

```math
\mathcal H = U_1 \oplus \cdots \oplus U_Q
```

is useful when a stable common block structure is supported by context
operators.

### Contextual fibre bundle

Canonical code is transported into a local context chart:

```math
z_{\mathrm{local}} = T_c z_{\mathrm{canonical}}.
```

This captures context-dependent rotations while retaining canonical
intervention and symbolic coordinates.

## Matching budgets

At minimum report:

- total parameters ever trained;
- deployment parameter count;
- mean active features;
- code width and group count;
- training wall clock;
- deployment wall clock;
- reconstruction or predictive loss;
- teacher-gap closure;
- intervention selectivity;
- continual-learning drift.

A model should not win merely because its overcomplete dictionary has several
times the capacity of a competing orthogonal code.

## Package entry points

- `RepresentationContest` for reconstruction-oriented comparisons;
- `RepresentationSteeringContest` for teacher-residual prediction;
- `SAEFeatureSteering` as a direct SAE baseline;
- `audit_dictionary_operators` for operator structure in overcomplete charts;
- `JointBlockDiagonalizer` for common orthogonal block hypotheses.

## Interpretation

A low SAE reconstruction loss does not prove causality. A low JBD off-block
loss does not prove real-world causal meaning. The contest selects useful
representation candidates for later intervention and continual-learning tests.
