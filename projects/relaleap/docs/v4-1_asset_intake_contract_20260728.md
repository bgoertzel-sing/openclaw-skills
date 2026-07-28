# V4-1 C4-prime substrate asset-intake contract

- Status: active; awaiting source assets
- Created: 2026-07-28
- Decision authority: Ben's explicit direction to treat V4-0 as sufficient to
  proceed to V4-1
- Upstream evidence: `../experiments/20260728T162149Z-v4-functional-gate-nonlinear-torch/`
- Scope: V4-1 substrate inspection and a `T=1` adapter only. This is not a
  C4-prime deployment, policy experiment, or remote-compute authorization.

## Admission boundary

The V4-0 run remains formally **inconclusive under its original preregistered
5-sigma fixture-admission rule**: B2 was 3.033 sigma and high-LR B1 was 0.868
sigma. Ben has nevertheless accepted its direct paired-rollout evidence as a
pragmatic success for moving to V4-1. Therefore V4-1 may begin, but records
must not describe V4-0 as an exact-D validation, a preregistered statistical
pass, or evidence for transformer/policy efficacy.

## Required delivery bundle

The Mesto owner must supply an immutable bundle containing the following, with
an explicit licence/access statement:

| Item | Required identity evidence | V4-1 use |
| --- | --- | --- |
| Anchor, mid, and terminal PC--GPT-2 checkpoints | SHA-256, rung/tau, seed, training step | Snapshot/restore and rung selection |
| Settle and local-update implementation | repository URL or archive SHA-256, pinned commit | Freeze-weight assertion and adapter |
| Runtime/configuration | dependency lockfile, model/tokenizer IDs, all relevant configs | Reproducible import |
| Data specification | dataset version, split IDs, preprocessing/tokenization description | Batch-plan reconstruction |
| Production telemetry | raw milestone table/logs, hardware summary, checkpoint mapping | Provenance and reported-claim audit |
| Access/licence terms | scope, redistribution/storage restrictions | Preservation and execution boundary |

## Receipt procedure

1. Preserve the received bundle under the local research library without
   altering originals; record SHA-256 for each file and its acquisition date.
2. Record the repository commit, dirty state, dependency versions, model and
   tokenizer identities, and checkpoint-to-rung mapping in a new V4-1 ledger.
3. Run import-only checks followed by deterministic snapshot/restore checks;
   no reconstruction from the PDF is allowed.
4. Implement the narrow pure interface
   `(theta, optimizer_state, batch, t, gate) -> state` at `T=1`, with a
   runtime assertion that every model weight is unchanged during settlement.
5. Run adapter unit tests and reproduce the admitted C4-class `T=1` behavior
   on the supplied substrate. Only then may V4-1 be marked complete.

## Stop conditions

Stop V4-1 and report the missing or incompatible item if any required artifact
is absent, unhashed, inaccessible under its terms, cannot be imported with the
recorded configuration, or fails exact snapshot/restore. Do not substitute a
reconstructed configuration, a reported metric, a different checkpoint, or a
synthetic surrogate.

## Current receipt status

Updated 2026-07-28: Mesto identified the public GPL repository
`https://github.com/MesTTo/metta-on-mork`. It is preserved and pinned at
`../../../library/metta-on-mork-2026/`. The visible repository contains an
actual synthetic `2-2-2` XOR ePC settle/local-update demonstrator and MORK
rules, but inspection of both visible branches and history found no committed
PC--GPT-2 homotopy training implementation or production assets.

No production checkpoint, GPT-2 settle/local-update path, configuration,
dataset split identity, or telemetry bundle has been received. Access/licence
is partially resolved for the public repository (GPL), not for any still
unidentified production assets. The repository and supplied technical reports
remain insufficient to complete production V4-1 intake.
