# Release Demo Script

The release demo should show a real Claude Code invocation. `make demo` is only a
guided terminal storyboard for rehearsal; it does not claim to be model output.

## 0–12 seconds: the missing layer

Show the README hero.

> Claude Code can search papers, write code, run experiments, and draft a paper.
> FIRM adds the research judgment needed after the result arrives.

## 12–25 seconds: install

In Claude Code:

```text
/plugin marketplace add Zarien-Li/FIRM
/plugin install firm@firm-research
/reload-plugins
```

Show `/help` with the `/firm:` namespace.

## 25–55 seconds: one neutral case

Open `demo/fixture/RESULT.md`, then invoke:

```text
/firm:method-development "Interpret RESULT.md"
```

The fixture prompt must remain neutral. Capture a real response and highlight only
claims supported by the raw result:

- run competence and comparison parity;
- the current realization's task-level loss;
- the gap between changed routing and unchanged target errors;
- the limit imposed by one seed;
- the most informative next experiment.

Do not cut together sentences that change the model's meaning.

## 55–75 seconds: constructive continuation

Show the next commands rather than another generic loop:

```text
/firm:method-development "Develop the primitive from this evidence"
/firm:method-development "Plan the decisive construction experiment"
/firm:research-review
```

Explain that each skill has a narrow job and that side-effectful workflows require
explicit invocation.

## 75–90 seconds: close

Return to the skill table and GitHub repository.

> A failed method is evidence—not a verdict on the field.
