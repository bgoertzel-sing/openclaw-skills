# Run 20260807T012000Z-protocosmo2-full-pdf-ingestion

- Project: `omegaclaw`
- Date: `2026-08-06` PDT / `2026-08-07` UTC
- Status: `succeeded`
- Local or remote: `local`

## Question

Can ProtoCosmo2 ingest Ben's complete OmegaSelf PDF without silently cutting it
at 60,000 characters while retaining a finite extraction-expansion bound?

## Inputs

- PDF: staged Telegram attachment, 104 pages, 656,809 bytes
- Extractor: local `pdftotext`
- Runtime test commit: `b2069d6`

## Results

- Extracted length: exactly 160,374 Unicode characters.
- Exact preservation regression: passed.
- Expansion bound: 2,000,000 characters; bound+1 fails with
  `telegram_document_text_too_large` rather than truncating.
- Focused provider-free suite: 33 passed in 0.85 seconds.
- `py_compile`, live config validation, and `git diff --check`: passed.
- Supervisor: restarted and active as PID `1553729`, startup offset
  `387572236`.

## Reproduction

```bash
PYTHONPATH=projects/omegaclaw/worktrees/protocosmo2-phase6-live \
python3 -m pytest -q \
  projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary.py \
  projects/omegaclaw/worktrees/protocosmo2-phase6-live/provider_free_tests/test_private_canary_telegram.py
```

## Interpretation

The earlier response's “truncated” qualifier was caused by the adapter ceiling,
not the source document. The current adapter admits this document in full and
fails explicitly for pathological extraction expansion.
