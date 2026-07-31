# Contributing — Bug Hunt Guide

This repo runs as an ongoing bug-hunt challenge. A maintainer occasionally
introduces a real, working bug into `src/oracle_mk19/` and opens a GitHub Issue
describing the *symptom* (not the cause). Your job is to track down the
cause and fix it.

## Workflow

1. **Pick an open issue** from the [Issues tab](../../issues).
2. **Fork & clone**, then install dev dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
3. **Reproduce it.** Two ways:
   - Run `pytest -v` — a bug in `rollout.py` or `overlay.py` will usually
     show up as a failing unit test with a clear expected-vs-actual diff.
   - Run `python main.py` and observe the app's behavior (wrong heatmap,
     crash, wrong label, etc.) if the bug isn't caught by an existing test.
4. **Fix the bug** in the smallest way that addresses the root cause. Avoid
   papering over it by changing test expectations — the tests encode the
   correct math/behavior; they should not need to change.
5. **Add a test** if the bug wasn't already caught by one. If you found a
   gap in coverage, that's a valuable part of the fix.
6. **Open a PR** that references the issue number (e.g. `Fixes #12`) and
   briefly explains root cause + fix.

## Guidelines

- Keep PRs scoped to one issue at a time.
- Don't refactor unrelated code in a bug-fix PR — open a separate PR for
  that so it's easy to review.
- All tests must pass (`pytest`) before a PR is merged.
- If you *can't* reproduce the reported bug, say so in the PR/issue thread
  rather than guessing — it may need a clearer repro from the maintainer.

## Reporting a new bug (maintainers)

Use the "Bug report" issue template. Describe only the observable symptom
(what breaks, what looks wrong) — not which line changed — so contributors
have to actually diagnose it.
