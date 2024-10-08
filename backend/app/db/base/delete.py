from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Type
from sqlalchemy.orm import DeclarativeMeta

async def delete_by_id(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    id: int
) -> int:
    """
    单个删除指定模型的数据

    Args:
        db (AsyncSession): 数据库会话
        model (Type[DeclarativeMeta]): 数据库模型
        id (int): 模型 id

    Returns:
        int: 删除的行数，如果未找到记录，则返回 0
    """
    # 创建删除语句
    query = delete(model).where(model.id == id)

    # 执行删除操作
    result = await db.execute(query)
    
    # 提交事务
    await db.commit()

    # 返回删除的行数
    return result.rowcount


async def delete_by_ids(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    ids: List[int]
) -> int:
    """
    批量删除指定模型的数据

    Args:
        db (AsyncSession): 数据库会话
        model (Type[DeclarativeMeta]): 数据库模型
        ids (List[int]): 模型id列表

    Returns:
        int: 删除的行数，如果没有删除任何记录则返回 0
    """
    if not ids:
        return 0  # 如果 ids 列表为空，直接返回 0

    # 创建删除语句
    stmt = delete(model).where(model.id.in_(ids))

    # 执行删除操作
    result = await db.execute(stmt)
    
    # 提交事务
    await db.commit()

    # 返回删除的行数
    return result.rowcount
