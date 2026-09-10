# CLA Frozen Held-Out MDL Benchmark — Preregistration v1

**Frozen:** 2026-07-13 PDT  
**Protocol status:** preregistered before implementation or benchmark execution  
**Reference repository state:** `projects/chaos-language-algorithm/repos/chaoslang`, branch `agent/hd-embedding-cla`, commit `4423f8f9c75b8b59a5ba700f03881216bfbb56d9`  
**Working-tree note:** the reference checkout had one unrelated untracked design document, `docs/cla_python_library_interface_design.tex`; it is not an input to this benchmark.

## Question

Can a CLA grammar learned on a fixed trajectory prefix provide a shorter total description of untouched suffixes than literal, unigram, Markov, and current-proxy controls, while preserving exact reconstruction and deterministic replay?

This benchmark tests frozen predictive coding. It is not a prequential-adaptation benchmark and does not test live PeTTa/Hyperon integration.

## Fixed ordering

1. Verify canonical persistence and deterministic edit-log replay.
2. Freeze the learned model and score one untouched suffix per trajectory without refitting.
3. Compare all methods under identical temporal splits and accounting rules.
4. Only after the frozen benchmark is reported may blockwise prequential adaptation be tested.

## Required fixture declaration before execution

The run record must be created before execution and freeze:

- trajectory/data identifiers and hashes;
- symbolization method and all fitted parameters;
- trajectory seeds;
- prefix/suffix boundary for every trajectory;
- model hyperparameters and random seeds;
- baseline orders and smoothing parameters;
- exact commands and repository commit.

No trajectory, seed, split, baseline, or stopping-rule changes may be made after inspecting benchmark outputs. Any correction requires a versioned amendment that states whether prior outputs were observed.

## Determinism and reconstruction gate

For each trajectory:

1. Fit only on the declared prefix.
2. Canonically serialize the complete learned state and edit log.
3. Load/replay independently twice from the recorded initial symbols.
4. Require byte-identical canonical state, canonical fact projection, reconstruction, and deterministic continuation edits.
5. Require exact reconstruction of every encoded prefix and suffix symbol.

Volatile transport metadata, wall-clock timestamps, and filesystem paths are excluded from canonical bytes and must be recorded separately. Any mismatch is a benchmark failure, not a warning.

## Frozen held-out evaluation

After prefix fitting, all learned parameters and grammar edits are frozen. Each method scores the declared untouched suffix without refitting, suffix-informed proposal generation, state mutation, or adaptive smoothing.

Report for each method and trajectory:

- model/state transmission bits;
- suffix data bits (negative log2 probability or the method's explicitly specified decodable code length);
- total bits = model/state bits + suffix data bits;
- bits per suffix symbol;
- reconstruction status;
- canonical state/output hashes.

The implementation must use one documented, deterministic, prefix-decodable accounting convention for model/state transmission across CLA and all baselines. If canonical serialized byte length is used as the initial convention, charge `8 × canonical byte count` to every method and serialize equivalent symbol dictionaries and parameters; do not charge only CLA.

## Baselines

At minimum:

1. Literal coding.
2. Prefix-trained unigram model.
3. Prefix-trained Markov model(s) at preregistered order(s).
4. The current CLA proxy/control, clearly labeled as a proxy rather than calibrated predictive CLA coding.

All methods receive identical prefix information and score identical suffix symbols. Baseline selection is fixed before outputs are inspected. The strongest baseline is the one with the lowest aggregate total held-out codelength among these preregistered controls.

## Aggregate statistic and pass criterion

Aggregate by summing total held-out bits across all preregistered trajectories; also report every trajectory separately.

CLA passes only if:

1. deterministic serialization/replay and exact reconstruction pass for every trajectory;
2. CLA aggregate total held-out codelength is strictly lower than the strongest preregistered baseline; and
3. no fallback, skipped validation, non-finite score, or suffix-informed fit occurred.

There is no post-hoc exclusion of losing trajectories and no claim of success from training-fit MDL, proxy compression, or a subset of seeds.

## Failure interpretation and next branch

If CLA does not pass, do not tune against the held-out suffixes. Run a separate, minimal, preregistered joint chunk/category fixture to distinguish:

- inadequate or unfair predictive coding/accounting; from
- greedy-search blindness to a jointly beneficial chunk/category move.

The diagnostic fixture is not a retroactive rescue of the failed benchmark and must be reported separately.

## Deferred secondary benchmark

Blockwise prequential adaptation is secondary. It must report update/transmission costs and use temporal blocks fixed before execution. Its results may not replace or be conflated with the frozen held-out result.

## Pre-run accounting clarification 1 — 2026-07-13

This clarification was frozen after implementation review but before any external benchmark output was produced. It resolves the accounting choice left conditional above; it does not change the pass criterion.

- Fitted model transmission is `8 ×` the byte length of a versioned canonical UTF-8 JSON model object (`sort_keys=True`, compact separators, Unicode preserved).
- The CLA object contains only the decodable grammar, frozen top-level entry counts, frozen category-member counts, escape/literal conventions, parsing convention, schema, and version. It excludes the training corpus, fitted parse, score, history, and edit log.
- Unigram and Markov objects use the same canonical JSON convention and contain all fitted parameters needed by a decoder. Markov includes the frozen initial suffix context.
- Every fitted count row reserves one ESC count: known-item probability is `count/(row_total+1)` and ESC probability is `1/(row_total+1)`. An unseen context has only ESC with probability one.
- Every ESC is followed by a fully charged literal payload. A literal token is encoded as one canonical UTF-8 JSON single-token array document. The literal baseline uses the same token documents.
- Common outer bitstream/method framing and suffix-length framing are omitted equally for every method; no method-specific fitted state or literal payload is omitted.

Implementation provenance: chaoslang branch `agent/frozen-suffix-scoring`, corrective commit `ce0e476` (following superseded initial commit `5be45e5`). The implementation record explicitly preserves why the first green test result was insufficient. No external benchmark was run before this clarification.
