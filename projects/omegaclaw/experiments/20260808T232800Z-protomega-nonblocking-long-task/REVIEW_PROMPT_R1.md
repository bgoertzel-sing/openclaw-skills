Act as an independent production-safety reviewer. Inspect the current uncommitted diff and source in:

- /home/openclaw/research-agent/projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary.py
- /home/openclaw/research-agent/projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary_telegram.py
- /home/openclaw/research-agent/projects/omegaclaw/protocosmo2/tools/phase6_private_canary_runner.py
- the corresponding provider_free_tests/test_private_canary*.py

The intended repair is: Telegram mobile users may forward a PDF and then reply to that exact PDF with instructions; same-user reply binding must extract the exact replied document, durably queue the long job outside the polling loop, preserve immutable source chat/message routing across restart, allow an interleaved short message, deliver a later final result, and never leak raw `(send ...)` action wrappers. Exact single wrappers may be unwrapped; malformed or multiple send-shaped actions must fail closed. Production must remain untouched during staging.

Run the narrow provider-free tests and diff checks yourself. Review for lost jobs, cross-user/cross-chat document confusion, unsafe replay after crash, duplicate delivery, queue/rate-limit inconsistencies, oversized state/prompt issues, and malformed wrapper leakage. Do not modify files. Return exactly one verdict line `PASS` or `BLOCK`, followed by concise evidence and any concrete blockers. A PASS means safe to proceed to a fresh external staging canary, not authorization to deploy production.
