# Machine-readable citation audit schema

Optional file: `citation-audit.json`

```json
{
  "schema_version": 1,
  "paper_root": ".",
  "generated_at": "ISO-8601 timestamp",
  "modes": {"uncited": false, "soft_only": false},
  "summary": {
    "cited_keys": 0,
    "verified": 0,
    "metadata_issues": 0,
    "context_issues": 0,
    "unverifiable": 0
  },
  "entries": [
    {
      "key": "example2026",
      "bib_file": "references.bib",
      "identity_status": "verified",
      "metadata_status": "correct",
      "authoritative_sources": [],
      "contexts": [
        {
          "file": "sections/related.tex",
          "line": 42,
          "text": "...",
          "verdict": "partial",
          "action": "narrow_sentence",
          "proposed_rewrite": "..."
        }
      ]
    }
  ],
  "uncited_keys": [],
  "remaining_manual_checks": []
}
```

Use stable lower-case enum values. Store source identifiers or URLs only when the
runtime and project policy permit it.
