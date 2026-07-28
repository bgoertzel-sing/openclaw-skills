# Fable review: learned/free-inhibition CAROM

Date: 2026-07-20

Materials reviewed: the r1 GPU report, the original CAROM sandbox report, and
the original itinerant-dynamics note.

## Main judgment

The 86.5% free-inhibition result is promising, but does not yet establish a
learned stable heteroclinic channel or learned transition graph. The current
comparison confounds controller quality with recurrent exposure, dwell time,
overlap, initialization, ordinal bias, and evaluation noise.

## Highest-priority findings

- The GLV modes represent command positions, not the 16 neural operators.
- Workspace fitness is effectively shared across modes, so workspace content
  cannot select which command-position mode should invade next.
- The free arm retains strong scaffolding: ordered command presentation,
  phase-0 initialization, ordinal bias, fatigue, and a positive activity floor.
- The 70-step itinerant arms are not compute/exposure matched to the five-step
  scheduled arm, and fixed versus free activity exposure is not normalized.
- Current trajectory evidence is one coarsely sampled example; it does not
  establish transition reproducibility, dwell distributions, perturbation
  recovery, or stable-heteroclinic-channel dynamics.
- Evaluation needs fixed suites, separate RNGs, multiple seeds, depth
  stratification, and deterministic control dynamics.

## Recommended direction

First repair the measurement instrument. Then add mode-specific
command/workspace fitness and generic, graph-unsupervised regularizers for
metastability, low overlap, forward progress, and non-revisitation. Do not
initialize near the hand-coded chain, because that would weaken the central
learning claim.

