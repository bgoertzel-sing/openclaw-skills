Final read-only review of commit `358fa61` atop `a2ac170`. R3b's only blockers
were lack of flock proof on inherited fd 9 and absent exact replay command. The
supervisor now runs `flock -n 9` after exact fd-path validation before trusting
the handoff. The experiment RUN now embeds the literal focused command, which
passes 85/85. Independently rerun that exact command, compilation, four shell
syntax checks, and scoped diff check; verify this closes the ambient bypass
without breaking watchdog handoff or detached-owner lock release. Return PASS
or BLOCK first. Do not modify anything; PASS does not authorize restart.
