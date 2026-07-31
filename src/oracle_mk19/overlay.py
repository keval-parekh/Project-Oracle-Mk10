import cv2
import numpy as np


def resize_attention_map(attn_grid: np.ndarray, width: int, height: int) -> np.ndarray:
    resized = cv2.resize(attn_grid, (width, height), interpolation=cv2.INTER_CUBIC)
    return np.clip(resized, 0, 1)


def make_heatmap(attn_resized: np.ndarray, colormap: int = cv2.COLORMAP_JET) -> np.ndarray:
    attn_uint8 = (attn_resized * 255).astype(np.uint8)
    return cv2.applyColorMap(attn_uint8, colormap)


def blend_heatmap(frame: np.ndarray, heatmap: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    return cv2.addWeighted(frame, alpha, heatmap, 1 - alpha, 0)


def draw_label_banner(
    frame: np.ndarray,
    label: str,
    confidence: float,
    banner_height: int = 40,
    banner_alpha: float = 0.6,
) -> np.ndarray:
    h, w = frame.shape[:2]
    text = f"{label}: {confidence:.1f}%"

    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, banner_height), (0, 0, 0), -1)
    blended = cv2.addWeighted(overlay, banner_alpha, frame, 1 - banner_alpha, 0)

    cv2.putText(
        blended,
        text,
        (10, 28),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    return blended


def render_frame(
    frame: np.ndarray,
    attn_grid: np.ndarray,
    label: str,
    confidence: float,
) -> np.ndarray:
    h, w = frame.shape[:2]
    attn_resized = resize_attention_map(attn_grid, w, h)
    heatmap = make_heatmap(attn_resized)
    blended = blend_heatmap(frame, heatmap)
    return draw_label_banner(blended, label, confidence)
