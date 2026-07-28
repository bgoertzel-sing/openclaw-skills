# Frozen detector identity contract

Before any measured OmegaSim/CLA run, the wrapper must verify all of the
following before importing or executing detector code:

1. the OmegaSim repository is at the predeclared full commit and is clean;
2. the external `chaoslang` repository is at the predeclared full commit and
   is clean;
3. every predeclared implementation file has its exact SHA-256 digest; and
4. the verification result is serialized as JSON in the experiment ledger.

Any mismatch exits nonzero before measurement. The verifier is provenance-only:
it must not import, modify, tune, or interpret the frozen detector. Expected
identities are supplied by the preregistered experiment wrapper so the same
seam can gate later independently frozen detectors.

Missing or unreadable repositories/files are identity mismatches, not verifier
crashes. They must produce a structured failure entry in the JSON report and a
nonzero exit so the ledger retains the reason measurement was refused.
For a readable but dirty repository, the report must also preserve the exact
`git status --porcelain` lines so the refusal is diagnosable without rerunning
against a worktree that may later have changed.

For the 2026-07-16 untouched-seed replication, the identities are OmegaSim
`18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`, chaoslang
`974af31efaf6e3cc239252f78367d20e657ac45c`, and detector SHA-256
`29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`.
