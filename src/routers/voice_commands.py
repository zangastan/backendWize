# app/routers/voice_command.py
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.repositories.voice_repository import VoiceRepository  # your repo

router = APIRouter(prefix="/voice", tags=["Voice Commands"])

class VoiceCommandRequest(BaseModel):
    text: str

class VoiceCommandResponse(BaseModel):
    response_text: str

@router.post("/", response_model=VoiceCommandResponse)
async def handle_voice_command(
    command: VoiceCommandRequest,
    repo: VoiceRepository = Depends()
):
    # use your repo to process command (or simple logic for now)
    response = await repo.process_command(command.text)
    return {"response_text": response}
