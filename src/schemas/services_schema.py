from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict

class ServiceSchema(BaseSchema):
    name: str
    departmentId: PyObjectId
    description: Optional[str] = None
    isEmergencyService: bool = False
    multilingual: Optional[Dict[str, str]] = None