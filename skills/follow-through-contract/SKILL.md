---
name: "follow-through-contract"
description: "\"Enforce durable follow-through on promised deliverables across session handoffs and model switches.\""
---

# Follow-Through Contract

Use whenever the agent promises a concrete deliverable, accepts a task, or says "I'm on it" / "I'll do that" / "working on it."

## Rules

1. **Before saying "I'm on it" or equivalent:** create or update a durable task entry (in the relevant project `TASKS.md` or a dedicated obligation ledger) with: deliverable name, acceptance test, exact next command, and completion-evidence path. No commitment without a task record.

2. **"Working on it" is permitted only after** a process, test run, or file write has actually started — not after inspection, planning, or reading code. If only inspection happened, say "inspecting" or "reading," not "working on it."

3. **At each session resume or model handoff:** reload the open-obligation list from `TASKS.md` / obligation ledger. Either resume the oldest incomplete promise or explicitly report that it remains incomplete. Never silently drop a commitment.

4. **Before any status reply to the user:** run an obligation audit — promised vs. evidence (artifact, test result, commit). If there is no evidence, say "not done," never "nearly ready" or "in progress" without an active process.

5. **A task is complete only when** the acceptance test passes and a durable record exists (experiment dir, commit, or updated project file). Then close the task entry and send the result with evidence.

6. **If blocked:** report the blocker and what was attempted. Do not rephrase a stall as progress.

## Quick self-check before any reply

- Did I promise something in a prior turn? Is there evidence it was done?
- If no evidence: "not done" — then do it or say what blocks it.
- Never let a promise age past one session without either completion evidence or an explicit "still incomplete" report.
