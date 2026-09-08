# Source: Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation

- Type: `paper | PDF`
- Authors/organization: Alexi Gladstone and Heng Ji (UIUC); Yilun Du (Harvard)
- Publication/version date: arXiv v1, 2026-07-29
- Retrieved: `2026-08-01`
- Canonical URL or identifier: arXiv `2607.27372v1`; https://arxiv.org/abs/2607.27372
- Local source path: `library/explorative-modeling-gladstone-ji-du-2026/2607.27372v1.pdf`
- SHA-256: `5296b62e821cf2a1420f311d11d825dd782b628546c78c8c378a6cab72f02419`
- License/access constraints: public arXiv preprint; copyright remains with authors
- Privacy tier: `public`
- Tags: explorative-modeling, best-of-k, generative-modeling, mode-coverage, diffusion, language-modeling, scaling
- Related projects: `relaleap`

## Summary

The paper frames generative modeling as choosing whether to factor generation or
training. Its Explorative Modeling (XM) factors training: generate or compare K
candidate pairings and backpropagate through the closest match. The authors argue
that K supplies a third scaling axis, “generative expressivity,” complementary to
parameters and data. They test XM with flow/diffusion, Jumpy models, masked
diffusion language models, behavior cloning, and goal-conditioned world models.

## Key claims or contents

- Forward XM minimizes the best reconstruction loss among K generated candidates;
  Reverse XM compares one generation with K data targets (Section 3, pp. 6–8).
- Reported scaling gains include 4.1x FLOP efficiency, 6.2x sample efficiency,
  47% parameter efficiency, and unguided ImageNet FID 1.43 (Abstract; Section 4).
- Exploration reportedly improves image FID, video FVD, and the perplexity–entropy
  frontier of masked diffusion language models (Figures 7–8, pp. 10–11).
- End-to-end XM policies/world models reportedly match diffusion baselines using
  16–256x fewer inference steps (Tables 2–3, pp. 14–15).

## Methods or implementation details

Forward XM samples K generations for a target and trains only on the closest.
Reverse XM generates once, searches K data targets, and trains against the closest.
The main experiments use Forward XM. Hybrid experiments add exploration to
existing recipes without XM-specific hyperparameter tuning. The theoretical
analysis interprets smooth Forward XM as maximum likelihood over a K-candidate
mixture and Reverse XM as reverse-KL-like but collapse-prone without an entropy or
coverage term (Appendix F).

## Limitations and uncertainties

- This is a v1 preprint under review; headline scaling claims are author-reported
  and have not been independently reproduced here.
- Forward XM costs roughly K candidate generations and becomes expensive for
  highly multimodal domains; Reverse XM is cheaper but can mode-collapse.
- Autoregressive language models were substantially harder to improve than
  continuous or masked-diffusion models (Section 7, pp. 16–17).
- Some highest-resolution video experiments were constrained by available compute,
  and the end-to-end control studies received limited tuning (Sections 4.2, 7,
  Appendix D).

## Relevance to current work

XM is conceptually adjacent to predictive coding because both spend training or
inference compute on an inner search/settling process, but the mechanisms differ.
XM selects a best discrete candidate/coupling; ePC iteratively settles internal
states under a predictive-coding objective. A useful RelaLeap experiment would
cross XM exploration K with KD/ePC settling depth T under fixed total compute and
measure not only distillation loss but mode coverage, representation collapse,
effective rank, and OOD behavior. The current ePC robustness run did none of this
and therefore neither supports nor contradicts the XM claims.

## Quotations or excerpts

“At each training step, the model explores K possible matches between what it
generates and the data, and trains on the closest.” (Abstract)

## Follow-up questions

- Does best-of-K coupling selection complement or merely duplicate ePC settling?
- Under fixed FLOPs, how should compute be allocated between exploration K,
  settling depth T, parameter count, and data?
- Can Reverse XM’s coverage constraint be expressed as a predictive-coding energy
  or implemented by a multiscale PC cap?
