# Frame-oracle v14 independent-fixture provenance protocol

- Frozen: `2026-08-08T01:13:00Z`
- Parent implementation: clean frame-oracle v13 at `8108d98`
- Status: process contract only; no fixture or candidate admitted

## Purpose

The previous mechanical fixture gate is inadmissible because its author saw
unadmitted v14 candidate tests first. This protocol defines the smallest
clean successor process. It does not create cases and does not authorize v14
implementation, runner work, sealed access, or inference.

## Input allowlist for the fixture-authoring phase

The authoring process may read only:

1. `docs/frame_oracle_v14_relation_bearing_contract_20260807.md`;
2. clean commit `8108d98`, limited to `src/relaleap/frame_oracle.py` and
   `tests/test_frame_oracle_v13.py`;
3. this protocol; and
4. a newly recorded local randomness receipt containing 256 bits from the OS,
   generated after the run directory and boundary declaration exist.

The process must not read any v14 candidate source/test, either failed fixture
run, any sealed battery path, any opened v13 artifact or failure identifier,
or any later semantic result. It must record every file read, its SHA-256, the
clean commit, and an explicit contamination attestation before authoring.
Unexpected input or prior visibility fails closed.

## Two-stage freeze

Stage A authors exactly one fixture per non-unknown predicate using fresh
entities derived deterministically from the randomness receipt. Each fixture
must assert only the premise needed for implementation: clean v13 returns the
proposed non-unknown tuple unchanged, while the frozen exact-template contract
rejects the whole sentence. Freeze fixture JSON, generator/derivation notes,
input ledger, and SHA-256 before reading or executing any candidate v14 code.
No fixture may be edited, replaced, or supplemented after this freeze.

Stage B, in a later clean turn, first verifies the Stage-A hashes and input
ledger, then may inspect or independently implement the minimal frozen
contract. It runs the frozen fixtures once, followed only on success by the
focused exposed v1--v13 and pinned suites. A premise mismatch, provenance
discrepancy, hash mismatch, or test failure retires the fixture set.

## Required receipts and boundary

Record UTC timestamps, exact commands, stdout/stderr/status/time, Git head and
status, file-read ledger, random receipt hash, fixture hash, and test counts.
Keep candidate implementation and runner/provenance adaptation in separate
isolated worktrees and turns. V14 remains sealed, unopened, and unconsumed.
Forbidden throughout are oracle/model calls, labels, readout, substitution
evaluation, semantic loss, remote compute, publication, push, and input from
the semantic-free lane.

