import uuid
import asyncio

from fastapi import APIRouter, BackgroundTasks
from app.utils.message import format_messages

from .langchain_chat_stream import yield_string


from app.config.config import get_settings
from app.utils.model import create_model

api_key = get_settings().api_key

router = APIRouter()


async def create_chat_service(chatIn, background_tasks: BackgroundTasks):
    llm = create_model(model_name="")
    msg = format_messages(chatIn.messages)
    gsn = llm.astream(msg)

    chat_id: None | str = None
    async for chunk in gsn:
        if not chat_id:
            chat_id = str(uuid.uuid4())
        ys = yield_string(chat_id=chat_id, content=chunk.content, role="assistant")
        yield ys.encode('utf-8')
