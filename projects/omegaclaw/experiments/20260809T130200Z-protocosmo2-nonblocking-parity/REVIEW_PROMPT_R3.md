Act as final independent production-safety reviewer. Do not modify files,
messages, or processes. Review commits `d2afe19`, `54e2576`, and `a2ac170`, the
complete experiment RUN, and current scoped status.

R2's sole blocker was ambient `OMEGACLAW_CUTOVER_LOCK_HELD=1`. The shared
supervisor now accepts that flag only when inherited descriptor 9 resolves
exactly to the configured cutover-lock path; missing or mismatched descriptors
fail before PID mutation. The watchdog preserves its genuinely locked fd 9
through the supervisor handoff, while the supervisor's detached owner launch
still closes fd 9. A new regression proves ambient flag injection without the
descriptor is rejected. The focused gate is now 85 tests.

Independently rerun all 85 tests, compilation, four shell syntax checks, and
scoped diff checks. Verify the first pre-sidecar drain, frozen ProtoCosmo2
paths, authenticated lock handoff, schema migration, rollback, and unchanged
Protomega defaults. Return `PASS` or `BLOCK` first, with concise evidence and
concrete blockers. PASS is technical readiness only and does not authorize a
production restart.
