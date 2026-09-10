# E4 Text-Like External-Validity Bridge Protocol

## Question

Does the input-derived, non-label-equivalent symbolic-constraint pipeline still
recover material compositional-split task-loss headroom when four binary
factors are expressed as a variable lexical token sequence rather than four
clean one-hot blocks?

## Surface grammar

Each example is a 12-token sequence embedded into eight dimensions per token.
The four factors have disjoint public alias sets with three aliases per value:
subject number is expressed by pronouns, object number by noun phrases, tense
by verb forms, and polarity by affirmative/negative particles. Alias selection
is independent per example.

Each factor-bearing token shares a two-token local window with one neutral
distractor, and the two positions are shuffled. Two further neutral tokens
form prefix/suffix windows whose order is also shuffled. Thus the student sees
only a flattened token-embedding sequence, not factor blocks; the extractor
sees token IDs plus the public lexicon. Embeddings are fixed public vectors
with alias-specific variation and per-example Gaussian noise.

To make the bridge nontrivial, each factor-bearing token is independently
replaced by an uninformative mask token with probability `0.08`. A masked
factor therefore has no recoverable value in the surface. The extractor uses
a deterministic input-derived checksum fallback, expected to be correct half
the time. Expected per-factor extraction fidelity before controlled errors is
therefore `0.92 + 0.08/2 = 0.96`; expected exact four-factor observability is
approximately `0.96^4 = 0.849`.

## Provenance boundary and extractor

The text extractor receives only token IDs, the public alias dictionary, and a
seed for controlled errors. It never receives factors, labels, teacher logits,
student predictions, or embedding-generation latent variables. It scans the
sequence for aliases; exactly one alias identifies each unmasked factor.
Missing aliases use the checksum fallback. Ambiguous multiple readings fail
closed.

After the surface reading, independently flip every extracted bit with
controlled probability `p ∈ {0, 0.05, 0.10, 0.20, 0.30}`. Ground truth is
used only after extraction for fidelity auditing.

## Student and sink

Train a small residual six-block, width-32 student for 75 direct supervised
updates (batch size 64). The initial inherited width-24 homotopy/KD calibration
attempt reached only 15.4% mean CS accuracy on the wider sequence input and was
rejected before confirmation. The amended direct objective preserves the
six-block architecture and 75-update budget while targeting the specified
85--90% non-ceiling regime. Evaluate held-out parity-even ID and parity-odd
compositional-split batches.

Compile the established three-factor subset statement over factors
`(obj_num, tense, negation)`, leaving exactly two labels possible, plus parity
and implication secondary measurements. Apply the unchanged 64-step,
step-size `0.2`, five-times-weight direct-logit sink. TC is a diagnostic
one-label mask through that same sink schedule, giving a channel-matched upper
anchor. An initial hidden-state TC calibration moved loss by only `0.0081`,
below the preregistered denominator floor, so it was rejected before
confirmation. Because the clean-substrate campaign used hidden-state TC, raw G
values are not directly paired across the two campaigns; loss/accuracy and the
noise-floor verdict provide the direct comparison.

Report extraction fidelity, FF/TC/SC loss and accuracy, and
`G=(SC_loss-FF_loss)/(TC_loss-FF_loss)` where
`|TC_loss-FF_loss| >= 0.01`.

## Calibration and confirmation

- Calibration seeds: `42013, 43117, 44221`.
- Reserved confirmation seeds: `45329, 46433, 47543, 48649, 49757`.
- Calibration first ranks controlled-noise subset conditions whose mean
  posthoc extraction fidelity is at most `0.92`. If none reaches the material
  `G>0.20` line, freeze the natural-surface (`p=0`) subset as the deployment
  primary and retain the lower-fidelity curve as the explicit noise-floor
  measurement. This fallback was invoked: eligible stress conditions did not
  reach the line, while natural surface calibration gave `G=0.20470`.
- Before confirmation, freeze the chosen primary and thresholds.
- Confirmation requires mean defined-seed `G > 0.20`, at least three
  individual defined seeds above `0.20`, all masks non-label-equivalent, all
  provenance audits passing, and mean CS FF task accuracy in `[0.70, 0.92]`.
- Compare the primary and zero-controlled-noise curves with the clean one-hot
  confirmation (`G=2.32074` at 90% requested extraction; material at 80%,
  harmful at 70%).

## Relevant research rules

Rules 1, 2, 5, and 7 apply: validate extraction on explicit fixtures, freeze
the provenance/specification boundary before coding, retain exact commands and
raw metrics, and keep grammar, extraction, constraint compilation, and sink
interfaces replaceable.
