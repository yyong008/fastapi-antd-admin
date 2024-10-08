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
    data = await base_crud.create(db=db, model=FeedBack, data=feedback)
    return data


async def update_feedback_by_id(db: AsyncSession, blog_id: int, feedback: FeedBack):
    data = await base_crud.update_by_id(
        db=db, model=FeedBack, id=blog_id, data=feedback
    )
    return data


async def delete_feedback_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db=db, model=FeedBack, ids=ids)
    return data
