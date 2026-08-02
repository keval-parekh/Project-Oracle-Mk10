# Project Oracle Mk19 👾

![Project Oracle Mk19 Challenge](oracle_mk19.gif) 

## The Lore

The Galactic Federation’s scout ship has crash-landed in the middle of Manipal, narrowly missing an auto-rickshaw and skidding into Student Plaza. Aliens Sparsh and Jasmine have stepped out onto Earth for the first time, and they must rely on Project Oracle Mk19, a highly advanced biological scanner, to navigate this strange new world by generating glowing heatmaps of threats and resources.

Unfortunately, atmospheric entry completely scrambled the scanner's neural pathways, triggering severe system failures. The Oracle now suffers from "amnesia," ignoring deep neural context to produce naive, jumpy readings. Its targeting system is entirely scattered, diluting its focus rather than locking onto specific objects. Furthermore, the optical contrast is broken, rendering highlights as a uniform blur, and the display interface is actively fighting them,paradoxically obscuring the camera feed when they try to lower the intensity. Behind all of this, the fundamental math stabilizing the neural matrix's "residual" connections is breaking down.

As the Federation’s top field engineer on Earth, your task is to dive into the codebase, diagnose these mathematical and visual vulnerabilities, and restore the scanner to full working order before the students notice there are aliens on campus!

## Project Structure

The core mathematical logic and visual pipeline are located in `src/oracle_mk19/`. 
The `tests/` directory contains diagnostics that pin down the expected numerical behavior of the scanner. We want you to explore the codebase yourself, so dive in and see how the components connect!

## Setup Guide

We recommend using [`uv`](https://github.com/astral-sh/uv) for lightning-fast environment setup.

1. Install `uv` if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Clone the repository and navigate into it.
3. Sync the dependencies and run the scanner:
   ```bash
   uv sync
   uv run main.py
   ```
   *(Press `q` in the webcam window to quit)*

To run the internal diagnostics (tests):
```bash
uv run pytest
```

## How to Participate (Bug Hunt)

This repo runs as an ongoing bug-hunt challenge! A maintainer occasionally introduces a real, working bug into `src/oracle_mk19/` and opens a GitHub Issue describing the *symptom* (not the cause). Your job is to track down the cause and fix it.

1. **Pick an open issue** from the Issues tab.
2. **Reproduce the bug**: Run `uv run pytest` or `uv run main.py` to observe the broken behavior.
3. **Fix the bug** in the smallest way that addresses the root cause. Avoid changing test expectations — they encode the correct math.
4. **Open a PR** referencing the issue number (e.g. `Fixes #12`) and briefly explain the root cause and your fix.

👉 **See [CONTRIBUTING.md](CONTRIBUTING.md) for the full step-by-step guide** — forking, branching, committing, opening a PR, and everything in between.
