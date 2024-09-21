def format_dept(item):
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
    item = {
        "id": role.id,
        "name": role.name,
        "value": role.value,
        "description": role.description,
        "status": role.status,
        "createdAt": role.createdAt,
        "updatedAt": role.updatedAt,
    }
    return item

def format_user(user):
    item = {
        "id": user.id,
        "name": user.name,
        "avatar": user.avatar,
        "email": user.email,
        "role": [role.name for role in user.roles],
        "department": {
            "id": None if not user.department else user.department.id,
            "name": None if not user.department else user.department.name,
        },
        "lang": user.lang,
        "phone": user.phone,
        "theme": user.theme,
        "status": user.status,
        "remark": user.remark,
        "nickname": user.nickname,
        "createdAt": user.createdAt,
        "updatedAt": user.updatedAt,
    }
    return item
