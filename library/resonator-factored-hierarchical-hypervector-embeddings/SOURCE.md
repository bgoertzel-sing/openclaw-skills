# Source: Resonator-Factored Hierarchical Hypervector Embeddings for Compact Structured Memory and Faster Factor-Aligned Computation

- Type: `PDF`
- Authors/organization: Ben Goertzel
- Publication/version date: 2026-07-25
- Retrieved: `2026-07-25`
- Canonical URL or identifier: Not supplied; author-provided PDF
- Local source path: `library/resonator-factored-hierarchical-hypervector-embeddings/paper.pdf`
- Extracted text: `library/resonator-factored-hierarchical-hypervector-embeddings/paper.txt`
- SHA-256: `8643b4aa4abd0bf068705a85c6399803c496a76eb61131e0c1d26d85402ef6f7`
- Companion code: `library/resonator-factored-hierarchical-hypervector-embeddings/hdc_musicgen_experiments.py`
- Companion-code SHA-256: `3521275a99a8256970a6c091fcdd082839670bd3d9613ee980f39cec4ad0683b`
- Experimental runbook: `library/resonator-factored-hierarchical-hypervector-embeddings/AGENT_RUNBOOK_hdc_musicgen.md`
- Runbook SHA-256: `e60b72c268f93f4603912df44d33873a1f73347a32baa473742768ee1a13c00c`
- License/access constraints: Copyright/license not specified; local research use
- Privacy tier: `local-private`
- Tags: `HDC`, `VSA`, `resonator networks`, `factorization`, `structured memory`, `HMH`, `PRIMUS`, `HBCML`, `ColBaC`, `episodic memory`
- Related projects: Project linkage not yet established

## Summary

The paper develops query-limited hierarchical hypervector codes for factor graphs and learned latent structures. It separates task error into an upstream factorization defect and a downstream HDC coding error, then gives coherence-aware cleanup bounds and a basin-conditional resonator guarantee. The practical thesis is deliberately conditional: compact HDC memory is useful when upstream representations expose reusable, role-stable, bounded-load factors and the intended query family is limited.

The paper also reverses the capacity argument into a learning objective: train upstream representations to reduce effective local load, codebook confusability/coherence, recomposition error, role instability, residual predictive information, and intervention nonlocality. Applications are proposed for resonant HMH/PRIMUS episodic memory and for HBCML/ColBaC causal columns.

## Key claims or contents

- Fixed-family path-query reliability depends on local load, subtree-codebook coherence and size, query depth/count, and dimension, rather than directly on raw object size (Theorem 1, pp. 14–15).
- Near-duplicate subtree dictionaries change the familiar `D ≳ k log M` requirement to approximately `D ≳ k^(3/2) log M` for bipolar sign codes and `D ≳ k^2 log M` for linear/phasor codes (Remark 2, pp. 13–14).
- Resonator decoding has slot-wise linear rather than product-space search cost only after basin entry; cold-start operational capacity remains polynomial and restart/beam/warm-start costs must be charged (Theorem 3, Corollary 1, Remark 5, pp. 15–16).
- Expected task loss is bounded by factorization defect plus bounded decoding-failure loss; increasing HDC dimension cannot remove an upstream factorization defect (Theorem 4, pp. 16–17).
- Ordered roles or argument-position permutations are necessary to preserve directed relations and temporal order under commutative binding (Sections 2, 8.2, and 11.6/11.8).
- Real-data studies find effective subtree dictionaries much smaller than formal product spaces but strongly coherent; noisy encoder/dictionary mismatch can make cleanup harmful below the coherence-aware dimension budget (Sections 11.7–11.8, pp. 38–41).
- The streaming-audio study establishes matched-interface parity and feasible warm-started resonator decoding at toy scale, but explicitly does not establish an end-to-end generation compute advantage (Section 11.9, pp. 41–43).

## Methods or implementation details

- Theory uses normalized random hypervectors, isometric binding, ordered roles/permutations, explicit subtree dictionaries, coherence-aware cleanup, and a supported-query model.
- Numerical implementation uses bipolar MAP vectors, Hadamard binding, integer-sum bundling, deterministic sign normalization, cyclic-shift permutation, matrix-vector hard cleanup, and project-onto-codebook resonator updates (Section 11.1, pp. 35–36).
- Synthetic tests cover single-step cleanup, hierarchical descent, near-duplicate scaling, cold/warm resonator decoding, and directed relations (Sections 11.2–11.6).
- Real-data studies use scikit-learn handwritten digits, the Free Spoken Digit Dataset, and a toy three-stage residual-quantized spoken-digit codec (Sections 11.7–11.9).

## Limitations and uncertainties

- The numerical studies are explicitly toy-scale and are presented as falsification/calibration rather than benchmarks.
- The resonator theorem is conditional on measurable margin and basin entry; it is not a global convergence theorem.
- Effective subtree dictionaries can have poor out-of-sample coverage and pervasive near-duplicates.
- HDC theory controls coding error, not the task-specific factorization defect.
- The long-context compression/compute claim is not tested with a competent long-form generative model.
- The supplied PDF does not provide a canonical URL, software archive/commit, dataset split artifact, or license statement, so independent reproduction provenance is incomplete.

## Relevance to current work

The paper supplies a concrete diagnostic vocabulary for deciding whether a learned modular or columnar representation is suitable for HDC caching: local load, coherence, cleanup margin, role consistency, residual defect, and intervention locality. The ColBaC/HBCML and resonant HMH/PRIMUS sections may connect to existing causal modularity and associative-memory projects once the intended active project is identified.

## Quotations or excerpts

“The HDC theory controls the second term through dimension, margin, coherence, and local load. It does not control the first.” (Introduction, p. 5)

## Follow-up questions

- Which active project should own the implementation and experimental follow-up?
- Is there a companion code archive for the Section 11 experiments?
- Should the next pass prioritize mathematical review, reproduction, or a minimal implementation of the HDC-guided factorization losses?

## Companion code audit — 2026-07-25

The supplied `hdc_musicgen_experiments.py` parses successfully under the local Python interpreter. It stages tokenization, context-value measurement, matched output-head probes, resonator feasibility, and an HDC history adapter. It has not been executed against AudioCraft or a GPU environment.

Pre-execution issues requiring correction or explicit validation:

- Stage B hooks delay-pattern LM hidden states but pairs them directly with ordinary next-frame codebook targets (`extract_hidden_and_targets`, lines 264–296). MusicGen's inter-codebook delay pattern makes that alignment a consequential assumption; it needs an index-level test against `compute_predictions` masks/targets before results are interpretable.
- Stage B promises an NLL proxy but records only per-codebook and exact-frame accuracy (lines 311–369).
- CUDA timings omit synchronization around the measured regions (lines 320–323 and 348–353), so reported wall-clock decode times can be invalid.
- Stage D samples training and evaluation windows from the same undivided track list (lines 470–516). This is not a held-out generalization test and permits track-level leakage.
- Stage D injects adapter outputs through the text-conditioning interface and infers `d_model` from version-sensitive internals (lines 463–490); this must be smoke-tested against the pinned AudioCraft 1.3.0 implementation.
- Stage A's 40–60 second and “full” contexts may exceed the pretrained model's effective context regime or implementation limit; the actual LM positional/streaming behavior must be inspected rather than inferred from successful execution.
- The code hard-codes `K=4`, cardinality `2048`, and frame rate `50`; these should be asserted against the loaded compression model.
- No dataset split manifest, dependency lock, hardware record, software commit, seeds beyond global defaults, confidence intervals, or per-example outputs are currently recorded.

## Runbook cross-check — 2026-07-25

The supplied runbook adds useful stage ordering, data-volume gates, sanity bands, permitted knobs, stop conditions, and a required result format. It does not resolve the code-level blockers above. Four protocol points should be corrected before freezing a run:

- Its Stage C statements conflict. It correctly says cold-start failure is expected at the approximately `2048^4` product space, but later says that at zero noise both warm and cold “must” recover approximately 1.0. Exact evidence does not remove a resonator's basin-entry problem, so this is not a valid bookkeeping test for cold-start convergence.
- Its Stage D gate says the adapter “can at worst be neutral.” On held-out data a learned adapter can legitimately worsen NLL; degradation is evidence against the adapter or of overfitting, not automatically training divergence. The current script's same-track evaluation makes this distinction impossible.
- The runbook treats Stage B's low probe accuracy mainly as a hook-wiring problem, but the more specific risk is delay-pattern target misalignment. A chance-beating probe is not sufficient to establish correct aligned-frame targets.
- Stage A's “full context” baseline and 40–60 second settings must first be shown to be within MusicGen's usable context behavior. Successful execution alone would not establish that older tokens are causally available to the prediction.

Decision: do not provision paid compute from this runbook as written. First repair and locally validate alignment, held-out splitting, timing, model/codec assertions, and the protocol contradictions; then freeze a new commit and prepare a costed GPU proposal.
