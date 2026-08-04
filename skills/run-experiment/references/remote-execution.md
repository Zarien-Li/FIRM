# Remote execution

## Preflight

On the remote target, verify:

- hostname and working directory;
- environment/container activation;
- code revision or synchronized file set;
- dataset/checkpoint accessibility;
- `nvidia-smi` or equivalent device state;
- disk space on the actual output filesystem;
- existing sessions and processes owned by this project.

Use non-interactive commands only when authentication is already configured. Never
embed passwords, tokens, or private keys in command text.

## Rsync pattern

Preview first:

```bash
rsync -avn --delete-delay \
  --exclude '.git/' --exclude '.env' --exclude 'data/' \
  --exclude 'checkpoints/' --exclude '__pycache__/' \
  ./ user@host:/approved/project/path/
```

Remove `-n` only after the preview matches the intended files. Avoid `--delete`
unless the user explicitly approved deletion semantics.

## Durable launch pattern

Prefer the project's approved process manager. A generic `tmux` example:

```bash
tmux new-session -d -s EXPERIMENT_ID \
  'cd /approved/project/path && bash runs/EXPERIMENT_ID/command.sh \
   > runs/EXPERIMENT_ID/stdout.log 2> runs/EXPERIMENT_ID/stderr.log'
```

Then verify the session, process, log, and GPU. Do not assume the shell initialized
conda or environment modules; activate them explicitly in `command.sh`.

## Attribution on shared servers

When multiple researchers share one Linux account or container, attribute a job by
its project path, current working directory, command, and run metadata—not only by
the Linux username or container name.
