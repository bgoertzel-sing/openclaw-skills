# Chaos Language Algorithm

## Purpose

Implement and test the Chaos Language Algorithm (CLA): symbolize continuous chaotic trajectories and induce exact-reconstructing grammars using joint chunk and category compression under MDL.

## Source specification

- Library sidecar: `../../library/chaos-language-algorithm/SOURCE.md`
- Algorithm spec PDF: `../../library/chaos-language-algorithm/chaos_language_algorithm_ascii.pdf`
- Algorithm spec extracted text: `../../library/chaos-language-algorithm/extracted.txt`
- Algorithm spec SHA-256: `468c5f49ec7d484bb58a6bc53e28a13f2bba1512be898791ddaea2e96c8af510`
- Python architecture PDF: `../../library/chaos-language-algorithm/cla_python_library_architecture_ascii.pdf`
- Python architecture extracted text: `../../library/chaos-language-algorithm/cla_python_library_architecture_extracted.txt`
- Python architecture SHA-256: `3beacd7855f2fa3912d43d026f175b5518ba08216e19f741540a5de7d20d97c4`

## Current status

`active` / local-only. Ben promoted CLA on 2026-07-03 as the prerequisite for resuming OmegaSim: build a general toolkit for recognizing grammars of strange attractors, strange transients, and related structures. Sprint-1 local pure-Python `chaoslang` prototype now implements exact-reconstructing symbolic-string grammar induction with chunks, categories, approximate MDL, fact projection, and tests; next target is richer persistence plus attractor benchmarks up to OmegaSim starter-vector dimensionality.

## Implementation principles

- Preserve the chunk/meta-symbol distinction.
- Accept edits by MDL reduction, not frequency alone.
- Preserve exact reconstruction after every accepted edit.
- Store category occurrences as `M[v]` or an equivalent explicit member side table.
- Start with hard/disjoint categories and deterministic tests.

## Repository

Local prototype: `projects/chaos-language-algorithm/repos/chaoslang`.
Remote: `https://github.com/bgoertzel-sing/chaos-language-algorithm` (public as of 2026-07-03; sprint-1 implementation pushed to `main` at `4a7399c`).

## Relationship to OmegaSim

Ben paused OmegaSim on 2026-07-03 until CLA or a similar grammar-of-attractors detector is robust enough to evaluate whether simulated OmegaHive dynamics actually contain complex strange-attractor structure. CLA therefore becomes the current prerequisite lane for OmegaSim detector calibration.
