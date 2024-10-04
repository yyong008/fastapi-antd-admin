from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.dict_item import (
    get_dictionary_entry_count,
    get_dictionary_entry_list,
    create_dict_item,
    update_dict_item_by_id,
)
from app.services.sys.format import format_dict_item
from app.models.system.dictionary import DictionaryEntry


async def get_dict_item_list_service(id, page, pageSize, db: Session):
    try:
        count = await get_dictionary_entry_count(id, db)
        users = await get_dictionary_entry_list(id, db, page, pageSize)

        dict_item_list = []
        for user in users:
            item = format_dict_item(user)
            dict_item_list.append(item)

        data = {"total": count, "list": dict_item_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_dict_item_by_id_service(id, db: Session):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_dict_item_service(dict_item, db):
    try:
        data = DictionaryEntry(**dict_item.model_dump())
        di = create_dict_item(data, db)
        return format_dict_item(di)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_dict_item_by_id_service(id, dict_item, db):
    try:
        dt = dict_item.model_dump(exclude_unset=True)
        di = await update_dict_item_by_id(db, id, dt)
        return format_dict_item(di)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_dict_item_by_ids_service():
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
