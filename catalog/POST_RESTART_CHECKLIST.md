# Post-Restart Checklist

Run this checklist after every OpenClaw gateway restart to catch silent
failures, lost jobs, or stale state.

## How to detect a restart

Check the gateway process start time. If it is younger than ~15 minutes,
treat the gateway as recently restarted.

```bash
ps -eo lstart,comm,args | grep openclaw-gateway | grep -v grep
```

## Checklist

1. **Cron job integrity**
   - `cron action=list` with `includeDisabled=true`
   - Compare against the known-expected job set
   - Flag any missing jobs, newly disabled jobs, or unexpected new jobs

2. **Error-state jobs**
   - Surface any job with `lastRunStatus: "error"`
   - Include the error message and last run time

3. **Disabled jobs audit**
   - List all disabled jobs
   - Confirm each is intentionally disabled (not disabled by a crash)

4. **Session connectivity**
   - `sessions_list` to verify active sessions are reachable
   - Flag any sessions in an error or stuck state

5. **Uncommitted work**
   - Scan project repos under `projects/*/repos/` for uncommitted changes
   - Flag anything older than 1 day

6. **Experiment integrity**
   - Scan `projects/*/experiments/` for directories missing `RUN.md`
     conclusions or exit status

7. **Heartbeat sensor**
   - Run `python3 bin/runpod-heartbeat-sensor.py` if any RunPod pods
     are expected to be active
   - Report any `unreachable_confirmed=true` or unexpected states

8. **Memory/catalog consistency**
   - Check `catalog/PROJECTS.md` for stale entries
   - Check for contradictions between MEMORY.md and project records

## Delivery

Results should be posted to the scheduled-updates channel
(`telegram:-1003983157420`) as a concise summary. Only flag items that
need attention; silent-pass items get a one-line "all clear" per section.
