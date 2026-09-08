# Frame-oracle v8 executable-provenance repair contract

- Frozen: `2026-08-05T01:35:24Z`
- Trigger: exact v8 one-use argv exited 126 before runner entry
- Battery state: unopened and scientifically unconsumed
- Status: current manifest revoked; repair required before any later opening

## Counterexample

The frozen manifest directly executes
`scripts/run_frame_oracle_v8_pinned.sh`. At clean commit
`b54fdcc1c391bff49fcf1c7dce8b394355a287e4`, both the filesystem and Git tree
record that wrapper as non-executable (`0644` / `100644`). The preopen freeze
validated shell syntax and no-inference behavior without testing the exact
direct-execution boundary. Consequently `/usr/bin/env` returned exit 126 with
`Permission denied` before the wrapper body ran.

Evidence: `experiments/20260805T013037Z-frame-oracle-v8-one-use-gate/`.

## Scientific state

The failure occurred before runner entry. No gate output or import-provenance
sidecar was created; the public contract retained its frozen SHA-256 and
`opened=false`; no answer content, case content, proposal, response, normalized
row, or model generation was reached. V8 therefore remains unopened and
scientifically unconsumed, but the exact frozen manifest is permanently
ineligible and must not be retried.

## Bounded repair

An isolated descendant may make only these execution-provenance changes:

1. change `scripts/run_frame_oracle_v8_pinned.sh` from Git mode `100644` to
   `100755` without changing its bytes;
2. add a focused assertion that the wrapper is executable;
3. invoke the wrapper directly through the same `/usr/bin/env` boundary with
   `--help`, proving exact argv reachability without inference or answer
   access;
4. preserve all semantic source, prompt, schema, decode, public, answer, model,
   and consumption-state commitments;
5. rerun focused, exposed, and full tests from a clean commit and issue a new
   provenance manifest that attests Git mode as well as content hashes.

The repair turn must stop unopened. Any scientific one-use execution requires
a later fresh turn and only the replacement manifest argv. No in-place chmod,
retry, semantic tuning, readout, substitution evaluation, or semantic loss is
permitted under the revoked manifest.
