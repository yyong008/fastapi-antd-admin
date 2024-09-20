from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db
from app.services.news.news import get_client_news_list_service, get_news_by_id_service

router = APIRouter(tags=["Client News"])


@router.get("/{id}")
def get_news_by_id(id: int, db: Session=Depends(get_db)):
    data = get_news_by_id_service(id,db)
    return ResponseSuccessModel(data=data)


@router.get("/", response_model=ResponseModel)
def get_news(page: int, pageSize: int, db: Session=Depends(get_db)):
    data = get_client_news_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)
