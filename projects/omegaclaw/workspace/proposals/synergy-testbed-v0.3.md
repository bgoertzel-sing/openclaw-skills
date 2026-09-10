# Testbed Protocol v0.3: Measuring Multiplicative Synergy — PLN + Perceptual NN

**Status:** draft for Ben's review (Hugo requested 2026-07-25, #hugo-chat; v0.2: D1 co-primary, open questions provisionally answered; v0.3: theory-driven interference pre-analysis plan)
**Claim under test:** shared-substrate integration (Hyperon AtomSpace) yields *superadditive* performance vs. best-in-class hub-style composition of the same modules.

## Primary metric
Superadditivity ratio: `S = P(integrated) / P(hub baseline)`, reported as a **distribution** across tasks, not a mean.
- S > 1 → synergy; S ≈ 1 → mere integration; S < 1 → interference (reported, not hidden).

## Co-primary contrasts
1. **C vs. B** — does full integration beat best-in-class hub composition? (Tests "integration is good.")
2. **C vs. D1** — does substrate coupling beat text-like exchange over the same shared memory? (Tests "*substrate* integration is good.") If D1 ≈ C, the win is memory-sharing — achievable without Hyperon — not substrate coupling. Both contrasts are preregistered co-primary; neither is a fallback for the other.

## Conditions (same modules, same training data, matched compute/parameter budget throughout)
- **A. Isolated modules** — floor reference only; never the primary denominator.
- **B. Hub baseline** — modules composed through an LLM hub with tool access (retrieval, code exec, API calls). Text/JSON interfaces. This is the *primary comparator*: the claim is shared-substrate beats best-in-class integration, not beats nothing.
- **C. Full Hyperon integration** — shared AtomSpace; modules recurrently transform shared state (PLN over grounded perceptual atoms).
- **D. Substrate ablations** (isolate the causal factor):
  - D1: shared AtomSpace but text-like message exchange only
  - D2: shared memory, separate reasoning loops
  - D3: shared reasoning, separate memories

## Module pairing
Perceptual NN (scene → relational representation grounded into AtomSpace) + PLN (relational/inferential reasoning). Chosen because neural/symbolic grounding mismatch is the known hard case — if synergy shows here, it's informative; if it fails here, that's equally informative.

## Task suite
Sampled **independently** of the grounding hypothesis (e.g., CLEVR-style relational VQA, physical-scene SORT-like tracking+query, novel-relation generalization splits). Stratified *post hoc* by cross-module grounding demand (trivial → hard). The persuasive output is the **dose-response curve**: S vs. grounding demand, per condition.

## Analysis plan
- Co-primary contrasts (C vs. B, C vs. D1): per-task S distributions; bootstrap CIs; preregistered threshold for "meaningful synergy" (propose S > 1.2 median on high-grounding stratum).
- S < 1 cases analyzed against the preregistered interference hypotheses below (theory-driven, not cherry-picked); collisions matching none of them are flagged as exploratory findings.

## Interference pre-analysis plan (preregistered hypotheses for S < 1)
- **H1 — grounding granularity mismatch:** NN's continuous embeddings are quantized into atoms; PLN over-commits on borderline cases. Signature: S<1 concentrated on ambiguous/borderline scenes.
- **H2 — truth-value noise amplification:** noisy perceptual confidences propagate through PLN deduction chains, compounding with proof depth. Signature: S declines monotonically with required proof depth.
- **H3 — attention/resource contention:** perceptual salience and reasoning salience compete in the shared AtomSpace (ECAN). Signature: S<1 on cluttered scenes with deep queries, spared on clean scenes with equally deep queries.
- **H4 — ontology mismatch:** NN's learned relation categories misalign with PLN's relational schema; mapping layer drops/distorts relations. Signature: failures concentrated on novel-relation generalization splits.
Each hypothesis has a distinct predicted failure signature, so post-hoc case studies are confirmatory against preregistered predictions, not narrative.
- Ablation contrasts (D1–D3 vs. C) attribute gains to shared memory vs. shared reasoning vs. both.
- Multiple seeds; report variance. No cherry-picked task subset.

## Deliverables
1. Preregistration doc (metric, baselines, thresholds) — before any runs.
2. Runnable harness (conditions A–D behind one config).
3. Results report: S distributions, dose-response curves, interference case studies.

## Open questions for Ben (Hugo's provisional answers, pending Ben's sign-off)
- Perceptual NN: reuse ECAN-tuned Hyperon vision components if available — keeps the substrate honest.
- AtomSpace: local for the harness; DAS adds a confound at this stage.
- Condition-B compute: same budget as C — not more, not less (keeps "best-in-class" honest without handicapping).
