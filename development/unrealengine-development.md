# Unreal Engine Development Specification 🏎️

This document defines the governance layer for Unreal Engine (UE5) projects. It establishes a strict boundary between **Blueprint Logic** and **C++ Architecture**.

## 1. The Unreal 3-Concept Canon

### 1.1 The Level Knob
Large-scale changes to `.umap` files or World Partition cells earn a dated Knob entry.
- **Verification**: Cite the specific Actor GUIDs or Layer changes.
- **Physics**: Level changes are verified by the `SourceControl` state of the binary asset.

### 1.2 Stratification (Blueprint vs. C++)
- **C++ (The Foundation)**: Owns the "Physics of Truth"—data structures, PDEs, and performance-critical loops.
- **Blueprint (The Interface)**: Owns the technical interface—visual state, event triggers, and designer-facing Knobs.
- **Rule**: No "Heavy Math" in Blueprints. If logic requires more than 5 nodes to express, move it to a C++ `UFUNCTION`.

### 1.3 Path PLTRF
- **Redirectors**: "Fix Up Redirectors" is a mandatory step zero for any file-move Knob.
- **Canonical Folders**: Follow the standard `/Content/[FeatureName]` structure. One home per asset.

---

## 2. Structural Verification

- **UProperty Integrity**: Every exposed variable MUST cite its `UPROPERTY` macro category and access level (e.g., `VisibleAnywhere`).
- **Include Hygiene**: A C++ claim is invalid if it introduces circular dependencies in the `.build.cs` or header graph.
- **Shader Compilation**: Large shader changes must be logged as "Performance Knobs" due to their impact on cold-start build times.

---

## 3. Project Governance

- **Plugins**: New plugins must be registered in the `docs/repo-organization.md` map.
- **Config Persistence**: Every change to `DefaultEngine.ini` or `DefaultInput.ini` must cite the specific section and key modified.
- **Session Identity**: Specify the Unreal Version (e.g., UE 5.4) in the `AGENT.md` Session Identity block.

---

The foundation is C++. The interface is Blueprint.
