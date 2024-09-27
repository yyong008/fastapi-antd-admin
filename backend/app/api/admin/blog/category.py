from typing import List
from fastapi import APIRouter, Depends

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.blog.blog_category import (
    get_blog_category_list_service,
    get_blog_category_by_id_service,
    create_blog_category_service,
    delete_blog_category_by_ids_service,
)

router = APIRouter(prefix="/category", tags=["Admin Blog Category"])


@router.get("/", response_model=ResponseModel)
def get_blog_category(page: int, pageSize: int, db=Depends(get_db)):
    data = get_blog_category_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_blog_category_by_id(id: int):
    data = get_blog_category_by_id_service(id)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_blog_category(blog_category: dict):
    data = create_blog_category_service(blog_category)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog_category_by_id(id: int, blog_category: dict):
    data = update_blog_category_by_id(id, blog_category)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_category(ids: List[int]):
    data = delete_blog_category_by_ids_service(ids)
    return ResponseSuccessModel(data=data)
