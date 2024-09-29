from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.db.client import get_db
from app.services.blog.blog import (
    get_blog_by_id_service,
    get_blog_list_service,
    create_blog_service,
    update_blog_service,
    delete_blog_by_ids_service,
)
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.schemas.blog.blog import BlogCreate, BlogUpdate, BlogDeleteByIds
from app.utils.current_user import get_current_user

router = APIRouter(tags=["Admin Blog Main"])


@router.get("/{id}", response_model=ResponseModel)
def get_blog_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    data = get_blog_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.get("/", response_model=ResponseModel)
def get_blogs(
    page: int = Query(1, description="当前页码"),
    pageSize: int = Query(10, description="每页条数"),
    categoryId: Optional[int] = Query(None, description="按分类 ID 搜索"),
    tagId: Optional[int] = Query(None, description="按标签 ID 搜索"),
    db: Session = Depends(get_db),
):
    data = get_blog_list_service(categoryId, tagId, page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_blog(blog: BlogCreate, current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    blog = blog.model_dump()
    data = create_blog_service(blog, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog(id: int, blog: BlogUpdate, current_user=Depends(get_current_user),  db: Session = Depends(get_db)):
    blog = blog.model_dump()
    data = update_blog_service(id, current_user.id, blog, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_by_ids(ids: BlogDeleteByIds, db: Session = Depends(get_db)):
    data = delete_blog_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
