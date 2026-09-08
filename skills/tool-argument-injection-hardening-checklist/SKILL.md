---
name: "tool-argument-injection-hardening-checklist"
description: "Systematic checklist for hardening tool-argument validation against text-injection vectors before runtime dispatch."
---

# Skill: tool-argument-injection-hardening-checklist

## When to use

When hardening a runtime that accepts text-sourced tool arguments (file paths, external queries, shell commands, emit payloads) against injection via malformed Unicode, control characters, or structural call-injection. Particularly relevant for bot/agent runtimes where untrusted text reaches tool-call boundaries.

## Context

ThreadKeeper (OmegaClaw) required 6+ incremental hardening commits over July 7–12, each discovering a new vector class one at a time: ASCII control characters, C1 controls, Unicode bidi/isolate formatting, Unicode line/paragraph separators, lone surrogates, unquoted same-line trailing calls, compact `)(` payloads. A systematic checklist front-loads all categories so hardening is comprehensive rather than iterative.

## Prerequisites

- A runtime with a tool-call boundary that accepts string arguments from untrusted or semi-untrusted sources.
- A validation function (e.g. `_validate_tool_args`) that runs before filesystem, provider, subprocess, or emit dispatch.
- A focused test suite for hardening regressions.

## Checklist

Validate each tool argument (and each sub-argument for nested calls) against the full taxonomy below before dispatch. Reject and log; do not silently sanitize unless the runtime explicitly requires preservation of benign prose.

### 1. ASCII control characters (U+0000–U+001F)
- Reject all C0 controls except those explicitly required (e.g. `\t`, `\n` if the tool accepts multi-line).
- Include DEL (U+007F).

### 2. C1 control characters (U+0080–U+009F)
- Reject the entire C1 range. These are rarely legitimate in text and can be confused with extended Latin.

### 3. Unicode bidi formatting controls
- Reject U+200E (LRM), U+200F (RLM), U+202A–U+202E (LRE/RLE/PDF/LRO/RLO), U+2066–U+2069 (LRI/RLI/FSI/PDI).
- These can reorder visible text to hide trailing calls or alter audit logs.

### 4. Unicode bidi isolate controls
- Explicitly reject U+2066 (LRI), U+2067 (RLI), U+2068 (FSI), U+2069 (PDI) even if covered above.
- These are newer and sometimes missed by older bidi-filter ranges.

### 5. Unicode line/paragraph separators
- Reject U+2028 (LINE SEPARATOR) and U+2029 (PARAGRAPH SEPARATOR).
- These break line-based audit/parsing without appearing as `\n` in ASCII-only checks.

### 6. Unicode format characters (non-bidi)
- Reject U+200B (ZWSP), U+200C/U+200D (ZWNJ/ZWJ) only if the tool does not require joiners for legitimate scripts. Preserve joiners if the runtime handles Arabic/Devanagari/etc.
- Reject U+FEFF (BOM/ZWNBSP) inside arguments (not at start of file).

### 7. Lone surrogates
- Reject unpaired UTF-16 surrogate halves (U+D800–U+DFFF) if the runtime decodes to UTF-8/UTF-32.
- These cause encoding errors or bypass filters that assume well-formed UTF-8.

### 8. Unquoted same-line trailing calls
- For tools that accept file-content or emit payloads: detect unquoted trailing-call syntax on the same line as legitimate content (e.g. `text )(tool-call)`, `text )(tool-call`).
- Reject if a closing `)` followed by `(` or a bare tool name appears after content that is not inside an explicit quoted string.
- Preserve ordinary parenthesized prose (e.g. "(see note 3)").

### 9. Compact trailing-call injection
- Detect compact `)(` sequences (no space) at end of content/payload.
- Reject if the `)(` pattern is followed by a tool-call name or bare token.

### 10. Null bytes and overlong encodings
- Reject U+0000 (NUL) explicitly even if covered by C0.
- Reject overlong UTF-8 sequences (e.g. 0xC0 0x80 for U+0000) if the runtime decodes byte streams.

### 11. Homoglyph and confusable checks (optional, project-specific)
- If the runtime is security-critical, consider flagging or rejecting confusable characters (Cyrillic a, Greek o) in tool names or file paths.
- This is project-specific and should not block legitimate international text.

## Test procedure

For each category:
1. Add a focused test that constructs an argument containing the rejected character/pattern.
2. Assert the validation function rejects it with the expected error type.
3. Add a control test with legitimate content (prose with parentheses, joiners if allowed, multi-line with `\n`).
4. Run the full focused hardening suite and verify no regressions.

```bash
# Example pattern (adapt to project)
pytest tests/test_tool_arg_hardening.py -v
# Full suite
pytest -v  # or python3 -m unittest discover -s tests -v
git diff --check
```

## Anti-patterns

- Do not reject characters required by legitimate scripts (Arabic, Devanagari, CJK) unless the specific tool cannot accept them.
- Do not silently strip rejected characters; always reject and log for auditability.
- Do not add categories one at a time across commits; use the full checklist.
- Do not skip the control tests — false positives on legitimate prose are as serious as false negatives.

## Maintenance

When a new injection vector is discovered:
1. Add it to the checklist above.
2. Add a focused test and control test.
3. Verify the full suite passes.
4. Update this skill if the new category is generalizable across runtimes.

## Source

Derived from ThreadKeeper (OmegaClaw) hardening commits on July 7–12, 2026:
- `25435f2` strict string argument types
- `cf0db9a` Unicode format character rejection
- `3a296ad` compact unquoted `)(` trailing-call rejection
- `08e7f39` unquoted file-content trailing-call rejection
- `8de75d5` C1 controls and line/paragraph separators
- `5624013` Unicode bidi/isolate controls

Provenance: `projects/omegaclaw/repos/Threadkeeper`, branch `agent/threadkeeper-hardening-next`.
