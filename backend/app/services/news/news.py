from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession 

import app.dal.news.news as news_dals
import app.services.news._format as f_n
from app.utils.bleach import clean_html


async def get_news_list_service(
    db: AsyncSession,
    category_id: int,
    page: int,
    pageSize: int,
):
    """
    更具 category_id 获取新闻列表
    """
    try:
        count = await news_dals.get_news_count_by_category_id(db, category_id)
        news = await news_dals.get_news_list(db, page, pageSize, category_id)

        news_list = [f_n.format_news(n) for n in news]
        data = {"total": count, "list": news_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_client_news_list_service(db: AsyncSession, page: int, pageSize: int):
    """
    获取客户端新闻列表
    """
    category_id = 1
    try:
        total = await news_dals.get_news_count_by_category_id(db, category_id)
        news = await news_dals.get_news_list(db, page, pageSize, category_id)

        news_list = [f_n.format_news(n) for n in news]
        data = {"total": total, "list": news_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_news_by_id_service(db: AsyncSession, id: int, is_client: bool = False):
    """
    根据获取新闻详情
    """
    try:
        news = await news_dals.get_news_by_id(db, id)
        if is_client:
            news.viewCount = news.viewCount + 1
            await db.commit()
            await db.refresh(news)
        data = f_n.format_news_by_id(news)
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_news_service(db: AsyncSession, news: dict, current_user_id: int):
    """
    创建新闻
    """
    try:
        format_news_data = f_n.format_news_from_old_news(current_user_id, news)
        format_news_data["content"] = clean_html(format_news_data["content"])
        data = await news_dals.create_news(db, format_news_data)
        return f_n.format_news(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")


async def update_news_service(
    db: AsyncSession, id: int, news: dict, current_user_id: int
):
    """
    更新新闻
    """
    try:
        format_news_data = f_n.format_news_from_old_news(current_user_id, news)
        count = await news_dals.update_news(db, id, format_news_data, current_user_id)
        if count == 0:
            raise HTTPException(status_code=400, detail="Update failed")
        data = await news_dals.get_news_by_id(db, id)
        return f_n.format_news(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_news_by_ids_service(db: AsyncSession, ids: list[int]):
    """
    根据id删除新闻
    """
    try:
        count = await news_dals.delete_news_by_ids(db, ids)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
