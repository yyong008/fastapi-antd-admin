from app.models.system.menu import role_menu_association
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def get_menu_role_list_by_role_id(db: AsyncSession, role_id: int):
    """根据 role_id 获取菜单权限列表"""
    query = select(role_menu_association).where(role_menu_association.c.role_id == role_id)
    result = await db.execute(query)
    data = result.fetchall()
    return data
