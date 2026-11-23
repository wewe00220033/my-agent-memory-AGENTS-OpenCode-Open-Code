# SUMMARY — LEDGER export

- 453 LEDGER files → 453 elements in 5 JSON part(s) (≤ 2,097,152 bytes each, largest 2,094,528) + `ledger.parts.json`.
- FORENSIC_DATABASE is a 100% duplicate of LEDGER (T0) and is not exported (Q5).
- Every string is redacted (`[REDACTED:*]`), home paths become `~`; HIGH_ENTROPY hits recorded by hash only.
- Reassemble with `tools.shard.read_shards('conversations/ledger/ledger.parts.json')`; canonical sha256 `bb2b7d4bc8f1a60e67cfc44f99e6882d7f466d95a931f1158d911a6944d92f7d`.
- EN: 453 files, 453 elements, 5 part(s); FORENSIC skipped as duplicate; see AUDIT.md for per-element hashes.
