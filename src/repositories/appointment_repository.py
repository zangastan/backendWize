# user repository file
from .base_repository import BaseRepository

class AppointmentRepository(BaseRepository):
    def __init__(self):
        super().__init__("appointments") #appointments is the collection name here
        