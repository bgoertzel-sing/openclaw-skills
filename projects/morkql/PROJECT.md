# Morkql

## Purpose
Rapidly implement and test the July 12, 2026 Morkql v0.1 draft: a MeTTa-shaped declarative query language compiling to existing Morkl finite-path-space algebra, with inspectable plans and eventual proof-carrying compilation.

## Status
Active, launched 2026-07-12. Local-first. MORK cloned at `repos/MORK`, commit `5464713539c1c1cb491397f4c7bb1d9cdc8b74a0` (trueagi-io/MORK main). PathMap cloned at `repos/PathMap`, commit `233fbbac7c7b8d8b2414b54689a2da4331d234c7` (Adam-Vandervorst/PathMap main, package version 0.3.0). MORK build reproduced with Rust nightly 1.99.0 (2026-07-12), installed in userspace via rustup. `cargo build` succeeds (1m42s), kernel tests pass (0 tests in default member, no failures). Upstream `eval` workspace test has a pre-existing import error (`SinkItem` not exported from `eval_ffi`) at pinned commit — not introduced by us. Morkql frontend: 9/9 tests pass. Rust toolchain: `~/.cargo/bin`, default set to nightly.

## Source specification
- `library/morkql-spec-v0.1.pdf`, SHA-256 `986da31b46c48ccabb412d63dffbbd4e7eeff59c8ca2625717c9a55f0927a551`
- `library/morkql-spec-v0.1.txt`
- Status: design proposal, not an official MORK/Morkl/MeTTa standard.

## Initial scope
1. Parse canonical ASCII Morkql surface syntax.
2. Implement static checks and normalized logical IR.
3. Produce deterministic explain plans and a typed Morkql Core/Morkl AST.
4. Implement Base-profile forms: `find`, long `query`, `union`, `intersect`, `except`, positive `rules`.
5. Connect emitted programs to the actual pinned MORK/Morkl implementation and test semantic equivalence.

## Explicitly deferred
- petta-memory and petta-chem integration.
- Distributed execution, transactions, persistence, broad optimization, and claims of verified compilation before a checker exists.

## Success criteria
- Small upstream MORK smoke reproduced at pinned commits.
- Compiler accepts all valid Base-profile examples and rejects specified static errors.
- Emitted target contains no surface-only forms.
- Differential tests compare reference logical semantics with emitted Morkl/path-space execution.
- Build/test commands, toolchains, commits, and failures are recorded.

## Repositories
- `repos/MORK`: https://github.com/trueagi-io/MORK at `5464713539c1c1cb491397f4c7bb1d9cdc8b74a0`.
- `repos/PathMap`: https://github.com/Adam-Vandervorst/PathMap at `233fbbac7c7b8d8b2414b54689a2da4331d234c7`; package `pathmap` 0.3.0, Rust >=1.88.
- `repos/morkql`: local implementation repository, initial commit `4cdf4c6`, MIT licensed.

## Risks / open questions
- MORK expects sibling `../PathMap/`; the package metadata points to Adam-Vandervorst/PathMap and the pinned checkout matches version 0.3.0, but upstream compatibility still needs an actual build.
- No Rust toolchain is installed on this host; install only after provenance inspection, in an isolated user-local location.
- The PDF cites Morkl/Zippy artifacts whose canonical repositories or branches still need identification.
- MORK byte encoding is intentionally unstable; compiler frontend should target an abstract versioned Core/AST boundary.
- Runpod CPU may help builds/tests, but autonomous spend is zero; use only after explicit costed approval.
