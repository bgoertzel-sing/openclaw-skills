# exp06: Bridge-to-ACS favorable-conditions path-search harness design

## Status

Partially implemented. The PeTTa repo now has an exp06 scaffold and a thin CPU-first host-side Dijkstra artifact writer over PeTTa-exposed intervention-cost rows. This document remains the design reference for later dynamic validation slices. The implemented bridge remains diagnostic and does not claim spontaneous ACS emergence.

## Overview and motivation

The exp06 question is:

> Given a verified non-ACS initial soup and an engineered ACS-rich terminal soup, what low-dimensional changes in chemistry conditions make the ACS-rich regime reachable by a short, inspectable path?

The inspiration is Benjamin Goertzel's geoteleomic origin-of-life framing in "Let's Get Chemical": formulate origin-of-life-like transitions as path-ensemble problems, using Schrödinger Bridges / Doob h-transforms to identify minimum-information deformations of native chemical trajectory distributions that land in a life-like target set. In this PeTTa project, exp06 should be the smallest abstract analog of that idea:

- **Initial condition:** a PeTTa chemistry already known to be ACS-negative under existing detectors and dynamics.
- **Terminal condition:** an ACS-rich PeTTa fixture, initially exp04's deliberately success-biased rich RAF chemistry.
- **Bridge/search object:** a shortest or least-cost path through intervention variables such as catalyst-affinity assignment, basal food/replenishment rate, candidate-pool cap, and catalysis-map offset.
- **Scientific output:** a ranked set of "favorable conditions" — minimal variable changes that move the system toward ACS-positive territory.
- **Validation output:** paired follow-up runs showing whether those variables bias unguided or weakly guided PeTTa-native dynamics, without fixing the terminal condition.

The bridge is a **diagnostic** and experimental-design tool. It should not be reported as evidence that ACSs emerged spontaneously. In particular, a path from a hand-engineered non-ACS soup to a hand-engineered ACS-rich soup only tells us which parameter directions are compatible with ACS formation in this toy system. It does not establish an unbiased emergence rate.

## Existing infrastructure to reuse

- **exp00:** PeTTa-native deterministic chamber kernel, seeded choice, candidate caps 2--8, chamber ticking, state accessors.
- **exp01:** planted ACS recovery, RAF-like detectors, ablation protocol.
- **exp02:** random catalytic polymer records and pair/triple/quadruple/quintuple/sextuple/septuple catalytic-cycle scanners; generated-unplanted seeds remain zero-active under existing scanners.
- **exp03:** multi-tick deterministic chamber dynamics, bounded candidate selection, run-records, exports, and file bundles for productive cap runs.
- **exp04:** success-biased rich RAF fixture and reduction sweep. It gives a useful positive terminal, with maximal RAF size 15 and greedy core size 2 (`lCD`, `lBCD2`), but it is catalysis-map-sensitive and not an unbiased-emergence claim.
- **exp05:** catalyst-affinity scaffold: token-overlap weights, positive baseline, rotated-weight controls, and projection into ordinary exp00 `candidate` / `candidate-pool` atoms. It is the natural entry point for affinity interventions.

## Design principles

1. **PeTTa-native chemistry boundary.** Chamber dynamics, candidate construction, candidate selection, catalysis facts, abundance updates, event traces, and RAF/ACS detection stay in MeTTa/PeTTa atoms.
2. **Host-side search only.** Python may enumerate intervention settings, call PeTTa queries, compute graph shortest paths, serialize artifacts, and generate reports. It must not implement alternative chemistry dynamics.
3. **Tiny deterministic state spaces first.** Start with a small discrete lattice. Avoid remote compute and avoid stochastic claims until the deterministic harness is verified.
4. **Treatment/control pairing.** Every favorable-condition setting should have matched controls preserving marginal budgets where possible: e.g. same affinity weight multiset under rotated assignment, same basal budget, same cap, same rule pool.
5. **Multi-objective scoring, no single magic metric.** Report functional and conversion-like scores separately. Do not collapse them into one scalar unless the weights are predeclared and sensitivity is reported.
6. **Fail-closed claims.** If a path exists only because the terminal is hand-engineered or because a control also becomes ACS-positive, report that plainly.

## State-space definition

The path-search state is not the full chemical soup state. It is an **intervention-setting vector** whose evaluation is performed by PeTTa-native dynamics and RAF detection.

### State vector

Initial exp06 should use a discrete lattice:

```text
x = (
  affinity_mode,
  affinity_strength,
  catalyst_offset,
  basal_interval,
  candidate_cap,
  protected_release_mode,
  protected_release_strength
)
```

The first implementation may omit protected-release variables until the base bridge harness works, but the design should reserve fields for them.

### Variable 1: `affinity_mode`

Purpose: choose how catalyst affinities are assigned or controlled.

Recommended discrete values:

- `none`: no catalyst affinity beyond baseline / no-catalysis where appropriate.
- `uniform`: all eligible catalyst-rule pairs have identical positive weight.
- `token_overlap`: exp05-style generic product-token overlap affinity.
- `rotated_control`: matched rotated-weight control preserving each rule's weight multiset.
- `terminal_specific`: exp04-style specificity-filtered catalysis. This is allowed only as an endpoint/control anchor, not as a generated favorable-condition claim.

PeTTa-side representation:

- PeTTa should expose named rule/catalyst assignments or candidate pools for each mode.
- Host selects the mode by querying a PeTTa atom such as `(exp06-condition-candidate-pool <mode> <strength> <offset> ...)`, once implemented.

Host-side role:

- Enumerate modes and map them to PeTTa queries.
- Treat `terminal_specific` as high-cost because it encodes hand-engineered target structure.

### Variable 2: `affinity_strength`

Purpose: scale generic affinity without outcome-conditioned edge insertion.

Recommended first values:

```text
0, 1, 2, 4
```

Interpretation:

- `0` means baseline-only / uniform positive floor.
- Higher values multiply the token-overlap component while keeping epsilon positive.

PeTTa-side representation:

- Integer weights are easiest initially: `w = epsilon + strength * overlap`.
- Keep `epsilon = 1` for all eligible catalyst-rule pairs.

Host-side role:

- Enumerate values and record the exact formula in each run artifact.

### Variable 3: `catalyst_offset`

Purpose: represent exp04's catalysis-map rotated controls and test sensitivity to how catalyst weights are assigned.

Recommended first values:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

Interpretation:

- `0` means identity or baseline assignment, depending on mode.
- Nonzero offsets rotate catalyst assignment among eligible catalysts.
- Offset should preserve candidate set and weight multiset where used as a control.

PeTTa-side representation:

- PeTTa should expose offset-specific catalysis facts or assigned rules.
- exp04 already provides offset-sensitivity precedent; exp06 should not reinvent it in Python.

### Variable 4: `basal_interval`

Purpose: control food/replenishment or basal uncatalyzed event frequency.

Recommended first values:

```text
none, 8, 4, 2, 1
```

or as integers:

```text
0, 8, 4, 2, 1
```

where `0` means no basal replenishment / no basal rescue, and smaller positive intervals mean more frequent basal support.

PeTTa-side representation:

- PeTTa dynamics should decide whether a basal feed or floor is applied at a tick.
- Host should not mutate abundance traces directly.

### Variable 5: `candidate_cap`

Purpose: vary per-tick visibility/choice among generated reaction candidates.

Recommended first values:

```text
2, 3, 4, 5, 6, 7, 8
```

PeTTa-side representation:

- exp00 already supports deterministic candidate caps 2--8.
- exp03 already tests productive cap runs. exp06 should reuse these seams.

Interpretation caveat:

- Larger candidate cap can make more reactions visible, but also changes event opportunity. Report this as an intervention, not as a neutral parameter.

### Variable 6: `protected_release_mode`

Purpose: turn value-relative anti-precedence on/off and choose the rule family scope.

Recommended first values:

- `off`
- `family_share`
- `motif_neighborhood`

First implementation should use `off` and `family_share`. `motif_neighborhood` can wait until motif neighborhoods are represented robustly.

### Variable 7: `protected_release_strength`

Purpose: penalize excess canalization.

Recommended first values:

```text
0, 1, 2
```

This variable should initially be diagnostic or weak. Strong release can destroy recurrence and therefore destroy individuation, which is exactly the failure mode the substack post warns against.

## Initial and terminal conditions

### Initial condition candidates

Use more than one initial anchor, but start with one tiny deterministic anchor.

#### Initial A: exp04 no-catalysis / RAF-negative control

- Same broad exp04 rule vocabulary as the rich fixture, but no catalysis or a matched no-catalysis mode.
- Known to be RAF-negative in exp04 reduction controls.
- Advantage: close to the terminal fixture, so the path search can be small and interpretable.
- Risk: because it shares the terminal hand-designed rule pool, shortest paths may reflect exp04 engineering rather than generic emergence.

#### Initial B: exp02 generated-unplanted ACS-negative seed

- Use one of the generated-unplanted exp02 seeds with zero pair through septuple active cycles.
- Advantage: stronger negative-control provenance.
- Risk: farther from exp04 terminal; path may require changing too many structural variables not represented in the first lattice.

Recommended first harness: **Initial A**, then repeat with **Initial B** after the search machinery works.

### Terminal condition candidates

#### Terminal T1: exp04 rich RAF fixture

- maximal RAF size: 15
- greedy core size: 2
- known core: `lCD`, `lBCD2`
- productive 56-tick dynamics under success-biased setting

This should be the first terminal because it is already positive and inspectable.

#### Terminal T2: exp05 affinity-derived positive, if found later

If exp05 later produces a generic-affinity positive across paired controls, exp06 should add it as a less engineered terminal. Until then, exp04 remains a validation anchor, not a natural-emergence endpoint.

### Target-set predicates

Define several predicates rather than one monolithic terminal condition.

#### Functional target

A condition is functionally ACS-positive if:

```text
maximal_raf_size >= 1
and dynamic_event_count >= min_events
and distinct_productive_rule_count >= min_distinct_rules
```

Recommended first thresholds:

```text
min_events = 1 or 4 for smoke; 16 for consequential exp04-like runs
min_distinct_rules = 1 for smoke; 2 or more for consequential runs
```

The smoke threshold can be permissive; the report must label it as smoke.

#### Core target

A condition reaches a core target if:

```text
greedy_core_size >= 1
and greedy_core_size <= max_core_size
and core_replay_or_ablation_drop is positive when available
```

Recommended first `max_core_size = 4` to prefer compact ACS-like organization.

#### Conversion-like target

PeTTa-chem lacks membrane mass, so define a membrane analog carefully.

First conversion proxy:

```text
conversion_score = target_product_count / (basal_event_count + catalyzed_event_count + resource_cost_floor)
```

Possible target products:

- exp04 productive products associated with the rich RAF core;
- later, a declared `M` or `membrane_analog` product family.

Do not retrofit a membrane analog after seeing which products win. The product family must be declared before the run.

#### Terminal exactness target

A condition reaches exact terminal only if it reproduces the exp04 terminal core or maximal RAF. This is useful for path anchoring but should not be the main favorable-condition predicate, because exact terminal reproduction is too hand-engineered.

## Path-search algorithm

### Graph model

Build a graph over discrete intervention settings.

- Node: one intervention vector `x`.
- Edge: one allowed atomic change in one variable.
- Edge cost: information/deformation cost of that change.
- Node evaluation: PeTTa-derived metrics for dynamics and RAF/ACS status under `x`.

### Edge definitions

Allowed single-step moves:

- increment/decrement `affinity_strength` by one level;
- switch `affinity_mode` along a predeclared partial order;
- rotate `catalyst_offset` by one step or jump to any offset with cost proportional to circular distance;
- increment/decrement `basal_interval` along ordered levels;
- increment/decrement `candidate_cap` by 1;
- turn protected release on/off or increment strength by one level.

Do not allow a single step that changes both rule pool and catalysis map unless explicitly encoded as a high-cost macro edge.

### Cost function

Use additive edge costs with transparent components.

Example initial cost:

```text
cost(x -> y) =
  w_mode      * mode_change_cost
+ w_strength  * abs(level_index(strength_y) - level_index(strength_x))
+ w_offset    * circular_offset_distance(offset_x, offset_y)
+ w_basal     * abs(level_index(basal_y) - level_index(basal_x))
+ w_cap       * abs(cap_y - cap_x)
+ w_release   * release_change_cost
+ w_terminal  * terminal_specific_penalty
```

Recommended defaults:

- small cost for smooth strength/cap/basal changes;
- moderate cost for offset changes;
- high cost for switching to hand-engineered `terminal_specific` mode;
- high or infinite cost for changes that inspect RAF membership before assigning edges.

The exact weights must be recorded in the artifact. Run a sensitivity report over at least two alternate weight settings before making claims about minimality.

### Evaluation cache

Each node evaluation may require running PeTTa queries. Cache by canonical intervention vector:

```text
cache_key = sha256(json_canonicalize(x) + peTTa_commit + query_version)
```

Node evaluation result should include:

- PeTTa query expressions used;
- run IDs / config IDs;
- event metrics;
- RAF metrics;
- score vector;
- stdout/stderr snippets or log paths;
- exit status.

### Algorithm choice

#### First implementation: Dijkstra to first target

Use Dijkstra because edge costs need not be uniform and the lattice is tiny.

Pseudocode:

```python
def dijkstra_to_target(start, is_target, neighbors, edge_cost, evaluate):
    pq = PriorityQueue()
    pq.push((0, start))
    dist = {start: 0}
    prev = {}
    eval_cache = {}

    while pq:
        cost_x, x = pq.pop_min()
        if cost_x != dist[x]:
            continue

        metrics_x = eval_cache.get(x)
        if metrics_x is None:
            metrics_x = evaluate(x)          # calls PeTTa, no host chemistry
            eval_cache[x] = metrics_x

        if is_target(metrics_x):
            return reconstruct_path(prev, x), eval_cache

        for y in neighbors(x):
            step = edge_cost(x, y)
            alt = cost_x + step
            if alt < dist.get(y, float("inf")):
                dist[y] = alt
                prev[y] = x
                pq.push((alt, y))

    return None, eval_cache
```

#### Second implementation: multi-target Dijkstra / Pareto frontier

After smoke validation, do not stop at the first target. Collect:

- cheapest path to any functional target;
- cheapest path to any conversion target;
- cheapest path to compact-core target;
- top-k paths per target;
- Pareto frontier over `(path_cost, maximal_raf_size, conversion_score, event_diversity, control_delta)`.

#### Optional A*

A* is not needed initially. A heuristic such as negative RAF-size gap is tempting but requires evaluating neighbors anyway and can bias interpretation. Add A* only if the lattice grows large and the heuristic is demonstrably admissible or clearly labeled as approximate.

### Handling expensive evaluations

The first lattice should be small enough that exhaustive Dijkstra is feasible. Example cardinality if protected release is off:

```text
5 affinity modes * 4 strengths * 10 offsets * 5 basal levels * 7 caps = 7000 nodes
```

This may still be too many if each node runs a full 56-tick PeTTa scenario. The first smoke lattice should be much smaller:

```text
3 modes * 2 strengths * 3 offsets * 2 basal levels * 3 caps = 108 nodes
```

Use staged expansion:

1. tiny smoke lattice;
2. exp04-focused lattice;
3. sensitivity lattice;
4. generated-seed lattice.

## ACS-distance scoring

The evaluation result should be a vector, not just a scalar:

```text
metrics(x) = {
  maximal_raf_size,
  greedy_core_size,
  dynamic_event_count,
  catalyzed_event_count,
  basal_event_count,
  distinct_productive_rule_count,
  rule_event_entropy,
  target_product_count,
  conversion_score,
  ablation_drop,
  control_delta,
  target_predicates
}
```

### Functional bridge score

Analog of the substack "functional bridge": favor productive ACS/RAF organization of any useful type.

Example scalar for ranking only:

```text
functional_score =
  a1 * log1p(maximal_raf_size)
+ a2 * log1p(dynamic_event_count)
+ a3 * rule_event_entropy
+ a4 * ablation_drop
- a5 * decoy_or_shuffle_positive_penalty
```

Use this for reports and Pareto sorting, not for PeTTa dynamics.

### Conversion bridge score

Analog of the substack "conversion bridge": favor conversion efficiency toward a declared output.

```text
conversion_score =
  target_product_count / (1 + resource_cost + basal_event_count + decoy_event_count)
```

If no membrane analog exists, the declared output can be a predeclared exp04 product family, but label it as a proxy.

### ACS distance

A simple distance-to-target for plotting:

```text
distance_functional =
  max(0, raf_threshold - maximal_raf_size)
+ max(0, event_threshold - dynamic_event_count) / event_scale
+ max(0, diversity_threshold - distinct_productive_rule_count) / diversity_scale
```

A conversion distance:

```text
distance_conversion = max(0, conversion_threshold - conversion_score)
```

Report these as diagnostic distances, not as physical thermodynamic distances.

### Control-aware scoring

A favorable condition is stronger if it beats matched controls:

```text
control_delta_raf = maximal_raf_size_treatment - maximal_raf_size_control
control_delta_conversion = conversion_score_treatment - conversion_score_control
```

For exp06, controls can include:

- rotated catalyst offset;
- no-catalysis;
- uniform affinity;
- same budget with shuffled affinity weights.

If treatment and control both reach ACS-positive territory, report sensitivity rather than clean evidence.

## Protected-release integration

Protected release should be designed as both an intervention and an analysis lens.

### Conceptual mapping

From the substack post:

```text
O_g = max(S_g - S*_g - theta, 0)
```

where:

- `g` is a pathway family or motif family;
- `S_g(t)` is actual recent ecological share;
- `S*_g(t)` is value-justified share, e.g. a softmax over recent value scores;
- `theta` is a tolerance margin;
- reactions have protection coefficients `c_r` so shared functional machinery is protected more than identity-specific cycling.

### Pathway families in PeTTa-chem

Start with simple family definitions already present or easy to expose:

- exp04 template family: ligation / cleavage / modification;
- exp04 motif/core neighborhood: rules sharing products/reactants with `lCD` or `lBCD2`;
- exp03/exp02 family labels: P/Q/R/S seed families;
- exp05 affinity groups: product-token-overlap buckets.

First implementation should use **rule family labels**, not inferred motifs, to avoid accidental host-side chemistry inference.

### Actual share `S_g`

Compute from PeTTa event logs:

```text
S_g = events_in_family_g / max(1, total_productive_events)
```

Use a sliding window only after fixed-window totals work. PeTTa should expose event records; host may aggregate by predeclared family labels.

### Value score and value-justified share `S*_g`

First value proxy:

```text
value_g = target_product_count_g / (1 + event_count_g + resource_cost_g)
```

Then:

```text
S*_g = softmax(beta * value_g)
```

For a tiny deterministic first pass, use a rational or fixed lookup approximation if PeTTa needs to expose it. Host-side computation is acceptable for the path-search analysis, but if protected release changes dynamics, the resulting adjusted weights must be represented back in PeTTa as explicit condition atoms.

### Protection coefficient `c_r`

Define:

```text
release_penalty_r = lambda * O_family(r) * (1 - c_r)
```

Initial coefficients:

- `c_r = 1.0` for declared shared functional / conversion machinery;
- `c_r = 0.5` for generic productive transformations;
- `c_r = 0.0` for identity-specific overcycling / decoy loops.

In exp04, these labels must be predeclared. Do not assign `c_r` after looking at which rules form the winning core unless the assignment is explicitly an analysis of the engineered terminal.

### How protected release enters exp06

Two phases:

#### Phase 1: post-hoc path analysis

For every evaluated node, compute:

- family shares `S_g`;
- value scores;
- excess canalization `O_g`;
- rules that would receive release pressure.

This does not alter dynamics and is safe for the first harness.

#### Phase 2: intervention variable

Introduce protected release as a transformation from baseline affinity weights to adjusted weights:

```text
w'_r = max(epsilon, w_r * exp(-release_penalty_r))
```

or, integer-friendly first version:

```text
w'_r = max(1, w_r - round(release_penalty_r))
```

PeTTa should receive the adjusted weights as explicit condition facts generated by a documented host analysis step, or PeTTa should compute the small integer adjustment if feasible. In either case, the dynamics run from adjusted weights must still be PeTTa-native.

### Risk

Protected release can make the harness circular if `value_g` is defined using future target success. Use only recent or same-run event/output quantities available before target classification, and label any terminal-informed variant as retrospective analysis.

## PeTTa-native / host-side boundary

### Must stay PeTTa-native

- reaction/rule definitions;
- molecule/state facts;
- candidate-pool construction;
- seeded candidate selection;
- chamber tick and multi-tick dynamics;
- abundance updates;
- event logging;
- catalysis facts and assigned-rule projections;
- ACS/RAF scanner predicates;
- run-record or run-file-bundle atoms.

### Allowed host-side operations

- enumerate intervention vectors;
- generate a condition manifest that selects among PeTTa-exposed modes;
- call PeTTa queries/scripts;
- parse PeTTa output atoms;
- compute shortest paths / Dijkstra / Pareto frontier;
- compute aggregate scores from PeTTa-emitted metrics;
- serialize artifacts to JSON/Markdown;
- render plots/reports later.

### Operations that straddle the boundary

Some operations need special care:

1. **Affinity-weight adjustment.** Host may compute path-search settings and protected-release adjustments, but adjusted weights used by dynamics must be materialized as PeTTa condition atoms and recorded.
2. **Family share aggregation.** Host may aggregate PeTTa event logs by predeclared family labels. It must not infer new reaction semantics unless those semantics are declared and reproducible.
3. **Target-product conversion proxy.** The target product family must be declared before evaluation. Host may count PeTTa-emitted products.
4. **Control construction.** Host may choose the offset/permutation seed; PeTTa should expose the resulting rotated-control assignments or verify them.

Clean boundary test:

> If the host path-search code is removed, each evaluated node should still be reproducible by a named PeTTa query or script that emits a run record for that exact condition.

## Artifact format

Write artifacts under an exp06 run directory, e.g.:

```text
projects/petta-chem/experiments/exp06_bridge_<YYYYMMDD>/
  RUN.md
  CONFIG.json
  NODE_EVALUATIONS.jsonl
  PATHS.json
  SCORE_TABLE.csv
  CONTROLS.md
  SUMMARY.md
  peTTa_queries/
    <condition-id>.metta-query.txt
  run_bundles/
    <condition-id>/
      CONFIG.metta
      EVENTS.metta
      METRICS.metta
      ACS.metta
      SUMMARY.metta
```

### `CONFIG.json`

Contains:

- git commit of petta-chem repo;
- PeTTa runtime info;
- exp06 harness version;
- state variable domains;
- edge cost weights;
- target predicates;
- scoring weights;
- control mapping;
- terminal and initial condition IDs;
- protected-release parameters if enabled.

### `NODE_EVALUATIONS.jsonl`

One JSON object per evaluated node:

```json
{
  "condition_id": "exp06-node-...",
  "x": {
    "affinity_mode": "token_overlap",
    "affinity_strength": 1,
    "catalyst_offset": 2,
    "basal_interval": 4,
    "candidate_cap": 4,
    "protected_release_mode": "off",
    "protected_release_strength": 0
  },
  "pettascript": "scripts/run_exp06_condition.sh ...",
  "query_atoms": ["..."],
  "exit_status": 0,
  "metrics": {
    "maximal_raf_size": 0,
    "greedy_core_size": 0,
    "dynamic_event_count": 12,
    "distinct_productive_rule_count": 3,
    "conversion_score": 0.0,
    "control_delta_raf": 0
  },
  "target_predicates": {
    "functional": false,
    "conversion": false,
    "compact_core": false
  }
}
```

### `PATHS.json`

Contains reconstructed paths:

```json
{
  "functional_cheapest": {
    "path_cost": 5.0,
    "nodes": ["condition-a", "condition-b", "condition-c"],
    "edge_costs": [2.0, 3.0],
    "target_reached": "functional"
  },
  "conversion_cheapest": null,
  "pareto_frontier": []
}
```

### `SUMMARY.md`

Human-readable summary:

- what was tested;
- which targets were reached;
- cheapest paths;
- matched controls;
- sensitivity to cost weights;
- explicit caveats: engineered terminal, diagnostic only, no emergence claim.

### Connection to existing run-contract format

Each node evaluation should either:

- reuse existing run-file-bundle sections (`CONFIG.metta`, `EVENTS.metta`, `METRICS.metta`, `ACS.metta`, `SUMMARY.metta`); or
- emit an exp06-specific run-record that can be projected into the same sections.

Avoid a separate incompatible artifact vocabulary unless the existing run-contract cannot represent a field. If a new field is needed, add it as a conservative extension, e.g. `intervention-condition`, `bridge-node-metrics`, or `bridge-path-summary` atoms.

## Validation strategy

### 1. Pure host graph validation

Before calling PeTTa, test the path-search code on synthetic lattices.

Cases:

- a 2-variable lattice with one known cheapest path;
- equal-cost multiple shortest paths;
- unreachable target;
- high-cost terminal-specific shortcut that should lose to a longer low-cost path;
- cache identity and canonicalization.

Expected: deterministic paths and stable `PATHS.json`.

### 2. PeTTa query smoke validation

Create or reuse tiny PeTTa atoms where target status is known.

Cases:

- known RAF-negative condition;
- known RAF-positive planted condition;
- known control pair with identical marginal weights but different assignment.

Expected: host parses PeTTa output correctly and labels targets correctly.

### 3. End-to-end tiny lattice

Use a tiny domain such as:

```text
affinity_mode: [none, token_overlap]
affinity_strength: [0, 1]
catalyst_offset: [0]
basal_interval: [0, 4]
candidate_cap: [2, 3]
protected_release_mode: [off]
```

At most 16 nodes. Run Dijkstra and produce all artifacts.

Expected:

- no crash;
- all nodes have reproducible condition IDs;
- PeTTa evaluations have exit status 0;
- if no target is found, report unreachable rather than weakening thresholds silently.

### 4. exp04 anchor validation

Run a small lattice including exp04 no-catalysis and terminal-specific settings.

Expected:

- no-catalysis anchor is RAF-negative;
- terminal-specific anchor is RAF-positive;
- high terminal-specific cost is visible in path cost;
- report says this validates harness reachability, not emergence.

### 5. Control-aware validation

For a favorable condition, evaluate matched rotated/uniform controls.

Expected:

- control metrics are recorded;
- treatment-control deltas are reported;
- if controls are also positive, favorable-condition claim is weakened to sensitivity finding.

### 6. Protected-release validation

Phase 1 only:

- compute family shares and excess canalization from a fixed event log;
- verify a hand-calculated small example.

Phase 2 later:

- run a condition with release off and on;
- verify adjusted weights are materialized and recorded;
- verify shared functional rules with high `c_r` are less penalized than identity-specific rules.

## Implementation sequence

1. **Write exp06 condition schema.** Define intervention vector, domains, canonical condition IDs, and cost weights in a design/config file. No chemistry changes yet.
2. **Define initial/terminal anchors in docs.** Pick Initial A (exp04 no-catalysis/control) and Terminal T1 (exp04 rich RAF). Record exact PeTTa atoms/scripts that reproduce them.
3. **Host-only graph smoke tests.** Implement Dijkstra and artifact skeleton against synthetic target functions.
4. **PeTTa evaluation adapter.** Add a thin adapter that calls existing PeTTa scripts/queries and parses metrics. It should not compute chemistry.
5. **Tiny PeTTa lattice.** Evaluate <=16 nodes using existing exp04/exp05 atoms or minimal exp06 condition projections.
6. **Artifact writer.** Emit `CONFIG.json`, `NODE_EVALUATIONS.jsonl`, `PATHS.json`, and `SUMMARY.md` with exact query provenance.
7. **exp04 reachability anchor.** Include enough domain values to connect no-catalysis/control to terminal-specific positive setting, with terminal-specific high cost.
8. **Functional vs conversion scoring.** Add separate target predicates and score tables; do not collapse them prematurely.
9. **Matched controls.** For candidate favorable nodes, automatically evaluate rotated/uniform/no-catalysis controls.
10. **Protected-release post-hoc metrics.** Compute `S_g`, `S*_g`, `O_g`, and protected release pressure from PeTTa event logs without changing dynamics.
11. **Protected-release intervention.** Only after post-hoc validation, materialize adjusted catalyst weights as explicit PeTTa condition atoms and compare off/on.
12. **Broader initial seeds.** Repeat with one exp02 generated-unplanted seed as Initial B. Keep it small.
13. **Sensitivity report.** Vary path-cost weights and target thresholds. Report whether minimal favorable variables are stable.

## Open questions and risks

### What exactly is the membrane analog?

The substack model has membrane mass and conversion efficiency. exp06 initially has products and event traces, not membranes. A conversion bridge requires a declared output family. Options:

- use exp04 core-associated products as a proxy;
- introduce a minimal `M` / membrane-analog product in a later PeTTa fixture;
- defer conversion bridge scoring and start with functional bridge only.

Recommendation: start functional; add conversion proxy only when a target product family is predeclared.

### How much of exp04 engineering should be allowed?

If terminal-specific catalysis is reachable as a cheap step, the path search will trivially rediscover the engineered fixture. Therefore terminal-specific mode must be high-cost and treated as an anchor, not a favorable condition.

### Are shortest paths meaningful in a hand-designed lattice?

Only conditionally. Shortest paths are meaningful relative to predeclared variables and costs. Therefore exp06 must include cost-weight sensitivity and report alternatives rather than one universal path.

### Does protected release require history-dependent PeTTa dynamics?

Eventually yes, if it changes dynamics based on recent ecological shares. First use post-hoc metrics. Then add a small explicit release-adjusted condition between runs, not an implicit mutable host-side intervention inside a run.

### Can controls become ACS-positive too?

Yes. exp04 already showed offset-sensitive RAF-like positives under some shuffled controls. If controls are positive, the conclusion is not "generic bias caused emergence" but "this chemistry is sensitive to catalysis-map structure under these budgets." That remains useful.

### Is ACS detection too narrow?

Existing scanners and RAF-like reductions are conservative and fixture-specific. Report which detector was used. Do not infer absence of all possible autocatalysis from zero under one detector.

### Will PeTTa query time be too high?

Possibly. Keep first lattices tiny and cache evaluations. If runtime becomes high, reduce lattice size before considering optimization. No remote compute for exp06 without a separate explicit approval packet.

### How to avoid accidental outcome conditioning?

All generation, affinity functions, protected-release coefficients, value proxies, and target product families must be declared before node evaluation. Any terminal-informed analysis must be labeled retrospective and excluded from favorable-condition evidence.

## Recommended minimal first experiment

Run the following as the first consequential exp06 harness target:

```text
initial_anchor = exp04_no_catalysis_control
terminal_anchor = exp04_rich_raf_fixture
state_domain = {
  affinity_mode: [none, token_overlap, terminal_specific],
  affinity_strength: [0, 1],
  catalyst_offset: [0, 1, 2],
  basal_interval: [0, 4],
  candidate_cap: [2, 4, 8],
  protected_release_mode: [off],
  protected_release_strength: [0]
}
targets = [functional_smoke, compact_core_smoke]
search = Dijkstra
controls = [rotated_control where applicable, no_catalysis]
```

Expected value of this first run:

- validates the path-search harness;
- verifies that PeTTa-native exp04 anchors can be evaluated through the harness;
- produces a transparent first bridge/path artifact;
- demonstrates how favorable-condition candidates will be reported;
- does **not** claim spontaneous emergence.

Only after this passes should exp06 attempt a less engineered initial/terminal pair or protected-release dynamics.
