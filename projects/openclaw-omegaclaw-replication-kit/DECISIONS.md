# Decision Log

## D-20260713-sanitized-overlay: Ship a sanitized recipe and pinned overlay, not machine state

- Date: `2026-07-13`
- Status: accepted
- Decision owner: Benjamin Goertzel
- Related task/run/commit: workspace commit `9b2db98`; v1.0.0 artifact

### Context

The working installation contains credentials, personal memory, live chat/session state, private projects/data, hard-coded paths/IDs, cloned repositories, caches, databases, and generated artifacts. Copying it would be unsafe, non-portable, and difficult to audit.

### Decision

Distribute an operator-driven kit containing generic prompts/policies, reusable skills/templates, pinned public dependency instructions, a sanitized OmegaClaw patch, parameterized scripts/configuration, declarative schedules, validation, and manifests. Recipients generate new credentials and identity/chat state locally.

### Alternatives considered

- Clone the entire workstation or `~/.openclaw` state.
- Export only prose documentation without executable support files.
- Publish a fully unattended installer immediately.

### Rationale and evidence

The sanitized overlay preserves reproducible behavior while excluding secrets and recipient-specific data. Shell/Python/plugin/patch/test/schedule/backup/secret/archive checks passed. A manual first release keeps configuration and permission decisions visible.

### Consequences

Fresh-host testing remains necessary. The Omega patch is larger than an ideal focused upstream series and should later be split into reviewable PRs. Credentials, models, databases, and project repositories are not restored by this kit.

### Revisit trigger

After at least one independent fresh-host deployment and any upstream OpenClaw/OmegaClaw version change.
