# Decision Log

## D-20260731-runpod-ssh-launch: Keep explicit ports without claiming a proven fix

- Date: `2026-07-31`
- Status: `accepted`
- Decision owner: operational research record
- Related run: `experiments/20260731T145013Z-runpodctl-payload-inspection/`

### Decision

Use the pinned official template with explicit `--ssh` and every required
port, including `22/tcp`, for canonical direct-SSH launches. Treat explicit
`--ssh` as defensive documentation in runpodctl 2.8.0, where it defaults true.
Do not claim that explicit `22/tcp` fixes the observed readiness failures.

### Rationale and evidence

Installed-binary loopback capture showed that omitted ports remove the
GraphQL `ports` field, whereas omitted `--ssh` still sends `startSsh:true`.
Archived exact commands show both failed and successful launches with
`22/tcp`, so port publication is necessary launch hygiene but not a sufficient
causal account. Use bounded readiness validation and retain launch responses.

### Revisit trigger

Provider documentation or telemetry that explains the relationship between
`startSsh`, port publication, container uptime, and endpoint allocation; or a
controlled same-placement failure reproduction.

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
