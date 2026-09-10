# Source: HDC–CGCCT source manuscript bundle

- Type: `PDF bundle`
- Authors/organization: Ben Goertzel
- Publication/version dates: 2026-05-04, 2026-05-20, 2026-06-03, and 2026-07-26
- Retrieved: `2026-07-26`
- Canonical URL or identifier: Not supplied; author-provided PDFs
- License/access constraints: Copyright/license not specified; local research use
- Privacy tier: `local-private`
- Tags: `HDC`, `CGCCT`, `linguistic universals`, `hypervector frames`, `closure`, `capacity`
- Related projects: `projects/hdc-cgcct-transformers`

## Files and hashes

| Manuscript | Local PDF | Extracted text | SHA-256 |
|---|---|---|---|
| *Hypervector Frames for Category-Guided Causal Coding* (2026-07-26) | `hdc_cgcct_synthesis.pdf` | `hdc_cgcct_synthesis.txt` | `086f282ce3f95e98bb3924de91cf7562553f6d42d6b8c58922f1a5a002d0fb20` |
| *Resonator-Factored Hierarchical Hypervector Embeddings* (2026-06-03) | `hdc_guided_factorization_v5.pdf` | `hdc_guided_factorization_v5.txt` | `fd5fdd12954c8d0e03c388f6ee466e868c0b0c55ecdfa1994cdeed252cb121d9` |
| *Category-Guided Causal-Coding Transformers* (2026-05-20) | `category_guided_causal_coding_transformers.pdf` | `category_guided_causal_coding_transformers.txt` | `6601e3d808846c44205762c35d071db810bf050536435e855c9191c0328d9f21` |
| *Linguistic Universals as Quantale-Enriched Cognition–Language Correspondences* (2026-05-04) | `causal_coding_linguistic_universals_category_v4.pdf` | `causal_coding_linguistic_universals_category_v4.txt` | `b2a9d341fc999c6a07d43d7b0e91ad559625d7c0f60a9ff6dfe78bfda0e64ca5` |
| *Linguistic Universals as Cognitive Universals* (2026-05-04) | `linguistic_universals_as_cognitive_universals_v5.pdf` | `linguistic_universals_as_cognitive_universals_v5.txt` | `3bf76aaf2176aebae87d33c894f5003eacadfa7e4fcd60789a6b200fb8439cb1` |

## Summary

The July synthesis proposes hypervector frame codes as a computable object
language for CGCCT and specifies stages P0–P6. P0 builds and self-tests a
deterministic bipolar-MAP frame library. P1 uses a planted hierarchy in a
synthetic grammar to validate cleanup/probe behavior before any frozen-model
or guided-training claim.

The June HDC manuscript establishes the independent-random-code cleanup bound
and fixed-query-family capacity theorem under random-atom, isometric-binding,
bounded-load, and finite-codebook assumptions. It does **not** contain the
coherence-aware lemma or near-duplicate exponent quoted by the July synthesis.
Those appear in the later 2026-07-25 HDC manuscript already preserved at
`../resonator-factored-hierarchical-hypervector-embeddings/`.

The May CGCCT manuscript gives an approximate closure-preservation result:
probe-level one-step errors telescope along a hierarchy chain, conditional on
the probes already being delta-calibrated. It does not define an empirical
estimator that turns HDC cleanup error into that delta.

## Key claims and evidence locations

- Frame encoding, capacity formula, and the explicit hierarchy-coherence
  conjecture: synthesis Sections 2.2–3.3, pp. 4–6; extracted lines 158–270.
- P0/P1 procedures and source gates: synthesis Appendix A.3–A.4, pp. 10–11;
  extracted lines 482–540.
- Independent cleanup and local query capacity: June HDC Sections 5.1–5.3,
  pp. 11–13; extracted lines 542–673.
- Approximate closure preservation conditional on delta-calibrated probes:
  CGCCT Theorem 7.3, p. 17; extracted lines 884–901.
- The synthesis itself labels “hierarchies live in the high-coherence regime”
  as Conjecture 1; it is not a consequence of the closure theorem.

## Methods or implementation details

- Synthesis P0 fixes float32 bipolar MAP and deterministic per-coordinate
  tie-breaking, but does not say whether an exact zero maps to `+1` or `-1`.
- P1 asks for a six-layer next-token transformer over a PCFG with hierarchy
  length 4 or 6, a linear residual-stream-to-frame readout, dimensions
  256–16384, coherence measurements, and a fitted required-dimension law.
- The exact PCFG, split construction, trial count, confidence procedure,
  calibration definition, feature thresholds, and fitted-exponent estimator
  are left unspecified.

## Limitations and uncertainties

- The July synthesis cites external literature from model memory and explicitly
  warns that those citations need verification.
- “Probe calibration is discharged” is stronger than the displayed results:
  HDC cleanup controls coding error conditional on a correctly encoded target
  plus admissible crosstalk, while a learned transformer readout introduces a
  separate factorization/readout error.
- An implication chain does not by itself make independently drawn feature
  atoms coherent. Near-duplicate scaling requires an additional code
  construction in which adjacent dictionary entries share constituents.
- The June and July HDC manuscripts are materially different versions. Claims
  must cite the version containing the claimed lemma.
- No source supplies a preregistered, independently runnable P1 implementation.

## Relevance to current work

The bundle is the source basis for
`projects/hdc-cgcct-transformers/docs/p0-p1-spec.md`. The specification
separates oracle-code capacity validation from learned-readout validation and
uses independent-code and planted-near-duplicate hierarchy fixtures so the
coherence conjecture cannot pass merely by construction.

## Follow-up questions

- What operational notion of delta-calibration is intended in CGCCT Theorem
  7.3: probability calibration, uniform score error, or classification error?
- Is the July 25 HDC manuscript the intended normative HDC source for the July
  26 synthesis?
- Should a future natural-language hierarchy test learn the feature dictionary
  without an adjacency-coherence prior, or impose the constituent-sharing
  representation proposed by the conjecture?
