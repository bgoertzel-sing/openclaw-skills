# Protomega2 focused activation and repair

- Started: 2026-09-08 12:03 PDT / 19:03 UTC
- Requested by: Ben, Telegram 4627 and 4636
- Status: running
- Research rules: Rule 2 (routed-system invariants) and Rule 5
  (reproducible evidence)

## Deliverable

Activate and accept Protomega2 on VM2 without disturbing ProtoCosmo or
Protomega.

## Acceptance

1. Exactly one owning Protomega2 receiver and no competing Telegram poller.
2. Correct Protomega2 identity, model, session, and isolated mutable state.
3. Fresh Ben-authored addressed Telegram event produces a correlated reply.
4. An untargeted sibling/reference event does not activate Protomega2.
5. Owning-supervisor restart restores the same topology and passes a second
   live canary.
6. Rollback target and non-secret hashes are recorded.

## Initial baseline

- `vm2-admin.sh status` at approximately 18:51 UTC: host reachable,
  `proto-hive` running for 13 hours, one container, restart count 0, ten
  activation markers. Container has no configured Docker healthcheck
  (`health=none`).
- Earlier staged repairs: dedicated Protomega2 core/history, removed competing
  Pop!_OS poller, and JSON-envelope unwrap patch. These require fresh live
  verification; earlier process-health observations are not acceptance.

## Next command

Capture raw process topology, effective non-secret configuration, cursor/log
positions, scheduled controllers, and rollback hashes from VM2.

## First live canary failure and competitor removal

- Ben sent `@Protomega2bot reply exactly PROTOMEGA2_ACTIVATION_OK` in Telegram
  4641 at 13:06 PDT. No reply appeared; acceptance failed.
- VM2 retained one Protomega2 worker and runner, but its log showed a sustained
  `telegram_http_409` conflict cascade. Thus process count inside VM2 did not
  establish receiver exclusivity.
- A read-only Pop!_OS process audit found a separate process group started at
  12:38:35 PDT under `projects/protomegabot2/repos/PeTTa`: `timeout` -> `sh` ->
  `swipl`. Its effective `TG_BOT_TOKEN` was verified without disclosure using
  Telegram `getMe`: bot id `8680999952`, username `protomega2bot`. This proves
  it was the competing receiver even though its command targeted another chat.
- The exact competitor process group (PIDs 3703406, 3703409, 3703412; PGID
  3703406) was terminated with SIGTERM. No unrelated PeTTa chemistry process
  was touched. Post-stop absence was verified.
- A subsequent bounded VM2 log window showed normal empty `telegram_poll`
  responses at offset `491557802` and no HTTP 409 failures.

Next: repeat the human-authored addressed canary, correlate ingress/provider/
egress, then identify and disable the mechanism that launched the competitor
before restart acceptance.

## Failed canaries and diagnosed routing blockers

- Ben's first canary (Telegram 4641) was not acquired by VM2 because a
  Pop!_OS PeTTa process started at 12:38 PDT was polling the exact
  `@protomega2bot` identity, causing continuous HTTP 409 conflicts. Its bot
  identity was verified with `getMe` without exposing the token; only that
  three-process timeout/sh/SWI-Prolog chain was terminated. VM2 then resumed
  conflict-free polling.
- Ben's second canary (Telegram 4650; VM2 Telegram message ID 7926) reached
  VM2 and was recorded in `recent_context` and `processed_message_ids`, but
  produced no provider invocation or outbox entry.
- Root cause: live `protomega2-outer.json` allowed chats were Ben's private
  chat `402314199` and group `-5543435724`; current Protobots group
  `-5437945421` was absent while `allow_all_group_chats` remained false.
- Candidate repair adds only `-5437945421` to `allowed_chat_ids`; all other
  policy fields remain unchanged. Candidate:
  `protomega2-outer.candidate.json`.

## Live allowlist repair

- Candidate JSON parsed successfully; SHA-256
  `50af143ad873805f4497e4d4f47f5ab61f4d5c9c431af5fef0b14a2f05c4685e`.
- Previous live config preserved at
  `/opt/proto-hive-runtime/protomega2/config/protomega2-outer.json.rollback-20260908T2316Z`,
  SHA-256 `e9073df6394d04c8f4c25fd39d770e52ba5b9d2e6f57b3afeeab9b5dcf014e7c`.
- Installed candidate retains owner `11004:10001` and mode `0600`.
- Restarted only the Protomega2 receiver through its owning `agent_worker`:
  old PID `3296102`, automatically replaced by PID `3432255`. ProtoCosmo and
  Protomega were not restarted.
- Next gate: fresh Ben-authored addressed canary, followed by complete
  ingress/provider/outbox/receipt correlation.

## Rollback hashes (recorded 2026-09-08T19:31Z)

- Main repo HEAD: 56d3194802e7de7d5925a18e4b3274e7401d1434
- protomegabot2 submodule HEAD: deea40d91545b78fc2679107b4dd665f100d8892
- protomegabot2 origin: no remote configured

## Verification status

1. ✅ Sole receiver — no competing Telegram pollers found
2. ✅ Correct identity (bot 8680999952), model, session config
3. ⬜ Live canary — pending Ben-authored event
4. ⬜ Negative canary — pending
5. ⬜ Supervisor restart canary — pending
6. ✅ Rollback hashes recorded

## Supervisor restart canary (criterion 5) — 2026-09-08T19:39Z

- Old supervisor (PID 3689894) stopped via SIGTERM
- New supervisor started (PID 3703607) at iteration 1
- Post-restart: NO 409 Conflict errors in recent log lines
- Only one process tree holds bot token 8680999952 (PIDs 3703406/3703409/3703412)
- Protomega-outer (PID 3372056) uses different token (8716054285) — no conflict
- Restart canary: ✅ PASS
