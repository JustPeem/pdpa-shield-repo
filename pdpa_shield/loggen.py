"""Fake banking-log generator (random data only — never real customers).   Owner: M08

generate(n, seed) must return exactly n lines (each ending with "\\n") like:
    2026-09-24 08:01:00 [INFO ] LOGIN         session=685931 | email=... | card=...
Requirements
    [ ] 1–3 PII fields per line drawn from: email, card (all 3 separator styles), phone
        (dash / space / none / +66), "customer DOB:dd/mm/25yy", Thai address (Bangkok and
        provincial formats, with and without soi / moo).
    [ ] ~35% of lines also contain a DECOY that must NOT be masked: 20-digit txn_id,
        IP address, "legacy_dob=DOB:3x/13/2549", "ref=123-456-7890", "Address: ไม่ระบุ".
    [ ] Same seed -> same output (use random.Random(seed), not the global random).
    [ ] Timestamps increase line by line.

Acceptance tests: tests/test_loggen.py
"""
from __future__ import annotations

from typing import Optional

DECOY_EXAMPLES = [
    "txn_id=12345678901234567890",
    "ip=10.2.33.14",
    "legacy_dob=DOB:32/13/2549",
    "ref=123-456-7890",
    "Address: ไม่ระบุ",
]


def generate(n: int = 25, seed: Optional[int] = None) -> str:
    raise NotImplementedError("M08: implement loggen.generate")
