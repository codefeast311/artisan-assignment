from fastapi import APIRouter, Body
from typing import List
from app.models import Message, MessageInDB
from app.controllers.message_controller import create_message, get_messages, delete_message, update_message

router = APIRouter()

# POST request to create a message
@router.post("/messages/", response_model=MessageInDB)
async def create_message_endpoint(message: Message):
    return await create_message(message)

# GET request to get all the stored messages
@router.get("/messages/", response_model=List[MessageInDB])
async def get_messages_endpoint():
    return await get_messages()

# DELETE request to delete a message
@router.delete("/messages/{message_id}", response_model=dict)
async def delete_message_endpoint(message_id: str):
    return await delete_message(message_id)

# PUT request to update a message
@router.put("/messages/{message_id}", response_model=MessageInDB)
async def update_message_endpoint(message_id: str, new_content: str = Body(...), sender: str = Body(...)):
    return await update_message(message_id, new_content, sender)
