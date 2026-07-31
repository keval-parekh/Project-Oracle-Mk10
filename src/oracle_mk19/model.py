import torch
from transformers import ViTImageProcessor, ViTForImageClassification

from .config import MODEL_NAME


def load_model(model_name: str = MODEL_NAME, device: torch.device = torch.device("cpu")):
    processor = ViTImageProcessor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(
        model_name,
        attn_implementation="eager",
        output_attentions=True,
    )
    model.eval()
    model.to(device)
    return processor, model
