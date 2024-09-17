from app.dal.sys.user import get_user_by_id
from app.dal.sys.menu import get_menu_all


def get_user_info(user_id, db):
  userInfo = get_user_by_id(user_id, db)
  menu_list = get_menu_all(db)


  user_info = {
    "id": userInfo.id,
    "name": userInfo.name,
  }
  if userInfo.department:
    user_info["department"] = {
      "id": userInfo.department.id,
      "name": userInfo.department.name
    }

  menu = get_sidebar_menu_by_menu_raw_no_type_three(menu_list)
  return {"userInfo": user_info, "menu": menu}

def get_sidebar_menu_by_menu_raw_no_type_three(menu_raw):
  menu = []
  for m in menu_raw:
    menu.append({
      "id": m.id,
      "name": m.name,
      "icon": m.icon,
      "path": m.path,
      "type": m.type,
      "description": m.description,
      "remark": m.remark,
      "path_file": m.path_file,
      "status": m.status,
      "isShow": m.isShow,
      "isCache": m.isCache,
      "permission": m.permission,
      "isLink": m.isLink,
      "order_no": m.order_no,
      "parent_menu_id": m.parent_menu_id,
    })
  return [item for item in menu if item["type"] <= 2]
