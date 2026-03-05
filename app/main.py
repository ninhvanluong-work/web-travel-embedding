from fastapi import FastAPI
from routers.api import apiRouter 

app = FastAPI()
app.include_router(apiRouter)

@app.get("/")
def home():
  return {"health": "true"}