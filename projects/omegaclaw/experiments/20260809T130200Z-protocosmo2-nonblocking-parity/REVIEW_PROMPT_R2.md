Act as final independent production-safety reviewer. Do not modify files,
messages, or processes. Review commits `d2afe19` and `54e2576`, the complete
experiment RUN, and current scoped status.

R1 blocked because the pre-sidecar live owner could be mistaken for inactive
and because ambient variables could redirect ProtoCosmo2 paths. The wrapper now
freezes all production identity/path values. Its one-purpose
`validate-pre-sidecar` / `stop-pre-sidecar` boundary holds the dedicated cutover
lock and requires caller-supplied expected PID, `/proc` start tick, and cmdline
SHA-256; it independently verifies the exact resolved wrapper `run` command,
process-group leadership, and exactly one child containing the expected runner,
core, PeTTa, and driver paths. Mismatch fails closed. Stop signals the verified
process group, waits for owner and child to disappear, rechecks the PID file,
then removes it. A read-only validation against the actual current live owner
passed for PID 1918102/start 41230822/cmdline SHA-256
`839ceb5e458138bf3f84e87396b0e5edbd889a240523939dcfdc9be1fcde0706`.

Independently rerun the 84-test gate, compilation, four shell syntax checks,
and scoped diff checks. Verify the first-cutover action cannot overlap a
receiver and that frozen wrapper paths preserve isolation. Return `PASS` or
`BLOCK` on the first line with concise evidence and concrete blockers. PASS is
technical readiness only and does not authorize deployment.
