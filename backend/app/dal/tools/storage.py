from sqlalchemy.orm import Session
from app.models.tools.storage import Storage


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Storage).count()
    return count


def get_storage_all(db: Session):
    sort_column = Storage.createdAt.desc()
    return db.query(Storage).order_by(sort_column).all()


def get_storage_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Storage.createdAt.desc()
    return db.query(Storage).order_by(sort_column).offset(offset).limit(limit).all()
