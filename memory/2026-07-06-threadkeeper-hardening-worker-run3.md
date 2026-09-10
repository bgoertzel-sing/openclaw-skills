# 2026-07-06 ThreadKeeper Hardening Worker (run 3)

## Summary

ThreadKeeper branch `agent/threadkeeper-hardening-next` commit `ee894d3` pushed to `fork/agent/threadkeeper-hardening-next`: **Add output size cap for search/tavily-search/technical-analysis tools**. 137 focused mock tests passing.

## Changes

- **External tool output cap**: Added `OMEGACLAW_SUBAGENT_MAX_SEARCH_OUTPUT_CHARS` (default 4000, 0 disables) to cap search/tavily-search/technical-analysis tool output at the tool level. This matches the defense-in-depth pattern already used by `_tool_read_file` (`_SUBAGENT_MAX_READ_FILE_CHARS`) and `_tool_shell` (`_SHELL_OUTPUT_CAP`). External API responses can be arbitrarily large; while `run_tools` clips results to 2000 chars for the prompt, the full unbounded response was in memory before clipping.
- **`_bound_tool_output()` helper**: Reads the module-level config at call time (not as a default parameter, which would be evaluated once at function definition time). All three search-type tool registrations in `_build_tool_registry()` are now wrapped: `lambda q: _bound_tool_output(websearch.search(q))`, etc.
- 6 focused tests added: large result truncation with marker, small result preservation, cap disabled when 0, non-string result handling, search registry wrapping (FakeWebsearch), tavily/technical-analysis registry wrapping (FakeAgentverse).

## Verification

- `git diff --check`
- `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`
- Focused mock pytest via `projects/omegaclaw/local/threadkeeper-pytest-venv` (`137 passed`)
- `origin/pr-1` remains an ancestor (75 commits ahead)
- Synced `subagent.py` to OmegaClaw-Core runtime tree with zero diff

## Constraints

No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.
