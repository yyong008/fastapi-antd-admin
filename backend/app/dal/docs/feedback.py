from fastapi import HTTPException
from app.models.docs.feedback import FeedBack
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_feedback_count(db: AsyncSession):
    count = await base_crud.get_count(db, FeedBack)
    return count


async def get_feedback_all(db: AsyncSession):
    sort_column = FeedBack.createdAt.desc()
    return db.query(FeedBack).order_by(sort_column).all()


async def get_feedback_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    data = await base_crud.get_list(
        db=db,
        model=FeedBack,
        order_by=None,
        filter=None,
        options=None,
        page=page,
        pageSize=pageSize,
    )
    return data


async def get_feedback_by_id(db: AsyncSession, id: int):
    return db.query(FeedBack).filter(FeedBack.id == id).first()


async def create_feedback(db: AsyncSession, feedback):
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback


async def update_feedback_by_id(db: AsyncSession, blog_id: int, feedback: FeedBack):
    db.query(FeedBack).filter(FeedBack.id == blog_id).update(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback


async def delete_feedback_by_ids(db: AsyncSession, ids: list[int]):
    try:
        count = (
            db.query(FeedBack)
            .filter(FeedBack.id.in_(ids))
            .delete(synchronize_session=False)
        )

        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
