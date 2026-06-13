# State-Bus Protocol

The **State-Bus Protocol** is the serialization mechanism that allows Bamboo agents to maintain state continuity across session resets, worker crashes, or machine reboots. It ensures that an agent's "Working Memory" can be reconstituted from a durable, versioned file.

## 1. The STATE.json Schema

The State-Bus utilizes a standardized JSON schema (`STATE.json`) to store the agent's current operational posture.

```json
{
  "protocol_version": "1.0.0",
  "timestamp": "ISO-8601-DATETIME",
  "active_knob": "KNOB_NAME",
  "persona": {
    "identity": "IDENTITY_LAYER",
    "role": "ROLE_LAYER",
    "tactical_posture": "SAMANTHA|DANIEL"
  },
  "operational_state": {
    "last_analysis_pulse": "TIMESTAMP",
    "heartbeat_status": "OK|WARN|ERROR",
    "pending_directives": ["TASK_ID_1", "TASK_ID_2"],
    "completed_directives": ["TASK_ID_3"]
  },
  "resource_metrics": {
    "ram_usage": "MB",
    "cpu_load": "PERCENTAGE",
    "latency_budget_spent": "TOKEN_COUNT"
  }
}
```

---

## 2. Serialization Discipline

- **Frequency**: The Orchestrator serializes to the State-Bus at the end of every **Analysis Pulse** or upon a **Knob Transition**.
- **Atomic Writes**: To prevent state corruption, the State-Bus uses atomic file-writing protocols (write-to-temp-then-move).
- **Versioning**: Each state object includes a `protocol_version`. If a project's logic changes, the Orchestrator must handle migration or a clean reset of the State-Bus.

---

3. **The "Resume" Mechanism**

On session wake, the agent's first tactical task is to consult the State-Bus:
1.  **Read**: Load `STATE.json`.
2.  **Verify**: Run the **Doctrine Auditor** (`bamboo_contract.py`) against the loaded state.
3.  **Reconstitute**: Populate the working memory with the `pending_directives` and `active_knob` data.
4.  **Announce**: Narrate the resumption (e.g., "Agent: [ACTIVE] Resuming from State X").

---

## 4. Isolation

Each track or lane in a **Multi-Track Workspace** must have its own isolated State-Bus (e.g., `STATE_RESEARCH.json`, `STATE_EXECUTION.json`) to prevent state-collision across parallel lanes.

---

## Conclusion

The State-Bus Protocol transforms AI agents from "Stateless Transients" into "Durable Workers." It is the persistent link between an agent's working context and the repository's long-term memory.

The discipline is structural.
