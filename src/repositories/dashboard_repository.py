from .base_repository import BaseRepository
from bson import ObjectId

class DashboardRepository(BaseRepository):
    def __init__(self):
        super().__init__("users") 

    async def count_users_by_role(self, role: str) -> int:
        return await self.collection.count_documents({"role": role})

    async def count_all_patients(self) -> int:
        from src.repositories.patient_repository import PatientsRepository
        patient_repo = PatientsRepository()
        return await patient_repo.collection.count_documents({})

    async def count_all_staff(self) -> int:
        from src.repositories.staff_repository import StaffRepository
        staff_repo = StaffRepository()
        return await staff_repo.collection.count_documents({})

    async def recent_users(self, limit: int = 5):
        cursor = self.collection.find().sort("createdAt", -1).limit(limit)
        return [user async for user in cursor]
