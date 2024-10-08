import app.dal.sys.user as user_dals

from typing import List
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from app.constant import NORMAL_USER
from app.models.system.role import Role
from app.models.system.user import User
from app.utils.token import hash_password
from ._format import format_user
from sqlalchemy.ext.asyncio import AsyncSession 

async def get_user_list(db: AsyncSession):
    """
    获取用户列表
    """
    try:
        count = await user_dals.get_count(db)
        users = await user_dals.get_user_all(db)
        user_list = []
        for user in users:
            item = format_user(user)
            user_list.append(item)
        data = {"total": count, "list": user_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_user_by_id(db: AsyncSession, id: int):
    """
    根据id获取用户
    """
    try:
        user = await user_dals.get_user_by_id(db, id)
        item = format_user(user)
        return item
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_user(db: AsyncSession, user):
    """
    创建用户
    """
    try:
        db_user = await user_dals.get_user_by_name(db, user.name)
        if db_user and db_user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User exist"
            )

        role_ids = [NORMAL_USER]
        roles = db.query(Role).filter(Role.id.in_(role_ids)).all()

        user_data = user.model_dump(exclude=["roles"])
        user_data["password"] = hash_password(user.password)
        new_user = User(**user_data)
        new_user.roles = roles

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        refresh_new_user = format_user(new_user)

        return refresh_new_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_user_by_id(user_id: int, item, db: AsyncSession):
    """
    根据id更新用户
    """
    user = await user_dals.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not exist"
        )

    for key, value in item.dict(exclude_unset=True).items():
        setattr(user, key, value)

    try:
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        db.rollback()
        raise HTTPException(status_code=400, detail="update failed")


async def delete_users_by_ids(ids: List[int], db: AsyncSession):
    """
    根据ids删除用户
    """
    try:
        data = await user_dals.delete_user(db, ids)
        if data == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return data
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_user_by_id( db: AsyncSession, id: int):
    """
    根据id删除用户
    """
    try:
        data = await user_dals.delete_user_by_id(db, id)
        return data
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e}")
