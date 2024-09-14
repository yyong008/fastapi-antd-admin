from sqlalchemy.orm import Session
from app.models.system.dictionary import Dictionary


# =====================================GET===================================================
def get_dictionary_count(db: Session):
    count = db.query(Dictionary).count()
    return count


def get_dictionary_all(db: Session):
    sort_column = Dictionary.createdAt.desc()
    return db.query(Dictionary).order_by(sort_column).all()


def get_dictionary_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Dictionary.createdAt.desc()
    return db.query(Dictionary).order_by(sort_column).offset(offset).limit(limit).all()
