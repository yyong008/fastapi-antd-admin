from fastapi import Depends, HTTPException

from app.utils.current_user import get_current_user
from app.dal.sys.user import get_user_by_id
from app.dal.sys.role import get_role_by_id
from app.db.client import get_db

def get_user_permissions(ps):
    def p(current_user=Depends(get_current_user), db=Depends(get_db)):
        id = current_user.id
        user = get_user_by_id(id, db)
        roles = user.roles
        role = get_role_by_id(roles[0].id, db)
        menus = role.menus
        role_permissions = []
        for menu in menus:
          if menu.permission:
            role_permissions.append(menu.permission)

        data = list(set(role_permissions))
        has_permission = role_checker(ps, data)
        return has_permission
    return p

def role_checker(ps, user_permissions) -> bool:
    if ps not in user_permissions:
        raise HTTPException(status_code=403, detail="没有权限")
    return True
