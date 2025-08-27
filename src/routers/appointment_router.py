from fastapi import APIRouter, HTTPException, Depends
from typing import List

# ---SERVICES ---
from src.services.appointement_service import AppointementService

# ---SCHEMA ---
from src.schemas.appointments import AppointmentSchema

from src.database import PyObjectId
from bson import ObjectId

router = APIRouter(prefix="/appointments", tags=["appointments"])
appointementService = AppointementService()

# --- Helper to convert string IDs to ObjectId before saving --- #
def _populate_objectids(data: dict) -> dict:
    objectid_fields = ["serviceId", "staffId", "departmentId", "createdBy", "patientId"]
    for key in objectid_fields:
        v = data.get(key)
        if v is not None and isinstance(v, str):
            try:
                data[key] = PyObjectId(v)
            except Exception:
                pass
    return data

# --- CREATE APPOINTMENT --- #
@router.post("/create-appointement", response_model=AppointmentSchema)
async def create_appointement(
    appointment: AppointmentSchema,
    current_user: str = Depends(appointementService.get_current_user)
):
    try:
        appointment_data = appointment.model_dump(exclude_unset=True)
        appointment_data["createdBy"] = current_user
        appointment_data["patientId"] = current_user
        appointment_data = _populate_objectids(appointment_data)
        new_appointment = await appointementService.create(appointment_data)
        return new_appointment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- LIST ALL APPOINTMENTS --- #
@router.get("/", response_model=List[AppointmentSchema])
async def list_appointments(
    current_user: str = Depends(appointementService.get_current_user)
):
    try:
        appointments = await appointementService.find_all()
        return [AppointmentSchema(**appt) for appt in appointments]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- GET APPOINTMENT BY ID --- #
@router.get("/{appointment_id}", response_model=AppointmentSchema)
async def get_appointment(
    appointment_id: str,
    current_user: str = Depends(appointementService.get_current_user)
):
    try:
        filter = {"_id" : ObjectId(appointment_id)}
        appointment = await appointementService.find_by_key(filter)
        if not appointment:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return appointment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# --- UPDATE APPOINTMENT --- #
@router.put("/{appointment_id}", response_model=AppointmentSchema)
async def update_appointment(
    appointment_id: str,
    appointment: AppointmentSchema,
    current_user: str = Depends(appointementService.get_current_user)
):
    """
    Update an appointment. Only provided fields will be updated.
    """
    appointment_data = appointment.model_dump(exclude_unset=True, exclude_defaults=True)

    try:
        appointment_data = _populate_objectids(appointment_data)

        try:
            filter_query = {"_id": ObjectId(appointment_id)}
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid appointment ID")

        updated = await appointementService.update(filter_query, appointment_data)

        if not updated:
            raise HTTPException(status_code=404, detail="Appointment not found or not updated")
        return updated

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
# --- DELETE APPOINTMENT (soft) --- #
@router.delete("/{appointment_id}")
async def delete_appointment(
    appointment_id: str,
    current_user: str = Depends(appointementService.get_current_user)
):
    try:
        filter = {"_id" : ObjectId(appointment_id)}
        result = await appointementService.delete_one(filter)
        if not result:
            raise HTTPException(status_code=404, detail="Appointment not found")
        return {"detail": "Appointment deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
