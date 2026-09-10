# exp05: Soft-biased ecological autocatalysis

## Status and question

This document specifies the first slice of exp05. The scientific question is:

> Do weak, generic ecological biases increase the probability, size, persistence, or activity of RAF-like organization relative to matched controls, without directly specifying the members or edges of a RAF?

Exp05 should use generated reaction and molecule pools, apply one or more low-information biases before RAF status is known, and compare every treatment with a control that preserves all non-target properties. A positive result requires an effect across held-out seeds and a bias-strength sweep; finding a RAF in one fixture is not sufficient.

The first executable slice implements only catalyst-affinity assignment. It represents atomic molecule names by generic token-incidence signatures, scores a potential catalyst by product-token overlap, and samples from the candidate catalyst pool with weight `1 + overlap`. Its shuffled-affinity control keeps the catalyst pool and the exact per-rule weight multiset but rotates which catalyst receives each weight. It does not yet run ecological dynamics or compute RAF metrics.

## Common generation protocol

1. Generate molecule strings/token sequences from a seed and a declared alphabet/length distribution.
2. Generate reaction templates and reactant/product choices independently of catalysis and independently of any RAF scan.
3. Generate compartment, feed, affinity, and persistence variables from generic molecule/rule features plus seeded noise. No step may inspect a candidate RAF and then add a missing catalytic edge, food molecule, compartment placement, or lifetime.
4. Freeze the generated pool before running the RAF detector or dynamics.
5. Derive treatment/control pairs from the same frozen pool and seed. Controls should preserve rule count, molecule count, resource budget, event opportunity, and the relevant marginal distribution.
6. Run the same bounded dynamics and RAF analysis on both members of each pair. Use separate generation, dynamics, and control-permutation seeds in consequential runs.

Auditable run records should store the generator version, all seeds, generated molecules/rules, bias parameters, permutation used by the control, event trace, abundance snapshots, RAF candidates/cores, and summaries.

## Bias families and matched controls

### 1. Compartment co-localization

**Mechanism.** Assign each molecule and rule/catalyst opportunity a soft compartment-membership vector. Reaction propensity is multiplied by a co-localization factor based on overlap between the reactants' and catalyst's membership vectors. Migration and leakage remain non-zero, so compartments bias encounters rather than forbid them.

**Generation without a wired RAF.** Generate compartment coordinates or memberships from seed-derived molecule features (for example, token hashes or length) plus noise before catalysis and RAF scanning. A rule inherits an encounter location from its reactants or receives a separately generated location. The generator never tests whether moving an item would complete a catalytic cycle.

**Matched null/control.** Permute complete compartment-membership vectors among molecules/catalysts within abundance or length strata. This preserves compartment sizes, migration rates, vector distribution, and global reaction opportunities while destroying feature-to-location correlation. A zero-bias well-mixed treatment is a secondary reference, not the only control.

### 2. Chemical availability

**Mechanism.** Apply soft differences in feed rate, initial abundance, replenishment, or degradation rate. Availability should multiply encounter or firing propensity while retaining a positive floor for all eligible food species.

**Generation without a wired RAF.** Draw resource preferences from generic properties such as molecule length, token composition, or a seeded environmental niche vector. Allocate a fixed total feed/degradation budget before RAF scanning. Do not enrich molecules because they are reactants or catalysts of a discovered RAF.

**Matched null/control.** Permute the complete availability schedules among molecules within food/non-food and length strata, preserving total material input, temporal autocorrelation, abundance distribution, and degradation budget. Also report a uniform-availability reference at the same total budget.

### 3. Catalyst affinity

**Mechanism.** Give every eligible catalyst-rule pair a positive weight

`w(c, r) = epsilon + strength * similarity(c, signature(r))`,

where the rule signature can use reactants, product, or a declared combination. Weighted seeded sampling chooses catalyst assignments or scales catalytic firing rates. `epsilon > 0` keeps the effect soft.

**Generation without a wired RAF.** Generate rule chemistry and catalyst candidates independently, then compute affinity from a generic, predeclared similarity function (token/substring overlap or edit distance). The computation is unaware of RAF membership and cannot add a requested edge. The first scaffold uses product-token overlap, `epsilon = 1`, four candidates, and deterministic seed/tick sampling from integer weights.

**Matched null/control.** For each rule, apply a seeded permutation to the affinity weights across the unchanged catalyst pool. This preserves the candidate set and exact weight multiset (and therefore total catalytic mass) but destroys the molecule-similarity association. The first scaffold uses a transparent one-position rotation; full sweeps must vary permutation seeds and include identity-permutation rejection.

### 4. Spatial/temporal persistence

**Mechanism.** Give compartments, molecules, catalysts, or local reaction contexts finite residence times. Similar items may have correlated retention, adsorption, dormancy, or environmental epochs, increasing repeated encounters without making any interaction permanent.

**Generation without a wired RAF.** Draw lifetimes or persistence-state transitions from generic features plus seeded noise, under fixed mean lifetime and occupancy budgets. Environmental epochs are generated independently of detected chemistry. No lifetime may be extended because its object belongs to a RAF.

**Matched null/control.** Permute complete lifetime/epoch trajectories among matched objects, preserving the lifetime histogram, epoch durations, occupancy, and total active time. A memoryless process with the same mean residence time is a secondary control for distinguishing persistence from mean exposure.

## Measurements and sweeps

All primary comparisons are paired by generated chemistry and reported across seeds with uncertainty, not as a single favorable fixture.

- **RAF rate:** fraction of runs with at least one RAF-like set, plus active-RAF and causal-RAF rates when dynamics/ablation are available. Report paired treatment-control differences and confidence intervals.
- **Core size:** maximal RAF size and greedily minimized or exact bounded core size. Report zero for RAF-negative runs separately from the conditional distribution among RAF-positive runs.
- **Event diversity:** number of distinct fired rule IDs and normalized rule-event entropy; also report catalyzed versus basal event counts so high event volume cannot masquerade as diverse organization.
- **Bias-strength sweeps:** include strength `0`, several weak/intermediate values, and at least one saturation value while holding the resource/catalytic budget fixed. For affinity, sweep the coefficient on overlap while retaining a positive baseline. For each value, run multiple generation seeds, dynamics seeds, and control permutations.

Secondary metrics should include time to first RAF, RAF persistence over windows, productivity, concentration/diversity collapse, compartment occupancy, and ablation drop. Predeclare bounds and avoid selecting the strength after viewing RAF outcomes.

## Difference from exp04

Exp04 is a positive, inspectable, deliberately success-biased fixture. Its rich reaction pool and specificity-filtered template-catalysis facts were chosen to make a RAF likely; its reduction sweep showed that the result is catalysis-map and shuffle-offset sensitive. It is useful for validating rich schemas, RAF pruning, and controls, but it is not evidence of unbiased emergence.

Exp05 instead treats bias as a parameterized population-level statistical tendency:

- rules and candidate catalysts are generated before RAF detection;
- no specific product-to-catalyst cycle or minimized core is selected by hand;
- treatment and null share the same generated chemistry and marginal budgets;
- evidence is a treatment-control change in rates/distributions across seeds and strengths;
- negative and mixed results remain valid outcomes.

The current exp05 scaffold demonstrates only that a generic affinity and matched shuffled-weight seam can be represented and tested in PeTTa. It makes no RAF, emergence, persistence, or ecological-effect claim.

## Immediate implementation boundary and next step

Implemented now:

- token-incidence molecule signatures for `AB`, `AC`, `BC`, and `CD`;
- generic product-overlap affinity `1 + overlap`;
- deterministic weighted catalyst selection and rule assignment;
- a rotated-weight shuffled-affinity control preserving each rule's weight multiset;
- a minimal smoke test.

Next exact step: generate a seed-indexed multi-rule prototype pool and catalyst permutation in PeTTa, instantiate both affinity and shuffled-affinity rule sets, then run the existing bounded RAF scanner on the paired sets to emit the first `RAF rate / core size / event diversity / bias strength` row for strength `0` and `1` without adding any outcome-conditioned edges.
