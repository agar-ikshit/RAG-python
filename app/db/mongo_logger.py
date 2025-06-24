from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "logicspice_chatbot"
COLLECTION_NAME = "conversations"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def log_chat(user_id: str, user_name: str, question: str, answer: str):
    collection.insert_one({
        "user_id": user_id,
        "user_name": user_name,
        "question": question,
        "answer": answer,
        "timestamp": datetime.utcnow()
    })
