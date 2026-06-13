# Bamboo Orchestrator (The Chassis)

The **Bamboo Orchestrator** is the "Chassis" of the repository. It is the operational DNA that manages the lifecycle of AI agents, ensuring they remain resource-contained, performant, and synchronized with the repository's state.

## 1. Dual-Loop Architecture

The Orchestrator operates on a dual-loop system to separate reasoning from health monitoring:

### 1.1 The Analysis Pulse
- **Frequency**: Configurable (e.g., every 60 seconds or on file-change).
- **Function**: Triggers the agent's reasoning cycle. It reads the current context, evaluates the active Knob, and executes tactical tasks.
- **Governance**: Adheres to **Latency-Based Governance** reasoning-depth limits.

### 1.2 The Resource Heartbeat
- **Frequency**: High-frequency (e.g., every 5 seconds).
- **Function**: Monitors system health (RAM, CPU, Disk) and verifies agent "Liveness."
- **Governance**: Triggers **Resource Guards** if limits are exceeded.

---

## 2. Resource Guards

To prevent context-window collapse or system-level resource exhaustion, the Orchestrator enforces strict limits using the **Resource Guard** protocol:

- **RAM Cap**: Monitors memory usage. If the agent's working memory exceeds the project-defined budget, the Orchestrator may trigger an emergency **Neural Reset** or **Compression Sweep**.
- **CPU Cap**: Limits reasoning-heavy processes to prevent system-wide lag.
- **Disk Cap**: Ensures logs and temporary context files do not saturate storage.

---

## 3. Priority Signaling (MAP)

The Orchestrator utilizes the **Multimodal Alerting Protocol (MAP)** to signal state changes. Specific projects may use audio cues (e.g., different voices for high-priority vs. routine alerts) to triage notifications.

---

## 4. Self-Healing Loop

The Orchestrator includes a **Self-Healing Loop** that monitors sub-agent processes and worker threads.
- **Detection**: Identifies crashed workers or stalled "Thinking" loops.
- **Action**: Attempts a **Hot-Reload** by reading the last serialized state from the **State-Bus**.

---

## 5. Agnostic Event Logic (Catalysts)

The Orchestrator remains project-agnostic by loading its event calendar from `event_calendar.yaml`.

- **Concept**: The user defines "Catalysts" (e.g., "Daily Backup," "Email Sweep") in the YAML file.
- **Logic**: The Orchestrator monitors these timestamps and triggers the relevant Tactical tasks when the Catalyst fires.

---

## 6. Implementation

The base class lives at `scripts/bamboo_orchestrator.py`. Specific projects must import and subclass this chassis to add their proprietary execution logic.

The OS is active.
