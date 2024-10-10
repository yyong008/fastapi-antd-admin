from sqlalchemy import select
from app.models.system.department import Department
from app.models.system.user import User
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_user_by_name(db: AsyncSession, name: str):
    data = await base_crud.get_by_name(db, User, name)
    return data


async def get_user_by_email(email: str, db: AsyncSession):
    # return db.query(User).filter(User.email == email).first()
    data = await base_crud.get_by_email(db, User, email)
    return data


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


async def get_count(db: AsyncSession):
    count = await base_crud.get_count(db, User)
    return count


async def get_user_all(db: AsyncSession):
    order_by = User.created_at.desc()
    options = [
        selectinload(User.department).load_only(Department.name),
        selectinload(User.roles),
    ]
    data = await base_crud.get_all(
        db=db, model=User, order_by=order_by, options=options
    )
    return data


async def get_user_by_id(db: AsyncSession, user_id):
    query = (
        select(User)
        .filter(User.id == user_id)
        .options(
            selectinload(User.department).load_only(Department.name),
            selectinload(User.roles),
        )
    )
    result = await db.execute(query)

    user = result.scalars().first()
    return user


async def get_users_by_ids(ids, db: AsyncSession):
    return db.query(User).filter(User.id.in_(ids)).all()


# =====================================CREATE===================================================
async def create_user(db: AsyncSession, name: str, email: str, hashed_password: str):
    obj_in = {"name": name, "email": email, "hashed_password": hashed_password}
    data = await base_crud.create(db, User, obj_in=obj_in)
    return data


# =====================================DELETE===================================================
async def delete_user_by_id(db: AsyncSession, user_id: int):
    data = await base_crud.delete_by_id(db, User, user_id)
    return data

async def delete_users_by_ids(db: AsyncSession, ids: list[int]):
    data = await base_crud.delete_by_ids(db, User, ids)
    return data
