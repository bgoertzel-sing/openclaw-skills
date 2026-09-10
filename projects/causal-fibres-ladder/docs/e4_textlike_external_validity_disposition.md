# E4 Text-Like External-Validity Disposition

## Verdict

The symbolic constraint pipeline survives the text-like external-validity
bridge under the frozen natural-surface primary. Five disjoint confirmation
seeds pass all five gates:

- mean CS task-loss `G=0.30387 ± 0.08379`, above `0.20`;
- all `5/5` individual G values exceed `0.20`;
- CS accuracy improves from `81.56%` FF to `82.50%` SC;
- mean factor extraction fidelity is `96.09%`;
- all constraints remain non-label-equivalent and all provenance audits pass;
- mean FF accuracy `81.56%` is inside the frozen `[70%,92%]` non-ceiling
  interval.

This confirms Stage-4 inversion beyond exposed one-hot factor blocks on a
controlled compositional text-like surface. It is still not evidence for
free-form natural language.

The source-family result is not universal: at zero added error, parity reached
`G=0.19075` (just below the material line) and implication reached `0.05054`.
The accepted claim is specifically the frozen three-factor subset pipeline.

## Surface and provenance

Each example is a 12-token, eight-dimensional embedding sequence. Four
factor-bearing aliases are selected from three synonyms per value, paired with
neutral distractors, shuffled inside local windows, and perturbed by embedding
noise. Eight percent of factor aliases are replaced by an uninformative blur
token. The extractor receives token IDs, the public alias dictionary, and a
controlled-error seed only; factors and labels are posthoc audit inputs.

The surface ambiguity produced a `7.58%` fallback rate and `96.09%` clean
extraction fidelity on confirmation, matching the expected 96%.

## Noise floor

| Added error | Realized extraction | Mean G | CS accuracy |
|---:|---:|---:|---:|
| 0% | 96.09% | 0.30387 | 82.50% |
| 5% | 91.91% | 0.25694 | 82.19% |
| 10% | 88.44% | 0.20826 | 82.34% |
| 20% | 77.38% | 0.22517 | 82.03% |
| 30% | 68.32% | 0.15250 | 81.72% |

Mean material recovery survives through 20% added errors and fails at 30%.
The observed noise floor is therefore between `77.38%` and `68.32%`
factor-extraction fidelity. The small nonmonotonicity between 10% and 20%
reflects finite samples and differing deterministic error draws; it does not
support a claim that more noise helps.

## Comparison with the one-hot substrate

The prior one-hot input-derived primary reported `G=2.32074` at about 90%
extraction, FF/SC accuracy `94.22%/96.09%`, and a noise floor between 80% and
70%. The text bridge reports much smaller normalized recovery and lower
absolute accuracy, but remains material and robust. Its observed fidelity
floor is similarly in the high-60s-to-high-70s range.

Raw G magnitudes are not directly comparable: the text bridge uses a
channel-matched label-equivalent direct-logit TC anchor because the inherited
hidden-state TC moved loss by only `0.0081`, below the preregistered denominator
floor. The appropriate cross-campaign conclusion is qualitative: surface
complexity sharply reduces margin but does not reverse the deployment verdict.

## Calibration corrections retained

Two negative calibration records are part of the evidence:

1. The inherited width-24 homotopy/KD student reached only `15.36%` mean CS
   accuracy and was rejected.
2. A 75-update width-32 supervised student reached `85.94%`, but hidden-state
   TC left G undefined. Switching only the diagnostic anchor to the same
   direct-logit channel produced defined calibration denominators.

Thresholds and the natural-surface primary were then frozen and committed at
`154e5cfb604ffeeca314b22429e34d26b490a61c` before confirmation.

## Evidence

- Protocol: `docs/e4_textlike_external_validity_protocol.md`.
- Final calibration:
  `experiments/20260724T234609Z-e4-textlike-calibration-channel-matched/`.
- Confirmation:
  `experiments/20260724T234938Z-e4-textlike-confirmation/`.
- Confirmation aggregate SHA-256:
  `975df588d0b03e4f077f1dd8015dd9ae013998b7a74ebbb41250d542c12f4681`.
- Focused checks: `18 passed`.
- Full repository suite: `212 passed in 18.98s`.
- Local implementation commit before final record updates: `154e5cf`.
