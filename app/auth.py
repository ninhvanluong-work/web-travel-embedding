from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

# Define the API key header scheme
api_key_header = APIKeyHeader(name="Authorization", auto_error=True)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "WebTravelEmbeddingKey123456":
        raise HTTPException(status_code=401, detail="Invalid auth key")
    return api_key