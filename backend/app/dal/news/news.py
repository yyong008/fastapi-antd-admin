from sqlalchemy import func
from app.models.news import News
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import app.db.base as base_crud


# =====================================GET===================================================
async def get_news_by_category_id(db: AsyncSession, category_id: int):
    """
    获取值制定 分类的新闻数量

    Args:
        db (AsyncSession): 数据库连接
        category_id (int): 分类id

    Returns:
        int: 新闻数量
    """
    stmt = select(func.count(News.id)).filter(News.news_id == category_id)
    result = await db.execute(stmt)
    count = result.scalar()
    return count


async def get_news_count_by_category_id(db: AsyncSession, category_id: int):
    """
    获取值制定 分类的新闻数量

    Args:
        db (AsyncSession): 数据库连接
        category_id (int): 分类id

    Returns:
        int: 新闻数量
    """
    if category_id:
        count = await get_news_by_category_id(db, category_id)
        return count

    count = await get_news_all_count(db)
    return count


async def get_news_all_count(db: AsyncSession):
    """
    获取所有新闻数量

    Args:
        db (AsyncSession): 数据库连接

    Returns:
        int: 新闻数量
    """
    count = await base_crud.get_count(db, News)
    return count


async def get_news_all(db: AsyncSession):
    """
    获取所有新闻

    Args:
        db (AsyncSession): 数据库连接

    Returns:
        list: 新闻列表
    """
    sort_column = News.created_at.desc()
    data = await base_crud.get_all(db, News, order_by=sort_column)
    return data


async def get_news_list(
    db: AsyncSession, page: int = 1, pageSize: int = 10, category_id: int = None
):
    """
    获取新闻列表

    Args:
        db (AsyncSession): 数据库连接
        page (int, optional): 页码. Defaults to 1.
        pageSize (int, optional): 每页数量. Defaults to 10.
        category_id (int, optional): 分类id. Defaults to None.

    Returns:
        list: 新闻列表
    """
    if category_id:
        data = await base_crud.get_list(
            db,
            News,
            order_by=None,
            filter=News.news_id == category_id,
            page=page,
            pageSize=pageSize,
        )
        return data
    data = await base_crud.get_all(db, News, order_by=None)
    return data


async def get_news_list_by_category_id(
    db: AsyncSession, category_id: int, page: int, pageSize: int
):
    """
    获取值制定 分类的新闻列表

    Args:
        db (AsyncSession): 数据库连接
        category_id (int): 分类id
        page (int): 页码
        pageSize (int): 每页数量

    Returns:
        list: 新闻列表
    """
    data = await base_crud.get_list(
        db,
        News,
        order_by=None,
        filter=News.news_id == category_id,
        page=page,
        pageSize=pageSize,
    )
    return data


async def get_news_by_id(db: AsyncSession, id: int):
    """
    获取值制定 id 的新闻

    Args:
        db (AsyncSession): 数据库连接
        id (int): 新闻id

    Returns:
        News: 新闻
    """
    data = await base_crud.get_by_id(db, News, id)
    return data


# =====================================CREATE===================================================
async def create_news(db: AsyncSession, news: dict):
    """
    创建新闻

    Args:
        db (AsyncSession): 数据库连接
        news (dict): 新闻数据

    Returns:
        News: 新闻
    """
    data = await base_crud.create(db, News, news)
    return data


# =====================================UPDATE===================================================
async def update_news(db: AsyncSession, id: int, news: dict, current_user_id: int):
    """
    更新新闻

    Args:
        db (AsyncSession): 数据库连接
        id (int): 新闻id
        news (dict): 新闻数据
        current_user_id (int): 当前用户id

    Returns:
        News: 新闻
    """
    data = await base_crud.update_by_id(db, News, id, news)
    return data


# =====================================DELETE===================================================
async def delete_news_by_ids(db: AsyncSession, ids: list[int]):
    """
    批量删除新闻

    Args:
        db (AsyncSession): 数据库连接
        ids (list[int]): 新闻id列表

    Returns:
        int: 删除数量
    """
    count = await base_crud.delete_by_ids(db, News, ids)
    return count
