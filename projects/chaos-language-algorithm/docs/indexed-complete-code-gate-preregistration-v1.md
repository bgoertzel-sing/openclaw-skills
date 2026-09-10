# Indexed complete-code synthetic decision gate v1

Status: protocol fixed before outcome inspection. This is a local synthetic
coding comparison, not an attractor benchmark and not chaos or semantic-grammar
evidence.

## Question

On the already frozen 19-frame fixture, does the one deterministic intended
joint category/generalized-chunk state reduce the complete indexed two-document
codelength relative to the initial literal state?

## Fixed fixture and candidate

- Use `fixture_symbols()` from `chaoslang.benchmarks.joint_diagnostic`: 19
  frames `a mNN b qNN`, 76 tokens, canonical-symbol SHA-256
  `c828bafa0955f0e30ee947865a944e03ac3081203e6bc9e5d34578951310af89`.
- Use `JointCategorySlotMiner(n_min=3, n_max=3, min_uses=2)`.
- Select exactly the proposal with members `m00` through `m18` and generalized
  pattern `a CategorySlot(category_name) b`. Missing or multiple matches are
  integrity failures; no alternate candidate may be substituted.

## Frozen codes, controls, and accounting

The decisive comparison uses
`chaoslang.scoring.indexed_state_code.encode_indexed_state` for both states.
Charge exactly eight bits per emitted canonical UTF-8 JSON byte. The shared
sorted token table and all integer references are transmitted in full.

Controls are descriptive and cannot replace the decisive comparison:

1. Encode both states with the unchanged canonical JSON v1 `encode_state`.
2. Report model, data, and total bits for all four state/code combinations.
3. Require both codecs and both states to decode to the frozen source corpus
   and re-encode byte-for-byte.
4. Require the indexed literal control to use the same codec and accounting as
   the indexed joint state; no dictionary or fixture is supplied out of band.

Proposal enumeration must repeat identically. Any failed fixture, candidate,
source-corpus, decoding, canonicality, or determinism gate aborts without a
scientific classification.

## Frozen classification and action

- `indexed_code_accepts_joint` iff indexed joint total bits are strictly less
  than indexed initial total bits.
- `indexed_code_rejects_joint` otherwise, including equality.

If accepted, the exact indexed complete-code delta may be considered for a
bounded joint-search scorer only after implementation tests; it does not by
itself authorize an attractor rerun. If rejected, keep the joint miner disabled
and do not iterate further representations against this fixture without a new,
outcome-independent rationale and preregistration.

Canonical-v1 results must reproduce the prior direction and totals or the run
is an integrity failure, not a new classification: initial 34,352 bits, joint
34,416 bits. This check validates candidate/fixture continuity; it does not
enter the indexed acceptance rule.

Either outcome leaves the failed Mackey--Glass/Lorenz--96 held-out calibration
unchanged. Those suffixes must not be inspected or used for tuning.

## Execution boundary

Run exactly `bash command.sh` from the experiment ledger only after repository
commit, implementation/protocol/command/fixture hashes, environment, and
outcome-independent focused checks are recorded. Local CPU only; no paid or
remote compute, push, integration, or held-out suffix inspection.

Relevant Research Rules: 1, 2, 5, 6, and 7. Conceptually, indexing quotients
repeated token spellings into stable transmitted identities; it changes code
representation overhead, not grammar meaning.
