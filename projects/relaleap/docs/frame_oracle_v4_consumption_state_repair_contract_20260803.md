# Frame-oracle v4 consumption-state repair contract

- Date: `2026-08-03`
- Status: frozen before implementation
- Parent implementation: `agent/frame-oracle-v4` commit `acf3fbf`
- Counterexample:
  `experiments/20260803T131110Z-frame-oracle-v4-consumption-counterexample/`

## Defect

The runner persists `gate_consumed=false` in its exception handler until an
entire pair has completed and been appended. If the first public inference
completes and the second call fails, the persisted record says zero pairs and
unconsumed. The same unsafe state can occur after later requests or an abrupt
process exit. This contradicts the frozen rule that any public-case inference
consumes the battery.

## Required state machine

1. `verified_unopened`: validate commit, import provenance, public contract,
   prompt/schema/source hashes, model identity, output nonexistence, and answer
   commitment without reading answers or issuing inference.
2. `consumed_pending`: immediately before the first network request, atomically
   persist a conservative record with `gate_consumed=true`, attempt timestamp,
   frozen identifiers, zero completed calls, and no answer-derived content.
3. `consumed_partial`: after every completed request, atomically replace the
   record with the raw response, normalized result when available, exact
   completed-call count, and any error. This state never reverts to unconsumed.
4. `consumed_decoded`: only after all 48 calls have completed may the runner
   verify and read the answer commitment.
5. `consumed_passed` or `consumed_failed`: persist the final exactness,
   determinism, and per-stratum result. Every error after state 2 is terminal
   for that battery.

Atomic persistence means write a same-directory temporary file, flush it,
`fsync` it, replace the destination, and `fsync` the parent directory. A
pre-request persistence failure must abort without inference. Conservatively
marking a process as consumed before a request that never reaches Ollama is
acceptable; under-reporting consumption is not.

## Bounded implementation scope

- Change only runner state persistence and its engineering tests.
- Do not alter prompt, schema, v2/v3/v4 normalization, model, seed, decode,
  public cases, or answers.
- Do not inspect any sealed answer or issue any Ollama inference.
- Reject a pre-existing output unless it is an explicit resumeless terminal
  diagnostic from a no-inference preflight; the one-use run cannot resume.
- Record and verify the actual local model digest before state 2. Do not merely
  copy a CLI digest into output metadata.

## Required failure-injection fixtures

Using synthetic public inputs and a mocked network function, independently
cover failure before state 2, first request failure, second paired-request
failure, failure after at least one complete pair, answer commitment mismatch,
atomic-write failure before inference, and atomic-write failure after
consumption. Assert that no test reads a real answer file or contacts Ollama.

## Refreeze gate

From a clean descendant commit, require focused tests, all exposed frame
regressions, the full suite, compilation, shell syntax, diff check, and exact
interpreter/import attestation. Freeze a replacement manifest and stop before
inference. The existing 24-case battery remains eligible only because the
counterexample used a synthetic fixture and the public record still says
`opened=false`; any uncertainty about real inference requires fresh cases.
