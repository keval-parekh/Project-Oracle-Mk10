# Project Oracle Mk19 👾

![Project Oracle Mk19 Challenge](oracle_mk19.gif) 

## The Lore

The Galactic Federation’s scout ship just crash-landed right in the middle of Manipal, narrowly missing an auto-rickshaw and skidding into Student Plaza. Aliens Sparsh and Jasmine have stepped out onto Earth for the first time, but human civilization makes absolutely no sense to them.

To navigate, they rely on Project Oracle Mk19, a highly advanced biological scanner. When pointed at a scene, the scanner is supposed to generate a glowing heatmap, highlighting the most important objects in the room to help them identify threats and resources.

Unfortunately, atmospheric entry completely scrambled the scanner's neural pathways. Right now, the Oracle Mk19 is suffering from severe system failures across the board:

First, the scanner is suffering from "amnesia." It is completely ignoring the deep, complex flow of information through its neural network, instead generating a naive, jumpy heatmap based entirely on its very last layer of processing. Sparsh cannot trust these shallow readings.

Worse, the scanner’s targeting system is completely scattered. When Jasmine points the scanner at a specific object-like a strange Earth fruit on a vendor's cart, the scanner refuses to track it. Instead, the signal is diluted, blurring its focus across the entire scene and disconnecting the heatmap from the actual object being analyzed.

Furthermore, the sensor's optical contrast is broken. Instead of sharp, glowing highlights on points of interest, the internal probability distribution has been flattened, rendering the heatmap as a useless, uniform blur.

And if that wasn't dangerous enough, the display interface is actively fighting them. When Sparsh attempts to lower the heatmap's intensity to get a clearer view of the actual physical environment, the alpha-blending inverts and the heatmap grows stronger, completely obscuring the camera feed and leaving them totally blind.

Behind all of this, the fundamental math stabilizing the neural matrix is breaking down, failing to preserve the vital "residual" connections between processing stages.

As the Federation’s top field engineer on Earth, your task is to dive into the Project Oracle Mk19 codebase, diagnose these critical mathematical and visual vulnerabilities, and restore the scanner to full working order before the local students realize there are aliens on campus.

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
