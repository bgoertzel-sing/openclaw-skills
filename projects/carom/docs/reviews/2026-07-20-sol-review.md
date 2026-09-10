# Sol review: learned/free-inhibition CAROM

Date: 2026-07-20

Materials reviewed: the r1 GPU report, the original CAROM sandbox report, and
the original itinerant-dynamics note.

## Main judgment

The result shows trainable competitive dynamics can support useful recurrent
computation, but not yet that the system learned a stable heteroclinic channel
or learned its transition graph from task supervision. The immediate priority
is exposure normalization and mechanism-valid diagnostics, not simply stronger
inhibition.

## Highest-priority findings

- Effective operator amplitude depends on total activity; integrated command
  exposure and overlap can explain much of the fixed/free accuracy gap.
- The free arm includes a fixed entry state, ordinal prior, fatigue, activity
  floor, and commands already arranged in the correct order.
- The dynamics are better described as heteroclinic-like metastable transients:
  the positive floor, noise, fatigue, changing fitness, and finite horizon
  remove the invariant axes and fixed saddles needed for an exact SHC claim.
- The learned inhibition matrix did move substantially and acquired qualitative
  forward adjacent asymmetry, so the learning signal is real enough to pursue.
- The displayed single-example trajectory hides substantial across-example
  heterogeneity and does not even visibly establish all five phases in the
  fixed-chain positive control.
- Evaluation and training RNGs are coupled; evaluation itself perturbs random
  state, and synonyms are not actually parameter-tied.

## Recommended direction

Normalize activity-weighted operator mixing, measure integrated exposure,
install fixed deterministic evaluation suites, and test generic regularizers
that reward low overlap and orderly non-revisiting transitions without encoding
a successor graph.

