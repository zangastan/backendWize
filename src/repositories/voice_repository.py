# app/repositories/voice_repository.py
class VoiceRepository:
    async def process_command(self, text: str) -> str:
        text = text.lower()

        if "show stats" in text:
            return "Here are your stats."
        elif "open profile" in text:
            return "Opening your profile."
        elif "help" in text:
            return "You can say things like 'show stats' or 'open profile'."
        else:
            return "Sorry, I didn't understand that command."
