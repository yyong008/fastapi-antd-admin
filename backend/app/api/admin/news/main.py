from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db
from app.services.news.news import get_news_list_service

router = APIRouter(tags=["News Main"])


@router.get("/{id}")
def get_news_by_id():
    return {"success": "ok"}


@router.get("/", response_model=ResponseModel)
def get_news(category_id: int, page: int, pageSize: int, db: Session=Depends(get_db)):
    data = get_news_list_service(category_id, page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/")
def create_news():
    return {"success": "ok"}


@router.put("/{id}")
def update_news():
    return {"success": "ok"}


@router.delete("/")
def delete_news_by_ids():
    return {"success": "ok"}
