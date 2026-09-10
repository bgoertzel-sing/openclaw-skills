# Frame-oracle v14 Stage-A isolation execution contract

- Frozen: `2026-08-08T03:14:41Z`
- Parent: clean frame-oracle v13 commit `8108d986e95d66e74cdb222695b9c94f81350c26`
- Status: orchestration contract only; no fixture or candidate admitted

## Blocker

The persistent semantics worker must audit `PROJECT.md`, `TASKS.md`,
`DECISIONS.md`, `NOTES.md`, and recent experiment records before acting. Those
records contain details of retired v14 fixture attempts. The frozen Stage-A
protocol simultaneously requires that the fixture author have no such prior
visibility. A normal persistent-worker turn therefore cannot truthfully attest
Stage-A independence.

## Required separation

Stage A may run only in a fresh, context-isolated process whose complete input
surface is mechanically restricted to the four items enumerated in
`docs/frame_oracle_v14_fixture_provenance_protocol_20260808.md`. The persistent
worker may prepare and verify the input manifest, but it must not author,
suggest, edit, or preview fixture content.

Before authoring, the isolated process must emit:

1. its exact input manifest with SHA-256 for every readable regular file;
2. a denial result for every project path outside the allowlist;
3. the clean parent commit and empty Git status;
4. a post-boundary 256-bit OS-random receipt and receipt hash; and
5. an attestation that no conversation transcript, memory, prior experiment,
   sealed path, candidate source/test, network input, or semantic-free input
   was available.

It must then deterministically derive exactly one fixture for each non-unknown
predicate, verify only the two frozen premises against clean v13 and the finite
contract, and write fixture JSON, derivation notes, ledger, command receipt,
and hashes. The fixture artifacts become immutable at first successful hash.
Any extra readable input, denial failure, premise mismatch, nondeterministic
replay, or post-freeze mutation permanently retires that fixture set.

## Stage-B boundary

Stage B remains a later turn. It may receive only the frozen Stage-A artifact
bundle and the inputs already permitted by the original two-stage protocol.
It must verify every hash before candidate visibility. No v14 sealed access,
oracle/model call, labels, readout, substitution evaluation, semantic loss,
runner adaptation, remote compute, publication, or push is authorized.

V14 remains sealed, unopened, and unconsumed.
