from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.db.client import get_db
from app.services.blog.blog import get_blog_by_id_service, get_blog_list_service
from app.schemas.response import ResponseModel, ResponseSuccessModel

router = APIRouter(tags=["Admin Blog Main"])


@router.get("/{id}", response_model=ResponseModel)
def get_blog_by_id(id: int,  db: Session = Depends(get_db),):
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
def create_blog(blog):
    data = {}
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog():
    data = {}
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_by_ids():
    data = {}
    return ResponseSuccessModel(data=data)
