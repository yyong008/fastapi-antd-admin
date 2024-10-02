from fastapi import HTTPException
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

async def create_storage(storage, db: Session):
    db.add(storage)
    db.commit()
    db.refresh(storage)
    return storage

def update_storage_by_id(db: Session, storage_id: int, storage: Storage):
    db.query(Storage).filter(Storage.id == storage_id).update(storage)
    db.commit()
    db.refresh(storage)
    return storage

def delete_storage_by_ids(ids, db):
    try:
        count = (
            db.query(Storage).filter(Storage.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
