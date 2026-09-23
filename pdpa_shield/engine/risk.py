"""PDPA Risk Score.                                                  Owner: M07

    risk  = min(100, sum(count[key] * weight[key]) * 2)
    level = "high" if risk >= 60 else "mid" if risk >= 25 else "low" if risk > 0 else "none"
    Thai level labels: none="ไม่พบ", low="ต่ำ", mid="กลาง", high="สูง"

Acceptance tests: tests/engine/test_risk.py
"""
from __future__ import annotations

from pdpa_shield.engine.types import Part, Rule, Stats


def stats(parts: list[Part], rules: list[Rule]) -> Stats:
    """Count pii parts per rule key (every key present, 0 if none) and compute the score."""
    raise NotImplementedError("M07: implement engine.risk.stats")
