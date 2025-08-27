from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict

class DepartmentSchema(BaseSchema):
    name: str
    roomNumbers: Optional[int] = None
    contactPhone: Optional[str] = None
    description: Optional[str] = None
    locationNodeId: Optional[PyObjectId] = None