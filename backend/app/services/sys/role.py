from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession 
import app.dal.sys.role as role_dals
from app.models.system.role import Role
from app.models.system.menu import Menu

from ._format import format_role

async def get_all_role_service(db: AsyncSession):
    """
    获取所有角色
    """
    try:
        count = await role_dals.get_count(db)
        roles_list_all = await role_dals.get_roles_all(db)

        user_list = [format_role(role) for role in roles_list_all]

        data = {"total": count, "list": user_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def get_role_by_id_service(db: AsyncSession, role_id: int):
    """
    根据id获取角色
    """
    try:
        data = await role_dals.get_role_by_id(db, role_id)
        return format_role(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

async def create_role_service(db: AsyncSession, role):
    """
    创建角色
    """
    try:
        menu_ids = role.menus if role.menus else []
        menus = []
        if menu_ids:
            menus = db.query(Menu).filter(Menu.id.in_(menu_ids)).all()
            menus = await role_dals.get_roles_all(db)
            if not menus or len(menus) != len(menu_ids):
                raise HTTPException(status_code=400, detail="有些菜单不存在")
        no_menu_role = role.model_dump()
        del no_menu_role['menus']
        new_role = Role(**no_menu_role, menus=menus)
        new_role = await role_dals.create_role(db, new_role)
        return format_role(new_role)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def update_role_by_id_service(db: AsyncSession, role_id: int, role):
    """
    更新角色
    """
    try:
        role_db = db.query(Role).options(joinedload(Role.menus)).filter(Role.id == role_id).first()
        if not role_db:
            raise HTTPException(status_code=400, detail="角色不存在")
        menus = []
        if role.menus:
            menus = db.query(Menu).filter(Menu.id.in_(role.menus)).all()
            if not menus or len(menus) != len(role.menus):
                raise HTTPException(status_code=400, detail="有些菜单不存在")
        role_db.menus = menus
        for key, value in role.model_dump().items():
            if value is not None and key != "menus":
                setattr(role_db, key, value)
        data = await role_dals.update_role_by_id(db, role_id, role_db)
        return format_role(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


async def delete_role_by_ids_service(db: AsyncSession, ids: list[int]):
    """
    根据ids删除角色
    """
    try:
        count = await role_dals.delete_role_by_ids(db, ids)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
