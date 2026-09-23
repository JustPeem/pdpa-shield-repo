#!/usr/bin/env bash
# Create the GitHub repository and everything the team needs, in one go.
#
# Requirements: git, GitHub CLI (https://cli.github.com) logged in:  gh auth login
# Usage:        scripts/github_bootstrap.sh [repo-name] [--public|--private] [owner-or-org]
# Example:      scripts/github_bootstrap.sh pdpa-shield --private my-toc-team
set -euo pipefail

NAME="${1:-pdpa-shield}"
VISIBILITY="${2:---private}"
OWNER="${3:-}"
FULL="${OWNER:+$OWNER/}$NAME"

cd "$(dirname "$0")/.."
command -v gh >/dev/null || { echo "Install the GitHub CLI first: https://cli.github.com"; exit 1; }
gh auth status >/dev/null || { echo "Run: gh auth login"; exit 1; }

echo "==> Creating $FULL ($VISIBILITY) and pushing main"
git switch main
gh repo create "$FULL" "$VISIBILITY" --source=. --remote=origin \
  --description "PDPA Shield — regex-based data masking for banking logs (ToC assignment)"
git push -u origin main
git push -u origin develop
git push -u origin reference

echo "==> Setting develop as the default branch (PRs land there)"
gh repo edit "$FULL" --default-branch develop --enable-issues --delete-branch-on-merge

echo "==> Labels, milestones and issues"
python3 scripts/create_github_items.py --repo "$(gh repo view "$FULL" --json nameWithOwner -q .nameWithOwner)"

echo "==> Branch protection (needs admin rights; skipped if not allowed)"
for BR in main develop; do
  gh api -X PUT "repos/{owner}/{repo}/branches/$BR/protection" --silent \
    -H "Accept: application/vnd.github+json" \
    -F "required_status_checks[strict]=true" -f "required_status_checks[contexts][]=test (3.12)" \
    -F "enforce_admins=false" \
    -F "required_pull_request_reviews[required_approving_review_count]=1" \
    -F "restrictions=null" 2>/dev/null \
    && echo "   protected $BR" || echo "   could not protect $BR (do it in Settings → Branches)"
done

echo
echo "Done: $(gh repo view "$FULL" --json url -q .url)"
echo "Next: fill scripts/members.json, run scripts/apply_members.py, invite members (Settings → Collaborators)."
