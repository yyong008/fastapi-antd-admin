from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import StreamingResponse
from app.services.chat.langchain_service import create_chat_service

from app.schemas.chat.chat import ChatIn

router = APIRouter(prefix="/langchain")

@router.post("/chat")
async def chat(chatIn: ChatIn, background_tasks: BackgroundTasks):
    return StreamingResponse(
         create_chat_service(chatIn, background_tasks),
        media_type="text/event-stream",
    )
