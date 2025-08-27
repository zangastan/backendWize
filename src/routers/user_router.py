from fastapi import APIRouter, HTTPException
from src.schemas.user_schema import UserSchema
from src.services.user_service import UserService
from typing import Optional
router = APIRouter(prefix="/users", tags=["users"])
userService = UserService()

@router.post("/create-user", response_model=UserSchema)
async def create_user(user : UserSchema):
    user_doc = await userService.create(user.dict())
    if not user_doc:
        raise HTTPException(status_code=404, detailes="User not found")
    
    user = UserSchema(**user_doc)
    return user

@router.get("/findUser/{user_id}")
async def find_user(user_id : str):
    user_doc = await userService.find_by_id(user_id)
    if not user_doc:
        raise HTTPException(status_code=404 , detail="user is not found")
    
    user = UserSchema(**user_doc)
    return user

@router.get("/get-all-users")
async def find_all():
    user_doc = await userService.find_all()
    if not user_doc:
        raise HTTPException(status_code=404, detail="no users found")
    
    users = [UserSchema(**user) for user in user_doc]
    return users

@router.post("/update-user/${id}")
async def update_user(id : str , data : UserSchema):
    user = await userService.update(id, data.dict())
    if not update_user:
        raise HTTPException(status_code=500 , detail="Failed to update server error")
    
    updated_user = UserSchema(**user)
    return updated_user