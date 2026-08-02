import torch

from .config import PATCH_GRID


def fuse_heads(layer_attention: torch.Tensor, head_fusion: str = "mean") -> torch.Tensor:
    if head_fusion == "mean":
        return layer_attention.mean(dim=0)
    if head_fusion == "max":
        return layer_attention.max(dim=0)[0]
    if head_fusion == "min":
        return layer_attention.min(dim=1)[0]
    raise ValueError(f"Unknown head_fusion strategy: {head_fusion!r}")


def add_residual_and_normalize(fused: torch.Tensor) -> torch.Tensor:
    fused = fused / fused.sum(dim=-1, keepdim=True)
    return fused


def rollout_layers(attentions, head_fusion: str = "mean") -> torch.Tensor:
    layer_attention = attentions[-1]
    fused = fuse_heads(layer_attention, head_fusion)
    return fused[0]


def cls_attention_to_grid(rollout: torch.Tensor, patch_grid: int = PATCH_GRID) -> torch.Tensor:
    cls_attention = rollout[:, 1:].mean(dim=0)
    cls_attention = cls_attention / cls_attention.max()
    return cls_attention.reshape(patch_grid, patch_grid)


@torch.no_grad()
def attention_rollout(
    attentions, head_fusion: str = "mean", patch_grid: int = PATCH_GRID
) -> "np.ndarray":
    rollout = rollout_layers(attentions, head_fusion)
    grid = cls_attention_to_grid(rollout, patch_grid)
    return grid.cpu().numpy()
