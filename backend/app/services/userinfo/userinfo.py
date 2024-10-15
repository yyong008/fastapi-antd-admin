from app.dal.sys.user import get_user_by_id
from app.dal.sys.menu import get_menu_all
from app.dal.sys.menu_role import get_menu_role_list_by_role_id
from . import _format
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

async def get_user_info(db: AsyncSession, user_id):
    """
    根据 user_id 获取用户信息

    Args:
      db (AsyncSession): 数据库连接
      user_id (int): 用户ID

    Returns:
      dict: 用户信息
    """
    userInfo = await get_user_by_id(db, user_id)
    if not userInfo.roles:
        raise HTTPException(403, "该用户没有角色")
    role_id = userInfo.roles[0].id
    # 根据 role id 获取 menu_role 数据
    menu_role_list = await get_menu_role_list_by_role_id(db, role_id)
    menu_ids = [menu_role.menu_id for menu_role in menu_role_list if menu_role.role_id == role_id]

    menu_list = await get_menu_all(db)
    menu_list = [menu for menu in menu_list if menu.id in menu_ids]

    user_info = {
        "id": userInfo.id,
        "name": userInfo.name,
    }
    if userInfo.department:
        user_info["department"] = {
            "id": userInfo.department.id,
            "name": userInfo.department.name,
        }

    menu = _format.get_sidebar_menu_by_menu_raw_no_type_three(menu_list)
    return {"userInfo": user_info, "menu": menu}
