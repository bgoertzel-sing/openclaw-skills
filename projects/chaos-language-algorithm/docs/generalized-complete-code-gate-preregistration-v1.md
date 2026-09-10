# Generalized complete-code synthetic decision gate v1

Status: frozen before outcome inspection. This is a local synthetic decision
gate, not an attractor benchmark and not chaos or semantic-grammar evidence.

## Question

On the already frozen 19-frame fixture, does the one deterministic intended
joint category/generalized-chunk proposal reduce the complete canonical
two-document codelength relative to transmitting the initial literal state?

## Fixed fixture and candidate

- Use `fixture_symbols()` from `chaoslang.benchmarks.joint_diagnostic`: 19
  frames `a mNN b qNN`, 76 tokens, canonical-symbol SHA-256
  `c828bafa0955f0e30ee947865a944e03ac3081203e6bc9e5d34578951310af89`.
- Use `JointCategorySlotMiner(n_min=3, n_max=3, min_uses=2)`.
- Select exactly the proposal with category members `m00` through `m18` and
  generalized pattern `a CategorySlot(category_name) b`. Missing or multiple
  matches are integrity failures; no alternate candidate may be substituted.

## Frozen code and classification

Encode both the untouched initial state and the state after applying the joint
proposal with `chaoslang.scoring.state_code.encode_state`. Charge exactly eight
bits per emitted canonical UTF-8 JSON byte, including the complete category,
production, parse, and ordered member side tables.

Both codes must decode to the exact source corpus and re-encode byte-for-byte.
Proposal enumeration must repeat identically. Any failed gate aborts without a
scientific classification.

- `joint_improves_complete_code` iff `joint_total_bits < initial_total_bits`.
- `complete_code_rejects_joint` otherwise, including equality.

If the joint improves, the next implementation step may integrate this exact
complete-code delta as a bounded joint-search acceptance scorer. If rejected,
do not enable the joint move; first specify a scientifically justified,
decodable code refinement without using attractor held-out suffix outcomes.
Either result leaves the Mackey--Glass/Lorenz--96 null unchanged and does not
authorize a new attractor benchmark by itself.

## Execution boundary

Run exactly `bash command.sh` from the experiment ledger after repository
commit, implementation/protocol/command hashes, environment, and focused
outcome-independent checks are recorded. Local CPU only; no paid/remote
compute, push, integration, or held-out suffix inspection.

Relevant Research Rules: 1, 2, 5, 6, and 7.
