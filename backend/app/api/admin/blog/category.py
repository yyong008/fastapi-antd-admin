from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.blog.blog_category import (
    get_blog_category_list_service,
    get_blog_category_by_id_service,
    create_blog_category_service,
    delete_blog_category_by_ids_service,
)
from app.schemas.blog.blog_category import (
    BlogCategoryCreate,
    BlogCategoryDeleteByIds,
    BlogCategoryUpdate,
)

router = APIRouter(prefix="/category", tags=["Admin Blog Category"])


@router.get("/", response_model=ResponseModel)
def get_blog_category(page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_blog_category_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_blog_category_by_id(id: int, db: Session = Depends(get_db)):
    data = get_blog_category_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_blog_category(
    blog_category: BlogCategoryCreate, db: Session = Depends(get_db)
):
    data = create_blog_category_service(blog_category, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_blog_category_by_id(
    id: int, blog_category: BlogCategoryUpdate, db: Session = Depends(get_db)
):
    data = update_blog_category_by_id(id, blog_category, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_blog_category(ids: BlogCategoryDeleteByIds, db: Session = Depends(get_db)):
    data = delete_blog_category_by_ids_service(ids, db)
    return ResponseSuccessModel(data=data)
