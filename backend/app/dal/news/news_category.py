from fastapi import HTTPException
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

def get_news_category_by_name(name: str, db: Session):
    return db.query(NewsCategory).filter(NewsCategory.name == name).first()

def get_news_category_by_id(id: int, db: Session):
    return db.query(NewsCategory).filter(NewsCategory.id == id).first()


def create_news_category_category(news_category, db: Session):
    db.add(news_category)
    db.commit()
    db.refresh(news_category)
    return news_category

def update_news_category_by_id(db: Session, news_category_id: int, news_category: NewsCategory):
    db.query(NewsCategory).filter(NewsCategory.id == news_category_id).update(news_category)
    db.commit()
    db.refresh(news_category)
    return news_category

def delete_news_category_by_ids(ids, db):
    try:
        count = (
            db.query(NewsCategory).filter(NewsCategory.id.in_(ids)).delete(synchronize_session=False)
        )
        db.commit()

        return count
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
