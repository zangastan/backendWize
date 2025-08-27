from .base_schema import BaseSchema
from src.database import PyObjectId
from typing import Optional, List, Dict
from .enums import AmbulancePriority, AmbulanceStatus

class AmbulanceRequestSchema(BaseSchema):
    patientId: Optional[PyObjectId] = None
    pickupLocation: Optional[Dict[str, float]] = None  # GeoJSON {lng, lat}
    priority: AmbulancePriority = AmbulancePriority.low
    status: AmbulanceStatus = AmbulanceStatus.requested
