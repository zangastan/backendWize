from typing import Optional
from .user_schema import UserSchema


from pydantic import BaseModel


class UserStatsSchema(BaseModel):
    patients: int
    hods: int
    admins: int
    staff: int


class AdminDashboardStatsSchema(BaseModel):
    users: UserStatsSchema
    departments: int
    userData: Optional[UserSchema] = None
