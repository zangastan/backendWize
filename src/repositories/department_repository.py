from .base_repository import BaseRepository

class DepartmentRepository(BaseRepository):
    def __init__(self):
        super().__init__("departments")  # assuming your collection is named "departments"
