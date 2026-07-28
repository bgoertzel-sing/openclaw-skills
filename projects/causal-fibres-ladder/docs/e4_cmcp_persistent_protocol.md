# E4/CMCP Persistent-Ledger Duplicate-Burst Protocol

## Question

Does persistent CMCP evidence accounting limit duplicate precision inflation,
overconfidence, and interference when constraint bursts recur over eight
episodes on the confirmed text-like E4 substrate?

## Frozen implementation contract

- Train the existing residual six-block student for 75 updates.
- Generate one fresh text-like evaluation batch per episode.
- Append one fresh innovation, a duplicate and deterministic descendant of
  episode 1, and every third episode a 50%-oracle-independent packet.
- Keep packet identifiers globally unique. Duplicate and descendant provenance
  share the episode-1 innovation identifier.
- Recompute each arm over the complete accumulated packet ledger at every
  episode. CMCP canonicalizes innovations and recomputes conditional score
  information in stable packet order.
- Compare naive, CMCP, first-per-mechanism-direction, and oracle accounting.
- Settle only logits with the existing weighted direct-logit sink; never change
  model parameters.
- Report current-batch task loss/accuracy, 10-bin ECE, multiclass Brier score,
  total effective precision, task-loss headroom against a label-clamped
  diagnostic anchor, and episode-1 retention under the current ledger.

## Invariants

- Packet identifiers are unique and packet tensors share one batch/factor
  shape.
- Duplicate provenance contributes at most one canonical CMCP/oracle packet.
- CMCP results are invariant to presentation order within an episode.
- Direction-only retains only the first mechanism-family packet.
- The terminal model hash is identical before and after all episodes.
- Output uses schema `causal_fibres.e4_cmcp_persistent.v1`.

## Calibration and confirmation

Calibration seeds are `61001, 62103, 63209`. Reserved confirmation seeds are
`64311, 65439, 66543, 67649, 68757`. Numerical thresholds will be frozen only
after the three calibration seeds. In particular, the stated protocol creates
one genuinely new innovation each episode, so oracle precision growth must be
measured before freezing a narrow episode-8 oracle range.
