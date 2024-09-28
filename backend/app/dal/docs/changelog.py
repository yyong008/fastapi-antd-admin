from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.docs.changelog import ChangeLog


# =====================================GET===================================================
def get_changelog_count(db: Session):
    count = db.query(ChangeLog).count()
    return count


def get_changelog_all(db: Session):
    sort_column = ChangeLog.createdAt.desc()
    return db.query(ChangeLog).order_by(sort_column).all()

def get_changelog_by_id(id: int, db: Session):
    return db.query(ChangeLog).filter(ChangeLog.id == id).first()

def get_changelog_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    # sort_column = ChangeLog.createdAt.desc()
    return db.query(ChangeLog).offset(offset).limit(limit).all()

def create_changelog(changelog, db: Session):
    db.add(changelog)
    db.commit()
    db.refresh(changelog)
    return changelog

def update_changelog_by_id(db: Session, blog_id: int, changelog: ChangeLog):
    db.query(ChangeLog).filter(ChangeLog.id == blog_id).update(changelog)
    db.commit()
    db.refresh(changelog)
    return changelog

def delete_changelog_by_ids(ids, db):
    try:
        count = (
            db.query(ChangeLog).filter(ChangeLog.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
