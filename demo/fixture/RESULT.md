# Development Result

| System | Task success | Invalid state changes | Training status |
|---|---:|---:|---|
| Strong matched baseline | 72.4% | 3.1% | converged |
| Routing prototype v1 | 69.1% | 3.0% | converged |

The paired difference is large enough to diagnose this realization. Training
loss and validation behavior are stable. The prototype changes routing
entropy, but not the action-state errors it was designed to repair.
