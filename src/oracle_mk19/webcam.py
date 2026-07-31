import cv2

from .device import get_device
from .model import load_model, MODEL_NAME
from .inference import classify_and_attend
from .overlay import render_frame

WINDOW_NAME = "Project Oracle Mk19 - ViT Attention Rollout (press 'q' to quit)"


def run(model_name: str = MODEL_NAME, camera_index: int = 0, head_fusion: str = "mean") -> None:
    device = get_device()
    print(f"[INFO] Using device: {device}")

    processor, model = load_model(model_name, device)

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam. Check camera permissions/index.")

    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARN] Failed to grab frame, exiting.")
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            attn_grid, label, confidence = classify_and_attend(
                rgb_frame, processor, model, device, head_fusion
            )

            blended = render_frame(frame, attn_grid, label, confidence)
            cv2.imshow(WINDOW_NAME, blended)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
