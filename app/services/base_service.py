from typing import List, Optional, Dict

class BaseService:
    def __init__(self, repository):
        self.repository = repository

    async def create(self, data: dict) -> dict:
        return await self.repository.create(data)

    async def find_by_key(self, filter : Dict) -> Optional[dict]:
        return await self.repository.find_by_key(filter)

    async def find_all(self, is_deleted: bool = False) -> List[dict]:
        return await self.repository.find_all(is_deleted)

    async def update(self, filter : Dict, data: dict) -> Optional[dict]:
        return await self.repository.update(filter, data)

    async def delete_one(self, filter : Dict) -> bool:
        data = {"is_deleted": True}
        return await self.repository.update(filter,data)
