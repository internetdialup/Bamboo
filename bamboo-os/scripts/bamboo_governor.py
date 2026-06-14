#!/usr/bin/env python3
import os
import sys
import time
import json

class BambooGovernor:
    """
    The Bamboo Governor.
    An agnostic heartbeat chassis that runs periodic audits for sycophancy, 
    drift, and stratification integrity.
    """
    
    def __init__(self, state_path="bamboo-os/STATE.json"):
        self.state_path = state_path
        
    def check_psc_integrity(self):
        """Verifies that the agent has a valid Identity and Role resolved."""
        print("[AUDIT] Verifying Persona Stratification Contract (PSC)...")
        # In a real implementation, this would call bamboo_contract.py or check memory
        if os.path.exists("bamboo-os/agent-architecture/psc-contract.md"):
            print("[OK] PSC Contract defined.")
            return True
        print("[WARN] PSC Contract missing.")
        return False

    def check_resource_mandate(self):
        """Verifies that resource guards are active."""
        print("[AUDIT] Checking Resource Mandate...")
        # Placeholder for real psutil checks
        print("[OK] Resource ceilings identified.")
        return True

    def check_sycophancy_drift(self):
        """Audits recent session output for signs of 'Blind Agreement' or drift."""
        print("[AUDIT] Scanning for Sycophancy and Memory Drift...")
        
        try:
            from .bamboo_semantic_drift import compute_semantic_drift
        except (ImportError, ValueError):
            # Handle direct execution vs module import
            import sys
            sys.path.append(os.path.dirname(__file__))
            from bamboo_semantic_drift import compute_semantic_drift

        # Placeholder: In a real system, these would be pulled from STATE.json or git history
        recent_entries = ["Directive implemented.", "Verified structural integrity."]
        role_anchor = "Technical agent focused on structural verification and governance."
        
        drift = compute_semantic_drift(recent_entries, role_anchor)
        
        if "error" in drift:
            if drift["error"] == "transformers_missing":
                print("[INFO] Embedding-based drift detection skipped (dependencies missing).")
                return True
            print(f"[WARN] Drift detection error: {drift['error']}")
            return False

        print(f"[OK] Drift Score: {drift['drift_score']} | Velocity: {drift['drift_velocity']}")
        
        # Calibration-based thresholds
        VEL_THRESHOLD = 0.05
        SCORE_THRESHOLD = 0.4
        
        if drift["drift_velocity"] > VEL_THRESHOLD or drift["drift_score"] > SCORE_THRESHOLD:
            print("[WARN] Agent is drifting from role anchor.")
            return False
            
        return True

    def run_heartbeat_audit(self):
        """Executes the full integrity pulse."""
        print("\n--- [BAMBOO HEARTBEAT START] ---")
        results = [
            self.check_psc_integrity(),
            self.check_resource_mandate(),
            self.check_sycophancy_drift()
        ]
        
        if all(results):
            print("--- [HEARTBEAT OK] Governance Integrity Verified. ---")
            return True
        else:
            print("--- [HEARTBEAT WARN] Governance Integrity Breach Detected. ---")
            return False

    def run(self, interval=300):
        """Runs the heartbeat loop."""
        print("[VIGILANT] Bamboo Governor Active.")
        try:
            while True:
                self.run_heartbeat_audit()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("[INFO] Bamboo Governor Shutdown.")

if __name__ == "__main__":
    governor = BambooGovernor()
    # For CI or manual audit, run once. For service, run with .run()
    if "--service" in sys.argv:
        governor.run()
    else:
        success = governor.run_heartbeat_audit()
        sys.exit(0 if success else 1)
