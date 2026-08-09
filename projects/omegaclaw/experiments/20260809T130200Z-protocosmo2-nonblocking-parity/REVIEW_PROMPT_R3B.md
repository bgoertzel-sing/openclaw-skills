Independent final production-safety review; read-only. Review commits
`54e2576..a2ac170` plus the current ProtoCosmo2 wrapper and shared supervisor.
R2's only blocker was ambient `OMEGACLAW_CUTOVER_LOCK_HELD=1`. Verify that the
new fd-9 exact-path authentication closes it, watchdog handoff retains a real
locked fd, detached owner closes it, frozen ProtoCosmo2 paths remain isolated,
and the pre-sidecar drain remains fail-closed. Run only the focused 85-test
command documented in the experiment RUN, compilation, four `bash -n` checks,
and scoped `git diff --check`. Do not use memory or modify anything. Return
`PASS` or `BLOCK` first. PASS does not authorize restart.
