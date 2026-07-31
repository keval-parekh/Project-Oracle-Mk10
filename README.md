# Project Oracle Mk19 🩻

![Project Oracle Mk19 Challenge](oracle_mk19.gif) 
*(Add your GIF here)*

## The Story

The Galactic Federation’s scout ship just crash-landed right in the middle of Manipal, skidding into Student Plaza. Aliens **Asavari** and **Aditya** have stepped out onto Earth for the first time, but human civilization makes absolutely no sense to them. 

To navigate, they rely on *Project Oracle Mk19* (a Vision Transformer scanner). When pointed at a scene, the scanner generates a glowing heatmap highlighting the most important objects in the room. Unfortunately, atmospheric entry scrambled the scanner's neural pathways. The logic has been downgraded, suffering from "amnesia" and ignoring the deep flow of information through its network. **Chirag** cannot trust these jumpy readings. Furthermore, when **Jasmine** points at a specific alien fruit, the scanner refuses to isolate it, and local students with contrasting graphic tees keep causing "attention hijacking." This leaves **Hariharan**, **Sparsh**, **Michelle**, and **Onas** completely blind to actual threats. 

As the Federation’s top field engineer, your task is to restore the scanner's deep mathematical rollout, fix the targeting feature, and patch the visual interface before the locals catch on.

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

This repo runs as an ongoing bug-hunt challenge!

1. **Pick an open issue** from the Issues tab. The maintainers have logged several critical symptoms affecting the scanner.
2. **Reproduce the bug**: Run `uv run pytest` or `uv run main.py` to observe the broken behavior (wrong heatmap, test failure, etc.).
3. **Fix the bug** in the smallest way that addresses the root cause. Avoid changing the test expectations—they encode the correct math.
4. **Open a PR** referencing the issue number (e.g. `Fixes #12`) and briefly explain the root cause and your fix.

**Note:** Keep PRs scoped to one issue at a time, and ensure all tests pass before submitting!
