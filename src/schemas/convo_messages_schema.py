from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict
from.enums import MessageSenderType
from datetime import datetime

class ConversationMessageSchema(BaseSchema):
    inquiryId: PyObjectId
    senderType: MessageSenderType
    senderId: PyObjectId
    body: str
    createdAt: Optional[datetime] = None
    readBy: Optional[List[PyObjectId]] = None