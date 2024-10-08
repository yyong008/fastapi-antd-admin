from app.models.tools.storage import Storage
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_storage_count(db: AsyncSession):
    count = await base_crud.get_count(db, Storage)
    return count


async def get_storage_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    data = await base_crud.get_list(db=db, model=Storage, page=page, pageSize=pageSize)
    return data


async def get_storage_by_id(db: AsyncSession, id):
    return db.query(Storage).filter_by(Storage.id == id).all()


async def create_storage(db: AsyncSession, storage: dict):
    data = await base_crud.create(db=db, model=Storage, obj_in=storage)
    return data

async def update_storage_by_id(db: AsyncSession, storage_id: int, storage: Storage):
    data = await base_crud.update_by_id(db=db, model=Storage, id=storage_id, new_data=storage)
    return data


async def delete_storage_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db=db, model=Storage, ids=ids)
    return data
