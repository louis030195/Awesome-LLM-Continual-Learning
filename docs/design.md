# Repository Design

## Goals

Maintain an auditable public map of LLM continual learning that supports both academic discovery and personal reading workflows.

## Architecture

YAML files under `data/` are the source of truth. Python modules validate schema and references, then deterministically render managed sections in the English and Chinese README files. Topic guides explain conceptual boundaries; reading lists provide curated routes; public notes are opt-in.

## Editorial principles

1. Prefer primary sources and stable URLs.
2. Separate papers from industrial implementations.
3. Label evidence and limitations; inclusion is not endorsement.
4. Keep generated views reproducible and review source-data diffs.
5. Treat provenance, consent, deletion, and reversibility as core continual-learning requirements.

The full approved implementation specification and plan are maintained as task artifacts outside the public repository until publication review.
