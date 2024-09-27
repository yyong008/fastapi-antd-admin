from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.blog.blog_tag import get_blog_tag_list_service
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db

router = APIRouter(prefix="/tag", tags=["Admin Blog Category Tag"])


@router.get("/", response_model=ResponseModel)
def get_blog_tag(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_blog_tag_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_blog_tag_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_blog_tag():
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog_tag_by_id():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_tag():
    data = {}
    return ResponseSuccessModel(data=data)
