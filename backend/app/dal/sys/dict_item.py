from fastapi import HTTPException
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

def create_dict_item_category(dict_item, db: Session):
    db.add(dict_item)
    db.commit()
    db.refresh(dict_item)
    return dict_item

def update_dict_item_by_id(db: Session, dict_item_id: int, dict_item: DictionaryEntry):
    db.query(DictionaryEntry).filter(DictionaryEntry.id == dict_item_id).update(dict_item)
    db.commit()
    db.refresh(dict_item)
    return dict_item

def delete_dict_item_by_ids(ids, db):
    try:
        count = (
            db.query(DictionaryEntry).filter(DictionaryEntry.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

