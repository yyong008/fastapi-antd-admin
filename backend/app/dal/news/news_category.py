from sqlalchemy.orm import Session
from app.models.news import NewsCategory


# =====================================GET===================================================
def get_news_category_count(db: Session):
    count = db.query(NewsCategory).count()
    return count


def get_news_category_all(db: Session):
    sort_column = NewsCategory.createdAt.desc()
    return db.query(NewsCategory).order_by(sort_column).all()


def get_news_category_list(db: Session, page: int = 1, pageSize: int = 10):
    limit = pageSize
    offset = (page - 1) * pageSize
    # sort_column = NewsCategory.createdAt.desc()
    return (
        db.query(NewsCategory).offset(offset).limit(limit).all()
    )
