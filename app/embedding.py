import torch
import numpy as np
from model_loader import model, tokenizer


def get_embedding(text: str):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :]  # CLS token
    # Normalize
    embeddings = embeddings / torch.norm(embeddings, p=2)
    return embeddings[0].tolist()

            