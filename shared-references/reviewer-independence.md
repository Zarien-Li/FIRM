# Reviewer Independence Protocol

Use this protocol when a reviewer must independently judge an artifact: paper
readiness, claim/citation/headline audit, experiment validity, rebuttal stress test,
or proof audit. It does not govern collaborative co-PI Interpret or Method Challenge.

## Independent Artifact Review

Pass:

- reviewer role and objective;
- primary artifact paths;
- venue, format, or explicit evaluation constraints;
- required output schema.

Do not pass:

- the executor's summary or interpretation;
- preferred conclusion or claimed strengths;
- proposed answers or leading questions;
- previous independent review findings;
- a narrative of what was fixed since the last fresh review.

The reviewer should read primary artifacts directly. This prevents the executor's
framing and blind spots from becoming the reviewer's input.

Use a fresh thread for readiness and audit judgments. A reply thread may check whether
the same reviewer's own findings were addressed, but it is no longer an independent
fresh assessment.

## Co-PI Exception

`research-review` deliberately defines collaborative roles:

- Field/Prize receives the program and empirical surface;
- Interpret receives the lead PI's competing explanations;
- Method Challenge receives the lead PI's candidate constructions.

Those packets are not independent artifact audits; their purpose is comparison and
scientific challenge. Include contrary evidence and exact paths, avoid asking for a
desired verdict, and preserve lead-PI synthesis. Do not apply the zero-summary rule in
a way that makes these roles impossible.

## Trace

For a fresh independent review record:

```markdown
independence_check:
- primary artifacts passed directly: yes | no
- executor interpretation excluded: yes | no
- prior review findings excluded: yes | no
- thread policy: fresh
```

If any required answer is `no`, label the review collaborative or reply-mode rather
than independent.
