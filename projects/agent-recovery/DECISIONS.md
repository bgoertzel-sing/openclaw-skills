# Decisions

## 2026-06-28: Use two separate private recovery repositories

**Decision:** Create separate disaster-recovery repositories for ZeroBot and Protomegabot rather than a single combined backup.

**Rationale:** The agents have different identities, runtimes, credentials, risk surfaces, and restoration paths. Keeping them separate reduces accidental context mixing and makes exclusion rules easier to audit.

**Constraints:** Repositories must be private unless Benjamin explicitly decides otherwise. Secrets and live credential stores are excluded.
