# src/services/chat_service.py
import os
from dotenv import load_dotenv
from langdetect import detect
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from ..repositories.chat_repository import ChatRepository
from .knowledge_base import vectorstore

load_dotenv()

# Map detected language codes to supported languages
LANGUAGE_MAP = {
    "en": "English",
    "ny": "Chichewa",    # Nyanja/Chichewa
    "tum": "Tumbuka"     # fallback for Tumbuka
}

class ChatService:
    SUPPORTED_LANGUAGES = ["English", "Chichewa", "Tumbuka"]

    def __init__(self):
        self.chat_repo = ChatRepository()
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.7
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            return_source_documents=True
        )

        self.base_prompt = """
        You are a helpful assistant for Wezi Medical Centre only.
        Focus on enquiries about services (Outpatient, Inpatient, Emergency, Antenatal, Theatre), navigation, and bookings.
        For bookings, suggest using /book command. Do not discuss unrelated topics.
        """

    async def process_message(self, user_id: str, message: str, preferred_lang: str = None):
        # 1️⃣ Determine language
        if preferred_lang in self.SUPPORTED_LANGUAGES:
            lang = preferred_lang
        else:
            detected_lang = detect(message)
            if detected_lang.startswith("ny"):
                lang = "Chichewa"
            elif detected_lang.startswith("tum") or detected_lang in ["tumbuka"]:
                lang = "Tumbuka"
            else:
                lang = "English"

        # 2️⃣ Build system prompt
        system_prompt = f"{self.base_prompt}\nRespond clearly in {lang}."

        # 3️⃣ Retrieve chat history
        history = await self.chat_repo.get_chat_history(user_id)
        full_prompt = f"{system_prompt}\nHistory: {history}\nUser: {message}\nAssistant:"

        # 4️⃣ Generate AI response
        result = self.qa_chain.invoke({"query": full_prompt})
        response = result['result']

        # 5️⃣ Detect booking intent
        if "book" in message.lower() or "appointment" in message.lower():
            from .appointement_service import AppointementService
            appt_service = AppointementService()
            booking_status = await appt_service.create(user_id, message)
            response += f"\nBooking status: {booking_status}"

        # 6️⃣ Save chat
        await self.chat_repo.save_message(user_id, message, response)
        return response
