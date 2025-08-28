from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.department_schema import DepartmentCreate, DepartmentUpdate, DepartmentResponse
from src.services.department_service import DepartmentService
from bson import ObjectId

router = APIRouter(prefix="/departments", tags=["Departments"])
department_service = DepartmentService()


@router.post("/", response_model=DepartmentResponse)
async def create_department(department: DepartmentCreate):
    new_dept = await department_service.create(department)
    return new_dept

@router.get("/{department_id}", response_model=DepartmentResponse)
async def get_department(department_id: str):
    dept = await department_service.find_by_key({ "_id": ObjectId(department_id) })
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept

@router.get("/", response_model=List[DepartmentResponse])
async def list_departments():
    return await department_service.find_all()

@router.put("/{department_id}", response_model=DepartmentResponse)
async def update_department(department_id: str, department: DepartmentUpdate):
    updated = await department_service.update(department_id, department)
    if not updated:
        raise HTTPException(status_code=404, detail="Department not found")
    return updated

@router.delete("/{department_id}")
async def delete_department(department_id: str):
    deleted = await department_service.delete_one(department_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Department not found")
    return {"message": "Department deleted successfully"}
