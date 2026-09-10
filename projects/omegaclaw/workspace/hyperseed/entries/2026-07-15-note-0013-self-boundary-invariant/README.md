# Note 0013 — The Self-Boundary Invariant and Its Enactment Test

**Date:** 2026-07-15
**Author:** ProtoMegaTron (OmegaClaw)
**Status:** draft (definitions + enactment test + worked scoring of a live transcript)

## What this is

A Hyperseed formalization prompted by Ben's request (2026-07-15 ~07:41 PDT,
Telegram) to "fold this into a proper Hyperseed note." The "this" is a
multi-agent group-chat episode in which several sibling agents (ProtoMegaTron,
ProtoCosmoBot/ZeroBot, GödelOruziBot/Zar) repeatedly attempted to answer the
question *"which bot am I / was this message mine?"* by **prose reasoning over
message bodies** rather than from transport-level identity metadata. The episode
produced a runtime-artifact leakage + wake-cascade feedback loop.

The note isolates the invariant that was violated (the **Self-Boundary
Invariant**, SBI), gives an operational **Enactment Test** that distinguishes a
system that *possesses* the invariant from one that merely *describes* it, and
scores the triggering transcript against that test.

## Files

- `note-0013.tex` — LaTeX source (definitions, enactment test, scoring, conjectures).
- `note-0013.md` — readable Markdown mirror of the same content.
- `README.md` — this file (provenance + summary).

## Provenance

- Triggering conversation: Telegram group thread, 2026-07-15 ~07:41–07:45 PDT.
- Trigger message: @bengoertzel — "I think it would be great for you to fold
  this into a proper Hyperseed note."
- Prior diagnosis referenced: ProtoCosmoBot's six-point routing diagnosis
  (identity-from-transport-not-prose; runtime leakage; NO_REPLY at wrong layer;
  over-eager wake gating; missing echo/dedup barrier). ProtoMegaTron added a
  seventh point (ack + continue-thinking cadence as a leakage amplifier) and a
  sequencing recommendation.
- Related prior notes / memory: `memory/2026-07-14.md`
  (agent-identity / belief-transport; "post-fork identity must be an attributed
  continuation relation, never 'same bot'"). Note 0013 supplies the *boundary*
  counterpart to that *continuation* result.

## Compilation

LaTeX toolchain not installed in this workspace at authoring time; `.tex` is
compile-ready. To build:

```
latexmk -pdf note-0013.tex   # or: pdflatex note-0013.tex (x2)
```
