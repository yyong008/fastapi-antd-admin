from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

import app.dal.blog.blog_tag as bt_dals
from ._format import format_blog_tag
from app.models.blog import BlogTag


async def get_blog_tag_list_service(db: AsyncSession, page: int, pageSize: int):
    """
    获取博客标签列表
    """
    try:
        count = await bt_dals.get_blog_tag_count(db)
        blog_tag = await bt_dals.get_blog_tag_list(db, page, pageSize)
        blog_tag_list = [format_blog_tag(blog_tag) for blog_tag in blog_tag]

        data = {"total": count, "list": blog_tag_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_blog_tag_by_id_service(db: AsyncSession, id: int, bt, current_user_id: int):
    """
    更新博客标签
    """
    try:
        bc_in_db = await bt_dals.get_blog_tag_by_id(db, id)
        if bc_in_db is None:
            raise HTTPException(status_code=400, detail="Tag not found")
        bc_in_db.description = bt["description"]
        bc_in_db.name = bt["name"]
        bc_in_db.user_id = current_user_id
        data = await bt_dals.update_blog_tag_by_id(db, id, bc_in_db)
        return format_blog_tag(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_blog_tag_service(db: AsyncSession, bt, current_user_id):
    """
    创建博客标签
    """
    try:
        bt["user_id"] = current_user_id
        bt = BlogTag(**bt)
        data = await bt_dals.create_blog_tag(db, bt)
        return format_blog_tag(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_blog_tag_by_ids_service(db: AsyncSession, ids: list[int]):
    """
    根据 ids 删除博客标签
    """
    try:
        data = await bt_dals.delete_blog_tag_by_ids(db, ids)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
