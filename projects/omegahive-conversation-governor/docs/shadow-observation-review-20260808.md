# B6 Shadow-observation review — 2026-08-08

## Scope and evidence

- Decision gate: `D-20260806-shadow-deployment-approved`.
- Ledger: `plugins/conversation-governor/ledger/decisions.jsonl`.
- Review window: append timestamps from `2026-08-07T06:20:00Z` through the
  last available record at `2026-08-08T06:14:18.154Z`.
- Observed records: 200 total — 45 admission and 155 egress.
- The B5 synthetic validation admission at `2026-08-07T06:48:59.006Z` is
  included. Most real observations began immediately afterward.

This is counterfactual policy review only. The plugin remained in shadow mode;
no ledger recommendation suppressed inference or delivery.

## Recommendations by class

| Layer | Recommendation class | Count | Review | Concrete concern |
|---|---|---:|---|---|
| Admission | `ADMIT / DEFAULT_ALLOW` | 44 | **Flag** | The class is safe as a fail-open default, but it is much too permissive to count as policy success. Thirty-six identical `DO NOT RE-SEND OR SPAM!` payloads, each under a changing synthetic channel ID, were all admitted. This is a concrete false-negative noise-suppression failure: obvious repeated traffic would still invoke agents. |
| Admission | `DROP / DUPLICATE_MESSAGE_ID` | 1 | **Reject for enforcement** | This was a false positive. The dropped record had `message_id="unknown"`; its event ID collided with two different messages in the same channel, with three distinct content hashes. Enforcing this recommendation would silence a legitimate, different human message. |
| Egress | `SEND / DEFAULT_SEND` | 155 | **Flag** | Ordinary substantive replies should remain sendable, so fail-open behavior is appropriate. But the class contains many operational failure narrations (`Bash failed`) and other likely noise, while producing zero suppress recommendations. Treating all 155 as endorsed would hide false negatives. The newly added watchdog-noise classifier was not evidenced by this live window, and cron/direct-post traffic may bypass this hook entirely. |

No other admission or egress recommendation class appeared. In particular,
there were no observed sibling, loopback, structured-silence, watchdog-noise,
or other egress suppression recommendations to endorse from live evidence.

## Data-quality findings

1. **Ingress identity is not enforcement-safe.** Forty-four of 45 admission
   records have `message_id="unknown"`. The adapter's fallback event identity
   can therefore collapse unrelated messages, as the false duplicate proves.
2. **Event identity is inconsistent across transport shapes.** One event ID
   appeared three times for three different contents; another appeared twice
   for identical content while both observations were admitted. Event ID alone
   is neither a reliable duplicate key nor a reliable observation key here.
3. **Content-level repetition is missed across synthetic session channels.**
   The 36-message identical burst used 36 changing channel IDs, defeating the
   present duplicate rule. A bounded provenance-aware repetition key is needed;
   raw global content deduplication would risk suppressing legitimate repeated
   commands in different conversations.
4. **Coverage is asymmetric.** The ledger proves the conversation hook is live,
   but it does not prove coverage of cron `announce` or other direct-post paths
   (B7), and it recorded no live examples for most intended suppression classes.

## Gate verdict

**B6 review complete; active admission or egress suppression is not approved.**

The observations make sense only as fail-open shadow telemetry. Before any
enforcement gate, the adapter must propagate stable transport message/update
identity (or decline duplicate suppression when it is absent), deduplication
must be tested against both unrelated same-channel messages and repeated
cross-session payloads, and B7 must establish direct-post coverage. The fixed
identity logic should then receive another shadow/replay window with labeled
examples of every suppression class intended for activation.

## Reproduction queries

Counts were obtained with `jq` over the append timestamps and grouped by
`data.decision.{decision,reason_codes}` for admission and
`data.{egress_decision,egress_reason}` for egress. Duplicate/event-identity
checks grouped admission records by `data.envelope.event_id` and separately by
`data.envelope.content.content_hash`.
