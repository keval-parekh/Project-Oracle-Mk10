# Project Oracle Mk19 🩻

Real-time webcam visualizer for Vision Transformers. Streams your camera
through `google/vit-base-patch16-224` and overlays a live heatmap showing
where the model's `[CLS]` token is "looking," via **Attention Rollout**
([Abnar & Zuidema, 2020](https://arxiv.org/abs/2005.00928)).

## Install & run

```bash
uv sync
uv run main.py
```

or with plain pip:

```bash
pip install -e ".[dev]"
python main.py
```

Press `q` in the window to quit.

## Project layout

```
src/oracle_mk19/
├── config.py
├── device.py
├── model.py
├── rollout.py
├── inference.py
├── overlay.py
└── webcam.py
tests/
```

## 🐛 This is a bug-hunt challenge repo

This project works end-to-end. Periodically, a bug is deliberately
introduced somewhere in `src/oracle_mk19/` and filed as a GitHub Issue. Your
job: find it, fix it, and open a PR.

**How to participate:**
1. Check the [Issues](../../issues) tab for an open bug report.
2. Fork the repo, reproduce the bug (run `pytest`, or run the app itself).
3. Fix it and open a PR referencing the issue number.
4. `pytest` must pass — the test suite pins down the expected numerical
   behavior of the rollout and overlay pipelines, so a correct fix should
   make the relevant test(s) pass without touching the tests themselves.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Running tests

```bash
pip install -e ".[dev]"
pytest
```

## Background reading

- Attention Rollout: Abnar & Zuidema, *"Quantifying Attention Flow in
  Transformers"* (2020)
- Model: [`google/vit-base-patch16-224`](https://huggingface.co/google/vit-base-patch16-224)
  on Hugging Face (ImageNet-1k classes)
