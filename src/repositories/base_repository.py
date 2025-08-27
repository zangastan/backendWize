from typing import List, Optional
from bson import ObjectId
from src.database import db

class BaseRepository:
    def __init__(self, collection_name: str):
        self.collection = db[collection_name]

    async def create(self, data: dict) -> dict:
        result = await self.collection.insert_one(data)
        data["_id"] = str(result.inserted_id)
        return data

    async def find_by_id(self,id: str) -> Optional[dict]:
        doc = await self.collection.find_one({"_id": ObjectId(id), "is_deleted": False})
        if doc:
            doc["_id"] = str(doc["_id"])
        return doc

    async def find_all(self, is_deleted : bool = False) -> List[dict]:
        docs = []
        cursor = self.collection.find({"is_deleted": is_deleted})  # Cursor, not awaitable
        async for doc in cursor:  # Correct way to iterate
            doc["_id"] = str(doc["_id"])
            docs.append(doc)
        return docs

    async def update(self, id: str, data: dict) -> Optional[dict]:
        await self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return await self.find_by_id(id)

    async def delete(self, id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count == 1
