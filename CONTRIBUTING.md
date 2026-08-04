# Contributing to FIRM

FIRM grows from recurring research-agent failures, not from accumulating generic
prompt text.

## A strong contribution contains

1. **Failure case:** the observable agent behavior and its scientific cost.
2. **Hidden confusion:** the inference or missing distinction that caused it.
3. **Minimal repair:** the smallest skill change that addresses the cause.
4. **Regression cases:** when the new instruction should not apply and the
   opposite mistake it might create.
5. **Neutral test:** an evidence packet and prompt that do not reveal the desired
   conclusion.

Bug fixes, clearer trigger descriptions, safer commands, better examples, and
runtime compatibility improvements are also welcome.

## Before opening a pull request

```bash
make check
```

Keep each `SKILL.md` below 500 lines. Put detailed procedures, schemas, or examples
in that skill's `references/` or `scripts/` directory. Do not add a hard dependency
on a specific reviewer model, private service, dataset, or unpublished artifact.

A pull request should explain:

- which failure it repairs;
- why the existing skill is insufficient;
- what files changed;
- how the change was tested;
- what undesirable behavior was checked for.

By contributing, you agree that your contribution is licensed under the project's
MIT License.
