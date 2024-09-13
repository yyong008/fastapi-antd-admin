from sqlalchemy.orm import Session
from app.models.system.role import Role


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Role).count()
    return count


def get_roles_all(db: Session):
    sort_column = Role.createdAt.desc()
    return db.query(Role).order_by(sort_column).all()


def get_role_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Role.createdAt.desc()
    return db.query(Role).order_by(sort_column).offset(offset).limit(limit).all()
