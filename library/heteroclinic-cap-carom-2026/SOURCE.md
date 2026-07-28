# Source: The Heteroclinic Cap

- Type: PDF working note plus supplied Python prototype
- Authors/organization: supplied by Benjamin Goertzel; authorship not stated in PDF metadata
- Publication/version date: July 2026
- Retrieved: 2026-07-20
- Canonical identifier: Telegram attachment; no public URL supplied
- Local source path: `heteroclinic-cap-report.pdf`
- Extracted text: `heteroclinic-cap-report.txt`
- PDF SHA-256: `95c4a0147320512cbb682cbecf5ba7bfb36116a85c5f1d25081af3ac5f666bdb`
- Supplied code SHA-256: `e8acb6a3dd9fb761c76487bfcd1eb49a4c93ebd2540f438a50e73550285d52b8`
- License/access constraints: no license stated; preserve locally, do not publish
- Privacy tier: local-private
- Tags: CAROM, heteroclinic dynamics, frozen language model, compiled control
- Related projects: `carom`, `relaleap`

## Summary

The note proposes a heteroclinic-dynamics runtime on frozen language-model span
representations. A hypernetwork maps command spans to operator mixtures; a
pairwise dependency scorer compiles a per-instance GLV inhibition matrix; an
entry scorer chooses the initial station. The new experiment scrambles command
presentation and tests whether dependency language can compile execution order.

## Key claims or contents

- The LM is framed as compiler and GLV/CAROM as persistent runtime (pp. 1--2).
- A supplied CPU sandbox reportedly validates fixed-chain execution and
  representation routing, but not semantic transfer or compiled topology
  (pp. 3--4).
- Experiment 2 compares compiler-supervised and task-only edge learning using
  task accuracy, edge quality, itinerary Kendall tau, and L=5 generalization
  after training on L=2--4 (pp. 4--5).
- Experiment 3 proposes an ePC-trained versus standard frozen-base comparison
  on probe accessibility and cap transfer (p. 5).

## Methods or implementation details

The script uses distinct primitives, natural-language predecessor clauses, a
pairwise edge scorer, an entry scorer, and differentiable GLV compilation. It
supports supervised edge loss and task-only learning. A two-update local CPU
smoke completed on 2026-07-20.

## Limitations and uncertainties

- The executable uses `TinyLM`; GPT-2 is only commented pseudocode (code lines
  130--141). Running it unchanged on GPU is not a GPT-2 experiment.
- Training and evaluation share one RNG, so evaluation changes later batches
  (lines 288 and 320--322).
- Threshold edge accuracy is class-imbalanced; AUROC, AUPRC, positive recall,
  and exact-graph accuracy are needed.
- Evaluation sets are regenerated and the default is one seed.
- The task-only regime retains dependency clauses, distinct primitives, fixed
  compilation constants, activity floor, and fatigue.
- Sandbox results remain supplied claims, not independent reproductions.

## Relevance to current work

This changes the question from learning one global inhibition matrix to
compiling per-instance topology from language. It complements, but does not
replace, the active E0/E1 exposure-controlled audit.

## Follow-up questions

- Which frozen base/layer passes a preregistered dependency/primitive probe?
- Does compiler supervision beat oracle-topology and null-graph controls?
- Does L=5 performance reflect topology rather than language/core leakage?
- Does E1 activity normalization alter compiled-channel performance?
