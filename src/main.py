from fastapi import FastAPI
from src.routers import user_router , appointment_router, chat_router, ussd_router

app = FastAPI(title="Wezi Clinic Backend Service")

app.include_router(user_router.router)
app.include_router(appointment_router.router)
app.include_router(chat_router.router)
# app.include_router(ussd_router.router)


@app.get("/")
def main_root():
    return {"message": "Backend is running..."}


# LindaKasolota@29