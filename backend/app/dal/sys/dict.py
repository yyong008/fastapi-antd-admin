from fastapi import HTTPException
from app.models.system.dictionary import Dictionary
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_dictionary_count(db: AsyncSession):
    count = await base_crud.get_count(db, Dictionary)
    return count


async def get_dictionary_all(db: AsyncSession):
    sort_column = Dictionary.createdAt.desc()
    return db.query(Dictionary).order_by(sort_column).all()


async def get_dictionary_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    order_by = Dictionary.createdAt.desc()
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


async def create_dict(db: AsyncSession, dict):
    db.add(dict)
    db.commit()
    db.refresh(dict)
    return dict


async def update_dict_by_id(db: AsyncSession, dict_id: int, dict):
    db.query(Dictionary).filter(Dictionary.id == dict_id).update(
        {**dict}, synchronize_session=False
    )
    db.commit()
    dict = db.query(Dictionary).filter(Dictionary.id == dict_id).first()
    db.refresh(dict)
    return dict


async def delete_dict_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(Dictionary)
            .filter(Dictionary.id.in_(ids))
            .delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
