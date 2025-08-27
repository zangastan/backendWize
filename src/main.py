from fastapi import FastAPI
from src.routers import user_router
app = FastAPI(title="Wezi Clinic Backend Service")


app.include_router(user_router.router)
@app.get("/")
def main_root():
    return {"message": "Backend is running..."}