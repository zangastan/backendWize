from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict
from pydantic import Field

class PatientSchema(BaseSchema):
    address: Dict[str, str]
    nationId: str = Field(..., min_length=6, max_length=6)
    conditions: Optional[List[str]] = None
    emergencyContact: Optional[Dict[str, str]] = None
    medicalRecords: Optional[List[str]] = None  # Could be file paths
