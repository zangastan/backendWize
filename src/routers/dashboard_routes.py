from fastapi import APIRouter, Depends, Header, HTTPException
from src.services.dashboard_service import DashboardService
from src.security.auth import decode_access_token
from src.schemas.dashoard_stats_schema import AdminDashboardStatsSchema
from jose import JWTError, ExpiredSignatureError

router = APIRouter(prefix="/dashboard", tags=["dashboard"])
dashboard_service = DashboardService()


async def get_current_user_role(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        payload = decode_access_token(token)
        role = payload.get("role")
        user_id = payload.get("sub")
        email = payload.get("email")
        if not role or not user_id:
            raise HTTPException(
                status_code=403, detail="Role or user_id not found in token"
            )
        return {"role": role, "user_id": user_id, "email": email}
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401, detail="Token has expired. Please login again."
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/{role}", response_model=AdminDashboardStatsSchema)
async def get_dashboard(role: str, current_user: dict = Depends(get_current_user_role)):
    if current_user["role"] != role:
        raise HTTPException(
            status_code=403, detail="Unauthorized to access this dashboard"
        )

    return await dashboard_service.get_dashboard_stats(role, current_user["email"])
