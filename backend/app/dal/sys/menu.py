from sqlalchemy.orm import Session
from app.models.system.menu import Menu


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Menu).count()
    return count


def get_menu_all(db: Session):
    sort_column = Menu.createdAt.desc()
    return db.query(Menu).order_by(sort_column).all()


def get_menu_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Menu.createdAt.desc()
    return db.query(Menu).order_by(sort_column).offset(offset).limit(limit).all()
