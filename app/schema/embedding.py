from pydantic import BaseModel, Field

class DestinationInput(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

class VideoInput(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

class ProductInput(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    
class VideoEmbeddingInput(BaseModel):
  destination: DestinationInput
  video: VideoInput
  product: ProductInput


class TextInput(BaseModel):
    text: str