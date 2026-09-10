---
name: "sealed-evaluation-gate-lifecycle"
description: "Fail-closed lifecycle for one-use sealed evaluations, including execution-capability equivalence before gate consumption."
---

# Sealed Evaluation Gate Lifecycle

## Purpose

Use when an evaluation has hidden answers, a one-use budget, or an integrity constraint that makes a partial or malformed execution scientifically non-recoverable. Preserve the distinction between instrument readiness, gate consumption, and scientific outcome.

## Before opening

1. Read the authoritative project `TASKS.md`, sealed-contract document, and prior consumption state. Confirm explicit authorization and that the exact gate is still unopened.
2. Freeze immutable inputs: case-root digest, expected schema, model/provider identity, runner source/commit digest, environment, command line, and an atomic state location outside generated results.
3. Define the exposure and consumption boundaries separately. Record which operation consumes the one-use budget and which first reads an answer, label, score, protected model output, or derived metric.
4. Run only non-answer-bearing checks: import/compile, schema fixtures with synthetic data, response-normalization fixtures, and command-help/provider identity probes as permitted by the contract.
5. Prove execution-capability equivalence under the exact intended launcher and isolation profile, using synthetic fixtures only:
   - create the same namespaces, mounts, environment clearing, limits, and working directory;
   - exercise required loopback/server-client connectivity, socket binding, IPC, filesystem writes, and subprocess creation;
   - load a tiny synthetic or non-protected stand-in through the same loader path when permitted;
   - record kernel, sandbox tool, privilege, dependency, and capability results in a machine-readable readiness manifest.
   A `--help` check is availability evidence, not capability evidence.
6. If any required capability cannot be tested without consuming the gate, state that limitation explicitly in the sealed contract and decide in advance whether the resulting readiness failure consumes the gate. Do not improvise this policy during execution.

## Opening and execution

7. Acquire the gate atomically at the preregistered consumption boundary. Record `opened=true`, run identifier, input manifest digest, readiness-manifest digest, and timestamp.
8. Stream only minimal operational metadata until the exposure boundary. Never print protected rows, answers, or unredacted provider payloads to logs.
9. On every capability, schema, transport, or normalization failure, fail closed. Persist completion counts and error class; mark `consumed_failed` only if the contract's consumption boundary was crossed. Do not retry in place.
10. Only after all response validation passes may the authorized readout stage access answers or compute scores.

## Triage and successor gate

11. Classify terminal state explicitly:
   - `readiness_failed_unconsumed`: required execution capability failed before the consumption boundary;
   - `instrument_failed_no_exposure`: the gate was consumed or execution began, but no protected content was read;
   - `scientific_result`: protected readout completed under the frozen protocol;
   - `integrity_compromised`: protected content may have been exposed; do not interpret or reuse it.
12. Preserve failed artifacts read-only. Diagnose only from source, synthetic fixtures, readiness metadata, and other contract-permitted evidence. State exactly whether models, cases, answers, labels, predictions, or scores were read.
13. A replacement gate requires a fresh sealed contract, a disjointness or reuse rationale, a new manifest digest, and separate authorization where project policy requires it. Never relabel a replacement as a retry.

## Ledger and reporting

14. Update project `TASKS.md` and `NOTES.md` with command/commit, readiness and gate-state transitions, evidence path, exposure statement, classification, and smallest next gate. Update the cross-project Kanban only when its compact status or next action changes.
15. In summaries, keep execution readiness, gate consumption, and scientific evidence as separate claims. Do not call an instrument failure a negative scientific result.

## Checklist

- [ ] Authorization and unopened state verified
- [ ] Inputs, runner, and source provenance frozen
- [ ] Consumption and exposure boundaries separately defined
- [ ] Exact-launcher synthetic capability rehearsal passed
- [ ] Readiness manifest recorded and hashed
- [ ] Atomic acquisition recorded at the preregistered boundary
- [ ] Failure state and exposure status recorded
- [ ] Replacement, if any, has a fresh contract and manifest
- [ ] Project ledger and Kanban pointer reconciled
