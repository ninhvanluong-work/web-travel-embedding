from fastapi import APIRouter
from routers.embedding import embeddingRouter

apiRouter = APIRouter()

apiRouter.include_router(embeddingRouter)