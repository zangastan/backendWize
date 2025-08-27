from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict
from .enums import NotificationRecipientType, NotificationType
from datetime import datetime

class NotificationSchema(BaseSchema):
    recipientId: NotificationRecipientType
    notificationType: NotificationType
    title: str
    body: str
    channels: Optional[List[str]] = None
    metadata: Optional[dict] = None
    deliveredAt: Optional[datetime] = None
    readAt: Optional[datetime] = None
    status: Optional[str] = None
    createdAt: Optional[datetime] = None