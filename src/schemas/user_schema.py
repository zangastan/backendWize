from .base_schema import BaseSchema
from pydantic import EmailStr, Field, field_validator, model_validator
from src.database import PyObjectId
from typing import Optional
from enum import Enum
from datetime import datetime, date

# ---- Permissions ---- #
class Permissions(str, Enum):
    VIEW_PATIENT = "view_patient"
    EDIT_PATIENT = "edit_patient"
    DELETE_PATIENT = "delete_patient"
    CREATE_STAFF = "create_staff"
    MANAGE_USERS = "manage_users"
    CREATE_APPOINTMENT = "create_appointment"
    EDIT_APPOINTMENT = "edit_appointment"


ROLE_PERMISSIONS = {
    "admin": {Permissions.MANAGE_USERS, Permissions.CREATE_STAFF, Permissions.EDIT_PATIENT, Permissions.DELETE_PATIENT},
    "doctor": {Permissions.VIEW_PATIENT, Permissions.EDIT_PATIENT, Permissions.EDIT_APPOINTMENT},
    "nurse": {Permissions.VIEW_PATIENT},
    "amb_driver": set(),
    "patient": {Permissions.VIEW_PATIENT, Permissions.CREATE_APPOINTMENT},
}

# ---- Enums ---- #
class StaffRoles(str, Enum):
    DOCTOR = "doctor"
    NURSE = "nurse"
    AMB_DRIVER = "amb_driver"  

class UserRoles(str, Enum):
    ADMIN = "admin"
    PATIENT = "patient"
    STAFF = "staff" 

class Genders(str, Enum):
    MALE = "male"
    FEMALE = "female"
    RNS = "rns"  # rather not say

# --- Response Schema --- #
class UserResponse(BaseSchema):
    id: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[UserRoles] = None
    staff_role: Optional[StaffRoles] = None

    class Config:
        orm_mode = True

    @model_validator(mode="before")
    def convert_objectid(cls, values):
        # Map Mongo _id to id
        if "_id" in values:
            values["id"] = str(values.pop("_id"))
        return values

# ---- User Schema ---- #
class UserSchema(BaseSchema):
    # Authentication
    _id : Optional[str] = ""
    email: EmailStr
    password_hash: str

    # Profile
    full_name: Optional[str] = None
    gender: Optional[Genders] = None
    dob: datetime   # ✅ store as datetime so Mongo accepts it
    phone_number: Optional[str] = None
    preferred_lang: Optional[str] = "en" 
    accessibility: Optional[str] = None  

    # Role & Relationships
    role: UserRoles
    staff_role: Optional[StaffRoles] = None   # Only required if role == STAFF
    
    # ---- Config ---- #
    class Config:
        use_enum_values = True  # Enums will serialize as "admin", not <UserRoles.ADMIN: 'admin'>
        json_encoders = {PyObjectId: str}

    # ---- Validators ---- #
    @field_validator("dob", mode="before")
    def parse_dob(cls, v):
        if isinstance(v, date) and not isinstance(v, datetime):
            return datetime.combine(v, datetime.min.time())
        return v
    
    # @field_validator("linked_patient_id", "linked_staff_id", mode="before")
    # def convert_objectid_to_str(cls, v):
    #     if v is not None:
    #         return str(v)  # convert ObjectId to string
    #     return v
    

