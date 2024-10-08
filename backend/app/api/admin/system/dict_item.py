from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.response import RM, RMS
import app.services.sys.dict_item as di_services
from app.db.client import get_db
import app.schemas.sys.dictionary_entry as di_schemas
from app.deps.permission import get_user_permissions
import app.constant.permission as permissions

router = APIRouter(prefix="/dict-item", tags=["Dict Item"])


@router.get("/", response_model=RM)
async def get_dict_item(
    dictId: int,
    page: int = 1,
    pageSize: int = 10,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_READ)),
):
    data = await di_services.get_dict_item_list_service(db, dictId, page, pageSize)
    return RMS(data=data)


@router.get("/{id}", response_model=RM)
async def get_dict_item_by_id(
    id: int,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_READ)),
):
    data = await di_services.get_dict_item_by_id_service(db, id)
    return RMS(data=data)


@router.post("/", response_model=RM)
async def create_dict_item(
    dict_item: di_schemas.DictionaryEntryCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_CREATE)),
):
    data = await di_services.create_dict_item_service(db, dict_item)
    return RMS(data=data)


@router.put("/{id}", response_model=RM)
async def update_dict_item_by_id(
    id: int,
    dict_item: di_schemas.DictionaryEntryUpdate,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_UPDATE)),
):
    data = await di_services.update_dict_item_by_id_service(db, id, dict_item)
    return RMS(data=data)


@router.delete("/", response_model=RM)
async def delete_dict_item(
    ids: di_schemas.DictinonaryEntryByIds,
    db: Session = Depends(get_db),
    _: bool = Depends(get_user_permissions(permissions.SYSTEM_DICT_ITEM_DELETE)),
):
    data = await di_services.delete_dict_item_by_ids_service(db, ids)
    return RMS(data=data)
