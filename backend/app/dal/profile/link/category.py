from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.profile.link import LinkCategory


# =====================================GET===================================================
def get_link_category_by_name(name: str, db: Session):
    return db.query(LinkCategory).filter(LinkCategory.name == name).first()


def get_link_category_list(db: Session, skip: int = 0, limit: int = 10):
    offset = (skip - 1) * limit
    limit = limit
    return db.query(LinkCategory).offset(offset).limit(limit).all()


def get_link_category_count(db: Session):
    count = db.query(LinkCategory).count()
    return count


def get_link_category_all(db: Session):
    sort_column = LinkCategory.createdAt.desc()
    return db.query(LinkCategory).order_by(sort_column).all()


def get_link_category_by_id(link_id, db: Session):
    return db.query(LinkCategory).filter_by(id=link_id).first()


def get_link_category_by_ids(ids, db: Session):
    return db.query(LinkCategory).filter(LinkCategory.id.in_(ids)).all()


def create_link_category(link_category, db: Session):
    db.add(link_category)
    db.commit()
    db.refresh(link_category)
    return link_category

def update_link_category_by_id(link_category_id: int, link_category: LinkCategory, db: Session):
    # db.query(LinkCategory).filter(LinkCategory.id == link_category_id).update(link_category)
    db.commit()
    db.refresh(link_category)
    return link_category

def delete_link_category_by_ids(ids, db):
    try:
        count = db.query(LinkCategory).filter(LinkCategory.id.in_(ids)).delete(synchronize_session=False)
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
