# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.

## 2026-07-24 — Fable/Sol ladder

- Audited all 40,960 E0/E1 evaluation rows and found the deterministic defect.
- Implemented E2 fitness ablations and five generic E3 penalties; permutation
  invariance is the executable no-successor-encoding guard.
- Smoke: 3.67 s, 305 MB, 10/10 deterministic. Fixture: 74.23 s, 375 MB,
  25/25 deterministic. The 40-update fixture is not an efficacy result.
