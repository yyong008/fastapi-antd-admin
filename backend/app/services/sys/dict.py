from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.dict import delete_dict_by_ids, get_dictionary_count, get_dictionary_list, create_dict, update_dict_by_id
from app.services.sys.format import format_dict
from app.models.system.dictionary import Dictionary
from app.schemas.sys.dictionary import DictionaryCreate, DictionaryUpdate


async def get_dict_lists_service(page, pageSize, db: Session):
    try:
        count = await get_dictionary_count(db)
        users = await get_dictionary_list(db, page, pageSize)

        dict_list = []
        for user in users:
            item = format_dict(user)
            dict_list.append(item)

        data = {"total": count, "list": dict_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_dict_by_id_service():
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def create_dict_service(dt: DictionaryCreate, db):
    try:
        dt = dt.model_dump()
        dt = Dictionary(**dt)
        data = await create_dict(dt, db)
        return format_dict(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def update_dict_by_id_service(id, dt: DictionaryUpdate, db):
    try:
        dt = dt.model_dump(exclude_unset=True)
        data = await update_dict_by_id(db, id, dt)
        return format_dict(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def delete_dict_by_ids_service(ids, db):
    try:
        count = await delete_dict_by_ids(ids, db)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
