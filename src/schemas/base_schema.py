# src/schemas/user_schema.py
from pydantic import BaseModel, Field
from src.database import PyObjectId
from typing import Optional
from datetime import datetime, timezone
from datetime import datetime, timezone

class BaseSchema(BaseModel):
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    is_deleted: bool = False

    class Config:
        json_encoders = {PyObjectId: str}
        orm_mode = True
