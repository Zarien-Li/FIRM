# Collaboration Without Split Ownership

Use this reference when another model can materially improve implementation, invention,
or factual verification. The persistent PI remains responsible for context,
interpretation, and the next scientific decision.

## Assign The Task, Not A Model Rank

Claude and GPT can each lead the full project through submission readiness, including
invention, implementation, experiments, interpretation, and authorship. Choose a
collaborator for the current uncertainty and available capabilities, not a fixed division
of models into thinker, coder, and reviewer. Working alone is legitimate. Calling another
model does not transfer leadership; explicit user-authorized handover does.

For a child call, use [delegated-task.md](delegated-task.md) as the shared bounded-role
context, plus a PI-authored task packet. The same skills support both identities. The
role context is not another research workflow and does not decide the method or next
experiment. Child prompts must establish their task even if host instructions default
to persistent PI ownership.

## Bounded Scientific And Engineering Work

Delegate a scientific question rather than a vague request to “continue the project.”
Provide the accepted task and information boundary, relevant code and raw evidence, the
comparison being implemented, writable surfaces, resource envelope, and durable output
paths. Ask the collaborator to return, as relevant to the assignment:

- the actual code and configuration changed;
- execution outcome and paths to the commands, logs, and raw artifacts;
- observations, implementation defects, and design consequences;
- any evidence that the delegated premise itself was false.

The collaborator may repair local code and adjust the realization when evidence requires it. It
must not silently rename the paper, close the program, choose a new broad seed, or write
a competing scientific state. The PI inspects the work and integrates it. Give creative
or analytical tasks room to challenge the premise and suggest a new principle; the PI
owns its adoption and validation, not the collaborator's model name.

## Choose The Smallest Useful Delegation

Default to the current host's native bounded subagents for separable, context-heavy
work: implementation, environment repair, log triage, or reading a paper or code path.
Delegate before pulling the detail into the PI conversation. Use a fresh noninteractive
`traecli exec` on the PI host when the task needs independent context or a specific
model, including Gemini. Fresh means no inherited conversation or preferred answer;
it does not mean no primary evidence or no host instructions.

These are transport choices, not model roles. Keep a small task in the PI when
delegation would cost more than it saves. An unavailable tool or provider does not
block ordinary research.

For a fresh Trae child, select an available model explicitly when model identity matters:

```bash
traecli exec --model "<available model slug chosen by the PI>" \
  --config "model_instructions_file=\"$HOME/.trae/skills/research-pipeline/references/delegated-task.md\"" \
  --ephemeral --skip-git-repo-check --sandbox read-only \
  "<PI-authored transfer packet>"
```

Omit `--model` when the verified host default is suitable. Use the role context installed
on the caller's host; a Claude-led PI may read the same file under `~/.claude/skills`.
The read-only sandbox suits advisory work; use supported task-scoped permissions for
delegated implementation, never a blanket bypass. A plugin
or project-local install uses its actual skill directory instead of an assumed global
path. The per-call `model_instructions_file` override replaces the default main-session
addendum without changing global config. Do not append the main PI prompt as the child's
only role instruction. Hooks, project instructions, skills, and MCP still apply.

## Complete The Collaboration Loop

Use the native subagent's supported result/wait mechanism or collect the foreground
CLI call through exit. A delegation is complete when the PI has the result and has
checked the artifacts that matter. The child cannot reliably wake a Trae session
after the parent turn ends; do not treat “launched” as a completed handoff.

Keep claim-bearing long experiments under the persistent PI. A collaborator may implement,
debug, canary, and return a launch-ready package; the PI then uses
`experiment-operations` to register, launch, monitor, recover, and read the run. If a
delegated child unexpectedly detaches work, record its durable process or scheduler
identity and artifact paths, take monitoring ownership immediately, and do not create a
duplicate run. Continue useful independent research while it runs, or use a supported
wait with concise progress at meaningful changes. Submission to a worker is not the
end of the scientific episode.

Use the monitor's verified receipt and recovery path when the runtime cannot keep a
parent turn alive. A rate limit, forced turn boundary, or process exit must leave the
actual job and next action recoverable. Foreground delegation does not create a
cross-turn notification facility; use the available mechanism described in
`experiment-operations/references/monitor-experiment.md`.

When collaborator output returns, separate proposals from observed facts, verify code
and provenance, integrate only supported conclusions into the sole scientific state,
and continue the research. A collaborator response is an input to the next PI decision,
not the endpoint of the project.

## Independent Design Race

Run two bounded collaborators in parallel with separate fresh contexts, using the
host's subagents or fresh headless calls. Give both the same research question,
accepted comparison, strongest rival, relevant successes and failures, and real
constraints. Withhold each other's proposal and the PI's preferred answer until
each has independently offered an explanation, a concrete design, and an observable
consequence. Both are authors who can revise their designs, not reviewers assigned
to defend or attack a predetermined side.

Exchange the core mechanisms and predictions, not the full conversations. Ask
each author to use the evidence to challenge both proposals, preserve what works
in the rival design, and say what they would change in their own. If the designs
converge, preserve the shared insight rather than manufacturing disagreement. If
they diverge, inspect existing evidence for the observation that separates them.
When an implementation would resolve the live choice, have the collaborators
use the same validated substrate and comparison protocol in separate writable
paths. The PI owns claim-bearing runs; do not duplicate the baseline campaign
or change the evaluator to settle the race.

Collect the replies and artifacts through the existing collaboration loop. The PI
reconciles the evidence and takes the next action: adopt, revise, or set aside
the constructions according to what they explain and offer on the original task,
not how convincingly they were argued. Keep only the decision-relevant evidence
and rationale in the existing project state.

## Creative Co-Invention And A Gemini Entry Point

Creative collaboration is available to either lead PI and is not reserved to Gemini.
See [method-development](../../method-development/SKILL.md) for when a different
design is worth soliciting. Use Gemini for an open design choice, not for a routine
review of a design the PI has already chosen.

Invoke Gemini through the local `traecli exec` command on the persistent PI's host, not
by searching for a Gemini MCP tool or a script in each project. Resolve it with
`command -v traecli`, or use `$HOME/.local/bin/traecli` only after checking that it is
executable. A remote experiment worker need not have this CLI. Use `traecli exec --help`
and `traecli models --json` when command support or
model availability is uncertain. An installed executable is not proof of a successful
authenticated call: preserve the actual error and host if invocation fails. Sandbox
denials of log/state writes or a localhost listener are execution-permission problems,
not absence of an entry point; request the ordinary supported permission rather than
bypassing restrictions or installing a second copy. Do not invent a remote host route
when the current session cannot access the PI host.

Send the original problem, strongest rival, conflicting observations, and real
constraints, not a request to repair the current mechanism. Give Gemini room to explain
how the observations could coexist and propose a different design with a different
observable consequence. If the evidence already points to a clear repair, do it without
an invention call. Treat the return as a construction to consider and test, not as
evidence or an approval.

Use the verified headless invocation:

```bash
traecli exec --model Gemini-3.1-Pro-Preview \
  --config 'model_backend_variant="standard"' \
  --config "model_instructions_file=\"$HOME/.trae/skills/research-pipeline/references/delegated-task.md\"" \
  --ephemeral --skip-git-repo-check --sandbox read-only \
  "<PI-authored prompt>"
```

Pin the listed model slug explicitly; do not rely on the parent session's default model
or the deprecated `gemini-3.1-pro` alias. Explicit Standard Mode on the child prevents
an inherited Max Mode from triggering the CLI's persistent auto-correction of the
parent's configuration. Do not change the main session's model settings for a child.
Check the invocation metadata and errors for
routing or fallback, rather than asking the model to identify itself. Use a fresh child
call, never `resume` or the main session's ID. `--ephemeral` avoids persisting the child
conversation, but does not disable installed instructions, hooks, skills, or MCP servers.
Use the caller's installed role context (under `~/.trae/skills` for a Trae install).
The PI-authored prompt must establish a bounded creative co-PI task: use the supplied
evidence, return the requested contribution, do not take over the project or invoke other
models, and do not read files or use tools unless the PI explicitly delegates that work.
The read-only sandbox is not a universal tool-disable switch.

Run in the foreground through process exit and read the final response. For a durable
receipt, add `--output-last-message /absolute/path/gemini-reply.txt`; this separates the
final answer from startup logs and reasoning output. A nonzero exit, partial output, or
failed required dependency is not a successful delegation. Authentication, capacity,
transport, version, or routing failure is infrastructure; continue non-dependent research.

## Independent Codex Review

Independent verification is a task role, not GPT's permanent identity. A Claude-led
project may request it, while a GPT-led project can use a separate fresh reviewer
episode. The main GPT PI is not restricted to review. Independence comes from the
evidence packet and separate context, not merely a different provider name.

For a separate Codex judgment, use
`research-review/references/independent-review.md`. This collaboration reference owns
only the shared transfer and context boundaries; the review reference owns when a call
is justified and how its advice is synthesized.

## Transfer Packet

A useful bounded transfer contains enough information to work without inheriting the
entire conversation:

- original research arena and explicit boundaries;
- live scientific question and why it matters;
- accepted task, evaluator, and strongest published comparisons;
- raw evidence and contradiction relevant to the task;
- exact requested scientific or engineering deliverable;
- writable paths, resource facts, and completion artifacts.

Do not transfer old menus, reviewer rhetoric, failed candidate names, or a historical
chronology unless they are necessary to avoid repeating a known error.

## Protect The Main Context

Keep the original program, live question, strongest supporting and contrary evidence,
representative raw cases, method lineage, and next scientific action in the main
context. Save full logs, retries, dependency traces, and long tool output with the
delegated work or run. Return a compact account of what changed, what was verified
or remains unverified, and where the evidence lives. Surface any result that breaks a
premise of the pending work, even if the assigned task succeeded. Bring an execution detail back
when it changes validity, interpretation, or the next decision: a truncated input
belongs in the PI context; ten connection retries usually do not.

The PI reads the raw predictions, contrary cases, or training traces that determine
the scientific decision. Context isolation is not delegation of interpretation.
Withhold preferred framing when independence matters, not inconvenient evidence.

For project-wide foundation work, separate comprehensive coverage from loading every
file into one context. Map the project first; give readers the original arena and exact
comparison question, not an undifferentiated transcript. A bounded literature reader
reads complete assigned papers, appendices, and relevant code, returning source-backed
method and evaluation contracts to `research-foundation`. Another reader may inspect
the corresponding implementation or artifact lineage without inheriting a preferred
verdict. Store long extracts and logs outside the main conversation.

The PI owns the shared task, method selection, matrix, adaptations, and unresolved
comparability questions. Verify decisive source or code locations when a returned
contract is uncertain or conflicts with another; synthesis is not voting over summaries.
Do not require a fresh session after each paper or duplicate one live scientific state
per reader. Refresh the concise comparison account when evidence changes so context
compression preserves the research decisions and contrary evidence, not only the latest
reader's framing.

## Refresh A Scientific Episode

Ordinary interruption or compaction calls for re-anchoring from current authority,
concise state, relevant raw artifacts, and active execution facts. Start a fresh
scientific episode when the old narrative has become a worse evidence index than a new
one: central evidence or the evaluator was invalidated; the governing primitive,
operational effect, or paper identity materially changed; the user transfers project
leadership to a different main session; the work enters submission maturation;
or repeated compaction, invented paths, duplicate actions, or forgotten contrary
evidence has made continuity unreliable.

A bounded collaborator return is not a leadership transfer and does not itself require
a fresh PI session. Model switching is not a reason to discard valid evidence.

Before that boundary, update the sole project state from artifacts and preserve active
process identities. Include completed but unread results, pending manuscript updates,
unresolved baseline deviations, the reason for the next action, and durable user
protocol changes in their existing owners. A receiving PI reconciles these against
current evidence and resolves contradictory summaries before dependent work; the
handoff is not just the previous session's bug list. Distinguish human messages from
runtime injections, approval-agent transcripts, and replayed history when recovering
intent. The receiving context does not inherit certainty, closure language, or maturity
from conversation history. Running
sessions do not absorb changed skills automatically: after the current atomic action,
explicitly reread any changed canonical skill that affects the work. Do not interrupt a
valid experiment merely to refresh its surrounding context.
