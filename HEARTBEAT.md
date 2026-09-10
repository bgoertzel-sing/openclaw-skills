# Heartbeat Checklist

Keep heartbeat work brief, read-only where possible, and free of paid actions.

1. Check remote jobs with the deterministic sensor first:
   `python3 /home/openclaw/research-agent/bin/runpod-heartbeat-sensor.py`.
   Treat its JSON as evidence, using these invariants:
   - `provider_uptime_seconds_advisory` is never readiness or activity evidence;
     RunPod is observed returning zero for healthy, SSH-reachable training pods.
   - `ready_active` means the pod is working. Do not emit a stalled/unready/cost
     alarm for it, even when provider uptime is zero.
   - `ready_idle` means reachable and currently idle, not “never started.” Check
     the experiment log/artifacts and job record before reporting completion or
     overdue cleanup.
   - `unreachable` is provisional. Alert only when
     `unreachable_confirmed=true` (three observations spanning at least 15
     minutes), and state exactly that SSH is unreachable; never claim “no work
     performed” without artifact/process evidence.
   - Never start, stop, or delete any paid resource from heartbeat. Heartbeat is
     observational and may alert Ben; cleanup requires an operator turn. This
     prohibition applies regardless of approval status.
   - Estimate elapsed time/cost from `createdAt` and `costPerHr`, not
     `uptimeSeconds`.
2. Check active project records for an explicitly time-sensitive open loop.
3. Notice uncommitted work older than one day and record a reminder; do not commit or discard it automatically.
4. Notice experiment directories missing `RUN.md` conclusions or exit status.
5. Notice stale catalog entries or memory contradictions and queue them for review.
6. If there is nothing actionable, do nothing.

Do not send repetitive status messages. Alert Benjamin only for material failure, unexpected cost exposure, security risk, completed requested work, or a genuinely blocking decision.
