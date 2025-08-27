# src/interfaces/base_interface.py
from typing import List, Optional, Any

class BaseRepositoryInterface:
    async def create(self, data: dict) -> Any:
        raise NotImplementedError

    async def find_by_id(self,is_deleted: bool, id: str) -> Optional[dict]:
        raise NotImplementedError

    async def find_all(self, is_deleted : bool) -> List[dict]:
        raise NotImplementedError

    async def update(self, id: str, data: dict) -> Optional[dict]:
        raise NotImplementedError

    async def delete(self, id: str) -> bool:
        raise NotImplementedError
