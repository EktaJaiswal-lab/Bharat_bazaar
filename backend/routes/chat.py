from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ai.chatbot import chatbot_engine

router = APIRouter()

class ChatMessage(BaseModel):
    role: str # "user" or "model"
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    reply: str

@router.post("/", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    try:
        reply = await chatbot_engine.get_response(request.message, request.history)
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
