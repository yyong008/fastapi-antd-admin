from fastapi import HTTPException
from app.models.docs.changelog import ChangeLog
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_changelog_count(db: AsyncSession):
    count = await base_crud.get_count(db, ChangeLog)
    return count


async def get_changelog_all(db: AsyncSession):
    sort_column = ChangeLog.createdAt.desc()
    return db.query(ChangeLog).order_by(sort_column).all()

async def get_changelog_by_id(id: int, db: AsyncSession):
    return db.query(ChangeLog).filter(ChangeLog.id == id).first()

async def get_changelog_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    # limit = pageSize
    # offset = (page - 1) * pageSize
    # sort_column = ChangeLog.createdAt.desc()
    data = await base_crud.get_list(db, ChangeLog, page=page, pageSize=pageSize)
    return data

async def create_changelog(db: AsyncSession, changelog):
    db.add(changelog)
    db.commit()
    db.refresh(changelog)
    return changelog

async def update_changelog_by_id(db: AsyncSession, changelog_id: int, changelog):
    # db.query(ChangeLog).filter(ChangeLog.id == changelog_id).update(changelog)
    db.commit()
    db.refresh(changelog)
    return changelog

async def delete_changelog_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = db.query(ChangeLog).filter(ChangeLog.id.in_(ids)).delete(synchronize_session=False)
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
