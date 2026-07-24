# CAROM E2/E3 Mode-Fitness and Generic Channel Specification

Date: 2026-07-24

## Question

Can randomly initialized free inhibition learn a more accurate and structurally
valid trajectory when fitness is mode-specific, and can generic channel
penalties improve it without encoding a successor relation?

## Frozen instrument

- Evaluation corpus seed `20260720`, balanced depths 2--5.
- Training seeds `7,17,27,37,47`; distinct Python training RNG per arm/seed.
- Evaluation is noise-free and has no random initial-activity perturbation.
- Every arm uses random free-inhibition initialization, never the fixed chain.
- Endpoints: paired accuracy, activity mass, overlap, switching, revisits,
  terminal trapping, exposure, and workspace-update norm.

## E2 and E3

E2's full score is an MLP over pooled workspace, command embedding, position
embedding, and pooled-workspace/command interaction. Compare workspace-,
command-, and position-ablated arms.

E3 adds only mode-permutation-invariant penalties: simultaneous overlap,
insufficient temporal switching/progress, lagged self-overlap, low tail
variance, and deviation from an activity-mass target. No term identifies a
mode pair, direction, successor, predecessor, or `m -> m+1`; a test verifies
invariance under arbitrary mode permutation.

E2/E3 advance only on held-out accuracy jointly with trajectory validity,
without excess exposure. E4 and E5 remain closed until a full five-seed result
passes. Paid or remote execution requires fresh authorization; the old USD 20
E0/E1 authorization does not apply.
