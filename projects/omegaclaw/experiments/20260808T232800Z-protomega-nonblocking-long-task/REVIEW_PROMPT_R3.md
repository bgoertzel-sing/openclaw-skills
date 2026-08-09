Act as an independent production-safety reviewer. Do not modify files, send
messages, or alter running processes. Inspect the pinned source and complete
evidence for the Protomega non-blocking long-document repair:

- projects/omegaclaw/protocosmo2/tools/phase5_omegaclaw_case.py
- projects/omegaclaw/protocosmo2/tools/phase6_private_canary_runner.py
- projects/omegaclaw/protocosmo2/tests/test_live_runtime_prompt.py
- projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary.py
- projects/omegaclaw/worktrees/protocosmo2-phase6-live/channels/private_canary_telegram.py
- projects/omegaclaw/experiments/20260808T232800Z-protomega-nonblocking-long-task/RUN.md

The prior review found prompt-file TOCTOU, cleanup-on-write/fsync failure,
missing adversarial tests, and missing combined live overlap evidence. The
revision reads through one O_NOFOLLOW descriptor validated by fstat, requires
a private regular single-link file, cleans every partial-file failure path,
and adds adversarial substitution and injected-flush-failure tests. Pinned
commits are transport `eb29a3388530dc7fdc27171b372037a9f77dc9ce` and outer
`b07936bad28fd06bf556b5dcb95374897469f7de`.

R4 externally passed under the hardened code: source 121, ack receipt 122,
interleaved `SHORT-R4-OK` receipt 124, successful final PDF result receipt 125
to source 121, with the short reply 31 seconds before the long result. Durable
task state is completed; no pending/undelivered item or `(send ...)` leak.

Run the exact narrow provider-free tests and targeted diff checks yourself.
Review prompt-file races, symlink/hardlink substitution, leakage, cleanup,
argv regression, immutable cross-chat/reply routing, duplicate/restart
behavior, renderer strictness, and the production restart/rollback boundary.
Return exactly one verdict line `PASS` or `BLOCK`, followed by concise evidence
and concrete blockers. PASS does not itself authorize deployment.
