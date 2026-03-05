from fastapi import APIRouter, HTTPException
from services.embedding import get_embedding, get_video_embedding
from schema.embedding import TextInput, VideoEmbeddingInput



embeddingRouter = APIRouter(prefix='/embedding', tags=['embedding'])

@embeddingRouter.post("")
async def embed_text(payload: TextInput):
    try:
        vector = get_embedding(payload.text)
        return {"embedding": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@embeddingRouter.post("/video")
async def embed_video(payload: VideoEmbeddingInput):
    try:
        vector = get_video_embedding(payload)
        return {"embedding": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


