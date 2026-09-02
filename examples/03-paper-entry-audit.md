# Case 3: A Draft Starts Before The Method Is Ready

## Situation

A project has dozens of result files, several ablations, and a polished
narrative. The proposed method still does not consistently beat the strongest
matched baseline, and provenance or evaluator details remain unresolved.

## Common Agent Failure

Experimental volume is mistaken for maturity. Once a draft exists, every new
result is interpreted in ways that protect the narrative. A late reviewer then
finds the baseline, scorer, seed provenance, or cost comparison is not fair.

## FIRM Response

Before complete manuscript writing, the researcher assembles a raw-evidence
packet and asks an independent second PI to judge:

- `PRIZE`: would the strongest honest result be worth a paper?
- `FIDELITY`: does the paper still solve the original program?
- `ENTRY`: are the method, baseline, evidence, and claim stable enough to write?

If entry fails, polishing freezes while research continues. The existing prose
is preserved, but it no longer sets scientific direction.

## Starting Prompt

```text
Run `/firm:research-review mode: experiment-audit` and `/firm:research-review mode: state-audit` on the raw artifacts before further
paper polishing. Verify provenance, splits, evaluator semantics, convergence,
information and compute parity, and the strongest matched baseline. Apply
PRIZE/FIDELITY/ENTRY. If ENTRY fails, preserve the draft but return ownership
to method formation; do not convert failed methods into an analysis paper.
```

## Expected Artifacts

- `RAW_EVIDENCE_PACKET.md` links every claim to source artifacts.
- `EXPERIMENT_AUDIT.md` records integrity and fairness.
- `PAPER_ENTRY.md` is an explicit `PASS` or `HOLD`.
- Full paper writing begins only after the positive object and decisive
  comparisons stabilize.

## Why It Matters

Writing is part of research, but a draft should summarize evidence rather than
become the force that bends later evidence.
