from typing import List
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy.exc import SQLAlchemyError

import app.dal.sys.menu as m_dals
from ._format import build_menu_tree_raw, format_menu, format_menu_all_list
from app.models.system.menu import Menu

async def get_all_menu_service(db: AsyncSession):
    """
    获取所有菜单
    """
    try:
        menu_list = await m_dals.get_menu_all(db)
        return format_menu_all_list(menu_list)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def get_menu_tree_service(db: AsyncSession):
    """
    获取菜单树
    """
    try:
        menu_list = await m_dals.get_menu_all(db)
        format_menu_list = format_menu_all_list(menu_list)
        menu_tree = build_menu_tree_raw(format_menu_list, None)
        return menu_tree
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_menu_tree_no_permission_service(db):
    """
    获取没有权限的菜单树
    """
    try:
        ml = await m_dals.get_menu_all(db)
        menu_list = [m for m in ml if not m.permission]
        format_menu_list = format_menu_all_list(menu_list)
        menu_tree = build_menu_tree_raw(format_menu_list, None)
        return menu_tree
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def get_menu_by_id_service( db: AsyncSession, menu_id: int,):
    """
    根据id获取菜单
    """
    try:
        data = await m_dals.get_menu_by_id(db, menu_id)
        return format_menu(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def create_menu_service(db: AsyncSession, menu):
    """
    创建菜单
    """
    try:
        m = Menu(**menu)
        data = await m_dals.create_menu(db, m)
        return format_menu(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_menu_by_id_service(db: AsyncSession, menu_id: int, item):
    """
    更新菜单
    """
    try:
        data = await m_dals.update_menu_by_id(db, menu_id, item.model_dump())
        return format_menu(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_menu_by_ids_service(db: AsyncSession, ids: List[int]):
    """
    删除菜单
    """
    try:
        count = await m_dals.delete_menu_by_ids(db, ids)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
