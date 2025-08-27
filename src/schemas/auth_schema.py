# auth schema
from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
from typing import Optional
from datetime import date
from .user_schema import UserRoles, StaffRoles , Genders 
from .base_schema import BaseSchema

class UserCreate(BaseSchema):
    email: EmailStr
    password: str  # plain password
    full_name: str
    gender: Genders
    dob: date
    phone_number: Optional[str] = None
    preferred_lang: Optional[str] = "en"
    accessibility: Optional[str] = None
    role: UserRoles
    staff_role: Optional[StaffRoles] = None
    
    @field_validator("dob", mode="before")
    def parse_dob(cls, v):
        if isinstance(v, date) and not isinstance(v, datetime):
            return datetime.combine(v, datetime.min.time())
        return v
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    role: str
    createdAt: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    
