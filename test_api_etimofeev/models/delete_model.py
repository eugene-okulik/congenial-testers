from pydantic import BaseModel


class ProductResponseModel(BaseModel):
    message: str
