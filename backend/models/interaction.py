from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class InteractionBase(BaseModel):
    user_id: str
    product_id: str
    interaction_type: str # 'view', 'wishlist', 'purchase', 'rate'
    rating_value: Optional[float] = None # Only used if interaction_type is 'rate'

class InteractionCreate(InteractionBase):
    pass

class InteractionInDB(InteractionBase):
    id: str = Field(alias="_id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class InteractionOut(InteractionInDB):
    pass
