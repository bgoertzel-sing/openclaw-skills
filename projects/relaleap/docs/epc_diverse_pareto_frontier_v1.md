# ePC diverse Pareto frontier v1

## Question

Does the semantic-free balanced tiny-transformer fixture contain at least two
ePC configurations that are both viable and conditionally complementary,
rather than merely exhibiting different aggregate failure modes?

## Controls and search space

The matched control is balanced winner assignment at `T=1`, initialized and
trained from the same seed.  The exploration grid changes six interpretable
controls around the existing calibration configuration: settlement depth,
activity relaxation rate, AdamW learning rate, output-error weight,
distillation temperature, and update count.  The grid is curated one-factor
and depth/relaxation coverage, not an exhaustive factorial.

## Splits

- Exploration seeds map the feasible and Pareto sets.
- Selection seeds re-evaluate only exploration-frontier candidates and choose
  at most five representatives.
- Confirmation seeds are untouched until representatives are fixed.  Only
  confirmation can support the `diversely_good` conclusion.

## Metrics and invariants

Every result records exact replay, ePC energy monotonicity, aggregate prototype
coverage NLL, the worst of four context-by-mode prototype NLLs, coherent-mode
coverage, candidate token disagreement, and final-hidden-state effective rank.
A candidate is viable on a split only if every seed replays exactly, remains
energy-monotone, recovers both modes in both contexts, has aggregate NLL no
more than `0.05` above its matched T=1 control, and stays below absolute NLL
`0.40`.

Pareto objectives are: minimize aggregate NLL, worst-regime NLL, and each of
the four context-by-mode NLLs; maximize effective rank and token disagreement.
Numerical dominance requires at least the configured tolerance on one
objective and no degradation beyond tolerance on any objective. The explicit
regime axes were added after v1 exposed that aggregate-only Pareto pruning can
discard the very conditional specialization relevant to an MoE. V1 is
preserved as an aggregate-frontier pilot; v2 uses fresh seeds for every stage.

## Diversely-good gate

At least two confirmation-viable representatives must exhibit a bidirectional
conditional crossover.  For some context/mode regime A must beat B by at least
`0.005` NLL on at least two confirmation seeds, while for a different regime B
must beat A by the same margin on at least two seeds.  This is deliberately
stronger than frontier membership.  Failure means no MoE motivation is
admitted from this fixture; it does not refute other ePC parameterizations.

## Research-rule application

Rules 1, 2, 5, and 7 are primary: validate the Pareto miner on constructed
cases, freeze this specification before execution, preserve exact provenance
and raw JSON, and keep analysis functions independent of the trainer.
