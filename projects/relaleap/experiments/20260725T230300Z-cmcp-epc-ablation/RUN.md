# CMCP bridge Step 4: ePC ablation

- Status: complete
- Project: `relaleap`
- Started: 2026-07-25T23:03:00Z
- Execution: local CPU
- Seeds: `701,809,907`

## Question

Do two ePC settle steps at KD coefficient 0.02 improve the calibrated
response-CMCP outcome enough to justify keeping ePC in this calibration loop?

## Frozen comparison

Compare the current two-step ePC packet objective against direct
temperature-2 KL distillation, holding fixture, response-CMCP weights, applied
mass, seeds, updates, initialization, teacher training, optimizer, and KD
coefficient fixed.

The primary comparison is CMCP Task-B loss. Task-A retention increase is the
secondary comparison. ePC earns its place only if it has lower mean Task-B loss
without a larger mean Task-A retention increase. Otherwise the calibration
loop will adopt direct KD for speed, while settled-error credit accounting
remains a separate future fibre-routing hypothesis rather than a demonstrated
component.

The ePC energy-monotonicity invariant remains required for the ePC arm but is
not evidence of outcome value.

## Results

Three-seed CMCP means:

| Mode | B loss | B accuracy | A retention increase | Mean runner wall seconds |
|---|---:|---:|---:|---:|
| two-step ePC | 2.16338287 | 0.22873264 | 0.42988435 | 14.9077 |
| direct KD | 2.19309518 | 0.22092014 | 0.38744885 | 6.8793 |

**Observation:** ePC improved Task-B loss by `0.02971231` and accuracy by
`0.00781250`, but worsened Task-A retention by `0.04243550` and took about
`2.17x` the measured runner time.

**Decision:** under the frozen joint criterion, ePC did not earn its place
because its lower Task-B loss came with larger retention loss. Adopt direct KD
for the fast selector-calibration loop. Preserve the two-step ePC mode and this
positive-plasticity/negative-retention result for future settled-error routing
work; do not interpret the decision as evidence that ePC has no effect.

Focused tests: `8 passed in 2.88s`. All six JSON artifacts exited cleanly and
their SHA-256 hashes are retained with the run.
