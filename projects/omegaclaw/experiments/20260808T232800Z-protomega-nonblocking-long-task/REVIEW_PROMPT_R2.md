Act as an independent production-safety reviewer. Do not modify files or send
messages. Inspect the current source/diff and evidence for the Protomega
non-blocking long-document repair:

- projects/omegaclaw/protocosmo2/tools/phase5_omegaclaw_case.py
- projects/omegaclaw/protocosmo2/tools/phase6_private_canary_runner.py
- projects/omegaclaw/protocosmo2/tests/test_live_runtime_prompt.py
- projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary.py
- projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary_telegram.py
- projects/omegaclaw/experiments/20260808T232800Z-protomega-nonblocking-long-task/RUN.md

The R2 staging failure was reproduced as Linux E2BIG: the 656,809-byte source
PDF extracts to 161,305 bytes and was previously passed as one `--prompt` argv
element. The repair uses a create-exclusive 0600 temporary prompt file,
requires the driver to accept exactly one prompt source, validates the file as
private/single-link/non-symlink/regular, and unlinks it on all responder paths.
R3 externally passed: source 118, ack 119, Anthropic Claude Opus 4.6 session,
durable final result, Telegram receipt 120, clean rendering. Production was not
restarted.

Run the narrow provider-free tests and targeted diff checks yourself. Review
for prompt-file races, symlink/hardlink substitution, secret/document leakage,
cleanup gaps, argv regression, cross-chat routing, duplicate delivery,
restart behavior, malformed `(send ...)` leakage, and whether the evidence is
sufficient for a guarded production deployment through the existing owning
supervisor. Return exactly one verdict line `PASS` or `BLOCK`, then concise
evidence and concrete blockers. PASS does not itself authorize deployment.
