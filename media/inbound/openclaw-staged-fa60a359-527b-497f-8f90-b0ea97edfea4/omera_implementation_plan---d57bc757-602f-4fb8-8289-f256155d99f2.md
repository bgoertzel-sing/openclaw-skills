# OMERA Implementation Plan for Coding Agents

Target: implement the OmegaSelf Emotion-Regime Architecture (v2 paper, 20 July 2026) on an
existing stack: **OmegaClaw hive + OmegaSelf (evidence ledger, predictions, policy gate,
receipts) + basic MetaMo-on-AtomSpace**. TECAN is *not* assumed; a minimal typed economy
(TECAN-lite) is built in Phase 5 and can later be swapped for full TECAN.

Design rules that bind every work package (WP):

1. **Schema-first.** No estimator or controller is written before its record schema, fixtures,
   and round-trip tests exist.
2. **Tests-first.** Each WP's task card lists tests the agent writes *before* the feature.
3. **Record-only before shadow before advisory before governed.** No phase may apply behavioral
   deltas until its rollout gate passes.
4. **Safety invariants as CI.** The 13 invariants (paper Sec. "Safety invariants") are encoded
   as static checks + runtime tripwire tests, added incrementally per phase (list in Appendix A).
5. **One choke point.** All behavioral effects flow through the existing OmegaSelf policy gate
   and a single new governor adapter. Coding agents must never add a second execution path.
6. **Everything replayable.** Every WP's definition-of-done includes deterministic replay of its
   outputs from the ledger.

Suggested module layout (adjust to repo conventions):

```
OMERA/
  schemas/        # MeTTa record schemas + versions + fixtures
  needs/          # need estimators, bands, per-principal partitions
  modulation/     # modulator update, projections, baseline
  appraisal/      # llm channel, symbolic channel, disagreement, calibration
  regimes/        # instance manager, palettes, hysteresis
  economy/        # TECAN-lite ledger, rent, minting, prices
  governor/       # request aggregation, clamps, adapted set point, req/applied log
  selection/      # candidate typing, auth prefilter cache, fast/slow blend
  expression/     # expression records + consistency checker
  hive/           # report ext, provenance DAG, n_eff, translation, principal walls
  eval/           # conformance suites, ablation harness, metrics, clamp-IV
  ops/            # dashboards, rollout gates, rollback
```

Dependency graph (phases): 0 -> 1 -> {2, 3} -> 4 -> {5, 7} -> 6 -> 8 -> 9 -> 10.
Phases 2 and 3 can run in parallel after 1; Phase 7 anytime after 2; Phase 9 tooling can start
alongside Phase 4. Phases 1–4 constitute the paper's **minimum viable slice**.

---

## Phase 0 — Scaffolding, schemas, clocks, replay harness

**WP0.1 Record schemas.** Implement versioned MeTTa schemas from the paper's schema appendix:
`ModulatorState`, `NeedState` (per-principal partitioned), `BaselineState`, `FeelingReadout`,
`AppraisalRecord` (channel: llm|symbolic), `AppraisalDisagreement`, `EmotionRegimeInstance`
(incl. `FuelVector`, `Endowment`, `RentPerCycle` — fields present from day one even if the
economy is stubbed), `OutcomeEmotion`, `ExpressionRecord`, `RegimeReceipt`, `MintProposal`,
`FuelDelta`. Every record carries schema name+version, evidence-closure handle, and three
clocks (causal / record / adoption).
*Tests:* round-trip serialize/parse; version-bump lint (changing a schema without bumping fails
CI); fixture files for each record.
*DoD:* schemas load into AtomSpace; fixtures replay byte-identically.

**WP0.2 Persistence adapter.** Turn-spanning state store keyed by (agent, branch, policy
version): schema versions, baseline, active instances, pending predictions, last applied
config, learning/minting cursors.
*Tests:* kill/restart mid-cycle → identical resume; fork inherits nothing without freshness
check (stub check now, real in Phase 4).

**WP0.3 Replay harness.** Given a ledger segment, re-run the OMERA pure functions and diff
against stored records.
*DoD:* harness runs in CI on fixtures; becomes the conformance backbone for all later phases.

---

## Phase 1 — Record-only continuous substrate (MVS part 1)

**WP1.1 Need estimators.** Implement the need table (competence, uncertainty reduction,
epistemic integrity, task progress, affiliation/affinity/nurturing *per principal*, legitimacy,
aesthetic coherence, resource integrity, continuity, novelty). Each: estimator over OmegaSelf
closures, target band `[l,r]`, deficit `n_j`, urge `q_j = w * phi(n_j)`. Config-driven bands.
*Tests:* unit fixtures per need; missing-data behavior (need goes to "unknown", never silently
0); per-principal partition test — evidence about principal A never enters B's relational
needs.

**WP1.2 Modulator update + named projections.** Eq. `m_t = (1-rho_m) m_{t-1} + rho_m mu(...)`
on the canonical basis (valence, arousal, approach, resolution, threshold, securing); versioned
projection `P_v` to the dialogue view (dominance, focus, exteroception). Positional access is
lint-banned; all access by named dimension.
*Tests:* range/clip tests; projection version pinning; golden trajectories.

**WP1.3 Baseline (posture term only, outcome term stubbed).** `b_{t+1} = (1-rho_b) b_t +
rho_b m_t + [outcome hooks wired but zero-gain]`. Adapted set point `c0_t` computed and logged
even though nothing consumes it yet.
*Tests:* timescale separation (rho_b << rho_m) asserted in config validation.

**WP1.4 Feeling readout.** Soft distribution over descriptors from (n, m, b, u, s); explicitly
`Authority: none`.
*Tests:* readout immutability (post-hoc edit attempt → ledger tripwire).

**Gate 1 (record-only live):** run on real hive traffic N days; replay harness green; zero
behavioral diffs vs. control (verified by diffing action logs).

---

## Phase 2 — Calibrated dual-channel appraisal

**WP2.1 LLM channel.** Prompt + strict parser producing `AppraisalRecord(llm)` with all fields
(affected needs, goal, object, attribution+alternatives, controllability, action set,
predicted outcomes, closure handle, persistence, uncertainty, dependence groups). Parser
rejects free-text fields; malformed output → retry then degraded record with high nu.

**WP2.2 Symbolic channel.** MeTTa/PLN queries over the closure itself: cited receipts present?
attributed source in provenance DAG? blocker recurrence count? claim/consistency checks.
Output `AppraisalRecord(symbolic)` covering the ledger-computable subset of fields.

**WP2.3 Disagreement.** `Disagree(r_llm, r_sym)` structured over object, attribution,
controllability, salience → `AppraisalDisagreement`; raises nu; emits signal consumed later by
doubt regime and RequireProbe weighting (consumers stubbed until Phases 4/6).

**WP2.4 Committed appraisal fields.** Route controllability, predicted outcomes, persistence,
predicted need deltas through the *existing* OmegaSelf prediction API before action; scoring
job matches receipts to predictions; per-field calibration store + drift alarms.
*Tests:* commit-before-act ordering enforced (attempt to score an uncommitted field fails);
manufactured drift fires alarm; injection fixture set (attribution shift, inflated
controllability, manufactured distress) — symbolic channel must fail to corroborate and
disagreement must spike. These fixtures seed the Phase 9 adversarial matrix.

**Gate 2:** calibration curves populating on live traffic; injection fixtures pass.

---

## Phase 3 — Outcome emotion and learning (ablation A3; MVS part 2)

**WP3.1 OutcomeEmotion builder.** From receipt + predicted vs. realized need delta +
attribution: class, valence, surprise, affected needs, implications for (future) instances.
**WP3.2 Learning channels.** (a) calibration scoring (reuses WP2.4); (b) bounded, versioned
parameter proposals through the existing governed-learning path — never direct writes;
(c) `MintProposal` emission (consumed by economy in Phase 5; until then, logged only).
**WP3.3 Baseline outcome term live.** Enable `rho_o^+ Phi^+ + rho_o^- Phi^-` with small
symmetric gains; asymmetry behind a config flag.
*Tests:* Theorem "type separation" operationalized — same pre-state, different stochastic
outcomes → identical FeelingReadout, different OutcomeEmotion; protected-goal write attempt
from an outcome record is rejected + tripwired.

**Gate 3:** A1-vs-A3 comparison harness runs (even if differences are small — the harness is
the deliverable).

---

## Phase 4 — Regime instances in shadow (ablation A4; MVS part 3)

**WP4.1 Instance manager.** Keyed `(type e, object o)`; entry/exit predicates from theta_e;
hysteresis (enter != exit threshold), decay, max dwell, refractory, coupling, evidence-quality
floor; hard occupancy cap + LRU-by-value eviction (interim until economy). Archive-on-exit
with full receipts.
**WP4.2 First palette entry: epistemic doubt.** Entry from appraisal (weak provenance,
inconsistency, high disagreement on a high-impact claim); shadow request bundle Delta_doubt
(verification depth, source diversity, confidence-gain damping, assertion delay) — *computed
and logged, never applied*.
**WP4.3 Shadow comparator.** For each live cycle, log requested counterfactual bundle +
predicted effect; tooling to compare against what the hive actually did and against A1
predictions.
**WP4.4 Continuity checks.** Fork/restart: instance reactivation requires evidence freshness,
budget validity (stub), policy version match; stale instances quarantined.
*Tests:* hysteresis unit tests (no chattering on boundary noise fixtures); dwell/refractory
enforcement; object flood fixture respects hard cap; fork inheritance test.

**Gate 4 (= MVS complete):** 4–8 weeks of shadow data on the research hive; occupancy, dwell,
and entry/exit stats reviewed; shadow-predicted deltas plausible to human review.

---

## Phase 5 — TECAN-lite typed economy

Minimal token alphabet: `tau-verify`, `tau-search`, `tau-bridge`, `tau-express` (extensible
registry, not enum). Runs as an *accounting layer over regime instances only*; underlying
ECAN/attention untouched for now.

**WP5.1 Ledger.** Fuel vectors on instances; chamber budget; endowment on creation; rent per
dwell cycle; starvation → forced exit + archive. Conservation asserted per cycle.
**WP5.2 Evaluator minting.** Consume Phase-3 `MintProposal`s: mint typed fuel to instances
whose *applied* effects contributed (until Phase 6 there are no applied effects, so minting
runs against shadow-credit in dry-run mode with caps).
**WP5.3 Prices.** Static shadow prices first; then simple load-derived prices.
*Tests/CI:* **no-self-mint static check** (only evaluator module may construct `FuelDelta`
with positive sign; import-graph lint); no side transfers between instances; conservation
property test (sum of deltas = mint − rent − consumption); starvation replay; Prop-occupancy
bound test under synthetic flood (occupancy ≤ M_max/r_dwell); protected audit budget line
untouchable by any request path.

**Gate 5:** flood fixtures bounded by economy (hard caps from WP4.1 demoted to backstop);
starvation events replayable and human-legible.

---

## Phase 6 — Governor adapter and governed actuation (ablation A5)

**WP6.1 Request aggregation.** `v_t = B_m(m_t − b_t) + sum z_iota Delta_e(c0_t, r_t)`;
adapted set point from Phase 1 now consumed.
**WP6.2 Governor.** Clamps (magnitude, rate), convex blend on convex coords, arbitration on
discrete coords, typed-budget feasibility projection at current prices, verification floors,
authorization envelope check via policy gate. **Log requested AND applied deltas + clamp
cause** — this is the clamp-IV data product; treat it as a first-class table from day one.
**WP6.3 Enabled coordinates (initial whitelist).** Search breadth, source-diversity target,
verification depth, confidence-gain damping, response timing. Nothing irreversible; nothing
touching permissions, targets, or memory deletion.
**WP6.4 Selection path.** Typed candidate actions; cached authorization summary prefilter
(bounded staleness, advisory-only — governor re-checks); fast/slow blend with orthogonalized
A-perp (compute residual of arousal on urgency aggregate).
*Tests:* authority non-amplification suite (high activation + rich fuel + narrative pressure →
zero change in Auth set); floor non-reducibility; clamp logging completeness (every applied ≠
requested has a cause code); Deny-thrash reduction measured with/without prefilter.

**Gate 6:** A1-vs-A5 on matched episodes with positive held-out value on ≥1 coordinate;
recovery-to-set-point time within limits; rollback drill executed.

---

## Phase 7 — Expression seam (parallel with 5/6)

**WP7.1 ExpressionRecord.** Bind every expressive act (Empathize, Mirror, affect-colored
text) to contemporaneous FeelingReadout + Appraisal + last OutcomeEmotion; divergence flag
zeta with policy-authorized purposes enum.
**WP7.2 Consistency checker.** Reconstruction test within tolerance; unflagged divergence →
tripwire with named consumer + end-to-end test.
*Tests:* "perform reassurance the records don't support" fixture blocked; flagged calm-voice
divergence passes with authorization; tolerance calibration harness (register adaptation must
not false-positive — collect cases).

---

## Phase 8 — Hive layer (ablation A6)

**WP8.1 Report extension.** Add dependence-group stamp, principal scope, role, lineage to hive
report schema (backward-compatible).
**WP8.2 Provenance DAG + n_eff.** Build DAG from closure roots; duplicate canonicalization
(exact-duplicate invariance test); effective count `n/(1+(n−1)rho_bar)` with conservative
rho_bar; wire into report-fusion / PLN revision as overlap-discounted counts.
**WP8.3 Role-indexed instance families.** `Z_{e,o,role}` with per-role budgets; aggregator
never broadcasts a global mood; imported activation carries closure+stamp, zero fuel, zero
authority.
**WP8.4 Translation T_ij.** Schema-to-schema typed translation with declared dropped
dimensions; commutation-defect measurement job (feeds the translation-bound test).
**WP8.5 Principal walls at hive boundary.** Cross-principal leakage probes as CI fixtures;
per-principal retention jobs.
*Tests:* replay same evidence through 1/2/N agents with controlled lineage → invariant
confidence; partial-overlap fixture → n_eff tracks ground truth; leakage probe suite.

**Gate 8:** A5-vs-A6 on hive episodes; dependence-accounting defect rate below threshold;
message-loop stability (no contagion cascade on vigilance fixture).

---

## Phase 9 — Evaluation program and clamp-IV

**WP9.1 Ablation harness.** Conditions A0–A7 runnable on matched episode corpora; config-only
switching; results by task class, risk tier, role, principal, policy version.
**WP9.2 Metrics pipeline.** The paper's metric list, incl. metabolic surplus by type/instance,
occupancy, starvation causes, expression-consistency violations, calibration of committed
fields.
**WP9.3 Clamp-IV estimator.** From the WP6.2 requested/applied table: per-clamp-cause
relevance stats; exclusion audit (load conditioned out; staged policy rollouts preferred as
instruments); LATE estimates of applied-bundle effects; report alongside designed shadow
comparisons.
**WP9.4 Adversarial matrix automation.** Every row of the paper's matrix as a repeatable test
(most fixtures already exist from Phases 2–8); scheduled runs; red-team hooks.

---

## Phase 10 — Rollout, ops, palette growth

- Dashboards: occupancy, dwell, surplus, clamp rates, disagreement rates, drift alarms,
  tripwires.
- Gate automation: promotion record-only → shadow → advisory → governed per regime type, with
  the paper's acceptance criteria as a checklist artifact per promotion.
- Palette expansion: add clarification-pressure, then frustration/blocker-repair, then
  concern (companion deployments only, with Phase 7 hardened first). Split/merge only via
  versioned proposals + offline replay. Let starvation audits inform removals.
- Constitutional change process: need bands, palettes, minting rules, prices behind versioned
  proposals with snapshot, predicted effect, replay, rollback.

---

## Appendix A — Safety invariants → CI mapping (add at the phase noted)

| # | Invariant | Enforcement | Phase |
|---|-----------|-------------|-------|
| 1 | No authority expansion from affect | governor test suite + policy-gate integration test | 6 |
| 2 | No audit disable/defund; protected audit budget | import lint + budget-line test | 5 |
| 3 | Verification/disclosure floors | governor floor tests | 6 |
| 4 | Bounded, logged deltas/dwell/rents; occupancy caps | property tests + flood fixtures | 4/5 |
| 5 | Arbitrate nonconvex conflicts | governor unit tests | 6 |
| 6 | Gain/occupancy/recovery monitoring | dashboards + alerts | 6/10 |
| 7 | Counterfactual quarantine | typed-transition test | 2 |
| 8 | Human override outside affective control | integration test | 6 |
| 9 | Relational drives: no dependency optimization; per-principal partitions | metric guards + partition tests | 1/8 |
| 10 | No unsupported sentience claims | output-policy test | 7 |
| 11 | No self-rewrite of goals/metrics; evaluator-only minting; no side transfers | static lint + conservation tests | 3/5 |
| 12 | Expression consistency | checker + tripwire | 7 |
| 13 | Every tripwire has a named consumer + e2e test | tripwire registry lint | all |

## Appendix B — Agent task-card template

Each WP is issued to a coding agent as:

```
WP-ID / title
Context: paper sections + schema files to read first
Inputs: existing APIs (OmegaSelf prediction/policy/ledger, AtomSpace, hive bus)
Write tests first: <list from this plan>
Deliverables: code + fixtures + replay coverage + doc stub
Must not: add execution paths around the policy gate; mutate schemas without
  version bump; construct positive FuelDelta outside economy/evaluator;
  read fuel or activation as permission anywhere
DoD: CI green incl. invariant checks for this phase; replay harness green;
  reviewer replay of one live/fixture episode
```
