from sqlalchemy.orm import Session
from app.models.tools.storage import Storage


# =====================================GET===================================================
def get_storage_count(db: Session):
    count = db.query(Storage).count()
    return count

def get_storage_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    return db.query(Storage).offset(offset).limit(limit).all()

def get_storage_by_id(db: Session, id):
    return db.query(Storage).filter_by(Storage.id == id).all()
