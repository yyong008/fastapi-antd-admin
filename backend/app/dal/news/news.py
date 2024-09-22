from sqlalchemy.orm import Session
from app.models.news import News
from fastapi import HTTPException


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


def get_news_by_id(id, db):
    return db.query(News).filter(News.id == id).first()


def create_news(news, db: Session):
    new_news = News(**news)
    db.add(new_news)
    db.commit()
    db.refresh(new_news)
    return new_news


def update_news(id, news, current_user_id, db):
    count = db.query(News).filter(News.id == id).update(news)
    db.commit()
    return count


def delete_news_by_ids(ids, db):
    try:
        count = (
            db.query(News).filter(News.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
