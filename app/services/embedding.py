import torch
import numpy as np
from model_loader import model, tokenizer
from schema.embedding import VideoEmbeddingInput

VIDEO_WEIGHT = {
    "destination": 0.5,
    "video": 0.2,
    "product": 0.3, 
}

def get_embedding(text: str):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state[:, 0, :]  # CLS token
    # Normalize
    embeddings = embeddings / torch.norm(embeddings, p=2)
    return embeddings[0].tolist()

def get_video_embedding(payload: VideoEmbeddingInput):
    destination = payload.destination
    video = payload.video
    product = payload.video
  
    fields = {
        "destination": destination,
        "video": video,
        "product": product,
    }

    vector_list = []
    for key, field in fields.items():
        text = f"{field.name} {field.description}"
        embedding = np.array(get_embedding(text))
        weighted = embedding * VIDEO_WEIGHT[key]
        vector_list.append(weighted)

    if(len(vector_list) == 0):
        return []
    # Combine all event vectors into a single vector
    vector_list = np.array(vector_list)
    final_vector = np.sum(vector_list, axis=0)
    norm = np.linalg.norm(final_vector)
    if norm == 0:
        return []
    final_vector = final_vector / norm
    return final_vector.tolist()
            