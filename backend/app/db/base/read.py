from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import  Type, Optional, Any, Dict
from sqlalchemy.orm import DeclarativeMeta

async def get_by_id(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    id: int
) -> Optional[Any]:
    """
    根据指定模型的 id 获取数据

    Args:
        db (AsyncSession): 数据库会话
        model (Type[DeclarativeMeta]): 数据库模型
        id (int): 模型 id

    Returns:
        Optional[Any]: 模型数据，如果未找到则返回 None
    """
    # 创建查询
    query = select(model).where(model.id == id)
    
    # 执行查询
    result = await db.execute(query)
    data = result.scalar()  # 获取单个结果

    return data  # 如果未找到，data 将为 None


async def get_by_name(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    name: str
) -> Optional[Any]:
    """
    根据指定模型的 name 获取数据

    Args:
        db (AsyncSession): 数据库会话
        model (Type[DeclarativeMeta]): 数据库模型
        name (str): 模型 name

    Returns:
        Optional[Any]: 模型数据，如果未找到则返回 None
    """
    # 创建查询
    query = select(model).where(model.name == name)
    
    # 执行查询
    result = await db.execute(query)
    data = result.scalar()  # 获取单个结果

    return data  # 如果未找到，data 将为 None

async def get_by_mail(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    mail: str
) -> Optional[Any]:
    """
    根据指定模型的 name 获取数据

    Args:
        db (AsyncSession): 数据库会话
        model (Type[DeclarativeMeta]): 数据库模型
        name (str): 模型 name

    Returns:
        Optional[Any]: 模型数据，如果未找到则返回 None
    """
    # 创建查询
    query = select(model).where(model.email == mail)
    
    # 执行查询
    result = await db.execute(query)
    data = result.scalar()  # 获取单个结果

    return data  # 如果未找到，data 将为 None

async def get_by_filters(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    filters: Dict[str, Any]
) -> Optional[Any]:
    """
    根据指定模型的多个过滤条件获取数据
    
    Args:
        db (AsyncSession): 数据库会话
        model (Type[DeclarativeMeta]): 数据库模型
        filters (Dict[str, Any]): 查询的过滤条件，以字段名为键，值为过滤值
    
    Returns:
        Optional[Any]: 模型数据，如果未找到则返回 None
    """
    # 动态构建 where 子句，支持多个过滤条件
    query = select(model).where(and_(*(getattr(model, key) == value for key, value in filters.items())))

        # 执行查询并获取数据
    result = await db.scalars(query)
    data = result.one_or_none()  # 返回单个结果或 None

    return data
