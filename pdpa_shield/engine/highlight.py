"""Regex syntax highlighter for the Rules page — itself written with `re`.   Owner: M07

Tokenise a pattern string into [token_class, text] pairs. Required classes:
    comment  "# ..." to end of line (re.VERBOSE comments)
    look     (?=  (?!  (?<=  (?<!
    backref  (?P=name)
    named    (?P<name>
    noncap   (?:
    paren    ( or )
    cls      [...]  character class (handle escaped ] inside)
    quant    * + ? (optionally lazy ?) and {n} {n,} {n,m}
    escape   \\d \\s \\. ...
    alt      |
    space    whitespace
    lit      anything else
Joining all token texts must give back the original pattern exactly.

Acceptance tests: tests/engine/test_highlight.py
"""
from __future__ import annotations


def highlight_pattern(pattern: str) -> list[list[str]]:
    raise NotImplementedError("M07: implement engine.highlight.highlight_pattern")
