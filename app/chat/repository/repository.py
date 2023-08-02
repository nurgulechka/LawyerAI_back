import os
from datetime import datetime
from typing import Optional

from bson.objectid import ObjectId
from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from pymongo.database import Database

from ..utils.security import hash_password

load_dotenv()


class ChatRepository:
    def __init__(self, database: Database):
        self.database = database

    def get_response(self, user_question: str):
        os.getenv("OPENAI_API_KEY")
        embeddings = OpenAIEmbeddings()
        db = Chroma(embedding_function=embeddings, persist_directory="database")
        llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0.0)
        chain = load_qa_chain(llm=llm, chain_type="stuff")
        docs = db.similarity_search(user_question)
        return chain.run({"input_documents": docs, "question": user_question})
        # payload = {
        #     "email": user["email"],
        #     "password": hash_password(user["password"]),
        #     "created_at": datetime.utcnow(),
        # }

        # self.database["message"].insert_one(payload)

    # def get_user_by_id(self, user_id: str) -> Optional[dict]:
    #     user = self.database["users"].find_one(
    #         {
    #             "_id": ObjectId(user_id),
    #         }
    #     )
    #     return user

    # def get_user_by_email(self, email: str) -> Optional[dict]:
    #     user = self.database["users"].find_one(
    #         {
    #             "email": email,
    #         }
    #     )
    #     return user
