"""Scanner: run all rules over a text and produce Parts.            Owner: M07

Algorithm (must be implemented exactly like this — the UI depends on it):
    1. For each rule in `rules` (priority order) whose key is in `enabled`:
         for each match of rule.pattern in text:
             span = match.span(rule.target)
             skip it if span overlaps ANY span already accepted  (higher priority wins)
             otherwise accept it
    2. Sort accepted spans by start position.
    3. Emit Parts, alternating {"kind": "text"} and {"kind": "pii"} so that
       "".join(original texts) == input text   (nothing is lost or duplicated).
    PiiPart fields: see engine/types.py (groups = groupdict() with None values removed,
    info = rule.info(match) if rule.info else None).

A rule whose pattern is None must be skipped (not crash), so the app runs while
rule owners are still working.

Acceptance tests: tests/engine/test_scanner.py (uses fake rules, no dependency on M02–M06).
"""
from __future__ import annotations

from typing import Iterable, Optional

from pdpa_shield.engine.types import Part, Rule


def scan(text: str, rules: list[Rule], enabled: Optional[Iterable[str]] = None) -> list[Part]:
    """Return the list of Parts for `text`. `enabled=None` means all rules."""
    raise NotImplementedError("M07: implement engine.scanner.scan")


def mask_text(text: str, rules: list[Rule], enabled: Optional[Iterable[str]] = None) -> str:
    """Return the fully masked text (join of text parts and masked pii parts)."""
    raise NotImplementedError("M07: implement engine.scanner.mask_text")
