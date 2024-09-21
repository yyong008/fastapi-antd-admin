from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.services.news.news_category import get_news_category_list_service
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.news.news_category import NewsCategoryCreate

router = APIRouter(prefix="/category", tags=["News Category"])


@router.get("/", response_model=ResponseModel)
def get_news_category(page: int, pageSize: int, db: Session=Depends(get_db)):
    data = get_news_category_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_news_category_by_id():
    return {"success": "ok"}


@router.post("/")
def create_news_category(category):
    return {"success": "ok"}


@router.put("/{id}")
def update_news_category_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_news_category():
    return {"success": "ok"}
