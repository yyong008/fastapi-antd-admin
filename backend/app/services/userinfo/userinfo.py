from app.dal.sys.user import get_user_by_id
from app.dal.sys.menu import get_menu_all
from ._format import format_userInfo
from sqlalchemy.ext.asyncio import AsyncSession 

async def get_user_info(db: AsyncSession, user_id):
  userInfo = await get_user_by_id(db, user_id)
  menu_list = await get_menu_all(db)

  user_info = {
    "id": userInfo.id,
    "name": userInfo.name,
  }
  if userInfo.department:
    user_info["department"] = {
      "id": userInfo.department.id,
      "name": userInfo.department.name
    }

  menu = await get_sidebar_menu_by_menu_raw_no_type_three(menu_list)
  return {"userInfo": user_info, "menu": menu}

async def get_sidebar_menu_by_menu_raw_no_type_three(menu_raw):
  menu = [format_userInfo(m) for m in menu_raw]
  return [item for item in menu if item["type"] <= 2]
