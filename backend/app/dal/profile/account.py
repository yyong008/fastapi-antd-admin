# from app.models.system.department import Department
from app.models.system.user import User
# from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_profile_account_by_name(db: AsyncSession, name: str):
    data = await base_crud.get_by_name(db, User, name)
    return data


async def get_profile_account_by_email(db: AsyncSession, email: str):
    data = await base_crud.get_by_email(db, User, email)
    return data


async def get_profile_account_by_id(db: AsyncSession, id: int):
    data = await base_crud.get_by_id(db, User, id)
    return data
