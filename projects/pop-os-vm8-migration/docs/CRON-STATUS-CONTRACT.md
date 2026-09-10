# Migration cron status contract

Only the independent status reporter posts routine scheduled updates to the
migration group. The implementation worker records evidence and returns a
structured summary, but does not independently announce it, preventing paired
or contradictory messages.

Every worker summary must use this compact structure:

```text
===MIGRATION UPDATE===
<plain-language headline describing the meaningful result>

PDF map (amended): Phase <n> / Gate <n> — <passed, partial, open, or not started>.
Changed: <new verified evidence, or "No material evidence changed this cycle.">
Blocker: <none or exact blocker>.
Next: <one concrete critical-path action>.
Safety: laptop agents live; VM1 clone polling disabled; VM2 out of scope.
```

The PDF is amended by `D-20260812-vm1-complete-deployment` (all four agents on
VM1) and `D-20260813-independent-branch-clone` (VM1 is a new branch, so strict
cursor-preserving cutover and laptop shutdown no longer apply).

Do not repeat file/byte counts unless they changed or are directly relevant to
a newly passed gate. Do not narrate commands, wrappers, bookkeeping, delivery
targets, or unchanged historical failures.
