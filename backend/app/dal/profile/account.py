from app.models.system.department import Department
from app.models.system.user import User
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_profile_account_by_name(db: AsyncSession, name: str):
    # return db.query(User).filter(User.name == name).first()
    data = await base_crud.get_by_name(db, User, name)
    return data


async def get_profile_account_by_email(db: AsyncSession, email: str):
    # return db.query(User).filter(User.email == email).first()
    # data = await base_crud.get_by_email(db, User, email)
    pass


async def get_profile_account_by_id(db: AsyncSession, user_id: int):
    pass
    # return (
    #     db.query(User)
    #     .filter_by(id=user_id)
    #     .options(joinedload(User.department).load_only(Department.name))
    #     .first()
    # )
