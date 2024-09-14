from sqlalchemy.orm import Session
from app.models.system.dictionary import DictionaryEntry


# =====================================GET===================================================
def get_dictionary_entry_count(id, db: Session):
    count = db.query(DictionaryEntry).filter(DictionaryEntry.dictionary_id == id).count()
    return count


def get_dictionary_entry_all(db: Session):
    sort_column = DictionaryEntry.createdAt.desc()
    return db.query(DictionaryEntry).order_by(sort_column).all()


def get_dictionary_entry_list(id, db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = DictionaryEntry.createdAt.desc()
    return (
        db.query(DictionaryEntry)
        .order_by(sort_column)
        .filter(DictionaryEntry.dictionary_id == id)
        .offset(offset)
        .limit(limit)
        .all()
    )
