from fastapi import APIRouter, Depends

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.blog.blog_category import get_blog_category_list_service

router = APIRouter(prefix="/category", tags=["Admin Blog Category"])


@router.get("/", response_model=ResponseModel)
def get_blog_category(page: int, pageSize: int, db = Depends(get_db)):
    data = get_blog_category_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}")
def get_blog_category_by_id():
    return {"success": "ok"}


@router.post("/")
def create_blog_category():
    return {"success": "ok"}


@router.put("/{id}")
def update_blog_category_by_id():
    return {"success": "ok"}


@router.delete("/")
def delete_blog_category():
    return {"success": "ok"}
