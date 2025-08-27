from fastapi import APIRouter, HTTPException, Depends

# --- SCHEMA --- 
from src.schemas.user_schema import UserSchema, UserResponse
from src.schemas.auth_schema import UserCreate, UserLogin, Token
from src.schemas.patients_schema import PatientSchema
from src.schemas.staff_schema import StaffSchema

# --- SERVICES ---
from src.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])
userService = UserService()

# --- Signup Route --- #
@router.post("/signup", response_model=UserSchema)
async def signup(
    user: UserCreate,
    patient: PatientSchema | None = None,
    staff: StaffSchema | None = None
):
    """
    Create a new user.
    If role == patient, provide patient details.
    If role == staff, provide staff details.
    """
    try:
        # Validate role-specific data
        if user.role == "patient" and not patient:
            raise HTTPException(status_code=400, detail="Patient data required for patient role")
        if user.role == "staff" and not staff:
            raise HTTPException(status_code=400, detail="Staff data required for staff role")

        # Register user and create related document
        user_doc = await userService.register_user(user, patient=patient, staff=staff)
        return UserSchema(**user_doc)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# --- Login Route --- #
@router.post("/login", response_model=Token)
async def login(userData: UserLogin):
    try:
        return await userService.login(userData)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


# --- Find Single Record --- #
@router.get("/find/{email}", response_model=UserResponse)
async def find_user(email: str):
    user_doc = await userService.find_by_key({"email" : email})
    if not user_doc:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(**user_doc)


# --- Find All Users --- #
@router.get("/all", response_model=list[UserResponse])
async def find_all():
    users = await userService.find_all()
    return [UserResponse(**user) for user in users]


# --- Update User --- #
@router.put("/update/{email}", response_model=UserSchema)
async def update_user(email: str, data: UserSchema):
    user = await userService.update(email, data.model_dump(exclude_unset=True))
    if not user:
        raise HTTPException(status_code=500, detail="Failed to update user")
    return UserSchema(**user)


# --- Delete User --- #
@router.delete("/delete/{id}")
async def delete_user(id: str):
    success = await userService.delete_one(id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or already deleted")
    return {"message": "User soft deleted successfully"}


# ---Testing --- #
from fastapi.security import OAuth2PasswordRequestForm

@router.post("/token", response_model=Token)
async def login_for_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await userService.login(
        UserLogin(email=form_data.username, password=form_data.password)
    )
    return user
