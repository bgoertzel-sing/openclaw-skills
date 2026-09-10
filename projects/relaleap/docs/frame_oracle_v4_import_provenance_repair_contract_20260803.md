# Frame-oracle v4 import-provenance repair contract

- Date: `2026-08-03`
- Scope: local semantic oracle lane only
- Status: required before the one-use v4 gate
- Failure evidence:
  `experiments/20260803T091034Z-frame-oracle-v4-exact-command-preflight/`

## Counterexample

The interpreter and runner frozen at commit `1cbcf9e` fail before argument
parsing:

```text
ModuleNotFoundError: No module named 'relaleap.hdpc.frame_oracle_v2'
```

The frozen virtual environment resolves `relaleap` to the separate
`causal-fibres-ladder/repos/relaleap-e1` source tree. Thus the paired-decode
argument vector does not, by itself, identify the implementation it is meant
to evaluate. No oracle call occurred and the 24-case battery remains sealed.

## Bounded repair

1. Work only on the existing isolated `agent/frame-oracle-v4` branch, from
   clean commit `1cbcf9e`.
2. Add a deterministic invocation wrapper or equivalent environment contract
   that sets one explicit source root and rejects resolution of any imported
   `relaleap` module outside the v4 worktree.
3. Before accepting arguments or calling Ollama, assert and record the real
   paths and SHA-256 hashes for `relaleap`, `frame_oracle_v2`,
   `frame_oracle_v3`, and `frame_oracle_v4`, plus interpreter realpath and
   version. Reject missing, symlink-escaped, or mixed-root modules.
4. Do not change the prompt, schema, normalization semantics, model, seed,
   decode settings, public cases, or answer file. If any semantic source must
   change, invalidate this bounded repair and preregister a versioned successor
   instead.
5. Commit the provenance repair, rerun the six focused v4 fixtures, all exposed
   frame regressions, the full suite, compilation, and `git diff --check` from
   a clean state.
6. Produce a replacement freeze manifest containing the new commit, wrapper
   hash, explicit environment, interpreter metadata, resolved module paths,
   semantic-source hashes, and exact one-use command.
7. Stop before inference. A later fresh experiment may consume the existing
   gate exactly once only after verifying the replacement manifest.

## Acceptance and failure boundary

Import resolution must be single-root, explicit, hash-matched, and reproducible
without relying on an editable install elsewhere in the workspace. Any
pre-decode failure leaves the battery unopened; any failure after the first
public-case inference consumes it and fails closed. No labels, readout,
substitution score, or semantic loss is admitted by the repair itself.
