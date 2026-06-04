# Project Setup

This workflow is procedural. It explains how to initialize a new repo using the `Documentation.md` system. Durable policy lives in `Documentation.md`, not here.

## Goal

Create a repo that is easy for humans and agents to enter, has the minimum governance layer, and includes the actual working structure for the product from the start.

## Procedure

1. Establish the repo type.
   Determine whether the repo is an application, research workspace, design system, library, or another structure the user already chose.
2. Create the minimum governance layer.
   Add `README.md`, `AGENT.md`, and `docs/context-orientation.md`.
3. Add `Documentation.md` if this repo will carry a local operating spec.
   Keep it repo-specific and aligned with the canonical contract.
4. Create only the working folders the repo needs.
   Examples: `src/`, `tests/`, `config/`, `research/`, `data/`, `design/`, `scripts/`.
5. Localize the root docs immediately.
   Rewrite `README.md` so it describes the actual repo, and trim `AGENT.md` so it routes to the right materials without restating broad policy.
6. Add environment-safe scaffolding.
   Use `.env.example` when environment variables are needed. Do not commit `.env` files unless the user explicitly instructs it.
7. Document the initial state.
   Add the first entry to `docs/context-orientation.md` with the repo purpose, structure, and current working boundaries.
8. Add optional modules only if they will be used.
   Bring in `behavior/`, `workflows/`, `skills/`, `architecture/`, or `design/` selectively.

## Setup Checklist

- root docs exist and have distinct roles
- working folders match the actual project
- no secrets are committed
- context log exists and starts with a concrete bootstrap entry
- optional modules are present only when justified
- the repo can be understood without reading generic template material first

## Notes

- Branch naming, versioning, licensing, CI, and release discipline should follow the project's own needs.
- If a forked project needs different procedures, define them locally in that project's `workflows/`.
- This canonical source repo stores its own state log under `docs/memory-context/`, but the default project setup contract for downstream repos stays `docs/context-orientation.md`.
