from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.client import get_db
from app.schemas.response import RM, RMS
import app.schemas.sys.dictionary as d_schemas
import app.services.sys.dict as d_services
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/dict", tags=["Dict"])


@router.get("/", response_model=RM)
async def get_dict(
    page: int = 1,
    pageSize: int = 10,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_READ)),
):
    data = await d_services.get_dict_lists_service(db, page, pageSize)
    return RMS(data=data)


@router.get("/{id}")
async def get_dict_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_READ)),
):
    data = await d_services.get_dict_by_id_service(db, id)
    return RMS(data=data)


@router.post("/")
async def create_dict(
    dict: d_schemas.DictionaryCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_CREATE)),
):
    data = await d_services.create_dict_service(db, dict)
    return RMS(data=data)


@router.put("/{id}")
async def update_dict_by_id(
    id: int,
    dict: d_schemas.DictionaryUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_UPDATE)),
):
    data = await d_services.update_dict_by_id_service(db, id, dict)
    return RMS(data=data)


@router.delete("/")
async def delete_dict(
    ids: d_schemas.DictionaryDeleteByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_DELETE)),
):
    data = await d_services.delete_dict_by_ids_service(db, ids.ids)
    return RMS(data=data)
