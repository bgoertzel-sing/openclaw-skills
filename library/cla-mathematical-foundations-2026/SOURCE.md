# Source: Mathematical Foundations for the Upgraded Chaos Language Algorithm

- Type: `PDF`
- Authors/organization: Working notes for Ben Goertzel, prepared with Claude (Anthropic)
- Publication/version date: 2026-07-23
- Retrieved: `2026-07-23`
- Canonical URL or identifier: supplied by Ben Goertzel in the Protobots Telegram group
- Local source path: `library/cla-mathematical-foundations-2026/cla_math_foundations_ascii_1.pdf`
- SHA-256: `6969a095f1139d52fb64afa564cca7acbe40f2f79bf0f89cb4d4769fa385ebcb`
- License/access constraints: supplied for project use; no explicit license stated
- Privacy tier: `local-private`
- Tags: `CLA`, `MDL`, `prequential coding`, `CSSR`, `epsilon-machine`, `substitution systems`, `quantale`, `Hyperseed`
- Related projects: `chaos-language-algorithm`, `omegasim`, `hyperseed-formalizations`

## Summary

The notes give a mathematical interpretation of the July 2026 adaptive-coding
upgrade. Their central reframing is that chunk-grammar CLA should detect
hierarchical generativity, not chaos in general. Positive-entropy sofic or
hyperbolic symbolic dynamics should favor causal-state, CTW, or adaptive
Markov coding; substitution-structured zero-entropy regimes are proposed as
the domain where hierarchical grammar codes can win decisively.

## Key claims or contents

- The invariance lemma states that invertible grammar rewriting cannot change
  source entropy; gains can arise only from redundancy reduction minus
  model/definition cost (Section 2, pp. 2--3).
- A recurrence-time argument places exact-repeat chunk grammars in an LZ-like
  redundancy class on positive-entropy stationary ergodic sources, while a
  finite-state causal coder can have logarithmic redundancy on a UHMM/sofic
  source (Section 3, pp. 3--4).
- A separation proposition claims linearly recurrent substitution words admit
  polylogarithmic-size grammar codes while finite-order Markov, CTW, and LZ
  controls remain nearly linear up to logarithmic factors (Section 3, p. 4).
- The adaptive two-part scorer is interpreted as MAP structure selection with
  Jeffreys-prior KT mixtures; the inline scorer has a source-adaptive implicit
  prior (Sections 4--5, pp. 4--6).
- Category acceptance is framed as a consistent MDL test of contextual
  exchangeability (Section 6, p. 6).
- The epsilon-machine is presented as the asymptotically MDL-minimal unifilar
  presentation of a sofic source; accepted CLA categories correspond to
  kernel classes of the alphabet action on causal states (Sections 7--8,
  pp. 6--8).
- Two new predictions are proposed: CLA should beat all controls at the
  Feigenbaum accumulation point and on Sturmian codings, while causal-state
  coding should beat chunk-CLA on fresh hyperbolic-regime fixtures (Section 9,
  p. 8).
- Mixed MDL second differences define edit synergy and yield a proposed
  ranking statistic for composite category-plus-chunk moves (Section 10,
  pp. 8--10).

## Methods or implementation details

- Add an `LZ77SLPInitializer` alongside Re-Pair in milestone M-D to provide a
  worst-case-guaranteed grammar initialization baseline.
- Add fresh E5b fixtures for logistic-map Feigenbaum and Sturmian regimes,
  evaluated over lengths 2^12, 2^14, and 2^16.
- Rank composite proposals using an estimated mixed second difference, but
  retain the exact official scorer as the acceptance authority and record
  estimated-versus-realized residuals in the ledger.
- Treat two-part/inline scorer disagreement beyond the stated additive slack
  as a bug diagnostic.

## Limitations and uncertainties

- Several project-specific results are proof sketches rather than fully
  formal proofs.
- The recurrence and separation claims rely on source-class assumptions that
  must be checked carefully for finite symbolized dynamical fixtures.
- The statement that fully developed Lorenz-like dynamics are sofic or well
  approximated by sofic processes depends on the chosen symbolizer and does
  not follow automatically from observing a continuous chaotic flow.
- The proposed E5b predictions and LZ77-SLP initializer are amendments to the
  governing programme, not yet frozen decisions or measured results.

## Relevance to current work

The paper sharpens E5/E7 interpretation, supplies a principled reason for a
CSSR win, and suggests two bounded additions: an LZ77-SLP initializer in M-D
and an E5b substitution-vs-sofic discrimination battery. Existing milestones
M-A through M-C and their acceptance criteria remain unchanged.

## Quotations or excerpts

“The algorithm's discriminating power is not ‘chaos detection’ but detection
of hierarchical generativity.” (Section 3)

## Follow-up questions

- Which propositions should be independently checked before being cited as
  theorem-level constraints in the frozen evaluation programme?
- Should E5b be inserted before E7, or run as a parallel scientific
  characterization after the original E3/E4 gates pass?
- What finite-sample operationalization best distinguishes stable causal-state
  count from LZ-like chunk-rule growth?
