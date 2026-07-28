# Decision Log

## D-20260727-telegram-network-gate: Gate gateway startup on stable Telegram connectivity

- Date: `2026-07-27`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `TASKS.md`; boot journal for `openclaw-agent.service`

### Context

At boot, `NetworkManager-wait-online.service` exited successfully at 00:15:33,
but OpenClaw subsequently saw Telegram DNS failure and then
`ENETUNREACH 149.154.167.220:443`. The gateway crashed three times, after which
its restart-loop breaker suppressed channel autostart.

### Decision

Add a systemd `ExecStartPre` gate that requires three consecutive successful
IPv4 DNS-and-HTTPS probes to `api.telegram.org` before launching the gateway.
Allow up to five minutes for connectivity and six minutes for systemd startup.

### Alternatives considered

- Rely only on `After=network-online.target`: already present and insufficient.
- Add a fixed boot delay: simple, but neither detects slow networking nor avoids
  needless delay when networking is ready.
- Modify OpenClaw's Telegram provider to contain startup network errors: more
  robust upstream work, but broader and slower than the host-level prevention.

### Rationale and evidence

The gate tests the actual dependency that caused the crash. Failures occur
before OpenClaw launches, so they cannot increment OpenClaw's own unclean-boot
counter. Consecutive successes reduce the chance of launching during a
transient route/DNS transition.

### Consequences

OpenClaw startup now depends on Telegram API reachability. During a Telegram
outage, startup waits up to five minutes and systemd retries rather than
starting other channels immediately.

### Revisit trigger

Replace or remove this host-level gate if OpenClaw changes Telegram startup
errors from process-fatal to locally retryable.

### Supersedes or superseded by

None.

## D-<YYYYMMDD>-<short-slug>: <Decision title>

- Date: `<YYYY-MM-DD>`
- Status: `proposed | accepted | superseded | rejected`
- Decision owner: Benjamin Goertzel or delegated role
- Related task/run/commit: `<pointer>`

### Context

### Decision

### Alternatives considered

### Rationale and evidence

### Consequences

### Revisit trigger

### Supersedes or superseded by
