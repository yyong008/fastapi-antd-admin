
def format_login_list(loginlogs):
    """
    格式化登录日志列表
    """
    list = [format_loginlog(loginlog) for loginlog in loginlogs]
    return list


def build_dept_list_to_tree(items: list, parent_id: int = None) -> list:
    """
    部门列表->数型结构
    """
    return [
        {
            **item,
            "children": build_dept_list_to_tree(
                items, item["id"]
            ),  # Recursively build child tree
        }
        for item in items
        if item.get("parent_department_id") == parent_id
    ]


def format_menu_all_list(menu_raw):
    """
    格式化菜单列表
    """
    menu = []
    for m in menu_raw:
        menu.append(format_menu(m))
    return menu


def build_menu_tree_raw(menu_data, parent_id=None):
    """
    构建菜单树
    """
    result = []

    for menu in menu_data:
        if menu["parent_menu_id"] == parent_id:
            menu_item = format_menu_tree(menu)

            children = build_menu_tree_raw(menu_data, menu["id"])
            if children:
                menu_item["children"] = children

            result.append(menu_item)

    def sort_key(x):
        order_no = x.get("order_no", float("inf"))  # 处理 None 为一个很大的值
        return order_no if order_no is not None else float("inf")

    result.sort(key=sort_key)

    return result

def format_dept(item):
    """
    格式化部门
    """
    return {
        "id": item.id,
        "name": item.name,
        "parent_department_id": item.parent_department_id,
        "order_no": item.order_no,
        "description": item.description,
        "createdAt": item.createdAt,
        "updatedAt": item.updatedAt,
    }


def format_dict_item(dict_item):
    """
    格式化字典条目
    """
    item = {
        "id": dict_item.id,
        "key": dict_item.key,
        "value": dict_item.value,
        "orderNo": dict_item.order_no,
        "status": dict_item.status,
        "remark": dict_item.remark,
        "createdAt": dict_item.createdAt,
        "updatedAt": dict_item.updatedAt,
    }
    return item


def format_dict(dict):
    """

    格式化字典
    """
    item = {
        "id": dict.id,
        "name": dict.name,
        "code": dict.code,
        "status": dict.status,
        "remark": dict.remark,
        "description": dict.description,
        "createdAt": dict.createdAt,
        "updatedAt": dict.updatedAt,
    }
    return item


def format_loginlog(log):
    """
    格式化登录日志
    """
    item = {
        "id": log.id,
        "name": log.name,
        "ip": log.ip,
        "address": log.address,
        "login_at": log.login_at,
        "system": log.system,
        "browser": log.browser,
        "userId": log.userId,
    }
    return item


def format_menu(m):
    """
    格式化菜单
    """
    return {
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
        "created_at": m.createdAt,
        "updated_at": m.updatedAt,
    }


def format_menu_tree(menu):
    """
    格式化菜单
    """
    return {
        **menu,
        "name": menu["name"],
        "title": menu["name"],
        "hideInMenu": menu["isShow"],
        "file_path": menu["path_file"],
        "orderNo": menu["order_no"],
        "createdAt": menu["created_at"],
        "updatedAt": menu["updated_at"],
    }

def format_role(role):
    """
    格式化角色
    """
    item = {
        "id": role.id,
        "name": role.name,
        "value": role.value,
        "description": role.description,
        "status": role.status,
        "createdAt": role.createdAt,
        "updatedAt": role.updatedAt,
    }
    if hasattr(role, "menus"):
        item["menus"] = [{"id": menu.id, "name": menu.name} for menu in role.menus]
    return item

def format_user(user):
    """
    格式化用户
    """
    item = {
        "id": user.id,
        "name": user.name,
        "avatar": user.avatar,
        "email": user.email,
        "roles": [role.id for role in user.roles],
        "lang": user.lang,
        "phone": user.phone,
        "theme": user.theme,
        "status": user.status,
        "remark": user.remark,
        "nickname": user.nickname,
        "createdAt": user.createdAt,
        "updatedAt": user.updatedAt,
        "department_id": user.department_id,
    }

    if user.department_id:
        item["department"] = {}
        item["department"]["id"] = user.department.id
        item["department"]["name"] = user.department.name
    return item
