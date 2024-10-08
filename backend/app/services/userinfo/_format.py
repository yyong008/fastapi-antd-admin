def format_userInfo(user):
    """
    格式化用户信息
    """
    return {
      "id": user.id,
      "name": user.name,
      "icon": user.icon,
      "path": user.path,
      "type": user.type,
      "description": user.description,
      "remark": user.remark,
      "path_file": user.path_file,
      "status": user.status,
      "isShow": user.isShow,
      "isCache": user.isCache,
      "permission": user.permission,
      "isLink": user.isLink,
      "order_no": user.order_no,
      "parent_menu_id": user.parent_menu_id,
    }

def get_sidebar_menu_by_menu_raw_no_type_three(menu_raw):
  """
  获取菜单栏数据，不包含type为3的数据
  """
  menu = [format_userInfo(m) for m in menu_raw]
  return [item for item in menu if item["type"] <= 2]
