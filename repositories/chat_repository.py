# src/repositories/chat_repository.py
from typing import List, Optional, Dict
from  repositories.base_repository import BaseRepository

class ChatRepository(BaseRepository):
    def __init__(self):
        super().__init__("chats")  # MongoDB collection for chat messages

    async def save_message(self, user_id: str, user_message: str, bot_response: str):
        await self.collection.insert_one({
            # "user_id": user_id,
            "user_message": user_message,
            "bot_response": bot_response
        })
    async def get_chat_history(self, user_id: str):
        ...
        # cursor = self.collection.find()
        # history = []
        # async for doc in cursor:
        #     history.append(f"User: {doc['user_message']}\nAssistant: {doc['bot_response']}")
        # return "\n".join(history)