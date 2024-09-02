from fastapi import HTTPException
from bson import ObjectId
from app.db.database import messages_collection, message_helper
from app.models import Message, MessageInDB

# Create a message
async def create_message(message: Message):
    result = await messages_collection.insert_one(message.dict())
    stored_message = await messages_collection.find_one({"_id": result.inserted_id})
    return message_helper(stored_message)

# Get all the messages
async def get_messages():
    messages = await messages_collection.find().to_list(1000)
    return [message_helper(message) for message in messages]

# Delete a message
async def delete_message(message_id: str):
    try:
        delete_result = await messages_collection.delete_one({"_id": ObjectId(message_id)})
        if delete_result.deleted_count == 1:
            return {"message": "Message deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Message not found")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid message ID")

# Updating a message
async def update_message(message_id: str, new_content: str, sender: str):
    update_result = await messages_collection.update_one(
        {"_id": ObjectId(message_id)},
        {"$set": {"content": new_content, "sender": sender}}
    )

    if update_result.matched_count == 1:
        updated_message = await messages_collection.find_one({"_id": ObjectId(message_id)})
        return message_helper(updated_message)
    else:
        raise HTTPException(status_code=404, detail="Message not found")
