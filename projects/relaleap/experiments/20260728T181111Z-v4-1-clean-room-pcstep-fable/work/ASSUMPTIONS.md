# Clean-room synthetic PCStep specification

This is an independently invented, synthetic executable hypothesis informed
only by Ahmad Mesto's July 26, 2026 technical report. It is **not** a
reproduction of Mesto's unpublished code, is not compatible with his
checkpoints, and supplies no evidence at transformer scale or for C4-prime
admission.

After this implementation and its tests were complete, Ben relayed Mesto's
pointer to the public `MesTTo/metta-on-mork` repository. The post-hoc inspection
and non-contamination boundary are documented in `UPSTREAM_PROVENANCE.md`.

## Paper-derived assumptions

- Each layer output is `x_l = f_l(x_(l-1)) + epsilon_l`.
- Settlement starts from zero errors and descends
  `0.5 * sum_l ||epsilon_l||^2 + task_loss`, while model weights are frozen.
- Weight learning is a separate phase. Settled states are treated as constants;
  each layer locally regresses its prediction onto its settled target.
- At `T=1`, the zero-error task-loss derivative supplies the backpropagation
  adjoint and one error step is the anchor for the local update.
- The optimizer is AdamW. A gate attenuates a module's local weight gradient
  after settlement and before the optimizer step.

These statements are re-expressions of equations (1)--(3) and the `T=1`
discussion in section 2.1 of the report. The report describes a head task-loss
update separately. This fixture has no separately parameterized head.

## Invented engineering choices

- The fixture is a two-layer bias-free linear network with squared-error task
  loss. It is deliberately small enough to have a separate handwritten oracle.
- Only `T=1` is supported and rejected otherwise. Error learning rate,
  AdamW hyperparameters, and float64 arithmetic are explicit configuration.
- The layer-local objective uses settled input and target arrays copied before
  weight differentiation. The implemented local gradient is
  `(prediction - settled_target)^T @ settled_input / batch_size`.
- Gates are a mapping with keys `layer1` and `layer2`, values in `[0, 1]`.
  This matches comcrit's conceptual R3 seam (module gradient multipliers), but
  the prototype does not import or modify comcrit.
- RNG is intentionally consumed once per step even though the current
  computation is deterministic. This makes RNG restoration testable and
  reserves an explicit state seam for later stochastic fixtures.
- Batch-plan state is an immutable tuple of batch identifiers plus a cursor.
  The current batch identifier must match the planned cursor, then the cursor
  advances exactly once.
- Snapshots use a canonical JSON encoding of float64 array bytes (hex), optimizer
  moments, NumPy generator state, and batch-plan state. This is fixture-level
  exactness, not a portable production checkpoint format.
- AdamW is independently implemented here and is not asserted bit-compatible
  with `torch.optim.AdamW`.

## Behavioral invariants

1. `pc_step(theta, optimizer_state, batch, t, gate)` has no hidden mutable
   state and returns a new state without modifying any argument.
2. Settlement and weight update are distinct functions. Settlement hashes
   weights before and after and raises if they differ.
3. Snapshot/restore preserves model arrays, moments, step, RNG, and batch plan
   byte-for-byte on the synthetic fixture.
4. The `T=1` result equals a separately expressed reference calculation,
   including the gate and AdamW update.
5. This prototype makes no claim about deep settles, attention, layer norm,
   tokenization, GPT-2, Mesto checkpoints, trajectory tangents, or C4-prime.
