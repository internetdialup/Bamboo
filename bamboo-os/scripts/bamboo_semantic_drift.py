# bamboo_semantic_drift.py — Agnostic embedding-based drift detection
from __future__ import annotations
import numpy as np
import os
import json

# Optional dependency: sentence_transformers
try:
    from sentence_transformers import SentenceTransformer
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"   # PINNED
_model = None

def _embed(texts: list[str]) -> np.ndarray:
    global _model
    if _model is None:
        if not HAS_TRANSFORMERS:
            raise ImportError("sentence-transformers not installed. Run 'pip install sentence-transformers'.")
        _model = SentenceTransformer(_MODEL_ID)
    return _model.encode(texts, normalize_embeddings=True)

def compute_semantic_drift(agent_entries: list[str], anchor_text: str) -> dict:
    """Drift = movement of recent output away from the role anchor.
    agent_entries: the agent's recent entries, CHRONOLOGICAL order (oldest→newest).
    anchor_text:   the agent's declared role/persona definition.
    """
    if not HAS_TRANSFORMERS:
        return {"error": "transformers_missing", "drift_score": 0.0, "drift_velocity": 0.0}

    if not agent_entries:
        return {"drift_score": 0.0, "drift_velocity": 0.0, "mean_distance": 0.0, "samples": 0}

    try:
        anchor = _embed([anchor_text])[0]
        embs   = _embed(agent_entries)
        dists  = [1.0 - float(np.dot(e, anchor)) for e in embs]   # cosine distance to anchor

        n = len(dists)
        velocity = float(np.polyfit(np.arange(n), dists, 1)[0]) if n >= 2 else 0.0  # slope

        return {
            "drift_score":    round(dists[-1], 3),       # current distance from role
            "drift_velocity": round(velocity, 4),        # rising = degrading
            "mean_distance":  round(float(np.mean(dists)), 3),
            "samples": n,
        }
    except Exception as e:
        return {"error": str(e), "drift_score": 0.0, "drift_velocity": 0.0}
