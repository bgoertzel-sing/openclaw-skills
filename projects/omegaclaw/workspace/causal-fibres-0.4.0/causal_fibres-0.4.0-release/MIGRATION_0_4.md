# Migrating from 0.3 to 0.4

## Backward compatibility

Existing terminal sidecars, solvers, routers, operator audits, interventions,
checkpoints, and symbolic stores remain available.

## Changed defaults

- `CreditConfig.kind` now defaults to `oracle_gated` rather than `oracle`.
- `CFEConfig` adds `representation`, `substrate`, and `evaluation` sections.
- the conservative representation default is `dense`;
- SAE comparison and observability controls are enabled in evaluation defaults;
- learned highways are no longer the default experimental next step.

## New lifecycle vocabulary

`FibreStatus.CAUSAL` remains as a backward-compatible alias for
`CAUSALLY_IDENTIFIED`. New statuses include `INTERVENTION_ALIGNED` and
`UNDERIDENTIFIED`.

## Recommended code changes

Before constructing a PC sidecar, add:

```python
FrozenReadProbe(...)
RepresentationSteeringContest(...)
```

Before a learned highway, add:

```python
ResponsibilityGradientGate(...)
NovelContextRoutingEvaluator(...)
```

Use `FreeSettlementEvaluator` to separate deployed, free, constrained, and
teacher-clamped results.
