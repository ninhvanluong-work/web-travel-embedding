from fastapi import FastAPI, Depends
from auth import verify_api_key
from api import router

#check authentication in all routes

#app = FastAPI(dependencies=[Depends(verify_api_key)])
app = FastAPI()
app.include_router(router)