# Frame-oracle v14 Stage-A output-bundle schema

- Frozen: `2026-08-08T09:14:00Z`
- Parent: `8108d986e95d66e74cdb222695b9c94f81350c26`
- Status: handoff schema only; no fixture or candidate admitted

An independently initialized Stage-A author must return one directory whose
top-level `MANIFEST.sha256` authenticates every other regular file and does not
list itself. The directory must contain exactly these files:

1. `attestation.json`
2. `input-ledger.json`
3. `denial-receipts.json`
4. `random-receipt.sha256`
5. `fixtures.json`
6. `derivation.md`
7. `command.txt`
8. `stdout.log`
9. `stderr.log`
10. `status.json`
11. `MANIFEST.sha256`

`attestation.json` must record schema version `1`, UTC start/freeze times,
author executable identity and SHA-256, exact parent commit, empty Git status,
network isolation, absence of inherited transcript/context, and absence of all
forbidden input classes named in the author-handoff contract. Every boolean
claim must be literal `true`; missing or additional fields fail closed.

`input-ledger.json` must enumerate exactly the four frozen readable inputs,
with logical name, mounted path, and SHA-256. `denial-receipts.json` must cover
project history, prior experiments, sealed material, candidate v14 source and
tests, conversation/memory inputs, and semantic-free-lane inputs. Every denial
must be successful.

`random-receipt.sha256` contains only the SHA-256 of the post-boundary 256-bit
receipt; the receipt itself must not leave Stage A. `fixtures.json` contains
exactly four records, one for each non-unknown predicate, plus the clean-v13
and frozen-contract premise results. Fixture content becomes visible to the
persistent worker only after `MANIFEST.sha256` is durably written.

`status.json` must report zero exit status, exact fixture count four, exact
predicate coverage, both premises passing for every fixture, and a freeze flag.
The outer verifier checks filenames, canonical JSON parseability, hashes,
timestamps, executable identity, parent/status, input hashes, denial coverage,
predicate coverage, premise results, and immutability. It must not print or
otherwise expose fixture text. Any discrepancy retires the entire bundle;
repair in place is forbidden.

Stage B remains a later turn. This schema authorizes no independent author by
itself and no v14 access, implementation, oracle/model call, labels, readout,
substitution evaluation, semantic loss, runner change, remote compute,
publication, or push.
