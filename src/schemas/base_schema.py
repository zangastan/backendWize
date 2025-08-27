# src/schemas/user_schema.py
from pydantic import BaseModel, Field
from src.database import PyObjectId
from typing import Optional
from datetime import datetime

class BaseSchema(BaseModel):
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt : datetime = Field(default_factory=datetime.utcnow)
    is_deleted : Optional[bool] = False 
    class Config:
        json_encoders = {PyObjectId: str}
        orm_mode = True
