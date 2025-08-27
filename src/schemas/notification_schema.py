from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict

class NotificationSubscriptionSchema(BaseSchema):
    is_push: bool = False
    is_email: bool = False
    is_sms: bool = False
    userId: PyObjectId