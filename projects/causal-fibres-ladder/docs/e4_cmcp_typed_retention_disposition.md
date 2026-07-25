# E4/CMCP Typed Retention Disposition

## Decision

The typed-store and parameter-learning harness pass their operational gates,
but the three-seed calibration does not justify confirmation of a CMCP
retention advantage.

## Established

- The store carries cohort, ordered example, packet, provenance, innovation,
  mechanism, precision, and content-hash identities.
- It fails closed on row permutation, unknown/mismatched cohort, duplicate
  packet identity, and conflicting reuse of an innovation identity.
- Five learning arms begin from one exact model hash, receive identical
  Task-B batches, and perform identical optimizer-update counts.
- CMCP effective precision remains close to oracle across the three
  calibration seeds (`6.8364--7.9343` versus oracle `7.5`) while naive reaches
  `21.0`.
- CMCP and oracle retain substantially more Task-A behavior than no-ledger or
  direction-only replay while learning Task B.

## Negative result

Naive duplicate accumulation was not practically harmful in the calibrated
one-factor reversal. It retained Task-A accuracy better on all three seeds and
matched or nearly matched CMCP Task-B accuracy on two. Aggregate losses also
favored naive. The preregistered confirmation seeds remain sealed.

## Interpretation

The earlier frozen-logit benefit does not automatically transfer to parameter
learning. In this protocol, extra replay weight behaves largely as useful
regularization rather than damaging overconfidence. CMCP remains the
statistically principled accounting rule and tracks oracle behavior, but a
continual-learning advantage is not demonstrated.

The next scientifically motivated stressor would need correlated evidence with
systematic bias or a longer nonstationary curriculum where excessive replay
weight creates measurable plasticity loss. Such a protocol must be frozen
independently; the present result must not be rescued by post-hoc thresholds.

## Evidence

- Protocol: `docs/e4_cmcp_typed_retention_protocol.md`
- Operational smoke:
  `experiments/20260725T020759Z-e4-cmcp-typed-retention-smoke/`
- Three-seed calibration:
  `experiments/20260725T021200Z-e4-cmcp-typed-retention-calibration/`
