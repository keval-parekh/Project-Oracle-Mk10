import torch
import numpy as np
import pytest

from oracle_mk19.rollout import (
    fuse_heads,
    add_residual_and_normalize,
    rollout_layers,
    cls_attention_to_grid,
    attention_rollout,
)


def test_fuse_heads_mean():
    layer_attention = torch.tensor(
        [[[[0.1, 0.9], [0.2, 0.8]], [[0.3, 0.7], [0.4, 0.6]]]]
    )
    fused = fuse_heads(layer_attention, "mean")
    expected = torch.tensor([[[0.2, 0.8], [0.3, 0.7]]])
    assert torch.allclose(fused, expected, atol=1e-6)


def test_fuse_heads_max():
    layer_attention = torch.tensor(
        [[[[0.1, 0.9], [0.2, 0.8]], [[0.3, 0.7], [0.4, 0.6]]]]
    )
    fused = fuse_heads(layer_attention, "max")
    expected = torch.tensor([[[0.3, 0.9], [0.4, 0.8]]])
    assert torch.allclose(fused, expected, atol=1e-6)


def test_fuse_heads_min():
    layer_attention = torch.tensor(
        [[[[0.1, 0.9], [0.2, 0.8]], [[0.3, 0.7], [0.4, 0.6]]]]
    )
    fused = fuse_heads(layer_attention, "min")
    expected = torch.tensor([[[0.1, 0.7], [0.2, 0.6]]])
    assert torch.allclose(fused, expected, atol=1e-6)


def test_fuse_heads_invalid_strategy_raises():
    layer_attention = torch.rand(1, 2, 2, 2)
    with pytest.raises(ValueError):
        fuse_heads(layer_attention, "bogus")


def test_add_residual_and_normalize():
    fused = torch.tensor([[0.5, 0.5], [0.3, 0.7]])
    result = add_residual_and_normalize(fused)
    expected = torch.tensor([[0.75, 0.25], [0.15, 0.85]])
    assert torch.allclose(result, expected, atol=1e-6)
    assert torch.allclose(result.sum(dim=-1), torch.ones(2), atol=1e-6)


def test_rollout_layers_two_layer_chain():
    layer1 = torch.tensor([[[[0.6, 0.4], [0.5, 0.5]]]])
    layer2 = torch.tensor([[[[0.9, 0.1], [0.2, 0.8]]]])

    result = rollout_layers((layer1, layer2), head_fusion="mean")
    expected = torch.tensor([[0.7725, 0.2275], [0.305, 0.695]])
    assert torch.allclose(result, expected, atol=1e-4)


def test_cls_attention_to_grid():
    rollout = torch.tensor(
        [
            [0.0, 0.1, 0.4, 0.2, 0.3],
            [0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0],
        ]
    )
    grid = cls_attention_to_grid(rollout, patch_grid=2)
    expected = torch.tensor([[0.25, 1.0], [0.5, 0.75]])
    assert torch.allclose(grid, expected, atol=1e-6)
    assert grid.max().item() == pytest.approx(1.0)


def test_attention_rollout_end_to_end_shape_and_range():
    torch.manual_seed(0)
    attentions = (
        torch.rand(1, 1, 5, 5),
        torch.rand(1, 1, 5, 5),
    )
    grid = attention_rollout(attentions, head_fusion="mean", patch_grid=2)

    assert isinstance(grid, np.ndarray)
    assert grid.shape == (2, 2)
    assert grid.max() == pytest.approx(1.0, abs=1e-5)
    assert grid.min() >= 0.0
