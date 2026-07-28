# exp00 — Upstream MORK smoke

## Status
Blocked at environment discovery (2026-07-12).

## Source
- MORK: `https://github.com/trueagi-io/MORK`
- Commit: `5464713539c1c1cb491397f4c7bb1d9cdc8b74a0`
- Branch: `main`

## Intended upstream command
`cd repos/MORK/kernel && cargo build --release`

## Observed prerequisites/blockers
- `rustc`, `cargo`, and `rustup` are not installed on the local host.
- Root workspace requires Rust edition 2024 and README says nightly.
- Workspace dependency `pathmap = { path = "../PathMap/", version = "0.3.0", features = ["jemalloc", "arena_compact", "nightly"] }` now has sibling checkout `repos/PathMap` at `233fbbac7c7b8d8b2414b54689a2da4331d234c7` from Adam-Vandervorst/PathMap. Its package metadata reports version 0.3.0, Rust >=1.88, and the expected features. Compatibility remains unverified until build.

## Result
Not run yet. No claim of successful MORK installation.
