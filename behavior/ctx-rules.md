# Context Rules

This document defines the hard operational rules and structural constraints for the Bamboo framework. It prioritizes binary verification over narrative "liturgy."

## 1. The 3-Concept Cold-Start Rule

Every agent must internalize these three directives before execution:
1. **Read `AGENT.md`**: Follow the cold-start loading order without exception.
2. **Log Knobs**: Every meaningful change earns a dated narrative entry in `docs/ctx-orientation.md`.
3. **Don't Bloat**: Keep the lexicon lean. Use only the load-bearing terms (**Knob**, **PLTRF**, **Hot/Warm/Cold**).

## 2. Structural Verification (The Physics of Truth)

Bamboo replaces vague mandates with structural requirements to enforce **Anti-Sycophancy**—the explicit audit of operator assumptions to combat cognitive degradation and "Blind Agreement."

- **Rule**: Every claim regarding the system's state, existence, or change MUST reference a specific file path or shell output. 
- **Enforcement**: Claims that cannot be reduced to a file path or a script exit code are considered "Liturgy" and are subject to immediate rejection.
- **Verification**: Anti-Sycophancy is not a "tone." It is a link to a raw data file or a command result. If you cannot cite the path, do not make the claim.

## 3. Chain of Custody (Evidence Integrity)

AI Forensics relies on the integrity of the record.
- **Rule**: Every log, handoff, or state artifact that supports a forensic audit MUST be tamper-evident.
- **Mechanism**: Use append-only logs (e.g., `agent-bus.jsonl`), integrity hashes (SHA256), and git authorship to maintain a verifiable chain of custody.
- **Enforcement**: Evidence that cannot prove its origin or has been silently modified is rejected as "forged context."

## 4. PLTRF (Preventative Long-Term Repo Fragmentation)

Maintaining repo integrity is a binary task.
- **One Home**: One canonical home per concept. No mirrors.
- **Propagated Renames**: When a file moves, all references must flip in the same commit.
- **Audited Maps**: The repo map (`docs/repo-organization.md`) must be 100% accurate.
- **CI Enforcement**: The `pltrf-check.yml` action fails the build on any broken pointer.

## 4. Knob Entry Format

Every Knob entry in the orientation log must contain:
1. **Date**: Full date (e.g., Saturday, June 13, 2026).
2. **Narrative**: 1-2 paragraphs of "Why" and "What."
3. **Cross-References**: Binary links to changed files or previous Knobs.

## 5. Hot/Warm/Cold Tiering

- **Hot**: Active Knob and current directives. Stays in context.
- **Warm**: Recent history (last 3-5 Knobs). Summarized or moved to `ctx-ori-summary-*.md`.
- **Cold**: Archived history. Externalized to the repo; pulled only on demand.

---

Liturgy purged. Physics enforced.
