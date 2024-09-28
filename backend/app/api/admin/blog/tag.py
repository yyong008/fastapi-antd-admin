from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.blog.blog_tag import get_blog_tag_list_service
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.db.client import get_db
from app.schemas.blog.blog_tag import BlogTagCreate, BlogTagDeleteByIds, BlogTagUpdate
from app.services.blog.blog_tag import (
    create_blog_tag_service,
    update_blog_tag_service,
    delete_blog_tag_by_ids_service,
)

router = APIRouter(prefix="/tag", tags=["Admin Blog Category Tag"])


@router.get("/", response_model=ResponseModel)
def get_blog_tag(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_blog_tag_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_blog_tag_by_id(id: int, db: Session = Depends(get_db)):
    data = get_blog_tag_by_id(id)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_blog_tag(blog_tag: BlogTagCreate, db: Session = Depends(get_db)):
    data = create_blog_tag_service(blog_tag, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog_tag_by_id(
    id: int, blog_tag: BlogTagUpdate, db: Session = Depends(get_db)
):
    data = update_blog_tag_service(id, blog_tag, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_tag(ids: BlogTagDeleteByIds, db: Session = Depends(get_db)):
    data = delete_blog_tag_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
