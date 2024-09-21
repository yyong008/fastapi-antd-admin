
from sqlalchemy.orm import Session

from app.dal.sys.menu import get_menu_all
from .format import format_menu, format_menu_tree

def format_menu_all_list(menu_raw):
  menu = []
  for m in menu_raw:
    menu.append(format_menu(m))
  return menu

def build_menu_tree_raw(menu_data, parent_id=None):
    result = []
    
    for menu in menu_data:
        if menu['parent_menu_id'] == parent_id:
            menu_item = format_menu_tree(menu)

            children = build_menu_tree_raw(menu_data, menu['id'])
            if children:
                menu_item['children'] = children

            result.append(menu_item)

    def sort_key(x):
        order_no = x.get('order_no', float('inf'))  # 处理 None 为一个很大的值
        return order_no if order_no is not None else float('inf')
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
