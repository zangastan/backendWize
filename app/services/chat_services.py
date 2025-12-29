# src/services/chat_service.py
import os
from dotenv import load_dotenv
from langdetect import detect
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from ..repositories.chat_repository import ChatRepository

load_dotenv()

LANGUAGE_MAP = {
    "en": "English",
    "ny": "Chichewa",
    "tum": "Tumbuka"
}

class ChatService:
    SUPPORTED_LANGUAGES = ["English", "Chichewa", "Tumbuka"]

    def __init__(self):
        self.chat_repo = ChatRepository()
        self.llm = None
        self.qa_chain = None

        self.base_prompt = """
You are Augustine Kasolota's personal assistant.
Answer questions about Augustine—his skills, education, interests, passions, hobbies, life, and general information about him.
Keep responses friendly, light, and sometimes playful.
Short answers are fine.
If unsure, respond thoughtfully instead of saying "I don’t know".
        """

    def _init_ai(self):
        """Lazy-load AI components (VERY IMPORTANT for Render)"""
        if self.qa_chain is not None:
            return

        from .knowledge_base import vectorstore  # import here, not at top

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.7
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            return_source_documents=True
        )

    async def process_message(self, user_id: str, message: str, preferred_lang: str = None):
        # initialize AI only when needed
        self._init_ai()

        # detect language
        if preferred_lang in self.SUPPORTED_LANGUAGES:
            lang = preferred_lang
        else:
            detected = detect(message)
            if detected.startswith("ny"):
                lang = "Chichewa"
            elif detected.startswith("tum"):
                lang = "Tumbuka"
            else:
                lang = "English"

        system_prompt = f"{self.base_prompt}\nRespond clearly in {lang}."

        history = await self.chat_repo.get_chat_history(user_id)
        full_prompt = f"{system_prompt}\nHistory: {history}\nUser: {message}\nAssistant:"

        result = self.qa_chain.invoke({"query": full_prompt})
        return result["result"]
