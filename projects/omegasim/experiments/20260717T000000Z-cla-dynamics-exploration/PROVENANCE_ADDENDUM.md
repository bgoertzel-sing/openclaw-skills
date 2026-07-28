# Provenance addendum: concurrent deterministic-content replay

- Original completion: `2026-07-17T00:46:42Z`.
- Concurrent replay start: `2026-07-17T00:46:41Z` (from test-log mtime).
- Concurrent replay finish: `2026-07-17T01:00:28Z` (from final manifest mtime).
- Repositories: clean OmegaSim
  `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`; clean detached chaoslang
  `974af31efaf6e3cc239252f78367d20e657ac45c`.
- Frozen detector SHA-256:
  `29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`.
- Command SHA-256:
  `234046061c93d9ab612ba5b72553f71bc7e59275abbbc0d5d10d45b0e4d4ddf7`.
- Wrapper SHA-256:
  `7b17ee9680ded6bf07ec911e503f736356d3ccb6a52d3a34ccef3a3d70f62f14`.
- Replay steps SHA-256:
  `b7fad1b3ad8f7fe8d2558e74702ae1abea3891b1936aa7139f753d29e889fde4`.
- Replay artifact manifest SHA-256:
  `065e815726b7cbdc5b802d8230bda6149162e421eb10aabb4aef4834c2a54f10`.

The second invocation reused all six already completed tight shards and
recomputed only the broad balanced phase. Eight focused tests passed; the
broad phase completed 72 tasks / 216 rows in `826.267` seconds with exit 0.
The current artifacts contain 486 rows and reproduce the original completion's
counts, four tight promotions, and uniform two-production/zero-category
structure. `fingerprint_aggregates.json` remained byte-identical at SHA-256
`3cdc05f12771898aa7f80e03712329bbfdb3ccf1cf7d5d40f7053b6cc81fa4ca`.

Current replay artifact hashes:

- `all_fingerprints.json`:
  `0afb61ad03e41f53769236d66209772583fc457489a48da4f1bcfc415fead942`
- `all_fingerprints.csv`:
  `c0c9c3c5b555dedd961a230d0dbef1eb43bed637acd9b82f753ab19fc2a9df9a`
- `broad_fingerprints.json`:
  `bf3fe1c9a97c01e0636a21ada8655a666971233551034cb3cc1803bb61e699b6`
- `broad_fingerprints.csv`:
  `c1643b452c093a9e4694c68091734deac0d41ceb7d254bb2541d5c72fde82382`
- `appraisal_control_deltas.json`:
  `8df4488531a8a81734fea55e4274d2eb9102ad119a89969eaa0e8df3af5e2e6f`
- `fingerprint_aggregates.json`:
  `3cdc05f12771898aa7f80e03712329bbfdb3ccf1cf7d5d40f7053b6cc81fa4ca`

The row-level hash difference is caused by the experiment wrapper collecting
process results with `as_completed` without a final deterministic sort. It
does not establish independent scientific evidence. No detector, threshold,
seed, control, or simulation implementation changed. Strong attractor and
grammar claims remain gated by the independent stricter CLA held-out coding
failure.
