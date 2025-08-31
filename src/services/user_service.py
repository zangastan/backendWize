from .base_service import BaseService
from enum import Enum
from datetime import date , datetime
from bson import ObjectId

# --- REPOSITORIES ---
from src.repositories.user_repository import UserRepository
from src.repositories.patient_repository import PatientsRepository
from src.repositories.staff_repository import StaffRepository

# --- SECURITY ---
from src.security.auth import hash_password, verify_password, create_access_token, create_refresh_token


# --- SCHEMAS ---
from src.schemas.auth_schema import UserCreate, UserLogin, Token
from src.schemas.user_schema import UserSchema
from src.schemas.patients_schema import PatientSchema
from src.schemas.staff_schema import StaffSchema

# from datetime import datetime


class UserService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
        self.patient_repo = PatientsRepository()
        self.staff_repo = StaffRepository()

# --- account creation --- #
    async def register_user(
        self, 
        user: UserCreate, 
        patient: PatientSchema | None = None, 
        staff: StaffSchema | None = None
    ) -> dict:
        existing_user = await self.repository.find_by_key({"email" :user.email})
        if existing_user:
            raise ValueError("User already exists")

        user_data = user.model_dump()

        # Convert Enums to values
        if isinstance(user_data["role"], Enum):
            user_data["role"] = user_data["role"].value
        if isinstance(user_data["gender"], Enum):
            user_data["gender"] = user_data["gender"].value
        if user_data.get("staff_role") and isinstance(user_data["staff_role"], Enum):
            user_data["staff_role"] = user_data["staff_role"].value

        # Ensure dob is datetime
        dob = user_data.get("dob")
        if isinstance(dob, date) and not isinstance(dob, datetime):
            user_data["dob"] = datetime.combine(dob, datetime.min.time())

        # Hash password
        user_data["password_hash"] = hash_password(user_data.pop("password"))

        new_user = await self.repository.create(user_data)

        if new_user["role"] == "patient" and patient:
            patient_data = patient.model_dump()
            patient_data["linkedPatientId"] = new_user["_id"]
            await self.patient_repo.create(patient_data)

        if new_user["role"] == "staff" and staff:
            staff_data = staff.model_dump()
            if staff_data.get("departmentId") and isinstance(staff_data["departmentId"], str):
                staff_data["departmentId"] = ObjectId(staff_data["departmentId"])
            staff_data["linkedStaffId"] = new_user["_id"]
            await self.staff_repo.create(staff_data)

        return new_user

    # --- user login --- #
    async def login(self, user: UserLogin) -> Token:
        db_user = await self.repository.find_by_key({"email":user.email})
        if not db_user or not verify_password(user.password, db_user["password_hash"]):
            raise ValueError("Invalid credentials")

        payload = {
            "sub": str(db_user["_id"]),
            "email": db_user["email"],
            "role": db_user["role"],
        }

        access_token = create_access_token(payload)
        refresh_token = create_refresh_token(payload)
        return Token(access_token=access_token, refresh_token=refresh_token)
