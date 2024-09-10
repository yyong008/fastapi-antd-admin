from sqlalchemy.orm import Session
from app.models.system.user import UserSignLog


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(UserSignLog).count()
    return count


def get_user_signlog_all(db: Session):
    sort_column = UserSignLog.createdAt.desc()
    return db.query(UserSignLog).order_by(sort_column).all()


def get_user_signlog_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = UserSignLog.createdAt.desc()
    return db.query(UserSignLog).order_by(sort_column).offset(offset).limit(limit).all()


# =====================================CREATE===================================================
def create_user_signlog(user_signlog, db: Session):
    sign_log = UserSignLog(user_signlog)
    db.add(sign_log)
    db.commit()
    db.refresh(sign_log)
    return sign_log
