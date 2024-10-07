from app.models.system.loginlog import Loginlog
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_count(db: AsyncSession):
    count = await base_crud.get_count(db, Loginlog)
    return count


async def get_Loginlog_by_name(db: AsyncSession, name: str):
    return db.query(Loginlog).filter(Loginlog.name == name).first()


async def get_Loginlog_by_email(db: AsyncSession, email: str):
    return db.query(Loginlog).filter(Loginlog.email == email).first()


async def get_Loginlog_by_id(db: AsyncSession, id: int):
    return db.query(Loginlog).filter(Loginlog.id == id).first()


async def get_Loginlog_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    order_by = Loginlog.login_at.asc()
    data = await base_crud.get_list(db, Loginlog, order_by=order_by, page=page, pageSize=pageSize)
    return data


async def get_loginlog_latest_by_user_id(db, user_id):
    data = await base_crud.get_by_id(db, Loginlog, user_id)
    return data

# =====================================CREATE===================================================
async def create_loginlog(
    db: AsyncSession,
    log,
):
    loginlog_ins = await base_crud.create(db=db, model=Loginlog, obj_in=log)
    return loginlog_ins


# =====================================DELETE===================================================
async def delete_Loginlog(
    db: AsyncSession,
    loginlog_id: int,
):
    loginlog = db.query(Loginlog).filter(Loginlog.id == loginlog_id).first()
    if loginlog:
        db.delete(loginlog)
        db.commit()
        return Loginlog
    return None
