# Notes

- Benjamin requested a GitHub-backed disaster-recovery repository for ZeroBot/OpenClaw context and daily updates on 2026-06-28.
- Benjamin then clarified that Protomegabot should have the same treatment, separately from ZeroBot.
- Current proposed hostnames for future multi-machine Tailscale work: `claws1-pop`, `codex1-mac`, `ben1-mac`.

## 2026-08-03: Restore drill and alert-route verification

- The delayed first monthly drill report exists at
  `drill-reports/2026-08-02.md`; both repositories passed all five checklist
  checks. Four portability/documentation findings are non-blocking follow-ups.
- Live inspection of daily backup cron
  `5ae59dd5-dfe3-4ace-999d-a08ca153325e` showed `delivery.mode=none` for quiet
  successful runs and an independent `failureAlert` to ProtoBots-updates after
  one error, with a 24-hour cooldown. `lastFailureNotificationDeliveryStatus`
  was `not-requested` because the latest run succeeded. No synthetic failure
  was introduced to exercise Telegram delivery.
