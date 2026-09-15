# Agent Memory

Agent memory keeps useful experience outside the base model so that behavior can improve without retraining. Practical systems combine working context, episodic records, semantic facts, and procedural knowledge.

## Memory pipeline

1. Observe and extract candidate memories.
2. Attach provenance, time, subject, confidence, and consent scope.
3. Consolidate duplicates and resolve conflicts without hiding history.
4. Retrieve by relevance, recency, importance, and task context.
5. Evaluate downstream utility; decay, archive, edit, or delete when appropriate.

Begin with Generative Agents, MemGPT, HippoRAG, and LongMemEval in the [main list](../README.md).
