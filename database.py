# src/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import Any
from pydantic_core import core_schema
import certifi  # ✅ for trusted CA bundle

MONGO_URI = "mongodb+srv://stanashady1:d0B3bR2FlscqhYNp@cluster0.4prt2wj.mongodb.net/portfolio?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "portfolio"

# Add tlsCAFile=certifi.where() to fix certificate verification
client = AsyncIOMotorClient(MONGO_URI, tls=True, tlsCAFile=certifi.where())
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
