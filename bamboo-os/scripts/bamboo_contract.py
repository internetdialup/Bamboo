#!/usr/bin/env python3
import os
import sys

def check_identity_layer():
    """Checks for the global Identity Layer (the 'Soul')."""
    # Look for common global gemini/agent config paths
    home = os.path.expanduser("~")
    possible_paths = [
        os.path.join(home, ".gemini", "gemini.md"),
        os.path.join(home, ".agents", "identity.md"),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return True, path
    return False, None

def check_role_layer():
    """Checks for the local Role Layer (the 'Job')."""
    # Look for project-level role definitions
    possible_paths = [
        "AGENT.md",
        "MEMORY.md",
        "docs/ctx-orientation.md",
        "docs/memory-ctx/ctx-orientation.md",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            with open(path, "r") as f:
                content = f.read()
                # Check for role-based keywords or "Ironhide" persona
                if "Ironhide" in content or "Role" in content or "Persona" in content:
                    return True, path
    return False, None

def main():
    print("Bamboo Doctrine Auditor: Verifying Structural Integrity...")
    
    identity_ok, identity_path = check_identity_layer()
    if identity_ok:
        print(f"[OK] Identity Layer found at: {identity_path}")
    else:
        print("[WARN] Identity Layer missing.")

    role_ok, role_path = check_role_layer()
    if role_ok:
        print(f"[OK] Role Layer found in: {role_path}")
    else:
        print("[WARN] Role Layer missing.")

    # Structural Verification Rule: Claims must name a file
    print("[INFO] Canon: Knob, PLTRF, Hot/Warm/Cold.")
    print("[INFO] Verification: Persistence claims MUST name a file path.")

    if identity_ok and role_ok:
        print("\n[VIGILANT] Integrity Verified. Physics of Truth enforced.")
        sys.exit(0)
    else:
        print("\n[ERROR] Integrity Violation: Agent is unanchored. Cognitive integrity at risk.")
        sys.exit(1)

if __name__ == "__main__":
    main()
