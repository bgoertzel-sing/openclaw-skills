# Source: Initial Abstract Algorithmic Chemistry Experiments in PeTTa

- Type: `PDF`
- Authors/organization: Benjamin Goertzel / human researchers and coding agents
- Publication/version date: June 2026
- Retrieved: `2026-06-26`
- Canonical URL or identifier: Telegram upload from Benjamin Goertzel; local OpenClaw media import
- Local source path: `library/petta-abstract-algorithmic-chemistry/source.pdf`
- Extracted text path: `library/petta-abstract-algorithmic-chemistry/extracted.txt`
- SHA-256: `341643e264c562d476b46172a5f284657de49f6eb2a99764c8ad71bbac693d23`
- License/access constraints: local research use; confirm before redistribution
- Privacy tier: `local-private`
- Tags: PeTTa, MeTTa, Atomspace, MORK, algorithmic chemistry, autocatalytic sets, RAF, active predictive coding, semantic chemistry, music chemistry
- Related projects: `projects/petta-chem`

## Summary

This 34-page design document specifies a PeTTa-first, MORK-ready research and implementation plan for abstract algorithmic chemistry. The immediate target is a bounded symbolic chemical soup represented in Atomspace-style atoms, with typed catalytic multiset rewrites, seedable stochastic execution, event logs, ACS/RAF-like mining, and replay/ablation tests.

The key scientific milestone is to demonstrate spontaneous, measurable, replayable, and intervention-relevant autocatalytic organization in an abstract PeTTa chemistry before adding semantic graphs, music-specific molecules, MORK execution, PLN, MOSES, or other larger integration layers.

## Key claims or contents

- First milestone: demonstrate spontaneous, measurable, replayable, intervention-relevant autocatalytic organization in bounded abstract PeTTa chemistry. Evidence: extracted text lines 171-177.
- Rationale for starting abstract: it reduces confounds from semantic normalization, truth-value dynamics, natural language realization, and musical scoring while preserving later substrate structure. Evidence: lines 182-205.
- MORK is a future acceleration/integration seam, not part of the first milestone; initial implementation should still preserve replaceable request/response interfaces for matching, sampling, scoring, ACS scanning, canonical hashing, replay, and structural mutation. Evidence: lines 207-227 and lines 1403-1422.
- Core questions: ACS emergence, ecological dynamics, endogenous rule evolution, predictive weighting, and causal relevance. Evidence: lines 230-262.
- Experiment ladder: exp00 deterministic replay smoke test, exp01 planted ACS recovery, exp02 random catalytic polymer chemistry, exp03 rule molecules, exp04 ecology/parasites, exp05 active-predictive weighting, exp06 trace-guided mutation, exp07 causal ACS archive. Evidence: contents lines 66-74 and appendix lines 1110-1398.
- Testing discipline emphasizes seed determinism, planted ACS recovery, ablation replay, candidate caps, and rejecting false ACSs in controls. Evidence: lines 1388-1401.

## Methods or implementation details

- Molecules start as token sequences/small symbolic objects with opaque typed views so later graph, phrase, motif, or rule-body views can be added.
- Rules are typed catalytic rewrites over multisets, initially one/two reactants and one/two products.
- Initial reaction families include concat, split, mutate-token, copy, compress/decompress, and later rule-mutate/rule-compose.
- Phase engine tick order: food inflow, decay/dilution, active signatures, candidate matching, scoring, seeded sampling, firing, abundance update, event logging, catalysis mining, ACS scanning, structural mutation, cleanup.
- Analytics should emit atoms for catalysis, inhibition, ACS membership, persistence, productivity, and causal tests, not only plots or external CSVs.
- Run outputs should include configs, manifest, events JSONL, abundances, metrics timeseries, ACS candidates, ablation results, rule lineages, and summary.

## Limitations and uncertainties

- The document is a plan, not an executed result; no ACS emergence is yet demonstrated.
- PeTTa implementation constraints, existing repository state, and available runtime APIs still need inspection before choosing exact language/runtime layout.
- The extracted text is OCR/text-conversion output from the PDF; inspect the PDF directly before relying on page formatting, figures, equations, or exact typography.
- Redistribution/license status is not specified in the PDF upload; treat as local-private until clarified.

## Relevance to current work

This is the seed specification for `projects/petta-chem`. It provides the initial milestone ladder, schema requirements, test criteria, implementation boundaries, and review checkpoints for a PeTTa abstract chemistry prototype.

## Quotations or excerpts

> Demonstrate spontaneous, measurable, replayable, and intervention-relevant autocatalytic organization in a bounded abstract PeTTa chemistry.

> A coding agent should not be asked to “implement algorithmic chemistry” in one step. It should be given the appendix as a milestone ladder.

## Follow-up questions

- Which existing PeTTa repository should be used as the primary implementation base, if any?
- Should version 0.1 be Python-first for rapid experiment iteration, Rust-first for performance/replay rigor, or mixed with a thin PeTTa/MeTTa atom protocol and Python host kernels?
- What minimum PeTTa integration is required for exp00 to count as PeTTa-first rather than merely Atomspace-shaped host code?
