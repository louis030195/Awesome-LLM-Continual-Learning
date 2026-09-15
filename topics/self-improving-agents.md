# Self-Improving Agents

Self-improving agents turn outcomes into reusable feedback, skills, memory policies, code, or model updates. Improvement claims require a held-out evaluation loop and controls against reward hacking.

## Safety envelope

- Run changes in a sandbox with explicit budgets and permissions.
- Preserve provenance and reversible checkpoints.
- Separate the system proposing changes from the evaluator approving them.
- Test regressions, security, and distribution shift—not only average task score.

Reflexion provides a non-parametric baseline; SEAL, Memory-R1, AgeMem, and Darwin Gödel Machine explore increasingly autonomous update loops.
