from sqlalchemy.orm import Session
from app.models.news import News


# =====================================GET===================================================
def get_news_count(category_id, db: Session):
    if category_id:
        count = get_news_by_category_id(category_id, db)
        return count

    count = db.query(News).count()
    return count


def get_news_by_category_id(category_id, db: Session):
    return db.query(News).filter(News.news_id == category_id).count()


def get_news_all(db: Session):
    sort_column = News.createdAt.desc()
    return db.query(News).order_by(sort_column).all()


def get_news_list(
    db: Session, page: int = 1, pageSize: int = 10, category_id: int = None
):
    limit = pageSize
    offset = (page - 1) * pageSize

    if category_id:
        return get_news_list_by_category_id(category_id, limit, offset, db)
    return db.query(News).offset(offset).limit(limit).all()


def get_news_list_by_category_id(category_id: int, limit, offset, db: Session):
    return (
        db.query(News)
        .filter(News.news_id == category_id)
        .offset(offset)
        .limit(limit)
        .all()
    )
