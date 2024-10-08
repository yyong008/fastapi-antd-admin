from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, Optional, Any, Dict
from sqlalchemy.orm import DeclarativeMeta

async def update_by_id(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    id: int, 
    new_data: Dict[str, Any]
) -> Optional[Any]:
    """
    更新指定模型的数据

    Args:
        db (AsyncSession): 数据库会话
        model (Type[DeclarativeMeta]): 数据库模型
        id (int): 模型 id
        new_data (Dict[str, Any]): 新的数据，键为字段名，值为更新内容

    Returns:
        Optional[Any]: 更新后的模型数据，如果未找到则返回 None
    """
    # 执行更新操作
    query = update(model).where(model.id == id).values(**new_data)
    result = await db.execute(query)

    if result.rowcount == 0:
        # 如果没有更新任何行，返回 None
        return None

    await db.commit()

    # 直接返回更新后的记录
    updated_record = await db.execute(select(model).where(model.id == id))
    return updated_record.scalar_one_or_none()
