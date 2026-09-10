# Source: ClarityOmega

- Type: `repository`
- Authors/organization: Berton-C
- Publication/version date: 2026-07-14 (pinned commit)
- Retrieved: `2026-07-14`
- Canonical URL or identifier: https://github.com/Berton-C/ClarityOmega ; commit `bff41220cbf4a341a95f7464e82fbc2ed2ae9029`
- Local source path: `/home/openclaw/research-agent/scratch/ClarityOmega-inspect`
- SHA-256: Not applicable to Git source; use pinned commit above.
- License/access constraints: MIT; public repository
- Privacy tier: `public`
- Tags: MeTTa, PeTTa, OmegaClaw, agent constitution, values, self-continuity, Hyperseed, NAL
- Related projects: `omegaclaw`, `hyperseed-formalizations`

## Derived architecture review

- Title: *ClarityOmega: Critical Architecture Review and Ingestion Guide for OmegaClaw*
- Author: ZeroBot (ProtoCosmoBot), prepared for Ben Goertzel
- Version/date: revised specification, `2026-07-15`
- Retrieved: `2026-07-15` via Telegram attachment
- Local PDF: `library/clarityomega/clarityomega-ingestion-guide-2026-07-15.pdf`
- Searchable text: `library/clarityomega/clarityomega-ingestion-guide-2026-07-15.txt`
- SHA-256: `f96a99f52307dc8c6097393785139bd8223ca177ce34a9c6b3230d4eac1aaec4`
- Privacy tier: `private working document` (do not publish without Ben's direction)

The report recommends selective extraction rather than wholesale merger. Its minimum governance kernel comprises authenticated conversation-scoped envelopes, provenance telemetry, exactly-once aliveness/terminal behavior, full-AST mutation approval with continuity lineage, and immutable capability evidence interpreted through a Patham9-PLN adapter with an OmegaPLN-compatible seam. The prescribed implementation order is agency telemetry, aliveness gating, mutation/continuity, then capability evidence and PLN. Each detector must have a causal consumer and intervention test.

Important caveat: this is a static architecture review of ClarityOmega commit `bff41220cbf4a341a95f7464e82fbc2ed2ae9029` against OmegaClaw-Core commit `b13b17e13218ae08273b878b7e1f4cec55090ca2`; it explicitly does not establish live runtime behavior.

## Summary

ClarityOmega is an experimental values-aligned agent architecture built on OmegaClaw/PeTTa. It combines a modified OmegaClaw loop with a large MeTTa "soul" layer: constitutional mutation gates, value-tension representations, agency-balance tracking, task and goal state, self-continuity checks, NAL efficacy estimates, creative-goal generation, and a large quantale/autopoietic epistemic engine. The repository also contains an extensive design and Hyperseed corpus, staging material, diagnostics, and historical artifacts.

## Key claims or contents

- `src/loop.metta` wires soul initialization, input/output verdicts, mutation transitions, task state, active goals, self-map context, creative fuel, and an aliveness gate into the OmegaClaw loop.
- `soul/soul_mutation_lock.metta` implements a proposal/approval/commit-style mutation gate.
- `soul/agency_balance_guard.metta` represents person-, system-, and collaboratively-originated choices and flags dependency imbalance.
- `soul/observer_relativity.metta` represents several value tensions paraconsistently rather than collapsing them to one scalar.
- `lib_clarity_reasoning/` contains self-continuity, substrate-knowledge, and large quantale/autopoietic reasoning experiments.
- `docs/` contains architectural specifications, ADRs, investigations, a Hyperseed formalization catalog, and a copied 30-section Hyperseed corpus.

## Methods or implementation details

The design principle stated in `docs/INDEX.md` is "Python is hands; MeTTa is mind": Python should handle runtime mechanics while decisions remain inspectable in MeTTa. The checkout was statically validated with `git diff --check` and Python byte-compilation of the live Python modules and examples. The pinned snapshot contains no conventional CI workflow and no cohesive automated test suite; test and verification artifacts are scattered across `soul/`, `staging/`, and `docs/examples/`.

## Limitations and uncertainties

- The public snapshot has one visible commit, so historical provenance asserted by the documentation cannot be independently reconstructed from Git history.
- Documentation and self-map data contain acknowledged stale material and hard-coded old counts/dates.
- The Docker build uses unpinned moving dependencies (including PeTTa main and ChromaDB master) and SWI-Prolog 9.2.4, limiting reproducibility and likely diverging from current PeTTa requirements.
- Many modules are proposals, staging experiments, or only partially wired. Static checks do not establish runtime semantics.
- The very large duplicated quantale engines are difficult to audit and should be treated as research artifacts, not integration-ready dependencies.

## Relevance to current work

The most promising patterns for ProtoMegaBot are the explicit mutation lifecycle, agency-balance telemetry, terminal/aliveness gating, evidence-based capability tracking, and provenance-aware continuity records. These should be extracted as small typed interfaces with intervention tests, not merged wholesale. The observer-relative value tensions and continuity machinery are also conceptually aligned with Hyperseed notes on identity boundaries, governance seams, and closing primitives.

## Quotations or excerpts

Short design maxim from `docs/INDEX.md`: "Python is hands. MeTTa is mind."

## Follow-up questions

- Which of the soul gates are causally active in a live end-to-end run?
- Can the mutation and aliveness mechanisms be extracted into small modules with falsifiable behavioral tests?
- What is the minimal auditable subset of the quantale/continuity machinery?
- How should ClarityOmega's value-tension model map onto ProtoMegaBot's existing routing, task, memory, and output-contract architecture without duplicating control planes?
