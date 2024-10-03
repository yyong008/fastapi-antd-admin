from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.system.dictionary import Dictionary


# =====================================GET===================================================
async def get_dictionary_count(db: Session):
    count = db.query(Dictionary).count()
    return count

async def get_dictionary_all(db: Session):
    sort_column = Dictionary.createdAt.desc()
    return db.query(Dictionary).order_by(sort_column).all()

async def get_dictionary_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Dictionary.createdAt.desc()
    return db.query(Dictionary).order_by(sort_column).offset(offset).limit(limit).all()

async def create_dict(dict, db: Session):
    db.add(dict)
    db.commit()
    db.refresh(dict)
    return dict

async def update_dict_by_id(db: Session, dict_id: int, dict):
    db.query(Dictionary).filter(Dictionary.id == dict_id).update({**dict}, synchronize_session=False)
    db.commit()
    dict = db.query(Dictionary).filter(Dictionary.id == dict_id).first()
    db.refresh(dict)
    return dict

async def delete_dict_by_ids(ids, db):
    try:
        count = db.query(Dictionary).filter(Dictionary.id.in_(ids)).delete(synchronize_session=False)
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

