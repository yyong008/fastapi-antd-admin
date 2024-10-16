from app.models.docs.changelog import ChangeLog
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_changelog_count(db: AsyncSession):
    count = await base_crud.get_count(db, ChangeLog)
    return count


async def get_changelog_all(db: AsyncSession):
    sort_column = ChangeLog.created_at.desc()
    return db.query(ChangeLog).order_by(sort_column).all()


async def get_changelog_by_id(id: int, db: AsyncSession):
    return db.query(ChangeLog).filter(ChangeLog.id == id).first()


async def get_changelog_list(
    db: AsyncSession,
    order_by=None,
    filter=None,
    options=None,
    page: int = 1,
    pageSize: int = 10,
):
    data = await base_crud.get_list(
        db=db,
        model=ChangeLog,
        order_by=order_by,
        filter=filter,
        options=options,
        page=page,
        pageSize=pageSize,
    )
    return data


async def create_changelog(db: AsyncSession, changelog):
    data = await base_crud.create(db=db, obj_in=changelog)
    return data


async def update_changelog_by_id(db: AsyncSession, changelog_id: int, changelog):
    data = await base_crud.update_by_id(
        db=db, model=ChangeLog, id=changelog_id, new_data=changelog
    )
    return data


async def delete_changelog_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db=db, model=ChangeLog, ids=ids)
    return data
