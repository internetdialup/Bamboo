# Unity Development Specification 🎮

This document defines the structural discipline for Unity-based projects governed by Bamboo. It prioritizes **Asset Integrity** and **Serialized State** over narrative vibes.

## 1. The Unity 3-Concept Canon

### 1.1 The Scene Knob
Every meaningful change to a `.unity` scene or a major Prefab MUST be logged as a Knob in `docs/ctx-orientation.md`. 
- **Rule**: Narrative entries must cite the specific Scene name and any modified Serialized Fields.
- **Physics**: A change is not "done" until the `.meta` files are verified and the GUIDs remain stable.

### 1.2 Prefab Stratification (The Interface vs. Logic Split)
- **The Interface Layer**: Prefab UI components and Visual Scripting triggers.
- **The Logic Layer**: C# scripts and Custom Inspectors.
- **Constraint**: Logic scripts should be decoupled from specific Scenes via **Interface-Driven Scaling**. Use ScriptableObjects for data persistence across Scene Knobs.

### 1.3 Asset PLTRF
- **One Home**: Every asset (Texture, Audio, Script) has exactly one canonical home in the `Assets/` directory.
- **Renames**: Renaming an asset must occur within the Unity Editor to preserve `.meta` integrity. Pointers in `Bamboo.md` or `repo-organization.md` must flip in the same commit.

---

## 2. Structural Verification (The Physics)

- **Assembly Definitions**: Use `.asmdef` files to enforce modular boundaries. A script claim is invalid if it violates the assembly dependency graph.
- **Version Control**: Enable **Force Text** serialization. Every claim of a "Scene Change" must be verifiable via the YAML diff in the `.unity` file.
- **Build Targets**: State the active Build Target (Xbox, iOS, WebGL) in the `AGENT.md` Session Identity block.

---

## 3. Mandatory Hygiene

- **No Orphaned Metas**: Run a "Stale Meta" scan before every major Knob transition.
- **Naming Conventions**: Follow the [Unity Style Guide](https://github.com/microsoft/Unity-style-guide). 
- **Persistence**: All "Project Settings" changes MUST name the specific `.asset` file in `ProjectSettings/` that was modified.

---

The engine is structural. The build is active.
