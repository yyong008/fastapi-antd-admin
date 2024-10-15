from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

import app.dal.profile.link.link as lk_dals 
from app.services.profile.link._format import format_link
from app.models.profile.link import Link


async def get_link_list_by_id_service(db: AsyncSession, category_id: int, current_user_id: int, page: int, pageSize: int):
    """
    根据 category_id 获取链接列表
    """
    try:
        count = await lk_dals.get_link_count_by_category_id(db, category_id, current_user_id)
        links = await lk_dals.get_links_by_category_id(db, category_id, current_user_id,page, pageSize)

        link_list = [format_link(link) for link in links]

        data = {"total": count, "list": link_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_link_list_by_ids_service(db: AsyncSession, ids):
    """
    根据 ids 获取链接列表
    """
    try:
        links = await lk_dals.get_links_by_category_id(db, ids)
        return links
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")


async def update_link_by_id_service(db: AsyncSession, id: int, link):
    """
    根据 id 更新链接
    """
    try:
        o_data = await lk_dals.get_link_by_id(db, id)
        if not o_data:
            raise HTTPException(status_code=400, detail="Oops, we encountered an error")
        o_data.name = link["name"]
        o_data.url = link["url"]
        o_data.category_id = link["category_id"]
        data = await lk_dals.update_link_by_id(db, id, o_data)
        return format_link(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")


async def delete_link_by_ids_service(db: AsyncSession, ids: list[int]):
    """
    根据 ids 删除链接
    """
    try:
        data = await lk_dals.delete_link_by_ids(db, ids)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")


async def create_link_service(db: AsyncSession,link,):
    """
    创建链接
    """
    try:
        del link['user_id']
        lk = Link(**link)
        data = await lk_dals.create_link_category(db, lk)
        return format_link(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail="Oops, we encountered an error")
