import numpy as np
import pytest

from oracle_mk19.overlay import (
    resize_attention_map,
    make_heatmap,
    blend_heatmap,
    draw_label_banner,
    render_frame,
)


def test_resize_attention_map_shape_and_clip():
    grid = np.array([[0.0, 0.5], [1.0, 2.0]])  # note: 2.0 is out-of-range on purpose
    resized = resize_attention_map(grid, width=32, height=16)
    assert resized.shape == (16, 32)
    assert resized.min() >= 0.0
    assert resized.max() <= 1.0


def test_make_heatmap_shape_and_dtype():
    attn = np.random.rand(16, 32).astype(np.float32)
    heatmap = make_heatmap(attn)
    assert heatmap.shape == (16, 32, 3)
    assert heatmap.dtype == np.uint8


def test_blend_heatmap_preserves_shape():
    frame = (np.random.rand(16, 32, 3) * 255).astype(np.uint8)
    heatmap = (np.random.rand(16, 32, 3) * 255).astype(np.uint8)
    blended = blend_heatmap(frame, heatmap, alpha=0.5)
    assert blended.shape == frame.shape
    assert blended.dtype == np.uint8


def test_blend_heatmap_alpha_zero_returns_original_frame():
    frame = (np.random.rand(16, 32, 3) * 255).astype(np.uint8)
    heatmap = (np.random.rand(16, 32, 3) * 255).astype(np.uint8)
    blended = blend_heatmap(frame, heatmap, alpha=0.0)
    assert np.array_equal(blended, frame)


def test_draw_label_banner_preserves_shape():
    frame = (np.random.rand(64, 128, 3) * 255).astype(np.uint8)
    labeled = draw_label_banner(frame, "golden retriever", 87.3)
    assert labeled.shape == frame.shape


def test_render_frame_end_to_end(rgb_frame):
    attn_grid = np.random.rand(14, 14)
    result = render_frame(rgb_frame, attn_grid, "tabby cat", 42.0)
    assert result.shape == rgb_frame.shape
    assert result.dtype == np.uint8
