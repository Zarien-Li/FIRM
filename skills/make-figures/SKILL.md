---
name: make-figures
description: Generates publication-quality plots, tables, and LaTeX include snippets from verified experiment data.
when_to_use: Invoke explicitly when the data source and intended scientific message are known. It may create or edit plotting scripts and output files.
argument-hint: "[figure plan or data path]"
disable-model-invocation: true
---

# Make Publication Figures

Create figures and tables that answer a scientific question at final paper size.
Do not decorate weak evidence or manually transcribe important values from prose.

## 1. Establish the figure contract

For each requested figure, resolve:

- scientific question;
- intended takeaway;
- exact source data and provenance;
- comparison systems, regimes, and sample definition;
- uncertainty or aggregation method;
- target venue format, columns, and output type;
- figure number and claim IDs it supports.

If the data source or metric semantics are unclear, stop and request the missing
artifact rather than drawing a plausible chart.

## 2. Inspect and validate data

Read machine-readable result files when available. Check:

- units, direction, and denominator;
- missing values and excluded runs;
- seed and sample aggregation;
- alignment of conditions across files;
- consistency with reported paper values;
- whether uncertainty bars are meaningful for the data-generating process.

Preserve the transformation from raw files to plotted values in code or a compact
manifest.

## 3. Choose the visual form from the question

- **Grouped bars:** a small number of discrete systems or conditions.
- **Line plot:** ordered sweep, training trajectory, horizon, depth, or budget.
- **Scatter:** relationship between two measured variables; show uncertainty and
  sample identity when relevant.
- **Heatmap:** structured matrix where both axes matter.
- **Distribution plot:** variability, tails, or heterogeneous examples.
- **Small multiples:** repeated comparable panels where one overloaded chart would
  obscure the pattern.
- **Table:** exact values and compact comparison are more important than visual
  trend.

Do not default to a complex composite figure. One figure should communicate one
primary claim.

## 4. Generate reproducibly

Create a dedicated script per figure or a clearly factored shared generator. The
script should:

- load data from declared paths;
- perform explicit aggregation;
- fail on missing expected conditions rather than silently dropping them;
- set dimensions for the intended one- or two-column placement;
- use vector output (`PDF` or `SVG`) when compatible, plus `PNG` only for preview;
- embed or use portable fonts allowed by the venue;
- save the exact plotted table when nontrivial transformations occur.

Do not hardcode final values when they can be derived from source files. Do not
overwrite raw results.

## 5. Apply academic visual discipline

At final size:

- labels, ticks, legends, and annotations are readable;
- axes include units and meaningful ranges;
- color is not the only encoding;
- line styles, markers, or hatching remain distinguishable in grayscale;
- panel labels and terminology match the manuscript;
- legends do not cover data;
- uncertainty is defined in the caption;
- significant digits reflect measurement precision;
- no 3D effects, gradients, decorative shadows, or generic dashboard styling;
- whitespace and alignment are intentional.

Use a restrained, consistent palette chosen for contrast and accessibility. Reuse
semantic encodings across the paper: the same method should not change appearance
between figures without reason.

## 6. Write the caption as evidence

A caption should state:

1. what is plotted and on which data;
2. what each axis, panel, and uncertainty element means;
3. the comparison needed to read the figure;
4. the bounded takeaway;
5. any important sample or evaluation limitation.

Do not make a stronger causal or generalization claim in the caption than the
experiment supports.

## 7. Inspect the rendered artifact

Open every generated figure at approximate final size. Check for clipping,
overlap, tiny text, excessive whitespace, misleading axis scales, rasterization,
and inconsistent panel geometry. For complex figures, request a fresh independent
visual/scientific review through `/firm:second-pi`.

## 8. Produce LaTeX integration

Return a snippet using the project's conventions, for example:

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/fig2.pdf}
  \caption{...}
  \label{fig:...}
\end{figure}
```

Do not guess placement specifiers, widths, or package requirements when the template
already defines them.

## Output

```markdown
# Figure Generation Report

| Figure | Question | Source data | Script | Output | Claim supported |
|---|---|---|---|---|---|

## Data checks

## Visual checks

## Captions and LaTeX snippets

## Remaining limitations
```

Keep scripts, generated figures, and the plotted-data manifest in predictable
project directories. Report any value discrepancy before modifying the manuscript.
