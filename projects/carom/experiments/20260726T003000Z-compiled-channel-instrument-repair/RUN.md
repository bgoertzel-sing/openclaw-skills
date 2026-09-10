# CAROM compiled-channel v2/v3 instrument repair

- Status: `completed local constructed-control gate`
- Date: `2026-07-26`

## Question

Do repaired v2/v3 instruments satisfy the audit contracts before application
to scientific checkpoints?

## Repairs

- Complete dwell-collapsed sequence scoring retains revisits and every
  transition; Kendall tau is explicitly first-visit-only.
- AUROC uses direct positive/negative comparisons with ties worth one half;
  degenerate class cases return undefined. Threshold-group AUPRC states a
  deterministic tie convention.
- Public evaluation requires an explicit frozen `span_fn`.
- Corpora serialize canonically on CPU; checkpoint loading uses
  `map_location`.
- Dominance margin, live-normalized entropy, classified fraction, and an
  unclassified state prevent arbitrary smeared-mode assignments.
- Integration-budget mutation is protected by `try/finally`.
- Probe randomness uses local seeded Torch generators.
- Switching output includes a matched natural baseline and uses descriptive,
  non-categorical language.
- Cross-slot aggregation is device-preserving and zero-safe.
- Padded modes are excluded from decisiveness metrics.

## Constructed controls

Command:

```bash
python3 -m unittest -v \
  test_harness_v2_repaired.py \
  test_harness_v3_repaired.py \
  test_gpt2_schedule_diagnostic.py \
  test_gpt2_controller_v6.py
```

Result: 19 tests passed. Controls cover full revisit sequences, all-tied and
mixed-tie AUROC, degenerate edges, smeared/unclassified activity, adapter
injection, CPU corpus/load portability, mutation restoration, locally seeded
repeatability, commuting/noncommuting linear phases, stable/unstable switching
words, zero/nonzero coupling, padded modes, schedule shape, and the v6 peak
guard. `py_compile` also passed for both harnesses and the Step-2 runner.
The complete repository suite also passed: `54 passed`, with one pre-existing
scheduler-order warning in the v4 regression fixture.

## Interpretation

The local constructed-control gate passes. This licenses use of these
instruments as measurements, not categorical claims about global commutation,
joint spectral radius, typed slots, or heteroclinic stability. GPU-device
execution remains an operational preflight within the first approved remote
run.
