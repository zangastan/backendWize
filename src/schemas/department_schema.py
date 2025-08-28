from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from src.database import PyObjectId

class DepartmentBase(BaseModel):
    name: str
    roomNumbers: Optional[int] = None
    contactPhone: Optional[str] = None
    description: Optional[str] = None
    locationNodeId: Optional[PyObjectId] = None

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    roomNumbers: Optional[int] = None
    contactPhone: Optional[str] = None
    description: Optional[str] = None
    locationNodeId: Optional[PyObjectId] = None

class DepartmentResponse(DepartmentBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
