from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.system.menu import Menu


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Menu).count()
    return count


def get_menu_all(db: Session):
    sort_column = Menu.order_no.asc()
    return db.query(Menu).order_by(sort_column).all()


def get_menu_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Menu.createdAt.desc()
    return db.query(Menu).order_by(sort_column).offset(offset).limit(limit).all()

def create_menu_category(meun, db: Session):
    db.add(meun)
    db.commit()
    db.refresh(meun)
    return meun

def update_menu_by_id(db: Session, menu_id: int, role: Menu):
    db.query(Menu).filter(Menu.id == menu_id).update(role)
    db.commit()
    db.refresh(role)
    return role

def delete_menu_by_ids(ids, db):
    try:
        count = (
            db.query(Menu).filter(Menu.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

