from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict

class MedicalRecordSchema(BaseSchema):
    patientId: PyObjectId
    recordType: str
    storagePath: str
    encryption: Optional[Dict[str, str]] = None
    accessRestricted: bool = True