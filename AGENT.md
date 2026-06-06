# AGENT.md

You are an agent. This file is the cold-start router.

If you need repo purpose or adoption guidance, read `README.md`.
If you need policy, roles, or fork rules, read `Documentation.md`.

Order of operations on first contact:

## 1. Read the policy source

Read `Documentation.md` to understand the repo contract, document roles, and mandatory rules.

## 2. Read behavior/

Read `behavior/` when you need the reasoning and context rules behind the system vocabulary. Documents in this folder use the `ctx-` prefix (CTX = Context); the full glossary lives in `behavior/ctx-rules.md`.

## 3. Read docs/memory-ctx/ctx-orientation.md

Read `docs/memory-ctx/ctx-orientation.md` for this repo's current state and most recent structural changes.

## 4. Pull architecture/ only when memory itself is the work

Load `architecture/` when the task touches memory architecture, ADM, RAG, drift, Watchdog, audits, or workflow governance.

## 5. Pull agent-architecture/ when the task is multi-agent coordination

Load `agent-architecture/` when the work is about agent identity, topology, orchestration, role boundaries, or handoff structure.

## 6. Load relevant Skills and workflows

Pull from `skills/` and `workflows/` only as the task requires. Do not ingest them just because they exist.

## 7. Skip design/ unless the task is design work

Treat `design/` as optional cold-start material.

This repo is the canonical documentation source, not a product repo. Keep the cold start lean and pull only the modules required for the task.
