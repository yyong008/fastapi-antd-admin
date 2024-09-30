from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import ResponseModel, ResponseSuccessModel
from app.services.profile.link.link import (
    get_link_list_by_id_service,
    create_link_service,
    update_link_by_id_service,
    delete_link_by_ids_service,
)
from app.utils.current_user import get_current_user
from app.schemas.profile.profile_link import LinkCreate, LinkDeleteByIds, LinkUpdate

router = APIRouter(prefix="/link", tags=["Link"])


# @router.get("/", response_model=ResponseModel)
# def get_link(id: int, page: int, pageSize: int, db: Session = Depends(get_db)):
#     data = {}
#     return ResponseSuccessModel(data=data)


@router.get("/{id}", response_model=ResponseModel)
def get_link_by_id(id: int, page: int, pageSize: int, db: Session = Depends(get_db)):
    data = get_link_list_by_id_service(id, page, pageSize, db)
    return ResponseSuccessModel(data=data)


@router.post("/", response_model=ResponseModel)
def create_link(
    link: LinkCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    link = link.model_dump(mode="json")
    data = create_link_service(link, current_user.id, db)
    return ResponseSuccessModel(data=data)


@router.put("/{id}", response_model=ResponseModel)
def update_link_by_id(
    id: int,
    link: LinkUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    link = link.model_dump(mode="json")
    data = update_link_by_id_service(id, link, db)
    return ResponseSuccessModel(data=data)


@router.delete("/", response_model=ResponseModel)
def delete_link_by_ids(ids: LinkDeleteByIds, db: Session = Depends(get_db)):
    ids = ids.model_dump(mode="json")
    data = delete_link_by_ids_service(ids['ids'], db)
    return ResponseSuccessModel(data=data)
