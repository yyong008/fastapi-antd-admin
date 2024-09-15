import app.dal.sys.user as user_dal

from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.constant import NORMAL_USER
from app.models.system.role import Role
from app.models.system.user import User
from app.schemas.sys.user import UserCreate
from app.dal.blog.blog_tag import get_blog_tag_count, get_blog_tag_list

def format_blog_tag(blog_tag):
    item = {
        "id": blog_tag.id,
        "name": blog_tag.name,
        "description": blog_tag.description,
    }
    return item


def get_blog_tag_list_service(page, pageSize, db: Session):
    try:
        count = get_blog_tag_count(db)
        blog_tag = get_blog_tag_list(db, page, pageSize)

        blog_tag_list = []
        for tag in blog_tag:
            item = format_blog_tag(tag)
            blog_tag_list.append(item)

        data = {"total": count, "list": blog_tag_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def get_user_by_id(user_id: int, db):
    try:
        user = user_dal.get_user_by_id(user_id, db)
        item = format_blog_tag(user)
        return item
    except Exception as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_user(user: UserCreate, db: Session):
    try:
        db_user = user_dal.get_user_by_name(user.name)
        if db_user and db_user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User exist"
            )

        role_ids = [NORMAL_USER]
        roles = db.query(Role).filter(Role.id.in_(role_ids)).all()
        new_user = User(name=user.name, password=user.password, roles=roles)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        refresh_new_user = format_blog_tag(new_user)

        return refresh_new_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e}")


def update_user_by_id(user_id: int, item, db: Session):
    user = user_dal.get_user_by_id(user_id)
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


def delete_users_by_ids(ids: List[int], db: Session):
    try:
        # 查询要删除的用户
        users = user_dal.get_users_by_ids(ids)

        if not users:
            raise HTTPException(
                status_code=404, detail="No users found for the given IDs"
            )

        # 遍历删除用户
        for user in users:
            db.delete(user)

        db.commit()
        return {}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_user_by_id(user_id: int, db: Session):
    try:
        user = user_dal.get_user_by_id(user_id, db)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        db.delete(user)
        db.commit()

        return user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{e}")
