
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, Any, Dict
from sqlalchemy.orm import DeclarativeMeta

async def create(
    db: AsyncSession, 
    model: Type[DeclarativeMeta], 
    obj_in: Dict[str, Any]
) -> DeclarativeMeta:
    """
    创建指定模型的数据

    Args:
        db (AsyncSession): 数据库会话
        model (DeclarativeMeta): 数据库模型
        obj_in (Dict[str, Any]): 要插入的模型数据，作为字典传入

    Returns:
        DeclarativeMeta: 创建的模型实例
    """
    # 创建数据库对象
    db_obj = model(**obj_in)
    db.add(db_obj)
    
    # 提交事务
    await db.commit()
    
    # 刷新对象以获取数据库生成的值（如自增ID）
    await db.refresh(db_obj)
    
    return db_obj
