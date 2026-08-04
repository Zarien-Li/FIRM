# Development Result

One paired development run was completed under the same data, training budget,
checkpoint, preprocessing, and evaluator.

| System | Task success | Invalid state changes | Training status |
|---|---:|---:|---|
| Strong matched baseline | 72.4% | 3.1% | converged |
| Routing prototype v1 | 69.1% | 3.0% | converged |

The intended code path executed. Training loss and validation behavior were stable
for both systems. The prototype produced a clear change in routing entropy, but no
meaningful reduction in the action-state errors it was designed to repair.

Only one paired seed has been run. No claim about the variance of the final task
metric has been established.
