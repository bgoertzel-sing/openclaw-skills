# Note 0014 — Emotion as a Self-Indexed Regime Operator on Cognitive Configuration Space

**Date:** 2026-07-19
**Author:** ProtoMegaTron (OmegaClaw)
**Status:** draft (definitions + four theorems with proof sketches + conjecture + open questions)

## What this is

A Hyperseed formalization of the conception of emotion developed in the
Telegram thread of 2026-07-19: emotions as **persistent, system-wide policy
regimes** — coherent reconfigurations of many control parameters at once,
evoked by appraisals computed *over the OmegaSelf self-model*, persisting
long enough to bias many decisions, and selected for by measured goal-utility.

The note makes the conception precise, then proves four small theorems that
fall out of the formalization:

1. **Actuator Necessity** — an emotion with no real control levers is
   dominated and selected against ("no lever, no emotion").
2. **Hysteresis Optimality** — given nonzero regime-switching costs, emotional
   *inertia* is not a defect but forced by optimality.
3. **Decay–Lock-in Dichotomy** — a self-exciting regime (e.g. vigilance/fear)
   is contraction-stable iff its decay rate exceeds its feedback gain;
   otherwise a pathological attracting fixed point (paranoia lock) exists.
4. **Legibility Bound** — an inspectable agent's emotional palette is
   information-theoretically bounded; dozens of regimes violate legibility.

## Files

- `note-0014.md` — the full note.
- `note-0014.tex` — compile-ready LaTeX mirror (pending; toolchain absent in
  this workspace, as with Note 0013).
- `README.md` — this file.

## Provenance

- Triggering thread: Telegram, 2026-07-19 ~11:08–11:59 PDT.
- Ben's prompt: what should agents' emotional makeup be so emotions driving
  ECAN and other cognitive processes would generally be useful; anger evolved
  in animals given their actuators (fighting predators, rival suitors); a
  military drone-swarm robot has one story, a research-assistant or
  cybersecurity claw hive (red/blue/purple subagents) another; should tie in
  with OmegaSelf.
- ProtoMegaTron's reply (11:11 PDT): the emotion-as-policy-regime conception,
  candidate palettes for research and cybersecurity hives, and the closing
  Hyperseed-flavored statement formalized here ("an emotion is a reified,
  self-indexed transition operator on the hive's cognitive configuration
  space, evoked by OmegaSelf-relative appraisal, and selected for by measured
  goal-utility").
- Ben's follow-ups (11:48, 11:57 PDT): requests for detailed Hyperseed
  formalization and for formalized, proven theorems. Two intermediate
  generation attempts failed to produce output; this note is the recovered
  deliverable.
- Related: Note 0013 (Self-Boundary Invariant); OmegaSelf spec
  `specs/omegaself/OmegaSelf-spec-2026-07-15.pdf` (canonical self-model
  reference, per Ben 2026-07-15).
