from .base_service import BaseService
from src.repositories.patient_repository import PatientsRepository
from src.security.auth import hash_password, verify_password, create_access_token, create_refresh_token
from src.schemas.auth_schema import UserCreate, UserLogin, Token
from src.schemas.user_schema import UserSchema
from src.schemas.patients_schema import PatientSchema
from datetime import datetime

class PatientService(BaseService):
    def __init__(self):
        super().__init__(PatientsRepository())
        self.patient_repo = PatientsRepository()