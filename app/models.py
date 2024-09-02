from pydantic import BaseModel

class Message(BaseModel):
    content: str
    sender: str  # "user" or "chatbot"

class MessageInDB(Message):
    id: str
