# user repository file
from .base_repository import BaseRepository

class StaffRepository(BaseRepository):
    def __init__(self):
        super().__init__("staff") #staff is the collection name here
        