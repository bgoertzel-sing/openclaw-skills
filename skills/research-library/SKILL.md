---
name: research-library
description: Ingest, preserve, summarize, and search papers, PDFs, web pages, datasets, repositories, archives, and binary artifacts. Use when external material should remain available and discoverable across research projects.
---

# Research Library

A vector index cannot reliably search a binary source without a durable textual representation. Create a Markdown sidecar for every important item.

## Ingest

1. Choose a stable lowercase slug under `~/research-agent/library/`.
2. Preserve the original file or canonical URL when permitted.
3. Copy `templates/LIBRARY_ITEM.md` to `SOURCE.md`.
4. Record title, type, authors/organization, version/date, retrieval date, canonical identifier, local path, SHA-256 for local files, license/access limits, privacy tier, tags, and related projects.
5. Summarize methods, claims, limitations, and relevance.
6. Add page/section/line/commit locations for important evidence.

Never store a credential-bearing page, private token export, or unrelated personal data.

## Read carefully

- For PDFs, inspect figures, tables, equations, and page context, not only extracted text.
- For repositories, pin a commit and inspect code/CI in addition to README prose.
- For datasets, capture schema, provenance, license, transformations, and hashes.
- For web pages, record retrieval date because content can change.
- Respect copyright: keep quotations short and use summaries.

## Search

- Use QMD/memory search for concepts, aliases, and related work.
- Use `rg` for exact terms in sidecars and extracted text.
- Open the original source before relying on a consequential claim.
- Report provenance with the answer.

## Update

When a source changes, preserve the prior version or hash when useful. Add a dated change note rather than silently replacing evidence that supported a prior decision.
