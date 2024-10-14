from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select
from typing import List, Type, Optional, Any
from sqlalchemy.orm import DeclarativeMeta

async def get_all(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    order_by: Optional[Any] = None, 
    options: Optional[Any] = None
) -> List[Any]:
    """
    获取指定模型的所有数据
    
    Args:
        db (AsyncSession): 数据库会话
        model (DeclarativeMeta): 数据库模型
        order_by (Optional[Any]): 排序字段，SQLAlchemy 排序表达式
    
    Returns:
        List[Any]: 模型数据列表
    """
    
    # 初始化查询
    query = select(model)
    # 应用排序
    if order_by is not None:
        query = query.order_by(order_by)
    if options is not None:
        if isinstance(options, (list, tuple)):
            query = query.options(*options)
            pass
        else:
            query = query.options(options)
    # 执行查询
    result = await db.execute(query)
    data = result.scalars().all()
    
    return data

async def get_list(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    order_by: Optional[Any] = None, 
    filter: Optional[Any] = None,
    options: Optional[Any] = None,
    page: int = 1, 
    pageSize: int = 10
) -> List[Any]:
    """
    获取指定模型的数据列表

    Args:
        db (AsyncSession): 数据库会话
        model (Base): 数据库模型
        order_by (str): 排序字段
        filter (str): 过滤条件
        page (int, optional): 页码. Defaults to 1.
        pageSize (int, optional): 每页数量. Defaults to 10.
    Returns:
        list: 模型数据列表
    """
    offset = (page - 1) * pageSize  # Calculate the offset

    query: Select = select(model)

    if order_by is not None:
       if isinstance(order_by, (list, tuple)): 
         query = query.order_by(*order_by)
       else:
         query = query.order_by(order_by)

    if options is not None:
        if isinstance(options, (list, tuple)):
            query = query.options(*options)
        else:
            query = query.options(options)

    if filter is not None:
        if isinstance(filter, (list, tuple)):
            query = query.filter(*filter)
        else:
            query = query.filter(filter)
    
    query = query.offset(offset).limit(pageSize)  # Apply limit and offset

    result = await db.execute(query)
    data = result.scalars().all()
    return data
