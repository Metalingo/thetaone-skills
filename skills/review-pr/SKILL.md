---
name: review-pr
description: Review a pull request for requirement compliance and code quality, or evaluate received review feedback against current evidence before applying fixes.
---

# Review PR

Read the target repository's review guidelines and required template. Identify the actual PR base and head, issue acceptance criteria, and diff. Review surrounding code and relevant tests rather than relying on the author's summary.

## Review a PR

First check requirement compliance: does the change solve the requested problem and satisfy the slice's observable criteria without expanding scope? Then check correctness, regressions, contracts, maintainability, and relevant test coverage. Scale scrutiny to the change.

Use a fresh review context or an independent subagent when available and authorized; otherwise review in the current session and reassess assumptions from source evidence. Never claim an independent review when none occurred.

Report actionable findings with severity, file/line evidence, a concrete failure condition, and impact. Separate confirmed defects from questions and optional preferences. Run focused checks where useful and state anything not verified. Do not invent findings to fill a template.

Preserve every mandatory project template section. If none exists, give scope, findings, verification, and verdict. Present the review to the user. Publish a GitHub review or comment only when explicitly authorized; check the current head before posting and reassess if it changed. Do not approve, request changes through the API, or merge merely because a local verdict exists.

## Respond to received feedback

Read the full feedback and verify each claim against the current code, requirements, and tests. Clarify ambiguity; explain with evidence when a suggestion is incorrect or conflicts with scope. Do not accept or reject a comment based on its author's status.

A Request Changes review does not authorize repairs by itself. Let the worker choose the response unless they already authorized fixes. Apply agreed corrections, run relevant checks, and report which findings were resolved or remain open. Avoid an automatic review/fix loop that chases approval indefinitely. Commit and push only within authorization.
