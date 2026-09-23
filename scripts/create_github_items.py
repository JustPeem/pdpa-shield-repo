"""Create labels, milestones and issues from scripts/issues.json using the GitHub CLI.

    python3 scripts/create_github_items.py --repo owner/pdpa-shield [--dry-run]

Safe to re-run: labels are upserted, milestones and issues with an existing title are skipped.
Issues are assigned only when scripts/members.json has a GitHub username for the owner.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LABELS = {
    "task": "5b6b7f", "bug": "d73a4a", "contract": "b60205", "infra": "0e8a16", "docs": "0075ca",
    "qa": "fbca04", "regex": "1d76db", "engine": "5319e7", "backend": "006b75", "frontend": "0a6cff",
    "design": "c5def5", "i18n": "bfdadc", "dfa": "7057ff", "perf": "e99695",
    "rule:card": "ef4444", "rule:email": "0a6cff", "rule:phone": "f59e0b", "rule:dob": "8b5cf6",
    "rule:address": "12b76a",
}
OWNER_LABEL_COLOR = "ededed"


def gh(args: list[str], dry: bool, capture: bool = False) -> str:
    if dry:
        print("  gh", " ".join(a if " " not in a else repr(a) for a in args)[:160])
        return "[]" if capture else ""
    res = subprocess.run(["gh", *args], check=True, text=True, capture_output=capture)
    return res.stdout if capture else ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    R, dry = ["--repo", a.repo], a.dry_run

    data = json.loads((ROOT / "scripts/issues.json").read_text(encoding="utf-8"))
    members = json.loads((ROOT / "scripts/members.json").read_text(encoding="utf-8"))["members"]

    print("Labels")
    owners = sorted({i["owner"] for i in data["issues"]})
    for name, color in {**LABELS, **{o: OWNER_LABEL_COLOR for o in owners}}.items():
        gh(["label", "create", name, "--color", color, "--force", *R], dry)

    print("Milestones")
    existing = {m["title"] for m in json.loads(gh(["api", f"repos/{a.repo}/milestones?state=all", "--paginate"], dry, True) or "[]")}
    for title in data["milestones"]:
        if title not in existing:
            gh(["api", f"repos/{a.repo}/milestones", "-f", f"title={title}"], dry)

    print("Issues")
    have = {i["title"] for i in json.loads(gh(["issue", "list", *R, "--state", "all", "--limit", "500", "--json", "title"], dry, True) or "[]")}
    for it in data["issues"]:
        title = f"[{it['owner']}] {it['title']}"
        if title in have:
            continue
        who = members.get(it["owner"], {})
        body = f"**Owner:** {it['owner']} — {who.get('name', '')} ({who.get('role', '')})\n\n{it['body']}\n\nSee docs/TEAM.md#{it['owner'].lower()}"
        args = ["issue", "create", *R, "--title", title, "--body", body, "--milestone", it["milestone"]]
        for lab in [it["owner"], *it["labels"]]:
            args += ["--label", lab]
        if who.get("github"):
            args += ["--assignee", who["github"]]
        gh(args, dry)
    print("done")


if __name__ == "__main__":
    main()
