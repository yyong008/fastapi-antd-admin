from fastapi import HTTPException

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


async def create_storage(db: AsyncSession, storage):
    db.add(storage)
    db.commit()
    db.refresh(storage)
    return storage


async def update_storage_by_id(db: AsyncSession, storage_id: int, storage: Storage):
    db.query(Storage).filter(Storage.id == storage_id).update(storage)
    db.commit()
    db.refresh(storage)
    return storage


async def delete_storage_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Storage)
            .filter(Storage.id.in_(ids))
            .delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
