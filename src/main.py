from fastapi import FastAPI
from src.routers import (
    user_router,
    appointment_router,
    chat_router,
    ussd_router,
    dashboard_routes,
    department_routes
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Wezi Clinic Backend Service")


# Allow requests from your frontend origin (Next.js dev server)
origins = [
    "http://localhost:3000",  # your Next.js frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)

app.include_router(user_router.router)
app.include_router(appointment_router.router)
app.include_router(chat_router.router)
app.include_router(dashboard_routes.router)
app.include_router(department_routes.router)
# app.include_router(ussd_router.router)


@app.get("/")
def main_root():
    return {"message": "Backend is running..."}


# LindaKasolota@29
