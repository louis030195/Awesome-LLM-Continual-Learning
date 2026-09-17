# Parametric Continual Learning

Parametric continual learning updates model weights as data, tasks, or time periods arrive. The central tension is plasticity versus stability: acquire useful behavior without erasing prior capabilities.

## Questions to track

- Which parameters change: full model, adapters, experts, or external update modules?
- Is replay allowed, and how are privacy and data retention handled?
- Are retention and backward/forward transfer measured after every stage?
- Can an update be audited, reverted, or selectively forgotten?

## Suggested path

Start with the [survey in the main list](../README.md#surveys--foundations), then compare ConPET and InsCL with temporal continual pretraining benchmarks such as TiC-LM and RECALL. Treat test-time weight updates as a related but higher-risk branch.
