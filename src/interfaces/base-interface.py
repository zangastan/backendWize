# src/interfaces/base_interface.py
from typing import List, Optional, Any, Dict

class BaseRepositoryInterface:
    async def create(self, data: dict) -> Any:
        raise NotImplementedError

    async def find_by_key(self,is_deleted: bool, filter : Dict) -> Optional[dict]:
        raise NotImplementedError

    async def find_all(self, is_deleted : bool) -> List[dict]:
        raise NotImplementedError

    async def update(self, filter : Dict, data : dict) -> Optional[dict]:
        raise NotImplementedError

    async def delete_one(self, filter: Dict) -> bool:
        raise NotImplementedError
    
    async def delete_many(self, data : List) -> bool:
        raise NotImplementedError
