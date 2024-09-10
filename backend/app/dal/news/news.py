from sqlalchemy.orm import Session
from app.models.news import News


# =====================================GET===================================================
def get_count(db: Session):
    count = db.query(News).count()
    return count


def get_news_all(db: Session):
    sort_column = News.createdAt.desc()
    return db.query(News).order_by(sort_column).all()


def get_news_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    sort_column = News.createdAt.desc()
    return db.query(News).order_by(sort_column).offset(offset).limit(limit).all()
