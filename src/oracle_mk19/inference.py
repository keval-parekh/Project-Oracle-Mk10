import torch
from PIL import Image

from .rollout import attention_rollout


def classify_and_attend(frame_rgb, processor, model, device, head_fusion: str = "mean"):
    pil_image = Image.fromarray(frame_rgb)
    inputs = processor(images=pil_image, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    attentions = tuple(torch.nn.functional.softmax(a, dim=-1) for a in outputs.attentions)
    attn_grid = attention_rollout(attentions, head_fusion=head_fusion)

    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)[0]
    top_prob, top_idx = probs.max(dim=-1)
    label = model.config.id2label[top_idx.item()]
    confidence = top_prob.item() * 100

    return attn_grid, label, confidence
