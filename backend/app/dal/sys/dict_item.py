from fastapi import HTTPException
from app.models.system.dictionary import DictionaryEntry
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_dictionary_entry_count(id, db: AsyncSession):
    filter = DictionaryEntry.dictionary_id == id
    count = await base_crud.get_count(db, DictionaryEntry, filter=filter)
    return count


async def get_dictionary_entry_all(db: AsyncSession):
    order_by = DictionaryEntry.createdAt.desc()
    data = await base_crud.get_all(db, DictionaryEntry, order_by)
    return data


async def get_dictionary_entry_list(db: AsyncSession, id, page: int = 1, pageSize: int = 10):
    order_by = DictionaryEntry.createdAt.desc()
    filter = DictionaryEntry.dictionary_id == id
    data = await base_crud.get_list(db, DictionaryEntry, order_by, filter, page, pageSize)
    return data

async def create_dict_item(db: AsyncSession, dict_item):
    db.add(dict_item)
    db.commit()
    db.refresh(dict_item)
    return dict_item

async def update_dict_item_by_id(db: AsyncSession, dict_item_id: int, dict_item):
    db.query(DictionaryEntry).filter(DictionaryEntry.id == dict_item_id).update({**dict_item}, synchronize_session=False)
    db.commit()
    dict_item = db.query(DictionaryEntry).filter(DictionaryEntry.id == dict_item_id).first()
    db.refresh(dict_item)
    return dict_item

async def delete_dict_item_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(DictionaryEntry).filter(DictionaryEntry.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

