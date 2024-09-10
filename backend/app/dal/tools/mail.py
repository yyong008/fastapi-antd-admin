from sqlalchemy.orm import Session
from app.models.tools.mail import Mail


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(Mail).count()
    return count


def get_mail_all(db: Session):
    sort_column = Mail.createdAt.desc()
    return db.query(Mail).order_by(sort_column).all()


def get_mail_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = Mail.createdAt.desc()
    return db.query(Mail).order_by(sort_column).offset(offset).limit(limit).all()
