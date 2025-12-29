from fastapi import FastAPI
from app.routers import chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Personal Assistant for Augustine Kasolota ")


origins = [
    "http://localhost:3000",
    "https://augustinekasolota.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,  # IMPORTANT
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router.router)

@app.get("/")
def main_root():
    return {"message": "Backend is running..."}
