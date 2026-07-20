# OmegaSelf — Notes

## 2026-07-15 — Phase 1 baseline

- The documented direct smoke command fails because `scripts/smoke_test.sh` is mode `0644`; invoking the unchanged file through `bash` is required.
- The smoke script assumes a `python` executable. The ProtoMegaBot2 `.venv` supplies Python 3.10.12 and all required validation dependencies.
- Under that isolated environment, 44/44 tests and pack validation pass. All 21 schemas also pass explicit Draft 2020-12 checks.
- ProtoMegaBot2 provider-free identity/publish boundary baseline is 7/7 passing. No Telegram token, provider call, live process, or restart was used.
- SWI-Prolog is not installed on this host. Full PeTTa/MeTTa runtime validation is therefore an explicit open limitation, not inferred success.
- The target has Patham9-style PeTTa PLN rules but no declared truth-semantics profile identifier. The rules-file hash is the temporary audit identity until OmegaSelf introduces an explicit profile.
- The current default sandbox policy is unsigned OpenShell YAML. It is not an OmegaSelf authorization manifest and cannot satisfy externally rooted allow-capable governance.
- Research Rules most relevant here: Rule 1 (validate the reasoner/runtime early), Rule 2 (keep the normative behavior spec explicit), Rule 5 (reproducible evidence), and Rule 7 (preserve the reasoner/governance abstraction seams).

## 2026-07-15 — Phase 2 record-only slice

- OmegaSelf reference 1.0.0 is installed only in the ProtoMegaBot2 venv. Editable and no-isolation wheel attempts failed under setuptools 59.6.0/no wheel; the package-declared isolated build succeeded.
- Isolated canary commit `2bfa244` adds a default-off, lazy-import bridge plus five loop observations without replacing the legacy evaluator.
- Observation bodies likely to contain user/tool content are stored as SHA-256 plus UTF-8 length, not raw strings.
- Startup prints verification status and root. Tamper detection prevents further appends in the current bridge instance but does not alter shadow-mode dispatch.
- The default OpenShell policy load is recorded as unsigned and unverified. It is not treated as an OmegaSelf manifest.
- Combined regression: 12/12 passed; compile and whitespace checks passed. Synthetic ledger: 5 records, root `3e300753c800f7c225e0785b1d77fc264162fcd144c253b5f183f678a1d19a42`.
- No live or canary process was started. Native hook syntax/runtime behavior still requires SWI-Prolog.

## 2026-07-15 — Phase 3 closure slice

- Commit `f5add4b` exposes typed evidence append with provenance/dependence stamps, append-only correction and disqualification events, and immutable closure construction.
- Closure tests retain controls for audit, exclude disqualified evidence only from the active view, aggregate correlated outcomes before independent revision, and explicitly report missing parents.
- Combined regressions pass 14/14 post-commit. No reasoner or gate can convert these closures into authority in this slice.

## 2026-07-20 — Track D interface contracts

- Added schema-first, provider-free contracts for evidence records, committed pre-action predictions, and typed policy decisions under `contracts/`.
- Canonical interchange is a strict MeTTa-shaped S-expression. Field order is normative; all records carry schema name/version, an immutable evidence-closure handle, and distinct causal/record/adoption clocks.
- Evidence records bind provenance, three UTC timestamps, event version, payload identity, and replay inputs without claiming that replay occurred.
- Predictions enforce normalized outcome distributions, bounded affected-need deltas and confidence, and `proposal-created < prediction-committed < action-authorized`; authorization may remain `null`, but hindsight predictions are invalid.
- Policy results are closed to Allow/Deny/RequireProbe/RequireReview/Defer. Allow requires verified, unexpired external authority and no rejection causes. Non-Allow requires a typed cause. Authority inputs beginning `affect:` are invalid, preserving the OMERA constraint that affect cannot expand authority.
- Dependency-free stub verification passes over nine fixtures: six valid/edge fixtures round-trip byte-identically and three malformed fixtures fail with `ContractError`. Command: `python3 projects/omegaself/contracts/stub_tests.py`.
- No PeTTa runtime, provider, Telegram, credential, or live/canary path was used. Relevant Research Rules: 2 (spec before logic), 5 (reproducible evidence), and 7 (substrate-neutral seams).
