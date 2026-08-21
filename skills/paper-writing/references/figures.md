# Reproducible Figures And Tables

Use this reference only for paper figures and tables. Design each visual from its
scientific and narrative job. After the draft exists, use `CLAIMS_EVIDENCE.md` to
verify that visual takeaways and captions remain supported.

## Select The Visual Job

Each visual should do one necessary job: establish the phenomenon, explain the
primitive, compare the decisive systems, test a unique prediction, show generality, or
bound utility/cost. Remove visuals that only replay run chronology or decorate a
section.

Architecture or mechanism diagrams must depict the implemented system, not an intended
future design. Use standard notation and label training-only versus inference-time
paths.

## Build From Source Artifacts

Generate quantitative visuals from machine-readable source artifacts with a checked-in
script or notebook entrypoint. Record:

- source paths and hashes or stable run IDs;
- filtering, aggregation, missing-data, and uncertainty rules;
- metric direction, units, sample size, and seed definition;
- exact command and output path.

Never manually transcribe claim-bearing values. Do not hardcode example numbers into a
production figure script. A manually edited annotation must be non-numeric or derived
from the same source in code.

## Design For Final Size

Use the project's existing plotting and typography conventions. At final manuscript
size:

- labels, legends, markers, and uncertainty remain readable;
- colors are distinguishable in grayscale and common color-vision deficiencies;
- panels share scales when visual comparison assumes they do;
- axes disclose truncation, transformations, and metric direction;
- uncertainty and sample definitions are stated;
- captions give the supported takeaway and decisive caveat.

Prefer direct labels and compact legends. Avoid redundant decoration, 3D effects, and
visual encodings that exaggerate small differences.

## Tables

Generate tables from the same evidence source used for claims. Preserve full-precision
calculation and round only for display. State whether variation is across seeds,
examples, folds, or runs. Mark missing, failed, and inapplicable results distinctly;
never convert them to zero or silently drop them.

Bold or underline only according to an explicit comparison rule. Verify that the rule
does not reward incomparable or statistically indistinguishable entries.

## Verification

Before handoff:

1. regenerate from a clean command;
2. compare plotted/table values with source artifacts and manuscript claims;
3. inspect rasterized or compiled output at final size;
4. check clipping, overflow, font embedding, line weights, and accessibility;
5. confirm every visual is cited and its caption stays within evidence scope.

Return the generation command, source artifacts, final asset paths, and any remaining
qualifier. Visual polish cannot repair missing or invalid science.
