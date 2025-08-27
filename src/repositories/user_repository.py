from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__("users") #users is the collection name here
        