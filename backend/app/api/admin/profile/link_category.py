from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.profile.link.category import (
    get_link_category_list_service,
    get_link_category_by_id_service,
    create_link_category_service,
    update_link_category_service,
    delete_link_category_by_ids_service,
)
from app.schemas.profile.profile_link_category import (
    LinkCategoryCreate,
    LinkCategoryUpdate,
    LinkCategoryDeleteByIds,
)
from app.utils.current_user import get_current_user

router = APIRouter(prefix="/link/category", tags=["Link Category"])


@router.get("/", response_model=ResponseModel)
def get_link_category(page: int = 1, pageSize: int = 10, db: Session = Depends(get_db)):
    data = get_link_category_list_service(page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_link_category_by_id(id: int, db: Session = Depends(get_db)):
    data = get_link_category_by_id_service(id, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_link_category(
    lc: LinkCategoryCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    lc = lc.model_dump()
    data = create_link_category_service(lc, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_link_category_by_id(
    id: int,
    lc: LinkCategoryUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    lc = lc.model_dump()
    data = update_link_category_service(id, lc, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_link_by_ids_category(
    ids: LinkCategoryDeleteByIds, db: Session = Depends(get_db)
):
    ids = ids.model_dump()
    data = delete_link_category_by_ids_service(ids["ids"], db)
    return ResponseSuccessModel(data=data)
