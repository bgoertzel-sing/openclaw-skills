# Structural-memory rewrite

- Project: `hdc-musicgen`
- Started: `2026-07-25`
- Finished: `2026-07-25`
- Status: `complete-code-only`
- Local or remote: local CPU; no paid compute

## Question

Can the new structural-memory runbook be represented as an inspectable,
pure-logic-tested five-stage experiment while preserving the frozen backbone,
stratification, controls, alignment, and NLL choices?

## Inputs

- Authoritative inbound runbook:
  `media/inbound/openclaw-staged-a9864da8-a296-4fa2-a4c4-365d79017414/AGENT_RUNBOOK_hdc_musicgen_structural---05e8fab1-d7bb-4011-aaaf-4d6462a55db3.md`
- Repository branch: `agent/stagec-oracle-diagnostic`
- Starting commit: `eade7867d20ef888ef4ae6f5fa04a12aa4105965`
- Existing `hdc_musicgen_experiments.py` infrastructure
- Hardware: CPU only

## Planned commands

```sh
PYTHONPATH=src:. python -m pytest test_hdc_musicgen_structural.py -q
PYTHONPATH=src:. python -m pytest test_hdc_musicgen.py -q
python -m py_compile hdc_musicgen_structural.py test_hdc_musicgen_structural.py
git diff --check
```

## Relevant research rules

Rules 1, 2, 5, and 7: validate the structure classifier and metrics with
explicit tests; treat the runbook as the software specification; preserve
reproducible commands and results; keep pure experiment logic separate from
AudioCraft-dependent execution.

## Results

- Implementation commit:
  `f4506a7094aaf5f549f16f605a8ef0bf808653c0`.
- `PYTHONPATH=src:. python -m pytest ...` could not start because `python` is
  absent from PATH.
- The project `.venv/bin/python` exists but has no pytest installation.
- `PYTHONPATH=src:. python3 -m pytest test_hdc_musicgen_structural.py -q`:
  6 passed in 0.92 s.
- `PYTHONPATH=src:. python3 -m pytest test_hdc_musicgen.py -q`:
  7 passed in 0.87 s.
- `python3 -m py_compile hdc_musicgen_structural.py
  test_hdc_musicgen_structural.py`: passed.
- `git diff --check`: passed.
- Copied runbook comparison against the inbound source: byte-identical.

## Implemented artifacts

- `repos/hdc_musicgen_structural.py`
- `repos/test_hdc_musicgen_structural.py`
- `repos/AGENT_RUNBOOK_hdc_musicgen_structural.md`

The pure helpers cover cosine self-similarity and classification, four-way
condition construction and evaluation alignment, relevance gain, noiseless
self-test logic, summary gain, and oracle fraction. Runtime stages write
`stage0_persistence.json`, `codes_meta.json`, `stageS_spans.json`,
`stageS_summary.json`, `stageA_spans.json`, `stageA_summary.json`,
`stageC_resonator.json`, `stageD_spans.json`, `stageD_summary.json`, and a
refreshed `RESULTS.md`.

## Decisions and limitations

- Because the runbook does not freeze classification thresholds, RELATED uses
  cosine >=0.80, UNRELATED <=0.50, and ambiguous spans are omitted.
- Wrong-content controls come from eligible history older than the window,
  preventing future leakage while preserving exact block length.
- Smoke mode (`--limit`) records but does not enforce the 20-track Stage-0
  corpus gate; a full run fails closed.
- Stage C remains an optional feasibility footnote and uses the actual cold
  and previous-frame initializers at noiseless `snr99`.
- No AudioCraft/model-dependent execution occurred. Cross-attention plumbing,
  numerical NLL bands, corpus gates, and all scientific claims remain
  unvalidated locally.
