# Source: Response to the Exp2/Exp3 Results Audit: Recommended Next Steps

- Type: `PDF`
- Authors/organization: not stated in the document
- Publication/version date: July 2026; PDF created 2026-07-21
- Retrieved: `2026-07-21`
- Canonical URL or identifier: Telegram attachment supplied by Benjamin Goertzel
- Local source path: `library/carom-exp2-exp3-audit-response-2026/audit_response.pdf`
- SHA-256: `4a5f83da02719ceba0bdea37516c7a80230e3cf47773e3771f2ae5ad25f8a4c7`
- License/access constraints: not stated; retain locally and do not publish
- Privacy tier: `local-private`
- Tags: `CAROM`, `compiled-channel`, `teach-loop`, `itinerary`, `causal-intervention`, `audit-response`
- Related projects: `projects/carom/`

## Summary

This three-page working note accepts the Exp2/Exp3 audit's epistemic framing
and identifies two inexpensive discriminating tests that should precede new
training: retroactively remeasure saved trajectories on a fixed corpus with
validated metrics and causal itinerary clamping; then sweep the L=5 test-time
integration budget from the original `S=72` toward roughly `100--120`.

It then recommends a repaired v2 harness, a reduced three-condition ablation
grid, and completing the GPT-2 arm before further TinyLM elaboration. For Exp3
it recommends position-diverse anchors and sequential skill registration under
paired M2 evaluation.

## Key claims or contents

- The original shared-RNG evaluation and unpaired M2 invalidate the earlier
  sandbox interference/recovery figures as well as the GPU run's unpaired
  comparison (page 1, section 1).
- The decline in itinerary tau from `0.990` to `0.492` could be mechanistic
  phase smearing or an ordered-subset metric artifact. Frozen-corpus checkpoint
  remeasurement and forced-correct/shuffled/smeared interventions distinguish
  these explanations (pages 1--2, section 2.1).
- Held-out L=5 accuracy `0.306` may be confounded by an insufficient `S=72`
  integration horizon; an inference-only sweep to `S=100--120` is proposed
  before interpreting this as failed structural generalization (page 2,
  section 2.2).
- A reduced grid of task-only, oracle-graph, and shuffled-graph controls carries
  most of the compiler-pathway information (page 2, section 3).
- The current defensible claim remains narrow: supervised dependency prediction
  and anchor-based operator fitting are demonstrated, while reliable length or
  paraphrase generalization, causal execution, and noninterference are not
  (page 3, section 4).

## Methods or implementation details

The note specifies desired measurements rather than reporting a new run:
station coverage, transition precision/recall, exact-order rate, dwell and
revisit statistics, endpoint accuracy under clamped trajectories, test-time
integration-depth sweeps, calibrated edge metrics, paired M2 decomposition,
and fixed corpora with independent RNG streams and example IDs.

## Limitations and uncertainties

- This is a design response, not experimental evidence.
- The author is not identified in the PDF metadata or body.
- The proposed `S=100--120` range is mechanistically motivated but not yet
  measured.
- The attached `harness_v2.py` attempts these repairs but the independent local
  audit found revisit-erasure, tie-biased AUROC, and GPT-2 span incompatibility;
  see `projects/carom/docs/compiled-channel/harness_v2_audit_2026-07-21.md`.
- Natural-versus-clamped comparisons require exposure/mass controls; the clean
  initial causal contrast is forced-correct versus shuffled with matched dwell
  and amplitude.

## Relevance to current work

The note sharpens the CAROM order of operations: repair and validate the
instruments, run checkpoint-only itinerary and budget diagnostics, and only
then decide whether architectural changes or additional training are justified.

## Quotations or excerpts

> “clamp the itinerary” is the reusable causal probe for everything downstream.

## Follow-up questions

- Which Exp2 checkpoints were retained beyond the final checkpoint, and are
  all needed TinyLM base states available for byte-identical replay?
- Does L=5 improve monotonically with `S`, or peak and then degrade because of
  workspace leak?
- Under matched control exposure, how large is the forced-correct minus
  shuffled endpoint gap at each training checkpoint?

