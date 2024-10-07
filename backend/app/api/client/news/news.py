from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db
import app.services.news.news as nns 

router = APIRouter(tags=["Client News"])


@router.get("/{id}")
async def get_news_by_id(id: int, db =Depends(get_db)):
    data = await nns.get_news_by_id_service(db, id)
    return ResponseSuccessModel(data=data)


@router.get("/", response_model=ResponseModel)
async def get_news(page: int = 1, pageSize: int = 10, db: AsyncSession = Depends(get_db)):
    data = await nns.get_client_news_list_service(db, page, pageSize)
    return ResponseSuccessModel(data=data)
