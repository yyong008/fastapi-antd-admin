
from sqlalchemy.orm import Session

from app.dal.sys.menu import get_menu_all


def get_all_menu_service(db: Session):
    menu_list = get_menu_all(db)
    return format_menu_all_list(menu_list)


def format_menu_all_list(menu_raw):
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
  return menu
