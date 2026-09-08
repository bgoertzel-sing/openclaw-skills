# Source: Why the RelaLeap ePC Distillation Programme Failed, and a Redesigned Path to Cap-Ready ePC Transformers

- Type: `PDF`
- Authors/organization: author not stated; prepared for Benjamin Goertzel and
  the RelaLeap research-agent workflow
- Publication/version date: `2026-08-04`
- Retrieved: `2026-08-04`
- Canonical URL or identifier: user-supplied Telegram document; no public
  canonical identifier supplied
- Local source path: `library/relaleap-epc-diagnosis-20260804/diagnosis.pdf`
- SHA-256: `39d8a7a0625284aedeb500ef2d97f59e752d6eb51922e437f8542b19999be6ff`
- License/access constraints: unknown; supplied privately by Ben, do not
  republish without confirmation
- Privacy tier: `local-private`
- Tags: `RelaLeap`, `ePC`, `predictive coding`, `error optimization`, `sPC`,
  `instrument audit`, `cap readiness`, `homotopy conversion`
- Related projects: `projects/relaleap`, `projects/causal-fibres-ladder`

## Summary

This 14-page diagnostic argues that the July--August RelaLeap programme did
not test the intended error-parameterized predictive-coding method and that
the final multi-regime fixture showed instrument-failure signatures. It
proposes replacing the existing programme with four stages: M0 analytic
equivalence gates, C1 homotopy conversion of a competent transformer, C2
pre-registered cap-readiness measures, and C3 a matched-cap falsifier.

The document is a technical critique and proposed protocol, not yet an audited
project decision. Its strongest claims require direct comparison with
Goemaere et al. arXiv:2505.20137, the authors' reference implementation, the
RelaLeap source, and the parallel adjoint-field experiment records.

## Key claims or contents

1. **Algorithm identity:** the RelaLeap code optimizes hidden states `z`, hence
   is state-based PC, whereas the cited EO/ePC method optimizes prediction
   errors `epsilon`; therefore the programme allegedly tested the wrong
   algorithm (Section 2, pp. 3--4).
2. **Instrument defect:** with vocabulary 64, uniform per-token NLL is
   `ln(64) = 4.159`; final T=1 NLLs `6.76--11.92` are worse than chance and
   allegedly indicate train/eval correspondence or aggregation-unit defects,
   not inadequate capacity (Section 3, pp. 4--5).
3. **Weak invariant:** monotone energy follows from the backtracking acceptance
   rule and does not establish fixed-point convergence. The report calls for
   gradient-residual and Jacobian-spectral-radius certificates (Section 4,
   p. 5; Appendix MG-3/MG-4).
4. **Objective mismatch:** PC/BP equilibrium equivalence makes BP loss parity a
   constraint rather than the scientific prize. The intended prize should be
   measured cap-readiness and matched-cap performance (Section 5, pp. 5--6).
5. **Redesigned programme:** M0 deep-linear analytic gates; C1 conversion by
   output-precision homotopy; C2 conditioning, injection-response,
   error-informativeness, additivity, and rank metrics; C3 identical caps on
   quality-matched ePC and BP bases (Sections 6--8, pp. 6--8).
6. **Agent requirements:** comprehension obligations, porting the reference
   EO implementation, mandatory chance/oracle baselines, metric units,
   analytic positive controls, and a named historical-failure regression suite
   (Appendix A, pp. 10--14).

## Methods or implementation details

- The critique compares the two RelaLeap reports and public bundle against
  arXiv:2505.20137 and cites parallel causal-fibres/adjoint-field results.
- Its proposed M0 uses float64 linear networks at depths 2/6/12/24 and widths
  16/64, requiring per-layer PC-vs-BP gradient relative error at most `1e-6`
  at convergence for small output precision.
- Proposed mechanism gates include immediate deep error-variable response,
  convergence residual `rho_T <= 1e-2`, settling-map spectral radius below 1,
  teacher-write integrity, oracle eval/train correspondence, depth-neutral
  energy shares, and deterministic replay.
- The proposed C1 path starts from a functionally identical pretrained model,
  anneals output precision over at least eight log-spaced rungs, and stops at a
  pre-registered quality or conditioning boundary.

## Limitations and uncertainties

- The claim that the cited EO/ePC paper's defining variable is `epsilon` and
  that the existing code cannot be considered an equivalent
  reparameterization has not yet been independently checked against the paper
  and reference code.
- The chance-baseline arithmetic assumes the reported metric is per-token mean
  NLL. The critique itself correctly notes that if the implementation reports
  a summed or differently aggregated quantity, `ln(64)` is not the comparable
  baseline; the actual aggregation must be inspected.
- Worse-than-uniform validation loss can occur without an evaluation bug when
  a trained model is confidently wrong under distribution shift. The tiny
  deterministic lookup fixture makes an instrument defect plausible, but it
  is not established by arithmetic alone.
- “Monotone energy is vacuous” is rhetorically stronger than warranted:
  monotonicity validates the line-search invariant, but indeed does not
  validate convergence or method identity.
- The asserted contradiction with the parallel adjoint-field track depends on
  whether those experiments used comparable models, objectives,
  parameterizations, and measurements.
- The prescribed thresholds (`1e-6`, `rho <= 1e-2`, factor-of-four energy
  balance, etc.) are proposals and require prospective justification before
  adoption.

## Relevance to current work

The document identifies a potentially programme-changing issue: if the current
implementation is sPC rather than the intended error-optimized method, the
published negative results are bounded to that legacy implementation and the
successor should begin with method-identity and analytic-equivalence gates.
It also points to a concrete immediate audit that is local and inexpensive:
verify method identity, compute exact chance/untrained/oracle baselines through
the actual r5 evaluator, and measure convergence residuals before authorizing
new training.

## Quotations or excerpts

> “Procedural gates certify that whatever happened, happened reproducibly.
> Mechanistic gates certify that the thing that happened is the thing you
> meant to study.” (Section 9, p. 8)

## Follow-up questions

1. Does the legacy RelaLeap relaxation optimize state variables, and is it
   mathematically or computationally equivalent to the EO reference method?
2. What exact units and reduction operations produce each r5 NLL, and what do
   uniform, untrained, teacher-oracle, and memorizing-oracle models score
   through the same evaluator?
3. Did any prior run record final gradient residual or fixed-point conditioning,
   or only monotone energy?
4. Is the causal-fibres adjoint-field track comparable enough to adjudicate the
   alleged credit-location contradiction?
5. Which proposed M0/MG thresholds should be frozen prospectively after
   reproducing the EO reference implementation?
