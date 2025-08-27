# src/services/base_service.py
from typing import List, Optional

class BaseService:
    def __init__(self, repository):
        self.repository = repository

    async def create(self, data: dict) -> dict:
        return await self.repository.create(data)

    async def find_by_id(self, id: str) -> Optional[dict]:
        return await self.repository.find_by_id(id)

    async def find_all(self, is_deleted : bool = False ) -> List[dict]:
        return await self.repository.find_all()

    async def update(self, id: str, data: dict) -> Optional[dict]:
        return await self.repository.update(id, data)

    async def delete(self, id: str) -> bool:
        return await self.repository.delete(id)
