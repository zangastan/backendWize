from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict
from .enums import StaffRoleWithin
from pydantic import field_validator
from bson import ObjectId

class StaffSchema(BaseSchema):
    roleWithin: StaffRoleWithin
    specialties: Optional[List[str]] = None
    departmentId: Optional[PyObjectId] = None
    workingHours: Optional[List[Dict[str, str]]] = None
    isAvailable: bool = True

    @field_validator("departmentId", mode="before")
    def convert_objectid_to_str(cls, v):
        if v is not None:
            return str(v)  # convert ObjectId to string
        return v
    