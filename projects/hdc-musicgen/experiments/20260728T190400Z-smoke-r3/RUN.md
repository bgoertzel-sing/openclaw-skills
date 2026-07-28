# Run 20260728T190400Z-smoke-r3

- Status: `running; remote setup in progress`
- Question: Does the amended eight-track MusicGen Stage 0/S/A smoke execute
  cleanly and report the preregistered related-versus-unrelated measurements?
- Source: `8907d0f`; pod `xgv04sy1g9a3q8`; cap 8 hours / USD 5.

## Execution evidence

- At 2026-07-28T19:07Z, transferred a Git archive of the pinned source and
  exactly eight explicit-CC MP3 files. The remote SHA-256 values matched the
  local selection manifest.
- Started `/workspace/hdc-musicgen-r3/remote_run.sh` in remote tmux session
  `hdc-musicgen-r3`; it is installing the isolated environment before tests
  and Stages 0/S/A. No stage result exists yet.
