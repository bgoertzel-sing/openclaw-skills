# Third-party software and provenance

This archive does not redistribute public dependency repositories or model weights. Installation fetches them from:

- OpenClaw: https://github.com/openclaw/openclaw — pinned package `2026.6.10`; inspect its license/release provenance.
- PeTTa: https://github.com/bgoertzel-sing/PeTTa.git — pinned commit `4ce1d0ea58855abb772b911278312c8846e5cc08`; upstream lineage https://github.com/trueagi-io/PeTTa.
- OmegaClaw-Core: https://github.com/asi-alliance/OmegaClaw-Core.git — base `16d380d9ff32675aa3f19bec7419229b99a7ae12`, patched locally; MIT at the reference base.
- PeTTa Chroma library: https://github.com/patham9/petta_lib_chromadb.git.
- Python dependencies: names/versions in OmegaClaw's pinned `requirements.txt`; each retains its own license.
- SWI-Prolog, Node.js, Python, Torch, Transformers, Chroma, Janus-SWI and platform packages retain their respective licenses.

The archive contains generalized local skill/plugin/template source. Review headers and source files for any additional notices. A patch is a derived modification, not an assertion of ownership over upstream source.

Do not redistribute provider model weights, proprietary prompts, credentials, private datasets, or recipient runtime stores merely because this recipe can access them locally.
