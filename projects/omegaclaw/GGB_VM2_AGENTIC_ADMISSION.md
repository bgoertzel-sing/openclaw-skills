# VM2 agentic-work admission gate

- Date: 2026-08-17
- Effect: none; evidence review only
- Purpose: make the `TASKS.md` post-VM2 prerequisite falsifiable without
  inspecting or changing a live runtime.

## Current pre-admission ledger

- Assessed: `2026-08-17 23:30 UTC` from project records only.
- Verdict: **not ready**.
- Target set: **unresolved**. The accepted transport baseline names
  `ProtoCosmo2`, `Protomega`, and `Protomega2`, but this gate must not infer
  that those are exactly the bots covered by the post-VM2 directive.
- Port-complete report from runtime owner: **absent from inspected records**.
- Complete digest-bound manifest: **absent**.
- Per-target VM2 deployment, post-deployment private-turn, single-owner,
  mutable-state/rollback, and explicit owner-acceptance evidence: **not
  assessed because no complete manifest exists**.

The next state transition requires one runtime-owner report that (a) names the
complete target set and (b) states that every named target has actually been
ported to VM2. Until then, absence is a negative gate result, not a request to
inspect production. This ledger does not authorize contacting the owner,
collecting live evidence, or creating a synthetic passing manifest.

## Admission predicate

Agentic work is admitted only when one immutable manifest covers every target
bot and all checks below are true. Missing or `unknown` values mean **not ready**;
they must never be inferred from a bot name, deployment slot, PID, or historical
capture.

For each target bot, the manifest must bind:

1. deployment slot and declared runtime identity as separate fields;
2. source commit and configuration fingerprint, excluding secrets;
3. canonical VM2 host/deployment evidence ID and SHA-256 digest;
4. one successful post-deployment private-turn evidence ID and digest;
5. receiver ownership showing exactly one accepted owner at capture time;
6. mutable-state location/fingerprint and rollback identity;
7. explicit acceptance by the runtime owner, with source-message ID and time;
8. capture time in canonical UTC and an evidence freshness policy.

Global checks:

- the target set is explicit and complete;
- evidence IDs and canonical evidence paths are unique across identities;
- every referenced digest reproduces from a regular, non-symlink local file;
- source/config, routing, receiver, or mutable-state drift after acceptance
  returns the gate to **not ready**;
- acceptance wording covers VM2 deployment only and grants no Iter,
  GoalChainer, memory-write, task-claim, provider, Telegram, or ThreadKeeper
  authority.

## Negative fixtures required before acceptance

A future executable validator must reject at least: omitted target; duplicate
identity or evidence ID; slot/runtime conflation; `unknown` runtime identity;
digest drift; pre-deployment turn evidence; zero or multiple owners; stale
capture; missing rollback identity; secret-like manifest fields; symlinked
evidence; and acceptance text widened into agentic/runtime authority.

## Next small task

Do not implement the validator or collect new live evidence until all target
bots have actually been ported. When the runtime owner reports that condition,
freeze a JSON schema and synthetic positive/negative fixtures first. Only then
encode the owner's existing secret-free evidence into a candidate manifest.
Passing this gate authorizes drafting the provider-free, effect-none
Protomega2 Iter contract described in `GGB_ACTIVE_FRONTIER.md`; it does not
authorize executing or staging that contract.

## Static checks

```sh
test -f projects/omegaclaw/GGB_VM2_AGENTIC_ADMISSION.md
rg -q 'Missing or `unknown` values mean \*\*not ready\*\*' projects/omegaclaw/GGB_VM2_AGENTIC_ADMISSION.md
rg -q 'Verdict: \*\*not ready\*\*' projects/omegaclaw/GGB_VM2_AGENTIC_ADMISSION.md
rg -q 'Target set: \*\*unresolved\*\*' projects/omegaclaw/GGB_VM2_AGENTIC_ADMISSION.md
rg -q 'grants no Iter' projects/omegaclaw/GGB_VM2_AGENTIC_ADMISSION.md
git diff --check -- projects/omegaclaw/GGB_VM2_AGENTIC_ADMISSION.md
```
