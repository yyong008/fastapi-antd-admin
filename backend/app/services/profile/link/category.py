from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

import app.dal.profile.link.category as lc_dals
from app.services.profile.link._format import format_category
from app.models.profile.link import LinkCategory


async def get_link_category_list_service(db: AsyncSession, current_user_id, page, pageSize):
    """
    获取所有分类
    """
    try:
        count = await lc_dals.get_link_category_count(db, current_user_id)
        categories = await lc_dals.get_link_category_list(db, current_user_id, page, pageSize)

        category_list = []
        for c in categories:
            item = format_category(c)
            category_list.append(item)

        data = {"total": count, "list": category_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_link_category_by_id_service(db: AsyncSession, id):
    """
    根据 id 获取分类
    """
    try:
        data = await lc_dals.get_link_category_by_id(db, id)
        item = format_category(data)
        return item
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_link_category_service(db: AsyncSession, link_category, user_id):
    """
    创建分类
    """
    try:
        lc = LinkCategory(**link_category)
        lc.user_id = user_id
        data = await lc_dals.create_link_category(db, lc)
        return format_category(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_link_category_service(db: AsyncSession, id, link_category, user_id):
    """
    根据 id 更新分类
    """
    try:
        o_data = await lc_dals.get_link_category_by_id(db, id)
        if o_data is None:
            raise HTTPException(status_code=400, detail="Link category not found")

        o_data.name = link_category['name']
        o_data.user_id = user_id
        o_data.description = link_category['description']
        data = await lc_dals.update_link_category_by_id(db, id, o_data)
        return format_category(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_link_category_by_ids_service(db: AsyncSession, ids: list[int]):
    """
    根据 ids 删除分类
    """
    try:
        data = await lc_dals.delete_link_category_by_ids(db, ids)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
