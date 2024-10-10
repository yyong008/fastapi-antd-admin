from app.models.system.user import UserSignLog
from app.utils.time import get_today_time
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_count(db: AsyncSession):
    count = await base_crud.get_count(db, UserSignLog)
    return count


async def get_user_signlog_all(db: AsyncSession):
    sort_column = UserSignLog.created_at.desc()
    data = await base_crud.get_all(db, UserSignLog, sort_column)
    return data


async def get_user_signlog_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    order_by = UserSignLog.created_at.desc()
    data = await base_crud.get_list(db, UserSignLog, order_by, page, pageSize)
    return data


async def get_user_today_is_sign_in_by_id(db: AsyncSession, user_id):
    start_time, end_time = get_today_time()
    result = select(UserSignLog).where(
            UserSignLog.userId == user_id,
            UserSignLog.sign_time >= start_time,
            UserSignLog.sign_time < end_time,
        )
    res = await db.execute(result)
    data = res.scalars().first()
    return data


async def get_signin_log_latest_by_user_id(db: AsyncSession, user_id: int):
    filter = UserSignLog.userId == user_id
    return await base_crud.get_by_filters(db, UserSignLog, filter)

# =====================================CREATE===================================================
async def create_user_signlog(db: AsyncSession, sign_log):
    data = await base_crud.create(db, UserSignLog, sign_log)
    return data
