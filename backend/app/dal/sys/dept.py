from sqlalchemy.orm import Session
from app.models.system.department import Department


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Department).count()
    return count


def get_dictionary_all(db: Session):
    sort_column = Department.createdAt.desc()
    return db.query(Department).order_by(sort_column).all()


def get_dictionary_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Department.createdAt.desc()
    return db.query(Department).order_by(sort_column).offset(offset).limit(limit).all()
