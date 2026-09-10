# ProtoMegaBot write-file / multiline-payload parser fix

Date: 2026-07-14
Author: ProtoMegaTron (self-diagnosis)
Scope: `repos/OmegaClaw-Core/src/helper.py :: balance_parentheses`
Trigger: repeated failures when ProtoMegaBot tried to write + compile the note
0012 LaTeX paper ("closing primitives / identity-tension"), while ZeroBot
(full OpenClaw, native `write` tool) succeeded.

## Symptom (Observed)

- ProtoMegaBot's tool calls surfaced in the Telegram transcript as garbled
  natural-language step-chains, e.g.
  `list files -> print text -> show first 40 lines of 2>/dev/null`, and every
  paper-write attempt produced "Exec failed" or "couldn't generate a response".
- Note 0012 only landed once ZeroBot wrote it directly.

## Root cause (Reproduced)

`balance_parentheses()` is the model-output -> skill-call parser. It did:

1. `s.replace("_newline_", "\n")` (expand encoded newlines) FIRST, then
2. split on physical newlines, then
3. treat each line as a separate command.

Consequence: a multi-line `write-file` body (LaTeX, code, config) was
**shredded**. Only the first line became the file content; every subsequent
line (`\begin{document}`, `Hi`, `\end{document}`, ...) was parsed as its own
bogus command `(\begin{document})`, `(Hi)`, ... which then failed as unknown
skills. `shell` scripts / heredocs spanning multiple lines failed the same way.

Reproduction (pre-fix):

```
IN : write-file paper.tex \documentclass{article}_newline_\begin{document}_newline_Hi_newline_\end{document}
OUT: ((write-file "paper.tex" "\documentclass{article}") (\begin{document}) (Hi) (\end{document}))
```

This is a **skill-invocation / output-parsing bug**, distinct from the
transport/ownership/native-crash classes tracked in
`PROTOMEGABOT_REPAIR_PLAN_20260712.md`.

## Fix

In `helper.py`:

1. New `_merge_multiline_payloads(lines)` (mirrors `_merge_send_continuations`):
   for `write-file` / `append-file` / `shell`, trailing lines that are not
   themselves known commands are folded back into the preceding command's
   payload instead of being parsed as new commands.
2. `balance_parentheses` now keeps raw physical lines, runs the multiline merge
   before the send merge, and only drops blank lines *between* commands.
3. Payload formatting: multiline / quote-bearing content is JSON-encoded
   (`json.dumps`, same technique already used for `send`) so newlines and
   quotes survive as a single well-formed string argument. Single-line behavior
   is unchanged.

Post-fix reproduction:

```
OUT: ((write-file "paper.tex" "\\documentclass{article}\n\\begin{document}\nHi\n\\end{document}"))
```

## Validation

- `python3 src/helper.py` (canonical `test_balance_parenthesis`): PASS, including
  all pre-existing single-line assertions plus new regression assertions for
  multiline write-file, multiline shell, and multiline append-file.
- `py_compile src/helper.py`: OK.
- Broader pytest collection errors (`py_landlock`, mock-driver imports) are
  pre-existing and unrelated.

## Not addressed here (follow-ups)

- `write-file` (Prolog `open/2` in `skills.metta`) does **not** create parent
  directories. Writing `papers/0012/foo.tex` when `papers/0012/` is absent will
  still fail. Recommend a `make_directory_path` before `open` in the
  `write-file` / `append-file` skill definitions.
- Consider surfacing unknown-command lines as an explicit parse error to the
  model rather than emitting `(unknown ...)` s-exprs that fail silently.
- The transport/crash reliability plan (20260712) remains separate and unchanged.
