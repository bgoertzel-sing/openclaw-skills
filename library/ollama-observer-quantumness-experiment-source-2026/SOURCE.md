# Source: Local Ollama test of observer-relative operator linguistics

- Type: `archive`
- Authors/organization: supplied by Benjamin Goertzel; package authorship not stated
- Publication/version date: not stated
- Retrieved: `2026-08-13`
- Canonical URL or identifier: Telegram source message `4963` in Protobot-updates
- Local source path: `library/ollama-observer-quantumness-experiment-source-2026/original.zip`
- SHA-256: `2f01eecef140f6b8d3e05c34f4353b8885c1b40d398c62f8f8974d970df4551a`
- License/access constraints: no license stated; retain locally and confirm before redistribution
- Privacy tier: `local-private`
- Tags: `ollama`, `observer-relative-quantumness`, `operator-linguistics`, `contextuality-by-default`, `compression`
- Related projects: `omegaclaw`; conceptually related to `relaleap`

## Summary

Source package underlying the local black-box Ollama experiment already present at
`projects/omegaclaw/workspace/experiments/ollama_observer_quantumness_experiment`.
It tests a conservative evidential ladder: ambiguity-sensitive choice entropy,
sequential order effects, cyclic-4 Contextuality-by-Default after direct influences,
and optional held-out operator-compression comparisons against classical and real-POVM controls.

## Key claims or contents

- The package explicitly does not claim that the model or language is physically quantum (`README.md`, opening section).
- A positive observer-relative result requires held-out complex-POVM advantage over nonnegative, signed-real, same-dimension real-POVM, and matched-or-larger-budget real-POVM baselines (`README.md`, section 7; `CODING_AGENT_SPEC.md`, Q4).
- The current black-box probe cannot test hidden-state complex resonances (`README.md`, opening section; `CODING_AGENT_SPEC.md`, sections 1-2).

## Methods or implementation details

The archive contains Python source, tests, task definitions, documentation, dependency manifests, and an internal `CHECKSUMS.sha256`. On ingestion, every entry covered by that checksum manifest verified successfully. No code from the archive was executed.

The source snapshot was compared with the existing working copy. The existing copy contains later run artifacts, a background-run script, environment/cache material, and changes in `design.py`, `metrics.py`, `tasks.py`, and the prior-pilot summary. The supplied archive was therefore preserved as source provenance and did not overwrite the evolved experiment tree.

## Limitations and uncertainties

- Package authorship, creation date, version identifier, license, and canonical public location are unstated.
- The archive contains no run directories or empirical result artifacts.
- The compression fit is nonconvex and is described as an approximate model-selection comparison, not a PSD-rank proof.
- Exact relationships between the supplied snapshot and later local code changes require a targeted source diff if scientifically relevant.

## Relevance to current work

This provides the missing immutable source snapshot for interpreting and reproducing the existing local Ollama observer-quantumness experiment without treating the evolved working directory as the original input.

## Quotations or excerpts

None retained; see the preserved source.

## Follow-up questions

- What date/version and author attribution should be attached to this package?
- Should later local modifications be audited against this supplied baseline before further interpretation of the experiment results?
