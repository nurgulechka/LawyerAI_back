import os

from app.config import database

from .adapters.chatgpt_service import ChatService
from .repository.repository import ChatRepository


class Service:
    def __init__(self):
        self.repository = ChatRepository(database)
        self.chat_service = ChatService(os.getenv("OPENAI_API_KEY"))
        # self.here_service = HereService(config.HERE_API_KEY)


def get_service():
    svc = Service()
    return svc
