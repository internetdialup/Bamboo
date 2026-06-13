# Persona Stratification Contract (PSC)

The **Persona Stratification Contract (PSC)** is the three-layer agent boot-up protocol that ensures cognitive integrity across project boundaries. It prevents "Context Amnesia" by anchoring an agent's core identity globally while allowing for project-specific role adaptation and tactical task execution.

## 1. The Three-Layer Protocol

For an agent to achieve synchronization on session wake, it must resolve its stratification in this specific order:

### 1.1 The Identity Layer (The "Soul")
- **Home**: Global configuration (`~/.gemini/gemini.md` or equivalent).
- **Function**: Defines the agent's fundamental character, tone, and long-term memory.
- **Example**: "Generalist Agent" — direct, high-signal, performance-oriented.
- **Integrity Rule**: This layer is immutable at the project level. It survives across all repositories.

### 1.2 The Role Layer (The "Job")
- **Home**: Project-specific memory (`MEMORY.md` or `AGENT.md`).
- **Function**: Defines the agent's lane within a specific repository's topology.
- **Example**: "Security Auditor" or "Frontend Developer."
- **Integrity Rule**: This layer is local to the repository and defines the ownership boundaries for that specific "Knob."

### 1.3 The Tactical Layer (The "Tasks")
- **Home**: Active session context (Current user prompt / directives).
- **Function**: Defines the immediate objective using the **Directive vs. Inquiry** distinction.
- **Directive**: A command to perform an action (e.g., "Implement X").
- **Inquiry**: A request for analysis or research (e.g., "How does X work?").
- **Integrity Rule**: Directives require execution; Inquiries require reporting. Never confuse the two.

---

## 2. Interface vs. Implementation Doctrine

The PSC enforces a strict separation between communication protocols and proprietary implementation logic to prevent context saturation.

- **The Interface (Protocol Layer)**: Owned by the **Protocol Architect**. Focuses on rendering efficiency, user interaction, state stability, and maintaining the governance layer.
- **The Implementation (Execution Layer)**: Owned by the **Execution Specialist**. Focuses on proprietary math, complex algorithms, and logic nodes.

**Stratification Rule**: The Protocol Architect remains "blind" to the underlying complexity of the implementation to prevent context bloat. The Execution Specialist remains "blind" to the UI constraints to focus on technical fidelity. Communication between the two happens via **Standardized Contracts** (JSON/Schema payloads).

---

## 3. Governance via Contract

By formalizing the Identity and Role layers, we enable **Interface-Driven Scaling**. Agents can be swapped in and out of the Execution Lane without requiring updates to the Protocol Lane, provided they adhere to the PSC.

### 3.1 Session Wake Verification
Every agent must run the **Doctrine Auditor** (`scripts/bamboo_contract.py`) or the **Bamboo Heartbeat** (`scripts/bamboo_governor.py`) on session wake to verify that their Identity and Role layers are correctly anchored. 

**Foundational Law**: The Orchestrator must block the execution of any Directive until the PSC is verified. If the PSC is violated (e.g., an agent starts acting without a defined Role or conflicts with its global Identity), the agent must stop and re-sync with the user.

---

## 4. Conclusion

The PSC transforms a standard LLM agent into a **Stratified Agent**. This discipline ensures that as the codebase scales and the implementation becomes more complex, the governance layer remains stable, fast, and governable.
