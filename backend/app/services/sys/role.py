from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.role import delete_role_by_ids, get_roles_all,get_count, create_role, update_role_by_id
from app.models.system.role import Role
from app.models.system.menu import Menu

from .format import format_role



def get_role_list(page, pageSize, db: Session):
    pass

def get_all_role_service(db: Session):
    try:
        count = get_count(db)
        roles_list_all = get_roles_all(db)

        user_list = []
        for role in roles_list_all:
            item = format_role(role)
            user_list.append(item)

        data = {"total": count, "list": user_list}
        return data
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def get_role_by_id_service(role_id: int, db):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")

def create_role_service(role, db: Session):
    try:
        menu_ids = role.menus if role.menus else []
        menus = []
        if menu_ids:
            menus = db.query(Menu).filter(Menu.id.in_(menu_ids)).all()
            if not menus or len(menus) != len(menu_ids):
                raise HTTPException(status_code=400, detail="有些菜单不存在")
        no_menu_role = role.model_dump()
        del no_menu_role['menus']
        new_role = Role(**no_menu_role, menus=menus)
        new_role = create_role(new_role, db)
        return format_role(new_role)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_role_by_id_service(role_id: int, role, db: Session):
    try:
        role_db = db.query(Role).options(joinedload(Role.menus)).filter(Role.id == role_id).first()
        if not role_db:
            raise HTTPException(status_code=400, detail="角色不存在")
        menus = []
        if role.menus:
            menus = db.query(Menu).filter(Menu.id.in_(role.menus)).all()
            if not menus or len(menus) != len(role.menus):
                raise HTTPException(status_code=400, detail="有些菜单不存在")
        role_db.menus = menus
        for key, value in role.model_dump().items():
            if value is not None and key != "menus":
                setattr(role_db, key, value)
        data = update_role_by_id(db, role_id, role_db)
        return format_role(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_role_by_ids_service(ids, db: Session):
    try:
        count = delete_role_by_ids(ids, db)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
