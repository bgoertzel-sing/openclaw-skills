# Working Notes

Use this file for provisional project notes. Add dates and source pointers. Promote durable decisions, results, or tasks to their dedicated files.
# 2026-07-29

## Local non-SSH transport validation

- **Observed:** branch `agent/transport-probe` commit `9192df1` adds a
  self-starting no-science probe. Locally, its public source download matched
  the release SHA-256 and produced a verified compact archive. The official
  RunPod CLI v2.7.2 download matched its pinned SHA-256. A Croc `send`/`receive`
  round trip preserved the README SHA-256 without SSH.
- **Limitation:** this does not establish RunPod container startup-command
  semantics. The next test must be a separately approved, short-lived remote
  probe with no scientific workload.
