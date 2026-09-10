# Source: Boundary Theorems and Bench Findings: Reconciling the CAROM Experimental Program with the Oruzi Formal Corpus

- Type: `PDF`
- Authors/organization: CAROM series working note; individual author not stated
- Publication/version date: July 2026 (PDF created 2026-07-21)
- Retrieved: `2026-07-21`
- Canonical URL or identifier: Telegram-supplied document; no public identifier stated
- Local source path: `library/carom-oruzi-reconciliation-2026/source.pdf`
- Extracted text: `library/carom-oruzi-reconciliation-2026/source.txt`
- SHA-256: `2c9d67957138aa1ec341e11b95788c3d6cb495891dc93b5614128ea90462c050`
- License/access constraints: Not stated; retain locally and do not publish without clarification
- Privacy tier: `local-private`
- Tags: `CAROM`, `Oruzi`, `Lean`, `commutation`, `intervention probes`, `predictive coding`, `consolidation`, `portfolio evaluation`
- Related projects: `projects/carom`; potentially `projects/hyperseed-formalizations`

## Summary

Six-page working note connecting CAROM bench findings to boundary theorems in
four Oruzi Lean-formalized notes. Its highest-information empirical proposal is
a checkpoint sweep combining repaired itinerary metrics, causal interventions,
local Jacobian commutator energy, and exact nonlinear phase-swap discrepancy to
distinguish metric artifact, mechanistic drift, and learned commutation. It also
proposes schedule-switching stress tests, perturbational cross-slot coupling,
decisiveness telemetry, staged PC-CAROM ignition, reachability-first teach-loop
registration, portfolio evaluation, and a belief-register CAROM arm.

## Key claims or contents

- The tau decline from 0.990 to 0.492 admits a third interpretation beyond
  metric artifact and mechanistic drift: learned phase commutation may make
  order causally unnecessary (section 3, page 3).
- The proposed discriminator is a joint checkpoint panel, not endpoint
  accuracy alone: repaired itinerary measures, causal gap, JVP commutator
  energy, and nonlinear swap discrepancy (section 3, page 3).
- A sandbox smoke checkpoint reportedly showed adversarial alternation growth
  of 3.85x median / 4.85x maximum over 16 phases and a sampled random-product
  p90 of 1.074 (section 4.3, page 4). This is supplied evidence, not independently
  reproduced here.
- Cross-slot perturbation reportedly yielded normalized off-diagonal mass 0.60
  on the sandbox artifact (section 4.4, page 4). This is supplied evidence and
  the categorical interpretation depends on an unvalidated normalization and
  threshold.
- PC-CAROM is rescoped toward staged BPTT-to-PC ignition in a thin cap over an
  exactly frozen backbone, with residual-criterion settling (section 5,
  pages 4-5).
- Teach-loop registration should test gate-space reachability before tuning a
  KL no-regression term, then use cached old-command routing distributions and
  paired routing/operator attribution (section 6, page 5).
- Execution semantics should be treated as a portfolio, reporting union and
  unique coverage, with a proposed belief-register fifth arm (section 7,
  page 5).
- Six candidates are proposed for formalization: heteroclinic execution,
  quantitative routing bottlenecks, routing interference under action-space
  growth, convergence-depth sensitivity, nonlinear order independence, and
  itinerant containment (section 8, pages 5-6).

## Methods or implementation details

The note refers to the separately supplied `harness_v3_probes.py`. It proposes
read-only evaluation of retained checkpoints, forward-mode JVPs rather than
explicit Jacobians, nonlinear swapped phase execution, adversarial switching,
input perturbations for slot coupling, and entropy-based decisiveness measures.
The immediate run list is on page 6.

## Limitations and uncertainties

- The named Lean declarations and their assumptions are not included or
  bibliographically linked in this PDF, so theorem-to-bench correspondence
  remains to be checked against the formal sources.
- The supplied v3 code has eight blocking compatibility/correctness issues;
  see `projects/carom/docs/compiled-channel/harness_v3_probes_audit_2026-07-21.md`.
- Metric artifact, mechanistic drift, and learned commutation can coexist; the
  page-3 decision table is a heuristic reading guide, not yet a validated
  classifier.
- A sampled random-product p90 above one can motivate a numerically validated
  instability witness, but the proxy and adversarial norm growth need a matched
  natural baseline; values below one could not certify joint spectral stability.
- The smoke readings are demonstrations on an early sandbox checkpoint and
  have not been independently reproduced.
- Visual inspection of all six pages found severe column overlap in the
  correspondence ledger on page 2. The extracted text is also interleaved there;
  use the original source material rather than page 2 for exact row attribution.
- Authorship, public canonical location, and license are not stated.

## Relevance to current work

Rules 1, 2, 5, 6, and 7 of `catalog/RESEARCH_RULES.md` are especially relevant:
validate the new estimators with constructed controls; specify the joint panel
before coding; preserve reproducible probe settings; connect the nonlinear
measurements to the formal boundary results; and expose span/checkpoint/probe
interfaces cleanly. The note strengthens the rationale for repairing v3 first,
then running the checkpoint-only tau panel without interrupting active training.

## Quotations or excerpts

“Learned commutation” is the note's label for the hypothesis that execution
order ceases to matter as effective phase maps approach commutation (page 3).

## Follow-up questions

- Which exact repositories, commits, and declarations comprise the four Oruzi
  formal notes, and do their assumptions match the CAROM phase maps?
- After probe repair and constructed controls, do interference and nonlinear
  swap discrepancy fall with tau across the retained checkpoints?
- Does a validated instability witness persist at the final GPT-2 checkpoint
  relative to a matched natural-schedule baseline?
- Can teach-loop reachability be operationalized as a rank/range test for the
  actual gate parameterization before KL registration experiments?
