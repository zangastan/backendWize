# src/routers/chat_router.py
from fastapi import APIRouter, Depends
from  app.services.chat_services import ChatService
from ..schemas.chat_schema import ChatRequest

router = APIRouter(prefix="/chatbot", tags=["chatbot"])

@router.post("/chat")
async def send_chat(request: ChatRequest, chat_service: ChatService = Depends()):
    response = await chat_service.process_message(request.user_id, request.message)
    return {"response": response}
