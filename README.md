# Awesome LLM Continual Learning

> A curated, evidence-aware map of continual learning, memory, personalization, and self-improving language agents.

[中文](README.zh-CN.md) · [Topics](#topics) · [Reading lists](#reading-lists) · [Industry](industry/README.md) · [Contributing](CONTRIBUTING.md)

This documentation-first repository tracks academic and industrial progress in a deliberately simple structure: the READMEs are the curated index, topic pages explain the landscape, and reading lists turn discovery into a repeatable learning workflow.

## Topics

- [Parametric continual learning](topics/parametric-continual-learning.md)
- [Agent memory](topics/agent-memory.md)
- [Personalization](topics/personalization.md)
- [Self-improving agents](topics/self-improving-agents.md)
- [Evaluation and benchmarks](topics/evaluation-benchmarks.md)

## Papers

### Surveys & Foundations

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2024 | [Continual Learning of Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2404.16789) | preprint | P0 | B | A broad taxonomy of continual-learning settings, methods, and evaluation for LLMs. |

### Parametric Continual Learning

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2025 | [TiC-LM: A Multi-Year Benchmark for Continual Pretraining of Language Models](https://arxiv.org/abs/2504.02107) | preprint | P1 | B | Evaluates continual pretraining on temporally evolving corpora over multiple years. |
| 2024 | [InsCL: A Data-efficient Continual Learning Paradigm for Fine-tuning Large Language Models with Instructions](https://arxiv.org/abs/2403.11435) | preprint | P1 | B | Uses instruction data to study efficient sequential adaptation. |
| 2023 | [ConPET: Continual Parameter-Efficient Tuning for Large Language Models](https://arxiv.org/abs/2309.14763) | preprint | P1 | B | Studies parameter-efficient adaptation across a stream of tasks. |

### Test-Time Learning

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2026 | [OAKS: Continual Test-Time Adaptation for Language Models](https://arxiv.org/abs/2603.07392) | accepted | P0 | A | A recent continual test-time adaptation result that connects online updates with retention. |
| 2025 | [Nested Learning: The Illusion of Deep Learning Architectures](https://arxiv.org/abs/2512.24695) | preprint | P1 | B | A recent perspective on learning systems composed of interacting optimization processes. |
| 2025 | [Self-Adapting Language Models](https://arxiv.org/abs/2506.10943) | accepted | P0 | A | Explores models that generate their own update data and learning directives at test time. |
| 2025 | [Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663) | preprint | P0 | B | Treats a neural long-term memory module as an online learner. |

### Agent Memory

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2025 | [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | preprint | P1 | B | Builds dynamic note links and evolves memory organization as experience accumulates. |
| 2025 | [MemoryOS: An Operating System for Personalized AI Memory](https://arxiv.org/abs/2506.06326) | preprint | P1 | B | Proposes tiered memory storage and lifecycle management for personalized assistants. |
| 2025 | [MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724) | preprint | P0 | B | Presents memory as a first-class system resource with unified lifecycle management. |
| 2025 | [MIRIX: Multi-Agent Memory System for LLM-Based Agents](https://arxiv.org/abs/2507.07957) | preprint | P1 | B | Separates memory responsibilities across specialized agents and memory types. |
| 2025 | [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) | preprint | P1 | B | Uses temporally aware knowledge graphs for changing facts and conversational memory. |
| 2024 | [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://arxiv.org/abs/2405.14831) | published | P0 | A | Connects knowledge graphs and personalized PageRank to associative long-term retrieval. |
| 2023 | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | published | P0 | A | Introduces the observation, reflection, and planning loop that shaped agent-memory systems. |
| 2023 | [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | preprint | P0 | B | Frames context management as a tiered virtual-memory problem for long-lived agents. |

### Memory Management

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2026 | [AgeMem: Learning to Manage Agent Memory with Experience](https://arxiv.org/abs/2601.01885) | preprint | P0 | B | A 2026 direction for learning memory policies from agent experience. |
| 2025 | [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) | preprint | P1 | B | Learns memory operations and answer behavior jointly with reinforcement learning. |

### Personalization

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2025 | [PERSONAMEM: Evaluating Personalized Memory for Long-Term Dialogue Agents](https://arxiv.org/abs/2504.14225) | preprint | P1 | B | Connects long-term memory quality to persona-consistent personalized interaction. |
| 2025 | [PrefEval: A Benchmark for Evaluating Personalized Preference Following in Large Language Models](https://openreview.net/forum?id=UqjPpZyW6Z) | published | P1 | A | Tests whether models infer and follow user preferences across interactions. |
| 2024 | [LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/) | published | P0 | A | A foundational benchmark for profile-conditioned personalized language tasks. |

### Self-Improving Agents

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2026 | [SkillLearnBench: Evaluating Continual Skill Learning in Language Agents](https://cxcscmu.github.io/SkillLearnBench/) | preprint | P1 | B | Evaluates whether agents acquire and reuse skills across an evolving task stream. |
| 2025 | [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) | accepted | P0 | A | Studies empirical self-modification with an archive of agent variants and evaluation feedback. |
| 2023 | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | published | P0 | A | Demonstrates improvement through stored natural-language feedback without weight updates. |

### Evaluation & Benchmarks

| Year | Paper | Status | Priority | Evidence | Why read |
|---:|---|---|:---:|:---:|---|
| 2025 | [MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://github.com/HUST-AI-HYZ/MemoryAgentBench) | preprint | P1 | B | Tests retrieval, selective forgetting, conflict handling, and long-range memory behavior. |
| 2025 | [RECALL: A Benchmark for Continual Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.829/) | published | P1 | A | Measures acquisition and retention under sequential learning conditions. |
| 2024 | [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://aclanthology.org/2024.acl-long.747/) | published | P0 | A | A long-conversation benchmark for question answering, event summarization, and temporal understanding. |
| 2024 | [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://openreview.net/forum?id=pZiyCaVuti) | published | P0 | A | Tests information extraction, multi-session reasoning, temporal reasoning, and abstention over long histories. |

## Industry updates

| Project | Organization | Kind | Evidence | Summary | Caveat |
|---|---|---|:---:|---|---|
| [Graphiti](https://github.com/getzep/graphiti) | Zep | open-source | B | A temporal knowledge-graph engine designed for changing facts and agent memory. | Graph construction and entity resolution add operational and quality trade-offs. |
| [Hyperconsciousness](https://github.com/louis030195/hyperconsciousness) | Louis Beaumont | open-source | B | Rust knowledge store with encrypted, signed append-only records, device sync, and scoped, expiring MCP access grants. | Developer alpha; grants do not sandbox local processes, and hosted models can see returned plaintext. |
| [LangMem](https://github.com/langchain-ai/langmem) | LangChain | open-source | B | Utilities for extracting, consolidating, and using long-term memories in agent workflows. | Framework integration can couple memory semantics to a particular orchestration stack. |
| [Letta](https://github.com/letta-ai/letta-code) | Letta | platform | B | Open-source framework descended from MemGPT for building stateful agents with managed memory. | Features and hosted-service behavior evolve; verify against current documentation before adoption. |
| [Mem0](https://github.com/mem0ai/mem0) | Mem0 | open-source | B | A memory layer and service for extracting and retrieving user- and agent-specific memories. | Benchmark results depend heavily on extraction, retrieval, and evaluation settings. |
| [MemoryOS](https://github.com/BAI-LAB/MemoryOS) | BAIR-NLP | research-release | B | A tiered memory architecture aimed at long-term personalized AI interaction. | Research prototype; repository availability and APIs should be rechecked before use. |
| [MemOS](https://github.com/MemTensor/MemOS) | MemTensor | research-release | B | A research system treating memory objects and their lifecycle as operating-system resources. | Early-stage research software; validate interfaces and production readiness independently. |
| [MIRIX](https://github.com/Mirix-AI/MIRIX) | MIRIX-AI | research-release | B | A multi-agent memory architecture separating multiple forms of long-term memory. | Claims are primarily supported by the associated preprint and project artifacts. |

## Reading lists

- [Essential 8](reading-lists/essential-8.md)
- [2025–2026 Frontier](reading-lists/2025-2026-frontier.md)
- [Public reading notes](notes/README.md)

## Scope and evidence

Items are labeled with evidence levels: **A** for peer-reviewed or primary official evidence, **B** for credible preprints or official technical releases, and **C** for early or secondary signals. Inclusion is not endorsement.

## License

The curated metadata and documentation are released under [CC0 1.0](LICENSE). Individual papers, codebases, and products retain their own licenses.
