from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProductData(BaseModel):
    year: Optional[int] = None
    price: Optional[float] = None
    CPU_model: Optional[str] = None
    Hard_disk_size: Optional[str] = None
    color: Optional[str] = None


class ProductUpdateRequestModel(BaseModel):
    name: str


class ProductResponseModel(BaseModel):
    id: str
    name: str
    data: Optional[ProductData] = None
    updatedAt: Optional[datetime] = None
