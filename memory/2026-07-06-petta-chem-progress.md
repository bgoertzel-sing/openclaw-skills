# 2026-07-06 petta-chem progress

## 20:30 PDT / 2026-07-07 03:30 UTC — Cap-4 rich bridge extended to seed-17

Dedicated petta-chem worker pushed commit `fa9a89f` extending the cap-4 rich bridge from seed-13 to seed-17 in `projects/petta-chem/repos/petta-chem`. Added S-family 12-molecule chamber tick clauses and seed-17 bridge/run-record atoms; random-polymer now fires all four cap-4 generated rules for 12 productive events, shuffled-catalysts records 8 events, and no-catalysis stays at 0. Added exp03 smoke coverage for counts, abundances, replay, discrimination, completeness, and trace events. Verification: `scripts/run_exp00.sh`, `scripts/run_exp03.sh`, `git diff --check`, and obvious secret-like scan passed. Remaining task: seed-7 and seed-11 cap-4 rich variants.


## 22:30 PDT / 2026-07-07 05:30 UTC — Cap-4 rich bridge extended to seed-11

Dedicated petta-chem worker extended the cap-4 rich bridge to seed-11/Q-family six-rule source pools. Added six-candidate cap support and 12-molecule/six-rule candidate generation in exp00, Q-family rich chamber tick clauses in exp03, and seed-11 cap-4 run-record atoms/tests. Commit `db187ab` pushed to GitHub `main` after checks: `scripts/run_exp03.sh`, `scripts/run_exp00.sh`, `git diff --check`, and obvious secret-like scan. Remaining cap-4 rich gap: seed-7/P-family.
