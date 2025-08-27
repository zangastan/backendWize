from .base_service import BaseService
from src.repositories.staff_repository import StaffRepository
from src.security.auth import hash_password, verify_password, create_access_token, create_refresh_token
from src.schemas.auth_schema import UserCreate, UserLogin, Token
from src.schemas.user_schema import UserSchema
from src.schemas.patients_schema import PatientSchema
from datetime import datetime

class StaffService(BaseService):
    def __init__(self):
        super().__init__(StaffRepository())
        self.patient_repo = StaffRepository()