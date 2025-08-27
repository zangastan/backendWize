# src/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import Any
from pydantic_core import core_schema
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "wezi_clinic"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Helper for ObjectId conversion
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
        
    # ✅ For Pydantic v2 schema generation
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, _handler: Any) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema(),
        )
    @classmethod
    def validate(cls, v: Any):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
