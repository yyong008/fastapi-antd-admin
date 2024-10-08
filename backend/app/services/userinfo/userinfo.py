from app.dal.sys.user import get_user_by_id
from app.dal.sys.menu import get_menu_all
from . import _format
from sqlalchemy.ext.asyncio import AsyncSession


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
    menu_list = await get_menu_all(db)

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
