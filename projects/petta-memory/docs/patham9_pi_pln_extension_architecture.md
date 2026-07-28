# Extending patham9’s PLN Toward πPLN

## Architecture, concepts, mathematics, current implementation, and proposed convergence

**Technical design report — 11 July 2026**  
**Project:** `petta-memory`  
**Prepared by:** ZeroBot and delegated source-analysis agents

> **Executive claim.** The current work is a tested, wrapper-first bridge around patham9’s scalar-STV PLN—not yet a native πPLN implementation inside patham9. It safely transports contextual evidence and provenance, performs an early EC→STV projection, controls which branches enter the chainer, and validates bounded queries and derivations. The central πPLN properties—persistent context-indexed contradictory evidence, context-local priors and charts, generated weakest adequate contexts, and compatibility-aware chart composition—remain the target architecture.

---

## 1. Why combine these systems?

The two systems have complementary strengths.

**patham9/PLN** already provides a compact functional chainer in MeTTa. It accepts `Sentence` atoms with scalar truth values, maintains task and belief queues, avoids some evidence reuse through stamps, applies familiar PLN formulas, and exposes bounded `PLN.Query` and `PLN.Derive` entry points.

**MesTTo’s πPLN work in PeTTaChainer** supplies a richer epistemic interpretation. Instead of treating one global scalar probability as persistent truth, it stores positive and negative evidence separately and indexes that evidence by context. A conventional PLN strength/confidence pair is a *local projection* made for a particular task or chart—not the durable representation itself. This preserves contradiction as information and avoids silently assuming that all local probabilistic views can be glued into one global distribution.

The proposed synthesis therefore uses:

- patham9 as the **bounded symbolic derivation engine**;
- `petta-memory` as the **evidence, context, provenance, and policy layer**;
- πPLN ideas as the **semantics for persistent evidence, local projection, and inference control**.

This division let us test useful behavior without destabilizing patham9’s working core or allowing tentative derivations to become durable memories.

---

## 2. Source and reproducibility baseline

This report describes the following inspected revisions:

| Component | Commit | Role |
|---|---|---|
| `petta-memory` | `f42d2930960c33732d53a3ebd8b0a5e9935aca99` | Wrapper, gates, provenance, tests |
| `patham9/PLN` | `55f1751d993f71b8a24da03e3aec94ab40789a59` | Functional scalar-STV chainer |
| `MesTTo/PeTTaChainer` | `e4db5cad60a39c0d3f81a07296d606af6de4d76d` | πPLN concepts and executable translation |
| `trueagi-io/chaining` | `bc9beb2672953e07971b3abecc1fe67651ecddc4` | Inference-control patterns |

The principal implementation examined is:

`projects/petta-memory/repos/petta-memory/src/petta_memory/patham9_pln.py`

The πPLN reference translation examined is:

`projects/petta-memory/repos/PeTTaChainer/pettachainer/metta/piPLN_paper_explained/`

The checkouts had pre-existing untracked local files. The cited tracked sources and commit identifiers, rather than a claim of pristine working trees, define the provenance baseline.

---

## 3. Conceptual model

### 3.1 Persistent truth as contextual evidence

For proposition φ in context C, πPLN retains an evidence-count pair

> EC_C(φ) = (n_C⁺, n_C⁻),

where `n⁺` is positive evidence and `n⁻` is negative evidence. Both coordinates may be large. Thus `(1000,1000)` means a strong live conflict, while `(1,1)` means weak and nearly ignorant evidence—even though both have empirical strength 0.5.

The evidence-count structure is ordered componentwise:

> (a⁺,a⁻) ≤ (b⁺,b⁻) iff a⁺ ≤ b⁺ and a⁻ ≤ b⁻.

For provenance-disjoint evidence, sequential composition adds counts:

> (a⁺,a⁻) ⊗ (b⁺,b⁻) = (a⁺+b⁺, a⁻+b⁻).

Alternative evidence bounds use componentwise maximum:

> (a⁺,a⁻) ∨ (b⁺,b⁻) = (max(a⁺,b⁺), max(a⁻,b⁻)).

This separation matters: evidence order is not truth order. More negative evidence can mean *more information* while making a proposition *less true*.

### 3.2 Local chart projection to ordinary PLN truth values

A selected local chart contributes a prior strength `p₀` and prior weight `k`. πPLN’s reference projection is

> s = (n⁺ + k p₀) / (n⁺ + n⁻ + k),  
> c = (n⁺ + n⁻) / (n⁺ + n⁻ + k).

Here `s` is projected strength and `c` is confidence. The same evidence can also be projected to a Beta posterior:

> α = k p₀ + n⁺,  
> β = k(1−p₀) + n⁻,

whose mean equals `s`. The prior belongs to the local chart, not to durable evidence storage.

This creates a strict semantic direction:

> persistent context-indexed EC → selected local chart → temporary STV → bounded PLN inference.

An inferred STV does **not** automatically become new durable EC; that requires an explicit, provenance-aware evidence transformation and promotion decision.

### 3.3 Why local contexts are substantive

A context is not merely a tag. It determines which evidence is relevant, which assumptions hold, and which probabilistic chart is adequate. πPLN’s executable examples generate conjunctions of evidence features at query time, score them by conflict reduction, select a weak but adequate guard, and provide ablation/minimality evidence explaining why a more general context failed.

This supports default/exception behavior without globally merging incompatible evidence—for example, “birds fly” and “penguins do not fly” can remain useful local charts rather than being averaged into a misleading universal scalar.

---

## 4. The current wrapper-first architecture

```text
Append-only memory / promoted beliefs
                 │
                 ▼
       petta-memory handoff cache
  STV + EvidencePacket/EC + provenance
                 │
                 ▼
       Context-selection wrapper
 domain / cluster / promotion-rule filters
                 │
                 ▼
         EC→STV projection layer
      (currently an adapter heuristic)
                 │
                 ▼
       Inference-control plan/gate
 rank ─ hold ─ continue ─ terminate ─ reject
                 │ admitted branches only
                 ▼
      patham9-compatible Sentence atoms
       simple numeric runtime stamps
                 │
                 ▼
      patham9 PLN.Query / PLN.Derive
                 │
                 ▼
       semantic and provenance checks
                 │
                 ▼
 artifact / GoalChainer appraisal only
  NO memory write; NO belief promotion
```

### 4.1 Boundary representation

The bridge emits ordinary patham9 sentences:

```metta
(Sentence ($Term (stv S C)) $Stamp)
```

while retaining richer information externally:

```metta
(EvidencePacket
  statement
  (EC support opposition)
  metadata
  promotion-event)
```

The runtime stamps are deliberately simple numeric lists such as `(0)` and `(1)`. patham9’s stamp utilities expect sortable values; richer symbolic `PMEvidence` stamps caused compatibility risk. A JSON sidecar maps every numeric stamp back to its belief, cluster, promotion event/rule/domain, contextual packets, and any synthetic smoke-test premise.

### 4.2 What patham9 contributes

At the inspected revision, patham9 supplies:

- `PLN.Query` and `PLN.Derive`;
- belief and task queues;
- bounded step controls;
- `StampDisjoint` evidence-overlap checks;
- confidence-oriented ranking and best-candidate selection;
- a library of scalar truth-value formulas and inference rules.

For the bridge’s two-premise smoke test, patham9’s modus-ponens formula is effectively

> s_out = s₁s₂ + 0.02(1−s₁),  
> c_out = c₁c₂.

The bridge verifies semantic `Passed:` markers and preserves the exact generated program and provenance sidecar. Results remain evidence about runtime behavior, not asserted beliefs.

---

## 5. The EC→STV adapter that exists today

The currently implemented `ec_projected_stv()` does **not** yet use πPLN’s context-prior formula. For each packet `(u,v)` it computes

> s_EC = u/(u+v),  
> c_EC = (u+v)/(u+v+2).

It then treats the base STV `(s₀,c₀)` and packet projections `(sᵢ,cᵢ)` as weighted observations:

> s′ = Σᵢ cᵢsᵢ / Σᵢ cᵢ,  
> c′ = maxᵢ cᵢ.

Zero-total packets are ignored; negative counts and out-of-range base STVs are rejected.

This has useful test behavior: supportive packets can reinforce a sentence, and conflicting EC can lower projected strength while raising confidence that genuine evidence exists. A recorded smoke, for example, moved a strong base STV `(0.94,0.80)` with opposing EC `(1,9)` to approximately `(0.511429,0.833333)`.

But the formula is an **engineering adapter heuristic**, not the canonical πPLN projection. It has three major semantic losses:

1. It collapses multiple contextual packets into one scalar before inference.
2. It has no context-local `p₀` and `k`.
3. Once collapsed, high balanced contradiction is distinguishable from ignorance mainly through confidence, not through persistent two-coordinate evidence.

The recommended next mathematical change is therefore to replace or version this projection behind an explicit `ProjectionPolicy`, retaining the current formula as a baseline and adding the canonical prior-aware chart projection.

---

## 6. Inference control: the most developed extension

A major practical lesson from the work is that πPLN’s value is not limited to better truth values. Contextual evidence can decide *where not to reason*.

The implementation surveys and adapts patterns from `trueagi-io/chaining`:

### 6.1 Context selection

`context_selection_wrapper()` filters EvidencePackets by:

- promotion domain;
- cluster identifier;
- promotion rule;
- minimum evidence relevance.

Its present relevance score is

> r = (n⁺+n⁻)/(n⁺+n⁻+2)

after exact context-field matches. It is a useful deterministic approximation, but not yet πPLN’s generated weakest-adequate-chart search.

### 6.2 Probabilistic filtering and ranking

`probabilistic_inference_filter()` applies the wrapper projection and scores a candidate by

> q = s′c′.

A confidence threshold and `top_k` cap bound the candidate set. `chained_inference_pipeline()` composes context selection with this ranking and remaps source indices, keeping provenance intact.

### 6.3 Continuation predicates

`continuation_predicate_wrapper()` gives every branch one of three decisions:

- **continue** — eligible for another reasoning step;
- **terminate** — acceptable result, but depth or another stopping condition has been reached;
- **reject** — fails strength, confidence, domain, promotion-rule, or EC-ratio requirements.

This reverses uncontrolled search: branches must justify continued computation.

### 6.4 Controlled chaining

`controlled_backward_chainer()` simulates bounded recursive control with:

- maximum steps;
- maximum total branches;
- derivation-depth updates;
- optional accumulated EC context;
- explicit traces of continued, terminated, and rejected branches.

It is currently a wrapper-level control simulation rather than a native interception of each internal patham9 recursive rule application.

### 6.5 PLN estimator and delayed calls

`pln_estimator_wrapper()` adopts the `EDCall` (Estimated Delayed Call) pattern. It forms a viability prior from branch STV/context evidence, uses Beta/Thompson sampling for exploration versus exploitation, and emits a ranked set of delayed branch calls. `ranked_inference_control_plan()` composes estimation with continuation checks; `ranked_plan_admitted_handoff()` materializes only admitted branches in the existing handoff schema.

This architecture keeps stochastic policy outside patham9. A seed makes experiments reproducible, and the admitted set is an inspectable artifact before any derivation occurs.

### 6.6 Controller as chainer

`controller_as_chainer()` models a meta-level controller that uses a PLN-like query to decide whether the object-level chainer should proceed. Conceptually:

> controller query → branch viability proof → admission → object-level derivation.

The long-term form would run a small patham9 control query separately from the main derivation. The current implementation remains bounded and wrapper-owned.

---

## 7. What is implemented, approximated, and still proposed

| πPLN capability | Current representation | Assessment |
|---|---|---|
| Separate positive/negative evidence | `EvidencePacket` with support/opposition | Implemented in handoff and sidecars |
| Provenance-preserving runtime handoff | Numeric stamps + `PMEvidence` sidecar | Implemented and smoke-tested |
| Bounded scalar PLN derivation | patham9 `Query`/`Derive` | Implemented and runtime-tested |
| Context filtering | Domain/cluster/rule packet filters | Implemented approximation |
| EC→STV projection | Confidence-weighted blend | Implemented heuristic; not canonical πPLN |
| Branch ranking/admission | score, thresholds, top-k, ranked plan | Implemented wrapper policy |
| Continue/terminate/reject control | continuation and controlled-chainer wrappers | Implemented simulation/policy |
| Context-indexed durable EC metagraph | Rich data stays outside patham9 | Not native; partially represented |
| Context-local priors | No `p₀,k` chart policy in current projection | Missing |
| Generated weakest adequate chart | Exact metadata filters only | Proposed |
| Contradiction-preserving native rules | patham9 uses scalar `Truth_*` formulas | Missing |
| Projection of derived STV back to EC | Deliberately absent | Proposed, high risk |
| Chart compatibility/global gluing | No implementation | Proposed research problem |
| Live memory write/belief promotion | Explicitly prohibited | Correctly absent |

The exact status distinction is important: this work extends the *system architecture surrounding patham9*, but it does not yet extend patham9’s internal truth semantics.

---

## 8. Safety and audit architecture

The bridge follows a fail-closed design because its eventual consumer may be an autonomous agent.

### 8.1 Read/write separation

The current path is read-only:

- no append to the `petta-memory` journal;
- no automatic conversion of a derivation into `DerivedBelief`;
- no PeTTaChainer `compileadd` path;
- no modification of patham9 source;
- no OmegaClaw task or directive claim.

Outputs are labeled as `pln-ready-input-not-inferred-belief` or retained as runtime artifacts.

### 8.2 Runtime proof gate

Before GoalChainer appraisal, the optional patham9 runtime gate checks, among other things:

- exact expected result/program schemas;
- integer zero return code;
- semantically passing marker counts;
- zero false/error markers;
- handoff sentence count equal to admitted items;
- total sentence count equal to admitted items plus the synthetic bridge premise;
- coherent provenance mappings.

### 8.3 Agent-boundary hardening

Copied GoalChainer artifacts are validated for shape, finite numbers, unique action IDs, known statuses, evidence/proof structure, and contextual EC provenance. Directive/task-shaped fields—including nested `claim`, `plan`, `next`, `skill`, and related keys—are rejected. This keeps an evidence/appraisal bridge from becoming a covert command channel.

---

## 9. Validation evidence

The implementation repository records a progression from sentence/query smokes to context and controller policies. Representative runtime artifacts include:

- `patham9_pln_handoff_query_smoke_2026-07-05T1000Z.json`;
- `patham9_pln_handoff_derivation_smoke_2026-07-05T1200Z.json`;
- `patham9_pi_pln_wrapper_boundary_plan_2026-07-05T1400Z.json`;
- `patham9_pln_ec_projection_smoke_2026-07-05T1600Z.json`;
- `patham9_pln_ec_conflicting_projection_smoke_2026-07-05T1800Z.json`;
- `patham9_pln_derivation_ec_projection_smoke_2026-07-05T1800Z.json`;
- `patham9_pln_multi_sentence_derivation_smoke_2026-07-05T2000Z.json`.

Tests in `tests/test_patham9_pln.py` cover parsing, handoff preservation, query and derivation serialization, EC projection and conflict behavior, API mapping, multi-sentence stamp lineage, inference filtering, and context selection. The broader project record reports **440 passing unit tests** at the latest hardening slices around commit `f42d293`, together with a clean `git diff --check` at those slices.

These results establish that the adapter/gating mechanics work under the recorded local environment. They do not establish the semantic adequacy of the current projection as full πPLN.

---

## 10. Recommended target architecture

The next architecture should make contexts and projection policies first-class while preserving the current audit boundary.

```text
Contextual Evidence Store
  key: (statement, context, provenance class)
  value: EC(n+,n−) + packet lineage
             │
             ▼
Query Context Generator
  evidence features → candidate guards/charts
             │
             ▼
Chart Scorer / Selector
 conflict reduction + adequacy + specificity + cost
             │
             ▼
ProjectionPolicy
  canonical EC,p₀,k → STV (plus baseline adapter for comparison)
             │
             ▼
Inference Controller
  EDCalls + utility + continuation + bounded budget
             │
             ▼
Patham9 Adapter
  Sentence atoms + collision-safe stamps + provenance map
             │
             ▼
Unmodified patham9 core initially
             │
             ▼
Proof/Result Sidecar
 chart, assumptions, selected packets, formulas, stamps, proof
             │
             ▼
Explicit Promotion Gate
 reject / artifact-only / reviewed evidence transformation
```

### Proposed interfaces

**`ContextualEvidenceStore`**  
Returns immutable packet sets and aggregate EC for a statement under a guard. It must detect provenance overlap before tensoring counts.

**`ContextGenerator`**  
Derives candidate conjunctions from query and evidence features. A bounded beam search should permit depth-3/4 exceptions while exposing every candidate and score.

**`ChartPolicy`**  
Carries `(guard, assumptions, p₀, k, selected packets, adequacy proof)`. Priors and assumptions become explicit data, not hidden constants.

**`ProjectionPolicy`**  
Versioned implementations:

1. `adapter-weighted-v1` — the current baseline;
2. `pipl-local-chart-v1` — canonical prior-aware EC projection;
3. optional Beta-posterior output for sampling/control.

**`InferenceController`**  
Ranks branches using projected truth, context adequacy, conflict, computational cost, and provenance risk. It emits an immutable admission plan.

**`Patham9Adapter`**  
Remains narrow. It serializes only admitted scalar sentences and maps collision-safe runtime stamps to packet lineage.

**`PromotionGate`**  
No inverse STV→EC operation should be presumed. Any derived result must identify the rule, premises, chart, assumptions, overlap policy, and a reviewed method for producing new evidence.

---

## 11. Mathematics for the next implementation slice

### 11.1 Canonical chart projection

For aggregated, provenance-disjoint contextual evidence `EC_C(φ)=(n⁺,n⁻)` and chart parameters `(p₀,k)`:

> Project_C(φ) = (s,c),  
> s = (n⁺+kp₀)/(n⁺+n⁻+k),  
> c = (n⁺+n⁻)/(n⁺+n⁻+k).

This should be implemented alongside, not silently substituted for, the existing baseline. Comparative tests should pin both outputs.

### 11.2 Conflict diagnostics

A controller should not identify balanced contradiction with uncertainty. Useful separate quantities are:

> evidence mass: N = n⁺+n⁻,  
> empirical balance: b = 2 min(n⁺,n⁻)/max(N,ε),  
> signed tendency: t = (n⁺−n⁻)/max(N,ε).

`N` distinguishes live conflict from ignorance; `b` measures balance/contradiction; `t` gives direction. These should influence context generation and branch utility separately from STV confidence.

### 11.3 Candidate-chart utility

A first reproducible utility for candidate chart C and branch j could be

> U(j,C) = α s_{j,C}c_{j,C} + β A(C) + γ ΔConflict(C) − δ Cost(j,C) − η OverlapRisk(j,C),

where:

- `A(C)` is chart adequacy/specificity;
- `ΔConflict(C)` is conflict reduction relative to a broader chart;
- `Cost` estimates search expense;
- `OverlapRisk` penalizes uncertain provenance reuse.

The coefficients must be configuration data and experiment-recorded—not embedded folklore.

### 11.4 Thompson-sampled exploration

From the local chart posterior

> Beta(α,β) = Beta(kp₀+n⁺, k(1−p₀)+n⁻),

sample `θ_j ~ Beta(α_j,β_j)` and rank a delayed branch by a seeded combination such as

> Q_j = θ_j − δ Cost_j − η OverlapRisk_j.

This directly aligns the controller’s uncertainty model with πPLN evidence, replacing an avoidable mismatch between canonical chart projection and an unrelated sampling prior.

---

## 12. Staged implementation plan

### Stage A — projection correctness

1. Add explicit `ChartPolicy(p₀,k,guard,assumptions)` data.
2. Implement canonical `ECToSTV` and Beta projection.
3. Keep `adapter-weighted-v1` as a comparison baseline.
4. Add tests for ignorance versus high balanced conflict, supportive/opposing evidence, zero counts, and prior sensitivity.
5. Re-run existing patham9 query/derive smokes with both policies.

**Exit criterion:** formulas match the MesTTo reference examples and preserve packet/provenance lineage.

### Stage B — generated context selection

1. Generate bounded guards from evidence/query features.
2. Score conflict reduction, adequacy, specificity, and cost.
3. Produce an ablation/minimality certificate.
4. Compare exact metadata filters against generated contexts on default/exception and depth-4 “needle” cases.

**Exit criterion:** the selected context and rejected alternatives are inspectable and reproducible.

### Stage C — controller/runtime coupling

1. Feed canonical chart posteriors into EDCall sampling.
2. Materialize only admitted branches.
3. Add a bounded control-query/object-query two-level path.
4. Record seed, budget, candidate list, and admission reason.

**Exit criterion:** controlled patham9 execution improves a declared metric (search cost, precision, or conflict handling) without changing semantic answers on baseline cases.

### Stage D — native extension decision

Only after A–C should we evaluate modifications inside patham9, such as context-aware sentence types or EC-aware rule formulas. Trigger this only if the wrapper cannot preserve required semantics or if repeated serialization materially dominates runtime.

**Exit criterion:** a written comparison shows that a native change provides benefits impossible or impractical at the wrapper boundary, with regression tests for stamps, queues, truth formulas, and provenance.

### Stage E — reviewed belief promotion

Design an explicit evidence-transformation protocol for derived results. Never “invert” an STV into EC without assumptions. Require provenance-disjointness analysis and operator-reviewed promotion policy.

**Exit criterion:** derivations can become durable evidence only through a typed, auditable, separately enabled gate.

---

## 13. Principal risks and open research questions

1. **Semantic compression.** Preprojecting EC to STV loses structure patham9 cannot recover.
2. **Evidence dependence.** Count addition is justified only for independent or provenance-disjoint packets.
3. **Context combinatorics.** Generated guards can grow exponentially; beam bounds and minimality certificates are essential.
4. **Prior selection.** Context-local `p₀,k` values need transparent estimation or calibration.
5. **Rule semantics.** Scalar patham9 formulas may not correspond to correct transformations of contextual EC.
6. **Stamp collisions.** Simple per-program numeric stamps are safe only within a carefully scoped invocation and sidecar mapping.
7. **Controller circularity.** A PLN-controlled PLN can amplify its own calibration errors; controller proofs and budgets must remain separately auditable.
8. **Gluing local charts.** Compatibility among locally coherent charts is conditional, not automatic. Detecting when chart results can be combined remains a substantive research problem.
9. **Promotion feedback.** Writing derived outputs back as evidence can create self-reinforcement and double counting unless lineage is explicit.

---

## 14. Conclusion

The proposal has already produced a useful architectural result: patham9 can remain a small, functioning derivation kernel while `petta-memory` supplies the richer epistemic and control boundary needed for agent memory. The tested bridge constructs patham9 sentences, preserves contextual EC and provenance externally, executes bounded query/derivation smokes, and admits branches through explicit context and inference-control policies.

The intellectually honest description is **πPLN-inspired wrapper and inference-control architecture**, not “πPLN implemented in patham9.” The most important next step is mathematical convergence: introduce explicit local chart parameters and MesTTo’s canonical EC→STV/Beta projections, then evaluate generated contexts and posterior-aligned branch control. Only after those wrapper experiments should native patham9 semantic changes be considered.

That sequencing keeps the system useful, inspectable, and reversible while moving toward the deeper πPLN objective: reasoning locally with contradiction-aware evidence, without pretending that every context belongs to one globally coherent probability space.

---

## References to checked-out source

1. `projects/petta-memory/repos/petta-memory/src/petta_memory/patham9_pln.py` — handoff, projection, context selection, inference-control wrappers, runtime builders.
2. `projects/petta-memory/repos/petta-memory/tests/test_patham9_pln.py` — wrapper and runtime-contract tests.
3. `projects/petta-memory/DECISIONS.md` — architectural decisions and preserved boundaries.
4. `projects/petta-memory/repos/patham9-pln/src/Deriver.metta` — query/derivation queues, stamps, ranking, bounded execution.
5. `projects/petta-memory/repos/patham9-pln/src/Formulas.metta` — scalar PLN truth-value formulas.
6. `projects/petta-memory/repos/PeTTaChainer/pettachainer/metta/piPLN_paper_explained/README.md` — scope and executable πPLN reading guide.
7. `projects/petta-memory/repos/PeTTaChainer/pettachainer/metta/piPLN_paper_explained/paper_translation.metta` — EC quantale, chart projection, Beta projection, revision, and control-label formulas.
8. `projects/petta-memory/repos/PeTTaChainer/pettachainer/metta/piPLN_paper_explained/generated_contexts_demo.metta` — evidence-derived context generation and minimality reports.
9. `projects/petta-memory/repos/PeTTaChainer/pettachainer/metta/piPLN_paper_explained/context_inference_control_demo.metta` — context-conditioned branch control.
10. `projects/petta-memory/repos/trueagi-chaining/experimental/` — EDCall, continuation, controlled-chaining, and probabilistic-control reference patterns.
