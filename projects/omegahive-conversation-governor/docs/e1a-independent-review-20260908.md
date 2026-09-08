# E1a Independent Code Review — 2026-09-08

## Scope

Reviewed uncommitted changes to plugins/conversation-governor/ implementing
E1a narrow deterministic egress activation, against acceptance criteria in
TASKS.md and the proposal in docs/narrow-activation-proposal-20260812.md.

## Files Reviewed

- core.js — egress classification, hook application, enforcement recording
- index.js — plugin registration, hook wiring, config defaults, error handling
- test/governor.test.js — 14 focused tests
- openclaw.plugin.json — config schema with mode enum
- ledger.js — append-only JSONL with 0o600 permissions

## Acceptance Criteria Checklist

### Focused tests (all pass, 14/14)

1. Allowlisted cancellation: NO_REPLY in active mode returns {cancel: true}
2. All other egress pass-through: substrings, normal watchdog alerts sent
3. Shadow compatibility: shadow mode never cancels or mutates payload
4. Fail-open exceptions: unsupported mode throws; both hooks catch and return undefined
5. Truthful active ledger mode: mode field reflects actual mode; enforcement_applied distinguishes shadow from active

### Independent review

No unresolved blocker. See findings below.

### Production canary (requires operator attendance — not yet executed)

- [ ] One production suppression canary durably correlated
- [ ] Normal control message delivered unchanged
- [ ] Exactly one gateway active
- [ ] Rollback recorded

## Code Review Findings

### 1. Egress classification is narrow and correct

Only two classes produce SUPPRESS:
- Exact text NO_REPLY or NO_RESPONSE (after .trim())
- Regex match for WATCHDOG_ALERT or the Telegram-rendered form followed by
  "attachment promise not fulfilled"

All other content is SEND. The regex uses \b word boundary and is
case-insensitive. Substrings of NO_REPLY within longer text are not matched
because EXACT_SILENCE.has(text) requires exact equality after trim.

NO BLOCKER.

### 2. Admission remains shadow-only

admissionEnforcementMode() always returns "shadow". The message_received hook
calls applyAdmissionToHook(decision, admissionEnforcementMode()) regardless
of config.mode. Admission filtering is observation-only even when egress is
active.

NO BLOCKER.

### 3. Fail-open on all error paths

Both message_received and message_sending hooks in index.js wrap their logic
in try/catch blocks that log a warning and return undefined (no cancellation).
A ledger write failure, classification error, or schema validation error does
not suppress messages.

NO BLOCKER.

### 4. Default mode is shadow

configOf() defaults mode to "shadow" when not specified. The plugin config
schema allows "shadow" or "active". No environment variable or fallback
enables active mode without explicit configuration.

NO BLOCKER.

### 5. Ledger integrity

appendLedgerRecord creates the directory with 0o700 and the file with 0o600.
Each record includes schema_version, record_id (deterministic SHA-256),
timestamp, kind, and data. recordEgressEnforcement adds enforcement_applied
which truthfully records whether cancellation was applied, preventing a
shadow record from being misread as an active suppression.

NO BLOCKER.

### 6. Deterministic IDs

deterministicId uses SHA-256 over a stable (sorted-key) JSON canonicalization.
The egress event ID incorporates channel, account, conversation, session, and
content — making each outbound decision uniquely identifiable.

NO BLOCKER.

## Minor Observations (not blockers)

1. UNSTABLE_ID_VALUES correctly prevents sentinel values from triggering
   duplicate-drop recommendations in admission.
2. message_sending hook uses content field from event, supporting both
   interactive replies and direct-post deliveries through the common seam.
3. The 0o600 file permissions on the ledger protect conversation privacy.

## Conclusion

The E1a implementation passes all provider-free focused tests and has no
unresolved blocker in this independent review. The code is ready for the
attended production canary, which requires operator presence to:
- Deploy in active mode
- Send a watchdog-form suppression canary
- Send a normal control message
- Verify exactly one gateway
- Record rollback readiness
