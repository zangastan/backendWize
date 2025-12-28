# src/schemas/chat_schema.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.database import PyObjectId

class ChatMessageSchema(BaseModel):
    patientId: PyObjectId
    sender: str  # "patient" or "bot"
    message: str
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
        json_encoders = {PyObjectId: str}

class ChatRequest(BaseModel):
    user_id: str
    message: str
