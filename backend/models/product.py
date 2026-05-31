from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    title: str
    description: str
    price: float
    category: str
    tags: List[str] = []
    image_url: Optional[str] = None
    stock: int = 0
    rating: float = 0.0

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: str = Field(alias="_id")
    created_at: datetime
    ai_summary: Optional[str] = None # AI generated summary

class ProductOut(ProductInDB):
    pass
