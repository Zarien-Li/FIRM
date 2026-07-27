# 90-Second Demo Script

Target duration: 85-90 seconds. Record at 1920x1080 or 1440x900 with terminal
font at least 18 px. Use captions even when voice-over is present.

Run `make demo` for the timed 90-second terminal storyboard. Use
`DEMO_SPEED=0 bash demo/demo.sh` for an instant rehearsal.

## Timeline And Voice-Over

### 0-8s: The problem

**Screen:** README hero, then `FAILURE_MAP.md`.

**Voice-over:** "Auto-research rarely fails because the agent cannot launch an
experiment. It fails after the first method loses, when the project drifts, or
when a draft becomes more important than the evidence."

### 8-20s: Attach to a project

**Screen:**

```bash
git clone https://github.com/Zoiya-Li/FIRM.git ~/FIRM
~/FIRM/firm init ~/research/my-project
```

Show the final `Verification passed` output and the generated research card,
first-message templates, and project-local skill directory.

**Voice-over:** "FIRM attaches to a real research project. It preserves
existing instructions, installs local skills, creates the research-program
card, and verifies itself."

### 20-36s: What 100B+ tokens bought

**Screen:** Scroll the Failure Map entries for seed drift, premature closure,
probe addiction, and late integrity failure.

**Voice-over:** "These rules were not written in one sitting. They were revised
through more than one hundred billion model tokens of live research, exposing
where agents repeatedly lose scientific judgment."

### 36-64s: The case

**Screen:** Open `demo/fixture/RESULT.md`, highlighting baseline 72.4 and method
69.1. Then paste `demo/fixture/PROMPT.md` into Claude Code. Cut to the agent's
three key decisions and the updated compact research state.

**On-screen captions:**

1. "One clear loss diagnoses the realization."
2. "Do not sweep seeds. Do not close the field."
3. "Repair the component the evidence implicates."

**Voice-over:** "Here the first method loses. A typical agent either abandons
the field or runs more seeds. FIRM separates statistical uncertainty
from design uncertainty, preserves the research program, and turns the loss
into the next constructive ablation."

### 64-79s: Independent second PI

**Screen:** Open the `research-review` decision sequence:
`Prize / Fidelity / Entry -> Interpret -> Invent -> Attack`.

**Voice-over:** "An independent model enters early as a second PI: does the
best-case result matter, does the project still honor its seed, and what
stronger method follows?"

### 79-90s: Close

**Screen:** Return to README hero and GitHub star button.

**Voice-over:** "FIRM is not another loop. It is the research judgment
needed to survive many loops. Open source now."

**Final caption:** "Inherit the failure map. Do not pay to rediscover it."
