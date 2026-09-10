# E4/CMCP Evidence-Ledger Disposition

## Disposition

The bounded E4/CMCP ledger experiment passes its frozen confirmation gates.
CMCP is admitted as an evidence-accounting layer for further ePC/MORK work,
but no predictive-performance or continual-learning advantage is claimed.

## Established locally

- Exact duplicates and deterministic descendants are idempotent.
- Independent repeats in the same mechanism direction remain usable. CMCP
  retained `0.997862` of the second packet on average, whereas a direction-
  only novelty filter discarded it.
- A known orthogonal change of score coordinates is removed to numerical
  precision.
- Canonical packet ordering makes the tested ledger result order invariant.
- The text-like E4 extractor and direct-logit sink remain compatible with
  ledger-weighted constraint packets.

## Important negative and unresolved evidence

- Naively counting a duplicate twice slightly improved immediate task loss.
  The result validates statistical multiplicity contracts, not immediate
  accuracy.
- Partial-redundancy weighting was imperfect: CMCP used `0.657531` of the
  second packet on average versus the experiment's `0.5` oracle and had mean
  absolute precision error `0.217595`.
- The experiment did not persist precision across episodes, alter model
  weights, or measure delayed overconfidence, interference, or forgetting.
- The rotated-frame test supplied the correct alignment; mechanism retrieval
  and learned intertwiners remain outside scope.

## Interpretation for ePC and MORK

ePC can provide extracted constraint packets and the direct-logit credit sink.
CMCP can decide how much statistical weight each packet deserves. MORK is a
natural eventual store for packet provenance, dependency edges, conditional-
information summaries, precision, and provisional/committed write state.

The next experiment should introduce repeated correlated manifestations across
episodes. It should compare naive and CMCP persistent ledgers on calibration,
precision growth, retention, and curriculum reversal. This is the smallest
test likely to reveal whether exactly-once assimilation produces a practical
benefit rather than only satisfying an accounting invariant.

## Evidence

- Calibration:
  `experiments/20260725T001336Z-e4-cmcp-ledger-calibration-v2/`
- Frozen confirmation:
  `experiments/20260725T001900Z-e4-cmcp-ledger-confirmation/`
- Protocol:
  `repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1/docs/e4_cmcp_ledger_protocol.md`
- Code commit: `9ed922d`
