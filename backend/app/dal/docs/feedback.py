from sqlalchemy.orm import Session
from app.models.docs.feedback import FeedBack


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(FeedBack).count()
    return count


def get_feedback_all(db: Session):
    sort_column = FeedBack.createdAt.desc()
    return db.query(FeedBack).order_by(sort_column).all()


def get_feedback_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = FeedBack.createdAt.desc()
    return db.query(FeedBack).order_by(sort_column).offset(offset).limit(limit).all()
