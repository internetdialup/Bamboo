# Repo Organization

A map of this repository. It describes what each folder is for, what lives inside it, and the order an agent (or a human) should consult things when picking the repo up cold. Pair this with `AGENT.md` at the root, which is the operational cold-start file. `AGENT.md` tells an agent *how* to enter the repo. This file tells it *where things are*.

This is `Bamboo.md`. Not a project repo. It is the canonical library of `.md` files that get forked into projects to give AI agents a consistent set of standards across vendors. `Bamboo.md` at the repo root is the policy source. `README.md` is the human overview. `AGENT.md` is the cold-start router.

---

## Top-level layout

```
Repository-md/
├── Bamboo.md            # Canonical operating spec for repos using this system
├── README.md                    # What this repo is, who it's for, what it does
├── AGENT.md                     # Cold-start router for any agent landing in the repo
├── CLAUDE.md                    # Claude-specific cold-start overlay (sits on top of AGENT.md)
├── REPORTING_TEMPLATE.md        # The Layered Reporting Template
├── LICENSE
├── behavior/                    # The rules an agent obeys. Cold-start required.
│   ├── ctx-rules.md             # Hard operational rules and constraints.
│   ├── ctx-lexicon.md           # The decoder ring (3-Concept Canon).
│   ├── ctx-entropy.md           # The preservation view (LTIP/PLTRF).
│   ├── persona-layer.md         # Identity boundaries and placement.
│   └── user-model.md            # User behavior and psychology modeling.
├── bamboo-os/                   # ADVANCED EXTENSION. Runtime engine and multi-agent OS.
│   ├── FRAMEWORK.md             # Operational Governance Protocol (The Law)
│   ├── agent-architecture/      # Role design and topology
│   ├── scripts/                 # Governance scripts (Governor, Orchestrator)
│   ├── tools/                   # Sidecars (Watcher)
│   ├── event_calendar.yaml      # Catalyst Loader
│   └── .bamboo/                 # Runtime state (Agent Bus)
├── development/                 # Implementation standards and engine specs.
│   ├── unity-development.md     # Structural discipline for Unity.
│   ├── unrealengine-development.md # Governance for UE5.
│   └── app-development.md       # Generic app standards.
├── docs/                        # Operational memory for this repo itself
│   ├── repo-organization.md     # ← this file. The map.
│   └── memory-ctx/
│       ├── ctx-orientation.md   # Hot per-Knob change log.
│       └── ctx-ori-summary-2.md # Cold storage for older Knobs.
├── architecture/                # ADVANCED ADD-ON. ADM/RAG, Watchdog, workflow tools.
│   ├── workflow-tools.md        # Tool/workflow memory friction.
│   └── memory/                  # Memory operating layer.
├── skills/                      # Portable AI capabilities. Cross-vendor.
├── workflows/                   # DevOps and project lifecycle patterns.
└── design/                      # Project-specific UI/UX rules.
```

---

## bamboo-os/ — advanced extension

The **Bamboo OS** provides the runtime engine for high-velocity or multi-agent squads. **Simple or single-agent projects should delete this folder on fork.**

- `FRAMEWORK.md` — the Operational Governance Protocol. Codifies the Resource, Persistence, and Structural Verification mandates as foundational laws.
- `agent-architecture/` — multi-agent role design and orchestration.
  - `agent-identity.md` — how an agent adopts a role-shaped working identity.
  - `agent-topology.md` — the coordination model: role lanes, ownership, and anti-conflict rules.
  - `agent-mms.md` — the Agent Memory Management System.
  - `psc-contract.md` — the Persona Stratification Contract. Defines the 3-layer identity protocol and the Interface vs. Implementation Doctrine.
  - `latency-governance.md` — Latency-Based Governance (Reasoning-depth limits).
  - `bamboo-orchestrator.md` — defines the Orchestrator lifecycle (Pulse/Heartbeat).
  - `state-bus.md` — defines the `STATE.json` serialization protocol.
- `scripts/` — implementation scripts for the Governor, Orchestrator, and Auditor.
- `tools/` — implementation scripts for the Bamboo Watcher.
- `event_calendar.yaml` — the agnostic catalyst loader.

---

## development/

Implementation and engine-specific governance. Use these to establish the structural guardrails for specific tech stacks.

- `unity-development.md` — structural discipline for Unity projects. Defines the Scene Knob, Prefab Stratification, and `.meta` hygiene.
- `unrealengine-development.md` — governance for UE5 projects. Blueprint vs. C++ stratification and redirector hygiene.
- `app-development.md`, `web-development.md`, `nextjs-development.md`, `swift-development.md` — implementation standards for various stacks.

---

## behavior/

The foundational rules. Everything an agent has to internalize before it touches the rest of the repo. Read this first on cold start.

- `ctx-rules.md` — hard operational rules and binary structural requirements.
- `ctx-lexicon.md` — the decoder ring. Single canonical home for the 3-concept canon (**Knob**, **PLTRF**, **Hot/Warm/Cold**).
- `ctx-entropy.md` — the preservation view. Defines PLTRF and memory tiering.
- `persona-layer.md` — the Persona Layer rules. Codifies the boundary between persona-rich repo layers and persona-free inherited canon.
- `user-model.md` — how the agent reads, models, and adapts to the user.

---

## Maintenance rules

- New folder or moved file gets map updates in the same change.
- One canonical home per concept (PLTRF).
- Broken pointers are build failures.
- This file gets re-audited every few Knobs. Stale maps are worse than no map.
