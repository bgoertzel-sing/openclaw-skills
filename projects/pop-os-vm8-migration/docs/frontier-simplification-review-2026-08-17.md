# Frontier Review: Simplifying the Remaining VM2 Migration

Date: 2026-08-17
Scope: Independent read-only review of the remaining VM2 test, deployment,
cutover, restart, reboot, rollback, and acceptance procedure.

## Conclusion

The disposable end-to-end Test-provider case has become an artificial blocker
and should be retired as a cutover gate. Its useful components already pass:
the mock channel initializes, ping/inject/receive works, the deterministic
provider initializes, and it returns the expected send action. The remaining
timeout is caused by the modified disposable MeTTa loop, not evidence of a
production failure.

More importantly, the accepted container is still offline-only:
`context/agent_worker.py` exits live mode with `live launcher not frozen`, and
`context/compose.yaml` fixes the container to offline mode, no restart, no
network, and polling disabled. The documented real launch commands have not
yet been wired into the container. Repaired laptop deltas also require one
final freeze and synchronization. Those are the real pre-cutover gates.

## Keep these safety gates

1. Freeze repaired laptop commits/dirty state, launcher/config hashes, mutable
   state timestamp, and cursors; synchronize the required deltas once.
2. Wire the four real launch paths behind fail-closed per-identity activation
   markers. With no markers, the container must produce zero pollers.
3. Build the final image once; verify config, executable startup, health, UID
   and secret isolation, clean removal, and one final inert audit.
4. Cut over one identity at a time: capture laptop baseline, stop it, prove
   zero receivers, transfer the final state delta, activate only VM2, and
   prove exactly one receiver.
5. Require fresh external Telegram text canaries with correlated ingress,
   invocation/action, and egress evidence. Test one safe attachment per
   runtime family unless identity configuration materially differs.
6. Verify container restart, VM reboot, rollback, and operator handover.
7. Keep the laptop stopped but rollback-ready during a short monitored soak.

## Retire or collapse

- Retire the disposable Test-provider end-to-end loop as a migration blocker.
- Do not repeat it separately for all three Omegas.
- Stop rebuilding or retransmitting the 1.7 GB image for harness-only edits.
- Stop five-minute inert-audit/process-tree narration; audit before activation
  and after cleanup or failure.
- Run shared backup/restore and secret-isolation mechanisms once, not after
  every unrelated edit.
- Treat soak as post-functional observation rather than active migration work.

## Shortest safe path

1. Reconcile repaired source truth: 30--60 minutes.
2. Wire production launchers and fail-closed markers: 45--90 minutes.
3. Perform one final build and relevant offline checks: 30--60 minutes.
4. Cut over and canary each identity: 20--40 minutes each, rolling back the
   current identity immediately before touching another if a canary fails.
5. Test attachment coverage, restart, reboot, and handover: 45--90 minutes.

Estimated active time to functional four-bot migration: 3--5 hours if the
documented commands work, plus 1--3 hours if real launcher wiring exposes a
genuine defect. A 6--24-hour soak follows functional completion.

## Important architecture caution

The one-container architecture enlarges the failure domain. Per-identity
cutover is valid only if the supervisor treats unmarked identities as
intentionally idle and does not kill already accepted identities when another
child is absent or fails. If it cannot do that, use one coordinated cutover or
split services; do not claim per-identity rollback that the supervisor cannot
provide.

## Stale-record findings

- `PROJECT.md` still contains superseded VM1/VM8 and VM2-exclusion language.
- The earlier PDF recommends four services, superseded by the accepted
  one-container decision, while some rollback text still assumes services.
- `TASKS.md` mixes stale VM1 and current VM2 obligations.
- Reports call real launch commands frozen, but they are documented rather
  than wired into the live container.
- The current Compose file cannot yet satisfy live, restart, or reboot
  acceptance despite reports implying only the synthetic test remains.

## Recommended decision

Retire the synthetic Test-provider gate now. Make repaired-delta
synchronization and production-launcher wiring the actual pre-cutover gates,
then proceed through exclusive receiver cutover, genuine external canaries,
restart/reboot, rollback, and soak.
