from sqlalchemy.orm import Session
from app.models.docs.changelog import ChangeLog


# =====================================GET===================================================
def get_changelog_count(db: Session):
    count = db.query(ChangeLog).count()
    return count


def get_changelog_all(db: Session):
    sort_column = ChangeLog.createdAt.desc()
    return db.query(ChangeLog).order_by(sort_column).all()


def get_changelog_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    # sort_column = ChangeLog.createdAt.desc()
    return db.query(ChangeLog).offset(offset).limit(limit).all()
