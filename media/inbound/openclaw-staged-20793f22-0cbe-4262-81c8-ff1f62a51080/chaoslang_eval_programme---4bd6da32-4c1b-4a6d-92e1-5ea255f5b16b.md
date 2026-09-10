# chaoslang Evaluation Programme for the Adaptive-Coding Upgrade

**Status:** preregistered experiment protocol (freeze before running E2 onward)
**Companion:** `chaoslang_upgrade_spec.md` (milestones M-A..M-F)
**Conventions:** identical to the July 2026 programme — frozen prefix/suffix splits, exact-marginal shuffled nulls, three seeds minimum unless stated, provenance ledgers named `YYYYMMDDTHHMMSSZ-<slug>`, all promotion rules stated before running, no tuning on inspected suffixes. All previously inspected frozen suffixes are burned: every experiment below uses **fresh trajectories/seeds** except where a frozen fixture is explicitly named for regression.

**Dependency map:** E0–E1 need M-A+M-B only. E2–E3 need M-C. E4 needs M-D. E5–E6 need M-E. E7 needs M-C..M-E (M-F optional arm). E8 needs everything and an E7 pass.

---

## E0 — Coder calibration battery (regression + theory checks)

**Question.** Do the new coders produce correct, theory-consistent code lengths?

**Design.** Synthetic sources with known entropy rates, 5 seeds, lengths {1k, 10k, 100k}:
(a) iid uniform over |V| ∈ {2, 4, 16}; (b) iid skewed (Zipf s=1.2); (c) order-1 Markov with known transition matrix; (d) order-3 Markov; (e) periodic; (f) the frozen LZ78 regression fixtures.

**Measurements.** Prequential bits/symbol vs true entropy rate for each registry coder; LZ78 bit-identity to stored values.

**Decision rule.** For each source, adaptive coder of matching order must converge to within 5% of the entropy rate at 100k; adaptive-Markov-2 must beat adaptive-unigram on (c)–(d) and match it within redundancy on (a)–(b); CTW must be within its redundancy band of the best matched Markov coder everywhere; any LZ78 bit mismatch is a hard fail. No grammar induction in E0.

---

## E1 — Re-baseline the frozen fixtures (no grammar, controls only)

**Question.** What do the *old* frozen fixtures cost under the new adaptive controls? This resets the bar every later result is judged against, and quantifies how much of CLA's historical losses were baseline miscalibration.

**Design.** Re-score, with no grammar arm at all, every named frozen fixture from the July ledgers (held-out v1/v2 attractor fixtures; synthetic families: de Bruijn-5, Fibonacci, paperfolding, Cantor, Rudin–Shapiro, 2-uniform and 3-uniform morphisms; Stage-B prefix-quantized fixtures) under: static controls (regression), adaptive-unigram/M1/M2, CTW-d8, LZ78, CSSR (once M-E lands — may be appended as E1b).

**Measurements.** Complete-code bits per fixture per coder; deltas vs the historical static-control numbers.

**Decision rule.** No pass/fail — E1 is a measurement that produces the **new control table**, checked in as a frozen artifact. Preregistered predictions to test the diagnosis: (P1) adaptive-Markov-2 or CTW is the strongest control on every chaotic fixture; (P2) the gap between best-adaptive and best-static control exceeds 15% of static bits on the attractor fixtures. If P1/P2 fail, the "static baseline" diagnosis is wrong — stop and rethink before E2.

---

## E2 — Replay historical decisions under the shared adaptive coder

**Question.** Which of the July synthetic passes/failures were artifacts of the weak data code?

**Design.** For each synthetic frozen fixture, re-run the *frozen historical grammar* (from the stored edit logs — no new search) under `AdaptiveTwoPartScorer` with base coder = adaptive-Markov-2, and compare against the E1 control table. Also recompute the 6,232/6,296/+64 gate fixture (legacy scorer regression) and its adaptive-scorer counterpart.

**Measurements.** Per fixture: grammar-arm total bits, margin vs best control, sign flips relative to July outcomes. Ledger `final_breakdown.json` for every arm.

**Decision rule.** Again primarily measurement, with preregistered predictions: (P3) ≥ 2 of the July synthetic "passes" lose their margin (shrink below the null-rejection threshold) under the fair coder; (P4) the Fibonacci/paperfolding *total* losses shrink by more than half once member/parameter codes are adaptive. Record outcomes; no tuning.

---

## E3 — D1 oracle decomposition battery (the central gate)

**Question.** With the adaptive code, is remaining failure representational, search, or sample-complexity?

**Design.** Ten tiny planted grammars (fresh, enumerable): 3 chunk-only hierarchical, 3 category-bearing (incl. the `a{x,y}b` synergy family), 2 substitution systems (Fibonacci-class), 2 stochastic-choice grammars. For each: n ∈ {1k, 16k}, 3 seeds, exact-marginal shuffled null. Arms: (i) **oracle** — the true generating grammar hand-encoded as a `GrammarState`, scored by `AdaptiveTwoPartScorer`; (ii) greedy from empty; (iii) greedy from Re-Pair init (if M-D done; else defer to E4); (iv) all E1 controls.

**Decision rule (preregistered, binding).**
* *Representation gate:* the oracle must beat every control on ≥ 9/10 families at 16k, with all nulls rejected. **If the oracle loses on ≥ 2 families, stop all search work** — the grammar format/coding is still inadequate; iterate on §1–2 of the spec (candidate fixes logged, then a fresh E3 with new planted families).
* *Search gate:* proceed to attractor work only if some search arm recovers a grammar within 10% of oracle bits on ≥ 8/10 families.
* The gap `search_bits − oracle_bits` per family is the canonical **search-deficit** statistic used in E4.

---

## E4 — Search ablation on the hard synthetic families

**Question.** How much of the search deficit do Re-Pair init, composite moves, and beam close, at what cost?

**Design.** Families: fresh Fibonacci word, paperfolding, complementary 3-uniform morphism, plus the two E3 families with the largest search deficit. Full factorial over {init: empty, repair} × {moves: single, +composite} × {search: greedy, beam-4, beam-16}, 3 seeds, fixed proposal budget. Base coder frozen (adaptive-Markov-2). Ledgers on.

**Measurements.** Total bits vs oracle and controls; fraction of oracle-to-greedy gap closed; first step at which the correct abstraction (planted category or hierarchical rule) appears (from ledgers); wall time; accepted-composite count; per-arm rejection-reason histograms.

**Decision rule.** A search configuration is **promoted to default** if it closes ≥ 80% of the oracle gap on every family within 4× greedy runtime, and its ledger shows the planted categories accepted (not merely proposed) on the category-bearing families. If no configuration passes, the rejection-reason histograms adjudicate: dominance of `positive_delta` on planted-structure proposals ⇒ coding still mispriced (return to E3); absence of the planted proposals entirely ⇒ miner coverage failure (extend proposal generators, rerun E4 only).

---

## E5 — Automata track: CSSR as detector and coder on chaotic fixtures

**Question.** Is the "grammar of the attractor" recoverable as a sofic/causal-state process where chunk grammars failed?

**Design.** Fresh trajectories (new seeds/initial conditions): Mackey–Glass, full-state Lorenz–96 (8D), each via the frozen low-cardinality microstate symbolizer (k ∈ {8, 16}, prefix-fitted); controls: stable Lorenz–96, periodic source, exact-marginal shuffle of each positive — the six-fixture battery shape. Prefix/suffix frozen before running. Arms: CSSR (max_history ∈ {3, 5, 8} — selected on *prefix* by prequential self-coding, single choice frozen before suffix scoring) as a **two-part complete code** (machine bits + held-out adaptive suffix bits) vs all E1 controls.

**Measurements.** Held-out suffix bits per arm; number of causal states; statistical complexity; forbidden-word list induced by the machine (states with zero-support successors) — reported, not gated.

**Decision rule.** *Detector sense:* CSSR complete code beats every non-CSSR control on both positives AND fails to beat adaptive-Markov-1 on the shuffled nulls (fail-closed on protocol errors, as in Stage-A). *Structure sense (secondary, reported):* recovered machine for Lorenz-class fixtures has > 2 states and reproduces at least one known forbidden word on a ground-truth lift (reuse the Lorenz-63 R256 lift protocol with fresh seeds). A detector-sense pass is the first legitimate successor to the Stage-A geometric pass at the *symbolic* level.

---

## E6 — Causal-state-seeded categories inside CLA

**Question.** Do CSSR-derived category proposals get accepted and recover planted structure where JS clustering did not?

**Design.** (a) Planted: 3 fresh category-bearing synthetic families with known latent classes, noise levels {0, 5%}; (b) chaotic: the E5 positive fixtures. Arms: CLA with inducers {js}, {cssr}, {js, cssr}, all under the E4-promoted search config. 3 seeds.

**Measurements.** Accepted categories per arm (from ledgers); adjusted mutual information between accepted categories and planted classes; held-out bits delta attributable to category edits (sum of accepted category-record `delta_total_bits`); stability of category membership across seeds (mean pairwise Jaccard).

**Decision rule.** CSSR seeding is promoted if, on planted families, {cssr} or {js,cssr} reaches AMI ≥ 0.8 to planted classes on ≥ 2/3 families with cross-seed Jaccard ≥ 0.7, and no arm's nulls are promoted. On chaotic fixtures: reported only — any accepted nontrivial category (≥ 2 members, positive ledger delta, stable across ≥ 2/3 seeds) is a headline result but not a gate.

---

## E7 — D3 rebuilt: the attractor gate

**Question.** Does the full upgraded pipeline produce a nontrivial grammar that beats all complete-code controls on fresh chaotic data?

**Design.** Fresh Mackey–Glass and full-state Lorenz–96 fixtures (new seeds; disjoint from E5's), stable + shuffled controls, frozen prefix/suffix. One pipeline configuration, **frozen in advance** from the E3–E6 winners (scorer, base coder, init, moves, inducers); one optional second arm: `PrequentialScorer` (M-F) with the same components. Controls: full E1 table including CSSR. 3 seeds.

**Promotion rule (binding, same shape as the July rule).** Both positives beat *every* control including CSSR and CTW; stable and shuffled controls not promoted; exact decode and frozen-prefix invariants pass; and the induced grammar is nontrivial: > 2 productions or ≥ 1 accepted category, stable across ≥ 2/3 seeds. Partial outcome worth recording: if CSSR (E5) passes as a control but the CLA arm cannot beat it, the documented conclusion is "attractor structure is sofic, not chunk-hierarchical" — which is a scientific result, not a failure of the programme, and redirects chunk/category CLA to protocol-like data.

---

## E8 — OmegaSim, gated

Only after E7 resolves (either a CLA pass, or a CSSR pass with the sofic conclusion adopted).

**E8a — planted positive control.** Implant a known recoverable grammar (an E3 family that the promoted pipeline reliably recovers) into an A6-like observation channel: map grammar symbols to appraisal-trace feature patterns with matched noise. 12 cells, 3 seeds. **Gate:** the pipeline recovers the planted grammar (nontrivial, beats controls, nulls rejected) in ≥ 10/12 cells. If not, the observation channel destroys structure — fix the export/featurization before any endogenous claim.

**E8b — endogenous A6 re-sweep.** Only cells and only the frozen pipeline; same promotion rule as E7 plus the A6 matched appraisal/linear/shuffled controls. Budget: one sweep. If every grammar is again trivial *with E8a passing*, that is now evidence about OmegaSim dynamics rather than about the instrument — the first time that inference becomes licensed.

---

## Cross-cutting rules

1. Freeze this document (config hashes, thresholds, predictions P1–P4) before E2. E0–E1 may run during freeze review since they induce no grammars.
2. Never tune coder order, alpha, CSSR alpha/history, k, or thresholds on any suffix that has been scored. Prefix-only selection, one frozen choice per experiment.
3. Every run: ledger on, config hash + commit + seed recorded, fresh-trajectory seeds drawn from a preregistered seed list.
4. A control beating CLA is a result, not an error. In particular, CSSR beating chunk-CLA on attractors is the *expected* outcome under the sofic hypothesis and should be written up as such.
5. Negative-result write-ups follow the observed/inferred separation of the July report.
6. Stop-loss: if E3's representation gate fails twice (two coding iterations), escalate to the math track (probabilistic grammar semantics / quantale formulation) before further engineering.
