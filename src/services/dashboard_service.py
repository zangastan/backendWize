from src.repositories.user_repository import UserRepository
from src.repositories.department_repository import DepartmentRepository
from src.services.base_service import BaseService
from src.schemas.dashoard_stats_schema import AdminDashboardStatsSchema, UserStatsSchema
from fastapi import HTTPException

class DashboardService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
        self.department_repository = DepartmentRepository()  # add department repo

    async def get_dashboard_stats(self, role: str, user_email: str):
        if role != "admin":
            raise HTTPException(status_code=501, detail="Dashboard stats not implemented for this role")

        # --- Admin stats ---
        total_patients = await self.repository.count({"role": "patient"})
        total_hods = await self.repository.count({"role": "hod"})
        total_admins = await self.repository.count({"role": "admin"})
        total_staff = await self.repository.count({"role": "staff"})
        users_stats = UserStatsSchema(
            patients=total_patients,
            hods=total_hods,
            admins=total_admins,
            staff=total_staff
        )

        # ✅ Get departments count
        departments_count = await self.department_repository.count({})

        # ✅ Fetch user data
        user_doc = await self.repository.find_by_key({"email": user_email})
        if "password_hash" in user_doc:
            user_doc["password_hash"] = "***"

        return AdminDashboardStatsSchema(
            users=users_stats,
            departments=departments_count,
            userData=user_doc
        )
