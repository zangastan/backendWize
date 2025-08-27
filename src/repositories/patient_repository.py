# user repository file
from .base_repository import BaseRepository

class PatientsRepository(BaseRepository):
    def __init__(self):
        super().__init__("patients") #patients is the collection name here
        