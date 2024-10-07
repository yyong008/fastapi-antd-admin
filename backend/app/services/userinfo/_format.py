def format_userInfo(user):
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
