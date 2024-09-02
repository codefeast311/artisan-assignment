from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = "chatdb"
COLLECTION_NAME = "messages"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]
messages_collection = db[COLLECTION_NAME]

# Helper function to convert MongoDB document to dict with a string ID
def message_helper(message) -> dict:
    return {
        "id": str(message["_id"]),
        "content": message["content"],
        "sender": message["sender"],
    }
