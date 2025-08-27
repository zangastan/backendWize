# inquries schema
from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict
from .enums import InquiryStatus 
from datetime import datetime

class InquirySchema(BaseSchema):
    patientId: Optional[PyObjectId] = None
    responder: Optional[PyObjectId] = None
    topic: Optional[str] = None
    departmentId: Optional[PyObjectId] = None
    status: InquiryStatus = InquiryStatus.open
    priority: str = "normal"
    lastActivityAt: Optional[datetime] = None