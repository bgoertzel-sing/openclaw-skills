# Source: Atlas-Indexed Reversible Evidence-Fibered Geodesic πPLN

- Type: `PDF`
- Authors/organization: Benjamin Goertzel, with GPT-5.6 Pro assistance
- Publication/version date: 2026-07-12
- Retrieved: 2026-07-11 PDT
- Canonical URL or identifier: Telegram attachment `pipln_patham9_software_design_spec`
- Local source path: `library/atlas-indexed-reversible-pipln/specification.pdf`
- Extracted text: `library/atlas-indexed-reversible-pipln/specification.txt`
- SHA-256 (PDF): `1af20c7427b484a978507181c44fb32112257f029aa130c30f1c8a45d0d7f0d3`
- SHA-256 (text): `26f782ec08cf84c3d51be0eaf65ca87d021915f089ab8b16311d580edb889e76`
- License/access constraints: Author-supplied project design; no redistribution license stated.
- Privacy tier: `local-private`
- Tags: `piPLN`, `patham9`, `PLN`, `evidence`, `provenance`, `geodesic-control`, `replay`, `contexts`, `charts`
- Related projects: `petta-memory`, `omegaclaw`, `hyperseed-formalizations`

## Summary

Normative software design for implementing an atlas-indexed, reversible, evidence-fibered and geodesically controlled πPLN around the public patham9 PLN kernel. The persistent source of truth is a context-indexed evidence/provenance layer; patham9 remains a replaceable chart-local scalar-STV derivation kernel. The design specifies typed records, exact overlap handling, deterministic episode-local stamps, chart projection policies, hierarchical outer/inner control, proof-class de-duplication, event-sourced replay and rollback, revision and promotion gates, curvature/descent diagnostics, interfaces, security boundaries, tests, migration, and an eight-phase roadmap.

## Key claims or contents

- The strict architecture boundary keeps persistent evidence, contexts, control and audit outside patham9; a patham9 call is a temporary local episode (Abstract; §§4–5).
- Semantic confidence must not carry controller utility because current patham9 scheduling and truth formulas consume confidence (§3.2, Invariant 3.1).
- Episode stamps must be collision-free deterministic integer aliases for immutable evidence-basis units; unequal IDs do not by themselves establish causal independence (§§3.3, 8.2–8.4).
- Empirical packets must be provenance-aware and aggregated before prior-aware projection; priors are chart-local and must not cycle into evidence (§§3.4, 5, 10).
- Pure inference conserves primitive evidence support; evidence fusion is idempotent; contexts remain separate absent typed translations (§5, Invariants 5.7–5.11).
- Migration maps current wrapper functions to target components while retaining compatibility adapters (§27.1–27.3).
- The implementation roadmap proceeds from baseline freeze through typed evidence/charts, isolated episodes, geodesic control, proof geometry/reversibility, atlas transitions, native geodesic integration, curvature/descent, and reviewed promotion (§29).
- Acceptance requires algebraic/property, differential, metamorphic, integration, security, replay, controller, geometry and chaos testing (§25).

## Methods or implementation details

- Content-addressed fingerprints include context, assumptions, prior, projection/rule policies, evidence snapshot, kernel and translator versions (§6).
- Canonical projection uses beta-prior virtual counts while retaining evidence mass, balanced conflict and signed tendency separately (§10).
- Three kernel-control modes share a capability-negotiated `KernelControlPort`: legacy microsteps, overlay hooks and future native geodesic control (§12).
- Repository layout and coding-agent task packet/definition-of-done are given in §§28–29 and Appendix A.

## Limitations and uncertainties

- Native patham9 geodesic API is forthcoming and must not be assumed (§30.4).
- Distinct primitive tokens do not prove causal/statistical independence (§30.2).
- Arbitrary derived STVs cannot generally be inverted to empirical counts (§§2.2, 10.4).
- Rule identity may remain ambiguous without an overlay or upstream event seam (§30.5).
- Curvature and chart-gluing conclusions are policy/model-class relative (§§30.8–30.9).

## Relevance to current work

This supersedes the earlier informal wrapper-extension roadmap as the normative implementation contract for the `petta-memory` patham9/πPLN track. Existing functions remain useful as compatibility baselines but should migrate behind typed components rather than accrete more one-off wrappers. At this strategic pivot, Research Rules 1, 2, 3 and 7 are especially relevant: validate semantic machinery, implement from this explicit specification, preserve patham9 as the existing framework, and enforce replaceable abstraction seams.

## Quotations or excerpts

> “The durable system is the atlas, evidence store, proof geometry, controller, and audit log. patham9 is a chart-local rule engine.” (§31)

## Follow-up questions

- Which existing serialized handoff artifacts require first-class migration readers beyond the compatibility adapter?
- What exact public API and event granularity will the native patham9 geodesic controller expose?
- Which evidence-basis policies can initially earn `PROVEN_DISJOINT` rather than `UNKNOWN`?
