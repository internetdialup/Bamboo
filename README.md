# Documentation.md

Canonical documentation and agent-governance starter for AI-assisted repositories.

## What This Repo Is

`Repository-md` is the source repo for a reusable documentation system. It is meant to be forked or copied into project repos so agents and humans inherit the same operating rules, shared vocabulary, and handoff patterns across vendors.

The policy source lives in `Documentation.md`.
Agents start in `AGENT.md`.
Recent state for this repo lives in `docs/memory-context/context-orientation.md`.

## What It Includes

- `behavior/` for context, memory, and reasoning rules
- `workflows/` for repeatable setup and delivery procedures
- `skills/` for portable capabilities and overlays
- `architecture/` for memory-system and workflow architecture
- `agent-architecture/` for multi-agent roles, topology, and coordination patterns
- `design/` for UI and visual guidance when a repo needs it
- `docs/` for this repo's own map and change log

These modules are reusable, but downstream repos should only copy the parts they actively need.

## How To Adopt It

1. Copy `Documentation.md`, `README.md`, `AGENT.md`, and `docs/context-orientation.md`.
2. Bring over only the folders the project needs.
3. Rewrite the project `README.md` immediately so it describes the actual product or workspace.
4. Keep `AGENT.md` short and repo-specific.
5. Add real working folders early so the repo is not mostly governance docs.

This repo keeps its own operational log under `docs/memory-context/`, but the default downstream template contract stays `docs/context-orientation.md` unless a project explicitly chooses a different layout.

## Who It Is For

- teams running multiple agent vendors
- repos that need durable handoff and context discipline
- projects that benefit from reusable Skills and workflow docs
- maintainers who want consistent repo initialization without rebuilding the docs system each time

## About

Created and maintained by Matt Stenquist.

## Recent Milestones

- 2026-06-03: Introduced a literal root `Documentation.md` and separated policy from README and cold-start routing.
- 2026-05-30: Added PRD and TDD workflow documents.
- 2026-05-28: Added Watchdog and Drift to the memory architecture layer.
- 2026-05-16: Reworked context documents, updated the Skills folder, and added `AGENT.md`.
- 2026-05-11: Initial release.
