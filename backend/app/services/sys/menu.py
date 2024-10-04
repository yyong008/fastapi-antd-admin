from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.dal.sys.menu import (
    delete_menu_by_ids,
    get_menu_all,
    create_menu,
    update_menu_by_id,
)
from .format import format_menu, format_menu_tree
from app.models.system.menu import Menu


def format_menu_all_list(menu_raw):
    menu = []
    for m in menu_raw:
        menu.append(format_menu(m))
    return menu


def build_menu_tree_raw(menu_data, parent_id=None):
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


def get_all_menu_service(db: Session):
    menu_list = get_menu_all(db)
    return format_menu_all_list(menu_list)


def get_menu_tree_service(db: Session):
    menu_list = get_menu_all(db)
    format_menu_list = format_menu_all_list(menu_list)
    menu_tree = build_menu_tree_raw(format_menu_list, None)
    return menu_tree


def get_menu_tree_no_permission_service(db):
    menu_list = [m for m in get_menu_all(db) if  not m.permission ]
    format_menu_list = format_menu_all_list(menu_list)
    menu_tree = build_menu_tree_raw(format_menu_list, None)
    return menu_tree


def get_menu_by_id_service(menu_id: int, db: Session):
    try:
        pass
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def create_menu_service(menu, db: Session):
    try:
        m = Menu(**menu)
        data = create_menu(m, db)
        return format_menu(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def update_menu_by_id_service(menu_id: int, item, db: Session):
    try:
        data = update_menu_by_id(db, menu_id, item.model_dump())
        return format_menu(data)
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")


def delete_menu_by_ids_service(ids: List[int], db: Session):
    try:
        count = delete_menu_by_ids(ids, db)
        return count
    except SQLAlchemyError as e:
        print(f"Oops, we encountered an error: {e}")
        raise HTTPException(status_code=400, detail=f"{e}")
