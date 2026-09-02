# Reproducible Figures And Tables

Use only for paper visuals. Each visual should establish a phenomenon, explain the
implemented primitive, make a decisive comparison, test a prediction, show supported
generality, or bound utility and cost. Remove visuals that merely replay run chronology
or decorate the manuscript.

## Generate From Evidence

Generate quantitative visuals from machine-readable artifacts through a checked-in
script or notebook entrypoint. Record source paths and hashes or run IDs; filtering,
aggregation, missing-data, and uncertainty rules; metric direction and units; sample
and seed definitions; command; and output path. Never manually transcribe
claim-bearing numbers or hardcode example values into production scripts.

Architecture and mechanism diagrams must show the system that actually ran, including
training-only and inference-time paths. Use standard notation and editable source.

## Design At Final Size

At manuscript size, labels, legends, markers, uncertainty, and panel relationships must
remain legible. Make colors distinguishable in grayscale and common color-vision
deficiencies. Disclose truncated axes, transformations, metric direction, uncertainty,
and sample definitions. Prefer direct labels and compact legends over decoration or
encodings that exaggerate small differences.

Generate tables from the same evidence used by the manuscript. Calculate at full
precision and round only for display. Distinguish variation across seeds, examples,
folds, and runs. Represent missing, failed, and inapplicable values explicitly. Apply
bold or underline only by a declared comparison rule that does not reward incomparable
or statistically indistinguishable entries.

Before handoff, regenerate from a clean command, compare displayed values and captions
with artifacts and manuscript claims, inspect the compiled result, and verify that every
visual is cited. After the narrative draft exists, use `CLAIMS_EVIDENCE.md` to check
visual takeaways. Return commands, source artifacts, final paths, and any qualifier that
materially changes interpretation.
