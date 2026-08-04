# LaTeX and compilation

## Discover the build

Inspect, in order:

- README or Makefile;
- venue instructions;
- root TeX file and `\documentclass`;
- bibliography backend (`bibtex` or `biber`);
- custom scripts or CI.

Prefer the existing reproducible build. Typical safe commands are:

```bash
latexmk -pdf -interaction=nonstopmode -file-line-error main.tex
# or the project's documented command
```

Do not install packages, alter the template, or use `sudo` without approval.

## Repair loop

1. Save the full compile log.
2. Find the earliest causal error, not the last cascade message.
3. Inspect the referenced source line and nearby macros.
4. Apply the smallest correct fix.
5. Recompile from a clean enough state for the error class.
6. Check bibliography, references, labels, and page count.

## Required checks

- no undefined references or citations;
- no duplicate labels;
- no missing figures, fonts, or bibliography files;
- no accidental template modification;
- no main-text overflow hidden by clipping;
- page count matches the current venue rules supplied by the user or verified from
  an authoritative source;
- PDF opens and important pages render correctly.

Treat overfull boxes by location and severity. A tiny bibliography overflow is not
equivalent to clipped equations or unreadable main-text figures.
