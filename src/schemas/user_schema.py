from .base_schema import BaseSchema
from pydantic import EmailStr, Field, field_validator
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


# ---- User Schema ---- #
class UserSchema(BaseSchema):
    # Authentication
    email: EmailStr
    password_hash: str

    # Profile
    full_name: str
    gender: Genders
    dob: datetime   # ✅ store as datetime so Mongo accepts it
    phone_number: Optional[str] = None
    preferred_lang: Optional[str] = "en" 
    accessibility: Optional[str] = None  

    # Role & Relationships
    role: UserRoles
    staff_role: Optional[StaffRoles] = None   # Only required if role == STAFF
    linked_patient_id: Optional[PyObjectId] = None
    linked_staff_id: Optional[PyObjectId] = None

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
    
    @field_validator("linked_patient_id", "linked_staff_id", mode="before")
    def convert_objectid_to_str(cls, v):
        if v is not None:
            return str(v)  # convert ObjectId to string
        return v
    

