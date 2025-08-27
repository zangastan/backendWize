from .base_service import BaseService
from src.repositories.user_repository import UserRepository
class UserService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
    