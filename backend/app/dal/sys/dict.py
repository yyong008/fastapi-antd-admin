from fastapi import HTTPException
from app.models.system.dictionary import Dictionary
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_dictionary_count(db: AsyncSession):
    count = await base_crud.get_count(db, Dictionary)
    return count


async def get_dictionary_all(db: AsyncSession):
    data = await base_crud.get_all(db, Dictionary)
    return data

async def get_dictionary_by_id(db: AsyncSession, id: int):
    data = await base_crud.get_by_id(db, Dictionary, id)
    return data

async def get_dictionary_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    order_by = Dictionary.created_at.desc()
    filter = None
    data = await base_crud.get_list(
        db=db,
        model=Dictionary,
        order_by=order_by,
        filter=filter,
        options=None,
        page=page,
        pageSize=pageSize,
    )
    return data


async def create_dict(db: AsyncSession, data):
    data = await base_crud.create(db=db, model=Dictionary, obj_in=data)
    return data


async def update_dict_by_id(db: AsyncSession, dict_id: int, dict):
    data = await base_crud.update_by_id(db=db, model=Dictionary, id=dict_id, new_data=dict)
    return data


async def delete_dict_by_ids(db: AsyncSession, ids: list[int]):
    try:
        data = await base_crud.delete_by_ids(db=db, model=Dictionary, ids=ids)
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
