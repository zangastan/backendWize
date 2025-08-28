from src.repositories.department_repository import DepartmentRepository
from src.schemas.department_schema import DepartmentCreate, DepartmentUpdate
from .base_service import BaseService


class DepartmentService(BaseService):
    def __init__(self):
        super().__init__(DepartmentRepository())
        
