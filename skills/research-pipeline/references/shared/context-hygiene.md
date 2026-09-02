# Context Hygiene For Continuous Research

Context is a scientific resource. Protect the main researcher's continuity without fragmenting the program into stage-specific personas.

## Keep The Thesis, Isolate The Noise

The main session should retain:

- the Program Compass and current episode question;
- strongest supporting and contrary evidence;
- representative raw cases needed for the live question;
- method lineage and design lessons;
- the positive object or author argument only after one exists;
- exact durable paths and the next action.

Keep bulk operational material outside the main context:

- installation and dependency logs;
- downloads and file-transfer output;
- long training stdout/stderr;
- exhaustive paper text and per-paper writing notes;
- compilation output and repeated environment diagnostics;
- large tables that can be queried from files.

Use subagents, background jobs, or durable files for noisy work. Return structured metrics, exit status, verified paths, a compact error summary, and only the excerpts needed for a scientific decision. Do not hide contrary cases merely to keep the summary short.

## Specialists Are Temporary

Load a specialist skill because the current uncertainty needs it, not because another skill finished. The same researcher owns the question before and after the call.

Pass the smallest sufficient evidence packet. A specialist returns one or more of:

- a credible new observation;
- a changed explanation;
- a method-design consequence;
- a durable execution result;
- a bounded claim or objection.

Do not chain artifacts through a fixed sequence and do not create a new report solely as an interface between skills. Update the existing authoritative state when a compact result is sufficient.

## Subagent Isolation

Use subagents when a task is self-contained and context-heavy, such as full-paper reading, broad literature extraction, environment setup, log triage, independent audit, or repeated figure inspection. Give each subagent minimum task-local context and require a compact evidence-linked output.

Do not delegate the evolving thesis, final method choice, or program ownership. The main researcher synthesizes subagent outputs and checks them against raw evidence.

For independent reviewers, withhold author-side summaries when independence matters. For co-author interpretation, include contrary evidence and enough context to reason scientifically.

## Durable Operational Output

Training and remote jobs should write configs, logs, checkpoints, metrics, and exit status to durable paths. Poll compact summaries rather than streaming hundreds of lines into the conversation. An interrupted job leaves an exact resume record; it never becomes a scientific result.

Prefer detached or scheduler-managed remote execution when appropriate to the project's server rules. Do not impose one universal `screen`, `tmux`, Slurm, Docker, or provider pattern over project-specific instructions.

## Re-Anchor Operations, Refresh Scientific Identity

For an ordinary interruption, skill update, or one-off compaction, re-anchor from current
project authority, the concise state, exact raw artifacts needed for the live question,
and active jobs. Do not restart merely because a command failed or a phase label changed.

Prefer a fresh scientific episode and context when continuity of the old narrative is
more dangerous than its convenience:

- central evidence or evaluator is invalidated;
- the governing primitive, operational effect, or paper identity materially changes;
- the PI's artifact-grounded candidate judgment changes the work from construction to
  submission maturation;
- project ownership passes between the GPT PI and a Claude implementation episode;
- repeated compaction, invented paths, duplicated actions, or forgotten contrary
  evidence makes the old context an unreliable evidence index.

Do not ask the same model to prove that its own framing is contaminated. Before the
boundary, update the sole state from artifacts, preserve active process identities, and
name the exact live question. The receiving context rereads authority and raw evidence;
it does not inherit method certainty, stop language, or maturity from conversation
history. Do not interrupt a valid run merely to refresh its surrounding conversation.

Running sessions do not automatically absorb skill changes from disk. After the current atomic action, explicitly ask an active session to reread the changed canonical skills when the update affects its behavior. Do not interrupt a valid experiment to do so.

Structured handoff artifacts remain optional. For GPT/Claude transfer, the sole state,
bounded delegation question, code diff, raw artifacts, and execution truth are the
handoff; neither model writes a competing thesis file.

## Judgment Over Quotas

There is no universal token budget per paper, candidate count, experiment count, or number of skill calls. Spend context and compute according to expected information and claim value. Compact when material no longer helps the live decision, not when a phase quota is reached.
