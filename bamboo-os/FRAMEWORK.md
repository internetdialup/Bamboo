# Bamboo Operational Governance Framework

The **Bamboo Framework** provides structural guardrails for AI-assisted repositories. It prioritizes binary, script-verifiable logic over narrative liturgy.

## 1. The Three Structural Requirements

Every Bamboo-compliant system must satisfy these requirements:

### 1.1 Resource Governance (The Ceilings)
- **Requirement**: The system MUST define resource ceilings (RAM/CPU/Disk).
- **Verification**: Ceilings must be codified in a configuration file (e.g., `watcher.config.json`) and monitored by a script (e.g., `scripts/bamboo_orchestrator.py`).
- **Optional**: Breach of ceilings may trigger an automated environment reset (Implementation-specific).

### 1.2 Memory Governance (The State-Bus)
- **Requirement**: The system MUST maintain a `STATE.json` for session continuity.
- **Verification**: Presence of a non-empty `STATE.json` after every analysis cycle.
- **Failure State**: A system without a valid state file cannot resume; it must undergo a full cold start.

### 1.3 Communication Governance (Structural Verification)
- **Requirement**: Every agentic claim MUST reference a specific file path or shell output.
- **Verification**: The report must contain at least one valid repo-relative path or command result.
- **Failure State**: Claims without evidence are rejected as "Liturgy."

---

## 2. The Agnostic Heartbeat

Cognitive integrity is maintained through a **BambooHeartbeat** (`scripts/bamboo_governor.py`). Its job is not to "grade tone," but to verify binary invariants:
1.  **PSC Verification**: Are the Identity and Role layers anchored in global/local files?
2.  **PLTRF Audit**: Are all repo references valid and maps accurate?
3.  **Path Citation**: Did the last agent interaction name the files it touched?

---

## 3. The 3-Concept Canon

To ensure cold-start efficiency, Bamboo recognizes only three load-bearing concepts:
- **Knob**: The unit of change (narrated in the log).
- **PLTRF**: The binary discipline of repo integrity (one home per concept).
- **Hot/Warm/Cold**: The memory preservation tiers.

All other terminology is considered decorative or project-specific.

---

Bamboo is not a philosophy; it is a structural OS for AI agents.
