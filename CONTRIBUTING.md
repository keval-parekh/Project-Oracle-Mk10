# How to Contribute

Everything you need to do is on the **Issues** tab. This page covers
the mechanics of getting your fix from your machine into a pull request here.

Each open issue describes a **symptom** — a bug a maintainer introduced into
`src/oracle_mk19/`. Your job is to find the root cause and fix it.

---

## 1. Fork the repository

Press **Fork** at the top right of this repo's page and create the fork under
your own account. Leave the name as it is.

You now have your own copy at `https://github.com/<your-username>/Project-Oracle-Mk19`.
All of your work happens there. You cannot push to this repository directly,
and you do not need to.

## 2. Clone your fork and set it up

```bash
git clone https://github.com/<your-username>/Project-Oracle-Mk19.git
cd Project-Oracle-Mk19
```

Add this repository as a second remote called `upstream`, so you can pull in
any changes made after you forked:

```bash
git remote add upstream https://github.com/Project-MANAS-Research-AI/Project-Oracle-Mk19.git
git remote -v      # origin = your fork, upstream = here
```

Then set up the environment. The project uses
[uv](https://docs.astral.sh/uv/):

```bash
uv sync --extra dev
```

Check it runs before you change anything:

```bash
uv run main.py        # live webcam window — press q to quit
uv run pytest -v      # all regular tests should pass
```

## 3. Pick an issue and read it properly

Read the whole issue. It describes a *symptom*, not a cause. Understand
exactly what is going wrong — then find *why*.

Two ways to reproduce it:

- **`uv run pytest -v`** — bugs in the math usually show up as a failing
  unit test with a clear expected-vs-actual diff.
- **`uv run main.py`** — subtler visual bugs (wrong heatmap, broken overlay)
  may only be visible in the live webcam window.

## 4. Make a branch

Do not work on `main` directly, even on your own fork. Branch off it:

```bash
git checkout main
git pull upstream main
git checkout -b fix/describe-the-bug
```

Name it after what you are doing. `fix/rollout-masking`,
`fix/overlay-contrast`, and `residual-connection` are all fine.
`patch-1` is not.

## 5. Do the work

**What you are expected to change:**

| Path | What it is |
|---|---|
| `src/oracle_mk19/rollout.py` | Attention rollout computation |
| `src/oracle_mk19/overlay.py` | Heatmap overlay / blending |
| `src/oracle_mk19/model.py` | ViT model loading |
| `src/oracle_mk19/inference.py` | Forward pass / attention extraction |
| `src/oracle_mk19/webcam.py` | Live webcam loop |

**What you must not change:**

| Path | Why |
|---|---|
| `tests/` | These are the checks — changing them does not change your result |
| `.github/` | The CI automation |
| `pyproject.toml` | Pinned on purpose |
| `uv.lock` | Locked on purpose |
| `.gitignore` | |

A pull request that touches any of those will be **rejected automatically**,
before anything else is looked at. If you think one of them is genuinely
wrong, say so in a comment on the relevant issue rather than editing it.

## 6. Check your work locally

```bash
uv run pytest -v
```

This runs the regular sanity tests: correct tensor shapes, expected numerical
behavior, and structural checks. Keep it green.

It is easy to "fix" a bug by accident — by making the output
non-reproducible, or letting a number run to infinity — and then every
measurement you report means nothing.

If you added a script of your own, make sure it runs from a clean checkout.

## 7. Commit

Commit in steps that make sense on their own, with messages that say what
changed and why:

```bash
git add src/oracle_mk19/rollout.py
git commit -m "Fix attention rollout masking

The CLS-token mask was applied after averaging instead of before,
so self-attention to non-CLS tokens diluted the rollout signal."
```

`update`, `fix`, `final`, and `asdf` tell a reviewer nothing. The diff already
says *what* changed; the message is where you say *why*.

## 8. Push to your fork

```bash
git push -u origin fix/describe-the-bug
```

## 9. Open the pull request

Go to your fork on GitHub. It will offer a **Compare & pull request** button;
press it. Check the direction carefully before you submit:

```
base repository: Project-MANAS-Research-AI/Project-Oracle-Mk19   base: main
head repository: <your-username>/Project-Oracle-Mk19              compare: your branch
```

The base branch is **`main`**. If the comparison shows hundreds of changed
files, the base is wrong.

In the PR description:

- **Which issue this fixes.** Write `Fixes #N` so it is linked and
  auto-closed on merge.
- **Root cause.** What was actually wrong, not just what you changed.
- **What you changed and why.** A short paragraph. The reasoning is the
  part worth reading; the diff is already there.

## 10. After you open it

Automated checks start within a minute or so. Your first pull request may
wait for someone to approve the run — that happens to everyone's first
contribution and does not mean anything is wrong.

When they finish, open the **Checks** tab and read the output. The CI
overlays hidden validation tests from the `tests` branch and runs the full
suite. Where a check fails, the log says exactly what it measured and what it
expected — that message is written to be useful, so read it before asking.

To update your pull request, just push more commits to the same branch. It
updates itself and everything re-runs. Do not close it and open a new one.

If you get review comments, reply to them. Pushing a fix without saying
anything leaves the reviewer guessing whether you understood the point or
changed something at random.

---

## Keeping your fork current

If this repository moves on while you are working:

```bash
git checkout main
git pull upstream main
git push origin main
git checkout your-branch
git rebase main
```

## Things that get a pull request sent back

- It changes `tests/`, `.github/`, `pyproject.toml`, or `uv.lock` — rejected
  automatically.
- It changes nothing at all — rejected automatically.
- The base branch is wrong, so the diff is enormous.
- The tests no longer pass: `uv run pytest` fails on your fork.
- No description, or a description that does not explain the root cause.
- It "fixes" the bug by changing test expectations instead of fixing the
  actual code.
- Unrelated refactoring bundled into a bug-fix PR.

## If you are stuck

Comment on the issue itself. Say which issue, what you tried, and what
happened — including the actual command and the actual output. That gets a
useful answer far faster than "it's not working".
