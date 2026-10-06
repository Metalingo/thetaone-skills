---
name: smart-commit
description: Inspect the requested changes, create a traceable Git commit, and push the working branch when asked to commit; honor narrower commit-only requests.
---

# Smart Commit

Default scope is commit and push. Honor an explicit commit-only request and project authorization rules.

1. Read repository commit rules and inspect status, staged and unstaged diffs, relevant untracked files, and recent commit style. Establish the intended branch and remote. Exclude unrelated work, credentials, generated clutter, and local configuration.
2. Stage only the requested changes. If unrelated intents require a grouping decision, propose the split and ask; many files alone do not require multiple commits.
3. Run required focused checks and honor Git hooks. Investigate hook failures and fix relevant causes; never bypass hooks with `--no-verify` or equivalent. Stop and report a blocker if the fix requires unrelated changes.
4. Write an imperative conventional subject, following project language and length rules. Explain what changed and why, material impact, related issues, verification, and useful rollback notes. Scale the body to the change; do not fill empty sections or duplicate the diff.
5. Commit, inspect the resulting commit, and push to the intended working branch. Set upstream for a new branch as needed. Never push directly to project-protected branches such as `main` or `staging` without explicit authorization. Do not infer that every branch is protected.
6. Verify the remote head matches the local commit and report the hash, branch, checks, and push result. Distinguish successful commit from failed push.

Do not force push, rewrite others' work, bypass branch rules, or switch authentication methods to evade a failure. On a rejected push, inspect remote divergence and preserve local work; ask when resolution needs a history or scope decision. Use only permission options supported by the current environment.

PR creation is a separate `create-pr` action. Do not merge or deploy as part of a commit request.
