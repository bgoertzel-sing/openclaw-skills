# CMCP-guided KD/ePC bridge

- Status: calibration complete; confirmation stopped
- Project: `relaleap`
- Started: 2026-07-25T16:10:00Z
- Execution: local CPU first

## Question

Under matched optimizer and teacher-call budgets, does typed CMCP accounting
prevent duplicate/derived teacher packets from inflating distillation credit
while retaining useful independent teacher views, and does that improve
calibration or curriculum retention for an ePC student?

## Arms

1. Ordinary single-view KD/ePC.
2. Naive multi-view accumulation.
3. CMCP-weighted multi-view KD/ePC.
4. Oracle-deduplicated multi-view KD/ePC.

All arms share initialization, batches, optimizer updates, teacher packets,
and evaluation batches. The initial reduced run is calibration only; disjoint
confirmation thresholds will be frozen from it.

## Results

Three protocol revisions were retained. The final valid calibration used three
seeds (`101,211,307`), 80 Task-A plus 80 contradictory Task-B updates, a fixed
half-vocabulary label permutation for Task B, four matched arms, four teacher
packets per update, and two-step ePC settlement.

All arms received exactly 160 optimizer updates and 640 packet presentations.
All ePC energy traces were monotone. Mean results:

| Arm | Effective precision | A retention loss increase | B loss | B accuracy | B ECE |
|---|---:|---:|---:|---:|---:|
| ordinary | 1.0000 | 0.16394 | 2.30898 | 0.14887 | 0.01092 |
| naive | 4.0000 | 0.15676 | 2.33139 | 0.14931 | 0.00962 |
| CMCP | 1.3541 | 0.16250 | 2.31240 | 0.15148 | 0.00934 |
| oracle | 2.0000 | 0.16003 | 2.31836 | 0.14714 | 0.00468 |

**Observed:** CMCP removed most duplicate precision inflation and consistently
improved Task-B loss over naive accumulation, but it did not consistently
improve the retention/plasticity tradeoff over ordinary single-view KD/ePC.
It also undercounted the constructed independent view relative to oracle
(`1.3541` versus `2.0` effective precision).

**Decision:** do not unseal confirmation. This reduced bridge supports CMCP as
duplicate-accounting protection, not as a demonstrated transformer-to-ePC
distillation improvement. A next attempt would need an independently motivated
teacher-view novelty estimator and a stronger real-teacher substrate rather
than further tuning this toy outcome.

Artifacts: `artifacts/calibration-seed{101,211,307}-u160-contradictory-v4.json`.
SHA-256 values are recorded in the session log. Focused compatibility suite:
`37 passed`.

## Detailed report

For external review of weighting alternatives, a four-page, self-contained PDF
was generated from the final v4 JSON artifacts, runner, and implementation:
`cmcp_epc_distillation_report_2026-07-25.pdf` (SHA-256
`1428abac9001325a5c4313140bfb347aac02d66913a8ae33a6c9020ed13d6163`).
It separates measurements from interpretation and identifies the key
selection-versus-total-KD-mass confound. The LaTeX source is retained alongside
the PDF.
