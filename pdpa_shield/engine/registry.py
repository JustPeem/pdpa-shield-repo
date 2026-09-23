"""Rule registry.                                                   Owner: M07

The ORDER of RULES is the priority order used by the scanner:
card must come before phone so that digits inside a card number are never read as a phone.
"""
from __future__ import annotations

from pdpa_shield.engine.types import Rule
from pdpa_shield.rules import address, card, dob, email, phone

RULES: list[Rule] = [card.RULE, email.RULE, phone.RULE, dob.RULE, address.RULE]
RULE_MAP: dict[str, Rule] = {r.key: r for r in RULES}
RULE_KEYS: list[str] = [r.key for r in RULES]
