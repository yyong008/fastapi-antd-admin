from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.utils.current_user import get_current_user
from app.dal.sys.user import get_user_by_id
# from app.dal.sys.role import get_role_by_id
from app.db.client import get_db
from app.models.system.role import Role

def get_user_permissions(ps):
    async def p(current_user=Depends(get_current_user), db=Depends(get_db)):
        id = current_user.id
        user = await get_user_by_id(db, id)
        roles = user.roles # 只能选选择一个角色（数组长度为 1）
        # role = await get_role_by_id(db, roles[0].id)
        query = select(Role).where(Role.id == roles[0].id).options(joinedload(Role.menus))
    
        # 执行查询
        result = await db.execute(query)
        role = result.scalar()  # 获取单个结果

        menus = role.menus
        role_permissions = [menu.permission for menu in menus if menu.permission]

        data = list(set(role_permissions))
        has_permission = role_checker(ps, data)
        return has_permission
    return p

def role_checker(ps, user_permissions) -> bool:
    if ps not in user_permissions:
        raise HTTPException(status_code=403, detail="没有权限")
    return True
