from typing import List, Optional, Dict
from bson import ObjectId
from src.database import db

class BaseRepository:
    def __init__(self, collection_name: str):
        self.collection = db[collection_name]

    async def create(self, data: dict) -> dict:
        result = await self.collection.insert_one(data)
        data["_id"] = str(result.inserted_id)
        return data

    async def find_by_key(self, filter : Dict) -> Optional[dict]:
        filter["is_deleted"] = False
        return await self.collection.find_one(filter)

    async def find_all(self, is_deleted: bool = False) -> List[dict]:
        docs = []
        cursor = self.collection.find({"is_deleted": is_deleted})
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            docs.append(doc)
        return docs

    async def update(self, filter : Dict, data: dict) -> Optional[dict]:
        await self.collection.update_one(filter, {"$set": data})
        return await self.collection.find_one(filter)

    async def delete_one(self,filter : Dict ) -> bool:
        result = await self.collection.update_one(
            filter,
            {"$set": {"is_deleted": True}}
        )
        return result.modified_count == 1
