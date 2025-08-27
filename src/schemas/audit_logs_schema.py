from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict
from datetime import datetime
from .enums import ActorType

class AuditLogSchema(BaseSchema):
    actorId: PyObjectId
    actorType: ActorType
    action: str
    targetCollection: str
    details: Optional[dict] = None
    ip: Optional[str] = None
    timestamp: Optional[datetime] = datetime.now()