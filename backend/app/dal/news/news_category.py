from typing import Any, Dict
from app.models.news import NewsCategory
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud

# =====================================GET===================================================
async def get_news_category_count(db: AsyncSession):
    """

    获取新闻分类数量

    Args:
        db (AsyncSession): 数据库连接

    Returns:    
        int: 新闻分类数量
                """
    count = await base_crud.get_count(db, NewsCategory)
    return count


async def get_news_category_all(db: AsyncSession):
    """

    获取所有新闻分类

    Args:
        db (AsyncSession): 数据库连接

    Returns:
        list[NewsCategory]: 所有新闻分类
    """
    sort_column = NewsCategory.created_at.desc()
    data = await base_crud.get_all(db, NewsCategory, order_by=sort_column)
    return data


async def get_news_category_list(db: AsyncSession, page: int = 1, pageSize: int = 10):
    """

    获取新闻分类列表

    Args:
        db (AsyncSession): 数据库连接
        page (int, optional): 页码. Defaults to 1.
        pageSize (int, optional): 每页数量. Defaults to 10.

    Returns:
        list[NewsCategory]: 新闻分类列表

    """
    data = await base_crud.get_list(db, NewsCategory, page=page, pageSize=pageSize)
    return data

async def get_news_category_by_name(db: AsyncSession, name: str):
    """
    获取新闻分类

    Args:
        db (AsyncSession): 数据库连接
        name (str): 新闻分类名称

    Returns:
        NewsCategory: 新闻分类
    """
    data = await base_crud.get_by_name(db, NewsCategory, name)
    return data

async def get_news_category_by_id(db: AsyncSession, id: int):
    """
    获取新闻分类

    Args:
        db (AsyncSession): 数据库连接
        id (int): 新闻分类id

    Returns:
        NewsCategory: 新闻分类
    """
    data = await base_crud.get_by_id(db, NewsCategory, id)
    return data


async def create_news_category(db: AsyncSession, news_category):
    """
    创建新闻分类

    Args:
        db (AsyncSession): 数据库连接
        news_category (NewsCategory): 新闻分类

    Returns: 
        NewsCategory: 创建后的新闻分类
    """
    data = await base_crud.create(db, NewsCategory, news_category)
    return data

async def update_news_category_by_id(db: AsyncSession, news_category_id: int, news_category: Dict[str, Any]):
    """
    更新新闻分类

    Args:
        db (AsyncSession): 数据库连接
        news_category_id (int): 新闻分类id
        news_category (NewsCategory): 新闻分类

    Returns:
        NewsCategory: 更新后的新闻分类
    """
    data = await base_crud.update_by_id(db, NewsCategory, news_category_id, news_category)
    return data

async def delete_news_category_by_ids(db: AsyncSession, ids: list[int]):
    """
    删除新闻分类

    Args:
        db (AsyncSession): 数据库连接
        ids (list[int]): id列表

    Returns:
        int: 删除的条数
    """
    count = await base_crud.delete_by_ids(db, NewsCategory, ids)
    return count
