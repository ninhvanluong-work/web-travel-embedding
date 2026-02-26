from fastapi import APIRouter, HTTPException
from embedding import get_embedding
from schemas import TextInput

router = APIRouter()

@router.post("/embed")
async def embed_text(payload: TextInput):
    try:
        vector = get_embedding(payload.text)
        return {"embedding": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


