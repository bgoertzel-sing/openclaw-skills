# Run 20260718T024500Z: A6 stratified CLA re-sweep 06

- Started/finished: `2026-07-18T02:46:21Z`
- Status: `failed before simulation measurement`

The fresh-ledger wrapper passed repository identity checks and the focused test suite, then failed when `ProcessPoolExecutor` could not pickle the dynamically loaded `task` function (`import of module 'prepared_batch05' failed`). No simulation result artifacts were written and this directory is not counted as grid coverage. The recovery registered the unchanged prepared module and ran it in the new batch-07 ledger; neither detector nor experimental design changed.
