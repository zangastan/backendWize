from .base_service import BaseService
from src.repositories.appointment_repository import AppointmentRepository
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from src.security.auth import decode_access_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/users/token")

class AppointementService(BaseService):
    def __init__(self):
        super().__init__(AppointmentRepository())
        
    async def get_current_user(self, token: str = Depends(oauth2_schema)):
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise ValueError("Invalid token: missing user id")
        return user_id
