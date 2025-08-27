from .base_schema import BaseSchema
from src.database import PyObjectId  # Custom ObjectId wrapper
from typing import Optional
from datetime import datetime
from .enums import AppointmentStatus
from pydantic import field_validator

class AppointmentSchema(BaseSchema):
    patientId: Optional[PyObjectId] = None
    serviceId: Optional[PyObjectId] = None
    staffId: Optional[PyObjectId] = None
    departmentId: Optional[PyObjectId] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    status: AppointmentStatus = AppointmentStatus.scheduled
    createdBy: Optional[PyObjectId] = None
    notes: Optional[str] = None

    @field_validator("departmentId", "staffId", "serviceId", "createdBy","patientId", mode="before")
    def convert_objectid_to_str(cls, v):
        if v is not None:
            return str(v)
        return v

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
