from fastapi import FastAPI
from app.routers import chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Personal Assistant for Augustine Kasolota ")


# Allow requests from your frontend origin (Next.js dev server)
origins = [
    "http://localhost:3000",  # 
    "http://127.0.0.1:5500", # testing...
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allow GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)


# app.include_router(chat_router.router)

@app.get("/")
def main_root():
    return {"message": "Backend is running..."}


# LindaKasolota@29