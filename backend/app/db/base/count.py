from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, Optional, Any
from sqlalchemy.orm import DeclarativeMeta

async def get_count(
    db: AsyncSession,
    model: Type[DeclarativeMeta],
    filter: Optional[Any] = None,
) -> int:
    """
    获取指定模型的数据库存储的数量

    Args:
        db (AsyncSession): 数据库会话
        model (DeclarativeMeta): 数据库模型
    Returns:
        int: 模型数量
    """
    
    # 获取模型的主键列，默认为第一个主键
    primary_key_column = model.__mapper__.primary_key[0]

    # 查询模型记录的数量
    query = select(func.count(primary_key_column))
    if filter:
        if isinstance(filter, list):
            query = query.where(*filter)
        else:
            query = query.where(filter)
    result = await db.execute(query)
    
    # 获取计数结果
    count = result.scalar()
    
    return count
