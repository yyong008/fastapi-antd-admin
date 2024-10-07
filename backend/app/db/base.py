from sqlalchemy import select, func, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select
from typing import List, Type, Optional, Any, Dict
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
        query = query.filter(filter)
    result = await db.execute(query)
    
    # 获取计数结果
    count = result.scalar()
    
    return count


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
        query = query.order_by(order_by)

    if options is not None:
        if isinstance(options, (list, tuple)):
            query = query.options(*options)
            pass
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
